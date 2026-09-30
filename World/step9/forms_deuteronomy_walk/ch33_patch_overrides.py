import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 21 — CHAPTER 33, THE BLESSING (LEAN, 2026-09-29; THE TAIL): the store's glosses at the chapter's seats read back into the display layer's
# override file — BY GLOSS where the store's every token of the gloss is the one word read the same at every seat (the families PROBED FIRST by ch33_patch_probe.py,
# the counts read from its print: the tribal frames "and-to-Asher" .. "and-to-Zebulun" one token each, the precious things' four seats one family, the fiery law's
# ketiv one token), BY REFERENCE at the chapter's own seats where the family is mixed — THE KETIV AND THE QERE at 33:9 ("his son" written, "his sons" read — both
# tokens in the store, each by its seat), the eight "he said" frames, the tribes' names in the dative ("of Benjamin", "for Judah"), the blessing's homographs among
# the one-word glosses ("hide" is "He loves" at 33:3 and "the hidden treasures of" at 33:19; "separate" the nazirite's word at 33:16 and "alone" at 33:28; "front"
# ancient and eternal; "reside" four seats; "eye" the fountain). NO "?" seat in the chapter; "Daniel" -> "Dan" and "meaning-accession" -> "also" ALREADY by gloss
# from an earlier walk (the design's candidates, found in force). THE LEAN FORM: the worst glosses only; the rest OWED. Display only; the frozen unit untouched.
# Run ONCE (the anchors assert the rows absent first). Sitting 20's form (ch32_patch_overrides.py): the anchors the LAST ROWS of sitting 20's two blocks — the by_gloss
# block's last row found by walking from sitting 20's marker (never typed), the by_ref block's last row 32:48's. Every by-reference row carries the OLD gloss and
# asserts it at the seat. RUN FROM THE REPO ROOT; after the freeze chain.
import re, sqlite3, subprocess, yaml
ROOT = _ROOT
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for v, i, hp, g in store.execute("SELECT v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=33 ORDER BY v.id, w.idx"):
    SG.setdefault(v, []).append((i, hp.replace('/', ''), g))
def sg(v, tok, nth=0):
    hit = [g for _, hp, g in SG[v] if hp == tok]; assert len(hit) > nth, (v, tok, nth, hit); return hit[nth]
def sidx(v, tok, nth=0):
    hit = [i for i, hp, _ in SG[v] if hp == tok]; assert len(hit) > nth, (v, tok, nth, hit); return hit[nth]
GL0 = [('adult-him/its', 'his-men'), ('aid-you/your', 'your-help'), ('altar-you/your', 'Your-altar'), ('and-Urim-you/your', 'and-Your-Urim'), ('and-act', 'and-the-work-of'), ('and-aid', 'and-a-help'), ('and-conceal', 'and-the-hidden-treasures-of'), ('and-copper', 'and-brass'), ('and-covenant-you/your', 'and-Your-covenant'), ('and-delight', 'and-the-favor-of'), ('and-from-deep', 'and-from-the-deep'), ('and-from-distinguished-thing', 'and-from-the-precious-things-of'), ('and-from-head', 'and-from-the-top-of'), ('and-from-under', 'and-underneath'), ('and-full', 'and-full-of'), ('and-fulness-her/its', 'and-its-fulness'), ('and-hate-him/its', 'and-those-who-hate-him'), ('and-horn', 'and-the-horns-of'), ('and-in-arrogance-him/its', 'and-in-His-majesty'), ('and-like-day-you/your', 'and-as-your-days'), ('and-must', 'and-wine'), ('and-precept-you/your', 'and-Your-law'), ('and-south', 'and-the-south'), ('and-to-Asher', 'and-of-Asher'), ('and-to-Daniel', 'and-of-Dan'), ('and-to-Gad', 'and-of-Gad'), ('and-to-Levi', 'and-of-Levi'), ('and-to-Naphtali', 'and-of-Naphtali'), ('and-to-Zebulun', 'and-of-Zebulun'), ('and-to-crown-of-the-head', 'and-on-the-crown-of-the-head-of'), ('and-to-mother-him/its', 'and-to-his-mother'), ('arrogance-you/your', 'your-excellency'), ('bolt-you/your', 'your-bars'), ('brighten-up', 'rejoice'), ('crown-of-the-head', 'the-crown-of-the-head'), ('death-him/its', 'his-death'), ('draw-together-the-feet', 'that-leaps-forth'), ('fire-law', 'fiery-law'), ('from-distinguished-thing', 'from-the-precious-things-of'), ('from-narrow-him/its', 'from-his-adversaries'), ('from-right-hand-him/its', 'from-His-right-hand'), ('from-word-you/your', 'of-Your-words'), ('happiness-you/your', 'happy-are-you'), ('heavens-him/its', 'his-heavens'), ('hide-by-covering', 'reserved'), ('in-aid-you/your', 'as-your-help'), ('in-gather-for-any-purpose', 'when-were-gathered'), ('in-nose-you/your', 'in-Your-nostrils'), ('in-tent-you/your', 'in-your-tents'), ('judgment-you/your', 'Your-ordinances'), ('kind-you/your', 'Your-pious-one'), ('like-roar', 'as-a-lioness'), ('like-strength', 'like-God'), ('perfections-you/your', 'Your-Thummim'), ('quiet-you/your', 'your-strength'), ('royal-edict', 'law'), ('sacred-him/its', 'His-holy-ones'), ('shoulder-him/its', 'his-shoulders'), ('something-said-you/your', 'Your-word'), ('to-foot-you/your', 'at-Your-feet'), ('to-place-of-refuge', 'in-safety'), ('toss-him/its', 'You-strove-with-him'), ('wild-bull', 'the-wild-ox'),
       ('abode', 'a-dwelling-place'), ('bramble', 'the-bush'), ('cub', 'whelp'), ('delight', 'favor'), ('resources', 'the-abundance-of'), ('satiated', 'sated'), ('strew', 'they-sat-down'), ('waist', 'the-loins-of')]
TRIBAL = ['and-to-Asher', 'and-to-Daniel', 'and-to-Gad', 'and-to-Levi', 'and-to-Naphtali', 'and-to-Zebulun']
P = f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'
t = open(P, encoding='utf-8').read()
d0 = yaml.safe_load(t); BG0 = d0['by_gloss']
DROP = [g for g, _ in GL0 if g in BG0]; GL = [(g, n) for g, n in GL0 if g not in BG0]
print('by-gloss candidates already rewritten by an earlier walk (dropped):', DROP)
SPEC = [
 (2, 'ואתה', 'and-He-came', 0, 'and-arrive'), (21, 'ויתא', 'and-he-came', 0, 'and-arrive'), (5, 'ויהי', 'and-there-was', 0, 'and-be'), (6, 'ויהי', 'and-let-be', 0, 'and-be'), (29, 'ויכחשו', 'and-shall-dwindle-away', 0, 'and-be-untrue'),
 (10, 'וכליל', 'and-whole-offering', 0, 'and-complete'), (24, 'וטבל', 'and-let-him-dip', 0, 'and-dip'), (6, 'ואל', 'and-let-not', 0, 'and-do-not'), (27, 'ויגרש', 'and-He-drove-out', 0, 'and-drive-out-from-a-possession'), (2, 'וזרח', 'and-He-rose', 0, 'and-irradiate'),
 (20, 'וטרף', 'and-tears', 0, 'and-pluck-off'), (28, 'וישכן', 'and-dwells', 0, 'and-reside'), (13, 'וליוסף', 'and-of-Joseph', 0, 'and-to-Joseph'), (11, 'קמיו', 'those-who-rise-against-him', 0, 'arise-him/its'), (11, 'יקומון', 'they-rise', 0, 'arise-suffix'),
 (29, 'נושע', 'saved', 0, 'be-open'), (11, 'תרצה', 'accept', 0, 'be-pleased-with'), (24, 'רצוי', 'favored', 0, 'be-pleased-with'), (17, 'ינגח', 'he-shall-gore', 0, 'butt-with-the-horns'), (2, 'בא', 'came', 0, 'come/bring'), (7, 'תביאנו', 'bring-him', 0, 'come/bring-him/its'), (16, 'תבואתה', 'let-it-come', 0, 'come/bring-suffix'),
 (11, 'מחץ', 'smite-through', 0, 'dash-asunder'), (29, 'במותימו', 'their-high-places', 0, 'elevation-them/their'), (10, 'יורו', 'they-shall-teach', 0, 'flow-as-water'), (24, 'רגלו', 'his-foot', 0, 'foot-him/its'), (11, 'חילו', 'his-substance', 0, 'force-him/its'), (2, 'מרבבת', 'from-the-myriads-of', 0, 'from-abundance'), (24, 'מבנים', 'above-sons', 0, 'from-son'),
 (7, 'ידיו', 'his-hands', 0, 'hand-him/its'), (11, 'ידיו', 'his-hands', 0, 'hand-him/its'), (17, 'קרניו', 'his-horns', 0, 'horn-him/its'), (18, 'בצאתך', 'in-your-going-out', 0, 'in-bring-forth-you/your'), (9, 'שמרו', 'they-kept', 0, 'keep/guard'), (3, 'ישא', 'receives', 0, 'lift/carry'), (7, 'רב', 'contend', 0, 'many/great'),
 (12, 'עליו', 'by-him', 0, 'over-him/its'), (12, 'עליו', 'over-him', 1, 'over-him/its'), (23, 'ירשה', 'possess', 0, 'possess/inherit-suffix'), (10, 'ישימו', 'they-shall-put', 0, 'put/set'), (9, 'ראיתיו', 'I-have-seen-him', 0, 'see-him/its'), (19, 'יזבחו', 'they-shall-offer', 0, 'slaughter-an-animal'),
 (9, 'בנו', 'his-son', 0, 'son-him/its'), (9, 'בניו', 'his-sons', 0, 'son-him/its'), (8, 'נסיתו', 'You-proved-him', 0, 'test-him/its'), (1, 'הברכה', 'the-blessing', 0, 'the-benediction'), (9, 'האמר', 'who-said', 0, 'the-say'), (26, 'אין', 'there-is-none', 0, 'there-is-not'),
 (12, 'לבנימן', 'of-Benjamin', 0, 'to-Benjamin'), (7, 'ליהודה', 'for-Judah', 0, 'to-Judah'), (1, 'לפני', 'before', 0, 'to-face'), (9, 'לאביו', 'of-his-father', 0, 'to-father-him/its'), (16, 'לראש', 'on-the-head-of', 0, 'to-head'), (8, 'לאיש', 'to-the-man', 0, 'to-man'), (2, 'למו', 'to-them', 0, 'to-them/their'), (2, 'למו', 'to-them', 1, 'to-them/their'), (7, 'קול', 'the-voice-of', 0, 'voice/sound'),
 (17, 'רבבות', 'the-ten-thousands-of', 0, 'abundance'), (20, 'זרוע', 'the-arm', 0, 'arm'), (27, 'זרעת', 'the-arms-of', 0, 'arm'), (4, 'קהלת', 'the-congregation-of', 0, 'assemblage'), (23, 'ברכת', 'the-blessing-of', 0, 'benediction'), (20, 'מרחיב', 'who-enlarges', 0, 'broaden'), (19, 'יקראו', 'they-shall-call', 0, 'call'),
 (17, 'אפסי', 'the-ends-of', 0, 'cessation'), (12, 'חפף', 'covers', 0, 'cover'), (13, 'רבצת', 'that-couches', 0, 'crouch'), (28, 'יערפו', 'drop-down', 0, 'droop'), (29, 'חרב', 'the-sword-of', 0, 'drought'), (21, 'מחקק', 'the-lawgiver', 0, 'hack'), (3, 'חבב', 'He-loves', 0, 'hide'), (19, 'טמוני', 'the-hidden-treasures-of', 0, 'hide'),
 (15, 'גבעות', 'hills', 0, 'hillock'), (28, 'דגן', 'corn', 0, 'increase'), (14, 'ירחים', 'moons', 0, 'lunation'), (17, 'הדר', 'majesty', 0, 'magnificence'), (10, 'קטורה', 'incense', 0, 'perfume'), (4, 'מורשה', 'an-inheritance', 0, 'possession'), (26, 'שחקים', 'the-skies', 0, 'powder'), (4, 'תורה', 'a-law', 0, 'precept'), (14, 'גרש', 'the-yield-of', 0, 'produce'),
 (19, 'צדק', 'righteousness', 0, 'right'), (5, 'שבטי', 'the-tribes-of', 0, 'scion'), (16, 'נזיר', 'the-one-separate', 0, 'separate'), (28, 'בדד', 'alone', 0, 'separate'), (2, 'הופיע', 'He-shone', 0, 'shine'), (21, 'חלקת', 'the-portion-of', 0, 'smoothness'), (19, 'יינקו', 'they-shall-suck', 0, 'suck'),
 (12, 'ישכן', 'shall-dwell', 0, 'reside'), (12, 'שכן', 'He-dwells', 0, 'reside'), (16, 'שכני', 'Him-that-dwelt-in', 0, 'reside'), (20, 'שכן', 'he-dwells', 0, 'reside'), (23, 'ים', 'the-sea', 0, 'seas'), (15, 'קדם', 'ancient', 0, 'front'), (27, 'קדם', 'eternal', 0, 'front'), (5, 'ראשי', 'the-heads-of', 0, 'head'), (21, 'ראשי', 'the-heads-of', 0, 'head'),
 (21, 'עשה', 'he-executed', 0, 'make'), (6, 'יחי', 'let-live', 0, 'live'), (6, 'ימת', 'let-die', 0, 'die'), (26, 'רכב', 'who-rides', 0, 'ride'), (2, 'קדש', 'holy-ones', 0, 'holiness'), (9, 'ינצרו', 'they-observe', 0, 'guard'), (9, 'ידע', 'he-acknowledged', 0, 'know'), (17, 'אלפי', 'the-thousands-of', 0, 'thousand'),
 (15, 'הררי', 'the-mountains-of', 0, 'mountain'), (19, 'הר', 'the-mountain', 0, 'mountain'), (28, 'עין', 'the-fountain-of', 0, 'eye'), (13, 'מברכת', 'blessed-of', 0, 'bless'), (20, 'ברוך', 'blessed-be', 0, 'bless'), (24, 'ברוך', 'blessed-be', 0, 'bless'), (29, 'מי', 'who', 0, 'who?')] + [(v, 'אמר', 'he-said', 0, 'say') for v in (8, 12, 13, 18, 20, 22, 23, 24)]
bad = [(v, tok, nth, sg(v, tok, nth), old) for v, tok, new, nth, old in SPEC if sg(v, tok, nth) != old]; assert not bad, bad   # the old gloss at the seat as read
REF3 = [(f'Deut.33.{v}:{sidx(v, tok, nth)}', new, tok) for v, tok, new, nth, old in SPEC]
REF = [(k, v) for k, v, _ in REF3]; TOK = {k: t_ for k, _, t_ in REF3}
assert len(REF) == len({k for k, _ in REF}) == len(SPEC) and len(GL) == len({g for g, _ in GL})
assert all(sg(v, tok, nth) != new for v, tok, new, nth, old in SPEC)   # no row rewrites a gloss to itself
CLASH = [(v, tok, old) for v, tok, _, nth, old in SPEC if old in dict(GL)]; assert not CLASH, CLASH   # a seat patched by gloss is not patched again by reference
GLSEATS = {g: [(v, i, hp) for v, L in SG.items() for i, hp, gg in L if gg == g] for g, _ in GL}; NOSEAT = [g for g, s in GLSEATS.items() if not s]; assert not NOSEAT, NOSEAT   # every by-gloss row has a seat in the chapter
assert not re.search(r'"Deut\.33\.', t) and all(g not in BG0 for g, _ in GL)
MARK = 'THE DEUTERONOMY WALK sitting 21 (2026-09-29, Deuteronomy 33, LEAN)'
assert MARK not in t
M20 = 'THE DEUTERONOMY WALK sitting 20 (2026-09-28, Deuteronomy 32, LEAN)'
i = t.index(f'  # {M20}: the worst glosses of the song\'s seats')
j = t.index('\n', i) + 1
rows = []
while True:
    m = re.match(r'  "[^"]+": "[^"]*"[^\n]*\n', t[j:])
    if not m: break
    rows.append(m.group(0)); j += len(m.group(0))
assert len(rows) == 117, len(rows)   # sitting 20's by-gloss rows (the probe's walk 117)
A1 = rows[-1]; assert t.count(A1) == 1
gl_block = A1 + f'\n  # {MARK}: the worst glosses of the blessing\'s seats, the families probed in the store first (ch33_patch_probe.py) — the lean form\'s patch; the rest OWED (COMPILE_DEBT\'s lean-pass box)\n' + ''.join(f'  "{k}": "{v}"\n' for k, v in GL)
t = t.replace(A1, gl_block)
m2 = re.search(r'^  "Deut\.32\.48:4": "in-the-selfsame"[^\n]*\n', t, re.M); assert m2 and t.count('"Deut.32.48:4": "in-the-selfsame"') == 1
A2 = m2.group(0)
ref_block = A2 + f'  # {MARK}: the chapter\'s seats by reference — the token named beside each; the indices the store\'s own (the ketiv and the qere at 33:9 each by its seat — "his son" written, "his sons" read; the eight "he said" frames; the tribes in the dative; the blessing\'s one-word homographs by their seat — "hide" He loves and the hidden treasures, "separate" the one separate and alone, "front" ancient and eternal, "reside" four ways, "eye" the fountain; the old gloss asserted at every seat)\n' + ''.join(f'  "{k}": "{v}"   # {TOK[k]}\n' for k, v in REF)
t = t.replace(A2, ref_block)
open(P, 'w', encoding='utf-8').write(t)
d = yaml.safe_load(open(P, encoding='utf-8'))
assert all(d['by_ref'][k] == v for k, v in REF) and all(d['by_gloss'][k] == v for k, v in GL)
KQ = sum(1 for v, tok, _, _, _ in SPEC if (v, tok) in ((9, 'בנו'), (9, 'בניו'))) + sum(len(GLSEATS[g]) for g in ('fire-law', 'royal-edict') if g in GLSEATS)
print('override rows written: by_ref', len(REF), 'by_gloss', len(GL), '| by_ref total', len(d['by_ref']), '| by_gloss total', len(d['by_gloss']), '| dropped (already by gloss)', len(DROP), '| the ketiv-qere seats', KQ, '| the tribal frames by gloss', sum(1 for g, _ in GL if g in TRIBAL), '| the he-said frames by reference', sum(1 for _, _, _, _, old in SPEC if old == 'say'), '| by-gloss seats in the chapter', sum(len(s) for s in GLSEATS.values()))
