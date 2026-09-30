import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 21 — CHAPTER 33, THE BLESSING (LEAN, 2026-09-29; THE TAIL): the store's glosses at the chapter's seats LISTED before the display patch —
# which are already rewritten by gloss (an earlier walk's by_gloss rows), which stand by reference, which are not yet touched (simple one-word glosses and complex
# hyphenated ones), the blank "?" seats; the anchors of the override file read (sitting 20's by-gloss block walked from its marker, the last Deut.32 by_ref row).
# Read-only; the counts printed, never typed. Sitting 20's gloss list's form (ch32_gloss_list.out). RUN FROM THE REPO ROOT.
import re, sqlite3, subprocess, yaml
ROOT = _ROOT
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
d = yaml.safe_load(OV); BG = d['by_gloss']; BR = d['by_ref']
D32 = [l for l in OV.split('\n') if l.startswith('  "Deut.32.')]
print('by_gloss total', len(BG), '| by_ref total', len(BR), '| Deut.33 by_ref rows present:', sum(1 for l in OV.split('\n') if l.startswith('  "Deut.33.')), '| Deut.32 by_ref rows:', len(D32))
print('the last Deut.32 by_ref line:', D32[-1])
M20 = 'THE DEUTERONOMY WALK sitting 20 (2026-09-28, Deuteronomy 32, LEAN)'
i = OV.index(f'  # {M20}: the worst glosses of the song\'s seats'); j = OV.index('\n', i) + 1; rows = []
while True:
    m = re.match(r'  "[^"]+": "[^"]*"[^\n]*\n', OV[j:])
    if not m: break
    rows.append(m.group(0)); j += len(m.group(0))
print('sitting 20 by-gloss rows walked from its marker:', len(rows), '| its last row:', rows[-1].strip()[:70])
CH = {}
for v, i_, hp, g in store.execute("SELECT v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=33 ORDER BY v.id, w.idx"):
    CH.setdefault(v, []).append((i_, hp.replace('/', ''), g))
NT = sum(len(L) for L in CH.values()); print('tokens', NT, 'verses', len(CH))
G = {}
for v, L in CH.items():
    for i_, hp, g in L: G.setdefault(g, []).append(f'{v}/{i_}/{hp}')
done = sorted(g for g in G if g in BG); todo = [g for g in G if g not in BG]
simple = sorted(g for g in todo if '-' not in g and '/' not in g and ' ' not in g); complex_ = sorted(g for g in todo if g not in simple)
print('glosses ALREADY rewritten by gloss:', len(done))
print('not yet by gloss: simple', len(simple), '| complex', len(complex_))
print('the "?" seats:', [(v, i_, hp) for v, L in CH.items() for i_, hp, g in L if g == '?'])
print('the "and-?" seats:', [(v, i_, hp) for v, L in CH.items() for i_, hp, g in L if g == 'and-?'])
print('the by-gloss REWRITES already in force at the chapter (gloss -> new):', {g: BG[g] for g in done})
print('---- COMPLEX (gloss: seats) ----')
for g in complex_: print(f'  {g!r}: {G[g]}')
print('---- SIMPLE (gloss: seats) ----')
for g in simple: print(f'  {g!r}: {G[g]}')
