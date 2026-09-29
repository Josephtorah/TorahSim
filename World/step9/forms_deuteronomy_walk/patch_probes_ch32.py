import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (2026-09-28): readback_probes.py Q49 written to FAIL before cold_run_song_charge_nebo.py exists (the design's THE PROBES paragraph — the
# FIRST step after the design: 7b's lesson 2; ONE probe in the lean form): the SIXTEEN OWN-DAY lines after the tape's last Deuteronomy 31 line — ALL on MOSES' LAST DAY
# (40, 12, 7), NO MARKER in the chapter (markers 173 UNMOVED); their writes — the forty-two NEW ONE each on their subjects (Israel, Moses, Joshua) with their lines' first
# verses and the three reuses' counts after on the world; no block; the ten heaven entries; the daemon registered; the readback's fifty-two rows one per verse in order with
# the state row at 32:30, no pointer, open or stretch row; the kin's counts unmoved. THE LITERALS GENERATED FROM THE SPEC MODULE (ch32b_spec.py), never typed twice.
# Idempotent. patch_probes_ch29.py's form. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad.
import subprocess, os, sys
ROOT = _ROOT
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ch32b_spec as S
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
assert 'def q49():' not in s, 'already patched'
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:90]); s = s.replace(old, new)
W = 'THE DEUTERONOMY WALK 20b (2026-09-28)'
OWN = tuple(S.KINDS)
W42 = [(e, l[1], sub) for l in S.LINES for e, _, sub in l[7]]
RE = [(e, S.REUSE_AFTER[e]) for e in S.REUSE_AFTER]
BLOCKS = tuple((e, sub) for e, op, sub in S.NEW_E if op == 'block'); HEAVEN = tuple((e, sub) for e, op, sub in S.NEW_E if op == 'heaven')
KIN = tuple(S.KIN_UNMOVED); KINV = tuple(S.KIN_UNMOVED[k] for k in KIN)
c = S.counts()
VERSES = ['Deut 32:%d' % v for v in range(1, 53)]
assert S.MARKER is None and not BLOCKS
Q49 = f'''
def q49():
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
    i_last31 = max([i for i, l in enumerate(W.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 31:')] or [-1])
    after = bool(own) and all(idx[id(e)] > i_last31 for e in own)
    mk32 = [l for l in W.log if l[0] == 'MARKER' and str(l[2].get('verse', '')).startswith('Deut 32:')]; nm = len([l for l in W.log if l[0] == 'MARKER'])
    days = sorted({{ex.date(e[1]) for e in own}}); dated = sum(1 for e in own if e[2].get('dated') is not None)
    W42 = {W42!r}
    RE = {RE!r}
    HEAVEN = {HEAVEN!r}
    FV = lambda t_: '%s %d:%d' % t_ if isinstance(t_, tuple) else str(t_)
    w42 = tuple((len(L(sub, eff)), FV(WE.first_verse(str(L(sub, eff)[0].get('case_source', '')))) if L(sub, eff) else None) for eff, _, sub in W42)
    re_ = tuple(nall(eff) for eff, _ in RE)
    blocks = sum(1 for eff, _, sub in W42 for e in L(sub, eff) if e.get('op') == 'block')
    heaven = sum(1 for eff, sub in HEAVEN for e in L(sub, eff) if e.get('op') == 'heaven')
    KIN = {KIN!r}
    kin = tuple(nall(k) for k in KIN)
    rows = CR.DATA['the_readback']['value']
    rb = (len(rows), [r['verses'] for r in rows] == {VERSES!r}, [r['verses'] for r in rows if r.get('pointer')], [r['verses'] for r in rows if r.get('state')], any(r.get('open') for r in rows), any(r.get('stretch') for r in rows))
    dd = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon_dispositions.yaml'), encoding='utf-8'))
    d = dd['daemons'].get('{S.DAEMON}', {{}})
    got = ([e[2]['kind'] for e in own], after, len(mk32), nm, days, dated, w42, re_, blocks, heaven, kin, rb, '{S.DAEMON}' in dd['daemons'], d.get('given_at'), d.get('installed_by'))
    return got == (list(OWN), True, 0, 173, [{S.DAY!r}], 0, tuple((1, v_) for _, v_, _ in W42), tuple(n_ for _, n_ in RE), 0, {len(HEAVEN)}, {KINV!r}, ({len(VERSES)}, True, {S.POINTER_ROWS!r}, {S.STATE_ROWS!r}, False, False), True, '{S.GIVEN_AT}', '{S.INSTALLED_BY}'), 'got (the sixteen own-day lines in the ink\\'s order, all after the tape\\'s last Deuteronomy 31 line, no marker at Deut 32, markers 173, their days (Moses\\' last day (40, 12, 7) alone), dated fields (none), the forty-two NEW writes on their subjects with their lines\\' first verses, the three reuses\\' counts after on the world (the witnesses 5, the hidden face 2, the length of days 2), no block, the ten heaven entries, the kin\\'s counts unmoved (as the callees read them), the readback (rows, one per verse in order, no pointer row, the state row 32:30, open, stretch), the daemon registered, given_at, installed_by) = %s' % (got,)
'''
rep("\nprint('READBACK PROBES (THE LOOP step 6, the first form)')", Q49 + "\nprint('READBACK PROBES (THE LOOP step 6, the first form)')")
rep("the readback\\'s seventy-eight rows with the state row and the pointer row, the daemon — LEAN', q48)", "the readback\\'s seventy-eight rows with the state row and the pointer row, the daemon — LEAN', q48), ('Q49 chapter 32\\'s sixteen own-day lines in three forms on Moses\\' last day with no marker, their forty-two writes on three ledgers and three reuses, no block and the ten heaven entries, the kin unmoved, the readback\\'s fifty-two rows with the state row at 32:30 and no pointer row, the daemon — LEAN', q49)")
lines = s.split('\n'); k = [i for i, l in enumerate(lines) if l.startswith('  THE DEUTERONOMY WALK 19b (2026-09-27) (DEUTERONOMY_WALK.md "Sitting 19b" THE PROBES')]; assert len(k) == 1, k
lines.insert(k[0], '  %s (DEUTERONOMY_WALK.md "Sitting 20b" THE PROBES; THE LEAN PASS) — written to FAIL before cold_run_%s.py exists: Q49 the SIXTEEN OWN-DAY lines %s after the tape\'s last Deuteronomy 31 line — ALL on MOSES\' LAST DAY (40, 12, 7), 19b\'s marker at Deut 31:1; NO MARKER in the chapter (32:48\'s "that selfsame day" that day — the Sifrei 337:1; markers 173 UNMOVED), no dated field on the lines; their writes — the FORTY-TWO NEW ONE each on their subjects (thirty-six on israel_people, five on moses, one on yehoshua; thirty-two STATUSES, no BLOCK, ten HEAVEN entries) and the THREE REUSES\' further entries (heaven_and_earth_witness at 32:1 — 4 -> 5, the chain\'s fifth seat; face_hidden_and_forsaken_foretold at 32:20 — 1 -> 2, the hidden face the third time; length_of_days_on_the_land_promised at 32:47 — 1 -> 2); the kin\'s counts UNMOVED (the references — no second write; the retellings run citations); the readback\'s fifty-two rows one per verse in order with THE STATE ROW at 32:30 (the joined thousand\'s condition — the Torah done or undone, two arms) and NO pointer, open or stretch row; the daemon %s registered, given_at %s, installed_by %s (ONE probe — the lean form)' % (W, S.RUNNER, ', '.join('%s (%s)' % (l[0], l[2]) for l in S.LINES), S.DAEMON, S.GIVEN_AT, S.INSTALLED_BY))
s = '\n'.join(lines)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched: Q49 written (to FAIL until the runner and the tape carry chapter 32); the file compiles; the literals from the spec — %d new writes, %d reuses, %d blocks, %d heaven, %d kin counts, %d readback verses' % (len(W42), len(RE), len(BLOCKS), len(HEAVEN), len(KIN), len(VERSES)))
