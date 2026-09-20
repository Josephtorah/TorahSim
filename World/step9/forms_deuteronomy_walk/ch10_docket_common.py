# THE DEUTERONOMY WALK 8b — the docket parts' shared helper: the dump's addresses in order (the source of truth for coverage — a part can never invent
# an address), a SPEC of (matcher, verdict, note) rows applied first-match, the part's slice asserted fully matched. R(prefix, lo, hi) matches
# 'prefix:n' for lo <= n <= hi; a bare string matches one address. The notes name the cell of cold_run_second_tablets.py (F1 the_second_tablets_and_the_ark, F2 the_stations_and_aarons_death, F3 the_levites_separated, F4 the_third_forty_and_the_go, F5 what_the_lord_asks,
# F6 the_god_of_gods_and_the_stranger) on LAW rows, or the callee's cell by CALL.
import os, re
SCR = os.path.dirname(os.path.abspath(__file__))
_dump = open(f'{SCR}/ch10_docket_dump.txt', encoding='utf-8').read()
ADDRS = [a.strip() for _, a, _ in re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  (.*)$', _dump, re.M)]
_N = int(re.match(r'ROWS (\d+) ', _dump).group(1)); assert len(ADDRS) == _N, (len(ADDRS), _N)  # the dump header's count, never typed
def R(prefix, lo, hi):
    def m(a):
        if not a.startswith(prefix + ':'): return False
        n = a.rsplit(':', 1)[1]
        return n.isdigit() and lo <= int(n) <= hi
    return m
def build(spec, lo, hi):
    rows, unmatched = [], []
    for a in ADDRS[lo:hi]:
        for key, verdict, note in spec:
            if (key == a) if isinstance(key, str) else key(a):
                rows.append((a, verdict, note)); break
        else:
            unmatched.append(a)
    assert not unmatched, ('UNMATCHED', unmatched[:20], len(unmatched))
    return rows
def apply_whole(rows, whole):
    # THE WHOLE-ROW RULE (owner-ruled 2026-09-17, "never ever cut corners with the Talmud"): every row of the part reread WHOLE; WHOLE = {address:
    # (verdict, note)} overrides the cut's verdict — the cut's row stays in SPEC above as the record of what 170 characters missed; a corrected note ends
    # "[whole: …]". The counts (verdicts changed, notes changed) are computed, never typed.
    idx = {a: i for i, (a, _, _) in enumerate(rows)}
    missing = [a for a in whole if a not in idx]; assert not missing, ('WHOLE names an address outside the part', missing)
    out = list(rows); cv = cn = 0
    for a, (v, n) in whole.items():
        assert v in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE'), (a, v)
        i = idx[a]; ov, on = rows[i][1], rows[i][2]
        assert (v, n) != (ov, on), ('WHOLE repeats the cut', a)
        assert '[whole:' in n, ('a WHOLE note names what the cut missed', a)
        cv += (v != ov); cn += (n != on); out[i] = (a, v, n)
    return out, {'rows': len(rows), 'corrected': len(whole), 'verdicts_changed': cv, 'notes_changed': cn}
