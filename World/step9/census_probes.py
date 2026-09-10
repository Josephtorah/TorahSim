#!/usr/bin/env python3
"""census_probes.py — THE NUMBERS WALK, the compile of Bamidbar (2026-09-09; World/step9/NUMBERS_WALK.md "Sitting 1b — THE COMPILE"):
the fire-probes for THE CENSUS'S NUMBER GRAMMAR in the engine's numeral parser (cold_run_sequence.ink_numbers, SEQUENTIAL_RUN.md
section 4), written BEFORE the parser is taught. Against the unchanged parser every census probe must FAIL (measured at the
reading sitting: 1:21 -> [1546]); after the code every probe must PASS, and the Genesis/Exodus grammar must be UNMOVED (the
regression probes here, and every marker on the tape re-verified by the stitcher and at run time). The expected numbers are the
ink's own, proved by the ledger script (write_bamidbar_ledgers.py): the twelve sum to 1:46, the camps to 2:32, 22,273 - 22,000 =
273, 273 x 5 = 1,365. Probes:
  N1  1:21 six-and-forty THOUSAND and five hundred = 46,500 (the thousand multiplies the group before it)
  N2  1:46 six hundred thousand and three thousands and five hundred and fifty = 603,550 (two thousands-words, each its own group)
  N3  2:9  a hundred thousand and eighty thousand and six thousands and four hundred = 186,400
  N4  3:39 two-and-twenty thousand = 22,000 ('two' before 'and twenty' is a numeral, not 'years')
  N5  3:43 22,273 (the thousands first, the remainder ascending)
  N6  3:46 the three and the seventy and the two hundred = 273 (the article on each part)
  N7  3:47 five, five shekels ... twenty gerah = [5, 20] (a doubled numeral is DISTRIBUTIVE, one number)
  N8  3:50 five and sixty and three hundred AND A THOUSAND = 1,365 ('and a thousand' ADDS; 'from' before 'the firstborn' is no number)
  N9  3:49 'from those who exceeded' = [] (מאת "from" is not מאת "a hundred of" — told by what follows it)
  N10 Exod 38:26 = [20, 603550] (the same count on the erection's seat)
  N11 3:22 seven thousands and five hundred = 7,500; 3:28 = 8,600; 3:34 = 6,200
  R1  Gen 5:6 five years and a hundred years = [105] (the year-word keeps the phrase open — UNMOVED)
  R2  Exod 24:18 forty days and forty nights = [40, 40] (a noun closes the phrase — UNMOVED)
  R3  Gen 23:20 'from (מאת) the sons of Heth' = [] (the homograph in Genesis, unmoved)
  R4  Exod 38:25 a hundred talents and a thousand seven hundred and seventy-five shekels = [100, 1775] ('and a thousand' adds here too)
Run: python3 World/step9/census_probes.py
"""
import os, sys, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS

CASES = [
    ('N1  Num 1:21 = 46,500', ('Num', 1, 21), [46500]),
    ('N2  Num 1:46 = 603,550', ('Num', 1, 46), [603550]),
    ('N3  Num 2:9 = 186,400', ('Num', 2, 9), [186400]),
    ('N4  Num 3:39 = 22,000', ('Num', 3, 39), [22000]),
    ('N5  Num 3:43 = 22,273', ('Num', 3, 43), [22273]),
    ('N6  Num 3:46 = 273', ('Num', 3, 46), [273]),
    ('N7  Num 3:47 = [5, 20]', ('Num', 3, 47), [5, 20]),
    ('N8  Num 3:50 = 1,365', ('Num', 3, 50), [1365]),
    ('N9  Num 3:49 = []', ('Num', 3, 49), []),
    ('N10 Exod 38:26 = [20, 603550]', ('Exod', 38, 26), [20, 603550]),
    ('N11 Num 3:22 = 7,500', ('Num', 3, 22), [7500]),
    ('N11 Num 3:28 = 8,600', ('Num', 3, 28), [8600]),
    ('N11 Num 3:34 = 6,200', ('Num', 3, 34), [6200]),
    ('R1  Gen 5:6 = [105]', ('Gen', 5, 6), [105]),
    ('R2  Exod 24:18 = [40, 40]', ('Exod', 24, 18), [40, 40]),
    ('R3  Gen 23:20 = []', ('Gen', 23, 20), []),
    ('R4  Exod 38:25 = [100, 1775]', ('Exod', 38, 25), [100, 1775]),
]

if __name__ == '__main__':
    ok = 0
    print('THE CENSUS GRAMMAR — the numeral parser\'s fire-probes')
    for name, (b, c, v), want in CASES:
        got = CS.ink_numbers(CS.verse_words(b, c, v))
        hit = got == want
        ok += hit
        print('  %s  %s   got %s' % ('PASS' if hit else 'FAIL', name, got))
    print('%d/%d probes' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
