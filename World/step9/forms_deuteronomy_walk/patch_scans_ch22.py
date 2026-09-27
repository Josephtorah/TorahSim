import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 17b (2026-09-26; LEAN): THE SEATS WIDENED — the tape's first run 9/10 (the verdicts' checkpoint: CU7 and DC4 DIVERGE) and the scan census's B section:
# (1) CU7 THE STATE (chapter 8's garment-and-shoe scan, cold_run_good_land.STATE_WORDS over name and value on israel_people) — SEVEN of this sitting's names read at the tape's
# print (the computed list): cross_dressing_barred, house_of_unshod_named, levirate_marriage_commanded, shoe_loosening_rite_declared, tassels_commanded, widow_outsider_marriage_barred,
# widows_garment_pledge_barred — a later chapter's names and values naming the garment and the shoe; CH19_GARMENT extended (16b's form); (2) DC4 THE RAIN'S HOLE (chapter 11's
# 'rain' substring over the effect names) and the readback probe's rainy/vocab_rain (readback_probes.py, the chapter-11 probe) — vow_refraining_permitted: the census's homograph
# (refRAINing), excluded by name. Every seat READ FROM THE PRINTS (ch22_tape_run1.out, ch22_scan_census.out); idempotent. RUN FROM THE REPO ROOT.
import subprocess, re, py_compile
ROOT = _ROOT
W = 'THE DEUTERONOMY WALK 17b (2026-09-26; LEAN)'
def sub1(path, old, new):
    s = open(path, encoding='utf-8').read()
    if new in s: return 'already'
    assert s.count(old) == 1, (path, s.count(old), old[:80])
    open(path, 'w', encoding='utf-8').write(s.replace(old, new)); py_compile.compile(path, doraise=True); return 'patched'
SEVEN = ('cross_dressing_barred', 'house_of_unshod_named', 'levirate_marriage_commanded', 'shoe_loosening_rite_declared', 'tassels_commanded', 'widow_outsider_marriage_barred', 'widows_garment_pledge_barred')   # READ from the tape's first-run print (CU7 computed)
r1 = sub1(ROOT + '/World/step9/cold_run_good_land.py',
    "CH19_GARMENT = ('captive_mourning_month_commanded',)   # THE DEUTERONOMY WALK 16b (2026-09-25; LEAN): chapters 19-21's name whose value names the garment (21:13's 'the garment of her captivity')",
    "CH19_GARMENT = ('captive_mourning_month_commanded',) + %r   # THE DEUTERONOMY WALK 16b (2026-09-25; LEAN): chapters 19-21's name whose value names the garment (21:13's 'the garment of her captivity'); %s: chapters 22-25's SEVEN names and values naming the garment, the cloth and the shoe (22:5's garment, 22:12's covering, 22:17's garment spread, 24:17's widow's garment, 25:5-10's shoe drawn off) — read at the tape's first run (CU7's computed list), a later chapter's entries" % (SEVEN, W))
r2 = sub1(ROOT + '/World/step9/cold_run_sequence.py',
    "    rainy_bc = sorted({e['effect'] for e in LG('israel') if 'rain' in e['effect'] or 'heavens_shut' in e['effect'] or 'yoke_of' in e['effect']})\n",
    "    rainy_bc = sorted({e['effect'] for e in LG('israel') if ('rain' in e['effect'] or 'heavens_shut' in e['effect'] or 'yoke_of' in e['effect']) and e['effect'] != 'vow_refraining_permitted'})   # %s: 23:23's vow_refraining_permitted the census's homograph of 'rain' (refRAINing) — excluded by name, read at the tape's first run (DC4 computed) and the scan census's B section\n" % W)
r3 = sub1(ROOT + '/World/step9/readback_probes.py',
    "    isr = ENT('israel_people'); rainy = sorted({e['effect'] for e in isr.ledger if any(t in e['effect'] for t in ('rain', 'heavens_shut', 'yoke_of'))}) if isr else None   # 'yoke' bare read the homograph yoked_to_baal_peor (the fast checker's print) — narrowed; 'heaven' bare would read heaven-op names\n",
    "    isr = ENT('israel_people'); rainy = sorted({e['effect'] for e in isr.ledger if any(t in e['effect'] for t in ('rain', 'heavens_shut', 'yoke_of')) and e['effect'] != 'vow_refraining_permitted'}) if isr else None   # 'yoke' bare read the homograph yoked_to_baal_peor (the fast checker's print) — narrowed; 'heaven' bare would read heaven-op names; %s: 'rain' reads 23:23's vow_refraining_permitted (refRAINing) — the census's homograph, excluded by name\n" % W)
r4 = sub1(ROOT + '/World/step9/readback_probes.py',
    "    vocab_rain = sorted(k for k in fx if 'rain' in k)\n",
    "    vocab_rain = sorted(k for k in fx if 'rain' in k and k != 'vow_refraining_permitted')   # %s: the registry's fourth 'rain' the homograph (23:23's refraining) — excluded by name\n" % W)
r5 = sub1(ROOT + '/World/step9/cold_run_blessing_and_curse.py', "RAIN_VOCAB = sorted(k for k in _FXV if 'rain' in k)", "RAIN_VOCAB = sorted(k for k in _FXV if 'rain' in k and k != 'vow_refraining_permitted')   # THE DEUTERONOMY WALK 17b (2026-09-26; LEAN): the registry's fourth 'rain' is 23:23's vow_refraining_permitted (refRAINing) — the scan census's homograph, excluded by name (the tape's second run read DC4's computed list)")   # the registry's 'rain' names at their source — DC4's declared list reads RAIN_VOCAB (the tape's second run 9/10, DC4 the one miss: the vocabulary's fourth 'rain')
print('RAIN_VOCAB', r5)
print('THE SEATS WIDENED: CU7 %s (seven names), DC4 %s, the chapter-11 probe rainy %s / vocab_rain %s' % (r1, r2, r3, r4))
