import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# DEUTERONOMY 1-3, THE READING: the register gate's lines on the chapters, the prior reads, the shelf's other works on Deuteronomy, the six
# drafts' step ids against the verse table, the store's glosses per token (to a file), and THE ONKELOS DUMP per verse (to a file). Nothing typed.
import json, re, html, os, sqlite3, subprocess, glob, unicodedata
from collections import Counter
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
print('==== THE REGISTER GATE on Deut 1-3')
RD = open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8').read()
print('  dispositions naming Deut 1-3:', re.findall(r'^([^\n]*Deut [123]:[^\n]*)$', RD, re.M)[:20])
RI = open(f'{ROOT}/World/step9/REGISTER_INDEX.md', encoding='utf-8').read()
print('  REGISTER_INDEX lines on Deut 1-3:'); [print('   ', l[:180]) for l in RI.split('\n') if re.search(r'Deut [123]:', l)]
print('==== THE PRIOR READS')
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}')}
print('  ledgers with an Onkelos Deut row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut', t, re.M)))
print('  ledgers with a Sifrei Devarim row:', sorted((f, len(re.findall(r'Sifrei Devarim', t))) for f, t in LED.items() if 'Sifrei Devarim' in t))
NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? [123]:\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? [123]:\d+(?:-\d+)?', t)))[:12]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? [123]:\d+', t))
print('  ledgers NAMING a verse of Deut 1-3:', len(NAMING)); [print('   ', n) for n in NAMING]
print('==== THE SHELF\'S WORKS ON DEUTERONOMY')
print('  ', sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Deuteronomy|Devarim', d)))
print('==== THE DRAFTS')
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
for uid in ('deu_01_frame_officers', 'deu_01_spies_refuse', 'deu_02_bypass_nations', 'deu_02_sihon', 'deu_03_og_gilead', 'deu_03_moses_barred'):
    t = open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
    st = sorted({(int(a), int(b)) for a, b in re.findall(r'id: STEP_Dt_(\d+)_(\d+)', t)})
    refs = re.search(r'refs: "([^"]+)"', t).group(1)
    print(f'  {uid}: refs {refs}; steps {st[0]}..{st[-1]} n={len(st)}; draft {"status: draft" in t}; operators {"operators:" in t}; depends_on {re.findall(r"depends_on:\n((?:    - \"[^\"]+\"\n)+)", t)[:1]}; scenarios {t.count(chr(10) + "  - id: S")}')
print('  VC Deut 1-3:', {c: VC[c] for c in (1, 2, 3)})
print('  the units\' claim prefixes present anywhere?', {p: sum(1 for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/*_claims.json') + glob.glob(f'{ROOT}/logic/units/*.yaml') if f'{p}-' in open(f, encoding='utf-8').read()) for p in ('DV01A', 'DV01B', 'DV02A', 'DV02B', 'DV03A', 'DV03B', 'DT01A')})
print('  existing manifests for deu_*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_*')))
print('  existing ledgers deu_*:', sorted(f for f in LED if f.startswith('deu_')))
print('==== THE STORE (the snapshot) on Deut 1-3: token counts per verse vs the DB; the glosses to a file')
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
rows = db.execute("SELECT v.chapter, v.verse, w.he, w.morph, w.lemma FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (1,2,3) ORDER BY v.id, w.idx").fetchall()
by = {}
for c, v, he, m, lem in rows: by.setdefault((c, v), []).append((plain(he), m, he, lem))
SG = {}
for c, v, i, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (1,2,3) ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((i, hp.replace('/', ''), g))
print('  verses whose store token count differs from the DB:', [(c, v, len(SG[(c, v)]), len(by[(c, v)])) for (c, v) in by if len(SG.get((c, v), [])) != len(by[(c, v)])])
print('  gloss Counter over the three chapters (the 40 commonest):', Counter(g for k in SG for _, _, g in SG[k]).most_common(40))
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Deuteronomy/en.json', encoding='utf-8'))['text']
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Deuteronomy/he.json', encoding='utf-8'))['text']
def accents(w): return [unicodedata.name(c).replace('HEBREW ACCENT ', '') for c in w if 0x0591 <= ord(c) <= 0x05AE]
with open(f'{SP}/deu_onkelos_1_3.txt', 'w', encoding='utf-8') as f:
    for c in (1, 2, 3):
        for v in range(1, VC[c] + 1):
            he = ' '.join(x for x, _, _, _ in by[(c, v)])
            morph = ' '.join(f'{x}:{m}' for x, m, _, _ in by[(c, v)])
            gl = ' | '.join(f'{hp}={g}' for _, hp, g in SG.get((c, v), []))
            f.write(f'\n== Deut {c}:{v}\n  HE  {he}\n  MOR {morph}\n  GL  {gl}\n  ONK {clean(onk[c - 1][v - 1])}\n  ARM {plain(clean(onk_he[c - 1][v - 1]))}\n')
print('  onkelos dump bytes', os.path.getsize(f'{SP}/deu_onkelos_1_3.txt'))
with open(f'{SP}/deu_store_glosses_1_3.txt', 'w', encoding='utf-8') as f:
    for (c, v) in sorted(SG): f.write(f'{c}:{v}: ' + str([(i, t, g) for i, t, g in SG[(c, v)]]) + '\n')
print('  gloss file bytes', os.path.getsize(f'{SP}/deu_store_glosses_1_3.txt'))
