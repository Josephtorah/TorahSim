import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (2026-09-28; LEAN) — RUN B: THE DEPENDENCY GATE'S DEMANDS FILED FROM ITS FIRST PRINT (ch32b_dependency_first.out): two token edges, both
# FALSE BY HOMOGRAPH (offerings [olah] at 32:49-50 — 'go up' (עלה — go up) the verb of the ascent, the burnt offering's consonants; yovel [holding] at 32:49 — 'for a possession'
# (לאחזה — for a possession) the word's plain sense, Leviticus 14:34's clause 'which I give you for a possession' and Genesis 17:8's everlasting possession, no jubilee institution
# in the verse), THE POINTER 32:50 AS_WHEN ('as Aaron your brother died') RUN_CITATION reference — the tape's own entries at Numbers 20:28 and 33:38 (predicted at the design),
# and — with --registration, AFTER the stitcher writes the import — the registration edge sequence -> song_charge_nebo (19b's form). The twenty-four CALL edges without a live
# call fixed IN THE RUNNER (the facts call a cell of each by its literal name — the gate reads `alias.name(`), not here. 19b's form (patch_deps_ch29.py). RUN FROM THE REPO ROOT.
import subprocess, yaml, sys
ROOT = _ROOT
F = f'{ROOT}/World/step9/dependency_dispositions.yaml'
t = open(F, encoding='utf-8').read()
d0 = yaml.safe_load(t); E0, P0 = len(d0['edges']), len(d0['pointers']); print('before: edges', E0, 'pointers', P0)
M = 'THE DEUTERONOMY WALK 20b (2026-09-28; LEAN)'
R = 'song_charge_nebo'
if '--registration' in sys.argv:
    assert E0 == 937 and P0 == 230, (E0, P0)   # after the first filing (two edges, one pointer)
    i = t.index('  - {from: sequence, to: covenant_return_charge, disposition: CALL, link: none,\n'); j = t.index('\n', t.index('\n', i) + 1) + 1
    assert t[j:].startswith('  - {from: food_tithe, to: shemini, disposition: CALL, link: reference, carries: verdict,'), t[j:j + 80]
    REG = (f'  - {{from: sequence, to: {R}, disposition: CALL, link: none,\n'
           f'     why: "{M} | THE REGISTRATION EDGE — the sequence file imports cold_run_song_charge_nebo (the live edge the gate reads; DAEMON_ORDER carries law_song_charge_nebo) so chapter 32\'s sixteen own-day lines in three forms join the tape after the last Deuteronomy 31 line with NO MARKER (Moses\' last day, 19b\'s); 19b\'s form; filed after the stitcher wrote the import (the gate\'s first print ran before it)"}}\n')
    t = t[:j] + REG + t[j:]
    d1 = yaml.safe_load(t); assert len(d1['edges']) == E0 + 1 and len(d1['pointers']) == P0
    open(F, 'w', encoding='utf-8').write(t); print('WRITTEN: the registration edge sequence -> song_charge_nebo; edges', len(d1['edges'])); sys.exit(0)
assert E0 == 935 and P0 == 229, (E0, P0)   # THE TYPES' print (ch32b_types_b.out): 'edges 935, pointers 229'
# 1. THE TOKEN EDGES after the runner's last edge on file (mekoshesh's two lines)
i = t.index(f'  - {{from: {R}, to: mekoshesh, disposition: CALL, link: reference, carries: verdict,\n'); j = t.index('\n', t.index('\n', i) + 1) + 1
assert t[j:].startswith('  - {from: festivals_judges, to: priesthood, disposition: FALSE, link: none,'), t[j:j + 80]
EDGES = (
 f'  - {{from: {R}, to: offerings, disposition: FALSE, link: none,\n'
 f'     why: "{M} | 32:49 \'GO UP (עלה — go up) into this mountain of Abarim\' and 32:50 \'the mount where you GO UP (עלה — go up)\' — the verb of the ascent (Numbers 27:12\'s summons retold — opening_speech by CALL), spelled with the burnt offering\'s consonants (olah — Leviticus 1\'s offering, the census\'s token): a HOMOGRAPH; no offering in the chapter (the libation of 32:38 the idols\' — the register empty); 17b\'s lesson 2 (the consonantal homograph named); no link"}}\n'
 f'  - {{from: {R}, to: yovel, disposition: FALSE, link: none,\n'
 f'     why: "{M} | 32:49 \'the land of Canaan which I give to the children of Israel FOR A POSSESSION (לאחזה — for a possession)\' — the word in its plain sense, a landholding given (Genesis 17:8\'s everlasting possession; Leviticus 14:34\'s clause \'which I give you for a possession\' the same words; Numbers 32\'s holding east — gad_reuben by CALL): no jubilee institution in the verse (Leviticus 25\'s release of the holding, the census\'s token) — the institution\'s term in its plain sense, a HOMOGRAPH by sense; no link"}}\n')
t = t[:j] + EDGES + t[j:]
# 2. THE POINTER appended after the file's last pointer (19b's 30:9)
assert t.endswith('the Aramaic\'s \'rejoiced\' settles it; firstfruits_ebal_curses\' DATA the_false_six); 17b\'s 22:26 precedent; predicted FALSE at the design; no link"}\n'), repr(t[-90:])
PTRS = (f'  - {{verse: "Deut 32:50", form: AS_WHEN, runner: {R}, disposition: RUN_CITATION, link: reference, why: "{M} | \'and die in the mount where you go up, and be gathered to your people, AS AARON YOUR BROTHER DIED IN MOUNT HOR and was gathered to his people\' — the tape\'s own entries BEHIND: garments_transferred_and_aaron_died at Numbers 20:28 ((40, 5, 1), aged 123 — chukat.edom_and_hor(death_dates, succession, aaron_age) by CALL) and its retelling at Numbers 33:38-40 (journeys.aarons_death_retold — no_write: a retelling never writes an act twice; second_tablets\' Moserah row OPEN); the manner commanded — by the kiss (chukat.meribah(death_by_the_kiss)); the Sifrei 339:3 AARON\'S DEATH THE RECEIPT; the readback row 32:50 a REFERENCE row on the tape\'s line; predicted RUN_CITATION at the design (DEUTERONOMY_WALK.md \'Sitting 20b\' THE KIN BY CALL)"}}\n')
t = t + PTRS
d1 = yaml.safe_load(t); E1, P1 = len(d1['edges']), len(d1['pointers']); print('after: edges', E1, 'pointers', P1)
assert E1 == E0 + 2 and P1 == P0 + 1, (E1, P1)
open(F, 'w', encoding='utf-8').write(t); print('WRITTEN; the departures: two token edges FALSE by homograph (the ascent\'s verb the burnt offering\'s consonants; the possession\'s word in its plain sense); the pointer 32:50 RUN_CITATION as predicted; the twenty-four CALL edges without a live call fixed in the runner (the facts call a cell of each by name); the registration edge after the stitcher (--registration)')
