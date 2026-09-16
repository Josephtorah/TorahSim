#!/usr/bin/env python3
# THE DEUTERONOMY WALK 1b (2026-09-15): THE PROBES TO FAIL — rule (30) THE HALF OF A NAMED WHOLE's nine probes (D10-D18) and seven regressions
# (R74-R80) inserted into World/step9/census_probes.py BEFORE the parser is taught; every expected number typed from deu_runner_measure.out and
# deu_compile_measure.out (the current reads printed beside the ink's own). Idempotent: refuses a second insertion. patch_probes_ref.py's form.
import re, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
P = ROOT + '/World/step9/census_probes.py'
src = open(P, encoding='utf-8').read()
assert 'D10 Deut 3:12' not in src, 'already inserted'
BLOCK = '''
# ---- THE DEUTERONOMY WALK 1b (2026-09-15; DEUTERONOMY_WALK.md "Sitting 1b" (e)): (30) THE HALF OF A NAMED WHOLE — the half-word in its bare and
#      prefixed forms (חצי 'half', וחצי 'and half', לחצי 'to half', ולחצי, בחצי, מחצי, ומחצי, כחצי, כבחצי, החצי 'the half', והחצי) and the half-part in
#      its unsuffixed forms (מחצית 'the half-part', ממחצית, וממחצית) read Fraction(1, 2) with the fraction mark when the token neither continues a
#      numeral or a unit noun (rule 7's 'and a half' stands) nor precedes a measure noun (the hin's and the shekel's fraction stands); the SUFFIXED
#      forms ('its half', 'our half', 'their half') stay silent — a part named, not a number counted. 139 tokens in 114 verses measured on the whole
#      Bible; the Torah's moving seats predicted FOURTEEN in thirteen verses. Written to FAIL on the parser 15b left (nine FAIL measured:
#      deu_runner_measure.out); the regressions unmoved before and after ----
CASES += [
    ('D10 Deut 3:12 = [1/2]  ("and HALF the hill country of Gilead" — the half before a named whole; was [])', ('Deut', 3, 12), [Fraction(1, 2)]),
    ('D11 Deut 3:13 = [1/2]  ("to the HALF tribe of Manasseh" — the prefixed half before the tribe; was [])', ('Deut', 3, 13), [Fraction(1, 2)]),
    ('D12 Num 32:33 = [1/2]  ("and to the half tribe of Manasseh son of Joseph" — the grant\\'s seat; was [])', ('Num', 32, 33), [Fraction(1, 2)]),
    ('D13 Num 34:13 = [9, 1/2]  ("to the nine tribes and the half tribe" — nine and a half; was [9])', ('Num', 34, 13), [9, Fraction(1, 2)]),
    ('D14 Num 34:14 = [1/2]  ("and the half tribe of Manasseh have taken their inheritance" — the other tribe-noun; was [])', ('Num', 34, 14), [Fraction(1, 2)]),
    ('D15 Num 34:15 = [2, 1/2]  ("the two tribes and the half tribe" — two and a half; was [2])', ('Num', 34, 15), [2, Fraction(1, 2)]),
    ('D16 Deut 29:7 = [1/2]  ("to the Reubenite and to the Gadite and to the half tribe of the Manassite" — the retelling\\'s own seat; was [])', ('Deut', 29, 7), [Fraction(1, 2)]),
    ('D17 Josh 13:7 = [9, 1/2]  ("to the nine tribes and the half tribe of Manasseh" — the run outside the Torah; was [9])', ('Josh', 13, 7), [9, Fraction(1, 2)]),
    ('D18 1Chr 5:18 = [1/2, 44760]  ("and the half tribe of Manasseh … forty-four thousand seven hundred and sixty" — the half then the count; was [44760])', ('1Chr', 5, 18), [Fraction(1, 2), 44760]),
    ('R74 Exod 25:10 = [2.5, 1.5, 1.5]  ("two cubits and a half … a cubit and a half" — rule 7\\'s continuation: UNMOVED)', ('Exod', 25, 10), [2.5, 1.5, 1.5]),
    ('R75 Exod 30:13 = [1/2, 20, 1/2]  ("half of the shekel … half of the shekel" — the fraction before the measure noun: UNMOVED)', ('Exod', 30, 13), [Fraction(1, 2), 20, Fraction(1, 2)]),
    ('R76 Num 15:9 = [3, 1/2]  ("three tenths … half of the hin" — UNMOVED)', ('Num', 15, 9), [3, Fraction(1, 2)]),
    ('R77 Num 28:14 = [1/2, 1/3, 1/4]  ("half of the hin … a third … a quarter" — UNMOVED)', ('Num', 28, 14), [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4)]),
    ('R78 Exod 26:16 = [10, 1.5, 1]  ("ten cubits … a cubit and a half of the cubit … the ONE board" — the unit noun as one continued by the half: UNMOVED)', ('Exod', 26, 16), [10, 1.5, 1]),
    ('R79 Lev 6:13 = [1/10]  ("a tenth of the ephah … its half in the morning and its half in the evening" — THE SUFFIXED HALVES silent: UNMOVED)', ('Lev', 6, 13), [Fraction(1, 10)]),
    ('R80 Num 31:47 = [1/50]  ("from the half-part of the children of Israel … one held out of the fifty" — the ratio stands; the half-part here inside the ratio\\'s phrase read as the ratio alone: UNMOVED)', ('Num', 31, 47), [Fraction(1, 50)]),
]
'''
i = src.index("\nif __name__ == '__main__':")
src = src[:i] + BLOCK + src[i:]
open(P, 'w', encoding='utf-8').write(src)
print('inserted 16 probes before the harness; census_probes.py now', len(re.findall(r"^\s*\('[A-Z]+\d+", src, re.M)), 'probe lines')
