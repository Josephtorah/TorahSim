import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# DEUTERONOMY CHAPTER 4, THE READING (THE DEUTERONOMY WALK sitting 2, 2026-09-16; the owner: "Go" after the rereads) — THE FIRST MEASUREMENT
# PASS, nothing typed: the shelf BY POSITION (the Sifrei on Deuteronomy's heads around chapter 4 — 30 on 3:29, 31 on 6:4 by sitting 1's
# measurement; whether any head falls in chapter 4), the WHOLE export scanned in BOTH files for rows citing chapter 4 (the export's forms:
# the Hebrew "(דברים ד n)" — "Deuteronomy 4:n" in Hebrew letters — and the English "(Dt.4:n)" with no space; the "ibid" candidates printed
# with their context), the Onkelos dump per verse (the Hebrew, the morphology, the store's glosses, the English, the Aramaic), THE PARSER on
# every verse, the case tokens, the frames and the register, the prior reads, the drafts' spans against the verse table, the store's token
# counts. Sitting 1's three scripts (deu_dump0 / deu_parser0 / deu_measure0) folded into one for one chapter.
import json, re, html, os, sqlite3, subprocess, sys, io, contextlib, glob, unicodedata
from collections import Counter
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f'{ROOT}/World/step9')
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
CH = 4
print('==== A. THE SHELF BY POSITION — the Sifrei on Deuteronomy around chapter', CH)
he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/he.json', encoding='utf-8'))['text']
en = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/en.json', encoding='utf-8'))['text']
print('  piskaot', len(he), len(en), 'rows', sum(len(s) for s in he), sum(len(s) for s in en), '| row-count mismatches:', [(p, len(he[p-1]), len(en[p-1])) for p in range(1, len(he)+1) if len(he[p-1]) != len(en[p-1])])
HEB = {'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90, 'ק': 100}
def gem(s): return sum(HEB.get(ch, 0) for ch in s)
heads = {}
for p in range(1, len(he) + 1):
    m = re.match(r'\(דברים ([א-ת]+) ([א-ת]+)(?:-[א-ת]+)?\)', clean(he[p-1][0]) if he[p-1] else '')
    heads[p] = (gem(m.group(1)), gem(m.group(2))) if m else None
print('  heads 24-36 (HE first citation | EN first quote | rows):')
for p in range(24, 37):
    e = clean(en[p-1][0]) if en[p-1] else ''; eq = re.search(r'“([^”]{0,70})', e)
    print(f'   {p:3d} head {heads[p]} | HE rows {len(he[p-1]):2d} EN rows {len(en[p-1]):2d} | EN first quote {eq.group(1)[:60] if eq else e[:60]!r}')
print('  heads whose chapter is', CH, ':', [(p, h) for p, h in heads.items() if h and h[0] == CH])
print('  heads by chapter (the count of piskaot heading in each chapter 1-8):', Counter(h[0] for h in heads.values() if h).most_common(8))
def he_cites(t): return [(b, gem(c), gem(v)) for b, c, v in re.findall(r'\(([א-ת]+(?: [א-ת])?) ([א-ת]{1,3}) ([א-ת]{1,3})\)', t)]
outside_he = [(p, r+1, c[2]) for p in range(1, len(he)+1) for r, row in enumerate(he[p-1]) for c in he_cites(clean(row)) if c[0] == 'דברים' and c[1] == CH]
print('  HE rows citing Deut', CH, ':', len(outside_he), outside_he)
en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(4):(\d+)')
outside_en = [(p, r+1, int(m.group(2))) for p in range(1, len(en)+1) for r, row in enumerate(en[p-1]) for m in en_forms.finditer(clean(row))]
print('  EN rows citing Deut', CH, ':', len(outside_en), outside_en)
ibid = [(p, r+1, m.group(0), clean(row)[max(0, m.start()-120):m.start()]) for p in range(1, len(en)+1) for r, row in enumerate(en[p-1]) for m in re.finditer(r'\((?:Ibid|ibid)\.? ?4:(\d+)\)', clean(row))]
print('  EN "ibid 4:n" candidates:', len(ibid)); [print('    ', p, r, f, '<<', ctx[-100:].replace('\n', ' ')) for p, r, f, ctx in ibid[:40]]
allrows = sorted(set((p, r) for p, r, _ in outside_he) | set((p, r) for p, r, _ in outside_en))
print('  the union of rows (both files):', len(allrows), allrows)
with open(f'{SP}/ch4_sifrei_outside.txt', 'w', encoding='utf-8') as f:
    for p, r in allrows:
        f.write(f'\n## Sifrei {p}:{r} (head {heads[p]}) HE\n{clean(he[p-1][r-1])}\n\n## Sifrei {p}:{r} EN\n{clean(en[p-1][r-1]) if r <= len(en[p-1]) else "(no EN row)"}\n')
print('  outside rows file bytes', os.path.getsize(f'{SP}/ch4_sifrei_outside.txt'))
print('==== B. ONKELOS chapter', CH, 'and the DB')
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Deuteronomy/en.json', encoding='utf-8'))['text']
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Deuteronomy/he.json', encoding='utf-8'))['text']
print('  VC Deut 1-6:', {c: VC[c] for c in range(1, 7)}, '| Onkelos export chapter', CH, 'verses EN', len(onk[CH-1]), 'HE', len(onk_he[CH-1]))
rows = db.execute("SELECT v.chapter, v.verse, w.he, w.morph, w.lemma FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=? ORDER BY v.id, w.idx", (CH,)).fetchall()
by = {}
for c, v, h, m, lem in rows: by.setdefault((c, v), []).append((plain(h), m, h, lem))
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, i, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=? ORDER BY v.id, w.idx", (CH,)):
    SG.setdefault((c, v), []).append((i, hp.replace('/', ''), g))
print('  verses whose store token count differs from the DB:', [(c, v, len(SG[(c, v)]), len(by[(c, v)])) for (c, v) in by if len(SG.get((c, v), [])) != len(by[(c, v)])])
print('  token count chapter', CH, ':', sum(len(by[(CH, v)]) for v in range(1, VC[CH] + 1)))
with open(f'{SP}/ch4_onkelos.txt', 'w', encoding='utf-8') as f:
    for v in range(1, VC[CH] + 1):
        f.write(f'\n== Deut {CH}:{v}\n  HE  {" ".join(x for x, _, _, _ in by[(CH, v)])}\n  MOR {" ".join(f"{x}:{m}" for x, m, _, _ in by[(CH, v)])}\n  LEM {" ".join(f"{x}:{(l or chr(63)).split(chr(47))[-1].strip()}" for x, _, _, l in by[(CH, v)])}\n  GL  {" | ".join(f"{hp}={g}" for _, hp, g in SG.get((CH, v), []))}\n  ONK {clean(onk[CH-1][v-1])}\n  ARM {plain(clean(onk_he[CH-1][v-1]))}\n')
print('  onkelos dump bytes', os.path.getsize(f'{SP}/ch4_onkelos.txt'))
print('==== C. THE PARSER on every verse of chapter', CH)
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
for v in range(1, VC[CH] + 1):
    vw = CS.verse_words('Deut', CH, v)
    marked = [t for t in vw if t[-1] in '#~^%@|*']
    n, o = CS.ink_numbers(vw), CS.ink_ordinals(vw)
    if n or o or marked: print(f'  {CH}:{v:<3} N {n!s:<24} O {o!s:<14} marked {marked}')
print('  number-word tokens present per verse (the bare check against the parser — any verse carrying a numeral consonant form):')
NUMW = ('אחד', 'אחת', 'שנים', 'שני', 'שתי', 'שלש', 'שלשה', 'שלשת', 'ארבע', 'ארבעה', 'ארבעים', 'חמש', 'שש', 'שבע', 'עשר', 'עשרה', 'עשרת', 'מאה', 'אלף', 'אלפים', 'ראשון', 'שני', 'שלישי', 'רבעים', 'שלשים')
print('  ', {f'{CH}:{v}': [x for x, _, _, _ in by[(CH, v)] if x in NUMW or x[1:] in NUMW] for v in range(1, VC[CH] + 1) if any(x in NUMW or x[1:] in NUMW for x, _, _, _ in by[(CH, v)])})
for v in (13, 41, 47, 46, 3, 10, 32, 34, 45, 44):
    print(f'  {CH}:{v} tokens:', CS.verse_words('Deut', CH, v))
print('==== D. CASE TOKENS, FRAMES, REGISTER, NAMES')
print('  case tokens (כי "when/for" / אם "if" / ואם / או "or" / פן "lest"):', {f'{CH}:{v}': [x for x, m, _, _ in by[(CH, v)] if x in ('כי', 'אם', 'ואם', 'או', 'פן')] for v in range(1, VC[CH] + 1) if any(x in ('כי', 'אם', 'ואם', 'או', 'פן') for x, m, _, _ in by[(CH, v)])})
print('  divine frames (ויאמר/וידבר + יהוה):', [f'{CH}:{v}' for v in range(1, VC[CH] + 1) for i, (x, _, _, _) in enumerate(by[(CH, v)][:-1]) if x in ('ויאמר', 'וידבר') and by[(CH, v)][i + 1][0] == 'יהוה'])
print('  לאמר "saying" seats:', [f'{CH}:{v}' for v in range(1, VC[CH] + 1) if any(x == 'לאמר' for x, _, _, _ in by[(CH, v)])])
print('  narrative-form verbs (V.w) per verse:', {v: [x for x, m, _, _ in by[(CH, v)] if m and re.search(r'V.w', m)] for v in range(1, VC[CH] + 1) if any(m and re.search(r'V.w', m) for _, m, _, _ in by[(CH, v)])})
print('  first-person verb forms (morph ...1cs / 1cp) per verse:', {v: [(x, m) for x, m, _, _ in by[(CH, v)] if m and re.search(r'1c[sp]', m) and m.startswith('HV')] for v in range(1, VC[CH] + 1) if any(m and re.search(r'1c[sp]', m) and m.startswith('HV') for _, m, _, _ in by[(CH, v)])})
print('  imperatives (Vq.v / Vp.v / Vh.v — the register of command) per verse:', {v: [(x, m) for x, m, _, _ in by[(CH, v)] if m and re.search(r'^HV..v', m)] for v in range(1, VC[CH] + 1) if any(m and re.search(r'^HV..v', m) for _, m, _, _ in by[(CH, v)])})
print('  name tokens (Np):', {v: [x for x, m, _, _ in by[(CH, v)] if m and 'Np' in m] for v in range(1, VC[CH] + 1) if any(m and 'Np' in m for _, m, _, _ in by[(CH, v)])})
print('  second-person plural vs singular — the verse\'s "you" number (2mp / 2ms tokens counted per verse):', {v: (sum(1 for _, m, _, _ in by[(CH, v)] if m and '2mp' in m), sum(1 for _, m, _, _ in by[(CH, v)] if m and '2ms' in m)) for v in range(1, VC[CH] + 1)})
print('==== E. THE REGISTER GATE on Deut', CH)
RD = open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8').read()
print('  dispositions naming Deut 4:', re.findall(r'^([^\n]*Deut 4:[^\n]*)$', RD, re.M)[:20])
RI = open(f'{ROOT}/World/step9/REGISTER_INDEX.md', encoding='utf-8').read()
print('  REGISTER_INDEX lines on Deut 4 (and the blocks whose edge names chapter 4):'); [print('   ', l[:220]) for l in RI.split('\n') if re.search(r'Deut 4:', l)]
print('==== F. THE PRIOR READS')
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}')}
print('  ledgers with an Onkelos Deut 4 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 4:', t, re.M)))
PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t)})
print('  prior Sifrei Devarim rows anywhere (strict form), those among the outside rows:', [(f, p, r) for f, p, r in PRIOR if (p, r) in allrows], '| all prior rows count', len(PRIOR))
NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 4:\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 4:\d+(?:-\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 4:\d+', t))
print('  ledgers NAMING a verse of Deut 4:', len(NAMING)); [print('   ', n) for n in NAMING]
print('==== G. THE DRAFTS')
for uid in ('deu_04_obey_horeb', 'deu_04_refuge_east', 'deu_05_decalogue'):
    t = open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
    st = sorted({(int(a), int(b)) for a, b in re.findall(r'id: STEP_Dt_(\d+)_(\d+)', t)})
    refs = re.search(r'refs: "([^"]+)"', t).group(1)
    print(f'  {uid}: refs {refs}; steps {st[0]}..{st[-1]} n={len(st)}; draft {"status: draft" in t}; operators {"operators:" in t}; depends_on {re.findall(r"depends_on:\n((?:    - \"[^\"]+\"\n)+)", t)[:1]}; scenarios {t.count(chr(10) + "  - id: S")}; has binary_trees {chr(10) + "binary_trees:" in t}; step E {"- step: E" in t}')
print('  VC Deut 4:', VC[CH], '| the two drafts cover', 40 + 9, 'of', VC[CH])
print('  the units\' claim prefixes present anywhere?', {p: sum(1 for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/*_claims.json') + glob.glob(f'{ROOT}/logic/units/*.yaml') if f'{p}-' in open(f, encoding='utf-8').read()) for p in ('DV04A', 'DV04B', 'DV03B')})
print('  existing manifests deu_04*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_04*')), '| ledgers deu_*:', sorted(f for f in LED if f.startswith('deu_')))
print('  unit count and standing (CORPUS_TRUTH literals):', re.findall(r'^(?:N_UNITS|UNITS_FROZEN|STANDING|N_STANDING|WORLD_HASH)[^\n]*', open(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py', encoding='utf-8').read(), re.M)[:6])
print('==== H. THE STORE\'S GLOSSES on chapter', CH)
print('  gloss Counter (the 50 commonest):', Counter(g for k in SG for _, _, g in SG[k]).most_common(50))
with open(f'{SP}/ch4_store_glosses.txt', 'w', encoding='utf-8') as f:
    for (c, v) in sorted(SG): f.write(f'{c}:{v}: ' + str([(i, t, g) for i, t, g in SG[(c, v)]]) + '\n')
print('  gloss file bytes', os.path.getsize(f'{SP}/ch4_store_glosses.txt'))
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
print('  overrides already for Deut.4:', re.findall(r'"Deut\.4\.[^"]+": "[^"]+"', OV)[:20], '| by_ref last Deut line:', [l for l in OV.split('\n') if l.startswith('  "Deut.3.')][-1:])
