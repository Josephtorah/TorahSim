import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 7b (2026-09-19): readback_probes.py Q22-Q24 written to FAIL before cold_run_not_righteousness.py exists (the design's THE PROBES
# paragraph; Q19-Q21's form). Q22 the runner and its the_readback table — THE READBACK'S SIXTH FORM (the retelling of a STRETCH): the rows and their census
# PREDICTED from the design's row list (thirty-two — 9:22's three names three rows, 9:23's two seats two rows; VERBATIM 14 / VARIANT 12 / EXPANDED 4 /
# TURNED 1 / SUPPLIED 1; twenty-two on the tape by kind and first verse, nine in the kin's cells by CALL; the four STRETCH rows measured on the running
# world by the markers' days; the one SUPPLIED row 9:20's WITH its write; the two OPEN rows; the one hole) — retyped ONCE from the runner's print if
# the census moves (4b's lesson); Q23 the retrograde line prayed_for_aaron dated (1, 4, 18) under the marker at Deut 9:20 (stated = the morrow's day),
# the forward marker at 9:21, markers 169, the counter (40, 11, 1); the write destruction_halved ONE on aaron, source 'Deut 9:20', dated with the line;
# Q24 the kin stands (decree_relented, blotted_from_the_book, tablets_delivered FOUR, fire_sank, atoned_forgiven UNMOVED; moses_interceded two, moses_pleaded
# one) and THE CLOCK — the four markers' dates and the three forties; the daemon registered. Idempotent. patch_probes_ch8.py's form.
import subprocess
ROOT = _ROOT
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
assert 'def q22():' not in s, 'already patched'
NEW = '''
# ---- THE DEUTERONOMY WALK 7b (2026-09-19): THE READBACK'S SIXTH FORM — the retelling of a STRETCH: chapter 9 is Moses telling the calf in his own voice; its rows are
# reference rows against the tape's lines by kind and first verse or the kin's cells by CALL (T1's form), ONE row fills a hole with a retrograde WRITE (9:20 Aaron's
# peril — T2's form, 3b's), and FOUR rows retell "forty days and forty nights" — a STRETCH between two markers graded against the clock's own arithmetic (the
# markers' days on the running world); written to FAIL before the runner exists (the design's Q22-Q24) ----
def q22():
    import cold_run_not_righteousness as NR
    tbl = NR.DATA['the_readback']; rows = tbl['value']; holes = tbl.get('holes') or []; opens = tbl.get('open_rows') or []
    gs = collections.Counter(r['grade'] for r in rows)
    on_tape = sum(1 for r in rows if r.get('tape_kind') and any(e[2]['kind'] == r['tape_kind'] and WE.first_verse(e[2].get('case_source')) == WE.first_verse(r['tape_verse']) for e in EV))
    by_call = sum(1 for r in rows if r.get('cell') and r.get('cell_found'))
    sup = [r for r in rows if r['grade'] == 'SUPPLIED']
    mk = {str(l[2].get('verse', '')): l for l in W.log if l[0] == 'MARKER'}
    st = [r for r in rows if r.get('stretch')]
    st_ok = bool(st) and all(r['stretch']['from'] in mk and r['stretch']['to'] in mk and mk[r['stretch']['to']][1] - mk[r['stretch']['from']][1] == r['stretch']['days'] for r in st)
    ok = len(rows) == 32 and on_tape + by_call == 31 and gs == collections.Counter({'VERBATIM': 14, 'VARIANT': 12, 'EXPANDED': 4, 'TURNED': 1, 'SUPPLIED': 1}) and len(holes) == 1 and len(opens) == 2 and not any(r.get('open') for r in rows) and len(sup) == 1 and sup[0]['verses'] == 'Deut 9:20' and sup[0].get('write') == 'destruction_halved' and len(st) == 4 and st_ok
    return ok, 'rows %d (found on the tape %d, in the kin\\'s cells by CALL %d), grades %s, the hole %d, the OPEN rows %d, open-flagged %d, the SUPPLIED row %s with its write %s, the STRETCH rows %d measured on the running world %s' % (len(rows), on_tape, by_call, dict(gs), len(holes), len(opens), sum(1 for r in rows if r.get('open')), [r['verses'] for r in sup], [r.get('write') for r in sup], len(st), st_ok)
def q23():
    pa = [e for e in EV if e[2]['kind'] == 'prayed_for_aaron']
    mk = {str(l[2].get('verse', '')): l for l in W.log if l[0] == 'MARKER'}; nm = len([l for l in W.log if l[0] == 'MARKER'])
    d = ex.date(pa[0][2]['dated']) if pa and pa[0][2].get('dated') is not None else None
    m20 = mk.get('Deut 9:20'); m21 = mk.get('Deut 9:21')
    retro = bool(m20) and bool(m20[2].get('retrograde')) and m20[2].get('stated') is not None and ex.date(m20[2]['stated']) == (1, 4, 18)
    fwd = bool(m21) and not m21[2].get('retrograde') and ex.date(m21[1]) == (40, 11, 1)
    aa = W.entities.get('aaron'); dh = [e for e in aa.ledger if e['effect'] == 'destruction_halved'] if aa else []
    d_w = ex.date(dh[0]['dated']) if dh and dh[0].get('dated') is not None else None
    got = (len(pa), d, retro, fwd, nm, ex.date(W.clock.day), len(dh), str(dh[0].get('case_source', ''))[:9] if dh else None, d_w, pa[0][2].get('placement') if pa else None, 'told only here' in str(pa[0][2].get('first_telling', '')) if pa else False)
    return got == (1, (1, 4, 18), True, True, 169, (40, 11, 1), 1, 'Deut 9:20', (1, 4, 18), 'reading_placed', True), 'got (prayed_for_aaron, its dated day, the RETROGRADE marker at Deut 9:20 stated (1, 4, 18), the FORWARD marker at 9:21 at the counter\\'s day, markers, the counter, destruction_halved on aaron, its source, its dated day, the line\\'s placement, first_telling told only here) = %s' % (got,)
def q24():
    import yaml as _y
    def L(ent, eff):
        e_ = W.entities.get(ent); return [e for e in e_.ledger if e['effect'] == eff] if e_ else []
    td = sum(len(L(x, 'tablets_delivered')) for x in ('moses', 'the-tablets', 'the_ark'))
    mi = [e for e in EV if e[2]['kind'] == 'moses_interceded']; mp = [e for e in EV if e[2]['kind'] == 'moses_pleaded_on_the_attributes']
    mk = {str(l[2].get('verse', '')): l for l in W.log if l[0] == 'MARKER'}
    FOUR = ('Exod 24:18', 'Exod 32:19', 'Exod 32:30', 'Exod 34:4')
    days = {v: mk[v][1] for v in FOUR if v in mk}
    dates = tuple(ex.date(days[v]) for v in FOUR if v in days)
    ten_tishri = W.clock.day_in('exodus', 1, 7, 10)
    forties = (days['Exod 32:19'] - days['Exod 24:18'], days['Exod 34:4'] - days['Exod 32:30'], ten_tishri - days['Exod 34:4']) if len(days) == 4 else None
    dd = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon_dispositions.yaml'), encoding='utf-8'))
    d = dd['daemons'].get('law_not_righteousness', {})
    got = (len(L('israel_people', 'decree_relented')), len(L('the-sinners', 'blotted_from_the_book')), td, len(L('israel_people', 'fire_sank')), len(L('aaron', 'atoned_forgiven')), len(mi), len(mp), dates, forties, 'law_not_righteousness' in dd['daemons'], d.get('given_at'), d.get('installed_by'))
    return got == (1, 1, 4, 1, 1, 2, 1, ((1, 3, 7), (1, 4, 17), (1, 4, 18), (1, 5, 29)), (40, 40, 40), True, 'Deut 9:1', 'boot'), 'got (decree_relented on Israel, blotted_from_the_book on the sinners, tablets_delivered over moses / the tablets / the ark, fire_sank, atoned_forgiven on aaron — the kin UNMOVED; moses_interceded lines, moses_pleaded lines — no third intercession; THE CLOCK: the four markers\\' dates, the three forties (the last to 10 Tishri); the daemon registered, given_at, installed_by) = %s' % (got,)
'''
a = "\nprint('READBACK PROBES (THE LOOP step 6, the first form)')"
assert s.count(a) == 1
s = s.replace(a, NEW + a)
old = "('Q21 the kin stands; the daemon', q21)):"
assert s.count(old) == 1
s = s.replace(old, "('Q21 the kin stands; the daemon', q21), ('Q22 chapter 9\\'s table — the readback\\'s sixth form, the retelling of a stretch', q22), ('Q23 the retrograde line and its write; the two markers', q23), ('Q24 the kin stands; the clock read back; the daemon', q24)):")
old2 = "Run: python3 World/step9/readback_probes.py"
assert s.count(old2) == 1
s = s.replace(old2, "  THE DEUTERONOMY WALK 7b (2026-09-19; DEUTERONOMY_WALK.md \"Sitting 7b\" THE PROBES) — written to FAIL before cold_run_not_righteousness.py exists:\n  Q22 chapter 9's table — THE READBACK'S SIXTH FORM (the retelling of a STRETCH): thirty-two rows predicted from the design (VERBATIM 14 / VARIANT 12 / EXPANDED 4 / TURNED 1 / SUPPLIED 1; twenty-two on the tape by kind and first verse, nine in the kin's cells by CALL — retyped once from the print if the census moves); the FOUR stretch rows (9:9, 9:11, 9:18, 9:25) measured on the running world by the markers' days (Exod 24:18 to 32:19 forty, 32:30 to 34:4 forty); the one SUPPLIED row 9:20's WITH its write destruction_halved; the two OPEN rows (the calf's own day, the second ascent's date); the one hole\n  Q23 the retrograde line prayed_for_aaron dated (1, 4, 18) under the RETROGRADE marker at Deut 9:20 (stated the morrow's day, Exod 32:30's), the FORWARD marker at 9:21 at the counter's day, markers 169, the counter (40, 11, 1); destruction_halved on aaron ONE, source 'Deut 9:20', dated with the line; the line reading_placed, first_telling told only here\n  Q24 the kin stands — decree_relented 1, blotted_from_the_book 1, tablets_delivered 4 (moses, the tablets twice, the ark), fire_sank 1, atoned_forgiven on aaron 1 UNMOVED; moses_interceded two lines, moses_pleaded_on_the_attributes one; THE CLOCK READ BACK — the four markers' dates (1, 3, 7), (1, 4, 17), (1, 4, 18), (1, 5, 29) and the three forties (the last to 10 Tishri); the daemon law_not_righteousness registered, given_at Deut 9:1, installed_by boot\n" + old2)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched readback_probes.py: Q22-Q24 added; compiles')
