import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# DEUTERONOMY chapters 1-3: THE PARSER MEASURED ON EVERY VERSE before any claim (the standing rule) — cold_run_sequence.verse_words' marks,
# ink_numbers, ink_ordinals; plus the case tokens, the divine frames, the name tokens and the narrative verbs per verse.
import sys, io, os, re, contextlib, sqlite3, subprocess
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
print('VC Deut:', VC, 'total', sum(VC.values()))
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
rows = db.execute("SELECT v.chapter, v.verse, w.he, w.morph, w.lemma FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter IN (1,2,3) ORDER BY v.id, w.idx").fetchall()
by = {}
for c, v, he, m, lem in rows: by.setdefault((c, v), []).append((plain(he), m, he, lem))
print('---- THE PARSER (numbers | ordinals | marked tokens) on every verse of 1-3 that carries any')
for c in (1, 2, 3):
    for v in range(1, VC[c] + 1):
        vw = CS.verse_words('Deut', c, v)
        marked = [t for t in vw if t[-1] in '#~^%@|*']
        n, o = CS.ink_numbers(vw), CS.ink_ordinals(vw)
        if n or o or marked: print(f'  {c}:{v:<3} N {n!s:<24} O {o!s:<14} marked {marked}')
for c, v in ((1, 2), (1, 3), (1, 11), (1, 15), (1, 23), (2, 7), (2, 14), (3, 4), (3, 11), (3, 13), (3, 14)):
    print(f'  {c}:{v} tokens:', CS.verse_words('Deut', c, v))
print('---- CASE TOKENS per verse (כי / אם / ואם / או / פן)')
print({f'{c}:{v}': [x for x, m, _, _ in by[(c, v)] if x in ('כי', 'אם', 'ואם', 'או', 'פן')] for c in (1, 2, 3) for v in range(1, VC[c] + 1) if any(x in ('כי', 'אם', 'ואם', 'או', 'פן') for x, m, _, _ in by[(c, v)])})
print('---- DIVINE FRAMES (ויאמר/וידבר + יהוה) and SPEECH FRAMES (ואמר / ויאמר / לאמר) per verse')
print('  divine:', [f'{c}:{v}' for c in (1, 2, 3) for v in range(1, VC[c] + 1) for i, (x, _, _, _) in enumerate(by[(c, v)][:-1]) if x in ('ויאמר', 'וידבר') and by[(c, v)][i + 1][0] == 'יהוה'])
print('  לאמר seats:', [f'{c}:{v}' for c in (1, 2, 3) for v in range(1, VC[c] + 1) if any(x == 'לאמר' for x, _, _, _ in by[(c, v)])])
print('---- NARRATIVE-FORM VERBS (V.w) per verse — the wayyiqtol test off the morphology; and the first-person forms')
for c in (1, 2, 3):
    print(f'  ch {c}:', {v: [x for x, m, _, _ in by[(c, v)] if m and re.search(r'V.w', m)] for v in range(1, VC[c] + 1) if any(m and re.search(r'V.w', m) for _, m, _, _ in by[(c, v)])})
print('---- NAME TOKENS per verse (morph Np)')
for c in (1, 2, 3):
    print(f'  ch {c}:', {v: [x for x, m, _, _ in by[(c, v)] if m and 'Np' in m] for v in range(1, VC[c] + 1) if any(m and 'Np' in m for _, m, _, _ in by[(c, v)])})
print('---- token counts per chapter:', {c: sum(len(by[(c, v)]) for v in range(1, VC[c] + 1)) for c in (1, 2, 3)})
