# THE DEUTERONOMY WALK 10b (9b's form by derive_ch12_docket_tools.py) — the docket parts' shared helper: the dump's addresses in order (the source of truth for coverage — a part can never invent
# an address), a SPEC of (matcher, verdict, note) rows applied first-match, the part's slice asserted fully matched. R(prefix, lo, hi) matches
# 'prefix:n' for lo <= n <= hi; a bare string matches one address. The notes name the cell of cold_run_place_name.py (F1 the_header_and_the_demolition, F2 the_place_chosen, F3 the_burnt_offerings_only_there, F4 the_profane_slaughter_the_blood_and_the_gates,
# F5 the_border_enlarged_and_the_altar, F6 the_nations_cut_off_and_the_abomination — the design's six cells on the six claims' spans; the_readback the table) on LAW rows, or the callee's cell by CALL.
import os, re
SCR = os.path.dirname(os.path.abspath(__file__))
_dump = open(f'{SCR}/ch12_docket_dump.txt', encoding='utf-8').read()
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

from ch12_credited_rows import CREDITED_SPEC   # 10b: the credited rows carried with their ledgers (ch12_credit_carry.py — 9b's form); a part prepends it to its SPEC
