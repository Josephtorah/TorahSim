import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 9b (2026-09-20): readback_probes.py Q28-Q30 written to FAIL before cold_run_blessing_and_curse.py exists (the design's THE PROBES
# paragraph; Q25-Q27's form). Q28 the runner and its the_readback table — THE FORMS ON FILE, NO NEW FORM: thirty-two rows predicted from the design (one per
# verse; VERBATIM 7 / VARIANT 19 / EXPANDED 4 / SUPPLIED 2; eleven on the tape by kind and first verse, nineteen in the kin's cells by CALL; the state row
# 11:5 SUPPLIED with NO write (chapter 8's fifth form); the ceremony row 11:29 SUPPLIED WITH THE WRITE gerizim_ebal_ceremony_owed — the debit's first seat;
# the pointer row 11:25; no hole, no open row, no stretch, no retrograde row) — retyped ONCE from the runner's print if the census moves (4b's lesson);
# Q29 the two OWN-DAY lines second_paragraph_declared (11:13-21) and blessing_and_curse_set (11:26-32) after the tape's last Deuteronomy 10 line, on the
# counter's day (40, 11, 1), no dated field, NO marker at any Deut 11 verse, markers 172 UNMOVED; their five writes on israel_people ONE each (rain_in_its_season
# and heavens_shut_for_turning HEAVEN entries conditional, yoke_of_the_commandments_accepted and blessing_and_curse_set statuses, gerizim_ebal_ceremony_owed a
# DEBIT OPEN toward Heaven), the open debits on israel_people 10; the daemon registered; Q30 the kin standing (DC6-DC7's counts) and THE RAIN'S HOLE FILLED
# (DC4 — no other effect naming the rain or the heavens shut on israel_people; the vocabulary's rain effects two). Idempotent. patch_probes_ch10.py's form.
import subprocess, os
ROOT = _ROOT
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
assert 'def q28():' not in s, 'already patched'
NEW = '''
# ---- THE DEUTERONOMY WALK 9b (2026-09-20): THE FORMS ON FILE, NO NEW FORM — chapter 11 is the discipline retold (11:1-7), the land watered by heaven (11:8-12), the
# second paragraph (11:13-21), the borders and the dread (11:22-25), the blessing and the curse (11:26-32): T1 reference rows against the tape's lines by kind and first
# verse or the kin's cells by CALL; T5 the state row 11:5 SUPPLIED with NO write (chapter 8's form); T4 the laws' form with THE CODE'S TWO HOLES compiled at the
# chapter's own day (the rain conditional, the blessing-and-curse set with the ceremony's debit); the receipt 11:25 a pointer; written to FAIL before the runner exists
# (the design's Q28-Q30) ----
def q28():
    import cold_run_blessing_and_curse as BC
    tbl = BC.DATA['the_readback']; rows = tbl['value']; holes = tbl.get('holes') or []; opens = tbl.get('open_rows') or []
    gs = collections.Counter(r['grade'] for r in rows)
    on_tape = sum(1 for r in rows if r.get('tape_kind') and any(e[2]['kind'] == r['tape_kind'] and WE.first_verse(e[2].get('case_source')) == WE.first_verse(r['tape_verse']) for e in EV))
    by_call = sum(1 for r in rows if r.get('cell') and r.get('cell_found'))
    sup = [r for r in rows if r['grade'] == 'SUPPLIED']
    ptr = [r for r in rows if r.get('pointer')]
    ok = len(rows) == 32 and on_tape + by_call == 30 and gs == collections.Counter({'VERBATIM': 7, 'VARIANT': 19, 'EXPANDED': 4, 'SUPPLIED': 2}) and len(holes) == 0 and len(opens) == 0 and not any(r.get('open') for r in rows) and not any(r.get('stretch') for r in rows) and len(sup) == 2 and [r['verses'] for r in sup] == ['Deut 11:5', 'Deut 11:29'] and [r.get('write') for r in sup] == [None, 'gerizim_ebal_ceremony_owed'] and [bool(r.get('state')) for r in sup] == [True, False] and [r['verses'] for r in ptr] == ['Deut 11:25']
    return ok, 'rows %d (found on the tape %d, in the kin\\'s cells by CALL %d), grades %s, the holes %d, the OPEN rows %d, open-flagged %d, stretch rows %d, the SUPPLIED rows %s with their writes %s (the state row %s), the pointer rows %s' % (len(rows), on_tape, by_call, dict(gs), len(holes), len(opens), sum(1 for r in rows if r.get('open')), sum(1 for r in rows if r.get('stretch')), [r['verses'] for r in sup], [r.get('write') for r in sup], [bool(r.get('state')) for r in sup], [r['verses'] for r in ptr])
def q29():
    import yaml as _y
    def ENT(*names):
        for n_ in names:
            if n_ in W.entities: return W.entities[n_]
        return None
    def L(ent, eff):
        e_ = ENT(*ent) if isinstance(ent, tuple) else ENT(ent); return [e for e in e_.ledger if e['effect'] == eff] if e_ else []
    OWN = ('second_paragraph_declared', 'blessing_and_curse_set')
    own = [e for e in EV if e[2]['kind'] in OWN]
    idx = {id(l): i for i, l in enumerate(W.log)}
    i_last10 = max([i for i, l in enumerate(W.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 10:')] or [-1])
    after = bool(own) and all(idx[id(e)] > i_last10 for e in own)
    mk11 = [l for l in W.log if l[0] == 'MARKER' and str(l[2].get('verse', '')).startswith('Deut 11:')]; nm = len([l for l in W.log if l[0] == 'MARKER'])
    days = sorted({ex.date(e[1]) for e in own}); dated = sum(1 for e in own if e[2].get('dated') is not None)
    W5 = [('rain_in_its_season', 'Deut 11:13'), ('heavens_shut_for_turning', 'Deut 11:13'), ('yoke_of_the_commandments_accepted', 'Deut 11:13'), ('blessing_and_curse_set', 'Deut 11:26'), ('gerizim_ebal_ceremony_owed', 'Deut 11:26')]
    w5 = tuple((len(L('israel_people', eff)), str(L('israel_people', eff)[0].get('case_source', ''))[:10] if L('israel_people', eff) else None) for eff, _ in W5)
    deb = L('israel_people', 'gerizim_ebal_ceremony_owed'); deb_open = bool(deb) and not deb[0].get('closed_by') and deb[0].get('counterparty') == 'HEAVEN'
    open_debits = len([e for e in ENT('israel_people').ledger if e.get('op') == 'debit' and not e.get('closed_by')]) if ENT('israel_people') else None
    dd = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon_dispositions.yaml'), encoding='utf-8'))
    d = dd['daemons'].get('law_blessing_and_curse', {})
    got = ([e[2]['kind'] for e in own], after, len(mk11), nm, days, dated, w5, deb_open, open_debits, 'law_blessing_and_curse' in dd['daemons'], d.get('given_at'), d.get('installed_by'))
    return got == (list(OWN), True, 0, 172, [(40, 11, 1)], 0, ((1, 'Deut 11:13'), (1, 'Deut 11:13'), (1, 'Deut 11:13'), (1, 'Deut 11:26'), (1, 'Deut 11:26')), True, 10, True, 'Deut 11:1', 'boot'), 'got (the two own-day lines in the ink\\'s order, both after the tape\\'s last Deuteronomy 10 line, markers at Deut 11 (none), markers, their day, dated fields (none), the five writes on israel_people with their sources\\' heads (rain_in_its_season, heavens_shut_for_turning, yoke_of_the_commandments_accepted, blessing_and_curse_set, gerizim_ebal_ceremony_owed), the debit OPEN toward Heaven, the open debits on israel_people, the daemon registered, given_at, installed_by) = %s' % (got,)
def q30():
    import yaml as _y
    def ENT(*names):
        for n_ in names:
            if n_ in W.entities: return W.entities[n_]
        return None
    def L(ent, eff):
        e_ = ENT(*ent) if isinstance(ent, tuple) else ENT(ent); return [e for e in e_.ledger if e['effect'] == eff] if e_ else []
    def n(ent, eff): return len(L(ent, eff))
    kin = (n('israel_people', 'shema_commanded'), n('israel_people', 'test_barred'), n('israel_people', 'blessings_for_hearing'), n('israel_people', 'pity_barred'), n('israel_people', 'fear_of_heaven_asked'), n('israel_people', 'cleaving_commanded'), n('israel_people', 'love_owed'), n('israel_people', 'other_gods_barred'), n('israel_people', 'coveting_barred'), n(('the-land-of-canaan', 'the_land_of_canaan'), 'borders_declared'))
    isr = ENT('israel_people'); rainy = sorted({e['effect'] for e in isr.ledger if any(t in e['effect'] for t in ('rain', 'heaven', 'yoke'))}) if isr else None
    fx = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
    vocab_rain = sorted(k for k in fx if 'rain' in k)
    es = [e for e in EV if e[2]['kind'] == 'earth_swallowed']; sh = [e for e in EV if e[2]['kind'] == 'shema_declared']
    lines = (len([e for e in EV if e[2]['kind'] == 'plague_struck']), len([e for e in EV if e[2]['kind'] == 'sea_split']), len([e for e in EV if e[2]['kind'] == 'sea_returned']), len([e for e in EV if e[2]['kind'] == 'all_flesh_expired']), len(es), es[0][2].get('korach_named') if es else None, len(sh))
    got = (kin, rainy, vocab_rain, lines)
    return got == ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1), ['heavens_shut_for_turning', 'rain_in_its_season', 'yoke_of_the_commandments_accepted'], ['fire_rained', 'rain_in_its_season'], (10, 1, 1, 1, 1, False, 1)), 'got (THE KIN STANDING (shema_commanded, test_barred, blessings_for_hearing, pity_barred, fear_of_heaven_asked, cleaving_commanded, love_owed, other_gods_barred, coveting_barred on israel_people; borders_declared on the land of Canaan), the effects naming the rain, the heavens or the yoke on israel_people (THE HOLE FILLED — this sitting\\'s three alone), the vocabulary\\'s rain effects, the retelling\\'s lines (plague_struck, sea_split, sea_returned, all_flesh_expired, earth_swallowed, korach_named, shema_declared)) = %s' % (got,)
'''
a = "\nprint('READBACK PROBES (THE LOOP step 6, the first form)')"
assert s.count(a) == 1
s = s.replace(a, NEW + a)
old = "('Q27 the four own-day lines and their writes; the kin stands; the daemon', q27)):"
assert s.count(old) == 1
s = s.replace(old, "('Q27 the four own-day lines and their writes; the kin stands; the daemon', q27), ('Q28 chapter 11\\'s table — the forms on file, no new form', q28), ('Q29 the two own-day lines and their five writes; no marker; the debit open; the daemon', q29), ('Q30 the kin stands; the rain\\'s hole filled', q30)):")
old2 = "Run: python3 World/step9/readback_probes.py"
assert s.count(old2) == 1
s = s.replace(old2, "  THE DEUTERONOMY WALK 9b (2026-09-20; DEUTERONOMY_WALK.md \"Sitting 9b\" THE PROBES) — written to FAIL before cold_run_blessing_and_curse.py exists:\n  Q28 chapter 11's table — THE FORMS ON FILE, NO NEW FORM (the discipline retold 11:1-7, the land watered by heaven 11:8-12, the second paragraph 11:13-21, the borders and the dread 11:22-25, the blessing and the curse 11:26-32): thirty-two rows predicted from the design, one per verse (VERBATIM 7 / VARIANT 19 / EXPANDED 4 / SUPPLIED 2; eleven on the tape by kind and first verse, nineteen in the kin's cells by CALL — retyped once from the print if the census moves); the state row 11:5 SUPPLIED with NO write (chapter 8's fifth form); the ceremony row 11:29 SUPPLIED WITH THE WRITE gerizim_ebal_ceremony_owed (the debit's first seat — no tape line to reference, Joshua 8:30-35 the run); the pointer row 11:25 (Exodus 23:27 by the Sifrei 52:4 and Tosefta Sotah 8:6); no hole, no open row, no stretch, no retrograde row\n  Q29 the two OWN-DAY lines second_paragraph_declared (11:13-21) and blessing_and_curse_set (11:26-32) after the tape's last Deuteronomy 10 line on the counter's day (40, 11, 1), no dated field, NO marker at any Deut 11 verse (markers 172 UNMOVED); their five writes on israel_people ONE each — rain_in_its_season and heavens_shut_for_turning (conditional HEAVEN entries), yoke_of_the_commandments_accepted and blessing_and_curse_set (statuses), gerizim_ebal_ceremony_owed (a DEBIT OPEN toward Heaven — the open debits on israel_people 10); the daemon law_blessing_and_curse registered, given_at Deut 11:1, installed_by boot\n  Q30 the kin stands — shema_commanded, test_barred, blessings_for_hearing, pity_barred, fear_of_heaven_asked, cleaving_commanded, love_owed, other_gods_barred, coveting_barred ONE each on israel_people, borders_declared ONE on the land of Canaan UNMOVED (no second shema line, no second block at 11:16); THE RAIN'S HOLE FILLED — the effects naming the rain, the heavens or the yoke on israel_people this sitting's three alone, the vocabulary's rain effects fire_rained and rain_in_its_season; the retelling's lines unmoved (plague_struck ten, sea_split, sea_returned, all_flesh_expired, earth_swallowed one with korach_named False, shema_declared one)\n" + old2)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched readback_probes.py: Q28-Q30 added (written to FAIL); compiles')
