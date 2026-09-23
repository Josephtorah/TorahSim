# THE DEUTERONOMY WALK 13b (12b's form by derive_ch15_docket_tools.py) — the docket parts' shared helper: the dump's addresses in order (the source of truth for coverage — a part can never invent
# an address), a SPEC of (matcher, verdict, note) rows applied first-match, the part's slice asserted fully matched. R(prefix, lo, hi) matches
# 'prefix:n' for lo <= n <= hi; a bare string matches one address. The notes name the cell of cold_run_release_firstborn.py (F1 the_release, F2 the_needy_and_the_blessing, F3 the_hand_opened, F4 the_hebrew_slave,
# F5 the_awl_and_the_double_hire, F6 the_firstling, F7 the_blemish_and_the_blood — the design's seven cells on the seven claims' spans; the_readback the table) on LAW rows, or the callee's cell by CALL.
import os, re
SCR = os.path.dirname(os.path.abspath(__file__))
_dump = open(f'{SCR}/ch15_docket_dump.txt', encoding='utf-8').read()
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

from ch15_credited_rows import CREDITED_SPEC   # 13b: the credited rows carried with their ledgers (ch15_credit_carry.py — 12b's form); a part prepends it to its SPEC

# 13b — THE TWO DOCKET RUNS BY ADDRESS (the design: D1 every address outside the two long ranges; D2 Kiddushin 14b-22b and Bekhorot 25a-28b WITH THEIR OWN LINK ROWS) —
# the sets computed from the dump, never typed; a part builds over a SUBSET of D1 (build_set) and the writer checks every address of the dump is verdicted once.
import re as _re
def long_range(a):
    m = _re.match(r'(Kiddushin|Bekhorot) (\d+)([ab]):\d+$', a)
    if not m: return None
    w, f, s = m.group(1), int(m.group(2)), m.group(3)
    if w == 'Kiddushin' and ((f == 14 and s == 'b') or 15 <= f <= 22): return 'Kiddushin 14b-22b'
    if w == 'Bekhorot' and 25 <= f <= 28: return 'Bekhorot 25a-28b'
    return None
D1 = [a for a in ADDRS if long_range(a) is None]
D2 = [a for a in ADDRS if long_range(a) is not None]
assert len(D1) + len(D2) == len(ADDRS)
def build_set(spec, addrs):
    rows, unmatched = [], []
    for a in addrs:
        for key, verdict, note in spec:
            if (key == a) if isinstance(key, str) else key(a):
                rows.append((a, verdict, note)); break
        else:
            unmatched.append(a)
    assert not unmatched, ('UNMATCHED', unmatched[:20], len(unmatched))
    return rows

# 13b — the kind at an address's FIRST seat in the dump (a link row inside a chapter read whole is listed twice; the parts partition D1 by this map and by work)
_kinds = _re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  ', _dump, _re.M)
KIND_FIRST = {}
for _k, _a in _kinds: KIND_FIRST.setdefault(_a.strip(), _k)
D1_UNIQUE = list(dict.fromkeys(D1)); D2_UNIQUE = list(dict.fromkeys(D2))
