import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 18b (2026-09-26): readback_probes.py Q47 written to FAIL before cold_run_firstfruits_ebal_curses.py exists (the design's THE PROBES paragraph — the
# FIRST step after the design: 7b's lesson 2; ONE probe in the lean form): the TWENTY-ONE OWN-DAY lines after the tape's last Deuteronomy 25 line on the counter's day
# (40, 11, 1), no dated field, NO marker at any Deut 26-28 verse (markers 172 UNMOVED); their writes — the ninety-one NEW ONE each on israel_people with their lines'
# first verses and the five reuses' counts after; the five blocks; the fifty-three heaven entries; the daemon registered; the readback's one hundred and fourteen rows
# one per verse in order with the state row at 28:1 and 28:15 and the two pointer rows at 28:3 and 28:68, no open, no stretch row; the kin's counts of DL4 unmoved.
# THE LITERALS GENERATED FROM THE SPEC MODULE (ch26b_spec.py), never typed twice. Idempotent. patch_probes_ch22.py's form. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad.
import subprocess, os, sys
ROOT = _ROOT
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ch26b_spec as S
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
assert 'def q47():' not in s, 'already patched'
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:90]); s = s.replace(old, new)
W = 'THE DEUTERONOMY WALK 18b (2026-09-26)'
OWN = tuple(S.KINDS)
W91 = [(e, l[1]) for l in S.LINES for e, _ in l[6]]
RE = [(e, S.REUSE_AFTER[e]) for e in S.REUSE_AFTER]
BLOCKS = tuple(e for e, op in S.NEW_E if op == 'block'); HEAVEN = tuple(e for e, op in S.NEW_E if op == 'heaven')
KIN = tuple(S.KIN_UNMOVED); KINV = tuple(S.KIN_UNMOVED[k] for k in KIN)
c = S.counts()
VERSES = ['Deut 26:%d' % v for v in range(1, 20)] + ['Deut 27:%d' % v for v in range(1, 27)] + ['Deut 28:%d' % v for v in range(1, 70)]
Q47 = f'''
def q47():
    import yaml as _y, cold_run_{S.RUNNER} as FE
    def ENT(*names):
        for n_ in names:
            if n_ in W.entities: return W.entities[n_]
        return None
    def L(ent, eff):
        e_ = ENT(*ent) if isinstance(ent, tuple) else ENT(ent); return [e for e in e_.ledger if e['effect'] == eff] if e_ else []
    def nall(eff): return sum(1 for ent in W.entities.values() for e in ent.ledger if e['effect'] == eff)
    OWN = {OWN!r}
    own = [e for e in EV if e[2]['kind'] in OWN]
    idx = {{id(l): i for i, l in enumerate(W.log)}}
    i_last25 = max([i for i, l in enumerate(W.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 25:')] or [-1])
    after = bool(own) and all(idx[id(e)] > i_last25 for e in own)
    mk26 = [l for l in W.log if l[0] == 'MARKER' and str(l[2].get('verse', '')).startswith(('Deut 26:', 'Deut 27:', 'Deut 28:'))]; nm = len([l for l in W.log if l[0] == 'MARKER'])
    days = sorted({{ex.date(e[1]) for e in own}}); dated = sum(1 for e in own if e[2].get('dated') is not None)
    W91 = {W91!r}
    RE = {RE!r}
    BLOCKS = {BLOCKS!r}
    HEAVEN = {HEAVEN!r}
    FV = lambda t_: '%s %d:%d' % t_ if isinstance(t_, tuple) else str(t_)
    w91 = tuple((len(L('israel_people', eff)), FV(WE.first_verse(str(L('israel_people', eff)[0].get('case_source', '')))) if L('israel_people', eff) else None) for eff, _ in W91)
    re_ = tuple(len(L('israel_people', eff)) for eff, _ in RE)
    blocks = sum(1 for eff in BLOCKS for e in L('israel_people', eff) if e.get('op') == 'block')
    heaven = sum(1 for eff in HEAVEN for e in L('israel_people', eff) if e.get('op') == 'heaven')
    KIN = {KIN!r}
    kin = tuple(nall(k) for k in KIN)
    rows = FE.DATA['the_readback']['value']
    rb = (len(rows), [r['verses'] for r in rows] == {VERSES!r}, [r['verses'] for r in rows if r.get('pointer')], [r['verses'] for r in rows if r.get('state')], any(r.get('open') for r in rows), any(r.get('stretch') for r in rows))
    dd = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon_dispositions.yaml'), encoding='utf-8'))
    d = dd['daemons'].get('{S.DAEMON}', {{}})
    got = ([e[2]['kind'] for e in own], after, len(mk26), nm, days, dated, w91, re_, blocks, heaven, kin, rb, '{S.DAEMON}' in dd['daemons'], d.get('given_at'), d.get('installed_by'))
    return got == (list(OWN), True, 0, 172, [(40, 11, 1)], 0, tuple((1, v_) for _, v_ in W91), tuple(n_ for _, n_ in RE), {len(BLOCKS)}, {len(HEAVEN)}, {KINV!r}, ({len(VERSES)}, True, ['Deut 28:3', 'Deut 28:68'], ['Deut 28:1', 'Deut 28:15'], False, False), True, '{S.GIVEN_AT}', '{S.INSTALLED_BY}'), 'got (the twenty-one own-day lines in the ink\\'s order, all after the tape\\'s last Deuteronomy 25 line, markers at Deut 26-28 (none), markers, their day, dated fields (none), the ninety-one NEW writes on israel_people with their lines\\' first verses, the five reuses\\' counts after (the rejoicing 4, the poor tithe 2, the blessings for hearing 3, the rain 2), the five blocks, the fifty-three heaven entries, the kin\\'s counts unmoved (as the recon and the callees read them — the ceremony owed, the pair set, the heavens shut, the treasure, the second tithe, the Levite, the pilgrimages, the hand blessed, the bribe, the landmark, the triad, the father\\'s wife, the return to Egypt, the horses, the witnesses, forgetting, the house\\'s abomination, hears and fears, the Shema, the covenants, the stars, the bondage, the cry, the plagues, the molten image, the yoke, the grace, the fleece, the scattering, the desolation, the sevenfold, the sabbath debt, put to death, stoned, the terumah of the tithe, the tithe granted, confessed, the altars), the readback (rows, one per verse in order, the pointer rows 28:3 and 28:68, the state rows 28:1 and 28:15, open, stretch), the daemon registered, given_at, installed_by) = %s' % (got,)
'''
rep("\nprint('READBACK PROBES (THE LOOP step 6, the first form)')", Q47 + "\nprint('READBACK PROBES (THE LOOP step 6, the first form)')")
rep("the readback\\'s ninety-six rows, the daemon — LEAN', q46)", "the readback\\'s ninety-six rows, the daemon — LEAN', q46), ('Q47 chapters 26-28\\'s twenty-one own-day lines, their ninety-one writes and five reuses, the five blocks and the fifty-three heaven entries, the kin unmoved, the readback\\'s one hundred and fourteen rows with the state row and the two pointer rows, the daemon — LEAN', q47)")
lines = s.split('\n'); k = [i for i, l in enumerate(lines) if l.startswith('  THE DEUTERONOMY WALK 17b (2026-09-26) (DEUTERONOMY_WALK.md "Sitting 17b" THE PROBES')]; assert len(k) == 1, k
lines.insert(k[0], '  %s (DEUTERONOMY_WALK.md "Sitting 18b" THE PROBES; THE LEAN PASS) — written to FAIL before cold_run_%s.py exists: Q47 the TWENTY-ONE OWN-DAY lines %s after the tape\'s last Deuteronomy 25 line on the counter\'s day (40, 11, 1), no dated field, NO marker at any Deut 26-28 verse (markers 172 UNMOVED — chapter 27\'s three frames are the lines\' speaker, "that day" the counter\'s); their writes — the NINETY-ONE NEW ONE each on israel_people (thirty-three STATUSES, five BLOCKS, fifty-three HEAVEN entries) and the FIVE REUSES\' further entries (rejoicing_before_the_lord_commanded at 26:11 and 27:7 — 2 -> 4; poor_tithe_owed at 26:12 — 1 -> 2; blessings_for_hearing at 28:1 — 2 -> 3; rain_in_its_season at 28:12 — 1 -> 2); the kin\'s counts UNMOVED (the references — no second write); the readback\'s one hundred and fourteen rows one per verse in order with THE STATE ROW at 28:1 and 28:15 (the hearkening\'s two arms) and THE TWO POINTER ROWS at 28:3 (the referent of 15:6 PAID) and 28:68 (the run citation of 17:16), no open or stretch row; the daemon %s registered, given_at %s, installed_by %s (ONE probe — the lean form)' % (W, S.RUNNER, ', '.join('%s (%s)' % (l[0], l[2]) for l in S.LINES), S.DAEMON, S.GIVEN_AT, S.INSTALLED_BY))
s = '\n'.join(lines)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched: Q47 written (to FAIL until the runner and the tape carry chapters 26-28); the file compiles; the literals from the spec — %d new writes, %d reuses, %d blocks, %d heaven, %d kin counts, %d readback verses' % (len(W91), len(RE), len(BLOCKS), len(HEAVEN), len(KIN), len(VERSES)))
