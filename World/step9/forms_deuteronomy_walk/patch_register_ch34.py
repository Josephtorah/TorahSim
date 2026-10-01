import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 22b (2026-09-30; LEAN): THE RECEIPT AT 34:9 RE-DECLARED — register_dispositions.yaml's 'Deut 34:9' retyped to the class THE REGISTER GATE COMPUTES, READ FROM ITS OWN PRINT
# (the seat's line prints the COMPUTED class; a declaration that differs is a LIE in the FAILS list — register_census.py verify()). THE FIND (22b, two prints): the gate classes a receipt from the
# REPLAYED TAPE (class_receipts — CLOSE/ACT/EVENT/CHAPTER by the entries whose case_source holds the verse), so run ALONE BEFORE THE STITCHER it held NONE with an empty evidence list (the tape
# carried no line at 34:9 yet — the first print, 'NONE declared | []'), and run AFTER THE STITCHER it computes the class the chapter's own line gives the seat (the second print — the file's
# argument). The seat's block replaced whole (whatever it held), the why the design's with the print's own line quoted; idempotent on the same print. RUN FROM THE REPO ROOT: python3 patch_register_ch34.py <the gate's out file>
import re, subprocess, yaml, sys, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else 'ch34b_register_first.out'
pr = open(f'{SP}/{OUT}', encoding='utf-8').read()
m = re.search(r"^\s+Deut 34:9\s+([A-Z\-]+)\s+(\S+)\s+\| (\[.*?)(?: \| why: (.*))?$", pr, re.M)   # the evidence list is CUT at 110 characters in the gate's print — the bracket may not close (the second print's find)
assert m, 'the gate\'s own line for the seat (Deut 34:9  CLASS  standing | [evidence] | why) — read, never guessed: %r' % [l for l in pr.split('\n') if '34:9' in l][:5]
CLS, STANDING, EVID = m.group(1), m.group(2), m.group(3); LINE = m.group(0).strip()
LIE = re.search(r"^\s+receipts Deut 34:9: LIE — declared ([A-Z\-]+), computed ([A-Z\-]+)$", pr, re.M)
print('the gate\'s line for Deut 34:9:', repr(LINE[:200])); print('the class the gate computes:', CLS, '| standing:', STANDING, '| the evidence:', EVID[:160], '| the FAILS line:', LIE.group(0).strip() if LIE else 'none')
if LIE: assert LIE.group(2) == CLS, (LIE.group(2), CLS)
F = f'{ROOT}/World/step9/register_dispositions.yaml'
t = open(F, encoding='utf-8').read()
i = t.index('\n  Deut 34:9:\n') + 1; j = i + 1
while True:
    j = t.find('\n', j) + 1
    if j <= 0 or j >= len(t) or (not t[j:].startswith('    ') and t[j:].strip()): break
OLD = t[i:j]; assert OLD.startswith('  Deut 34:9:\n') and 'class:' in OLD, OLD[:200]
BEFORE = yaml.safe_load(OLD)['Deut 34:9']
WHY = ("THE DEUTERONOMY WALK 22b (2026-09-30; LEAN) | 'and the children of Israel hearkened to him, and did AS THE LORD COMMANDED MOSES' — THE RECEIPT of chapter 34 (the tabernacle's formula at its "
       "last Torah seat, thirty-eight in the Torah): the class %s AS THE REGISTER GATE COMPUTES IT, read from its own print with the tape carrying chapter 34 (register_census.py --strict run alone "
       "after the stitcher at 22b's RUN B; its line '%s'%s); the gate classes a receipt from the REPLAYED TAPE — the chapter's own line joshua_full_of_the_spirit_israel_hearkened at 34:9 writes "
       "spirit_of_wisdom_by_the_hands_laid on yehoshua and israel_hearkened_to_joshua_as_the_lord_commanded_moses on israel_people with the seat in their case_source (an ACT on the tape — 10:5's "
       "and 20:17's precedent); run alone BEFORE the stitcher the same gate held NONE with an empty evidence list (the first print — 22b's find: the gate decides only after the stitcher); the "
       "referent the READBACK supplies BY CALL as a RUN CITATION: THE COMMISSION Numbers 27:18-23 on the tape (joshua_commissioned at 27:22 — invested_office on yehoshua; 31:7 and 31:23 the charge "
       "and the commission at the tent; the readback's RECEIPT ROW 34:9, tape_kind joshua_commissioned at Num 27:22; zelophehad and opening_speech by CALL); the NONE line of Numbers' close "
       "('Deuteronomy is not on the tape (the book not read) — the seat waits for its reading and compile') REMOVED — the book read to its last verse and compiled" % (CLS, LINE[:170].replace('"', "'"), (" — the FAILS line '%s' the lie the retype repairs" % LIE.group(0).strip()) if LIE else ''))
NEW = "  Deut 34:9:\n    class: %s\n    why: %s\n" % (CLS, yaml.safe_dump(WHY, allow_unicode=True, width=10**6, default_style='"').strip())
t2 = t[:i] + NEW + t[j:]
rg = yaml.safe_load(t2); assert rg['receipts']['Deut 34:9']['class'] == CLS and 'compiled' in rg['receipts']['Deut 34:9']['why'] and len(rg['receipts']) == 53, (rg['receipts']['Deut 34:9'], len(rg['receipts']))
open(F, 'w', encoding='utf-8').write(t2)
print('WRITTEN: register_dispositions.yaml receipts Deut 34:9 — class %s -> %s (the gate\'s print %s); receipts %d' % (BEFORE['class'], CLS, OUT, len(rg['receipts'])))
