import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 8b (2026-09-20): readback_probes.py Q25-Q27 written to FAIL before cold_run_second_tablets.py exists (the design's THE PROBES
# paragraph; Q22-Q24's form). Q25 the runner and its the_readback table — THE FORMS COMBINED, NO SEVENTH: the rows and their census PREDICTED from the
# design's row list (twenty-five — 10:2 two rows (God's word and the supplied clause), 10:6 three rows (the stations, the death, the burial), 10:10 two
# (the stretch and the hearkening); VERBATIM 9 / VARIANT 10 / EXPANDED 3 / TURNED 1 / SUPPLIED 2; ten on the tape by kind and first verse, thirteen in the
# kin's cells by CALL; the ONE stretch row 10:10 measured on the running world by the markers' days; the two SUPPLIED rows WITH their writes; the one
# OPEN row (the place of the death); the one hole outside the span (the go)) — retyped ONCE from the runner's print if the census moves (4b's lesson);
# Q26 the two RETROGRADE lines — fragments_placed_in_the_ark dated (2, 1, 1) under the marker at Deut 10:2 (stated = M['erected'], Exod 40:17's day),
# aaron_buried dated (40, 5, 1) under the marker at Deut 10:6 (stated = M['aaron_death'], Num 20:28's) — the FORWARD marker at 10:12, markers 172, the
# counter (40, 11, 1); the writes fragments_in_the_ark ONE on the_ark (source 'Deut 10:2', dated (2, 1, 1)) and buried ONE on aaron (source 'Deut 10:6',
# dated (40, 5, 1)); Q27 the four OWN-DAY lines (demand_declared, heart_circumcision_commanded, stranger_love_commanded, cleaving_commanded — no dated
# field, after the forward marker) and their five writes on israel_people ONE each (love_owed its FIRST on the tape), and the kin standing (DB6-DB7's
# counts); the daemon registered. AND Q23's 'markers 169' retyped to 172 (its text and its tuple — a count literal in a probe moves like one in a
# checkpoint; 7b's lesson 12). Idempotent. patch_probes_ch9.py's form.
import subprocess
ROOT = _ROOT
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
assert 'def q25():' not in s, 'already patched'
NEW = '''
# ---- THE DEUTERONOMY WALK 8b (2026-09-20): THE FORMS COMBINED, NO SEVENTH — chapter 10 is the retelling's tail (10:1-11) and the laws' head (10:12-22): T1 reference
# rows against the tape's lines by kind and first verse or the kin's cells by CALL; T2 SUPPLIED WITH A WRITE, TWICE (the fragments in the ark, Aaron's burial — two
# acts told only here, each written ONCE at its own day by a RETROGRADE marker); T6 ONE stretch row (10:10's third forty, measured on the clock); T4 the laws' form on
# 10:12-22 with the code's holes compiled at the chapter's own day; an OPEN row (the place of the death); a hole outside the span (the go); written to FAIL before the
# runner exists (the design's Q25-Q27) ----
def q25():
    import cold_run_second_tablets as ST
    tbl = ST.DATA['the_readback']; rows = tbl['value']; holes = tbl.get('holes') or []; opens = tbl.get('open_rows') or []
    gs = collections.Counter(r['grade'] for r in rows)
    on_tape = sum(1 for r in rows if r.get('tape_kind') and any(e[2]['kind'] == r['tape_kind'] and WE.first_verse(e[2].get('case_source')) == WE.first_verse(r['tape_verse']) for e in EV))
    by_call = sum(1 for r in rows if r.get('cell') and r.get('cell_found'))
    sup = [r for r in rows if r['grade'] == 'SUPPLIED']
    mk = {str(l[2].get('verse', '')): l for l in W.log if l[0] == 'MARKER'}
    st = [r for r in rows if r.get('stretch')]
    st_ok = bool(st) and all(r['stretch']['from'] in mk and r['stretch']['to'] in mk and mk[r['stretch']['to']][1] - mk[r['stretch']['from']][1] == r['stretch']['days'] for r in st)
    ok = len(rows) == 25 and on_tape + by_call == 23 and gs == collections.Counter({'VERBATIM': 9, 'VARIANT': 10, 'EXPANDED': 3, 'TURNED': 1, 'SUPPLIED': 2}) and len(holes) == 1 and len(opens) == 1 and not any(r.get('open') for r in rows) and len(sup) == 2 and [r['verses'] for r in sup] == ['Deut 10:2', 'Deut 10:6'] and [r.get('write') for r in sup] == ['fragments_in_the_ark', 'buried'] and len(st) == 1 and st_ok
    return ok, 'rows %d (found on the tape %d, in the kin\\'s cells by CALL %d), grades %s, the hole %d, the OPEN rows %d, open-flagged %d, the SUPPLIED rows %s with their writes %s, the STRETCH rows %d measured on the running world %s' % (len(rows), on_tape, by_call, dict(gs), len(holes), len(opens), sum(1 for r in rows if r.get('open')), [r['verses'] for r in sup], [r.get('write') for r in sup], len(st), st_ok)
def q26():
    def ENT(*names):
        for n_ in names:
            if n_ in W.entities: return W.entities[n_]
        return None
    fp = [e for e in EV if e[2]['kind'] == 'fragments_placed_in_the_ark']; ab = [e for e in EV if e[2]['kind'] == 'aaron_buried']
    mk = {str(l[2].get('verse', '')): l for l in W.log if l[0] == 'MARKER'}; nm = len([l for l in W.log if l[0] == 'MARKER'])
    D_ = lambda ev: ex.date(ev[0][2]['dated']) if ev and ev[0][2].get('dated') is not None else None
    m2 = mk.get('Deut 10:2'); m6 = mk.get('Deut 10:6'); m12 = mk.get('Deut 10:12')
    r2 = bool(m2) and bool(m2[2].get('retrograde')) and m2[2].get('stated') is not None and ex.date(m2[2]['stated']) == (2, 1, 1)
    r6 = bool(m6) and bool(m6[2].get('retrograde')) and m6[2].get('stated') is not None and ex.date(m6[2]['stated']) == (40, 5, 1)
    fwd = bool(m12) and not m12[2].get('retrograde') and ex.date(m12[1]) == (40, 11, 1)
    ark = ENT('the_ark', 'the-ark'); aa = ENT('aaron')
    fi = [e for e in ark.ledger if e['effect'] == 'fragments_in_the_ark'] if ark else []; bu = [e for e in aa.ledger if e['effect'] == 'buried'] if aa else []
    DW = lambda ws: ex.date(ws[0]['dated']) if ws and ws[0].get('dated') is not None else None
    got = (len(fp), D_(fp), len(ab), D_(ab), r2, r6, fwd, nm, ex.date(W.clock.day), len(fi), str(fi[0].get('case_source', ''))[:9] if fi else None, DW(fi), len(bu), str(bu[0].get('case_source', ''))[:9] if bu else None, DW(bu), sorted({e[2].get('placement') for e in fp + ab}), all('told only here' in str(e[2].get('first_telling', '')) for e in fp + ab) and bool(fp + ab))
    return got == (1, (2, 1, 1), 1, (40, 5, 1), True, True, True, 172, (40, 11, 1), 1, 'Deut 10:2', (2, 1, 1), 1, 'Deut 10:6', (40, 5, 1), ['reading_placed'], True), 'got (fragments_placed_in_the_ark, its dated day, aaron_buried, its dated day, the RETROGRADE marker at Deut 10:2 stated (2, 1, 1), the RETROGRADE marker at Deut 10:6 stated (40, 5, 1), the FORWARD marker at 10:12 at the counter\\'s day, markers, the counter, fragments_in_the_ark on the ark, its source, its dated day, buried on aaron, its source, its dated day, the lines\\' placement, first_telling told only here) = %s' % (got,)
def q27():
    import yaml as _y
    def ENT(*names):
        for n_ in names:
            if n_ in W.entities: return W.entities[n_]
        return None
    def L(ent, eff):
        e_ = ENT(*ent) if isinstance(ent, tuple) else ENT(ent); return [e for e in e_.ledger if e['effect'] == eff] if e_ else []
    OWN = ('demand_declared', 'heart_circumcision_commanded', 'stranger_love_commanded', 'cleaving_commanded')
    own = [e for e in EV if e[2]['kind'] in OWN]
    i12 = [i for i, l in enumerate(W.log) if l[0] == 'MARKER' and str(l[2].get('verse', '')) == 'Deut 10:12']
    idx = {id(l): i for i, l in enumerate(W.log)}
    after = bool(i12) and all(idx[id(e)] > i12[0] for e in own)
    days = sorted({ex.date(e[1]) for e in own}); dated = sum(1 for e in own if e[2].get('dated') is not None)
    W5 = [('fear_of_heaven_asked', 'Deut 10:1'), ('heart_circumcision_commanded', 'Deut 10:1'), ('stiffening_barred', 'Deut 10:1'), ('love_owed', 'Deut 10:1'), ('cleaving_commanded', 'Deut 10:2')]
    w5 = tuple((len(L('israel_people', eff)), str(L('israel_people', eff)[0].get('case_source', ''))[:9] if L('israel_people', eff) else None) for eff, _ in W5)
    dd = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon_dispositions.yaml'), encoding='utf-8'))
    d = dd['daemons'].get('law_second_tablets', {})
    lv = L(('the_levites', 'the-levites'), 'invested_office')
    kin = (len(L('israel_people', 'shema_commanded')), len(L('israel_people', 'test_barred')), len(lv), tuple(lv[0]['value']) if lv and isinstance(lv[0].get('value'), (list, tuple)) else (lv[0].get('value') if lv else None), len(L(('the_levites', 'the-levites'), 'given_to_aaron')), len(L(('the_levites', 'the-levites'), 'inheritance_barred')), len(L('aaron', 'inheritance_barred')), len(L(('the_levites', 'the-levites'), 'tithe_granted')), len(ENT('aaron').ledger) if ENT('aaron') else None, len(L(('eleazar', 'eleazar_son_of_aaron'), 'invested_office')))
    got = ([e[2]['kind'] for e in own], after, days, dated, w5, kin, 'law_second_tablets' in dd['daemons'], d.get('given_at'), d.get('installed_by'))
    return got == (list(OWN), True, [(40, 11, 1)], 0, ((1, 'Deut 10:1'), (1, 'Deut 10:1'), (1, 'Deut 10:1'), (1, 'Deut 10:1'), (1, 'Deut 10:2')), (1, 1, 1, (1, 2), 2, 1, 1, 1, 30, 1), True, 'Deut 10:1', 'boot'), 'got (the four own-day lines in the ink\\'s order, all after the forward marker at 10:12, their day, dated fields (none), the five writes on israel_people with their sources\\' heads (fear_of_heaven_asked, heart_circumcision_commanded, stiffening_barred, love_owed, cleaving_commanded), THE KIN STANDING (shema_commanded, test_barred, invested_office on the Levites and its value (1, 2), given_to_aaron TWO, inheritance_barred on the Levites and on aaron, tithe_granted, aaron\\'s entries 30, eleazar\\'s invested_office ONE), the daemon registered, given_at, installed_by) = %s' % (got,)
'''
a = "\nprint('READBACK PROBES (THE LOOP step 6, the first form)')"
assert s.count(a) == 1
s = s.replace(a, NEW + a)
old = "('Q24 the kin stands; the clock read back; the daemon', q24)):"
assert s.count(old) == 1
s = s.replace(old, "('Q24 the kin stands; the clock read back; the daemon', q24), ('Q25 chapter 10\\'s table — the forms combined, no seventh', q25), ('Q26 the two retrograde lines and their writes; the three markers', q26), ('Q27 the four own-day lines and their writes; the kin stands; the daemon', q27)):")
old2 = "Run: python3 World/step9/readback_probes.py"
assert s.count(old2) == 1
s = s.replace(old2, "  THE DEUTERONOMY WALK 8b (2026-09-20; DEUTERONOMY_WALK.md \"Sitting 8b\" THE PROBES) — written to FAIL before cold_run_second_tablets.py exists:\n  Q25 chapter 10's table — THE FORMS COMBINED, NO SEVENTH (the retelling's tail 10:1-11 and the laws' head 10:12-22): twenty-five rows predicted from the design (VERBATIM 9 / VARIANT 10 / EXPANDED 3 / TURNED 1 / SUPPLIED 2; ten on the tape by kind and first verse, thirteen in the kin's cells by CALL — retyped once from the print if the census moves); the ONE stretch row (10:10, the third forty — Exod 34:4 to 34:28 forty) measured on the running world by the markers' days; the two SUPPLIED rows 10:2's and 10:6's WITH their writes fragments_in_the_ark and buried; the one OPEN row (the place of the death); the one hole (the go — outside the span)\n  Q26 the two retrograde lines — fragments_placed_in_the_ark dated (2, 1, 1) under the RETROGRADE marker at Deut 10:2 (stated the erection's day, Exod 40:17's), aaron_buried dated (40, 5, 1) under the RETROGRADE marker at Deut 10:6 (stated Aaron's death, Num 20:28's) — the FORWARD marker at 10:12 at the counter's day, markers 172, the counter (40, 11, 1); fragments_in_the_ark on the ark ONE (source 'Deut 10:2', dated with its line), buried on aaron ONE (source 'Deut 10:6', dated with its line — the world's ninth buried); both lines reading_placed, first_telling told only here\n  Q27 the four own-day lines (demand_declared 10:12-13, heart_circumcision_commanded 10:16, stranger_love_commanded 10:17-19, cleaving_commanded 10:20-22) after the forward marker at 10:12 on the counter's day, no dated field; their five writes on israel_people ONE each — fear_of_heaven_asked, heart_circumcision_commanded (statuses), stiffening_barred (a block), love_owed (REUSED — its first on the tape), cleaving_commanded; THE KIN STANDING — shema_commanded 1, test_barred 1, invested_office on the Levites 1 with its value (1, 2), given_to_aaron 2, inheritance_barred 1 on the Levites and 1 on aaron, tithe_granted 1, aaron's entries 30, eleazar's invested_office 1; the daemon law_second_tablets registered, given_at Deut 10:1, installed_by boot\n" + old2)
# Q23's count literal — 169 -> 172 (the text and the tuple; every line of a literal covered)
old3 = "the FORWARD marker at 9:21 at the counter's day, markers 169, the counter (40, 11, 1); destruction_halved on aaron ONE"
assert s.count(old3) == 1, s.count(old3)
s = s.replace(old3, "the FORWARD marker at 9:21 at the counter's day, markers 169 (172 since THE DEUTERONOMY WALK 8b, 2026-09-20 — the retrograde markers at Deut 10:2 and 10:6 and the forward marker at 10:12), the counter (40, 11, 1); destruction_halved on aaron ONE")
old4 = "return got == (1, (1, 4, 18), True, True, 169, (40, 11, 1), 1, 'Deut 9:20', (1, 4, 18), 'reading_placed', True)"
assert s.count(old4) == 1, s.count(old4)
s = s.replace(old4, "return got == (1, (1, 4, 18), True, True, 172, (40, 11, 1), 1, 'Deut 9:20', (1, 4, 18), 'reading_placed', True)")
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched readback_probes.py: Q25-Q27 added; Q23 markers 169 -> 172 (the text and the tuple); compiles')
