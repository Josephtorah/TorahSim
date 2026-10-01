import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 22b (2026-09-30): readback_probes.py Q51 written to FAIL before cold_run_moses_death.py exists (the design's THE PROBE paragraph — the FIRST step after the
# design: 7b's lesson 2; ONE probe in the lean form): the SIX OWN-DAY lines after the tape's last Deuteronomy 33 line — ALL on MOSES' LAST DAY (40, 12, 7), NO MARKER in the chapter
# (markers 173 UNMOVED); their writes — the twelve NEW effects ONE each on their subjects (moses, israel_people, yehoshua) with their lines' first verses; THE THREE REUSES' counts
# after (the spec's KIN_AFTER); no block; no heaven entry; the daemon registered; the readback's twelve rows one per verse in order with THE THREE POINTER ROWS 34:4, 34:5, 34:6 and no
# state, open or stretch row; the kin's counts as the spec computed them. THE LITERALS GENERATED FROM THE SPEC MODULE (ch34b_spec.py), never typed twice. Idempotent.
# patch_probes_ch33.py's form. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad.
import os, sys, subprocess
ROOT = _ROOT
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ch34b_spec as S
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
assert 'def q51():' not in s, 'already patched'
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:90]); s = s.replace(old, new)
W = 'THE DEUTERONOMY WALK 22b (2026-09-30)'
OWN = tuple(S.KINDS)
WN = [(e, l[1], sub) for l in S.LINES for e, _, sub in l[7]]
RE = [(e, S.REUSE_AFTER[e]) for e in S.REUSE_NAMES]
HEAVEN = tuple((e, sub) for e, op, sub in S.NEW_E if op == 'heaven'); BLOCKS = tuple((e, sub) for e, op, sub in S.NEW_E if op == 'block')
KIN = tuple(S.KIN); KINV = tuple(S.KIN_AFTER[k] for k in KIN)
c = S.counts()
VERSES = ['Deut 34:%d' % v for v in range(1, 13)]
assert S.MARKER is None and not BLOCKS and not HEAVEN and len(RE) == 3
Q51 = f'''
def q51():
    import yaml as _y, cold_run_{S.RUNNER} as CR
    def ENT(*names):
        for n_ in names:
            if n_ in W.entities: return W.entities[n_]
        return None
    def L(ent, eff):
        e_ = ENT(ent); return [e for e in e_.ledger if e['effect'] == eff] if e_ else []
    def nall(eff): return sum(1 for ent in W.entities.values() for e in ent.ledger if e['effect'] == eff)
    OWN = {OWN!r}
    own = [e for e in EV if e[2]['kind'] in OWN]
    idx = {{id(l): i for i, l in enumerate(W.log)}}
    i_last33 = max([i for i, l in enumerate(W.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 33:')] or [-1])
    after = bool(own) and all(idx[id(e)] > i_last33 for e in own)
    mk34 = [l for l in W.log if l[0] == 'MARKER' and str(l[2].get('verse', '')).startswith('Deut 34:')]; nm = len([l for l in W.log if l[0] == 'MARKER'])
    days = sorted({{ex.date(e[1]) for e in own}}); dated = sum(1 for e in own if e[2].get('dated') is not None)
    WN = {WN!r}
    RE = {RE!r}
    FV = lambda t_: '%s %d:%d' % t_ if isinstance(t_, tuple) else str(t_)
    wn = tuple((len(L(sub, eff)), FV(WE.first_verse(str(L(sub, eff)[0].get('case_source', '')))) if L(sub, eff) else None) for eff, _, sub in WN)
    re_ = tuple(nall(e) for e, _ in RE)
    blocks = sum(1 for eff, _, sub in WN for e in L(sub, eff) if e.get('op') == 'block')
    heaven = sum(1 for eff, _, sub in WN for e in L(sub, eff) if e.get('op') == 'heaven')
    KIN = {KIN!r}
    kin = tuple(nall(k) for k in KIN)
    rows = CR.DATA['the_readback']['value']
    rb = (len(rows), [r['verses'] for r in rows] == {VERSES!r}, [r['verses'] for r in rows if r.get('pointer')], [r['verses'] for r in rows if r.get('state')], any(r.get('open') for r in rows), any(r.get('stretch') for r in rows))
    dd = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon_dispositions.yaml'), encoding='utf-8'))
    d = dd['daemons'].get('{S.DAEMON}', {{}})
    got = ([e[2]['kind'] for e in own], after, len(mk34), nm, days, dated, wn, re_, blocks, heaven, kin, rb, '{S.DAEMON}' in dd['daemons'], d.get('given_at'), d.get('installed_by'))
    return got == (list(OWN), True, 0, 173, [{S.DAY!r}], 0, tuple((1, v_) for _, v_, _ in WN), tuple(n_ for _, n_ in RE), 0, 0, {KINV!r}, ({len(VERSES)}, True, {S.POINTER_ROWS!r}, {S.STATE_ROWS!r}, False, False), True, '{S.GIVEN_AT}', '{S.INSTALLED_BY}'), 'got (the six own-day lines in the ink\\'s order, all after the tape\\'s last Deuteronomy 33 line, no marker at Deut 34, markers 173, their days (Moses\\' last day (40, 12, 7) alone), dated fields (none), the NEW writes on their subjects with their lines\\' first verses, the three reuses\\' counts after, no block, no heaven entry, the kin\\'s counts (the three moved by one, the rest unmoved), the readback (rows, one per verse in order, the three pointer rows 34:4, 34:5, 34:6, no state row, open, stretch), the daemon registered, given_at, installed_by) = %s' % (got,)
'''
rep("\nprint('READBACK PROBES (THE LOOP step 6, the first form)')", Q51 + "\nprint('READBACK PROBES (THE LOOP step 6, the first form)')")
OLD = "the readback\\'s twenty-nine rows with the two pointer rows 33:5 and 33:28 paid, the daemon — LEAN', q50)"
assert s.count(OLD) == 1, s.count(OLD)
s = s.replace(OLD, OLD + ", ('Q51 chapter 34\\'s six own-day lines in two forms on Moses\\' last day with no marker, their %d new writes on moses, Israel\\'s and Joshua\\'s ledgers and three reuses at their forward seats, no block, no heaven entry, the kin as computed, the readback\\'s twelve rows with the three pointer rows 34:4, 34:5, 34:6 paid, the daemon — LEAN, THE BOOK\\'S LAST', q51)" % len(WN))
lines = s.split('\n'); k = [i for i, l in enumerate(lines) if l.startswith('  THE DEUTERONOMY WALK 21b (2026-09-29) (DEUTERONOMY_WALK.md "Sitting 21b" THE PROBES')]; assert len(k) == 1, k
lines.insert(k[0], '  %s (DEUTERONOMY_WALK.md "Sitting 22b" THE PROBE; THE LEAN PASS; THE BOOK\'S LAST) — written to FAIL before cold_run_%s.py exists: Q51 the SIX OWN-DAY lines %s after the tape\'s last Deuteronomy 33 line — ALL on MOSES\' LAST DAY (40, 12, 7), 19b\'s marker at Deut 31:1; NO MARKER in the chapter (the death on the marker\'s day; the thirty days of weeping a DURATION — the counter unmoved by the design\'s ruling; markers 173 UNMOVED), no dated field on the lines; their writes — the %d NEW ONE each on their subjects (%s; all STATUSES, no BLOCK, no HEAVEN entry) and THREE REUSES at their own forward seats (%s — the counts after); the kin\'s counts as the spec computed them on the one database; the readback\'s twelve rows one per verse in order with THE THREE POINTER ROWS at 34:4, 34:5 and 34:6 (the song\'s two and the blessing\'s one PAID — grade R) and NO state, open or stretch row; the daemon %s registered, given_at %s, installed_by %s (ONE probe — the lean form)' % (W, S.RUNNER, ', '.join('%s (%s)' % (l[0], l[2]) for l in S.LINES), len(WN), ', '.join('%d on %s' % (n, k_) for k_, n in c['subjects_new'].items()), ', '.join('%s %d' % (e, n) for e, n in RE), S.DAEMON, S.GIVEN_AT, S.INSTALLED_BY))
s = '\n'.join(lines)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched: Q51 written (to FAIL until the runner and the tape carry chapter 34); the file compiles; the literals from the spec — %d new writes, %d reuses, %d kin counts, %d readback verses, %d pointer rows' % (len(WN), len(RE), len(KIN), len(VERSES), len(S.POINTER_ROWS)))
