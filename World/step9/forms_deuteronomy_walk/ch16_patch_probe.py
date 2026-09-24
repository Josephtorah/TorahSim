import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DISPLAY PATCH PROBED (sitting 14, LEAN): for each candidate gloss of chapter 16's seats, the store's token families over the WHOLE store — by gloss where
# every token is the one word; the counts printed, never typed. Read-only.
import sqlite3, subprocess
ROOT = _ROOT
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
CAND = ['pretermission', 'the-pretermission', 'the-green', 'sweetness', 'the-sweetness', 'ferment', 'barm', 'sevened', 'the-sevened', 'the-hut', 'stroke', 'donation', 'the-donation', 'something-stationed', 'try', 'depression', 'in-hasty-flight', 'stop', 'cord-you/your', 'score-with-a-mark-as-a-tally', 'to-score-with-a-mark-as-a-tally', 'from-bore', 'bore', 'in-something-that-rises', 'abundance', 'spontaneity', 'and-brighten-up', 'move-in-acircle', 'in-years', 'like-present', 'like-benediction', 'and-scribe', 'stretch', 'scrutinize', 'wrench', 'run-after--gone-by)', 'strike-in', 'arise', 'seasons', 'like-come/bring', 'new-moon', 'in-new-moon', 'and-boil-up', 'in-nearest-part-you/your', 'to-scion-you/your', 'judge', 'mark', 'and-mark', 'in-gather-for-any-purpose-you/your', 'from-threshing-floor-you/your', 'income-you/your', 'blithe', 'particle-of-affirmation', 'to-tent-you/your', 'male-you/your', 'very-widely-used-as-a-relati', 'as-demonstrative', 'the-enactment', 'the-these', 'bring-forth', 'bring-forth-you/your', 'keep/guard', 'sickle', 'assembly', 'festival', 'in-festival', 'and-in-festival', 'in-festival-you/your', 'the-bereaved-person', 'and-the-bereaved-person', 'just', 'wise', 'right', 'side', 'hate', "'Asherah", 'to-face', 'emptily', 'in-one', 'from-Egypt', 'in-Egypt', 'to-reside', 'name-him/its', 'see', 'set', 'alive-you/your', 'from-earth', 'the-earth', 'and-servant-you/your', 'and-maidservant-you/your', 'and-son-you/your', 'and-daughter-you/your', 'and-the-sojourner', 'and-the-widow', 'and-the-Levite', 'hand-you/your', 'hand-him/its', 'over-him/its', 'to-morning', 'the-flesh', 'so-that', 'the-first', 'the-seventh', 'in-evening', 'in-day', 'and-in-day', 'day', 'all', 'eat', 'make', 'and-make', 'work', 'to-you/your']
for g in CAND:
    fam = store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1 ORDER BY 2 DESC, 1", (g,)).fetchall()
    print(f'  {g!r}: {len(fam)} families, {sum(n for _, n in fam)} tokens: {fam[:8]}')
CH = {}
for c, v, i, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=16 ORDER BY v.id, w.idx"):
    CH.setdefault(v, []).append((i, hp.replace('/', ''), g))
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
import yaml; d = yaml.safe_load(OV); BG = d['by_gloss']
print('the chapter\'s glosses ALREADY rewritten by the earlier walks\' by-gloss overrides:', sorted({g for v in CH for _, _, g in CH[v] if g in BG}))
print('by_gloss total', len(BG), '| by_ref total', len(d['by_ref']), '| the last by_ref line:', [l for l in OV.split('\n') if l.startswith('  "Deut.15.')][-1], '| sitting 13 marker present:', 'THE DEUTERONOMY WALK sitting 13 (2026-09-22, Deuteronomy 15)' in OV)
