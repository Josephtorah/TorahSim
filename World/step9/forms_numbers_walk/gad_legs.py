# THE LEG DIAGNOSTIC (sitting 6's lesson): exec the ink module's non-assert statements, then print each failing assert's legs one by one
import ast, sys
path = sys.argv[1]; src = open(path, encoding='utf-8').read(); tree = ast.parse(src); ns = {'__name__': 'gad_ink', '__file__': path}
for node in tree.body:
    if isinstance(node, ast.Assert): continue
    exec(compile(ast.Module([node], []), path, 'exec'), ns)
LEGS = [
 "sorted({f'{b} {c}:{v} {x}' for (b, c, v), ws in by.items() if b in T for x, m in ws if m and 'V' in m and ('ניא' in x or 'נוא' in x)})",
 "FILL",
 "U('וינעם')", "morphs('Num', 32, 13)[4]", "[f'{b} {c}:{v} {x}' for (b, c, v), ws in by.items() if b in T for x, m in ws if m and m.startswith('HVh') and x in ('וינעם', 'הניעה', 'יניעו', 'הניעמו', 'יניעון', 'יניע')]", "words('Num', 14, 33)[:6]", "aramaic(32, 13)[4]",
 "morphs('Josh', 1, 14)[words('Josh', 1, 14).index('חמשים')]", "morphs('Num', 4, 3)[words('Num', 4, 3).index('חמשים')]", "byp[('Josh', 1, 14)][words('Josh', 1, 14).index('חמשים')]", "byp[('Num', 4, 3)][words('Num', 4, 3).index('חמשים')]",
 "phrase(['הנה', 'חטאתם', 'ליהוה'], None)", "phrase(['חטאתם', 'ליהוה'], None)", "phrase(['חטאתכם', 'אשר', 'תמצא', 'אתכם'], None)", "phrase(['מצא', 'את', 'עון'], None)", "words('Gen', 44, 16)[9:13]", "aramaic(32, 23)[9:12]",
 "words('Josh', 13, 17)", "words('Josh', 13, 19)[:2]", "words('Josh', 13, 20)[:2]", "words('Josh', 13, 25)[:5]", "words('Josh', 13, 25)[12:14]", "words('Josh', 13, 26)[0]", "words('Josh', 13, 27)[1:5]",
 "words('Jer', 48, 1)[8:10]", "words('Jer', 48, 1)[13]", "words('Jer', 48, 18)[6]", "words('Jer', 48, 19)[6]", "words('Jer', 48, 22)", "words('Jer', 48, 23)[:2]", "words('Jer', 48, 23)[-2:]", "words('Jer', 48, 32)[1]", "words('Jer', 48, 32)[5]", "words('Jer', 48, 34)[1:4]",
 "words('Judg', 8, 11)[6:8]", "U('יגבהה', 'ויגבהה')", "U('נבח')", "U('לנבח')", "U('קנת')",
 "words('Num', 26, 29)[5:9]", "words('Josh', 17, 1)[7:12]", "words('Josh', 17, 1)[15:18]", "words('Deut', 3, 15)",
 "words('Deut', 33, 21)[:8]", "words('Deut', 34, 1)[4:8]", "words('Deut', 34, 1)[18:21]", "words('Ps', 60, 9)[:4]", "words('1Chr', 5, 26)[12:17]",
]
for e in LEGS:
    try: print(f'{e}  =>  {eval(e, ns)!r}')
    except Exception as ex: print(f'{e}  =>  ERROR {ex!r}')
