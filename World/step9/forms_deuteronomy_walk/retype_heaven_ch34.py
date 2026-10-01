import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK 22b TAIL (2026-10-01): the chain's SECOND PASS fell at one count — chapter 32's "ten heaven entries" are ELEVEN
# since 34:4's reuse of see_the_land_from_afar_not_go_there (a heaven write on moses); the checkpoint DN2 (the tape: declared 10, computed 11)
# and the probe Q49 (the forty-two's last slot 1 -> 2 and the heaven count 10 -> 11, got against the typed tuple). EVERY NUMBER READ FROM
# ITS PRINT: ch34b_gates/tape.out line 1008 (computed) and ch34b_gates/probe_readback.out line 52 (got). RUN FROM THE REPO ROOT.
import subprocess, re, sys
ROOT = _ROOT
def rep(path, pairs):
    t = open(path, encoding='utf-8').read()
    for old, new in pairs:
        n = t.count(old)
        assert n == 1, (path, n, old[:90])
        t = t.replace(old, new)
    open(path, 'w', encoding='utf-8').write(t)
    print('%s: %d replacements' % (path.split('/')[-1], len(pairs)))
SEQ = ROOT + '/World/step9/cold_run_sequence.py'
rep(SEQ, [
    ("no block; the ten heaven entries; law_song_charge_nebo registered",
     "no block; the ELEVEN heaven entries (the song\\'s ten and see_the_land_from_afar_not_go_there\\'s second at 34:4 — THE DEUTERONOMY WALK 22b\\'s reuse, a heaven write on moses; retyped from the chain\\'s second-pass print, 2026-10-01); law_song_charge_nebo registered"),
    (", 0, 10, True, 'Deut 32:1', 'boot', 17), (tuple(zip(n42_cp, src_cp)), re_cp, blocks_cp, heaven_cp,",
     ", 0, 11, True, 'Deut 32:1', 'boot', 17), (tuple(zip(n42_cp, src_cp)), re_cp, blocks_cp, heaven_cp,"),
])
RB = ROOT + '/World/step9/readback_probes.py'
rep(RB, [
    ("tuple((1, v_) for _, v_, _ in W42), tuple(n_ for _, n_ in RE), 0, 10, (2, 6, 2,",
     "tuple((1, v_) for _, v_, _ in W42[:-1]) + ((2, 'Deut 32:51'),), tuple(n_ for _, n_ in RE), 0, 11, (2, 6, 2,"),
    ("no block, the ten heaven entries, the kin\\'s counts unmoved (as the callees read them)",
     "no block, the eleven heaven entries (the song\\'s ten and the land seen from afar\\'s second at 34:4 — 22b\\'s reuse), the kin\\'s counts unmoved (as the callees read them)"),
    ("    # THE DEUTERONOMY WALK 22b (2026-09-30; LEAN): Q49: gathered_to_his_people 5 -> 6",
     "    # THE DEUTERONOMY WALK 22b TAIL (2026-10-01): Q49: see_the_land_from_afar_not_go_there 1 -> 2 (the forty-two\\'s last — 34:4\\'s reuse) and the heaven entries 10 -> 11 (the reuse a heaven write on moses) — retyped from the chain\\'s second-pass print (FAIL Q49, the got against the typed tuple); the first retype caught the kin\\'s gathered alone\n    # THE DEUTERONOMY WALK 22b (2026-09-30; LEAN): Q49: gathered_to_his_people 5 -> 6"),
])
# the proof: the typed tuples now equal the prints' computed values
import ast
sp = sys.argv[1]
t = open(sp + '/ch34b_gates/tape.out').read().splitlines()
com = ast.literal_eval(t[1007].strip()[len('computed: '):])
assert com[3] == 11 and com[0][-1] == (2, ('Deut 32:51', 'moses')), com[3]
rb = open(sp + '/ch34b_gates/probe_readback.out').read().splitlines()
l = rb[51]; got = ast.literal_eval(l[l.index(') = (') + 4:])
assert got[9] == 11 and got[6][-1] == (2, 'Deut 32:51'), (got[9], got[6][-1])
print('THE PRINTS: DN2 computed heaven %d, its forty-two\'s last %r; Q49 got heaven %d, its forty-two\'s last %r' % (com[3], com[0][-1], got[9], got[6][-1]))
print('RETYPED: DN2 declared 10 -> 11 (the label ELEVEN); Q49 the forty-two\'s last (1 -> 2), heaven 10 -> 11, the why and the comment')
