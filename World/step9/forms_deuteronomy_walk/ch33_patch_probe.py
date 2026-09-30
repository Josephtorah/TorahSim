import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DISPLAY PATCH PROBED (sitting 21, LEAN; THE TAIL): for each candidate gloss of chapter 33's seats, the store's token families over the WHOLE store — by gloss where
# every token is the one word; the counts printed, never typed. Read-only. Sitting 20's form (ch32_patch_probe.py) over one chapter; the candidates the worst glosses
# read off the store's gloss list for the chapter (printed at the tail's open, ch33_gloss_list.out: 103 simple + 142 complex not yet by gloss; 18 already rewritten by
# gloss — "Daniel" -> "Dan" and "meaning-accession" -> "also" among them, the design's candidates already in force; NO "?" seat in the chapter) — the lean form's patch,
# the rest OWED. RUN FROM THE REPO ROOT.
import re, sqlite3, subprocess, yaml
ROOT = _ROOT
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
CAND = ['adult-him/its', 'aid-you/your', 'altar-you/your', 'and-Urim-you/your', 'and-act', 'and-aid', 'and-arrive', 'and-be', 'and-be-untrue', 'and-between', 'and-complete', 'and-conceal', 'and-copper', 'and-covenant-you/your', 'and-delight', 'and-dip', 'and-do-not', 'and-drive-out-from-a-possession', 'and-from-deep', 'and-from-distinguished-thing', 'and-from-head', 'and-from-under', 'and-full', 'and-fulness-her/its', 'and-hate-him/its', 'and-horn', 'and-in-arrogance-him/its', 'and-irradiate', 'and-like-day-you/your', 'and-must', 'and-pluck-off', 'and-precept-you/your', 'and-reside', 'and-south', 'and-to-Asher', 'and-to-Daniel', 'and-to-Gad', 'and-to-Joseph', 'and-to-Levi', 'and-to-Naphtali', 'and-to-Zebulun', 'and-to-crown-of-the-head', 'and-to-mother-him/its', 'arise-him/its', 'arise-suffix', 'arrogance-you/your', 'be-open', 'be-pleased-with', 'bolt-you/your', 'brighten-up', 'butt-with-the-horns', 'come/bring', 'come/bring-him/its', 'come/bring-suffix', 'crown-of-the-head', 'dash-asunder', 'death-him/its', 'draw-together-the-feet', 'elevation-them/their', 'fire-law', 'flow-as-water', 'foot-him/its', 'force-him/its', 'from-abundance', 'from-distinguished-thing', 'from-narrow-him/its', 'from-right-hand-him/its', 'from-son', 'from-word-you/your', 'hand-him/its', 'happiness-you/your', 'heavens-him/its', 'hide-by-covering', 'horn-him/its', 'in-aid-you/your', 'in-bring-forth-you/your', 'in-gather-for-any-purpose', 'in-nose-you/your', 'in-tent-you/your', 'judgment-you/your', 'keep/guard', 'kind-you/your', 'lift/carry', 'like-roar', 'like-strength', 'many/great', 'over-him/its', 'perfections-you/your', 'possess/inherit-suffix', 'put/set', 'quiet-you/your', 'royal-edict', 'sacred-him/its', 'see-him/its', 'shoulder-him/its', 'slaughter-an-animal', 'something-said-you/your', 'son-him/its', 'test-him/its', 'the-benediction', 'the-say', 'there-is-not', 'to-Benjamin', 'to-Judah', 'to-face', 'to-father-him/its', 'to-foot-you/your', 'to-head', 'to-man', 'to-place-of-refuge', 'to-them/their', 'toss-him/its', 'voice/sound', 'wild-bull',
        'abode', 'abundance', 'arm', 'assemblage', 'benediction', 'bramble', 'broaden', 'call', 'cessation', 'cover', 'crouch', 'cub', 'delight', 'droop', 'drought', 'hack', 'hide', 'hillock', 'increase', 'lunation', 'magnificence', 'perfume', 'possession', 'powder', 'precept', 'produce', 'resources', 'right', 'satiated', 'scion', 'separate', 'shine', 'smoothness', 'strew', 'suck', 'waist', 'reside', 'seas', 'front', 'head', 'make', 'live', 'die', 'ride', 'say', 'holiness', 'guard', 'know', 'thousand', 'mountain', 'eye', 'bless', 'who?']
seen = set()
for g in CAND:
    if g in seen: continue
    seen.add(g)
    fam = store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1 ORDER BY 2 DESC, 1", (g,)).fetchall()
    print(f'  {g!r}: {len(fam)} families, {sum(n for _, n in fam)} tokens: {fam[:6]}')
CH = {}
for v, i, hp, g in store.execute("SELECT v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=33 ORDER BY v.id, w.idx"):
    CH.setdefault(v, []).append((i, hp.replace('/', ''), g))
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
d = yaml.safe_load(OV); BG = d['by_gloss']
print('candidates', len(seen), '| the chapter\'s glosses ALREADY rewritten by the earlier walks\' by-gloss overrides:', len(sorted({g for k in CH for _, _, g in CH[k] if g in BG})))
print('candidates already in by_gloss (excluded from GL):', sorted(g for g in seen if g in BG))
M20 = 'THE DEUTERONOMY WALK sitting 20 (2026-09-28, Deuteronomy 32, LEAN)'
i = OV.index(f'  # {M20}: the worst glosses of the song\'s seats'); j = OV.index('\n', i) + 1; rows = []
while True:
    m = re.match(r'  "[^"]+": "[^"]*"[^\n]*\n', OV[j:])
    if not m: break
    rows.append(m.group(0)); j += len(m.group(0))
print('sitting 20 by-gloss rows walked from its marker:', len(rows), '| its last row:', rows[-1].strip()[:60])
D32 = [l for l in OV.split('\n') if l.startswith('  "Deut.32.')]
print('by_gloss total', len(BG), '| by_ref total', len(d['by_ref']), '| the last Deut.32 by_ref line:', D32[-1][:50], '| Deut.33 by_ref rows present:', sum(1 for l in OV.split('\n') if re.match(r'  "Deut\.33\.', l)))
print('the "?" seats in the chapter:', [(v, i, hp) for v, L in CH.items() for i, hp, g in L if g == '?'])
print('the candidates\' seats in the chapter (gloss: verse/idx/token):')
for g in CAND:
    s = [f'{v}/{i}/{hp}' for v, L in CH.items() for i, hp, gg in L if gg == g]
    if s: print(f'  {g!r}: {s}')
