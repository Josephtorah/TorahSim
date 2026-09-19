import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 6b (2026-09-19): readback_probes.py Q19-Q21 written to FAIL before cold_run_good_land.py exists (the design's THE PROBES paragraph;
# Q16-Q18's form). Q19 the runner and its the_readback table — THE READBACK'S FIFTH FORM (the retelling of a STATE): eighteen rows, VERBATIM 6 / VARIANT 5 /
# EXPANDED 4 / TURNED 2 / SUPPLIED 1 predicted, seventeen found (the tape by kind and first verse, the kin's cells by CALL) and ONE SUPPLIED row (8:4 the
# garment and the foot) with its ledger scan EMPTY, the three holes named, no row OPEN; Q20 the three lines on the counter's day with NO marker (markers 167)
# and the three writes on Israel with their sources; Q21 the kin stands (the counts measured on the one database before the run — per source, the live
# world's: manna_provided 1, water_from_the_rock 2, serpents_sent 1, shema_commanded 1, test_barred 1, other_gods_barred 1, blessings_for_hearing 1,
# treasured_people 1) and the daemon registered. Idempotent.
import subprocess
ROOT = _ROOT
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
assert 'def q19():' not in s, 'already patched'
NEW = '''
# ---- THE DEUTERONOMY WALK 6b (2026-09-19): THE READBACK'S FIFTH FORM — the retelling of a STATE: chapter 8 retells the wilderness as the reason for a law; its rows are
# reference rows against the tape's lines by kind and verse or the kin's cells by CALL, and ONE row retells a state the tape never wrote (8:4 the garment and the foot —
# SUPPLIED, no retrograde write); written to FAIL before the runner exists (the design's Q19-Q21) ----
def q19():
    import cold_run_good_land as GL
    tbl = GL.DATA['the_readback']; rows = tbl['value']; holes = tbl.get('holes') or []
    gs = collections.Counter(r['grade'] for r in rows)
    on_tape = sum(1 for r in rows if r.get('tape_kind') and any(e[2]['kind'] == r['tape_kind'] and WE.first_verse(e[2].get('case_source')) == WE.first_verse(r['tape_verse']) for e in EV))
    by_call = sum(1 for r in rows if r.get('cell') and r.get('cell_found'))
    sup = [r for r in rows if r['grade'] == 'SUPPLIED']
    ok = len(rows) == 18 and on_tape + by_call == 17 and gs == collections.Counter({'VERBATIM': 6, 'VARIANT': 5, 'EXPANDED': 4, 'TURNED': 2, 'SUPPLIED': 1}) and len(holes) == 3 and not any(r.get('open') for r in rows) and len(sup) == 1 and sup[0]['verses'] == 'Deut 8:4' and sup[0].get('ledger_scan') == []
    return ok, 'rows %d (found on the tape %d, in the kin\\'s cells by CALL %d), grades %s, the code\\'s holes %d, open %d, the SUPPLIED row %s with its ledger scan %s' % (len(rows), on_tape, by_call, dict(gs), len(holes), sum(1 for r in rows if r.get('open')), [r['verses'] for r in sup], [r.get('ledger_scan') for r in sup])
def q20():
    gc = [e for e in EV if e[2]['kind'] == 'grace_commanded']; fw = [e for e in EV if e[2]['kind'] == 'forgetting_warned']; pt = [e for e in EV if e[2]['kind'] == 'perishing_testified']
    mk = {str(l[2].get('verse', '')): l for l in W.log if l[0] == 'MARKER'}; nm = len([l for l in W.log if l[0] == 'MARKER'])
    isr = W.entities.get('israel_people')
    def L(eff): return [e for e in isr.ledger if e['effect'] == eff] if isr else []
    bl = L('bless_after_eating_commanded'); fb = L('forgetting_barred'); hw = L('heaven_and_earth_witness')
    got = (len(gc), len(fw), len(pt), any(k.startswith('Deut 8:') for k in mk), nm, len(bl), len(fb), len(hw), str(bl[0].get('case_source', ''))[:8] if bl else None, str(fb[0].get('case_source', ''))[:9] if fb else None, str(hw[-1].get('case_source', ''))[:9] if hw else None, str(hw[0].get('case_source', ''))[:9] if hw else None)
    return got == (1, 1, 1, False, 167, 1, 1, 2, 'Deut 8:7', 'Deut 8:11', 'Deut 8:19', 'Deut 4:25'), 'got (grace_commanded, forgetting_warned, perishing_testified, a chapter-8 marker, markers, bless_after_eating_commanded, forgetting_barred, heaven_and_earth_witness, their sources — the status at the first line, the block at the second, the testimony\\'s reuse at the third, the 4:26 entry first) = %s' % (got,)
def q21():
    import yaml as _y
    isr = W.entities.get('israel_people')
    def L(eff): return [e for e in isr.ledger if e['effect'] == eff] if isr else []
    dd = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon_dispositions.yaml'), encoding='utf-8'))
    d = dd['daemons'].get('law_good_land', {})
    got = (len(L('manna_provided')), len(L('water_from_the_rock')), len(L('serpents_sent')), len(L('shema_commanded')), len(L('test_barred')), len(L('other_gods_barred')), len(L('blessings_for_hearing')), len(L('treasured_people')), 'law_good_land' in dd['daemons'], d.get('given_at'), d.get('installed_by'))
    return got == (1, 2, 1, 1, 1, 1, 1, 1, True, 'Deut 8:1', 'boot'), 'got (manna_provided, water_from_the_rock, serpents_sent, shema_commanded, test_barred, other_gods_barred, blessings_for_hearing, treasured_people on Israel — the kin UNMOVED, no second write; the daemon registered, given_at, installed_by) = %s' % (got,)
'''
a = "\nprint('READBACK PROBES (THE LOOP step 6, the first form)')"
assert s.count(a) == 1
s = s.replace(a, NEW + a)
old = "('Q18 the kin stands; the daemon', q18)):"
assert s.count(old) == 1
s = s.replace(old, "('Q18 the kin stands; the daemon', q18), ('Q19 chapter 8\\'s table — the readback\\'s fifth form, the retelling of a state', q19), ('Q20 the three lines on the speech\\'s day, no marker; the three writes', q20), ('Q21 the kin stands; the daemon', q21)):")
# the docstring's index
old2 = "Run: python3 World/step9/readback_probes.py"
assert s.count(old2) == 1
s = s.replace(old2, "  THE DEUTERONOMY WALK 6b (2026-09-19; DEUTERONOMY_WALK.md \"Sitting 6b\" THE PROBES) — written to FAIL before cold_run_good_land.py exists:\n  Q19 chapter 8's table — THE READBACK'S FIFTH FORM (the retelling of a STATE): eighteen rows, VERBATIM 6 / VARIANT 5 / EXPANDED 4 / TURNED 2 / SUPPLIED 1; seventeen found (the tape by kind and first verse, the kin's cells by CALL), the one SUPPLIED row 8:4's (the garment and the foot) with its ledger scan EMPTY — no retrograde write; the three holes named; no row OPEN\n  Q20 the three lines of chapter 8 (grace_commanded 8:7-10, forgetting_warned 8:11-18, perishing_testified 8:19-20) on the speech's own day — NO marker, the markers 167; bless_after_eating_commanded (a status) and forgetting_barred (a block) on Israel ONE each, heaven_and_earth_witness TWO (4:26's entry and the reuse at 8:19), their sources the lines' first verses\n  Q21 the kin stands — manna_provided 1, water_from_the_rock 2, serpents_sent 1, shema_commanded 1, test_barred 1, other_gods_barred 1, blessings_for_hearing 1, treasured_people 1 on Israel UNMOVED (measured on the one database per source before the run); the daemon law_good_land registered, given_at Deut 8:1, installed_by boot\n" + old2)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched readback_probes.py: Q19-Q21 added; compiles')
