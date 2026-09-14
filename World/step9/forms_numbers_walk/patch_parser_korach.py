#!/usr/bin/env python3
# THE NUMBERS WALK 5b — THE PARSER TAUGHT (2026-09-10; NUMBERS_WALK.md "Sitting 5b"): the rules into cold_run_sequence.py's INK block, each
# anchored on the 4b text (every anchor asserted once). (17) THE DEFINITE NUMERAL AT THE HEAD OF A COMPOUND — an article-bearing numeral
# followed by plain "and" + a bare numeral opens the chain (Num 16:35, Exod 38:28's head); (17b) the article on the hundreds-word after a
# unit multiplies (Exod 38:28 "seven THE hundreds"); (17c) the article-bearing PLURAL thousands / hundreds with no unit before it is a noun
# (Num 31:54 "the captains of the thousands and of the hundreds"); (18) THE DEFINITE ONE joins a following "and N" only under a CONJUNCTIVE
# accent (Exod 12:18's darga) — a disjunctive closes it (Exod 26:5, 36:12 a segolta; 25:32, 37:18 a zaqef). The probes (census_probes.py
# G1-G7) were written to FAIL first.
p = '<repo-old>/World/step9/cold_run_sequence.py'
s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    assert s.count(a) == 1, ('anchor', a[:80], s.count(a))
    s = s.replace(a, b)

# ---- (18) verse_words: the definite one's join gated by the accent ----
rep("""        elif bare in ('האחד', 'האחת', 'והאחד', 'והאחת'):                              # (14) the definite one
            if nb1.startswith('ו') and not nb1.startswith('וה') and nb1[1:] in UNITS:   # "the ONE and twentieth day" (Exod 12:18) — a chain joined by the conjunction: the article dropped, the numeral joins
                bare = bare[-3:]""",
    """        elif bare in ('האחד', 'האחת', 'והאחד', 'והאחת'):                              # (14) the definite one
            # THE NUMBERS WALK 5b (2026-09-10; NUMBERS_WALK.md "Sitting 5b"): (18) THE DEFINITE ONE'S JOIN IS GATED BY THE ACCENT — "the ONE and
            # twentieth day" (Exod 12:18) joins under a darga (conjunctive); "in the ONE curtain, and fifty loops" (Exod 26:5, 36:12 — a segolta)
            # and "from its ONE side, and three branches" (25:32, 37:18 — a zaqef) CLOSE: M-26's read extended to the definite one (the 4b diff
            # had accepted [50, 51] and [6, 3, 4])
            if nb1.startswith('ו') and not nb1.startswith('וה') and nb1[1:] in UNITS and not any(c in _DISJ for c in w):   # the chain joined by the conjunction under a conjunctive accent: the article dropped, the numeral joins
                bare = bare[-3:]""")

# ---- (17), (17b), (17c) ink_numbers: the article rule ----
rep("""            if not (i + 1 < len(words) and words[i + 1].startswith('וה') and _bare(words[i + 1]) is not None):
                b = None""",
    """            # THE NUMBERS WALK 5b (2026-09-10): (17) THE DEFINITE NUMERAL AT THE HEAD OF A COMPOUND — the article-bearing numeral before plain 'and'
            # + a bare numeral ALSO opens the chain: Num 16:35 החמשים ומאתים ('THE fifty and two hundred' = 250, read [200] since 1b), Exod
            # 38:28 האלף ושבע המאות ('THE thousand and seven THE hundreds...' = 1,775 — 38:25's own number, read [7, 75])
            nxt = words[i + 1].rstrip('|#') if i + 1 < len(words) else ''
            if not ((nxt.startswith('וה') and _bare(nxt) is not None) or (nxt.startswith('ו') and not nxt.startswith('וה') and _bare(nxt) is not None)):
                b = None""")
rep("""        if b is not None and b == 'אלפים' and len(add) == k and not w.startswith('ו'):""",
    """        if b in ('אלפים', 'מאות') and (w.startswith('ה') or w.startswith('וה')) and not prev_unit:
            # THE NUMBERS WALK 5b (2026-09-10): (17c) THE ARTICLE-BEARING PLURAL UNIT WORD IS A NOUN unless a unit numeral precedes it — 'the captains
            # of THE THOUSANDS and of THE HUNDREDS' (Num 31:54 — read [2100] by the 'and the' chain since 1b; 31:14, 31:48 the same phrase) against
            # (17b) 'seven THE hundreds' (Exod 38:28 — the article on the hundreds-word after a unit MULTIPLIES, the existing hundreds rule)
            b = None
        if b is not None and b == 'אלפים' and len(add) == k and not w.startswith('ו'):""")
open(p, 'w', encoding='utf-8').write(s)
print('patched', p)
