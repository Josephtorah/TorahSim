import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK 4b — THE PARSER TAUGHT (2026-09-10; NUMBERS_WALK.md "Sitting 4b"): the five rules into cold_run_sequence.py's INK block,
# each anchored on the 3b text (every anchor asserted once). (12) THE FRACTION BEFORE A MEASURE NOUN; (13) THE UNIT NOUN AS ONE (the tenth,
# the cubit by its points, the hin); (14) THE DEFINITE ONE; (15) THE THIRD-GENERATION HOMOGRAPH by the lamed's vowel and SHESHAI by the
# tsere; (16) THE TITHE VERB by the patach. The probes (census_probes.py F1-F33, O4) were written to FAIL first.
p = (_ROOT + '/World/step9/cold_run_sequence.py')
s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    assert s.count(a) == 1, ('anchor', a[:80], s.count(a))
    s = s.replace(a, b)

# ---- the units table: the definite one closes its phrase like a suffixed numeral ----
rep("UNITS.update({'יומים~': 2, 'אמתים~': 2, 'שני#': 2, 'שתי#': 2, 'שלשת#': 3, 'ארבעת#': 4, 'חמשת#': 5, 'ששת#': 6, 'שבעת#': 7, 'שמנת#': 8, 'תשעת#': 9, 'עשרת#': 10})",
    """UNITS.update({'יומים~': 2, 'אמתים~': 2, 'שני#': 2, 'שתי#': 2, 'שלשת#': 3, 'ארבעת#': 4, 'חמשת#': 5, 'ששת#': 6, 'שבעת#': 7, 'שמנת#': 8, 'תשעת#': 9, 'עשרת#': 10})
# THE NUMBERS WALK 4b (2026-09-10; NUMBERS_WALK.md "Sitting 4b" — the libation table's own grammar, measured on the whole Tanakh DB):
# (12) THE FRACTION BEFORE A MEASURE NOUN — the quarter (רֶבַע / רְבִעִית / רְבִיעִת / רְבִיעִית, six spellings, every one before הַהִין "the hin"),
#      the third (שְׁלִשִׁית / שְׁלִישִׁת), the tenth (עֲשִׂירִת / עֲשִׂירִית before הָאֵפָה "the ephah") and the half (חֲצִי / מַחֲצִית before the hin or
#      הַשֶּׁקֶל "the shekel") read as exact fractions when the NEXT word is a measure noun — emitted with a percent sign; before anything else
#      the same words stay words (the night, Exod 12:29; the blood; the tribe; Reba the king, Num 31:8; the fourth part of Israel, 23:10).
# (13) THE UNIT NOUN AS ONE — a singular measure noun standing WITHOUT a numeral counts one: the tenth עִשָּׂרוֹן (Num 15:4, Exod 29:40; doubled
#      "a tenth, a tenth" the distributive — one), the cubit אַמָּה / וְאַמָּה told BY ITS POINTS (a patach under the alef and a dagesh in the mem:
#      not the maidservant אָמָה of Exod 21:32, not "her mother" אִמָּהּ of Deut 21:13 — "a cubit and a half" = 1.5, 3b's residue), the hin הִין
#      (Exod 30:24); emitted with an at sign; after a numeral the noun is the number's unit and adds nothing ("fifty cubits"); before its own
#      numeral adjective it stays silent ("a tenth, ONE" — Num 29:4; Lev 14:21). The other measure nouns (the omer, the ephah, the homer, the
#      bath, the gerah, the shekel) are NAMED AND LEFT with their homographs — the sheaf, "where", the donkey, the daughter, the cud.
# (14) THE DEFINITE ONE — הָאֶחָד / הָאַחַת, with or without the vav (96 Torah tokens: "for the ONE lamb", "the ONE board", "the one... and the
#      other"), counts ONE and closes its phrase (Num 28:21 "for the one lamb, for the seven lambs" = [1, 7]) — emitted as the numeral with the
#      hash; the answer sheet reads the token too (Menachot 91b:9, 91b:20).
# (15) THE THIRD-GENERATION HOMOGRAPH — שִׁלֵּשִׁים "the third generation" (Exod 20:5, 34:7, Num 14:18, Deut 5:9, Gen 50:23 — a tsere under the
#      lamed) and וּשְׁלִשִׁים "third stories" (Gen 6:16 — a hiriq) had read as THIRTY: only a holam under the lamed is thirty; and SHESHAI the
#      Anakite (שֵׁשַׁי, Num 13:22 — a tsere under the shin) had read as the ordinal "sixth" (שִׁשִּׁי, a hiriq and a dagesh).
# (16) THE TITHE VERB — עַשֵּׂר "tithe" (Gen 28:22, Deut 14:22, 26:12 — a patach under the ayin) had read as TEN (עֶשֶׂר, a segol); the tenth-day
#      noun עָשֹׂר (Exod 12:3, a qamats) stays ten.
from fractions import Fraction   # inside the INK block: the stitcher and the diff exec this block into their own namespace
UNITS.update({'אחד#': 1, 'אחת#': 1})
FRACTIONS = {'רבע': Fraction(1, 4), 'רבעית': Fraction(1, 4), 'רביעת': Fraction(1, 4), 'רביעית': Fraction(1, 4), 'שלשית': Fraction(1, 3), 'שלישת': Fraction(1, 3),
             'שלישית': Fraction(1, 3), 'עשירת': Fraction(1, 10), 'עשירית': Fraction(1, 10), 'חצי': Fraction(1, 2), 'מחצית': Fraction(1, 2)}
MEASURES = {'ההין', 'האפה', 'האיפה', 'השקל', 'הקב', 'החמר'}
UNIT_NOUNS = {'עשרון': 'tenth', 'עשרן': 'tenth', 'אמה': 'cubit', 'הין': 'hin'}""")

# ---- verse_words: the new marks, before out.append(bare) ----
rep("""            if ok:
                bare = (m.group(1) or '') + stem + '#'
        out.append(bare)
    return out""",
    """            if ok:
                bare = (m.group(1) or '') + stem + '#'
        # ---- THE NUMBERS WALK 4b (2026-09-10): rules (12)-(16) ----
        nb1 = re.sub(r'[֑-ׇ/]', '', raws[i + 1]) if i + 1 < len(raws) else ''
        core = bare
        for pre in ('ו', 'ב', 'ל', 'כ'):
            if bare.startswith(pre) and bare[len(pre):] in FRACTIONS:
                core = bare[len(pre):]; break
        if core in FRACTIONS and nb1 in MEASURES and not bare.endswith('*'):      # (12) the fraction before a measure noun
            bare = bare + '%'
        elif bare in ('עשרון', 'ועשרון', 'עשרן', 'ועשרן', 'אמה', 'ואמה', 'הין'):    # (13) the unit noun as one — the cubit by its points
            stem_ok = True
            if bare.endswith('אמה'):
                st = pw[pw.rfind('א'):]
                stem_ok = bool(re.match(r'^א\\u05B7מ\\u05BC', st)) and not st.endswith('\\u05BC')
            if stem_ok:
                bare = bare + '@'
        elif bare in ('האחד', 'האחת', 'והאחד', 'והאחת'):                              # (14) the definite one
            bare = bare[:-3] + bare[-3:] + '#'
        elif bare.lstrip('ובלכה') == 'שלשים' and not bare.endswith('*'):             # (15) thirty only with a holam under the lamed
            st = pw[pw.rfind('ל'):]
            if '\\u05B9' not in st[:4]:
                bare = bare + '*'
        elif bare == 'ששי' and '\\u05B5' in pw[:pw.find('ש') + 4]:                   # (15) Sheshai — a tsere under the shin, not the ordinal
            bare = bare + '*'
        elif bare.lstrip('ובלכמה') == 'עשר' and bare.endswith('עשר') and not bare.endswith('*'):   # (16) the tithe verb — a patach under the ayin
            st = pw[pw.rfind('ע'):]
            if '\\u05B7' in st[:3]:
                bare = bare + '*'
        out.append(bare)
    return out""")

# ---- ink_numbers: the marks read ----
rep("""        cut = w.endswith('|'); w = w.rstrip('|')                  # THE NUMBERS WALK 2b: the bar — a disjunctive on 'one' before a bare numeral (M-26)
        b = _bare(w)""",
    """        cut = w.endswith('|'); w = w.rstrip('|')                  # THE NUMBERS WALK 2b: the bar — a disjunctive on 'one' before a bare numeral (M-26)
        # ---- THE NUMBERS WALK 4b (2026-09-10): (12) the fraction of a measure, (13) the unit noun as one ----
        if w.endswith('%'):
            core = w[:-1]
            if core == 'וחצי' and seen and len(add) > k:              # (7) keeps precedence: "a cubit and a half OF THE cubit" continues the numeral
                add.append(0.5); prev_unit = 0; last = None
                continue
            for pre in ('ו', 'ב', 'ל', 'כ'):
                if core.startswith(pre) and core[len(pre):] in FRACTIONS:
                    core = core[len(pre):]; break
            if seen:
                out.append(sum(add))
            out.append(FRACTIONS[core])
            add, k, seen, prev_unit, last, after_year = [], 0, False, 0, None, False
            continue
        if w.endswith('@'):
            after_year = False
            if seen:                                                  # after a numeral the noun is the number's unit: it closes, adds nothing
                out.append(sum(add)); add, k, seen, prev_unit, last = [], 0, False, 0, None
                continue
            look = [x.rstrip('|#') for x in words[i + 1:i + 3]]
            if any(_bare(x) in ('אחד', 'אחת') for x in look):         # "a tenth, ONE" — the numeral adjective after the noun counts it
                add, k, seen, prev_unit, last = [], 0, False, 0, None
                continue
            add.append(1); seen = True; prev_unit = 0; last = w        # the unit noun as one; the phrase stays open for "and a half"
            continue
        b = _bare(w)""")

rep("""        if b is not None and w.startswith('ה') and not w.startswith('וה'):
            # THE ARTICLE ON A NUMERAL counts only at the head of a chain joined by 'and the' (Num 3:46 השלשה והשבעים והמאתים);""",
    """        if b in ('אחד#', 'אחת#'):                                  # (14) 4b: THE DEFINITE ONE — the article rules below do not apply; it counts one and closes
            pass
        elif b is not None and w.startswith('ה') and not w.startswith('וה'):
            # THE ARTICLE ON A NUMERAL counts only at the head of a chain joined by 'and the' (Num 3:46 השלשה והשבעים והמאתים);""")
rep("""        if b is not None and w.startswith('וה'):
            # 'and the N' counts only INSIDE a chain (after a numeral word): 'and the other' (Gen 42:13, Lev 14:22 והאחד) is no number""",
    """        if b is not None and w.startswith('וה') and b not in ('אחד#', 'אחת#'):   # 4b: "and the one" (Lev 14:22) now counts — the definite one
            # 'and the N' counts only INSIDE a chain (after a numeral word): 'and the other' (Gen 42:13, Lev 14:22 והאחד) is no number""")
open(p, 'w', encoding='utf-8').write(s)
print('patched', p)
