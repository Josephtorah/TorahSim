# the ten forms retyped from the diag print (ch11_ink_diag.py): the Proverbs range citation invisible to the regex at 45:1 (chapter 8's lesson), the colon inside
# 37:3's opening, Deuteronomy 12's thirty-one verses, Exodus 14:31's three shared tokens, "Your greatness" at 3:24 (a second suffix), the hiphil's two infinitives
# at 4:38 and 7:17, the sorted order of "I set before you today", the Aramaic tail's index, the by-gloss count sixty-four, the ALREADY thirty-six
import os, sys
SP = os.path.dirname(os.path.abspath(__file__))
p = f'{SP}/ch11_ink_body.py'; s = open(p, encoding='utf-8').read()
REPL = [
 ("he_cites(Hb(45, 1)) == [('בראשית', 4, 7), ('משלי', 25, 21), ('בראשית', 8, 21)]", "he_cites(Hb(45, 1)) == [('בראשית', 4, 7), ('בראשית', 8, 21)] and '(משלי כה כא-כב)' in Hb(45, 1)"),
 ("HB0(37, 3).startswith('ואם תאמר לא מי שבנה את זו')", "HB0(37, 3).startswith('ואם תאמר: לא מי שבנה את זו')"),
 ("assert VC[5] == 33 and VC[10] == 22 and VC[11] == 32 and VC[12] == 32 and", "assert VC[5] == 33 and VC[10] == 22 and VC[11] == 32 and VC[12] == 31 and"),
 ("max(SH(D11(4), ('Exod', 14, v)) for v in range(1, 32)) == 2 and max(SH(D11(4), ('Exod', 15, v)) for v in range(1, 22)) == 2   # THE SEA TOLD IN NEW WORDS: no verse of Exodus 14-15 shares more than two tokens",
  "max((SH(D11(4), ('Exod', 14, v)), v) for v in range(1, 32)) == (3, 31) and max(SH(D11(4), ('Exod', 15, v)) for v in range(1, 22)) == 2   # THE SEA TOLD IN NEW WORDS: no verse of Exodus 14-15 shares more than three tokens (14:31's 'which the LORD did against Egypt' the three)"),
 ("[s for s in U('גדלו') if s.startswith('Deut')] == ['Deut 11:2', 'Deut 3:24', 'Deut 5:24']", "[s for s in U('גדלו') if s.startswith('Deut')] == ['Deut 11:2', 'Deut 5:24'] and 'Deut 3:24' in U('גדלך')"),
 ("[(s, x) for s, x, m in LEMT('3423', books=('Deut',)) if m and 'Vh' in m] == [('Deut 9:3', 'והורשתם'), ('Deut 9:4', 'מורישם'), ('Deut 9:5', 'מורישם'), ('Deut 11:23', 'והוריש'), ('Deut 18:12', 'מוריש')]",
  "[(s, x) for s, x, m in LEMT('3423', books=('Deut',)) if m and 'Vh' in m] == [('Deut 4:38', 'להוריש'), ('Deut 7:17', 'להורישם'), ('Deut 9:3', 'והורשתם'), ('Deut 9:4', 'מורישם'), ('Deut 9:5', 'מורישם'), ('Deut 11:23', 'והוריש'), ('Deut 18:12', 'מוריש')]"),
 ("P('אנכי', 'נתן', 'לפניכם', 'היום') == ['Deut 11:32', 'Deut 4:8', 'Deut 11:26']", "P('אנכי', 'נתן', 'לפניכם', 'היום') == ['Deut 11:26', 'Deut 11:32', 'Deut 4:8']"),
 ("aramaic(11, 19)[4:] == aramaic(6, 7)[2:] ==", "aramaic(11, 19)[5:] == aramaic(6, 7)[3:] =="),
 ("len(OVERRIDE_GLOSS) == 63 and len({k for k, _ in OVERRIDE_GLOSS}) == 63", "len(OVERRIDE_GLOSS) == 64 and len({k for k, _ in OVERRIDE_GLOSS}) == 64"),
 ("the rewrite covers the whole store (SIXTY-THREE)", "the rewrite covers the whole store (SIXTY-FOUR)"),
 ("assert len(ALREADY) == 37", "assert len(ALREADY) == 36"),
 ("the seat named (ONE HUNDRED AND ELEVEN)", "the seat named (ONE HUNDRED AND FIFTY-EIGHT)"),
]
for old, new in REPL:
    assert s.count(old) == 1, ('ABSENT', old[:80]); s = s.replace(old, new)
open(p, 'w', encoding='utf-8').write(s); print('patched', len(REPL))
