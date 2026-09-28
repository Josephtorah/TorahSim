import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DISPLAY PATCH PROBED (sitting 20, LEAN; THE TAIL): for each candidate gloss of chapter 32's seats, the store's token families over the WHOLE store — by gloss where
# every token is the one word; the counts printed, never typed. Read-only. Sitting 19's form (ch29_patch_probe.py) over one chapter; the candidates the worst glosses
# read off the store's gloss list for the chapter (printed at the tail's open, ch32_gloss_list.out: 153 simple + 226 complex not yet by gloss; 41 already rewritten by
# gloss) — the lean form's patch, the rest OWED. RUN FROM THE REPO ROOT.
import re, sqlite3, subprocess, yaml
ROOT = _ROOT
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
CAND = ['?', 'and-?', 'act-him/its', 'alive-you/your (pl)', 'and-Hosea', 'and-atone', 'and-be-complete', 'and-be-erect-you/your', 'and-burn', 'and-cessation', 'and-daughter-him/its', 'and-drought-me/my', 'and-exile', 'and-feed-on', 'and-from-apartment', 'and-from-cultivated-field', 'and-gather-for-any-purpose', 'and-hating-us/our', 'and-hurry', 'and-in-formless', 'and-lick', 'and-like-rain', 'and-loosen', 'and-poisonous-plant', 'and-pound', 'and-prepared', 'and-produce-her/its', 'and-requital', 'and-revenge', 'and-ruin', 'and-scorn', 'and-seize', 'and-shine', 'and-suck-him/its', 'and-surround-you/your (pl)', 'and-tell-you/your', 'and-there-suffix', 'and-to-hate-me/my', 'and-tooth', 'and-tortuous', 'and-trample-down', 'and-wilt', 'be--circumspect-and-hence', 'be--long', 'be--zealous-him/its', 'be--zealous-me/my', 'be--zealous-them/their', 'be-complete', 'be-dense', 'be-high-actively', 'be-safe', 'be-wise', 'bear-young-you/your', 'become-tipsy', 'break-apart', 'bunch-of-grapes', 'cliff-them/their', 'close-up', 'cover-up', 'curdled-milk', 'dash-asunder', 'drought-me/my', 'erect-you/your', 'flee-for-protection', 'from-blood--of-man', 'from-craggy-rock', 'from-flint', 'from-man-in-general', 'from-vexation', 'from-vine', 'go-away', 'grape-them/their', 'grow-fat', 'guard-him/its', 'guide-him/its', 'if-not', 'in-Hor', 'in-bone', 'in-break-through-him/its', 'in-depository-me/my', 'in-emptiness-them/their', 'in-something-disgusting', 'in-turn-aside', 'keep-in-memory', 'last-them/their', 'like-cliff-us/our', 'like-little-man-of-the-eye', 'like-shower', 'live-coal', 'memento-them/their', 'narrow-them/their', 'nestling-him/its', 'oppression-them/their', 'piercer-me/my', 'pinion-him/its', 'puff-them/their', 'revolve-him/its', 'ride-him/its', 'sacrifice-them/their', 'scrape--together', 'sea-monster', 'sell-them/their', 'separate-mentally', 'separate-mentally-him/its', 'shut-up-them/their', 'slaughter-an-animal', 'snatch-away', 'something-poured-out-them/their', 'something-received-me/my', 'something-said', 'something-said-me/my', 'something-saved-him/its', 'stain-them/their', 'store-away', 'storm-them/their', 'straight-course', 'the-cliff', 'to-doemon', 'to-narrow-him/its', 'to-narrow-me/my', 'to-something-seized', 'treat-a-person', 'trouble-him/its', 'trouble-me/my', 'trouble-them/their', 'turn-aside-from-the-road', 'twist-you/your', 'wine-them/their', 'with-him/its', 'people-him/its', 'people-you/your', 'in-mountain', 'foot-them/their', 'and-die', 'and-live', 'to-last-them/their', 'command-them/their', 'from-head', 'from-outside', 'from-near', 'know-them/their', 'old-age', 'pass-over', 'put/set', 'vine-them/their', 'the-song',
        'abundance', 'advice', 'asp', 'bitterness', 'boundary', 'cease', 'cliff', 'cover', 'crawl', 'creak', 'decay', 'deity', 'desolation', 'do', 'drip', 'droop', 'drought', 'elevation', 'entire', 'established', 'evil', 'exhausted', 'firmness', 'fright', 'give', 'grudge', 'heat', 'hovering', 'howl', 'inclose', 'inflame', 'intelligence', 'kidney', 'leadership', 'lightning', 'livestock', 'lowermost', 'magistrate', 'magnitude', 'mark', 'mend', 'miscarry', 'pasture', 'point', 'prepared', 'produce', 'quarrel', 'ram', 'rope', 'sanctify', 'selected', 'separate', 'shine', 'sigh', 'smoothness', 'strength', 'stupid', 'suck', 'violent', 'wake', 'waver', "Shᵉ'Owl", 'bad', 'forever', 'living', 'hide', 'send', 'return', 'arise']
seen = set()
for g in CAND:
    if g in seen: continue
    seen.add(g)
    fam = store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1 ORDER BY 2 DESC, 1", (g,)).fetchall()
    print(f'  {g!r}: {len(fam)} families, {sum(n for _, n in fam)} tokens: {fam[:6]}')
CH = {}
for v, i, hp, g in store.execute("SELECT v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=32 ORDER BY v.id, w.idx"):
    CH.setdefault(v, []).append((i, hp.replace('/', ''), g))
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
d = yaml.safe_load(OV); BG = d['by_gloss']
print('candidates', len(seen), '| the chapter\'s glosses ALREADY rewritten by the earlier walks\' by-gloss overrides:', len(sorted({g for k in CH for _, _, g in CH[k] if g in BG})))
print('candidates already in by_gloss (excluded from GL):', sorted(g for g in seen if g in BG))
print('by_gloss values of interest:', {g: BG.get(g) for g in ['?', 'and-?', 'the-cliff', 'cliff', 'strength', 'deity', 'and-shine', 'shine', 'set', 'bad', 'creak']})
M19 = 'THE DEUTERONOMY WALK sitting 19 (2026-09-27, Deuteronomy 29-31, LEAN)'
i = OV.index(f'  # {M19}: the worst glosses of the three chapters\' seats'); j = OV.index('\n', i) + 1; rows = []
while True:
    m = re.match(r'  "[^"]+": "[^"]*"[^\n]*\n', OV[j:])
    if not m: break
    rows.append(m.group(0)); j += len(m.group(0))
print('sitting 19 by-gloss rows walked from its marker:', len(rows), '| its last row:', rows[-1].strip()[:60])
D31 = [l for l in OV.split('\n') if l.startswith('  "Deut.31.')]
print('by_gloss total', len(BG), '| by_ref total', len(d['by_ref']), '| the last Deut.31 by_ref line:', D31[-1][:50], '| Deut.32 by_ref rows present:', sum(1 for l in OV.split('\n') if re.match(r'  "Deut\.32\.', l)))
print('the "?" seats (the pronoun I) in the chapter:', [(v, i, hp) for v, L in CH.items() for i, hp, g in L if g == '?'])
print('the prefixed blank seats ("and-?"):', [(v, i, hp) for v, L in CH.items() for i, hp, g in L if g == 'and-?'])
print('the candidates\' seats in the chapter (gloss: verse/idx/token):')
for g in CAND:
    s = [f'{v}/{i}/{hp}' for v, L in CH.items() for i, hp, gg in L if gg == g]
    if s: print(f'  {g!r}: {s}')
