import ast, sys, io, contextlib
path = sys.argv[1]; src = open(path, encoding='utf-8').read(); tree = ast.parse(src); ns = {'__name__': 'deu_ink', '__file__': path}
for node in tree.body:
    try: exec(compile(ast.Module([node], []), path, 'exec'), ns)
    except Exception as e: pass
g = ns
E, HB0, P, U, W9, SHN, SHARED, LEMT, T, by = g['E'], g['HB0'], g['P'], g['U'], g['W9'], g['SHN'], g['SHARED'], g['LEMT'], g['T'], g['by']
D9 = lambda v: ('Deut', 9, v)
print('25:4 HE parts:', [(k, k in HB0(25, 4)) for k in ('(דברים ט א)', 'לשון הבאי', 'רבן שמעון בן גמליאל', '(בראשית כו ד)')], [(k, k in E(25, 4)) for k in ('hyperbole', '(Dt.9:1)', '(Gn.26:4)')])
print('25:4 HE0:', HB0(25, 4)[:200])
print('27:2 HE parts:', [(k, k in HB0(27, 2)) for k in ('קל וחומר', 'הרף ממני ואשמידם', 'תפוס')], [(k, k in E(27, 2)) for k in ('(Dt.9:14)', 'logic', 'grab')])
print('27:2 HE0:', HB0(27, 2)[:260])
NAME = ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')
print('the Name per verse:', {v: sum(1 for x in W9(v) if x in NAME) for v in range(1, 30) if any(x in NAME for x in W9(v))}, 'total', sum(1 for v in range(1, 30) for x in W9(v) if x in NAME))
print('SHN 319:', SHN(D9(17), ('Exod', 32, 19)), SHN(D9(18), ('Exod', 34, 28)), SHN(D9(19), ('Deut', 10, 10)), SHN(D9(19), ('Exod', 32, 14)), SHN(D9(20), ('Exod', 32, 21)), SHN(D9(20), ('Exod', 32, 35)))
print('SHN 321:', SHN(D9(26), ('1Kgs', 8, 51)), SHN(D9(26), ('Exod', 32, 11)), SHN(D9(27), ('Exod', 32, 13)), SHARED(D9(27), ('Exod', 32, 13)), SHN(D9(28), ('Num', 14, 16)), SHN(D9(28), ('Exod', 32, 12)), SHN(D9(29), ('1Kgs', 8, 51)))
print('327:', P('ערים', 'גדלת', 'ובצרת', 'בשמים'), P('עם', 'גדול', 'ורם'), len(U('ענקים', 'ענק', 'הענק', 'הענקים', 'ענקי', 'וענקים')), P('מי', 'יתיצב', 'לפני'))
print('328:', P('אש', 'אכלה'), P('העבר', 'לפניך'), [(s, x) for s, x, _ in LEMT('3665', books=('Deut',))])
print('332:', [(s, x) for s, x, _ in LEMT('7564', books=T)], P('ובישר', 'לבבך'), P('ישר', 'לבב'), P('בישר', 'לבב'))
print('365:', U('תבערה', 'ובתבערה', 'בתבערה'), U('מסה', 'ובמסה', 'במסה'), P('קברת', 'התאוה') + P('ובקברת', 'התאוה') + P('מקברת', 'התאוה') + P('בקברת', 'התאוה'), P('קברות', 'התאוה'), P('מקברות', 'התאוה'))
print('367:', P('ותמרו', 'את', 'פי'), P('מריתם', 'פי'), P('מריתם', 'את', 'פי'), P('פי', 'יהוה', books=('Deut',)), P('ולא', 'האמנתם', 'לו'), P('אינכם', 'מאמינם'), P('ולא', 'שמעתם', 'בקלו'))
print('376:', P('והם', 'עמך', 'ונחלתך'), P('בכחך', 'הגדל', 'ובזרעך', 'הנטויה'), P('בכח', 'גדול'), P('בכחו', 'הגדל'), P('בכחך', 'הגדל'), P('בכחך', 'הגדול'), [(s, x) for s, x, _ in LEMT('2220', books=('Deut',))][:4])
