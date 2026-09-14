# THE LEG DIAGNOSTIC (sitting 6's lesson): exec the ink module's non-assert statements, then print each failing assert's legs one by one
import ast, sys
path = sys.argv[1]; src = open(path, encoding='utf-8').read(); tree = ast.parse(src); ns = {'__name__': 'midian_ink', '__file__': path}
for node in tree.body:
    if isinstance(node, ast.Assert): continue
    exec(compile(ast.Module([node], []), path, 'exec'), ns)
LEGS = [
 "morphs('Num', 31, 28)[11:13]", "words('Num', 31, 28)[10:13]", "words('Num', 31, 30)[4:8]", "accents(byraw[('Num', 31, 28)][10])",
 "phrase(['ויקצף', 'משה'], None)", "U('ויקצף', books=T)", "words('Exod', 16, 20)[-3:]", "words('Lev', 10, 16)[-6:-3]",
 "[x for v in range(1, 43) for x, _ in by[('Num', 32, v)] if re.match(r'^(ו|נ|ת)?חל(ו|)צ', x)]", "U('חלציך')", "words('Lev', 14, 40)[1]",
 "phrase(['מלכי', 'מדין'], None)", "phrase(['חמשת', 'מלכי', 'מדין'], None)", "words('Judg', 8, 12)[7:12]",
 "words('Josh', 13, 21)[16:31]", "words('Josh', 13, 22)",
 "phrase(['הן', 'הנה'], None)", "phrase(['בדבר', 'בלעם'], None)", "aramaic(31, 16)[4:7]", "phrase(['דבר', 'פעור'], None)", "phrase(['מעל', 'ביהוה'], None)",
 "words('Judg', 21, 10)[6:9]", "words('Judg', 21, 11)[4:12]", "words('Judg', 21, 12)[5:11]", "N('Judg', 21, 12)",
 "seats_in(lambda x, m: x == 'שבעת')", "morphs('Num', 31, 43)[9]", "phrase(['ביום', 'השלישי', 'וביום', 'השביעי'], None)",
 "U('בדיל', books=T)", "U('הבדיל', books=T)", "morphs('Deut', 10, 8)[0]", "U('עפרת', 'העפרת', 'כעופרת', 'ועופרת', 'עופרת', books=T)", "words('Num', 31, 22)",
 "U('וחצית')", "U('המחצה')", "U('מחצת', 'ממחצת', 'וממחצת')", "U('מחצית')", "U('וממחצית', 'ממחציתם')",
 "words('Num', 31, 28)[13:]", "words('Num', 31, 30)[8:18]", "phrase(['מכל', 'הבהמה'], None)",
 "U('אצעדה', 'ואצעדה')", "U('צמיד', 'וצמיד')", "U('צמיד', 'וצמיד', 'צמידים', 'וצמידים')", "words('Num', 19, 15)[:6]", "len(U('טבעת', 'וטבעת'))", "U('עגיל')", "U('עגיל', 'ועגיל', 'עגילים', 'ועגילים')", "U('כומז', 'וכומז')",
 "aramaic(31, 50)[8:13]", "aramaic(31, 52)[13]", "aramaic(31, 54)[13:16]", "aramaic(31, 49)[11:15]", "sg(31, 54, 'מועד')", "sg(31, 8, 'בחרב')",
 "words('Esth', 2, 22)[-5:]", "words('Num', 19, 14)[:6]", "words('Ps', 106, 30)",
]
for e in LEGS:
    try: print(f'{e}  =>  {eval(e, ns)!r}')
    except Exception as ex: print(f'{e}  =>  ERROR {ex!r}')
