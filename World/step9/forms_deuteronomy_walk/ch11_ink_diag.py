# the ten statements that fell on the first typed pass — every part printed (ch10_ink_diag.py's form)
import ast, sys, io, contextlib, re
path = sys.argv[1]; src = open(path, encoding='utf-8').read(); tree = ast.parse(src); ns = {'__name__': 'deu_ink', '__file__': path}
for node in tree.body:
    try: exec(compile(ast.Module([node], []), path, 'exec'), ns)
    except Exception as e: pass
g = ns
HB0, E, Hb, he_cites, VC, P, U, LEMT, words, onk_seats, aramaic = g['HB0'], g['E'], g['Hb'], g['he_cites'], g['VC'], g['P'], g['U'], g['LEMT'], g['words'], g['onk_seats'], g['aramaic']
SH, D11 = g['SH'], g['D11']
print('169:', HB0(45, 1)[:40], '|', he_cites(Hb(45, 1)), '|', '(Dt.11:18)' in E(45, 1), 'סם חיים' in HB0(45, 1))
print('189:', repr(HB0(37, 3)[:40]), '|', repr(E(37, 3)[:30]), '|', E(37, 4)[:20], '|', E(39, 6).startswith(E(37, 3).strip()[:120]), '|', repr(E(37, 3).strip()[:120]), '|', repr(E(39, 6)[:130]))
print('222:', VC[5], VC[10], VC[11], VC[12], sum(VC.values()), len(VC))
print('296:', SH(D11(4), ('Deut', 34, 6)), SH(D11(4), ('Josh', 24, 6)), max((SH(D11(4), ('Exod', 14, v)), v) for v in range(1, 32)), max((SH(D11(4), ('Exod', 15, v)), v) for v in range(1, 22)))
print('315:', P('ידו', 'החזקה', 'וזרעו', 'הנטויה'), P('ביד', 'חזקה', 'ובזרע', 'נטויה'), [s for s in U('גדלו') if s.startswith('Deut')], P('אשר', 'לא', 'ידעו', 'ואשר', 'לא', 'ראו'))
print('351:', P('והוריש', 'יהוה', 'את', 'כל', 'הגוים', 'האלה', 'מלפניכם'), [(s, x, m) for s, x, m in LEMT('3423', books=('Deut',)) if m and 'Vh' in m], P('גוים', 'גדלים', 'ועצמים', 'מכם'), P('גוים', 'גדלים', 'ועצמים', 'ממך'), P('רבים', 'ועצומים', 'ממך'))
print('358:', [(s, x) for s, x, m in LEMT('7200', books=('Deut',)) if m == 'HVqv2ms'], P('אנכי', 'נתן', 'לפניכם', 'היום'))
print('377:', onk_seats('תפלין'), aramaic(6, 8), aramaic(11, 19), aramaic(6, 7))
SPEC = g['OVERRIDE_REF_SPEC']; sidx = g['sidx']
keys = [f'Deut.11.{v}:{sidx(11, v, tok, nth)}' for v, tok, new, nth in SPEC]
from collections import Counter
print('423:', len(SPEC), len(set(keys)), [k for k, n in Counter(keys).items() if n > 1], len(g['OVERRIDE_GLOSS']), [(v, tok, nth) for (v, tok, new, nth), k in zip(SPEC, keys) if Counter(keys)[k] > 1])
print('426:', len(g['ALREADY']))
