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
from fractions import Fraction   # THE NUMBERS WALK 4b (2026-09-10): the fraction class reads as exact fractions
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
    ('N10 Exod 38:26 = [1/2, 20, 603550]  (4b: "HALF of the shekel by the shekel of the sanctuary" read as the fraction; was [20, 603550], retyped from the reading)', ('Exod', 38, 26), [Fraction(1, 2), 20, 603550]),
    ('N11 Num 3:22 = 7,500', ('Num', 3, 22), [7500]),
    ('N11 Num 3:28 = 8,600', ('Num', 3, 28), [8600]),
    ('N11 Num 3:34 = 6,200', ('Num', 3, 34), [6200]),
    ('R1  Gen 5:6 = [105]', ('Gen', 5, 6), [105]),
    ('R2  Exod 24:18 = [40, 40]', ('Exod', 24, 18), [40, 40]),
    ('R3  Gen 23:20 = []', ('Gen', 23, 20), []),
    ('R4  Exod 38:25 = [100, 1775]', ('Exod', 38, 25), [100, 1775]),
    # ---- THE NUMBERS WALK 2b (2026-09-10; NUMBERS_WALK.md "Sitting 2b"): NASO'S GAPS, written to FAIL on the parser 1b left ----
    ('N12 Num 7:3 = [6, 12, 2, 1]  (the construct "two of" by its points; "twelve" = two-of + ten)', ('Num', 7, 3), [6, 12, 2, 1]),
    ('N13 Num 7:7 = [2, 4]  ("two of the wagons")', ('Num', 7, 7), [2, 4]),
    ('N14 Num 6:10 = [2, 2]  ("two turtledoves or two young pigeons")', ('Num', 6, 10), [2, 2]),
    ('N15 Num 7:13 = [1, 130, 1, 70, 2]  (M-26: the revia on "one" ends the number; 3b: "BOTH OF THEM full" — the suffixed numeral, the fifth number)', ('Num', 7, 13), [1, 130, 1, 70, 2]),
    ('N16 Num 7:14 = [1, 10]  (M-26: the tevir on "one" — one pan, ten of gold)', ('Num', 7, 14), [1, 10]),
    ('N17 Num 7:72 = [11]  ("ashtei asar" — eleven)', ('Num', 7, 72), [11]),
    ('N18 Num 28:27 = [2, 1, 7]  (the etnachta on "one ram" before "seven lambs" — the fused one at a third seat)', ('Num', 28, 27), [2, 1, 7]),
    ('N19 Exod 26:7 = [11]  (eleven curtains)', ('Exod', 26, 7), [11]),
    ('R5  Gen 32:23 = [2, 2, 11]  (a merkha on "one": joined; "his TWO wives and his TWO maids" the construct now read — the row retyped from the diff)', ('Gen', 32, 23), [2, 2, 11]),
    ('R6  Deut 1:2 = [11]  (a qadma on "one": joined — UNMOVED)', ('Deut', 1, 2), [11]),
    ('R7  Num 7:78 = [12]  (the twelfth day — UNMOVED)', ('Num', 7, 78), [12]),
    ('R8  Num 7:85 = [130, 1, 70, 1, 2400]  (the totals — 4b: THE DEFINITE ONE "the one dish", "the one bowl" read; was [130, 70, 2400], retyped from the reading)', ('Num', 7, 85), [130, 1, 70, 1, 2400]),
    ('R9  Num 4:36 = [2750]  (the dual thousands — UNMOVED)', ('Num', 4, 36), [2750]),
    ('R10 Num 1:21 = [46500]  (the tevir on "forty" before "thousand" does NOT cut — UNMOVED)', ('Num', 1, 21), [46500]),    # THE NUMBERS WALK 3b (2026-09-10; NUMBERS_WALK.md "Sitting 3b"): THE DUAL NOUN, THE HALF, THE SUFFIXED NUMERAL — typed to FAIL before the rules
    ('D1  Num 11:19 = [1, 2, 5, 10, 20]  (the day-ladder: "not one day, nor TWO DAYS (the dual), nor five days, nor ten days, nor twenty days")', ('Num', 11, 19), [1, 2, 5, 10, 20]),
    ('D2  Num 11:31 = [2]  ("about TWO CUBITS above the face of the earth" — the dual)', ('Num', 11, 31), [2]),
    ('D3  Num 12:4 = [3, 3]  ("come out, THE THREE OF YOU... and THE THREE OF THEM came out" — the suffixed numeral)', ('Num', 12, 4), [3, 3]),
    ('D4  Exod 25:10 = [2.5, 1.5, 1.5]  ("TWO CUBITS AND A HALF its length" — the dual and the half; 4b: "a cubit and a half" twice after it now READ — the unit noun as one, 3b\'s residue paid; was [2.5])', ('Exod', 25, 10), [2.5, 1.5, 1.5]),
    ('D5  Exod 25:23 = [2, 1, 1.5]  ("TWO CUBITS its length, and A CUBIT its breadth, and A CUBIT AND A HALF its height" — the table; 4b: the cubit as one; was [2])', ('Exod', 25, 23), [2, 1, 1.5]),
    ('D6  Exod 30:2 = [1, 1, 2]  ("A CUBIT its length and A CUBIT its breadth... and TWO CUBITS its height" — the incense altar; 4b: the cubit as one; was [2])', ('Exod', 30, 2), [1, 1, 2]),
    ('D7  Gen 2:25 = [2]  ("and THE TWO OF THEM were naked")', ('Gen', 2, 25), [2]),
    ('D8  Gen 27:45 = [2, 1]  ("why should I be bereaved of THE TWO OF YOU in ONE day")', ('Gen', 27, 45), [2, 1]),
    ('D9  Exod 16:29 = [2]  ("the bread of TWO DAYS")', ('Exod', 16, 29), [2]),
    ('D10 Exod 21:21 = [2]  ("a day or TWO DAYS")', ('Exod', 21, 21), [2]),
    ('D11 Num 10:36 = []  ("the myriads of the thousands of Israel" — two plural nouns, no numeral: the shelf\'s 22,000 a DATUM — UNMOVED)', ('Num', 10, 36), []),
    ('D12 Gen 4:24 = [77]  ("sevenfold... seventy and seven" — שבעתים "sevenfold" is an adverb, not read: UNMOVED; the hand had typed [7, 77] and the first run read it)', ('Gen', 4, 24), [77]),
    # THE NUMBERS WALK 3b (2026-09-10): FOUR PRE-EXISTING FALSE READINGS SURFACED BY THE SITTING'S DIFF, typed to FAIL before the rules — the seven-stem's homographs
    ('E1  Gen 41:29 = [7]  ("seven years of great PLENTY" — שָׂבָע with the SIN dot is plenty, not seven; the hand read [7, 7])', ('Gen', 41, 29), [7]),
    ('E2  Gen 41:34 = [5, 7]  ("a fifth... IN THE SEVEN years of PLENTY" — בְּשֶׁבַע the true seven before the starred plenty-word: UNMOVED; the hand had typed [5] and the first run read the ink)', ('Gen', 41, 34), [5, 7]),
    ('E3  Deut 6:11 = []  ("and you shall eat and be SATED" — the sin dot; was [7])', ('Deut', 6, 11), []),
    ('E4  Gen 25:8 = []  ("old and FULL of days" — the sin dot; was [7])', ('Gen', 25, 8), []),
    ('E5  Exod 22:10 = [2]  ("the OATH of the LORD shall be between the two of them" — שְׁבֻעַת with the qubuts is the oath; was [7, 2])', ('Exod', 22, 10), [2]),
    ('E6  Deut 16:9 = [7, 7]  ("seven WEEKS you shall count... seven WEEKS" — שָׁבֻעֹת with the qubuts is weeks; was [14, 7])', ('Deut', 16, 9), [7, 7]),
    ('E7  Exod 34:22 = []  ("the feast of WEEKS" — the qubuts; was [7])', ('Exod', 34, 22), []),
    ('E8  Gen 29:28 = []  ("and he fulfilled the WEEK of this one" — שְׁבֻעַ the qubuts; was [7])', ('Gen', 29, 28), []),
    ('E9  Num 5:21 = []  ("with the OATH of the curse... for an OATH" — the qubuts twice; was [7, 7])', ('Num', 5, 21), []),
    ('E10 Lev 5:4 = [1]  ("to swear with an OATH... one of these" — the qubuts; was [7, 1])', ('Lev', 5, 4), [1]),
    ('E11 Num 30:3 = []  ("or swears an OATH" — the qubuts; was [7])', ('Num', 30, 3), []),
    ('E12 Exod 21:2 = [6]  ("six years he shall serve and in the SEVENTH he shall go out" — שְּׁבִעִת with the hiriq under the vet is the ordinal; was [6, 7])', ('Exod', 21, 2), [6]),
    ('E13 Gen 21:31 = [2]  ("BEER-SHEBA, for there the two of them swore" — the name after באר, as Kiriath-arba; was [7, 2])', ('Gen', 21, 31), [2]),
    ('E14 Gen 22:19 = []  ("to BEER-SHEBA; and Abraham dwelt at BEER-SHEBA" — the name twice; was [7, 7])', ('Gen', 22, 19), []),
    ('E15 Gen 26:33 = []  ("and he called it SHIBAH; therefore the name of the city is BEER-SHEBA" — the well named by the naming verb, the city by באר; was [7, 7])', ('Gen', 26, 33), []),
    ('E16 Gen 41:47 = [7]  ("in the seven years of PLENTY" — the sin dot; the years-of neighbor list already knew הַשָּׂבָע; UNMOVED)', ('Gen', 41, 47), [7]),
    ('E17 Num 1:39 = [62700]  ("two and sixty thousand and seven hundred" — וּשְׁבַע with the shureq on the CONJUNCTION, not the vet: seven — UNMOVED)', ('Num', 1, 39), [62700]),
    # ---- THE NUMBERS WALK 4b (2026-09-10; NUMBERS_WALK.md "Sitting 4b"): SHELACH'S GAPS — THE FRACTION CLASS, THE UNIT NOUN AS ONE, THE DEFINITE ONE,
    #      THE THIRD-GENERATION HOMOGRAPH, THE TITHE VERB; written to FAIL on the parser 3b left ----
    ('F1  Num 15:4 = [1, 1/4]  ("a tenth of fine flour... a quarter of the hin" — the unit noun as ONE; the fraction before the measure noun)', ('Num', 15, 4), [1, Fraction(1, 4)]),
    ('F2  Num 15:5 = [1/4, 1]  ("wine for the libation a quarter of the hin... for the ONE lamb" — the fraction; THE DEFINITE ONE)', ('Num', 15, 5), [Fraction(1, 4), 1]),
    ('F3  Num 15:6 = [2, 1/3]  ("two tenths... a third of the hin" — the ram\'s row)', ('Num', 15, 6), [2, Fraction(1, 3)]),
    ('F4  Num 15:7 = [1/3]  ("wine for the libation a third of the hin")', ('Num', 15, 7), [Fraction(1, 3)]),
    ('F5  Num 15:9 = [3, 1/2]  ("three tenths... half of the hin" — the bull\'s row)', ('Num', 15, 9), [3, Fraction(1, 2)]),
    ('F6  Num 15:10 = [1/2]  ("wine for the libation half of the hin" — the half before the measure noun, no numeral before it)', ('Num', 15, 10), [Fraction(1, 2)]),
    ('F7  Num 15:11 = [1, 1]  ("for the ONE ox or for the ONE ram" — the definite one twice)', ('Num', 15, 11), [1, 1]),
    ('F8  Num 28:14 = [1/2, 1/3, 1/4]  ("half of the hin for the bull, a third of the hin for the ram, a quarter of the hin for the lamb" — the table\'s second seat)', ('Num', 28, 14), [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4)]),
    ('F9  Exod 29:40 = [1, 1/4, 1/4, 1]  ("a tenth of fine flour... a quarter of the hin... a quarter of the hin of wine for the ONE lamb" — the tamid\'s seat: the quarter spelled two ways in one verse)', ('Exod', 29, 40), [1, Fraction(1, 4), Fraction(1, 4), 1]),
    ('F10 Lev 23:13 = [2, 1/4]  ("two tenths... wine a quarter of the hin" — the omer\'s lamb)', ('Lev', 23, 13), [2, Fraction(1, 4)]),
    ('F11 Num 28:5 = [1/10, 1/4]  ("a tenth of the ephah of fine flour... a quarter of the hin" — the tenth as a FRACTION of the ephah)', ('Num', 28, 5), [Fraction(1, 10), Fraction(1, 4)]),
    ('F12 Num 28:7 = [1/4, 1]  ("its libation a quarter of the hin for the ONE lamb")', ('Num', 28, 7), [Fraction(1, 4), 1]),
    ('F13 Exod 30:13 = [1/2, 20, 1/2]  ("half of the shekel... twenty gerah the shekel; half of the shekel a terumah" — the half before the shekel, twice)', ('Exod', 30, 13), [Fraction(1, 2), 20, Fraction(1, 2)]),
    ('F14 Lev 5:11 = [2, 2, 1/10]  ("two turtledoves or two young pigeons... a tenth of the ephah")', ('Lev', 5, 11), [2, 2, Fraction(1, 10)]),
    ('F15 Num 5:15 = [1/10]  ("a tenth of the ephah of barley flour" — the jealousy offering)', ('Num', 5, 15), [Fraction(1, 10)]),
    ('F16 Num 28:13 = [1, 1]  ("and a tenth, a tenth of fine flour... for the ONE lamb" — the doubled unit noun is DISTRIBUTIVE, one; the definite one)', ('Num', 28, 13), [1, 1]),
    ('F17 Num 29:4 = [1, 1, 7]  ("and a tenth, ONE, for the ONE lamb, for the seven lambs" — the unit noun before its own numeral stays silent; the definite one; seven)', ('Num', 29, 4), [1, 1, 7]),
    ('F18 Num 28:21 = [1, 1, 7]  ("a tenth, a tenth for the ONE lamb, for the seven lambs")', ('Num', 28, 21), [1, 1, 7]),
    ('F19 Num 29:15 = [1, 1, 14]  ("and a tenth, a tenth for the ONE lamb, for the fourteen lambs")', ('Num', 29, 15), [1, 1, 14]),
    ('F20 Exod 25:10 = [2.5, 1.5, 1.5]  ("two cubits and a half its length, and a cubit and a half its breadth, and a cubit and a half its height" — THE CUBIT AS ONE by its points: 3b\'s residue paid)', ('Exod', 25, 10), [2.5, 1.5, 1.5]),
    ('F21 Exod 26:16 = [10, 1.5, 1]  ("ten cubits the length of the board, and a cubit and a half OF THE cubit the breadth of the ONE board" — the article form is the fraction\'s object, not a second cubit)', ('Exod', 26, 16), [10, 1.5, 1]),
    ('F22 Exod 30:24 = [500, 1]  ("cassia five hundred by the shekel of the sanctuary, and olive oil a HIN" — the hin as one)', ('Exod', 30, 24), [500, 1]),
    ('F23 Gen 6:16 = [1]  ("to a CUBIT you shall finish it above... lower, SECOND and THIRD stories" — the cubit as one; the third-stories word (a hiriq under the lamed) no longer thirty)', ('Gen', 6, 16), [1]),
    ('F24 Num 14:18 = []  ("upon the third and upon the fourth generation" — THE THIRD-GENERATION HOMOGRAPH: a hiriq under the shin, a dagesh and a tsere in the lamed, read as thirty at five seats)', ('Num', 14, 18), []),
    ('F25 Exod 34:7 = []  (the attributes\' own verse — the third generation, was [30])', ('Exod', 34, 7), []),
    ('F26 Exod 20:5 = []  (the Decalogue — the third generation, was [30])', ('Exod', 20, 5), []),
    ('F27 Deut 5:9 = []  (the second Decalogue — was [30])', ('Deut', 5, 9), []),
    ('F28 Gen 50:23 = []  ("the children of the third generation" — was [30])', ('Gen', 50, 23), []),
    ('F29 Exod 26:19 = [40, 20, 2, 1, 2, 2, 1, 2]  ("forty sockets under the twenty boards: two sockets under the ONE board for its two tenons, and two sockets under the ONE board for its two tenons" — the definite one closes its phrase)', ('Exod', 26, 19), [40, 20, 2, 1, 2, 2, 1, 2]),
    ('F30 Lev 14:22 = [2, 2, 1, 1]  ("the one a sin offering and THE ONE a burnt offering" — the definite one with the vav counts too: the 2b "and the other" seat retyped)', ('Lev', 14, 22), [2, 2, 1, 1]),
    ('F31 Gen 28:22 = []  ("I will surely TITHE it" — the tithe verb, a patach under the ayin, read as ten; was [10])', ('Gen', 28, 22), []),
    ('F32 Deut 14:22 = []  ("you shall surely TITHE" — was [10])', ('Deut', 14, 22), []),
    ('F33 Deut 26:12 = []  ("when you have finished TITHING all the tithe... in the third year, the year of the tithe" — was [10])', ('Deut', 26, 12), []),
    ('F34 Exod 12:18 = [14, 21]  ("on the fourteenth day... until the ONE AND TWENTIETH day" — the definite one before a conjoined numeral JOINS it: the diff read [14, 1, 20] on the first rule)', ('Exod', 12, 18), [14, 21]),
    ('R11 Exod 12:29 = []  ("at HALF of the night" — the half before a non-measure stays a word: THE EXODUS MARKER\'S VERSE, UNMOVED)', ('Exod', 12, 29), []),
    ('R12 Num 23:10 = []  ("the fourth part of Israel" — a holam, no measure after it: UNMOVED)', ('Num', 23, 10), []),
    ('R13 Num 31:8 = [5]  ("Evi and Rekem and Zur and Hur and REBA, the five kings" — the name, not the quarter: UNMOVED)', ('Num', 31, 8), [5]),
    ('R14 Exod 21:32 = [30]  ("a MAIDSERVANT... thirty shekels" — the qamats, not the cubit: UNMOVED)', ('Exod', 21, 32), [30]),
    ('R15 Gen 21:10 = []  ("cast out this MAIDSERVANT" — UNMOVED)', ('Gen', 21, 10), []),
    ('R16 Deut 21:13 = []  ("her father and HER MOTHER" — the mappiq: UNMOVED)', ('Deut', 21, 13), []),
    ('R17 Num 32:33 = []  ("and to HALF the tribe of Manasseh" — no measure noun: UNMOVED)', ('Num', 32, 33), []),
    ('R18 Lev 19:24 = []  ("in the FOURTH year" — the ordinal stays an ordinal: UNMOVED)', ('Lev', 19, 24), []),
    ('R19 Num 35:4 = [1000]  ("a thousand cubits round about" — the cubit after its numeral does not add: UNMOVED)', ('Num', 35, 4), [1000]),
    ('R20 Exod 12:3 = [10]  ("on the TENTH of this month" — the date noun: UNMOVED)', ('Exod', 12, 3), [10]),
    ('R21 Lev 14:21 = [1, 1]  ("one lamb... a tenth of fine flour, ONE... a log of oil" — the unit noun before its numeral two words on stays silent: UNMOVED)', ('Lev', 14, 21), [1, 1]),
    # ---- THE NUMBERS WALK 5b (2026-09-10; NUMBERS_WALK.md "Sitting 5b"): KORACH'S GAP — THE DEFINITE NUMERAL AT THE HEAD OF A COMPOUND, and the three
    #      false readings the class's census surfaced (Exod 38:28, Num 31:54, Exod 26:5 / 36:12 — the last a 4b join accepted off the diff); written to FAIL on the parser 4b left ----
    ('G1  Num 16:35 = [250]  ("THE fifty and two hundred men" — the article on the head of a chain joined by plain "and" + a bare numeral OPENS the chain; was [200])', ('Num', 16, 35), [250]),
    ('G2  Exod 38:28 = [1775]  ("THE thousand and seven THE hundreds and five and seventy" — the head\'s article, and the article on the hundreds-word after a unit MULTIPLIES: 38:25\'s own 1,775 at its second seat; was [7, 75])', ('Exod', 38, 28), [1775]),
    ('G3  Num 31:54 = []  ("the captains of THE THOUSANDS and of THE HUNDREDS" — the article-bearing PLURAL unit word with no numeral before it is a noun; the "and the" chain needs a numeral head; was [2100])', ('Num', 31, 54), []),
    ('G4  Exod 26:5 = [50, 1, 50]  ("fifty loops... in the ONE curtain, and fifty loops" — the definite one under a DISJUNCTIVE accent (a segolta) CLOSES and counts one by 4b\'s rule (14), as at 26:4 and 26:10: M-26\'s read extended to the definite one; the 4b join had read [50, 51]; THE HAND HAD TYPED [50, 50] — retyped from the reading of the class)', ('Exod', 26, 5), [50, 1, 50]),
    ('G5  Exod 36:12 = [50, 1, 50, 1, 1]  ("fifty loops in the ONE curtain, and fifty loops... the one... the one" — the segolta closes, the definite one counts one; was [50, 51, 1, 1]; the hand had typed [50, 50, 1, 1])', ('Exod', 36, 12), [50, 1, 50, 1, 1]),
    ('G6  Exod 25:32 = [6, 3, 1, 3]  ("six branches... three branches from its ONE side, and three branches from its second side" — the definite one under a zaqef (disjunctive) closes and counts one (25:33\'s "in the one branch" the same class); the 4b join had read [6, 3, 4]; the hand had typed [6, 3, 3])', ('Exod', 25, 32), [6, 3, 1, 3]),
    ('G7  Exod 37:18 = [6, 3, 1, 3]  (the same verse at the making; was [6, 3, 4]; the hand had typed [6, 3, 3])', ('Exod', 37, 18), [6, 3, 1, 3]),
    ('R22 Exod 12:18 = [14, 21]  ("the ONE and twentieth" under a darga (conjunctive) still JOINS — F34 UNMOVED)', ('Exod', 12, 18), [14, 21]),
    ('R23 Num 3:46 = [273]  ("the three and the seventy and the two hundred" — the article on each part: UNMOVED)', ('Num', 3, 46), [273]),
    ('R24 Num 31:52 = [16750]  ("the captains of the thousands and FROM the captains of the hundreds" — the plural noun silent, "from" by its points: UNMOVED)', ('Num', 31, 52), [16750]),
    ('R25 Num 31:14 = []  ("the captains of the thousands and the captains of the hundreds" — no chain: UNMOVED)', ('Num', 31, 14), []),
    ('R26 Num 31:48 = []  (the same phrase: UNMOVED)', ('Num', 31, 48), []),
    ('R27 Exod 28:10 = [6, 1]  ("six of their names on the one stone, and the names of THE six remaining" — the article-numeral with no chain after it: UNMOVED)', ('Exod', 28, 10), [6, 1]),
    ('R28 Deut 19:9 = [3]  ("upon THESE THREE" — UNMOVED)', ('Deut', 19, 9), [3]),
    ('R29 Num 31:30 = [1]  ("one drawn out of THE fifty" — the ratio\'s fifty silent by the standing rule: UNMOVED, named and left)', ('Num', 31, 30), [1]),
    ('R30 Num 16:2 = [250]  ("fifty and two hundred" without the article: UNMOVED)', ('Num', 16, 2), [250]),
    ('R31 Num 16:17 = [250]  (the same: UNMOVED)', ('Num', 16, 17), [250]),
    ('R32 Exod 38:25 = [100, 1775]  (the accounts\' seat of the same 1,775 — R4 UNMOVED)', ('Exod', 38, 25), [100, 1775]),
    ('R33 Num 28:12 = [3, 1, 2, 1]  ("three tenths for the ONE bull, and two tenths for the ONE ram" — the definite one before "and two" closes: UNMOVED)', ('Num', 28, 12), [3, 1, 2, 1]),
    ('R34 Exod 26:21 = [40, 2, 1, 2, 1]  ("forty sockets... two sockets under the ONE board, and two sockets under the ONE board" — UNMOVED)', ('Exod', 26, 21), [40, 2, 1, 2, 1]),
    # ---- THE NUMBERS WALK 6b (2026-09-11; NUMBERS_WALK.md "Sitting 6b"): CHUKAT'S GAP — THE DUAL "TWICE" (20:11's pa'amayim: the consonants of
    #      "times", the patach under the pe — the Torah's four seats, nine in the Tanakh; the plural with the sheva stays a word); written to FAIL on the parser 5b left ----
    ('H1  Num 20:11 = [2]  ("and he struck the rock with his staff TWICE" — the dual of the noun of occurrences, told from 19:4\'s plural "seven TIMES" by the patach under the pe; was [])', ('Num', 20, 11), [2]),
    ('H2  Gen 27:36 = [2]  ("he has supplanted me these TWO TIMES" — the dual; was [])', ('Gen', 27, 36), [2]),
    ('H3  Gen 41:32 = [2]  ("the dream was repeated to Pharaoh TWICE" — was [])', ('Gen', 41, 32), [2]),
    ('H4  Gen 43:10 = [2]  ("we could have returned TWICE" — was [])', ('Gen', 43, 10), [2]),
    ('R35 Num 19:4 = [7]  ("seven TIMES" — the plural with the sheva stays a word: UNMOVED)', ('Num', 19, 4), [7]),
    ('R36 Lev 4:6 = [7]  ("seven times" — UNMOVED)', ('Lev', 4, 6), [7]),
    ('R37 Lev 16:14 = [7]  ("seven times" — UNMOVED)', ('Lev', 16, 14), [7]),
    ('R38 Exod 23:17 = [3]  ("three times in the year" — UNMOVED)', ('Exod', 23, 17), [3]),
    ('R39 Num 14:22 = [10]  ("these ten times" — UNMOVED)', ('Num', 14, 22), [10]),
    ('R40 Num 24:10 = [3]  ("these three times" — UNMOVED)', ('Num', 24, 10), [3]),
    ('R41 Deut 1:11 = [1000]  ("a thousand times" — UNMOVED)', ('Deut', 1, 11), [1000]),
    ('R42 Num 24:1 = []  ("as time upon time" — the singular, no numeral: UNMOVED)', ('Num', 24, 1), []),
    # ---- THE NUMBERS WALK 7b (2026-09-11; NUMBERS_WALK.md "Sitting 7b"): BALAK'S GAP — THE PLENE "THREE" (22:32's שָׁלוֹשׁ with the vav inside the
    #      word, the Torah's three seats; fifty-nine tokens in the Tanakh under any prefix), and THE CONSTRUCT "THOUSANDS OF" after a unit numeral
    #      (Exod 32:28's "about three thousands of men" read 3 since the parser's first day — found by the reading's plague-count cross-check);
    #      written to FAIL on the parser 6b left ----
    ('J1  Num 22:32 = [3]  ("why have you struck your she-ass these THREE times" — the plene spelling; 22:28 and 22:33 defective read 3 already; was [])', ('Num', 22, 32), [3]),
    ('J2  Deut 16:16 = [3]  ("THREE times in the year" plene beside Exod 23:17\'s defective; "the feast of WEEKS" with the qubuts stays a word — E6; was [])', ('Deut', 16, 16), [3]),
    ('J3  Deut 19:2 = [3]  ("THREE cities you shall separate" — plene; was [])', ('Deut', 19, 2), [3]),
    ('J4  Exod 32:28 = [3000]  ("about THREE THOUSANDS OF men" — the construct plural אַלְפֵי "thousands of" after the unit multiplies as the plural does; was [3])', ('Exod', 32, 28), [3000]),
    ('R44 Num 22:28 = [3]  ("these three times" defective — UNMOVED)', ('Num', 22, 28), [3]),
    ('R45 Num 22:33 = [3]  ("these three times" defective — UNMOVED)', ('Num', 22, 33), [3]),
    ('R46 Num 10:36 = []  ("the myriads of the thousands of Israel" — the construct "thousands of" with NO numeral before it is a noun: D11 UNMOVED)', ('Num', 10, 36), []),
    ('R47 Deut 33:17 = []  ("the ten thousands of Ephraim and the thousands of Manasseh" — the bare construct, no numeral: UNMOVED)', ('Deut', 33, 17), []),
    ('R48 Exod 12:37 = [600000]  ("about six hundred thousand" — the approximation prefix on a unit before the hundreds and the thousand: UNMOVED)', ('Exod', 12, 37), [600000]),
    ('R49 Num 1:46 = [603550]  ("six hundred thousand and three THOUSANDS" — the plural after the unit: UNMOVED)', ('Num', 1, 46), [603550]),
]
ORDS = [   # the ordinal reader must keep "second" and lose the construct
    ('O1  Num 6:10 ordinals = [8]  (the eighth day; "two of" no longer an ordinal)', ('Num', 6, 10), [8]),
    ('O2  Num 7:18 ordinals = [2]  (the second day — UNMOVED)', ('Num', 7, 18), [2]),
    ("O3  Exod 40:17 ordinals = [1]  (the first month; the feminine 'second' was never in the table — 1b's note at the marker; UNMOVED)", ('Exod', 40, 17), [1]),
    ('O4  Num 13:22 ordinals = []  (SHESHAI the Anakite — a tsere under the shin, a proper noun — read as "sixth": THE NUMBERS WALK 4b)', ('Num', 13, 22), []),
    ('O5  Exod 16:5 ordinals = [6]  (the SIXTH day — a hiriq and a dagesh: UNMOVED)', ('Exod', 16, 5), [6]),
    # ---- THE NUMBERS WALK 6b (2026-09-11): THE DEFINITE NUMERAL AFTER THE YEAR-CONSTRUCT IS AN ORDINAL YEAR — Num 33:38 "in the year of THE forty"
    #      = the fortieth year (Aaron's death-date read whole: year 40, month 5, day 1); written to FAIL on the ordinal reader 5b left ----
    ('H5  Num 33:38 ordinals = [40, 5]  ("in the FORTIETH year... in the fifth month" — the article-bearing numeral after "in the year of" read as the ordinal year; was [5])', ('Num', 33, 38), [40, 5]),
    ('O6  Exod 40:17 ordinals = [1]  ("in the first month in the second year" — the feminine "second" was never in the table: UNMOVED)', ('Exod', 40, 17), [1]),
    ('O7  Num 1:1 ordinals = [2]  ("on the first of the second month in the second year" — UNMOVED)', ('Num', 1, 1), [2]),
    # THE NUMBERS WALK 6b (2026-09-11): THREE MORE SEATS OF RULE (20) THE CORPUS-WIDE DIFF SURFACED (the design had typed "the Torah's one seat" without
    # running the census — the diff ran it): "the year of THE seven" and "the year of THE fifty" are the seventh and the fiftieth year — read right, typed
    # from the diff's own print as accepted rows
    ('O9  Deut 15:9 ordinals = [7]  ("the SEVENTH year, the year of release" — שְׁנַת הַשֶּׁבַע "the year of the seven": the release year read as an ordinal; was [])', ('Deut', 15, 9), [7]),
    ('O10 Lev 25:10 ordinals = [50]  ("you shall sanctify the FIFTIETH year" — שְׁנַת הַחֲמִשִּׁים "the year of the fifty": the jubilee\'s own year; was [])', ('Lev', 25, 10), [50]),
    ('O11 Lev 25:11 ordinals = [50]  ("a jubilee that FIFTIETH year shall be to you" — was [])', ('Lev', 25, 11), [50]),
]
CASES.append(('R43 Num 33:38 = [1]  (the day "on the first" — the numbers reader UNMOVED; the hand had typed this row into the ORDINALS list on the first FAIL run — it read [5], the ordinal reader\'s own answer — a probe typed into the wrong list, retyped here)', ('Num', 33, 38), [1]))

if __name__ == '__main__':
    ok = 0
    print('THE CENSUS GRAMMAR — the numeral parser\'s fire-probes')
    for name, (b, c, v), want in CASES:
        got = CS.ink_numbers(CS.verse_words(b, c, v))
        hit = got == want
        ok += hit
        print('  %s  %s   got %s' % ('PASS' if hit else 'FAIL', name, got))
    for name, (b, c, v), want in ORDS:
        got = CS.ink_ordinals(CS.verse_words(b, c, v))
        hit = got == want
        ok += hit
        print('  %s  %s   got %s' % ('PASS' if hit else 'FAIL', name, got))
    print('%d/%d probes' % (ok, len(CASES) + len(ORDS)))
    sys.exit(0 if ok == len(CASES) + len(ORDS) else 1)
