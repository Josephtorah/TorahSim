import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 16b (LEAN): FOUR SCAN SEATS WIDENED FROM THE SCAN CENSUS'S PRINT (ch19_scan_census3.out — run after the tape's first run, 14b's lesson 2; the census
# extended to the tape's NAMED-PATTERN form re.search(cold_run_X.NAME_WORDS, …), the third form it had not covered — the tape's first run 9/10 read CU7 and DA6 DIVERGE):
# (1) good_land's GARMENT_SCAN (STATE_WORDS on israel_people, asserted empty at import) found this sitting's captive_mourning_month_commanded — its value names 'the garment
# of her captivity'; (2) not_righteousness's STIFF_SCAN (STIFF_WORDS) found heifer_neck_broken_commanded (the name) and elders_hands_washed_commanded (its value — the
# heifer whose neck was broken); (3) the tape's CU7 and (4) DA6 read the same two patterns on the running world. Each seat widened with the sitting's note; nothing else
# moves. patch_scans_ch17.py's and patch_tape_de4_ch17.py's forms. RUN FROM THE REPO ROOT.
import subprocess, py_compile
ROOT = _ROOT
W = 'THE DEUTERONOMY WALK 16b (2026-09-25; LEAN)'
def patch(path, pairs):
    s = open(path, encoding='utf-8').read()
    for old, new in pairs:
        if new in s: continue   # already on file (the first run's own writes before it fell)
        assert s.count(old) == 1, (path, s.count(old), old[:80]); s = s.replace(old, new)
    open(path, 'w', encoding='utf-8').write(s); py_compile.compile(path, doraise=True)
patch(ROOT + '/World/step9/cold_run_good_land.py', [("GARMENT_SCAN = ledger_scan('israel_people', STATE_WORDS)",
    "CH19_GARMENT = ('captive_mourning_month_commanded',)   # %s: chapters 19-21's name whose value names the garment (21:13's 'the garment of her captivity')\n_gs = ledger_scan('israel_people', STATE_WORDS); GARMENT_SCAN = None if _gs is None else [e for e in _gs if e not in CH19_GARMENT]   # %s: the captive's month excluded — a later chapter's write moved this scan's ground once the tape's first run put it in the one database (the scan census's print; the tape's CU7 read this pattern and diverged 9/10 — 14b's and 15b's lesson)" % (W, W))])
patch(ROOT + '/World/step9/cold_run_not_righteousness.py', [("STIFF_SCAN = None if _stiff is None else [e for e in _stiff if e != 'stiffening_barred']",
    "CH19_NECK = ('heifer_neck_broken_commanded', 'elders_hands_washed_commanded')   # %s: chapters 19-21's names carrying the neck (21:4's heifer's neck broken; 21:6's hands washed over the heifer whose neck was broken)\nSTIFF_SCAN = None if _stiff is None else [e for e in _stiff if e != 'stiffening_barred' and e not in CH19_NECK]" % W)])
patch(ROOT + '/World/step9/cold_run_sequence.py', [
    ("st_gl = sorted({e['effect'] for e in LG('israel') if re.search(cold_run_good_land.STATE_WORDS, '%s %s' % (e['effect'], e.get('value', '')), re.I)})",
     "st_gl = sorted({e['effect'] for e in LG('israel') if e['effect'] not in cold_run_good_land.CH19_GARMENT and re.search(cold_run_good_land.STATE_WORDS, '%s %s' % (e['effect'], e.get('value', '')), re.I)})   # WWW: the captive's month excluded — its value names the garment (the scan census's named-pattern section, added at 16b; the tape's first run read this seat 9/10)".replace('WWW', W)),
    ("cp('CU7 THE STATE — no effect naming a garment, clothing, a shoe or a swelling on israel_people (the SUPPLIED grade\\'s assertion, run on the running world with the runner\\'s own word list); the readback\\'s SUPPLIED row 8:4'",
     "cp('CU7 THE STATE — no effect naming a garment, clothing, a shoe or a swelling on israel_people (the SUPPLIED grade\\'s assertion, run on the running world with the runner\\'s own word list; THE DEUTERONOMY WALK 16b: 21:13\\'s captive_mourning_month_commanded excluded — a later chapter\\'s value naming the garment); the readback\\'s SUPPLIED row 8:4'"),
    ("st_nr = sorted({e['effect'] for e in LG('israel') if e['effect'] != 'stiffening_barred' and re.search(cold_run_not_righteousness.STIFF_WORDS, '%s %s' % (e['effect'], e.get('value', '')), re.I)})",
     "st_nr = sorted({e['effect'] for e in LG('israel') if e['effect'] != 'stiffening_barred' and e['effect'] not in cold_run_not_righteousness.CH19_NECK and re.search(cold_run_not_righteousness.STIFF_WORDS, '%s %s' % (e['effect'], e.get('value', '')), re.I)})   # WWW: the heifer's neck and the hands washed over it excluded — a later chapter's names (the scan census's named-pattern section; the tape's first run read this seat 9/10)".replace('WWW', W)),
    ("cp('DA6 THE STIFF NECK — no effect naming stiff / neck / nape on israel_people (the state in the first telling, Exodus 32:9 — no entry, no write; the runner\\'s own word list, run on the running world); the DATA row\\'s six seats all the calf\\'s'",
     "cp('DA6 THE STIFF NECK — no effect naming stiff / neck / nape on israel_people (the state in the first telling, Exodus 32:9 — no entry, no write; the runner\\'s own word list, run on the running world; THE DEUTERONOMY WALK 16b: the heifer\\'s neck and the hands washed over it excluded — a later chapter\\'s names); the DATA row\\'s six seats all the calf\\'s'")])
# (5) second_tablets' LAW_SCAN (LAW_WORDS — cleaving, stiff, neck, nape, bribe, the heart's circumcision, the fear of Heaven — on israel_people, asserted empty at import) found the same two neck names:
# READ AT THE TAPE'S SECOND RUN (its import fell — the census's anchored regex had read the first of three patterns sharing one line; the census widened, the seat here)
patch(ROOT + '/World/step9/cold_run_second_tablets.py', [("LAW_SCAN = None if _law is None else [e for e in _law if e not in ('bribe_barred', 'cleaving_commanded', 'stiffening_barred', 'heart_circumcision_commanded', 'fear_of_heaven_asked', 'love_owed', 'devoted_thing_cleaving_barred')]",
    "CH19_NECK_ST = ('heifer_neck_broken_commanded', 'elders_hands_washed_commanded')   # WWW: chapters 19-21's names carrying the neck (21:4, 21:6) — read at the tape's second run\nLAW_SCAN = None if _law is None else [e for e in _law if e not in ('bribe_barred', 'cleaving_commanded', 'stiffening_barred', 'heart_circumcision_commanded', 'fear_of_heaven_asked', 'love_owed', 'devoted_thing_cleaving_barred') and e not in CH19_NECK_ST]".replace('WWW', W))])
print('widened, fifth: second_tablets LAW_SCAN (heifer_neck_broken_commanded, elders_hands_washed_commanded)')
print('widened: good_land GARMENT_SCAN (captive_mourning_month_commanded), not_righteousness STIFF_SCAN (heifer_neck_broken_commanded, elders_hands_washed_commanded), the tape\'s CU7 and DA6; all compile')
