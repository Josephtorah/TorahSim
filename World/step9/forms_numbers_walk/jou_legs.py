# THE LEG DIAGNOSTIC (sitting 6's lesson): exec the ink module's non-assert statements, then print each failing assert's legs one by one
import ast, sys
path = sys.argv[1]; src = open(path, encoding='utf-8').read(); tree = ast.parse(src); ns = {'__name__': 'jou_ink', '__file__': path}
for node in tree.body:
    if isinstance(node, ast.Assert): continue
    exec(compile(ast.Module([node], []), path, 'exec'), ns)
LEGS = [
 "[(p, r) for p, rows in enumerate(sif_he, 1) for r, row in enumerate(rows, 1) if 'ביד רמה' in clean(row)]", "heads[112]", "Hb(112, 2)[:60]",
 "AARON_DATE", "N('Num', 20, 28)", "O('Deut', 1, 3)", "N('Deut', 1, 3)",
 "len(HEADS)", "[h for h in HEADS if h.startswith('Num 3')]", "'Gen 2:4' in HEADS",
 "[(v, arm(33, v).count('מימרא')) for v in range(1, 57) if 'מימרא' in arm(33, v)]", "aramaic(33, 2)[5:8]", "aramaic(33, 38)[5:8]", "aramaic(33, 1)[-3:]", "aramaic(33, 1)[6]", "aramaic(33, 1)",
 "phrase(['ובאלהיהם', 'עשה', 'יהוה', 'שפטים'], None)", "phrase(['אעשה', 'שפטים'], None)", "phrase(['עשה', 'שפטים'], None)", "words('Exod', 12, 12)[-6:]",
 "words('Num', 33, 7)", "words('Exod', 14, 2)[3:9]",
 "NP('רפידם', 'ברפידם', 'מרפידם', 'ברפידים', 'מרפידים')", "U('רפידם', 'ברפידם', 'מרפידם')", "words('Exod', 17, 1)[11]", "words('Exod', 19, 2)[1]",
 "words('Num', 33, 36)", "phrase(['הוא', 'קדש'], None)", "words('Gen', 14, 7)[3:6]", "words('Gen', 14, 7)",
 "onk_seats('רקם')", "words('Num', 31, 8)[6]", "words('Num', 31, 8)", "aramaic(33, 36)[-2:]", "aramaic(33, 37)[1]", "onk_seats('הור טורא')",
 "words('Num', 33, 39)", "words('Exod', 7, 7)[4:9]", "words('Deut', 32, 50)[10:15]", "words('Deut', 32, 50)",
 "words('Num', 20, 28)", "aramaic(33, 38)[11:13]", "aramaic(33, 38)",
 "phrase(['והורשתם', 'את', 'כל', 'ישבי', 'הארץ'], None)", "U('והורשתם')", "phrase(['ישבי', 'הארץ'])", "words('Exod', 23, 31)[-6:]", "words('Exod', 23, 31)",
 "U('משכית', 'משכיתם')", "words('Lev', 26, 1)[9:11]", "phrase(['צלמי', 'מסכתם'], None)", "U('צלמי')",
 "words('Lev', 26, 30)[:3]", "U('תשמידו')", "U('במתם')", "onk_seats('בית סגד')", "aramaic(33, 52)[10:12]", "aramaic(33, 52)[0]", "aramaic(33, 52)",
 "words('Exod', 34, 13)", "words('Deut', 7, 5)[4:]", "words('Deut', 7, 5)",
]
for e in LEGS:
    try: print(f'{e}  =>  {eval(e, ns)!r}')
    except Exception as ex: print(f'{e}  =>  ERROR {ex!r}')
