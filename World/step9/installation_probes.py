#!/usr/bin/env python3
"""installation_probes.py — THE LOOP's step 3 fire-probes (2026-09-09; THE_LOOP.md "Step 3 INSTALLATION — the design", the
decisions D1-D6), written BEFORE the engine's dispatch gate, the tent daemon and the gate's field check. Against the unchanged
engine every probe must FAIL; after the code every probe must PASS. All six run in-process on a SMALL probe world over
REGISTERED kinds only (the tape's registry refuses a probe-only type): the covenant's blood (Exod 24:8), the call from the tent
(Lev 1:1), the people's answer as a stand-in law event, the blasphemer's own case kind (cursed_the_name) as the uncovered case,
Joseph's custody_three_days standing in for the custody act, Marah's statute_set as the tent's output act. The probe daemons'
two fields are given EXPLICITLY (the dispositions' rows belong to the real daemons); the real tent daemon (world_engine.law_tent)
is registered first, as the sequence runner registers it. Six probes:
  I1 under from_event a law whose installing act has not fired is SKIPPED — a SKIP log line (why not_in_force), no write, the
     daemon's skipped count 1; the line sinks to the journal as run.skip and the register carries the kind
  I2 after the act fires the institution's ledger carries in_force (written_by law_tent, the act's verse) and the law FIRES
  I3 in force needs BOTH: the institution stands but the tape has not reached the law's given_at — skipped as not_given;
     after a marker past the verse, it fires
  I4 under boot NOTHING is skipped, no SKIP line exists, and the would-skip count equals the from_event world's skips; a world
     that did not opt in has no installation, no SKIP line and no in_force write (the exam bench, D1)
  I5 the daemon gate's field check refuses a daemon missing either field, or naming an act that is not an installing act, and
     passes the real dispositions file with zero fails
  I6 custody and the case-born installation: the uncovered case carries fired_by [] and a SKIP line; the custody act writes
     in_custody on the person and declaration_owed OPEN on the court's docket; the output act writes rule_installed naming the
     law whose own act never fires, closes the docket's debit, and that law fires on the next case
Not run by the sweep; run by hand at the sitting and after any engine edit. Run: python3 World/step9/installation_probes.py
"""
import os, sys, tempfile, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import world_engine as WE

results = []


def probe(name):
    def deco(fn):
        try:
            ok, note = fn()
        except BaseException as e:                   # the old engine lacks the construct: a FAIL, named
            ok, note = False, '%s: %s' % (type(e).__name__, str(e)[:200])
        results.append((name, bool(ok), note))
        return fn
    return deco


def _eff(effect, subject, event, **kw):
    d = {'effect': effect, 'subject': subject, 'counterparty': None, 'amount': None, 'due': None,
         'source_law': 'probe', 'case_source': event['case_source']}
    d.update(kw)
    return d


# ---- the probe daemons (their fields below; registered kinds only) ----
def law_probe_covenant(event, world):
    """a Sinai law: given at Exod 21:2, installed by the covenant's blood (Exod 24:8)"""
    if event['kind'] == 'people_answered':
        return [_eff('accepted', event['subject'], event)]
    return []


def law_probe_tent_law(event, world):
    """a Leviticus law: given at Lev 5:20, installed by the call from the tent (Lev 1:1)"""
    if event['kind'] == 'people_answered':
        return [_eff('accepted', event['subject'], event, value='tent')]
    return []


def law_probe_case(event, world):
    """the case-born law: given at Lev 24:10; its installing act (entered_the_land) never fires on this tape — it is installed
    only by the tent's output (rule_installed naming it)"""
    if event['kind'] == 'cursed_the_name':
        return [_eff('stoned', event['subject'], event)]
    return []


def law_probe_tent(event, world):
    """the probe's stand-in for the tent daemon's two Numbers branches: the custody act and the output act"""
    k = event['kind']
    if k == 'custody_three_days':
        person = event['subject']
        return [_eff('in_custody', person, event),
                _eff('declaration_owed', 'the-court', event, counterparty=person)]
    if k == 'statute_set':
        world.close('the-court', 'declaration_owed', event['case_source'])
        return [_eff('rule_installed', 'the-tabernacle', event, value='law_probe_case')]
    return []


FIELDS = {
    'law_tent':           {'given_at': 'Exod 18:25', 'installed_by': 'boot'},
    'law_probe_covenant': {'given_at': 'Exod 21:2', 'installed_by': 'covenant_blood_thrown'},
    'law_probe_tent_law': {'given_at': 'Lev 5:20', 'installed_by': 'called_from_the_tent'},
    'law_probe_case':     {'given_at': 'Lev 24:10', 'installed_by': 'entered_the_land'},
    'law_probe_tent':     {'given_at': 'Lev 24:12', 'installed_by': 'boot'},
}
REG = {'the-tabernacle': 'the_tent_of_meeting', 'the-court': 'the_court', 'the-covenant': 'the_covenant_at_sinai'}


def probe_world(setting, opt_in=True, tent=True):
    """the probe tape: the covenant's law before and after the blood; the tent's law before and after the call and before and
    after its verse; the uncovered case, the custody act, the output act, the case again"""
    laws = ([WE.law_tent] if tent else []) + [law_probe_covenant, law_probe_tent_law, law_probe_case, law_probe_tent]
    kw = {'installation': {'setting': setting, 'fields': FIELDS}} if opt_in else {}
    w = WE.World(era='probe', epoch='count', registry=REG, **kw)
    w.laws = laws
    w.marker('Exod 21:1', 10, value='the ordinances')
    w.submit({'kind': 'people_answered', 'subject': 'the-people', 'case_source': 'Exod 21:2 — probe: before the blood'})       # I1: skipped
    w.submit({'kind': 'covenant_blood_thrown', 'subject': 'the-people', 'case_source': 'Exod 24:8 — probe: the blood'})        # law_tent: in_force
    w.submit({'kind': 'people_answered', 'subject': 'the-people', 'case_source': 'Exod 24:7 — probe: after the blood'})        # I2: fires
    w.submit({'kind': 'called_from_the_tent', 'subject': 'moses', 'case_source': 'Lev 1:1 — probe: the call'})                  # law_tent: in_force
    w.submit({'kind': 'people_answered', 'subject': 'the-people', 'case_source': 'Lev 4:1 — probe: before the verse'})         # I3: not_given
    w.marker('Lev 6:1', 30, value='the priests')
    w.submit({'kind': 'people_answered', 'subject': 'the-people', 'case_source': 'Lev 6:2 — probe: after the verse'})          # I3: fires
    w.submit({'kind': 'cursed_the_name', 'subject': 'the-blasphemer', 'case_source': 'Lev 24:11 — probe: the uncovered case'})   # I6: skipped, fired_by []
    w.submit({'kind': 'custody_three_days', 'subject': 'the-blasphemer', 'case_source': 'Lev 24:12 — probe: the custody act'})  # I6: the halt
    w.submit({'kind': 'statute_set', 'subject': 'moses', 'case_source': 'Lev 24:13 — probe: the output'})                       # I6: the output
    w.submit({'kind': 'cursed_the_name', 'subject': 'the-blasphemer', 'case_source': 'Lev 24:14 — probe: the case again'})       # I6: fires
    return w


def skips(w):
    return [l for l in w.log if l[0] == 'SKIP']


def entries(w, token, effect):
    ent = w.entities.get(REG.get(token, token))
    return [e for e in (ent.ledger if ent else []) if e['effect'] == effect]


@probe('I1 under from_event a law whose act has not fired is SKIPPED: a SKIP line, no write, skipped count 1, run.skip in the journal')
def i1():
    w = probe_world('from_event')
    s = skips(w)
    first = [l for l in s if l[2].get('daemon') == 'law_probe_covenant' and l[2].get('why') == 'not_in_force']
    acc = [e for e in entries(w, 'the-people', 'accepted') if e['case_source'].startswith('Exod 21:2')]
    cov = w.watch['law_probe_covenant'].get('skipped')
    import world_journal as WJ
    d = tempfile.mkdtemp()
    path, n, coerced = WJ.sink(w, source='installation_probes/from_event', out_dir=d)
    db = os.path.join(d, 'probe.sqlite'); WJ.index(db, [path]); c = WJ.counts(db)
    ok = bool(first) and not acc and cov == 1 and c.get('run.skip') == len(s) and 'run.skip' in WJ.KINDS.values()
    return ok, 'skips %d (the covenant law not_in_force at Exod 21:2: %s); accepted at 21:2: %d; skipped count %r; journal run.skip %r' % (
        len(s), bool(first), len(acc), cov, c.get('run.skip'))


@probe('I2 after the act fires the institution carries in_force (written_by law_tent, the act\'s verse) and the law FIRES')
def i2():
    w = probe_world('from_event')
    inf = entries(w, 'the-covenant', 'in_force')
    acc = [e for e in entries(w, 'the-people', 'accepted') if e['case_source'].startswith('Exod 24:7')]
    ok = len(inf) == 1 and inf[0].get('written_by') == 'law_tent' and inf[0].get('value') == 'covenant_blood_thrown' \
        and inf[0]['case_source'].startswith('Exod 24:8') and len(acc) == 1 and acc[0].get('written_by') == 'law_probe_covenant'
    return ok, 'in_force on the covenant: %d (%s, value %r); the law fired after the blood: %d' % (
        len(inf), inf[0].get('written_by') if inf else None, inf[0].get('value') if inf else None, len(acc))


@probe('I3 in force needs BOTH: the tent stands but the verse is not reached — not_given; after the marker it fires')
def i3():
    w = probe_world('from_event')
    # a law given later is skipped as not_given on EVERY earlier event (the design's own semantics — the law does not exist yet);
    # the probe reads the skip AT THE VERSE where the institution already stands, and the silence after the marker
    ng_all = [l for l in skips(w) if l[2].get('daemon') == 'law_probe_tent_law' and l[2].get('why') == 'not_given' and l[2].get('needs') == 'Lev 5:20']
    ng = [l for l in ng_all if str(l[2].get('case_source', '')).startswith('Lev 4:1')]
    late = [l for l in skips(w) if l[2].get('daemon') == 'law_probe_tent_law' and str(l[2].get('case_source', '')).startswith('Lev 6:2')]
    inf = entries(w, 'the-tabernacle', 'in_force')
    before = [e for e in entries(w, 'the-people', 'accepted') if e.get('value') == 'tent' and e['case_source'].startswith('Lev 4:1')]
    after = [e for e in entries(w, 'the-people', 'accepted') if e.get('value') == 'tent' and e['case_source'].startswith('Lev 6:2')]
    ok = len(ng) == 1 and not late and len(inf) == 1 and not before and len(after) == 1 and all(l[2]['why'] == 'not_given' for l in ng_all)
    return ok, 'not_given skips: %d at Lev 4:1 (with the tent standing), %d on every earlier event, %d after the marker; in_force on the tent %d; fired before the verse %d, after %d' % (
        len(ng), len(ng_all), len(late), len(inf), len(before), len(after))


@probe('I4 under boot nothing is skipped and the would-skip count equals from_event\'s skips; a world not opted in has no installation, no SKIP, no in_force')
def i4():
    wf = probe_world('from_event')
    wb = probe_world('boot')
    wn = probe_world(None, opt_in=False, tent=False)
    rb = wb.installation_report()
    ok = not skips(wb) and rb['would_skip'] == len(skips(wf)) and rb['skipped'] == 0 and rb['setting'] == 'boot' \
        and wn.installation is None and not skips(wn) and not entries(wn, 'the-covenant', 'in_force') \
        and len([e for e in entries(wn, 'the-people', 'accepted')]) == 8
    return ok, 'boot: skips %d, would_skip %d (from_event skipped %d); no opt-in: installation %r, skips %d, in_force %d, accepted %d' % (
        len(skips(wb)), rb['would_skip'], len(skips(wf)), wn.installation, len(skips(wn)), len(entries(wn, 'the-covenant', 'in_force')),
        len(entries(wn, 'the-people', 'accepted')))


@probe('I5 the gate refuses a daemon missing a field or naming a non-installing act; the real file passes with zero fails')
def i5():
    import daemon_census as DC
    bad = {'law_a': {'file': 'x.py', 'installed_by': 'boot'},                                   # no given_at
           'law_b': {'file': 'x.py', 'given_at': 'Exod 21:2'},                                 # no installed_by
           'law_c': {'file': 'x.py', 'given_at': 'Exod 21:2', 'installed_by': 'plague_struck'},   # a registered kind, not an installing act
           'law_d': {'file': 'x.py', 'given_at': 'nowhere', 'installed_by': 'boot'},           # an unparseable verse
           'law_e': {'file': 'x.py', 'given_at': 'Lev 24:10', 'installed_by': 'pending'}}      # pending without a why
    f_bad = DC.check_installation(bad)
    real = DC.load_yaml()[0]
    f_real = DC.check_installation(real)
    pend = [n for n, d in real.items() if d.get('installed_by') == 'pending']
    ok = len(f_bad) == 5 and not f_real and len(real) == 66 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 4b (2026-09-17): 65 -> 66, law_hear_o_israel (given_at Deut 6:4 — the Shema's own giving; installed_by boot); 3b: 64 -> 65, law_covenant_at_horeb (given_at Exod 20:3 — the second word's first giving, compiled from its second copy; installed_by covenant_blood_thrown); 2b: 63 -> 64, law_obey_horeb (installed_by boot — a law in Moses' voice with no divine frame, the class named); 1b: 62 -> 63, law_opening_speech (installed_by boot — a law in Moses' voice with no divine frame, the class named); 15b: 61 -> 62, law_refuge (installed_by boot — a law in the divine voice in the plains of Moab, the class named); 14b: 60 -> 61, law_borders (installed_by boot — a law in the divine voice relayed at 34:13 in 36:5's form, the class named); 13b: 59 -> 60, law_journeys (installed_by boot — a law in the divine voice spoken in the plains of Moab, the class named); 12b: 58 -> 59, law_gad_reuben (installed_by boot — a stipulation in Moses' voice with no divine frame, 30:2's class named); 11b: 57 -> 58, law_midian (installed_by boot — the third relayed form, the priest's voice citing Moses, the class named); 10b: 56 -> 57, law_vows (installed_by boot — the form for a law in Moses' voice, the class named); 9b: 55 -> 56, law_musafim; 8b: 54 -> 55, law_second_census; 7b: 53 -> 54, law_balak; 6b: 52 -> 53, law_chukat; 5b: 51 -> 52, law_korach; 4b: 50 -> 51, law_shelach; 3b: 49 -> 50, law_beha; 2b: 48 -> 49, law_naso; 1b: 47 -> 48, law_census; THE TENT sitting 4: 46 -> 47, law_zelophehad; sitting 3: 45 -> 46, law_mekoshesh
    return ok, 'bad rows refused %d of 5; real file: %d daemons, fails %d, pending %s' % (len(f_bad), len(real), len(f_real), pend)


@probe('I6 custody and the case-born installation: fired_by [], in_custody + declaration_owed OPEN, rule_installed closes it, the law then fires')
def i6():
    w = probe_world('from_event')
    ev = [l[2] for l in w.log if l[0] == 'EVENT' and l[2]['kind'] == 'cursed_the_name']
    first_fb, second_fb = ev[0].get('fired_by'), ev[1].get('fired_by')
    # the case law is consulted on EVERY event once its verse is reached — skipped not_in_force at 24:11, 24:12 and 24:13 (the output's own
    # dispatch: the probe tent daemon writes rule_installed AFTER the case law was consulted), in force from the next event; the probe reads
    # the skip at the case's verse and the silence at the case again
    sk = [l for l in skips(w) if l[2].get('daemon') == 'law_probe_case' and l[2].get('why') == 'not_in_force' and str(l[2].get('case_source', '')).startswith('Lev 24:11')]
    sk_after = [l for l in skips(w) if l[2].get('daemon') == 'law_probe_case' and str(l[2].get('case_source', '')).startswith('Lev 24:14')]
    cust = entries(w, 'the-blasphemer', 'in_custody')
    owed = entries(w, 'the-court', 'declaration_owed')
    rule = entries(w, 'the-tabernacle', 'rule_installed')
    stoned = entries(w, 'the-blasphemer', 'stoned')
    ok = first_fb == [] and second_fb == ['law_probe_case'] and len(sk) == 1 and not sk_after and len(cust) == 1 and len(owed) == 1 \
        and owed[0].get('open') is False and str(owed[0].get('closed_by', '')).startswith('Lev 24:13') and owed[0].get('counterparty') == 'the-blasphemer' \
        and len(rule) == 1 and rule[0].get('value') == 'law_probe_case' and len(stoned) == 1 and stoned[0]['case_source'].startswith('Lev 24:14')
    return ok, 'fired_by first %r second %r; skips of the case law %d; in_custody %d; declaration_owed %d (open %r, closed_by %r); rule_installed %d; stoned %d' % (
        first_fb, second_fb, len(sk), len(cust), len(owed), owed[0].get('open') if owed else None, (owed[0].get('closed_by') or '')[:9] if owed else None, len(rule), len(stoned))


if __name__ == '__main__':
    n_ok = sum(1 for _, ok, _ in results if ok)
    for name, ok, note in results:
        print('  %s  %s\n        %s' % ('PASS' if ok else 'FAIL', name, note))
    print('INSTALLATION PROBES: %d/%d' % (n_ok, len(results)))
    assert results, 'ZERO-REPORT: no probe ran'
    sys.exit(0 if n_ok == len(results) else 1)
