import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b (2026-09-27): readback_probes.py Q48 written to FAIL before cold_run_covenant_return_charge.py exists (the design's THE PROBES paragraph — the
# FIRST step after the design: 7b's lesson 2; ONE probe in the lean form): the TWENTY OWN-DAY lines after the tape's last Deuteronomy 28 line — nine on the counter's day
# (40, 11, 1), eleven on MOSES' LAST DAY (40, 12, 7) after THE ONE MARKER at Deut 31:1 (markers 172 -> 173); their writes — the fifty-nine NEW ONE each on their subjects
# (Israel, Joshua, Moses, the Levites) with their lines' first verses and the nine reuses' counts after on the world; the two blocks; the twenty-six heaven entries; the
# daemon registered; the readback's seventy-eight rows one per verse in order with the state row at 30:15 and 30:17 and the pointer row at 31:10, no open, no stretch row;
# the kin's counts of DM4 unmoved. THE LITERALS GENERATED FROM THE SPEC MODULE (ch29b_spec.py), never typed twice. Idempotent. patch_probes_ch26.py's form. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad.
import subprocess, os, sys
ROOT = _ROOT
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ch29b_spec as S
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
assert 'def q48():' not in s, 'already patched'
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:90]); s = s.replace(old, new)
W = 'THE DEUTERONOMY WALK 19b (2026-09-27)'
OWN = tuple(S.KINDS)
W59 = [(e, l[1], sub) for l in S.LINES for e, _, sub in l[7]]
RE = [(e, S.REUSE_AFTER[e]) for e in S.REUSE_AFTER]
BLOCKS = tuple((e, sub) for e, op, sub in S.NEW_E if op == 'block'); HEAVEN = tuple((e, sub) for e, op, sub in S.NEW_E if op == 'heaven')
KIN = tuple(S.KIN_UNMOVED); KINV = tuple(S.KIN_UNMOVED[k] for k in KIN)
c = S.counts()
VERSES = ['Deut 29:%d' % v for v in range(1, 29)] + ['Deut 30:%d' % v for v in range(1, 21)] + ['Deut 31:%d' % v for v in range(1, 31)]
Q48 = f'''
def q48():
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
    i_last28 = max([i for i, l in enumerate(W.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 28:')] or [-1])
    after = bool(own) and all(idx[id(e)] > i_last28 for e in own)
    mk31 = [l for l in W.log if l[0] == 'MARKER' and str(l[2].get('verse', '')).startswith('Deut 31:')]; nm = len([l for l in W.log if l[0] == 'MARKER'])
    days = sorted({{ex.date(e[1]) for e in own}}); dated = sum(1 for e in own if e[2].get('dated') is not None)
    W59 = {W59!r}
    RE = {RE!r}
    BLOCKS = {BLOCKS!r}
    HEAVEN = {HEAVEN!r}
    FV = lambda t_: '%s %d:%d' % t_ if isinstance(t_, tuple) else str(t_)
    w59 = tuple((len(L(sub, eff)), FV(WE.first_verse(str(L(sub, eff)[0].get('case_source', '')))) if L(sub, eff) else None) for eff, _, sub in W59)
    re_ = tuple(nall(eff) for eff, _ in RE)
    blocks = sum(1 for eff, sub in BLOCKS for e in L(sub, eff) if e.get('op') == 'block')
    heaven = sum(1 for eff, sub in HEAVEN for e in L(sub, eff) if e.get('op') == 'heaven')
    KIN = {KIN!r}
    kin = tuple(nall(k) for k in KIN)
    rows = CR.DATA['the_readback']['value']
    rb = (len(rows), [r['verses'] for r in rows] == {VERSES!r}, [r['verses'] for r in rows if r.get('pointer')], [r['verses'] for r in rows if r.get('state')], any(r.get('open') for r in rows), any(r.get('stretch') for r in rows))
    dd = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon_dispositions.yaml'), encoding='utf-8'))
    d = dd['daemons'].get('{S.DAEMON}', {{}})
    got = ([e[2]['kind'] for e in own], after, len(mk31), nm, days, dated, w59, re_, blocks, heaven, kin, rb, '{S.DAEMON}' in dd['daemons'], d.get('given_at'), d.get('installed_by'))
    return got == (list(OWN), True, 1, 173, [{S.DAY_BEFORE!r}, {S.DAY_AFTER!r}], 0, tuple((1, v_) for _, v_, _ in W59), tuple(n_ for _, n_ in RE), {len(BLOCKS)}, {len(HEAVEN)}, {KINV!r}, ({len(VERSES)}, True, ['Deut 31:10'], ['Deut 30:15', 'Deut 30:17'], False, False), True, '{S.GIVEN_AT}', '{S.INSTALLED_BY}'), 'got (the twenty own-day lines in the ink\\'s order, all after the tape\\'s last Deuteronomy 28 line, the marker at Deut 31 (one), markers 173, their days (the counter\\'s (40, 11, 1) for chapters 29-30 and Moses\\' last day (40, 12, 7) for chapter 31), dated fields (none), the fifty-nine NEW writes on their subjects with their lines\\' first verses, the nine reuses\\' counts after on the world (the covenant entered 4, the LORD\\'s people 2, the witnesses 4, the pair set 2, the cleaving 3, fear not 6, the glory 7), the two blocks, the twenty-six heaven entries, the kin\\'s counts unmoved (as the recon and the callees read them), the readback (rows, one per verse in order, the pointer row 31:10, the state rows 30:15 and 30:17, open, stretch), the daemon registered, given_at, installed_by) = %s' % (got,)
'''
rep("\nprint('READBACK PROBES (THE LOOP step 6, the first form)')", Q48 + "\nprint('READBACK PROBES (THE LOOP step 6, the first form)')")
rep("the readback\\'s one hundred and fourteen rows with the state row and the two pointer rows, the daemon — LEAN', q47)", "the readback\\'s one hundred and fourteen rows with the state row and the two pointer rows, the daemon — LEAN', q47), ('Q48 chapters 29-31\\'s twenty own-day lines in three forms and the one marker (Moses\\' last day), their fifty-nine writes on four ledgers and nine reuses, the two blocks and the twenty-six heaven entries, the kin unmoved, the readback\\'s seventy-eight rows with the state row and the pointer row, the daemon — LEAN', q48)")
lines = s.split('\n'); k = [i for i, l in enumerate(lines) if l.startswith('  THE DEUTERONOMY WALK 18b (2026-09-26) (DEUTERONOMY_WALK.md "Sitting 18b" THE PROBES')]; assert len(k) == 1, k
lines.insert(k[0], '  %s (DEUTERONOMY_WALK.md "Sitting 19b" THE PROBES; THE LEAN PASS) — written to FAIL before cold_run_%s.py exists: Q48 the TWENTY OWN-DAY lines %s after the tape\'s last Deuteronomy 28 line — nine on the counter\'s day (40, 11, 1) and eleven on MOSES\' LAST DAY (40, 12, 7) after THE ONE MARKER at Deut 31:1 (31:2\'s "a hundred and twenty years old this day" with Exodus 7:7\'s eighty; the 7th of Adar the answer sheet\'s — Tosefta Sotah 11:3; markers 172 -> 173), no dated field on the lines; their writes — the FIFTY-NINE NEW ONE each on their subjects (fifty-three on israel_people, three on yehoshua, two on moses, one on the_levites; thirty-one STATUSES, two BLOCKS, twenty-six HEAVEN entries) and the NINE REUSES\' further entries (entered_the_covenant at 29:11 — 3 -> 4; became_the_lords_people_this_day at 29:12 — 1 -> 2; heaven_and_earth_witness at 30:19 and 31:28 — 2 -> 4; blessing_and_curse_set at 30:19 — 1 -> 2; cleaving_commanded at 30:20 — 2 -> 3; fear_not_promised at 31:6 on Israel and 31:8 on Joshua — 4 -> 6; glory_appeared at 31:15 on the tent of meeting — 6 -> 7); the kin\'s counts UNMOVED (the references — no second write); the readback\'s seventy-eight rows one per verse in order with THE STATE ROW at 30:15 and 30:17 (life and death — the two arms) and THE ONE POINTER ROW at 31:10 (15b\'s owed pointer for the hakhel PAID — the copy of the law\'s seat forward), no open or stretch row; the daemon %s registered, given_at %s, installed_by %s (ONE probe — the lean form)' % (W, S.RUNNER, ', '.join('%s (%s)' % (l[0], l[2]) for l in S.LINES), S.DAEMON, S.GIVEN_AT, S.INSTALLED_BY))
s = '\n'.join(lines)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched: Q48 written (to FAIL until the runner and the tape carry chapters 29-31); the file compiles; the literals from the spec — %d new writes, %d reuses, %d blocks, %d heaven, %d kin counts, %d readback verses' % (len(W59), len(RE), len(BLOCKS), len(HEAVEN), len(KIN), len(VERSES)))
