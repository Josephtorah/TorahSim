import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 21b (2026-09-29): readback_probes.py Q50 written to FAIL before cold_run_blessing_of_moses.py exists (the design's THE PROBES paragraph — the
# FIRST step after the design: 7b's lesson 2; ONE probe in the lean form): the ELEVEN OWN-DAY lines after the tape's last Deuteronomy 32 line — ALL on MOSES' LAST DAY
# (40, 12, 7), NO MARKER in the chapter (markers 173 UNMOVED); their writes — the NEW effects ONE each on their subjects (Israel, the tribes' own ledgers as Genesis 49's
# testament wrote them) with their lines' first verses; NO reuse; no block; no heaven entry; the daemon registered; the readback's twenty-nine rows one per verse in order with
# THE TWO POINTER ROWS at 33:5 and 33:28 (20b's owed pointers PAID) and no state, open or stretch row; the kin's counts unmoved. THE LITERALS GENERATED FROM THE SPEC MODULE
# (ch33b_spec.py), never typed twice. Idempotent. patch_probes_ch32.py's form. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad.
import subprocess, os, sys
ROOT = _ROOT
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ch33b_spec as S
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
assert 'def q50():' not in s, 'already patched'
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:90]); s = s.replace(old, new)
W = 'THE DEUTERONOMY WALK 21b (2026-09-29)'
OWN = tuple(S.KINDS)
WN = [(e, l[1], sub) for l in S.LINES for e, _, sub in l[7]]
RE = [(e, S.REUSE_AFTER[e]) for e in S.REUSE_AFTER]
BLOCKS = tuple((e, sub) for e, op, sub in S.NEW_E if op == 'block'); HEAVEN = tuple((e, sub) for e, op, sub in S.NEW_E if op == 'heaven')
KIN = tuple(S.KIN_UNMOVED); KINV = tuple(S.KIN_UNMOVED[k] for k in KIN)
c = S.counts()
VERSES = ['Deut 33:%d' % v for v in range(1, 30)]
assert S.MARKER is None and not BLOCKS and not RE
Q50 = f'''
def q50():
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
    i_last32 = max([i for i, l in enumerate(W.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 32:')] or [-1])
    after = bool(own) and all(idx[id(e)] > i_last32 for e in own)
    mk33 = [l for l in W.log if l[0] == 'MARKER' and str(l[2].get('verse', '')).startswith('Deut 33:')]; nm = len([l for l in W.log if l[0] == 'MARKER'])
    days = sorted({{ex.date(e[1]) for e in own}}); dated = sum(1 for e in own if e[2].get('dated') is not None)
    WN = {WN!r}
    HEAVEN = {HEAVEN!r}
    FV = lambda t_: '%s %d:%d' % t_ if isinstance(t_, tuple) else str(t_)
    wn = tuple((len(L(sub, eff)), FV(WE.first_verse(str(L(sub, eff)[0].get('case_source', '')))) if L(sub, eff) else None) for eff, _, sub in WN)
    blocks = sum(1 for eff, _, sub in WN for e in L(sub, eff) if e.get('op') == 'block')
    heaven = sum(1 for eff, sub in HEAVEN for e in L(sub, eff) if e.get('op') == 'heaven')
    KIN = {KIN!r}
    kin = tuple(nall(k) for k in KIN)
    rows = CR.DATA['the_readback']['value']
    rb = (len(rows), [r['verses'] for r in rows] == {VERSES!r}, [r['verses'] for r in rows if r.get('pointer')], [r['verses'] for r in rows if r.get('state')], any(r.get('open') for r in rows), any(r.get('stretch') for r in rows))
    dd = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon_dispositions.yaml'), encoding='utf-8'))
    d = dd['daemons'].get('{S.DAEMON}', {{}})
    got = ([e[2]['kind'] for e in own], after, len(mk33), nm, days, dated, wn, blocks, heaven, kin, rb, '{S.DAEMON}' in dd['daemons'], d.get('given_at'), d.get('installed_by'))
    return got == (list(OWN), True, 0, 173, [{S.DAY!r}], 0, tuple((1, v_) for _, v_, _ in WN), 0, {len(HEAVEN)}, {KINV!r}, ({len(VERSES)}, True, {S.POINTER_ROWS!r}, {S.STATE_ROWS!r}, False, False), True, '{S.GIVEN_AT}', '{S.INSTALLED_BY}'), 'got (the eleven own-day lines in the ink\\'s order, all after the tape\\'s last Deuteronomy 32 line, no marker at Deut 33, markers 173, their days (Moses\\' last day (40, 12, 7) alone), dated fields (none), the NEW writes on their subjects with their lines\\' first verses, no block, no heaven entry, the kin\\'s counts unmoved (as the callees read them), the readback (rows, one per verse in order, the two pointer rows 33:5 and 33:28, no state row, open, stretch), the daemon registered, given_at, installed_by) = %s' % (got,)
'''
rep("\nprint('READBACK PROBES (THE LOOP step 6, the first form)')", Q50 + "\nprint('READBACK PROBES (THE LOOP step 6, the first form)')")
rep("the readback\\'s fifty-two rows with the state row at 32:30 and no pointer row, the daemon — LEAN', q49)", "the readback\\'s fifty-two rows with the state row at 32:30 and no pointer row, the daemon — LEAN', q49), ('Q50 chapter 33\\'s eleven own-day lines in two forms on Moses\\' last day with no marker, their %d writes on Israel\\'s and the tribes\\' ledgers, no reuse, no block, no heaven entry, the kin unmoved, the readback\\'s twenty-nine rows with the two pointer rows 33:5 and 33:28 paid, the daemon — LEAN', q50)" % len(WN))
lines = s.split('\n'); k = [i for i, l in enumerate(lines) if l.startswith('  THE DEUTERONOMY WALK 20b (2026-09-28) (DEUTERONOMY_WALK.md "Sitting 20b" THE PROBES')]; assert len(k) == 1, k
lines.insert(k[0], '  %s (DEUTERONOMY_WALK.md "Sitting 21b" THE PROBES; THE LEAN PASS) — written to FAIL before cold_run_%s.py exists: Q50 the ELEVEN OWN-DAY lines %s after the tape\'s last Deuteronomy 32 line — ALL on MOSES\' LAST DAY (40, 12, 7), 19b\'s marker at Deut 31:1; NO MARKER in the chapter (the blessing spoken "before his death" — markers 173 UNMOVED), no dated field on the lines; their writes — the %d NEW ONE each on their subjects (%s; all STATUSES, no BLOCK, no HEAVEN entry) and NO reuse (no effect\'s own forward seat in the chapter); the kin\'s counts UNMOVED (the references — no second write; the retellings run citations); the readback\'s twenty-nine rows one per verse in order with THE TWO POINTER ROWS at 33:5 and 33:28 (20b\'s owed pointers PAID — the piskaot 346 and 356 read here in their own chapter) and NO state, open or stretch row; the daemon %s registered, given_at %s, installed_by %s (ONE probe — the lean form)' % (W, S.RUNNER, ', '.join('%s (%s)' % (l[0], l[2]) for l in S.LINES), len(WN), ', '.join('%d on %s' % (n, k_) for k_, n in c['subjects_new'].items()), S.DAEMON, S.GIVEN_AT, S.INSTALLED_BY))
s = '\n'.join(lines)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched: Q50 written (to FAIL until the runner and the tape carry chapter 33); the file compiles; the literals from the spec — %d new writes, %d reuses, %d blocks, %d heaven, %d kin counts, %d readback verses' % (len(WN), len(RE), len(BLOCKS), len(HEAVEN), len(KIN), len(VERSES)))
