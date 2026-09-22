#!/usr/bin/env python3
# THE DEUTERONOMY WALK 12b — THE DOCKET, TWO RUNS (2026-09-21): the docket's five instruments DERIVED from 11b's forms by asserted substitutions (11b derived them
# from 10b's the same way): ch14_docket_common.py, ch14_docket_rows.py, ch14_docket_uncred.py, ch14_credit_survey.py, ch14_credit_carry.py. Departures from 11b's
# forms, each asserted: the cells' names (cold_run_food_tithe.py's seven, the design's F1-F7); the chunk cap 64,000 kept; THE RUN BOUNDARY COMPUTED from the dump
# (SPLIT_AT = the first Chullin topic row past folio 66 — D1 the link rows, the Mishnah rows and Chullin 59a-66b; D2 the rest), asserted contiguous; the unresolved
# rows' print led by the dump index so the two runs split them. Run from the repo root.
import subprocess, os, re
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__)); FORMS = f'{ROOT}/World/step9/forms_deuteronomy_walk'
def load(name):
    for d in (FORMS, SP):
        p = f'{d}/{name}'
        if os.path.exists(p): return open(p, encoding='utf-8').read()
    raise FileNotFoundError(name)
def sub(text, old, new, n=1):
    assert text.count(old) == n, (old[:60], text.count(old), n); return text.replace(old, new)
CELLS_OLD = "cold_run_seducers.py (F1 the_header, F2 the_prophet_and_the_test, F3 the_inciter, F4 the_city_heard_of_the_inquiry_and_the_sword,\n# F5 the_whole_offering_the_heap_and_the_mercy, F6 the_footer — the design's six cells on the six claims' spans; the_readback the table)"
CELLS_NEW = "cold_run_food_tithe.py (F1 the_sons_and_the_cuttings, F2 the_beasts, F3 the_water_and_the_birds, F4 the_carcass_and_the_kid,\n# F5 the_second_tithe, F6 the_far_place_the_money_the_rejoicing_and_the_levite, F7 the_third_year — the design's seven cells on the seven claims' spans; the_readback the table)"
# 1 common
t = load('ch13_docket_common.py')
t = sub(t, "# THE DEUTERONOMY WALK 11b (10b's form by derive_ch13_docket_tools.py)", "# THE DEUTERONOMY WALK 12b (11b's form by derive_ch14_docket_tools.py)")
t = sub(t, CELLS_OLD, CELLS_NEW)
t = sub(t, "# 11b: the credited rows carried with their ledgers (ch13_credit_carry.py — 10b's form)", "# 12b: the credited rows carried with their ledgers (ch14_credit_carry.py — 11b's form)")
t = t.replace('ch13', 'ch14'); assert 'ch13' not in t and '11b' not in t.replace("11b's form", ''), [l for l in t.split('\n') if 'ch13' in l or '11b' in l]
open(f'{SP}/ch14_docket_common.py', 'w', encoding='utf-8').write(t)
# 2 rows
t = load('ch13_docket_rows.py'); t = t.replace('ch13', 'ch14'); assert t.count('ch14') == 1; open(f'{SP}/ch14_docket_rows.py', 'w', encoding='utf-8').write(t)
# 3 uncred (the cap kept; the boundary computed)
t = load('ch13_docket_uncred.py')
t = sub(t, "# 11b docket (10b's form) — the UNCREDITED rows of the dump printed WHOLE (THE WHOLE-ROW RULE) into chunk files of at most 64,000 bytes each (one chunk one Read —\n# the cost rules' rule C; 10b's cap was 76,000 and its chunks took two pages), in dump order; the chunk",
           "# 12b docket (11b's form) — the UNCREDITED rows of the dump printed WHOLE (THE WHOLE-ROW RULE) into chunk files of at most 64,000 bytes each (one chunk one Read —\n# the cost rules' rule C; 11b's cap, one page each), in dump order; a chunk never spans the two docket runs (SPLIT_AT computed from the dump: D1 the link rows, the\n# Mishnah rows and Chullin 59a-66b; D2 from the first Chullin topic row past folio 66); the chunk")
t = sub(t, "CAP = 64000\nSPLIT_AT = set()   # ONE docket run this chapter (566 addresses, 196 credited — under the ~700 clause): no run boundary",
           "CAP = 64000\n"
           "def _folio(a):\n"
           "    m = re.match(r'Chullin (\\d+)[ab]:\\d+$', a); return int(m.group(1)) if m else None\n"
           "_addrs = [(m.group(1), m.group(2).strip()) for m in (re.match(r'\\[(LINK|TOPIC)\\] (.+?)  ', b.partition('\\n')[0]) for b in blocks)]\n"
           "_c0 = _addrs.index(('TOPIC', 'Chullin 59a:1'))   # the first Chullin topic row (the design's first range)\n"
           "_d2 = [i for i, (k, a) in enumerate(_addrs) if k == 'TOPIC' and _folio(a) is not None and _folio(a) > 66]\n"
           "SPLIT_AT = {_d2[0]}   # TWO docket runs this chapter (the ~700 clause): D1 = the link rows, the Mishnah rows and Chullin 59a-66b; D2 = the rest — the boundary COMPUTED, never typed\n"
           "assert all(k == 'TOPIC' and 59 <= _folio(a) <= 66 for k, a in _addrs[_c0:_d2[0]]), 'D1 ends with Chullin 59a-66b whole'\n"
           "assert all(_folio(a) is None or k == 'LINK' for k, a in _addrs[:_c0]), 'no Chullin topic row before 59a:1'")
t = sub(t, "print('uncredited rows', nu, 'chunks', len(chunks))", "print('uncredited rows', nu, 'chunks', len(chunks), 'SPLIT_AT', sorted(SPLIT_AT), 'D1 rows', _d2[0], 'D2 rows', len(_addrs) - _d2[0])")
t = t.replace('ch13', 'ch14'); assert 'ch13' not in t; open(f'{SP}/ch14_docket_uncred.py', 'w', encoding='utf-8').write(t)
# 4 survey
t = load('ch13_credit_survey.py'); t = sub(t, "# 11b docket (10b's form) — the credited addresses by ledger", "# 12b docket (11b's form) — the credited addresses by ledger")
t = t.replace('ch13', 'ch14'); assert 'ch13' not in t; open(f'{SP}/ch14_credit_survey.py', 'w', encoding='utf-8').write(t)
# 5 carry (the unresolved lines led by the dump index)
t = load('ch13_credit_carry.py')
t = sub(t, "# 11b docket (10b's form) — THE CREDITED ROWS CARRIED WITH THEIR LEDGERS (THE WHOLE-ROW RULE", "# 12b docket (11b's form) — THE CREDITED ROWS CARRIED WITH THEIR LEDGERS (THE WHOLE-ROW RULE")
t = sub(t, "# ch13_credited_rows.py (CREDITED_SPEC in dump order) and ch13_uncred_unres.txt (the unresolved rows whole); prints the counts.",
           "# ch14_credited_rows.py (CREDITED_SPEC in dump order) and ch14_uncred_unres.txt (the unresolved rows whole, each line led by its dump index — the two docket runs split them); prints the counts.")
t = sub(t, "out = ['# 11b docket — THE CREDITED ROWS CARRIED WITH THEIR LEDGERS, generated by ch13_credit_carry.py (10b\\'s form; never typed)",
           "out = ['# 12b docket — THE CREDITED ROWS CARRIED WITH THEIR LEDGERS, generated by ch14_credit_carry.py (11b\\'s form; never typed)")
t = sub(t, "CRED, ORDER, TEXT = {}, [], {}\nfor blk in blocks:", "CRED, ORDER, TEXT, IDX = {}, [], {}, {}\nfor bi, blk in enumerate(blocks):")
t = sub(t, "ORDER.append((kind, addr)); TEXT[addr] = ' '.join(body.split())", "ORDER.append((kind, addr)); TEXT[addr] = ' '.join(body.split()); IDX[addr] = bi")
t = sub(t, "lines = ['%s %s %s | %s' % ('U', kind[0], addr, TEXT[addr]) for kind, addr in unresolved]", "lines = ['%d U %s %s | %s' % (IDX[addr], kind[0], addr, TEXT[addr]) for kind, addr in unresolved]")
t = t.replace('ch13', 'ch14'); assert 'ch13' not in t and '10b' not in t; open(f'{SP}/ch14_credit_carry.py', 'w', encoding='utf-8').write(t)
for f in ('ch14_docket_common.py', 'ch14_docket_rows.py', 'ch14_docket_uncred.py', 'ch14_credit_survey.py', 'ch14_credit_carry.py'):
    print('written', f, os.path.getsize(f'{SP}/{f}'), 'bytes')
