import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 21b (2026-09-29; LEAN) — RUN B: THE DEPENDENCY GATE'S DEMANDS FILED FROM ITS FIRST PRINT (ch33b_dependency_first.out): three token edges, every one
# FALSE BY HOMOGRAPH — lev24 [talion_formula] at 33:13 ('the deep that couches BENEATH' — the talion's 'under' (תחת — under, beneath) in its plain sense, 19b's precedent at 30:9),
# pesach [firstborn] at 33:17 ('his FIRSTLING bullock' — the firstborn's word (בכור — firstborn, firstling) for Joseph's majesty, the Sifrei 353:9-13's Joshua; no Passover, no firstborn law
# in the verse — the firstling law 15:19 release_firstborn's, CALLED for the poor law at 33:21), sanctions [molech_ov] at 33:5 ('a KING in Jeshurun' — Molech's consonants (מלך — king) the
# noun 'king', 19b's precedent: Molech FALSE by homograph at 29:16); NO pointer demanded (the gate's pointer forms find none in the blessing — 33:21's grave a readback row FORWARD, not a
# gate pointer); the thirty-nine CALL edges every one LIVE at the gate's first print (the facts call a cell of each by its literal name — no CALL-without-a-live-edge failure, 20b's
# twenty-four demands not repeated); and — with --registration, AFTER the stitcher writes the import — the registration edge sequence -> blessing_of_moses (20b's form).
# 20b's form (patch_deps_ch32.py). RUN FROM THE REPO ROOT.
import subprocess, yaml, sys
ROOT = _ROOT
F = f'{ROOT}/World/step9/dependency_dispositions.yaml'
t = open(F, encoding='utf-8').read()
d0 = yaml.safe_load(t); E0, P0 = len(d0['edges']), len(d0['pointers']); print('before: edges', E0, 'pointers', P0)
M = 'THE DEUTERONOMY WALK 21b (2026-09-29; LEAN)'
R = 'blessing_of_moses'
if '--registration' in sys.argv:
    assert E0 == 980 and P0 == 230, (E0, P0)   # after the first filing (three edges, no pointer)
    i = t.index('  - {from: sequence, to: song_charge_nebo, disposition: CALL, link: none,\n'); j = t.index('\n', t.index('\n', i) + 1) + 1
    assert t[j:].startswith('  - {from: food_tithe, to: shemini, disposition: CALL, link: reference, carries: verdict,'), t[j:j + 80]
    REG = (f'  - {{from: sequence, to: {R}, disposition: CALL, link: none,\n'
           f'     why: "{M} | THE REGISTRATION EDGE — the sequence file imports cold_run_blessing_of_moses (the live edge the gate reads; DAEMON_ORDER carries law_blessing_of_moses) so chapter 33\'s eleven own-day lines in two forms join the tape after the last Deuteronomy 32 line with NO MARKER (Moses\' last day, 19b\'s); 20b\'s form; filed after the stitcher wrote the import (the gate\'s first print ran before it)"}}\n')
    t = t[:j] + REG + t[j:]
    d1 = yaml.safe_load(t); assert len(d1['edges']) == E0 + 1 and len(d1['pointers']) == P0
    open(F, 'w', encoding='utf-8').write(t); print('WRITTEN: the registration edge sequence -> blessing_of_moses; edges', len(d1['edges'])); sys.exit(0)
assert E0 == 977 and P0 == 230, (E0, P0)   # THE TYPES' print (ch33b_types_b.out): 'edges 977, pointers 230'
# 1. THE TOKEN EDGES after the runner's last edge on file (pre_sinai's two lines)
i = t.index(f'  - {{from: {R}, to: pre_sinai, disposition: CALL, link: reference, carries: verdict,\n'); j = t.index('\n', t.index('\n', i) + 1) + 1
assert t[j:].startswith('  - {from: festivals_judges, to: priesthood, disposition: FALSE, link: none,') or t[j:].startswith('  - {from: song_charge_nebo, to: offerings, disposition: FALSE') or t[j:].startswith('  - {from: '), t[j:j + 80]
EDGES = (
 f'  - {{from: {R}, to: lev24, disposition: FALSE, link: none,\n'
 f'     why: "{M} | 33:13 \'and for the deep that couches BENEATH (תחת — under, beneath)\' — Genesis 49:25\'s phrase taken whole by Moses (joseph by CALL): the preposition in its plain sense, the deep under the earth; the talion\'s formula \'eye for (under) eye\' (Leviticus 24:20, the census\'s token) nowhere in the blessing — a HOMOGRAPH; 19b\'s precedent (30:9\'s \'under\' FALSE); no link"}}\n'
 f'  - {{from: {R}, to: pesach, disposition: FALSE, link: none,\n'
 f'     why: "{M} | 33:17 \'his FIRSTLING (בכור — firstborn, firstling) bullock, majesty is his\' — the firstborn\'s word for Joseph\'s majesty and Joshua\'s splendor (the Sifrei 353:9-13; Numbers 27:20 — zelophehad and opening_speech by CALL), a figure: no Passover and no firstborn law in the verse (Exodus 12\'s firstborn the census\'s token; the firstling law 15:19 release_firstborn\'s, CALLED for the poor law at 33:21) — a HOMOGRAPH by sense; no link"}}\n'
 f'  - {{from: {R}, to: sanctions, disposition: FALSE, link: none,\n'
 f'     why: "{M} | 33:5 \'and there was a KING (מלך — king) in Jeshurun\' — the noun \'king\' (Moses or the LORD — the Sifrei 346:1\'s two readings a DATA note; Onkelos Israel for Jeshurun), spelled with Molech\'s consonants (Leviticus 20\'s Molech, the census\'s token): a HOMOGRAPH; 19b\'s precedent (29:16\'s Molech FALSE); no link"}}\n')
t = t[:j] + EDGES + t[j:]
d1 = yaml.safe_load(t); E1, P1 = len(d1['edges']), len(d1['pointers']); print('after: edges', E1, 'pointers', P1)
assert E1 == E0 + 3 and P1 == P0, (E1, P1)
open(F, 'w', encoding='utf-8').write(t); print('WRITTEN; the departures: three token edges FALSE by homograph (the talion\'s under at 33:13, the Passover\'s firstborn at 33:17, Molech\'s letters in the king at 33:5); NO pointer demanded by the gate (the design\'s pointers readback rows — 33:21 FORWARD, 33:5 and 33:28 paid); every CALL edge live at the first print (no demand of the twenty-four\'s kind); the registration edge after the stitcher (--registration)')
