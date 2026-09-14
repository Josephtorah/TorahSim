#!/usr/bin/env python3
# THE NUMBERS WALK 15b (2026-09-13): THE PROBES TO FAIL — rule (29) THE BARE DUAL THOUSAND's nine probes (D1-D9) and nine regressions (R62-R70)
# inserted into World/step9/census_probes.py BEFORE the parser is taught; every expected number typed from ref_runner_measure.out (the
# current reads printed beside the ink's own). Idempotent: refuses a second insertion.
import re
P = '<repo-old>/World/step9/census_probes.py'
src = open(P, encoding='utf-8').read()
assert 'D1  Num 35:5' not in src, 'already inserted'
BLOCK = '''
# ---- THE NUMBERS WALK 15b (2026-09-13; NUMBERS_WALK.md "Sitting 15b"): (29) THE BARE DUAL THOUSAND BY THE POINTS ON THE STEM — the dual
#      אַלְפַּיִם ('two thousand': a sheva under the lamed, a patach with the dagesh in the pe; TWENTY-NINE Tanakh seats measured) had read only inside a
#      compound (4:36, 4:40, 7:85, Exod 38:29, Dan 8:14 …); BARE it read nothing (Num 35:5 x4, 1 Kgs 7:26, 2 Kgs 18:23, Isa 36:8), the cubit as one
#      (Josh 3:4), was swallowed (Josh 7:3, Judg 20:45) or read as a thousand (1 Sam 13:2); and the bare PLURAL אֲלָפִים ('thousands': a qamats under
#      the lamed; 146 seats) after a conjunction took the dual's path — Ps 8:8 'sheep and OXEN' read [2000] since 1b. The rule: verse_words marks the
#      dual by the points (the dual mark ~), ink_numbers reads the marked dual as 2,000 wherever it stands and the bare plural as a noun. Written to FAIL
#      on the parser 14b left (nine FAIL measured: ref_runner_measure.out); the regressions unmoved before and after ----
CASES += [
    ('D1  Num 35:5 = [2000, 2000, 2000, 2000]  ("two thousand by the cubit" four times — the prefixed cubit no unit-noun mark; was [])', ('Num', 35, 5), [2000, 2000, 2000, 2000]),
    ('D2  Josh 3:4 = [2000]  ("about two thousand cubits" — the approximation prefix; the cubit consumed as the unit noun; was [1])', ('Josh', 3, 4), [2000]),
    ('D3  Josh 7:3 = [2000, 3000]  ("about two thousand men or about three thousand men" — the dual then the plural after a unit; was [3000])', ('Josh', 7, 3), [2000, 3000]),
    ('D4  Judg 20:45 = [5000, 2000]  ("five thousand men … two thousand men" — was [5000])', ('Judg', 20, 45), [5000, 2000]),
    ('D5  1Sam 13:2 = [3000, 2000, 1000]  ("three thousand … two thousand with Saul … and a thousand with Jonathan" — the dual had read as a thousand: was [3000, 1000])', ('1Sam', 13, 2), [3000, 2000, 1000]),
    ('D6  1Kgs 7:26 = [2000]  ("two thousand baths it held" — the sea of Solomon; was [])', ('1Kgs', 7, 26), [2000]),
    ('D7  2Kgs 18:23 = [2000]  ("two thousand horses" — was [])', ('2Kgs', 18, 23), [2000]),
    ('D8  Isa 36:8 = [2000]  ("two thousand horses" — the parallel; was [])', ('Isa', 36, 8), [2000]),
    ('D9  Ps 8:8 = []  ("sheep and OXEN, all of them" — the plural\\'s consonants after the conjunction, a qamats under the lamed: a NOUN; the false reading [2000] since 1b, surfaced by the class measurement)', ('Ps', 8, 8), []),
    ('R62 Num 4:36 = [2750]  ("two thousand seven hundred and fifty" — the dual inside a compound: UNMOVED)', ('Num', 4, 36), [2750]),
    ('R63 Exod 38:29 = [70, 2400]  ("seventy talents and two thousand and four hundred shekels" — the dual with the conjunction: UNMOVED)', ('Exod', 38, 29), [70, 2400]),
    ('R64 Dan 8:14 = [2300]  ("two thousand and three hundred" — UNMOVED)', ('Dan', 8, 14), [2300]),
    ('R65 Num 7:85 = [130, 1, 70, 1, 2400]  ("two thousand and four hundred by the shekel of the sanctuary" — the definite ones cut, UNMOVED)', ('Num', 7, 85), [130, 1, 70, 1, 2400]),
    ('R66 Exod 18:21 = [100, 50, 10]  ("rulers of thousands, rulers of hundreds …" — the bare plural a noun: UNMOVED)', ('Exod', 18, 21), [100, 50, 10]),
    ('R67 Num 1:46 = [603550]  ("six hundred thousand and three thousands and five hundred and fifty" — the plural after a unit multiplies: UNMOVED)', ('Num', 1, 46), [603550]),
    ('R68 Exod 32:28 = [3000]  ("about three thousands of men" — the construct after a unit: UNMOVED)', ('Exod', 32, 28), [3000]),
    ('R69 Num 26:62 = [23000]  ("three and twenty thousand" — UNMOVED)', ('Num', 26, 62), [23000]),
    ('R70 Ezra 2:3 = [2172]  ("two thousand a hundred seventy and two" — the dual heading a compound without the conjunction: UNMOVED)', ('Ezra', 2, 3), [2172]),
]
'''
i = src.index("\nif __name__ == '__main__':")
src = src[:i] + BLOCK + src[i:]
open(P, 'w', encoding='utf-8').write(src)
print('inserted 18 probes before the harness; census_probes.py now', len(re.findall(r"^\s*\('[A-Z]+\d+", src, re.M)), 'probe lines')
