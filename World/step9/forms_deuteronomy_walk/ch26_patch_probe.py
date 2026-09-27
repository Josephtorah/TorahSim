import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DISPLAY PATCH PROBED (sitting 18, LEAN; THE TAIL): for each candidate gloss of chapters 26-28's seats, the store's token families over the WHOLE store — by gloss where
# every token is the one word; the counts printed, never typed. Read-only. Sitting 17's form (ch22_patch_probe.py) over three chapters; the candidates the worst glosses
# read off the three store-gloss dumps (ch26_store_glosses.txt, ch27_store_glosses.txt, ch28_store_glosses.txt) and the GL lines read at the rows — the lean form's patch, the rest OWED.
import re, sqlite3, subprocess, yaml
ROOT = _ROOT
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
CAND = ['?', 'and-eye', 'Aramite', 'wander-away', 'and-turn-aside-from-the-road', 'in-adult', 'and-spoil', 'and-depress-literally-us/our', 'and-shriek', 'depression-us/our', 'and-in-fear', 'and-in-miracle', 'flow-freely', 'and-brighten-up', 'the-good--in-the-widest-sense', 'be-complete', 'tenth', 'the-tenth', 'income-you/your', 'to-bereaved-person', 'bereaved-person', 'and-sate', 'kindle', 'the-holiness', 'mislay', 'in-strictly-nothingness', 'in-foul-in-a-religious-sense', 'to-die', 'lean-out-suffix', 'from-abode', 'say', 'say-you/your', 'wealth', 'elevation', 'to-laudation', 'and-to-ornament', 'try', 'to-reside', 'tell', 'from-beginning', 'and-deposit-him/its', 'and-depress', 'and-old', 'and-grave', 'the-precept', 'quiver', 'complete', 'requital', 'dig', 'be--make-well', 'observe-quietly', 'execrate', 'and-pouring-over', 'something-disgusting', 'fabricator', 'sure', 'be-light', 'retreat', 'cord', 'associate-him/its', 'stray', 'stretch', 'wing', 'denude', 'give--away-in-marriage-him/its', 'donation', 'blood--of-man', 'arise', 'Daniel', 'be-high-actively', 'the-vilification', 'in-pass-over-you/your (pl)', 'pass-over', 'in-pass-over-you/your', 'in-lime', 'nation', 'the-benediction', 'and-reach-you/your', 'and-reach-you/your', 'bless', 'fetus', 'family-you/your', "and-'Ashtᵉrah", 'push', 'flit', 'sending-out', 'and-jut-over-you/your', 'to-good--in-the-widest-sense', 'depository-him/its', 'and-twine', 'twine', 'twine-you/your', 'twine-him/its', 'leanness', 'and-dark', 'hind-part', 'hinder', 'the-execration', 'the-confusion', 'the-reproof', 'desolate-you/your', 'wander-away-you/your', 'hurrying', 'loosen-me/my', 'impinge', 'and-impinge', 'in-emaciation', 'and-in-drought', 'and-in-paleness', 'and-run-after--gone-by)-you/your', 'light-particles', 'to-agitation', 'dominion', 'flabby-thing-you/your', 'shudder-with-terror', 'in-inflammation', 'and-in-tumor', 'and-in-boil', 'and-in-scurf', 'and-in-itch', 'to-mend', 'in-craziness', 'and-in-consternation', 'feel-of', 'in-light', 'push-forward', 'press-upon', 'and-pluck-off', 'pluck-off', 'be-open', 'engage-for-matrimony', 'copulate-with-her/its', 'lie-down-her/its', 'garden', 'strike-in', 'bore-him/its', 'bullock-you/your', 'and-pining', 'to-strength', 'and-crack-in-pieces', 'rave-through-insanity', 'from-view', 'the-leg', 'go', 'to-ruin', 'to-pithy-maxim', 'and-to-something-pointed', 'drive-forth-you/your', 'gather-for-any-purpose', 'eat-off-him/its', 'harvest', 'the-crimson-grub', 'smear-over', 'in-exiled', 'the-clatter', 'upper-part-suffix', 'and-to-miracle', 'in-blithesomeness', 'from-abundance', 'and-in-nudity', 'and-in-poverty', 'dart', 'strong', 'bend', 'swell-up', 'increase', 'must', 'and-cramp', 'the-elevated', 'and-the-gather-grapes', 'in-something-hemming-in', 'and-in-narrow-place', 'compress', 'and-the-luxurious', 'the-luxurious', 'spoil', 'and-in-overhanging', 'jut-over', 'from-set', 'from-failure', 'place-permanently', 'from-be-soft', 'and-from-softness', 'and-in-fetus-her/its', 'the-bring-forth', 'the-grave', 'grave', 'in-writing', 'the-be-heavy', 'and-the-fear', 'and-perhaps-to-separate', 'wound', 'and-build-up', 'build-up', 'and-malady', 'malady', 'go-up-them/their', 'and-swell-up', 'be-bright', 'to-be--make-well', 'to-wander-away', 'and-to-desolate', 'and-tear-away', 'and-dash-in-pieces-you/your', 'toss-violently-and-suddenly', 'quiet', 'timid', 'suspend', 'from-front', 'and-be-startled', 'be-startled', 'from-alarm', 'add', 'erect', 'from-to-separation', 'set']
seen = set()
for g in CAND:
    if g in seen: continue
    seen.add(g)
    fam = store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1 ORDER BY 2 DESC, 1", (g,)).fetchall()
    print(f'  {g!r}: {len(fam)} families, {sum(n for _, n in fam)} tokens: {fam[:6]}')
CH = {}
for c, v, i, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (26, 27, 28) ORDER BY v.id, w.idx"):
    CH.setdefault((c, v), []).append((i, hp.replace('/', ''), g))
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
d = yaml.safe_load(OV); BG = d['by_gloss']
print('the chapters\' glosses ALREADY rewritten by the earlier walks\' by-gloss overrides:', sorted({g for k in CH for _, _, g in CH[k] if g in BG}))
print('candidates already in by_gloss (excluded from GL):', sorted(g for g in seen if g in BG))
M17 = 'THE DEUTERONOMY WALK sitting 17 (2026-09-26, Deuteronomy 22-25, LEAN)'
i = OV.index(f'  # {M17}: the worst glosses of the four chapters\' seats'); j = OV.index('\n', i) + 1; rows = []
while True:
    m = re.match(r'  "[^"]+": "[^"]*"[^\n]*\n', OV[j:])
    if not m: break
    rows.append(m.group(0)); j += len(m.group(0))
print('sitting 17 by-gloss rows walked from its marker:', len(rows), '| its last row:', rows[-1].strip()[:60])
print('by_gloss total', len(BG), '| by_ref total', len(d['by_ref']), '| the last Deut.25 by_ref line:', [l for l in OV.split('\n') if l.startswith('  "Deut.25.')][-1][:50], '| Deut.26-28 by_ref rows present:', sum(1 for l in OV.split('\n') if re.match(r'  "Deut\.2[678]\.', l)))
print('the anokhi seats (the "?" gloss) in the three chapters:', [(c, v, i) for (c, v), L in CH.items() for i, hp, g in L if g == '?'])
