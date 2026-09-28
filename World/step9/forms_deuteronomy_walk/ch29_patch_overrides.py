import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 19 — CHAPTERS 29-31 (LEAN, 2026-09-27; THE TAIL): the store's glosses at the three chapters' seats read back into the display layer's
# override file — BY GLOSS where the store's every token of the gloss is the one word or one family read the same at every seat (the families PROBED FIRST by
# ch29_patch_probe.py, the counts read from its print; the glosses the earlier walks already rewrote by gloss DROPPED here with a print), BY REFERENCE at the chapters'
# own seats where the family is mixed (the eight "?" seats of the pronoun I among them — "?" is by gloss to a blank from an earlier walk, "and-?" to "and-I", so the two
# prefixed seats 31:18 and 31:23 are covered already; "the oath" and "the curse" for the one Hebrew word at four seats; "be strong" at three). THE LEAN FORM: the worst
# glosses only; the rest OWED. Display only; the frozen units untouched. Run ONCE (the anchors assert the rows absent first). Sitting 18's form (ch26_patch_overrides.py):
# the anchors the LAST ROWS of sitting 18's two blocks — the by_gloss block's last row found by walking from sitting 18's marker (never typed), the by_ref block's last
# row 28:68's. Every by-reference row carries the OLD gloss and asserts it at the seat (this sitting's addition — the one Hebrew word "ha-alah" is "these" elsewhere).
# The simple one-word glosses ("nose", "box", "cremation" …) are patched at EVERY seat of the token in the three chapters by computation (GEN), the seats never typed.
# RUN FROM THE REPO ROOT; after the freeze chain.
import re, sqlite3, subprocess, yaml
ROOT = _ROOT
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, i, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (29, 30, 31) ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((i, hp.replace('/', ''), g))
def sg(c, v, tok, nth=0):
    hit = [g for _, hp, g in SG[(c, v)] if hp == tok]; assert len(hit) > nth, (c, v, tok, nth, hit); return hit[nth]
def sidx(c, v, tok, nth=0):
    hit = [i for i, hp, _ in SG[(c, v)] if hp == tok]; assert len(hit) > nth, (c, v, tok, nth, hit); return hit[nth]
GL0 = [('and-broadness.-i.e.--the-ear', 'and-ears'), ('in-broadness.-i.e.--the-ear', 'in-the-ears-of'), ('in-broadness.-i.e.--the-ear-them/their', 'in-their-ears'), ('and-be--make-well-you/your', 'and-do-you-good'), ('and-be-alert', 'and-be-of-good-courage'), ('and-be-fat', 'and-grown-fat'), ('and-break-up', 'and-break'), ('and-in-splinter', 'and-in-great-indignation'), ('and-intoxicant', 'and-strong-drink'), ('and-loosen-me/my', 'and-forsake-Me'), ('and-loosen-them/their', 'and-I-will-forsake-them'), ('loosen-you/your', 'forsake-you'), ('and-powder', 'and-salt'), ('and-sandal-tongue-you/your', 'and-your-sandal'), ('and-scorn-me/my', 'and-spurn-Me'), ('and-scribe-you/your (pl)', 'and-your-officers'), ('and-the-denude', 'and-the-revealed-things'), ('and-tear-away-them/their', 'and-He-plucked-them-up'), ('and-tightness', 'and-troubles'), ('burning--anger', 'the-heat-of'), ('cypress-resin', 'brimstone'), ('dash-in-pieces-you/your', 'has-scattered-you'), ('disgusting-them/their', 'their-detestable-things'), ('exile-you/your', 'your-captivity'), ('from-chop', 'from-the-hewer-of'), ('in-non-occurrence', 'before'), ('in-obstinacy', 'in-the-stubbornness-of'), ('in-still/again-me/my', 'while-I-am-yet'), ('like-destruction', 'like-the-overthrow-of'), ('log-them/their', 'their-idols'), ('malady-her/its', 'its-sicknesses'), ('nape-you/your', 'your-neck'), ('poisonous-plant', 'gall'), ('run-after--gone-by)-you/your', 'who-persecuted-you'), ('the-hide', 'the-hidden-things'), ('and-in-imprecation-him/its', 'and-into-His-oath'), ('the-sated', 'the-watered'), ('to-concretely', 'for-a-witness'), ('to-be-bright', 'to-rejoice'), ('to-encountering-us/our', 'to-meet-us'), ('to-grave', 'to-write'), ('from-side', 'at-the-side-of'), ('in-column', 'in-a-pillar-of'), ('and-the-strange', 'and-the-foreigner'), ('in-seasons', 'at-the-appointed-time-of'), ('in-festival', 'at-the-feast-of'), ('and-in-heat', 'and-in-fury'), ('and-in-heat-him/its', 'and-in-His-wrath'), ('in-nose', 'in-anger'), ('nose-me/my', 'My-anger'), ('and-jealousy-him/its', 'and-His-jealousy'), ('and-grasp-you/your', 'and-gather-you'), ('grasp-you/your', 'will-He-gather-you'), ('and-possess/inherit-her/its', 'and-you-shall-possess-it'), ('and-Jehoshua', 'and-Joshua'), ('to-Jehoshua', 'to-Joshua'), ('the-Menashshite', 'the-Manassite'), ('in-alive', 'life'), ('the-alive', 'life'), ('the-death', 'death'), ('and-the-death', 'and-death'), ('family-you/your (pl)', 'your-little-ones'), ('dress-you/your (pl)', 'your-garments'), ('to-pass-over-you/your', 'that-you-should-enter'), ('there-is-him/its', 'who-is-here'), ('the-they', 'those'), ('and-divide-him/its', 'and-shall-separate-him'), ('and-come/bring-you/your', 'and-bring-you'), ('belly-you/your', 'your-body'), ('and-length', 'and-the-length-of'), ('from-face-them/their', 'from-before-them'), ('in-tent', 'in-the-tent'), ('behold-you/your', 'behold-you'), ('in-nearest-part-me/my', 'in-my-midst'), ('in-nearest-part-him/its', 'in-its-midst'), ('put/set-her/its', 'put-it'), ('form-him/its', 'his-inclination'), ('and-hear-us/our', 'and-make-us-hear-it')]
P = f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'
t = open(P, encoding='utf-8').read()
d0 = yaml.safe_load(t); BG0 = d0['by_gloss']
DROP = [g for g, _ in GL0 if g in BG0]; GL = [(g, n) for g, n in GL0 if g not in BG0]
print('by-gloss candidates already rewritten by an earlier walk (dropped):', DROP)
ANOKHI = [(29, 5, 'אני', 'I', 0, '?'), (29, 13, 'אנכי', 'I', 0, '?'), (30, 2, 'אנכי', 'I', 0, '?'), (30, 8, 'אנכי', 'I', 0, '?'), (30, 11, 'אנכי', 'I', 0, '?'), (30, 16, 'אנכי', 'I', 0, '?'), (31, 2, 'אנכי', 'I', 0, '?'), (31, 27, 'אנכי', 'I', 0, '?')]
SPEC = ANOKHI + [
 (31, 16, 'וזנה', 'and-shall-go-whoring', 0, 'and-commit-adultery'), (29, 19, 'ורבצה', 'and-shall-lie-upon', 0, 'and-crouch'), (31, 28, 'ואעידה', 'and-I-will-call-to-witness', 0, 'and-duplicate'),
 (31, 13, 'ולמדו', 'and-they-shall-learn', 0, 'and-goad'), (31, 19, 'ולמדה', 'and-teach-it', 0, 'and-goad-her/its'), (31, 22, 'וילמדה', 'and-taught-it', 0, 'and-goad-her/its'),
 (29, 3, 'ועינים', 'and-eyes', 0, 'and-eye'), (31, 21, 'וענתה', 'and-shall-testify', 0, 'and-eye'),
 (30, 17, 'ונדחת', 'and-you-are-drawn-away', 0, 'and-push-off'), (30, 1, 'הדיחך', 'has-driven-you', 0, 'push-off-you/your'), (30, 4, 'נדחך', 'your-outcasts', 0, 'push-off-you/your'),
 (29, 19, 'ומחה', 'and-shall-blot-out', 0, 'and-stroke'), (29, 27, 'וישלכם', 'and-cast-them', 0, 'and-throw-out-them/their'), (29, 10, 'שאב', 'the-drawer-of', 0, 'bale-up-water'),
 (31, 27, 'ממרים', 'rebellious', 0, 'be--bitter'), (29, 8, 'תשכילו', 'you-may-prosper', 0, 'be--circumspect-and-hence'), (29, 21, 'חלה', 'has-laid-upon', 0, 'be-rubbed'), (29, 25, 'חלק', 'had-allotted', 0, 'be-smooth'),
 (31, 6, 'חזקו', 'be-strong', 0, 'fasten-upon'), (31, 7, 'חזק', 'be-strong', 0, 'fasten-upon'), (31, 23, 'חזק', 'be-strong', 0, 'fasten-upon'),
 (31, 10, 'מקץ', 'at-the-end-of', 0, 'from-extremity'), (30, 4, 'בקצה', 'at-the-end-of', 0, 'in-extremity'),
 (31, 25, 'נשאי', 'who-carried', 0, 'lift/carry'), (31, 9, 'הנשאים', 'who-carried', 0, 'the-lift/carry'), (30, 11, 'נפלאת', 'too-hard', 0, 'perhaps-to-separate'), (29, 18, 'ספות', 'to-add', 0, 'scrape--together'),
 (29, 13, 'האלה', 'the-oath', 0, 'the-imprecation'), (29, 18, 'האלה', 'the-oath', 0, 'the-imprecation'), (29, 19, 'האלה', 'the-curse', 0, 'the-imprecation'), (30, 7, 'האלות', 'the-curses', 0, 'the-imprecation'),
 (31, 27, 'הקשה', 'the-stiff', 0, 'the-severe'), (29, 26, 'הקללה', 'the-curse', 0, 'the-vilification'), (29, 22, 'הפך', 'overthrew', 0, 'turn-about'), (29, 22, 'תזרע', 'sown', 0, 'yield-seed'),
 (29, 2, 'והמפתים', 'and-the-wonders', 0, 'and-the-miracle'), (29, 21, 'האחרון', 'the-later', 0, 'the-hinder'), (29, 17, 'פרה', 'bearing', 0, 'be-fruitful'), (29, 22, 'באפו', 'in-His-anger', 0, 'in-nose-him/its'),
 (31, 17, 'והסתרתי', 'and-I-will-hide', 0, 'and-hide'), (31, 17, 'ומצאהו', 'and-shall-befall-him', 0, 'and-find-him/its'), (31, 17, 'מצאוני', 'have-befallen-me', 0, 'find-me/my'), (31, 29, 'וקראת', 'and-shall-befall', 0, 'and-encounter'),
 (31, 16, 'וקם', 'and-will-rise-up', 0, 'and-arise'), (31, 14, 'ואצונו', 'and-I-will-commission-him', 0, 'and-command-him/its'), (31, 14, 'והתיצבו', 'and-present-yourselves', 0, 'and-place'), (31, 14, 'ויתיצבו', 'and-they-presented-themselves', 0, 'and-place'), (31, 14, 'קרבו', 'draw-near', 0, 'bring-near'),
 (31, 20, 'ופנה', 'and-they-shall-turn', 0, 'and-turn'), (29, 6, 'ונכם', 'and-we-smote-them', 0, 'and-strike-them/their'), (29, 18, 'והתברך', 'and-he-blesses-himself', 0, 'and-bless'), (31, 3, 'וירשתם', 'and-you-shall-dispossess-them', 0, 'and-possess/inherit-them/their'),
 (30, 1, 'הברכה', 'the-blessing', 0, 'the-benediction'), (30, 19, 'הברכה', 'the-blessing', 0, 'the-benediction'),
 (30, 15, 'הרע', 'the-evil', 0, 'the-bad'), (31, 17, 'הרעות', 'the-evils', 0, 'the-bad'), (31, 18, 'הרעה', 'the-evil', 0, 'the-bad'), (31, 29, 'הרעה', 'the-evil', 0, 'the-bad'),
 (31, 9, 'הכהנים', 'the-priests', 0, 'the-priest'), (31, 12, 'האנשים', 'the-men', 0, 'the-man'), (31, 12, 'והנשים', 'and-the-women', 0, 'and-the-woman'),
 (29, 18, 'בשמעו', 'when-he-hears', 0, 'in-hear-him/its'), (29, 20, 'לרעה', 'for-evil', 0, 'to-bad'), (30, 7, 'שנאיך', 'who-hate-you', 0, 'hate-you/your'),
 (31, 2, 'אוכל', 'I-am-able', 0, 'be-able'), (31, 2, 'לצאת', 'to-go-out', 0, 'to-bring-forth'), (31, 6, 'ההלך', 'who-goes', 0, 'the-walk/go'), (31, 8, 'ההלך', 'who-goes', 0, 'the-walk/go'), (31, 11, 'בבוא', 'when-comes', 0, 'in-come/bring'),
 (31, 16, 'שכב', 'lie', 0, 'lie-down'), (31, 20, 'אביאנו', 'I-bring-him', 0, 'come/bring-him/its'), (31, 21, 'אביאנו', 'I-bring-him', 0, 'come/bring-him/its'),
 (30, 12, 'ונעשנה', 'and-do-it', 0, 'and-make-her/its'), (30, 13, 'ונעשנה', 'and-do-it', 0, 'and-make-her/its'), (30, 12, 'ויקחה', 'and-take-it-for-us', 0, 'and-take-her/its'), (30, 13, 'ויקחה', 'and-take-it-for-us', 0, 'and-take-her/its')]
GEN = [('nose', 'אף', 'the-anger-of'), ('cremation', 'שרפה', 'a-burning'), ('loosen', 'עזבו', 'they-forsook'), ('box', 'ארון', 'the-ark-of'), ('wound', 'מכות', 'the-plagues-of'), ('scion', 'שבט', 'tribe'), ('scion', 'שבטי', 'the-tribes-of'), ('assemblage', 'קהל', 'the-assembly-of'), ('opening', 'פתח', 'the-door-of'), ('remote', 'רחקה', 'far'), ('smoke', 'יעשן', 'shall-smoke'), ('find', 'תמצאן', 'shall-befall'), ('imprecation', 'אלות', 'the-curses-of'), ('cut', 'כרת', 'made'), ('front', 'נגד', 'before'), ('food', 'לחם', 'bread'), ('root', 'שרש', 'a-root'), ('old', 'זקני', 'the-elders-of'), ('bad', 'רעות', 'evils'), ('column', 'עמוד', 'a-pillar-of'), ('grave', 'כתבו', 'write')]
GENROWS = []
for g, tok, new in GEN:
    hits = [(c, v, i) for (c, v), L in SG.items() for i, hp, gg in L if hp == tok and gg == g]
    print(f'  GEN {g!r} {tok} -> {new!r}: {len(hits)} seats {hits}')
    GENROWS += [(f'Deut.{c}.{v}:{i}', new, tok) for c, v, i in hits]
assert all(sg(c, v, tok, nth) == old for c, v, tok, new, nth, old in SPEC), [(c, v, tok, sg(c, v, tok, nth), old) for c, v, tok, new, nth, old in SPEC if sg(c, v, tok, nth) != old]   # the old gloss at the seat as read
REF3 = [(f'Deut.{c}.{v}:{sidx(c, v, tok, nth)}', new, tok) for c, v, tok, new, nth, old in SPEC] + GENROWS
REF = [(k, v) for k, v, _ in REF3]; TOK = {k: t_ for k, _, t_ in REF3}
assert len(REF) == len({k for k, _ in REF}) == len(SPEC) + len(GENROWS) and len(GL) == len({g for g, _ in GL})
assert all(sg(c, v, tok, nth) != new for c, v, tok, new, nth, old in SPEC)   # no row rewrites a gloss to itself
CLASH = [(c, v, tok, old) for c, v, tok, _, nth, old in SPEC if old in dict(GL)] + [(g, tok) for g, tok, _ in GEN if g in dict(GL)]; assert not CLASH, CLASH   # a seat patched by gloss is not patched again by reference
assert not re.search(r'"Deut\.(29|30|31)\.', t) and all(g not in BG0 for g, _ in GL)
MARK = 'THE DEUTERONOMY WALK sitting 19 (2026-09-27, Deuteronomy 29-31, LEAN)'
assert MARK not in t
M18 = 'THE DEUTERONOMY WALK sitting 18 (2026-09-26, Deuteronomy 26-28, LEAN)'
i = t.index(f'  # {M18}: the worst glosses of the three chapters\' seats')
j = t.index('\n', i) + 1
rows = []
while True:
    m = re.match(r'  "[^"]+": "[^"]*"[^\n]*\n', t[j:])
    if not m: break
    rows.append(m.group(0)); j += len(m.group(0))
assert len(rows) == 104, len(rows)   # sitting 18's by-gloss rows (the probe's walk 104)
A1 = rows[-1]; assert t.count(A1) == 1
gl_block = A1 + f'\n  # {MARK}: the worst glosses of the three chapters\' seats, the families probed in the store first (ch29_patch_probe.py) — the lean form\'s patch; the rest OWED (COMPILE_DEBT\'s lean-pass box)\n' + ''.join(f'  "{k}": "{v}"\n' for k, v in GL)
t = t.replace(A1, gl_block)
m2 = re.search(r'^  "Deut\.28\.68:18": "a-buyer"[^\n]*\n', t, re.M); assert m2 and t.count('"Deut.28.68:18": "a-buyer"') == 1
A2 = m2.group(0)
ref_block = A2 + f'  # {MARK}: the three chapters\' seats by reference — the token named beside each; the indices the store\'s own (the eight "?" seats of the pronoun I read "I"; "the oath" and "the curse" for the one word ha-alah at four seats; "be strong" at three; the one-word glosses at every seat of their token in the three chapters, computed)\n' + ''.join(f'  "{k}": "{v}"   # {TOK[k]}\n' for k, v in REF)
t = t.replace(A2, ref_block)
open(P, 'w', encoding='utf-8').write(t)
d = yaml.safe_load(open(P, encoding='utf-8'))
assert all(d['by_ref'][k] == v for k, v in REF) and all(d['by_gloss'][k] == v for k, v in GL)
print('override rows written: by_ref', len(REF), 'by_gloss', len(GL), '| by_ref total', len(d['by_ref']), '| by_gloss total', len(d['by_gloss']), '| dropped (already by gloss)', len(DROP), '| the eight I seats', len(ANOKHI), '| the one-word seats computed', len(GENROWS))
