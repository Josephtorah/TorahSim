# the five statements that fell on the first typed pass — every part printed (ch11_ink_diag.py's form)
import ast, sys, io, contextlib, re
path = sys.argv[1]; src = open(path, encoding='utf-8').read(); tree = ast.parse(src); ns = {'__name__': 'deu_ink', '__file__': path}
for node in tree.body:
    try: exec(compile(ast.Module([node], []), path, 'exec'), ns)
    except Exception as e: pass
g = ns
HB0, E, Hb, he_cites, SG, sidx = g['HB0'], g['E'], g['Hb'], g['he_cites'], g['SG'], g['sidx']
print('194:', repr(E(179, 2)[:400]), '|', he_cites(Hb(179, 2)), '|', 'וישבת בארצם' in HB0(179, 2), '|', repr(HB0(179, 2)[:120]))
print('195:', he_cites(Hb(138, 1)), '|', '(Dt.12:7' in E(138, 1), '|', 'נאמרה כאן שמחה' in HB0(138, 1), '|', repr(HB0(138, 1)[:80]), '|', repr(E(138, 1)[:200]))
print('257:', [(v, i, hp, gl) for (c, v), L in sorted(SG.items()) for i, hp, gl in L if '?' in gl])
from collections import Counter
print('384:', Counter(k for k, _ in g['OVERRIDE_GLOSS']).most_common(2), len(g['OVERRIDE_GLOSS']))
