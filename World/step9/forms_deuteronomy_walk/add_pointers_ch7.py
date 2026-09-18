#!/usr/bin/env python3
import os as _os, subprocess as _sp
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK 5b (2026-09-18): the dispositions the dependency gate demanded after the runner existed (gates_ch7b/dependency.out — ONE demand:
# an EDGE seven_nations -> sanctions [molech_ov] at Deut 7:8 — the token census matched 'king' in "Pharaoh KING of Egypt" (7:8) to the sanctions span's
# Molech (Leviticus 20:2-5 — the same consonants): A HOMOGRAPH, dispositioned FALSE with its why, the lemmas checked on the DB; NO POINTER demanded —
# the design's (n) predicted RUN_CITATION pointers at 7:6, 7:8, 7:12, 7:13, 7:18, 7:19, 7:22 and the census demanded none: the citations ride the CALL
# edges' whys (4b's lesson again — the design's pointer list is a prediction, the census decides). Inserted after the registration edge; the yaml parsed
# before it is trusted. Idempotent. add_pointers_ch6.py's form.
import subprocess, yaml, sqlite3
ROOT = _ROOT
db = sqlite3.connect(f"file:{ROOT}/Data/tanakh.sqlite?mode=ro", uri=True)
pl = lambda w: ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
row = [(pl(he), (lem or '').split('/')[-1].strip()) for he, lem in db.execute("SELECT w.he, w.lemma FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=7 AND v.verse=8 ORDER BY w.idx")]
king = [(t, l) for t, l in row if t == 'מלך']; assert king == [('מלך', '4428')], (king, row)   # 'king' (the lemma 4428), not Molech (4432)
molech = [l for he, lem in db.execute("SELECT w.he, w.lemma FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Lev' AND v.chapter=20 AND v.verse=2 ORDER BY w.idx") for l in [(lem or '').split('/')[-1].strip()] if pl(he) == 'למלך']
assert molech == ['4432'], molech
P = ROOT + '/World/step9/dependency_dispositions.yaml'
s = open(P, encoding='utf-8').read()
W = 'THE DEUTERONOMY WALK 5b (2026-09-18) | '
if '{from: seven_nations, to: sanctions, disposition: FALSE' not in s:
    a = "  - {from: sequence, to: seven_nations, disposition: CALL, link: none,"
    i = s.index(a); j = s.index('\n', s.index('why:', i)) + 1
    s = s[:j] + '  - {from: seven_nations, to: sanctions, disposition: FALSE, link: none,\n     why: "' + W + "7:8's 'from the hand of Pharaoh KING of Egypt' — the token census matches the king-word (the lemma 4428, 'king') to the sanctions span's Molech (Leviticus 20:2-5 'who gives of his seed to Molech' — the lemma 4432, the same consonants): A HOMOGRAPH, named; the verse is the going out read back (brought_out at 12:51 — the readback row 7:8 EXPANDED), Pharaoh's title at its one seat in the chapter; no call; the design's (n) RUN_CITATION pointers (7:6, 7:8, 7:12, 7:13, 7:18, 7:19, 7:22) were NOT demanded — the citations ride the CALL edges' whys (exodus_story, mamre, joseph, ordinances)\"}\n" + s[j:]
open(P, 'w', encoding='utf-8').write(s)
d = yaml.safe_load(open(P, encoding='utf-8'))
mine = [p for p in d['pointers'] if p.get('runner') == 'seven_nations']
assert mine == [], mine   # no pointer demanded
n_edges = sum(1 for e in d['edges'] if e['from'] == 'seven_nations')
assert n_edges == 14 and any(e['from'] == 'seven_nations' and e['to'] == 'sanctions' and str(e['disposition']).upper() == 'FALSE' for e in d['edges']), n_edges
print('edges: %d for seven_nations (13 CALL + the FALSE edge to sanctions at 7:8 — the king/Molech homograph); pointers for seven_nations 0 (none demanded); the yaml parses; pointers on file %d, edges %d' % (n_edges, len(d['pointers']), len(d['edges'])))
