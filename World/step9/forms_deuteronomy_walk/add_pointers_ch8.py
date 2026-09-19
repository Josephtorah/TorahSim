import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 6b (2026-09-19): the disposition the dependency gate demanded after the runner existed (gates_ch8b/dependency.out, the first chain —
# ONE demand: a POINTER at Deut 8:5 in the AS_WHEN form ("as a man disciplines his son"): the token census reads the 'as' (כאשר, "as / when") as a citation form
# and asks its disposition — RUN_CITATION: 8:5 cites 1:31's "as a man carries his son" (the readback row 8:5 VARIANT — carried made disciplined; the kin's cell
# opening_speech.the_spies_read_back('the_carrying') CALLED) and the discipline's row on the shelf (Berakhot 5a:22 — the Land through suffering: 8:5 then 8:7);
# no ledger write pays it (R5), the frame writes nothing (R6); the register gate lists no seat (its finder scans 'commanded', not 'disciplines'). NO EDGE
# demanded (the design's thirteen CALL edges the census's own). Inserted after the last pointer row; the yaml parsed before it is trusted. Idempotent.
# add_pointers_ch7.py's form (there an edge, here a pointer — 4b's form for the AS_WHEN pointers).
import subprocess, yaml, sqlite3, re
ROOT = _ROOT
db = sqlite3.connect(f"file:{ROOT}/Data/tanakh.sqlite?mode=ro", uri=True)
pl = lambda w: ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
row = [pl(he) for he, in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=8 AND v.verse=5 ORDER BY w.idx")]
assert row[:6] == ['וידעת', 'עם', 'לבבך', 'כי', 'כאשר', 'ייסר'] and row[6:9] == ['איש', 'את', 'בנו'], row   # 'and you shall know with your heart that AS a man disciplines his son' — the demanded tokens on the DB
row131 = [pl(he) for he, in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=1 AND v.verse=31 ORDER BY w.idx")]
assert 'כאשר' in row131 and row131[row131.index('כאשר') + 1:row131.index('כאשר') + 4] == ['ישא', 'איש', 'את'], row131   # 1:31 'AS a man carries his son' — the citation's seat
P = ROOT + '/World/step9/dependency_dispositions.yaml'
s = open(P, encoding='utf-8').read()
W = 'THE DEUTERONOMY WALK 6b (2026-09-19) | '
NEW = '  - {verse: "Deut 8:5", form: AS_WHEN, runner: good_land, disposition: RUN_CITATION, link: reference, why: "' + W + "'and you shall know with your heart that AS A MAN DISCIPLINES HIS SON, so the LORD your God disciplines you' (כַּאֲשֶׁר יְיַסֵּר אִישׁ — as a man disciplines) — the readback row 8:5 VARIANT: 1:31's 'AS A MAN CARRIES HIS SON' (the same three tokens 'a man … his son'; the form's three Bible seats with 2 Kings 23:10) made the discipline — a RUN CITATION of the first form's row (opening_speech.the_spies_read_back('the_carrying') CALLED by F2 the_discipline) and of the shelf's row Berakhot 5a:22 (the Land through suffering — 8:5 then 8:7); Onkelos 'as a man TEACHES his son'; the frame writes nothing (R6); no ledger write pays a citation (R5); the register gate lists no seat (its finder scans 'commanded', not 'disciplines'); the census's one demand this sitting — no edge demanded, the design's thirteen CALL edges the census's own\"}\n"
if 'runner: good_land, disposition: RUN_CITATION' not in s:
    ptr_i = s.index('\npointers:\n')
    last = max(m.end() for m in re.finditer(r'^  - \{verse: .*\}\n', s[ptr_i:], re.M))
    s = s[:ptr_i + last] + NEW + s[ptr_i + last:]
    open(P, 'w', encoding='utf-8').write(s)
d = yaml.safe_load(open(P, encoding='utf-8'))
mine = [p for p in d['pointers'] if p.get('runner') == 'good_land']
assert len(mine) == 1 and mine[0]['verse'] == 'Deut 8:5' and mine[0]['disposition'] == 'RUN_CITATION', mine
n_edges = sum(1 for e in d['edges'] if e['from'] == 'good_land')
assert n_edges == 13, n_edges
print('pointers for good_land 1 (Deut 8:5 AS_WHEN — RUN_CITATION of 1:31 by the readback row); edges 13 CALL (none demanded); the yaml parses; pointers on file %d, edges %d' % (len(d['pointers']), len(d['edges'])))
