import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b (2026-09-27; LEAN) — RUN B: THE DEPENDENCY GATE'S DEMANDS FILED FROM ITS FIRST PRINT (ch29b_dependency_first.out): four token edges, every
# one FALSE BY HOMOGRAPH (pre_sinai [sabbath] at 30:1-2 — 'and you take to heart' and 'and you return' share the sabbath's consonants; priesthood [harlot] at 31:16 — 'and whore'
# the verb of apostasy, Leviticus 21:7's harlot a noun; lev24 [talion_formula] at 31:8 — 'nor be dismayed' the verb, the talion's 'in place of' a homograph; sanctions [molech_ov]
# at 29:6 — 'king' of Heshbon and of Bashan, Molech's consonants), the registration edge sequence -> covenant_return_charge (18b's form — filed before the chain, the gate's
# first print ran before the stitcher wrote the import), and the four AS_WHEN pointers (29:12, 31:3, 31:4 RUN_CITATION reference — the oath, the charge and the kings BEHIND
# on the tape; 30:9 FALSE — the comparative 'as He rejoiced', 28:63's precedent). The design predicted five pointers with 29:22 FALSE; the gate demands four — 29:22's 'like the
# overthrow' is a bare kaf, not the AS_WHEN form: A DEPARTURE for the AS BUILT. The three CALL edges without a live import (not_righteousness, beha, journeys) fixed IN THE
# RUNNER (the facts call a cell of each — the gate reads `alias.name(`), not here. 18b's form (patch_deps_ch26.py). RUN FROM THE REPO ROOT.
import subprocess, yaml
ROOT = _ROOT
F = f'{ROOT}/World/step9/dependency_dispositions.yaml'
t = open(F, encoding='utf-8').read()
d0 = yaml.safe_load(t); E0, P0 = len(d0['edges']), len(d0['pointers']); print('before: edges', E0, 'pointers', P0)
assert E0 == 888 and P0 == 225, (E0, P0)   # THE TYPES' print (ch29b_types_b.out): 'edges 888, pointers 225'
M = 'THE DEUTERONOMY WALK 19b (2026-09-27; LEAN)'
R = 'covenant_return_charge'
# 1. THE TOKEN EDGES after the runner's last edge on file (place_name's two lines)
i = t.index(f'  - {{from: {R}, to: place_name, disposition: CALL, link: reference, carries: verdict,\n'); j = t.index('\n', t.index('\n', i) + 1) + 1
assert t[j:].startswith('  - {from: festivals_judges, to: priesthood, disposition: FALSE, link: none,'), t[j:j + 80]
EDGES = (
 f'  - {{from: {R}, to: pre_sinai, disposition: FALSE, link: none,\n'
 f'     why: "{M} | 30:1 \'and you TAKE IT TO HEART (והשבת — and you take to heart)\' and 30:2 \'and you RETURN (ושבת — and you return) to the LORD your God\' — the return\'s root (shuv, seven times in the chapter) spelled with the sabbath\'s three consonants: the census\'s sabbath token a HOMOGRAPH — no rest, no seventh day in the three chapters; 17b\'s lesson 2 (the consonantal homograph named); no link"}}\n'
 f'  - {{from: {R}, to: priesthood, disposition: FALSE, link: none,\n'
 f'     why: "{M} | 31:16 \'this people will rise AND WHORE (וזנה — and whore) after the gods of the land\' — the verb of apostasy (Exodus 34:15-16\'s form; Numbers 25:1\'s at Shittim), not Leviticus 21:7\'s noun (the harlot the priest may not marry): the census\'s harlot token a HOMOGRAPH of the root; the runner\'s edge to erection carries the form; no link"}}\n'
 f'  - {{from: {R}, to: lev24, disposition: FALSE, link: none,\n'
 f'     why: "{M} | 31:8 \'fear not NOR BE DISMAYED (ולא תחת — nor be dismayed)\' — the verb of fear (the same at 31:6 in the plural, Joshua 1:9), not the talion formula\'s preposition \'in place of\' (Leviticus 24:20\'s eye for eye): the census\'s token a HOMOGRAPH; no link"}}\n'
 f'  - {{from: {R}, to: sanctions, disposition: FALSE, link: none,\n'
 f'     why: "{M} | 29:6 \'Sihon KING (מלך — king) of Heshbon and Og KING of Bashan\' — the kings of the retelling (2:26-3:11; Numbers 21:21-35 the tape\'s own lines), not Molech (Leviticus 18:21, 20:2-5 the sanctions\' seat): the census\'s molech token the consonants of \'king\' — a HOMOGRAPH; no link"}}\n')
t = t[:j] + EDGES + t[j:]
# 2. THE REGISTRATION EDGE after 18b's (sequence -> firstfruits_ebal_curses, two lines)
i = t.index('  - {from: sequence, to: firstfruits_ebal_curses, disposition: CALL, link: none,\n'); j = t.index('\n', t.index('\n', i) + 1) + 1
assert t[j:].startswith('  - {from: food_tithe, to: shemini, disposition: CALL, link: reference, carries: verdict,'), t[j:j + 80]
REG = (f'  - {{from: sequence, to: {R}, disposition: CALL, link: none,\n'
 f'     why: "{M} | THE REGISTRATION EDGE — the sequence file imports cold_run_covenant_return_charge (the live edge the gate reads; DAEMON_ORDER carries law_covenant_return_charge) so chapters 29-31\'s twenty own-day lines in three forms join the tape after the last Deuteronomy 28 line with ONE MARKER at 31:1 (Moses\' last day); 18b\'s form; filed from the gate\'s first print, which ran before the stitcher wrote the import"}}\n')
t = t[:j] + REG + t[j:]
# 3. THE POINTERS appended after the file's last pointer (18b's 28:63)
assert t.endswith('no link; NOT predicted by the design — filed from the gate\'s first print"}\n'), repr(t[-90:])
PTRS = (
 f'  - {{verse: "Deut 29:12", form: AS_WHEN, runner: {R}, disposition: RUN_CITATION, link: reference, why: "{M} | \'that He may establish you this day for a people to Himself and He will be your God, AS HE SPOKE TO YOU AND AS HE SWORE TO YOUR FATHERS, to Abraham, to Isaac and to Jacob\' — the oath lines by kind BEHIND on the tape (seven_nations.the_holy_people(the_oath) by CALL — the three lines; seducers\' 13:18 the pointer row\'s form; Genesis 22:16, 26:3 the patriarchs\' oaths; Exodus 19:5-6 the speaking); became_the_lords_people_this_day REUSED at the seat; predicted at the design; the runner\'s readback row 29:12 a reference row"}}\n'
 f'  - {{verse: "Deut 31:3", form: AS_WHEN, runner: {R}, disposition: RUN_CITATION, link: reference, why: "{M} | \'Joshua, he shall cross before you, AS THE LORD HAS SPOKEN\' — 3:28\'s \'charge Joshua … he shall cross before this people\' (moses_besought\'s answer; joshua_encouraged the tape\'s line at 3:21-22) and Numbers 27:18-23\'s commission (joshua_commission_commanded, joshua_commissioned the tape\'s kinds — opening_speech.the_commission by CALL) BEHIND on the tape; predicted at the design; the readback row 31:3 references both"}}\n'
 f'  - {{verse: "Deut 31:4", form: AS_WHEN, runner: {R}, disposition: RUN_CITATION, link: reference, why: "{M} | \'and the LORD will do to them AS HE DID TO SIHON AND TO OG, the kings of the Amorites\' — the tape\'s own lines sihon_smitten_land_possessed and og_came_out_and_fear_not (Numbers 21:21-35; kings_smitten on sihon and og; chukat.well_and_kings(joshua_refrain) by CALL — the refrain born at 21:35) BEHIND on the tape; 2:26-3:11\'s retelling (opening_speech.sihon_and_og); predicted at the design; the readback row 31:4 references the kings\' lines"}}\n'
 f'  - {{verse: "Deut 30:9", form: AS_WHEN, runner: {R}, disposition: FALSE, link: none, why: "{M} | \'for the LORD will again rejoice over you for good, AS HE REJOICED (כאשר שש — as He rejoiced) over your fathers\' — a comparison clause (the \'as … so\' of two rejoicings), an act not a text: כאשר (as) the comparative, no referent on the tape — 28:63\'s twin exactly (THE FALSE SIX a second time: the same word the number parser read as SIX, the Aramaic\'s \'rejoiced\' settles it; firstfruits_ebal_curses\' DATA the_false_six); 17b\'s 22:26 precedent; predicted FALSE at the design; no link"}}\n')
t = t + PTRS
d1 = yaml.safe_load(t); E1, P1 = len(d1['edges']), len(d1['pointers']); print('after: edges', E1, 'pointers', P1)
assert E1 == E0 + 5 and P1 == P0 + 4, (E1, P1)
open(F, 'w', encoding='utf-8').write(t); print('WRITTEN; the departures: 29:22 not demanded (a bare kaf, not the AS_WHEN form — predicted FALSE, no row); four token edges FALSE by homograph (the sabbath, the harlot, the talion\'s \'in place of\', Molech — all named); the three CALL edges without a live import fixed in the runner')
