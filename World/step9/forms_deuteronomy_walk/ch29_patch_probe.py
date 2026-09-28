import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DISPLAY PATCH PROBED (sitting 19, LEAN; THE TAIL): for each candidate gloss of chapters 29-31's seats, the store's token families over the WHOLE store — by gloss where
# every token is the one word; the counts printed, never typed. Read-only. Sitting 18's form (ch26_patch_probe.py) over three chapters; the candidates the worst glosses
# read off the store's gloss list for the three chapters (printed at the tail's open: 95 simple + 351 complex not yet by gloss; 106 already rewritten by gloss) — the lean form's patch, the rest OWED.
import re, sqlite3, subprocess, yaml
ROOT = _ROOT
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
CAND = ['?', 'and-?', 'and-broadness.-i.e.--the-ear', 'in-broadness.-i.e.--the-ear', 'in-broadness.-i.e.--the-ear-them/their', 'and-be--make-well-you/your', 'and-be-alert', 'and-be-fat', 'and-break-up', 'and-commit-adultery', 'and-crouch', 'and-duplicate', 'and-goad', 'and-goad-her/its', 'and-eye', 'and-in-splinter', 'and-intoxicant', 'and-loosen-me/my', 'and-loosen-them/their', 'loosen-you/your', 'and-powder', 'and-push-off', 'push-off-you/your', 'and-sandal-tongue-you/your', 'and-scorn-me/my', 'and-scribe-you/your (pl)', 'and-stroke', 'and-the-denude', 'and-tear-away-them/their', 'and-throw-out-them/their', 'and-tightness', 'bale-up-water', 'be--bitter', 'be--circumspect-and-hence', 'be-rubbed', 'be-smooth', 'burning--anger', 'cypress-resin', 'dash-in-pieces-you/your', 'disgusting-them/their', 'exile-you/your', 'fasten-upon', 'from-chop', 'from-extremity', 'in-extremity', 'in-non-occurrence', 'in-obstinacy', 'in-still/again-me/my', 'lift/carry', 'the-lift/carry', 'like-destruction', 'log-them/their', 'malady-her/its', 'nape-you/your', 'perhaps-to-separate', 'poisonous-plant', 'run-after--gone-by)-you/your', 'scrape--together', 'the-hide', 'the-imprecation', 'and-in-imprecation-him/its', 'the-sated', 'the-severe', 'the-vilification', 'to-concretely', 'to-be-bright', 'to-encountering-us/our', 'to-grave', 'turn-about', 'yield-seed', 'from-side', 'in-column', 'and-the-miracle', 'the-hinder', 'and-the-strange', 'be-fruitful', 'in-seasons', 'in-festival', 'and-in-heat', 'and-in-heat-him/its', 'in-nose', 'in-nose-him/its', 'nose-me/my', 'and-jealousy-him/its', 'and-grasp-you/your', 'grasp-you/your', 'and-hide', 'and-find-him/its', 'find-me/my', 'and-encounter', 'and-arise', 'and-command-him/its', 'and-place', 'bring-near', 'and-turn', 'and-strike-them/their', 'and-bless', 'and-possess/inherit-her/its', 'and-possess/inherit-them/their', 'and-Jehoshua', 'to-Jehoshua', 'the-Menashshite', 'in-alive', 'the-alive', 'the-benediction', 'the-death', 'and-the-death', 'the-bad', 'the-priest', 'the-man', 'and-the-woman', 'family-you/your (pl)', 'dress-you/your (pl)', 'to-pass-over-you/your', 'there-is-him/its', 'the-they', 'in-hear-him/its', 'and-divide-him/its', 'to-bad', 'and-come/bring-you/your', 'hate-you/your', 'belly-you/your', 'and-length', 'be-able', 'to-bring-forth', 'the-walk/go', 'from-face-them/their', 'in-come/bring', 'in-tent', 'lie-down', 'behold-you/your', 'in-nearest-part-me/my', 'in-nearest-part-him/its', 'put/set-her/its', 'come/bring-him/its', 'form-him/its', 'and-hear-us/our', 'and-make-her/its', 'and-take-her/its',
        'nose', 'cremation', 'loosen', 'box', 'column', 'wound', 'sprout', 'scion', 'assemblage', 'opening', 'remote', 'living', 'smoke', 'find', 'imprecation', 'decay', 'prostrate', 'grave', 'cut', 'front', 'foreign', 'food', 'family', 'fear', 'root', 'set', 'make', 'over', 'near', 'forever', 'tell', 'call', 'old', 'bad', 'silver', 'be']
seen = set()
for g in CAND:
    if g in seen: continue
    seen.add(g)
    fam = store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1 ORDER BY 2 DESC, 1", (g,)).fetchall()
    print(f'  {g!r}: {len(fam)} families, {sum(n for _, n in fam)} tokens: {fam[:6]}')
CH = {}
for c, v, i, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (29, 30, 31) ORDER BY v.id, w.idx"):
    CH.setdefault((c, v), []).append((i, hp.replace('/', ''), g))
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
d = yaml.safe_load(OV); BG = d['by_gloss']
print('the chapters\' glosses ALREADY rewritten by the earlier walks\' by-gloss overrides:', len(sorted({g for k in CH for _, _, g in CH[k] if g in BG})))
print('candidates already in by_gloss (excluded from GL):', sorted(g for g in seen if g in BG))
print('by_gloss values of interest:', {g: BG.get(g) for g in ['?', 'and-?', 'duplicate', 'goad', 'try', 'and-try', 'convoke', 'the-remission', 'the-hut', 'awe', 'the-testing', 'station', 'seasons', 'safe']})
for g in ['?', 'and-?']:
    i = OV.find(f'\n  "{g}":'); print(f'  the by_gloss row for {g!r} at byte {i}:', OV[i+1:OV.find(chr(10), i+1)][:120], '| the marker above it:', ([l for l in OV[:i].split('\n') if l.startswith('  # ')] or ['(none — the row sits above every marker)'])[-1][:110])
M18 = 'THE DEUTERONOMY WALK sitting 18 (2026-09-26, Deuteronomy 26-28, LEAN)'
i = OV.index(f'  # {M18}: the worst glosses of the three chapters\' seats'); j = OV.index('\n', i) + 1; rows = []
while True:
    m = re.match(r'  "[^"]+": "[^"]*"[^\n]*\n', OV[j:])
    if not m: break
    rows.append(m.group(0)); j += len(m.group(0))
print('sitting 18 by-gloss rows walked from its marker:', len(rows), '| its last row:', rows[-1].strip()[:60])
print('by_gloss total', len(BG), '| by_ref total', len(d['by_ref']), '| the last Deut.28 by_ref line:', [l for l in OV.split('\n') if l.startswith('  "Deut.28.')][-1][:50], '| Deut.29-31 by_ref rows present:', sum(1 for l in OV.split('\n') if re.match(r'  "Deut\.(29|30|31)\.', l)))
print('the anokhi seats (the "?" gloss) in the three chapters:', [(c, v, i) for (c, v), L in CH.items() for i, hp, g in L if g == '?'])
print('the prefixed blank seats ("and-?"):', [(c, v, i) for (c, v), L in CH.items() for i, hp, g in L if g == 'and-?'])
SIMPLE = ['nose', 'cremation', 'loosen', 'box', 'column', 'wound', 'sprout', 'scion', 'assemblage', 'opening', 'remote', 'living', 'smoke', 'find', 'imprecation', 'decay', 'prostrate', 'grave', 'cut', 'front', 'foreign', 'food', 'family', 'fear', 'root', 'forever', 'tell', 'call', 'old', 'bad', 'be']
print('the simple candidates\' seats in the three chapters:')
for g in SIMPLE: print(f'  {g!r}:', [f'{c}:{v}/{i}/{hp}' for (c, v), L in CH.items() for i, hp, gg in L if gg == g])
