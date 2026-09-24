import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 14b (2026-09-23): readback_probes.py Q43 written to FAIL before cold_run_festivals_judges.py exists (the design's THE PROBES paragraph — the
# FIRST step, before the types: 7b's lesson 2; ONE probe in the lean form): the FIVE OWN-DAY lines after the tape's last Deuteronomy 15 line on the counter's day
# (40, 11, 1), no dated field, NO marker at any Deut 16 verse (markers 172 UNMOVED); their writes — the fifteen NEW ONE each on israel_people with their lines' first
# verses, bribe_barred ONE (its FIRST entry anywhere — 16:18's line); the nine blocks; the daemon registered; the readback's twenty-two rows one per verse in order,
# no pointer, no state, no open, no stretch row. THE GREP DECIDED: no probe seat counts a reused effect of this chapter (the one stale literal DB7 is the sequence
# file's, retyped at the literals step). Idempotent. patch_probes_ch15.py's form. RUN FROM THE REPO ROOT.
import subprocess, os
ROOT = _ROOT
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
assert 'def q43():' not in s, 'already patched'
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:90]); s = s.replace(old, new)
W = 'THE DEUTERONOMY WALK 14b (2026-09-23)'
Q43 = '''
def q43():
    import yaml as _y, cold_run_festivals_judges as FJ
    def ENT(*names):
        for n_ in names:
            if n_ in W.entities: return W.entities[n_]
        return None
    def L(ent, eff):
        e_ = ENT(*ent) if isinstance(ent, tuple) else ENT(ent); return [e for e in e_.ledger if e['effect'] == eff] if e_ else []
    def nall(eff): return sum(1 for ent in W.entities.values() for e in ent.ledger if e['effect'] == eff)
    OWN = ('passover_at_the_place_declared', 'weeks_and_booths_declared', 'three_pilgrimages_declared', 'judges_in_every_gate_commanded', 'asherah_and_pillar_barred')
    own = [e for e in EV if e[2]['kind'] in OWN]
    idx = {id(l): i for i, l in enumerate(W.log)}
    i_last15 = max([i for i, l in enumerate(W.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 15:')] or [-1])
    after = bool(own) and all(idx[id(e)] > i_last15 for e in own)
    mk16 = [l for l in W.log if l[0] == 'MARKER' and str(l[2].get('verse', '')).startswith('Deut 16:')]; nm = len([l for l in W.log if l[0] == 'MARKER'])
    days = sorted({ex.date(e[1]) for e in own}); dated = sum(1 for e in own if e[2].get('dated') is not None)
    W15 = [('passover_at_the_place_commanded', 'Deut 16:1'), ('passover_in_the_gates_barred', 'Deut 16:1'), ('leaven_with_the_passover_barred', 'Deut 16:1'), ('flesh_till_morning_barred', 'Deut 16:1'), ('seventh_day_assembly_commanded', 'Deut 16:1'), ('weeks_at_the_place_commanded', 'Deut 16:9'), ('booths_at_the_place_commanded', 'Deut 16:9'), ('three_pilgrimages_commanded', 'Deut 16:16'), ('empty_appearance_barred', 'Deut 16:16'), ('judges_and_officers_commanded', 'Deut 16:18'), ('judgment_wresting_barred', 'Deut 16:18'), ('person_respecting_barred', 'Deut 16:18'), ('justice_pursuit_commanded', 'Deut 16:18'), ('asherah_beside_the_altar_barred', 'Deut 16:21'), ('pillar_barred', 'Deut 16:21')]
    FV = lambda t_: '%s %d:%d' % t_ if isinstance(t_, tuple) else str(t_)   # WE.first_verse returns a (book, chapter, verse) tuple — formatted to the literal's 'Deut 16:1' (10b's Q32 form)
    w15 = tuple((len(L('israel_people', eff)), FV(WE.first_verse(str(L('israel_people', eff)[0].get('case_source', '')))) if L('israel_people', eff) else None) for eff, _ in W15)
    br = (nall('bribe_barred'), [FV(WE.first_verse(str(e.get('case_source', '')))) for e in L('israel_people', 'bribe_barred')])
    blocks = sum(1 for eff in ('passover_in_the_gates_barred', 'leaven_with_the_passover_barred', 'flesh_till_morning_barred', 'empty_appearance_barred', 'judgment_wresting_barred', 'person_respecting_barred', 'asherah_beside_the_altar_barred', 'pillar_barred', 'bribe_barred') for e in L('israel_people', eff) if e.get('op') == 'block')
    rows = FJ.DATA['the_readback']['value']
    rb = (len(rows), [r['verses'] for r in rows] == ['Deut 16:%d' % v for v in range(1, 23)], any(r.get('pointer') for r in rows), any(r.get('state') for r in rows), any(r.get('open') for r in rows), any(r.get('stretch') for r in rows))
    dd = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon_dispositions.yaml'), encoding='utf-8'))
    d = dd['daemons'].get('law_festivals_judges', {})
    got = ([e[2]['kind'] for e in own], after, len(mk16), nm, days, dated, w15, br, blocks, rb, 'law_festivals_judges' in dd['daemons'], d.get('given_at'), d.get('installed_by'))
    return got == (list(OWN), True, 0, 172, [(40, 11, 1)], 0, tuple((1, v_) for _, v_ in W15), (1, ['Deut 16:18']), 9, (22, True, False, False, False, False), True, 'Deut 16:1', 'boot'), 'got (the five own-day lines in the ink\\'s order, all after the tape\\'s last Deuteronomy 15 line, markers at Deut 16 (none), markers, their day, dated fields (none), the fifteen NEW writes on israel_people with their lines\\' first verses, bribe_barred ONE — its FIRST entry anywhere, on the line judges_in_every_gate_commanded at 16:18 (Exodus 23:8\\'s block declared and never written before — DB7), the nine blocks, the readback (rows, one per verse in order, pointer, state, open, stretch), the daemon registered, given_at, installed_by) = %s' % (got,)
'''
rep("\nprint('READBACK PROBES (THE LOOP step 6, the first form)')", Q43 + "\nprint('READBACK PROBES (THE LOOP step 6, the first form)')")
rep("('Q42 the kin stands; the holes filled; the scans; the release on the bare world; the parameters', q42)", "('Q42 the kin stands; the holes filled; the scans; the release on the bare world; the parameters', q42), ('Q43 chapter 16\\'s five own-day lines, their sixteen writes (the bribe\\'s first), the nine blocks, the readback\\'s twenty-two rows, the daemon — LEAN', q43)")
rep("  Q42 the kin stands — interest_barred,", "  %s (DEUTERONOMY_WALK.md \"Sitting 14b\" THE PROBES; THE LEAN PASS) — written to FAIL before cold_run_festivals_judges.py exists: Q43 the FIVE OWN-DAY lines passover_at_the_place_declared (16:1-8), weeks_and_booths_declared (16:9-15), three_pilgrimages_declared (16:16-17), judges_in_every_gate_commanded (16:18-20) and asherah_and_pillar_barred (16:21-22) after the tape's last Deuteronomy 15 line on the counter's day (40, 11, 1), no dated field, NO marker at any Deut 16 verse (markers 172 UNMOVED); their writes — the fifteen NEW ONE each on israel_people (seven STATUSES, eight BLOCKS) and bribe_barred ONE, ITS FIRST ENTRY ANYWHERE (Exodus 23:8's block declared at the ordinances' cell, never written — DB7's 'NEVER' retyped at the literals step); the nine blocks; the readback's twenty-two rows one per verse in order with no pointer, state, open or stretch row; the daemon law_festivals_judges registered, given_at Deut 16:1, installed_by boot (ONE probe — the lean form)\n  Q42 the kin stands — interest_barred," % W)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched: Q43 written (to FAIL until the runner and the tape carry chapter 16); the file compiles')
