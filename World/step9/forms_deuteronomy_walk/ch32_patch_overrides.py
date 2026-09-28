import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 20 — CHAPTER 32, THE SONG (LEAN, 2026-09-28; THE TAIL): the store's glosses at the chapter's seats read back into the display layer's
# override file — BY GLOSS where the store's every token of the gloss is the one word read the same at every seat (the families PROBED FIRST by ch32_patch_probe.py,
# the counts read from its print), BY REFERENCE at the chapter's own seats where the family is mixed — THE SONG'S HOMOGRAPHS AMONG THEM: "cliff" is the Rock (32:15,
# 18, 37) and the flinty rock (32:13), "strength" is God (32:4, 18) and a no-god (32:12, 21), "deity" God (32:15) and gods (32:17), "pasture" the wilderness,
# "elevation" the Most High and the high places (the ketiv and the qere both tokens at 32:13); the seven "?" seats of the pronoun I by reference ("?" is by gloss to
# a blank from an earlier walk, "and-?" to "and-I", so 32:21 and 32:39's prefixed seats are covered already). THE LEAN FORM: the worst glosses only; the rest OWED.
# Display only; the frozen units untouched. Run ONCE (the anchors assert the rows absent first). Sitting 19's form (ch29_patch_overrides.py): the anchors the LAST
# ROWS of sitting 19's two blocks — the by_gloss block's last row found by walking from sitting 19's marker (never typed), the by_ref block's last row 31:19's.
# Every by-reference row carries the OLD gloss and asserts it at the seat. No one-word GEN computation this sitting — the song's one-word glosses are homographs.
# RUN FROM THE REPO ROOT; after the freeze chain.
import re, sqlite3, subprocess, yaml
ROOT = _ROOT
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for v, i, hp, g in store.execute("SELECT v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=32 ORDER BY v.id, w.idx"):
    SG.setdefault(v, []).append((i, hp.replace('/', ''), g))
def sg(v, tok, nth=0):
    hit = [g for _, hp, g in SG[v] if hp == tok]; assert len(hit) > nth, (v, tok, nth, hit); return hit[nth]
def sidx(v, tok, nth=0):
    hit = [i for i, hp, _ in SG[v] if hp == tok]; assert len(hit) > nth, (v, tok, nth, hit); return hit[nth]
GL0 = [('act-him/its', 'His-work'), ('alive-you/your (pl)', 'your-life'), ('and-Hosea', 'and-Hoshea'), ('and-be-erect-you/your', 'and-established-you'), ('and-burn', 'and-it-burns'), ('and-drought-me/my', 'and-my-sword'), ('and-exile', 'and-captives'), ('and-from-apartment', 'and-from-the-chambers'), ('and-from-cultivated-field', 'and-from-the-fields-of'), ('and-hating-us/our', 'and-our-enemies'), ('and-hurry', 'and-hastens'), ('and-in-formless', 'and-in-the-waste'), ('and-lick', 'and-sets-on-fire'), ('and-like-rain', 'and-like-showers'), ('and-poisonous-plant', 'and-the-venom-of'), ('and-prepared', 'and-he-goats'), ('and-produce-her/its', 'and-its-increase'), ('and-requital', 'and-recompense'), ('and-revenge', 'and-vengeance'), ('and-ruin', 'and-destruction'), ('and-scorn', 'and-He-spurned'), ('and-shine', 'and-grew-fat'), ('and-surround-you/your (pl)', 'and-help-you'), ('and-tell-you/your', 'and-he-will-tell-you'), ('and-there-suffix', 'and-there'), ('and-to-hate-me/my', 'and-to-those-who-hate-Me'), ('and-tooth', 'and-the-teeth-of'), ('and-tortuous', 'and-crooked'), ('and-trample-down', 'and-kicked'), ('and-wilt', 'and-despised'), ('be--zealous-him/its', 'they-roused-Him-to-jealousy'), ('be--zealous-me/my', 'they-roused-Me-to-jealousy'), ('be--zealous-them/their', 'I-will-rouse-them-to-jealousy'), ('bear-young-you/your', 'who-begot-you'), ('become-tipsy', 'I-will-make-drunk'), ('bunch-of-grapes', 'the-clusters-of'), ('cliff-them/their', 'their-Rock'), ('drought-me/my', 'my-sword'), ('erect-you/your', 'who-acquired-you'), ('flee-for-protection', 'they-took-refuge'), ('from-blood--of-man', 'from-the-blood-of'), ('from-craggy-rock', 'from-the-crag'), ('from-flint', 'from-the-flinty'), ('from-man-in-general', 'from-among-men'), ('from-vexation', 'from-the-provocation-of'), ('from-vine', 'from-the-vine-of'), ('go-away', 'is-gone'), ('grape-them/their', 'their-grapes'), ('grow-fat', 'you-grew-gross'), ('guard-him/its', 'He-kept-him'), ('guide-him/its', 'led-him'), ('in-break-through-him/its', 'when-He-separated'), ('in-depository-me/my', 'in-My-treasuries'), ('in-emptiness-them/their', 'with-their-vanities'), ('in-something-disgusting', 'with-abominations'), ('in-turn-aside', 'with-strange-gods'), ('keep-in-memory', 'you-were-unmindful'), ('last-them/their', 'their-end'), ('like-cliff-us/our', 'like-our-Rock'), ('like-little-man-of-the-eye', 'as-the-apple-of'), ('like-shower', 'like-small-rain'), ('live-coal', 'burning-heat'), ('memento-them/their', 'their-memory'), ('narrow-them/their', 'their-adversaries'), ('nestling-him/its', 'its-young'), ('oppression-them/their', 'their-calamity'), ('piercer-me/my', 'My-arrows'), ('pinion-him/its', 'its-pinions'), ('puff-them/their', 'I-would-scatter-them'), ('revolve-him/its', 'He-encircled-him'), ('sea-monster', 'serpents'), ('sell-them/their', 'had-sold-them'), ('separate-mentally-him/its', 'He-cared-for-him'), ('shut-up-them/their', 'had-delivered-them-up'), ('something-poured-out-them/their', 'their-drink-offering'), ('something-received-me/my', 'My-doctrine'), ('something-said', 'the-words-of'), ('something-said-me/my', 'my-speech'), ('something-saved-him/its', 'his-salvation'), ('stain-them/their', 'their-blemish'), ('store-away', 'laid-up-in-store'), ('storm-them/their', 'dreaded-them'), ('to-doemon', 'to-demons'), ('to-narrow-him/its', 'to-His-adversaries'), ('to-narrow-me/my', 'to-My-adversaries'), ('trouble-him/its', 'they-provoked-Him'), ('trouble-me/my', 'they-provoked-Me'), ('trouble-them/their', 'I-will-provoke-them'), ('twist-you/your', 'who-bore-you'), ('wine-them/their', 'their-wine'), ('to-last-them/their', 'their-latter-end'), ('from-near', 'of-late'), ('know-them/their', 'they-knew-them'), ('vine-them/their', 'their-vine'),
       ('advice', 'counsel'), ('asp', 'asps'), ('boundary', 'the-borders-of'), ('crawl', 'the-crawling-things-of'), ('creak', 'sing-aloud'), ('desolation', 'a-wilderness'), ('established', 'faithfulness'), ('exhausted', 'wasted-with'), ('howl', 'howling'), ('inflame', 'is-kindled'), ('intelligence', 'understanding'), ('kidney', 'the-kidneys-of'), ('leadership', 'the-leaders-of'), ('lightning', 'the-lightning-of'), ('magistrate', 'judges'), ('magnitude', 'greatness'), ('point', 'I-whet'), ('selected', 'the-young-man'), ('violent', 'cruel'), ('wake', 'stirs-up'), ("Shᵉ'Owl", 'Sheol'), ('stupid', 'foolish'), ('fright', 'terror')]
P = f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'
t = open(P, encoding='utf-8').read()
d0 = yaml.safe_load(t); BG0 = d0['by_gloss']
DROP = [g for g, _ in GL0 if g in BG0]; GL = [(g, n) for g, n in GL0 if g not in BG0]
print('by-gloss candidates already rewritten by an earlier walk (dropped):', DROP)
ANOKHI = [(39, 'אני', 'I', 0, '?'), (39, 'אני', 'I', 1, '?'), (39, 'אני', 'I', 2, '?'), (40, 'אנכי', 'I', 0, '?'), (46, 'אנכי', 'I', 0, '?'), (49, 'אני', 'I', 0, '?'), (52, 'אני', 'I', 0, '?')]
SPEC = ANOKHI + [
 (4, 'הצור', 'the-Rock', 0, 'the-cliff'), (13, 'צור', 'rock', 0, 'cliff'), (15, 'צור', 'the-Rock-of', 0, 'cliff'), (18, 'צור', 'the-Rock', 0, 'cliff'), (37, 'צור', 'the-rock', 0, 'cliff'),
 (4, 'אל', 'God', 0, 'strength'), (12, 'אל', 'god', 0, 'strength'), (18, 'אל', 'God', 0, 'strength'), (21, 'אל', 'god', 0, 'strength'), (15, 'אלוה', 'God', 0, 'deity'), (17, 'אלה', 'gods', 0, 'deity'),
 (8, 'עליון', 'the-Most-High', 0, 'elevation'), (13, 'במותי', 'the-high-places-of', 0, 'elevation'), (13, 'במתי', 'the-high-places-of', 0, 'elevation'), (10, 'מדבר', 'a-wilderness', 0, 'pasture'), (51, 'מדבר', 'the-wilderness-of', 0, 'pasture'),
 (45, 'ויכל', 'and-finished', 0, 'and-be-complete'), (19, 'ובנתיו', 'and-His-daughters', 0, 'and-daughter-him/its'), (24, 'ולחמי', 'and-devoured-by', 0, 'and-feed-on'), (50, 'והאסף', 'and-be-gathered', 0, 'and-gather-for-any-purpose'), (50, 'ויאסף', 'and-was-gathered', 0, 'and-gather-for-any-purpose'),
 (36, 'ועזוב', 'and-left', 0, 'and-loosen'), (36, 'ואפס', 'and-there-is-none', 0, 'and-cessation'), (15, 'ויטש', 'and-he-forsook', 0, 'and-pound'), (41, 'ותאחז', 'and-takes-hold', 0, 'and-seize'), (13, 'וינקהו', 'and-He-made-him-suck', 0, 'and-suck-him/its'),
 (29, 'ישכילו', 'they-would-understand', 0, 'be--circumspect-and-hence'), (47, 'תאריכו', 'you-shall-prolong', 0, 'be--long'), (23, 'אכלה', 'I-will-spend', 0, 'be-complete'), (15, 'עבית', 'you-grew-thick', 0, 'be-dense'), (27, 'רמה', 'is-exalted', 0, 'be-high-actively'), (41, 'אשלם', 'I-will-repay', 0, 'be-safe'), (29, 'חכמו', 'they-were-wise', 0, 'be-wise'),
 (11, 'יפרש', 'He-spreads', 0, 'break-apart'), (34, 'חתם', 'sealed', 0, 'close-up'), (51, 'מעלתם', 'you-trespassed', 0, 'cover-up'), (14, 'חמאת', 'the-curd-of', 0, 'curdled-milk'), (39, 'מחצתי', 'I-have-wounded', 0, 'dash-asunder'), (27, 'לולי', 'were-it-not', 0, 'if-not'),
 (13, 'ירכבהו', 'He-made-him-ride', 0, 'ride-him/its'), (38, 'זבחימו', 'their-sacrifices', 0, 'sacrifice-them/their'), (23, 'אספה', 'I-will-heap', 0, 'scrape--together'), (7, 'בינו', 'consider', 0, 'separate-mentally'), (29, 'יבינו', 'they-would-discern', 0, 'separate-mentally'),
 (17, 'יזבחו', 'they-sacrificed', 0, 'slaughter-an-animal'), (39, 'מציל', 'who-delivers', 0, 'snatch-away'), (36, 'ידין', 'will-judge', 0, 'straight-course'), (49, 'לאחזה', 'for-a-possession', 0, 'to-something-seized'), (6, 'תגמלו', 'do-you-requite', 0, 'treat-a-person'), (27, 'אגור', 'I-feared', 0, 'turn-aside-from-the-road'),
 (12, 'עמו', 'with-Him', 0, 'with-him/its'), (9, 'עמו', 'His-people', 0, 'people-him/its'), (36, 'עמו', 'His-people', 0, 'people-him/its'), (43, 'עמו', 'His-people', 0, 'people-him/its'), (43, 'עמו', 'His-people', 1, 'people-him/its'), (50, 'עמיו', 'his-people', 0, 'people-him/its'), (50, 'עמיך', 'your-people', 0, 'people-you/your'),
 (50, 'בהר', 'on-the-mountain', 0, 'in-mountain'), (35, 'רגלם', 'their-foot', 0, 'foot-them/their'), (39, 'ואחיה', 'and-I-make-alive', 0, 'and-live'), (46, 'תצום', 'you-shall-command-them', 0, 'command-them/their'), (25, 'שיבה', 'gray-hairs', 0, 'old-age'), (47, 'עברים', 'are-crossing', 0, 'pass-over'), (46, 'שימו', 'set', 0, 'put/set'),
 (30, 'רבבה', 'ten-thousand', 0, 'abundance'), (26, 'אשביתה', 'I-would-make-cease', 0, 'cease'), (38, 'סתרה', 'a-protection', 0, 'cover'), (5, 'שחת', 'has-dealt-corruptly', 0, 'decay'), (27, 'פעל', 'has-wrought', 0, 'do'), (2, 'תזל', 'shall-distil', 0, 'drip'), (2, 'יערף', 'shall-drop', 0, 'droop'), (25, 'חרב', 'the-sword', 0, 'drought'),
 (4, 'תמים', 'perfect', 0, 'entire'), (4, 'עול', 'iniquity', 0, 'evil'), (4, 'אמונה', 'faithfulness', 0, 'firmness'), (3, 'הבו', 'ascribe', 0, 'give'), (43, 'יקום', 'He-will-avenge', 0, 'grudge'), (24, 'חמת', 'the-poison-of', 0, 'heat'), (33, 'חמת', 'the-poison-of', 0, 'heat'), (11, 'ירחף', 'hovers', 0, 'hovering'), (36, 'עצור', 'shut-up', 0, 'inclose'),
 (24, 'בהמות', 'beasts', 0, 'livestock'), (22, 'תחתית', 'the-lowest', 0, 'lowermost'), (7, 'זכר', 'remember', 0, 'mark'), (39, 'ארפא', 'I-heal', 0, 'mend'), (25, 'תשכל', 'shall-bereave', 0, 'miscarry'), (35, 'עתדת', 'the-things-to-come', 0, 'prepared'), (13, 'תנובת', 'the-fruits-of', 0, 'produce'), (51, 'מריבת', 'Meribath', 0, 'quarrel'), (14, 'כרים', 'lambs', 0, 'ram'),
 (9, 'חבל', 'the-lot-of', 0, 'rope'), (51, 'קדשתם', 'you-sanctified', 0, 'sanctify'), (12, 'בדד', 'alone', 0, 'separate'), (15, 'שמנת', 'you-grew-fat', 0, 'shine'), (36, 'יתנחם', 'repent-Himself', 0, 'sigh'), (9, 'חלק', 'the-portion-of', 0, 'smoothness'), (25, 'יונק', 'the-suckling', 0, 'suck'), (35, 'תמוט', 'shall-slip', 0, 'waver'),
 (23, 'רעות', 'evils', 0, 'bad'), (7, 'עולם', 'of-old', 0, 'forever'), (40, 'חי', 'live', 0, 'living'), (20, 'אסתירה', 'I-will-hide', 0, 'hide'), (24, 'אשלח', 'I-will-send', 0, 'send'), (41, 'אשיב', 'I-will-render', 0, 'return'), (43, 'ישיב', 'He-will-render', 0, 'return'), (38, 'יקומו', 'let-them-rise-up', 0, 'arise'), (48, 'בעצם', 'in-the-selfsame', 0, 'in-bone')]
bad = [(v, tok, nth, sg(v, tok, nth), old) for v, tok, new, nth, old in SPEC if sg(v, tok, nth) != old]; assert not bad, bad   # the old gloss at the seat as read
REF3 = [(f'Deut.32.{v}:{sidx(v, tok, nth)}', new, tok) for v, tok, new, nth, old in SPEC]
REF = [(k, v) for k, v, _ in REF3]; TOK = {k: t_ for k, _, t_ in REF3}
assert len(REF) == len({k for k, _ in REF}) == len(SPEC) and len(GL) == len({g for g, _ in GL})
assert all(sg(v, tok, nth) != new for v, tok, new, nth, old in SPEC)   # no row rewrites a gloss to itself
CLASH = [(v, tok, old) for v, tok, _, nth, old in SPEC if old in dict(GL)]; assert not CLASH, CLASH   # a seat patched by gloss is not patched again by reference
GLSEATS = {g: [(v, i, hp) for v, L in SG.items() for i, hp, gg in L if gg == g] for g, _ in GL}; NOSEAT = [g for g, s in GLSEATS.items() if not s]; assert not NOSEAT, NOSEAT   # every by-gloss row has a seat in the chapter
assert not re.search(r'"Deut\.32\.', t) and all(g not in BG0 for g, _ in GL)
MARK = 'THE DEUTERONOMY WALK sitting 20 (2026-09-28, Deuteronomy 32, LEAN)'
assert MARK not in t
M19 = 'THE DEUTERONOMY WALK sitting 19 (2026-09-27, Deuteronomy 29-31, LEAN)'
i = t.index(f'  # {M19}: the worst glosses of the three chapters\' seats')
j = t.index('\n', i) + 1
rows = []
while True:
    m = re.match(r'  "[^"]+": "[^"]*"[^\n]*\n', t[j:])
    if not m: break
    rows.append(m.group(0)); j += len(m.group(0))
assert len(rows) == 78, len(rows)   # sitting 19's by-gloss rows (the probe's walk 78)
A1 = rows[-1]; assert t.count(A1) == 1
gl_block = A1 + f'\n  # {MARK}: the worst glosses of the song\'s seats, the families probed in the store first (ch32_patch_probe.py) — the lean form\'s patch; the rest OWED (COMPILE_DEBT\'s lean-pass box)\n' + ''.join(f'  "{k}": "{v}"\n' for k, v in GL)
t = t.replace(A1, gl_block)
m2 = re.search(r'^  "Deut\.31\.19:1": "write"[^\n]*\n', t, re.M); assert m2 and t.count('"Deut.31.19:1": "write"') == 1
A2 = m2.group(0)
ref_block = A2 + f'  # {MARK}: the chapter\'s seats by reference — the token named beside each; the indices the store\'s own (the seven "?" seats of the pronoun I read "I"; the song\'s homographs by their seat — the Rock and the rock, God and a no-god, the Most High and the high places with the ketiv and the qere both tokens at 32:13, the wilderness; the old gloss asserted at every seat)\n' + ''.join(f'  "{k}": "{v}"   # {TOK[k]}\n' for k, v in REF)
t = t.replace(A2, ref_block)
open(P, 'w', encoding='utf-8').write(t)
d = yaml.safe_load(open(P, encoding='utf-8'))
assert all(d['by_ref'][k] == v for k, v in REF) and all(d['by_gloss'][k] == v for k, v in GL)
print('override rows written: by_ref', len(REF), 'by_gloss', len(GL), '| by_ref total', len(d['by_ref']), '| by_gloss total', len(d['by_gloss']), '| dropped (already by gloss)', len(DROP), '| the seven I seats', len(ANOKHI), '| the homograph seats by reference', sum(1 for _, _, _, _, old in SPEC if old in ('cliff', 'the-cliff', 'strength', 'deity', 'elevation', 'pasture')), '| by-gloss seats in the chapter', sum(len(s) for s in GLSEATS.values()))
