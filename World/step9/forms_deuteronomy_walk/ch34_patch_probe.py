import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DISPLAY PATCH PROBED (sitting 22, LEAN; THE TAIL): for each candidate gloss of chapter 34's seats, the store's token families over the WHOLE store — by gloss where
# every token is the one word; the counts printed, never typed. Read-only. Sitting 21's form (ch33_patch_probe.py) over one chapter; the candidates the worst glosses
# read off the store's gloss list for the chapter (printed at the tail's open, ch34_gloss_list.out: 46 simple + 58 complex not yet by gloss; 16 already rewritten by
# gloss — "Daniel" -> "Dan", "the-seas" -> "the-sea", "in-gorge" -> "in-the-valley" and the blank "?" -> "" among them, the design's candidates already in force; ONE "?" seat
# at 34:6's "house" of Beth-peor, blanked by gloss — a by-reference row owed) — the lean form's patch, the rest OWED. RUN FROM THE REPO ROOT.
import re, sqlite3, subprocess, yaml
ROOT = _ROOT
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
CAND = ['and-complete', 'and-die', 'and-go-up', 'and-hear', 'and-make', 'and-say', 'and-see-him/its', 'and-the-miracle', 'and-weep', 'be-weak', 'eye-him/its', 'freshness-him/its', 'from-desert', 'in-desert', 'in-death-him/its', 'know-him/its', 'pass-over', 'see-you/your', 'send-him/its', 'sepulture-him/its', 'set-her/its', 'still/again', 'the-circle', 'the-earth', 'the-fear', 'the-hinder', 'the-palm-tree', 'the-this', 'to-eye', 'to-seed-you/your', 'servant-him/its', 'hand-him/its', 'over-him/its', 'to-him/its', 'and-twenty', 'and-not', 'in-earth', 'to-make', 'like-Moses', 'and-Moses', 'and-Manasseh', 'and-to-Jacob', 'and-to-all', 'to-all', 'the-day', 'the-great', 'the-hand', 'the-signs', 'the-south', 'the-Gilead', 'the-Pisgah', 'in-Israel', 'to-Abraham', 'to-Isaac', 'to-Pharaoh',
        'split', 'lamentation', 'weeping', 'arise', 'command', 'swear', 'know', 'make', 'mouth', 'full', 'servant', 'head', 'face', 'that', 'day', 'son', 'until', 'over', 'there', 'city', 'Bethpeor', 'years', 'thirty', 'hundred', 'man', 'all', 'earth', 'spirit', 'wisdom', 'prophet', 'this', 'not', 'which', 'to']
seen = set()
for g in CAND:
    if g in seen: continue
    seen.add(g)
    fam = store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1 ORDER BY 2 DESC, 1", (g,)).fetchall()
    print(f'  {g!r}: {len(fam)} families, {sum(n for _, n in fam)} tokens: {fam[:6]}')
CH = {}
for v, i, hp, g in store.execute("SELECT v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=34 ORDER BY v.id, w.idx"):
    CH.setdefault(v, []).append((i, hp.replace('/', ''), g))
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
d = yaml.safe_load(OV); BG = d['by_gloss']
print('candidates', len(seen), '| the chapter\'s glosses ALREADY rewritten by the earlier walks\' by-gloss overrides:', len(sorted({g for k in CH for _, _, g in CH[k] if g in BG})))
print('candidates already in by_gloss (excluded from GL):', sorted(g for g in seen if g in BG))
M21 = 'THE DEUTERONOMY WALK sitting 21 (2026-09-29, Deuteronomy 33, LEAN)'
i = OV.index(f'  # {M21}: the worst glosses of the blessing\'s seats'); j = OV.index('\n', i) + 1; rows = []
while True:
    m = re.match(r'  "[^"]+": "[^"]*"[^\n]*\n', OV[j:])
    if not m: break
    rows.append(m.group(0)); j += len(m.group(0))
print('sitting 21 by-gloss rows walked from its marker:', len(rows), '| its last row:', rows[-1].strip()[:60])
D33 = [l for l in OV.split('\n') if l.startswith('  "Deut.33.')]
print('by_gloss total', len(BG), '| by_ref total', len(d['by_ref']), '| the last Deut.33 by_ref line:', D33[-1][:50], '| Deut.34 by_ref rows present:', sum(1 for l in OV.split('\n') if re.match(r'  "Deut\.34\.', l)))
print('the "?" seats in the chapter:', [(v, i, hp) for v, L in CH.items() for i, hp, g in L if g == '?'])
print('the candidates\' seats in the chapter (gloss: verse/idx/token):')
for g in CAND:
    s = [f'{v}/{i}/{hp}' for v, L in CH.items() for i, hp, gg in L if gg == g]
    if s: print(f'  {g!r}: {s}')
