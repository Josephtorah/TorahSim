import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 2b (2026-09-16): THE PROBES TO FAIL — readback_probes.py gains Q7-Q9 (chapter 4's readback rows, the two supplied
# Horeb lines dated by the retrograde markers, the register seats and the refuge debit after the three cities) and Q4 narrows to the opening
# speech's stretch (chapters 1-3 — the probe tests 1b's form, not the tape's length); checkpoint_probes.py's "beyond the tape" verse COMPUTED
# from the tape (lesson xiii's second half). Every replacement anchored on the exact prior text; both files asserted to compile after.
import re, subprocess, py_compile
ROOT = _ROOT
def rep(s, old, new, n=1):
    assert s.count(old) == n, (s.count(old), old[:80]); return s.replace(old, new)
W = 'THE DEUTERONOMY WALK 2b (2026-09-16)'
# ---- readback_probes.py ----
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
s = rep(s, "  Q6 the register gate's seats on the new tape — Deut 1:3 ACT, 1:19 CHAPTER, 1:41 CHAPTER (the gate's class for a receipt whose chapter holds a closed entry — read at the first run; the design said NONE), Deut 4:45 DAEMONS, Num 27:22 CLOSE\n",
        "  Q6 the register gate's seats on the new tape — Deut 1:3 ACT, 1:19 CHAPTER, 1:41 CHAPTER (the gate's class for a receipt whose chapter holds a closed entry — read at the first run; the design said NONE), Deut 4:45 DAEMONS, Num 27:22 CLOSE\n"
        "  THE DEUTERONOMY WALK 2b (2026-09-16; DEUTERONOMY_WALK.md \"Sitting 2b\" THE PROBES) — written to FAIL before cold_run_obey_horeb.py exists:\n"
        "  Q7 the runner and its the_readback table: eleven rows (SHORTENED 3, EXPANDED 5, SUPPLIED 2, DISAGREES 1), the two SUPPLIED rows naming their first tellings Exod 20:1 and 31:18 (THE TAPE'S HOLE)\n"
        "  Q8 the two supplied Horeb lines DATED by the retrograde markers at Deut 4:10 and 4:13 — (1, 3, 7) the giving, (1, 4, 17) the tablets; the tablets' day = the breaking marker's (Exod 32:19)\n"
        "  Q9 the register seats after chapter 4 — Deut 4:5 ACT, Deut 4:45 DAEMONS with daemons 2; the refuge debit appoint_six_cities_of_refuge OPEN after the three cities' line (Makkot 2:4); cities_set_apart on Israel ONE\n"
        "  (Q4 NARROWED at 2b to chapters 1-3's lines and markers — the probe tests 1b's form, not the tape's length)\n")
s = rep(s, "    lines = [e for e in EV if str(e[2].get('case_source', '')).startswith('Deut ')]\n    dated = [e for e in lines if e[2].get('dated') is not None]\n    mk = [l for l in W.log if l[0] == 'MARKER' and str(l[2].get('verse', '')).startswith('Deut ') and l[2].get('retrograde')]",
        "    lines = [e for e in EV if re.match(r'Deut [123]:', str(e[2].get('case_source', '')))]   # %s: chapters 1-3 only (the probe tests 1b's form)\n    dated = [e for e in lines if e[2].get('dated') is not None]\n    mk = [l for l in W.log if l[0] == 'MARKER' and re.match(r'Deut [123]:', str(l[2].get('verse', ''))) and l[2].get('retrograde')]" % W)
Q = '''def q7():
    import cold_run_obey_horeb as OH
    rows = OH.DATA['the_readback']['value']
    gs = collections.Counter(r['grade'] for r in rows)
    sup = [r for r in rows if r['grade'] == 'SUPPLIED']
    named = sum(1 for r in sup if 'Exod 20:1' in str(r.get('entry', '')) + str(r.get('why', ''))) + sum(1 for r in sup if 'Exod 31:18' in str(r.get('entry', '')) + str(r.get('why', '')))
    return len(rows) == 11 and gs == collections.Counter({'EXPANDED': 5, 'SHORTENED': 3, 'SUPPLIED': 2, 'DISAGREES': 1}) and named == 2, 'rows %d, grades %s, the first tellings named %d' % (len(rows), dict(gs), named)
def q8():
    tw = [e for e in EV if e[2]['kind'] == 'ten_words_declared']; tb = [e for e in EV if e[2]['kind'] == 'tablets_given']
    mk = {str(l[2].get('verse', '')): l for l in W.log if l[0] == 'MARKER'}
    d_tw = ex.date(tw[0][2]['dated']) if tw and tw[0][2].get('dated') is not None else None
    d_tb = ex.date(tb[0][2]['dated']) if tb and tb[0][2].get('dated') is not None else None
    same = bool(tb) and 'Exod 32:19' in mk and tb[0][2].get('dated') == mk['Exod 32:19'][1]
    ok = len(tw) == 1 and len(tb) == 1 and d_tw == (1, 3, 7) and d_tb == (1, 4, 17) and 'Deut 4:10' in mk and 'Deut 4:13' in mk and mk['Deut 4:10'][2].get('retrograde') and mk['Deut 4:13'][2].get('retrograde') and same
    return ok, 'ten_words_declared %d dated %s; tablets_given %d dated %s; the markers at Deut 4:10 / 4:13 %s / %s; the tablets\\' day = the breaking\\'s %s' % (len(tw), d_tw, len(tb), d_tb, 'Deut 4:10' in mk, 'Deut 4:13' in mk, same)
def q9():
    with contextlib.redirect_stdout(io.StringIO()):
        ink = RG.read_ink(); cr = RG.class_receipts(ink, W); cf = RG.class_footers(ink)
    isr = W.entities.get('israel_people')
    deb = [e for e in isr.ledger if e['effect'] == 'commanded' and e.get('value') == 'appoint_six_cities_of_refuge'] if isr else []
    csa = [e for e in isr.ledger if e['effect'] == 'cities_set_apart'] if isr else []
    got = (cr.get('Deut 4:5', {}).get('class'), cf.get('Deut 4:45', {}).get('class'), cf.get('Deut 4:45', {}).get('daemons'), len(deb), bool(deb) and deb[0].get('open'), len(csa))
    return got == ('ACT', 'DAEMONS', 2, 1, True, 1), 'got (4:5 class, 4:45 class, 4:45 daemons, the refuge debit, open, cities_set_apart) = %s' % (got,)

'''
s = rep(s, "print('READBACK PROBES (THE LOOP step 6, the first form)')", Q + "print('READBACK PROBES (THE LOOP step 6, the first form)')")
s = rep(s, "('Q5 the open disagreements', q5), ('Q6 the register seats', q6)):", "('Q5 the open disagreements', q5), ('Q6 the register seats', q6), ('Q7 chapter 4\\'s table', q7), ('Q8 the Horeb lines dated', q8), ('Q9 the seats and the debit after chapter 4', q9)):")
open(P, 'w', encoding='utf-8').write(s); py_compile.compile(P, doraise=True)
# ---- checkpoint_probes.py ----
P2 = ROOT + '/World/step9/checkpoint_probes.py'
t = open(P2, encoding='utf-8').read()
t = rep(t, "            w, M, n = CS.run_to('Deut 4:1')                 # beyond the tape's last line",
        "            w, M, n = CS.run_to(beyond_the_tape())          # %s: the verse COMPUTED from the tape — the first verse of the chapter after the tape's last line (lesson xiii's second half; 'Deut 4:1' became a position on the tape when chapter 4 joined it); beyond the tape's last line" % W)
B = '''

def beyond_the_tape():
    """THE DEUTERONOMY WALK 2b (2026-09-16): the first verse of the chapter AFTER the tape's last line, read from the sequence file's own tape section
    and checked against the Tanakh DB (a verse beyond the tape runs the whole tape); at a book's last chapter the next book's 1:1 in the tape's order;
    past the fifth book the last verse itself (then run_to needs a whole-tape form — filed)."""
    import re as _re, sqlite3 as _sq
    src = open(os.path.join(HERE, 'cold_run_sequence.py'), encoding='utf-8').read()
    tape = src[src.find('# ==== TAPE BEGIN'):src.find('# ==== TAPE END ====')]
    refs = _re.findall(r"'case_source': '(Gen|Exod|Lev|Num|Deut) (\\d+):(\\d+)", tape)
    order = ['Gen', 'Exod', 'Lev', 'Num', 'Deut']
    last = max(refs, key=lambda r: (order.index(r[0]), int(r[1]), int(r[2])))
    db = _sq.connect('file:' + os.path.join(ROOT, 'Data', 'tanakh.sqlite') + '?mode=ro', uri=True)
    def exists(b, c, v): return bool(db.execute('SELECT 1 FROM verses WHERE book=? AND chapter=? AND verse=?', (b, c, v)).fetchone())
    b, c = last[0], int(last[1])
    if exists(b, c + 1, 1): return '%s %d:1' % (b, c + 1)
    if order.index(b) + 1 < len(order): return '%s 1:1' % order[order.index(b) + 1]
    return '%s %s:%s' % last
'''
t = rep(t, "\n\ndef whole():", B + "\n\ndef whole():")
open(P2, 'w', encoding='utf-8').write(t); py_compile.compile(P2, doraise=True)
print('patched readback_probes.py (Q7-Q9; Q4 narrowed) and checkpoint_probes.py (beyond_the_tape computed); both compile')
