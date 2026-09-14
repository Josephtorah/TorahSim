# THE LEG DIAGNOSTIC (sitting 6's lesson): exec the ink module's non-assert statements, then print each failing assert's legs one by one
import ast, sys
path = sys.argv[1]; src = open(path, encoding='utf-8').read(); tree = ast.parse(src); ns = {'__name__': 'bor_ink', '__file__': path}
for node in tree.body:
    if isinstance(node, ast.Assert): continue
    exec(compile(ast.Module([node], []), path, 'exec'), ns)
LEGS = [
 "CIT_A", "CIT_B", "CIT_C", "CIT_D", "re.findall(r'\\([^)]*\\)', Hb(1, 2))[-4:]", "re.findall(r'\\([^)]*\\)', Hb(1, 7))[-2:]", "Hb(135, 1).rstrip()[-80:]", "NAMING",
 "STORE44", "[(x, m) for x, m in by[('Josh', 15, 4)] if x in ('והיה', 'והיו')]",
 "PARSED", "[(v, t) for v in range(1, NV + 1) for t in CS.verse_words('Num', 34, v) if t[-1] in '#~^%@|*']",
 "DIV[34]", "DIV[35]", "[c for c in range(1, 37) if len(DIV.get(c, [])) == 2]", "REG", "Counter(x for _, x in WQ)", "[x for v, x in WQ if v == 4]",
 "phrase(['צו', 'את', 'בני', 'ישראל'])", "U('צו', books=T)", "phrase(['זאת', 'הארץ'])", "U('תפל', books=T)", "aramaic(34, 2)[12:17]", "onk_seats('תתפלג')", "seats_in(GB)", "GBN",
 "sorted(S34 & S15)", "len(S34)", "len(U('פאת', 'לפאת', 'ולפאת', 'פאה', 'ופאת', books=T))", "sorted(phrase(['מדבר', 'צן'], None) + phrase(['ממדבר', 'צן'], None) + phrase(['במדבר', 'צן'], None))", "len(U('צנה'))", "NP('צנה')",
 "aramaic(34, 3)", "seats_in(lambda x, m: x == 'קדמה')", "len(U('קדמה', books=T))", "KB", "len(onk_seats('רקם'))", "words('Josh', 15, 3)[12:15]", "[t for t in byp[('Num', 34, 4)] if plain(t) == 'עצמנה']",
 "TOTS", "words('Gen', 15, 18)[13:15]", "words('1Kgs', 8, 65)[11:16]", "words('Deut', 11, 24)[12:16]", "words('Josh', 1, 4)[4:8]", "words('Exod', 23, 31)[3:8]", "[t for t in byp[('Num', 34, 2)] if plain(t) == 'בנחלה']",
 "YAM", "aramaic(34, 6)", "words('Josh', 15, 12)[:6]", "phrase(['הים', 'הגדול'], None)", "words('Gen', 15, 18)[16:20]",
 "U('תתאו', 'והתאויתם')", "[t for t in byp[('Prov', 23, 3)] if plain(t) == 'תתאו']", "U('ותאר', books=None)", "HOR", "onk_seats('הור טורא')", "onk_seats('הר טורא')", "aramaic(34, 7)[-2:]", "aramaic(34, 8)[:2]", "aramaic(34, 8)[3:5]",
 "U('שפמה', 'משפם', 'שפם')", "[t for t in byp[('Num', 34, 10)] if plain(t) == 'שפמה']", "len(U('רבלה', 'רבלתה', 'ברבלה', 'ברבלתה'))", "words('2Kgs', 23, 33)[3:6]", "U('ומחה')", "words('Num', 5, 23)[6:10]", "aramaic(5, 23)[6]", "aramaic(34, 11)[8]", "KTF", "U('כתף', books=None)", "words('Exod', 27, 14)[3:5]", "words('Num', 7, 9)[-3:]",
 "U('כנרת', 'כנרות', 'מכנרת')", "aramaic(34, 11)[11:13]", "U('הירדנה')", "words('Num', 34, 3)[14:16]", "words('Num', 34, 12)[5:7]", "aramaic(34, 12)[-2:]", "len(onk_seats('סחור סחור'))", "phrase(['זה', 'יהיה', 'לכם', 'גבול'], None)", "sum(1 for (c, v) in SPAN for x in words('Num', 34, v) if x == 'לכם')",
 "len(N34 & EZ)", "words('Ezek', 47, 13)[4:10]",
 "cnt_in(MT)", "sum(1 for (b, c, v), ws in by.items() if b == 'Num' for x, m in ws if MT(x, m))", "words('Num', 32, 33)[7:10]", "U('תשעת', 'לתשעת', 'ותשעת')", "RG", "words('Josh', 21, 5)[8:11]", "words('Josh', 21, 6)[10:13]", "len(U('אבתם', books=T))", "len([s for s in phrase(['לבית', 'אבתם']) if s.startswith('Num')])", "sum(1 for v in range(1, 30) for x in aramaic(34, v) if 'שבט' in x)", "aramaic(32, 33)[7:10]", "aramaic(34, 14)[12:15]", "aramaic(34, 15)[:2]",
 "len(phrase(['ואלה', 'שמות']))", "words('Num', 13, 16)[:5]", "wm('Josh', 14, 1)[:15]", "words('Josh', 19, 51)[:9]", "words('Josh', 13, 32)[:4]", "words('Num', 32, 28)[:10]", "words('Josh', 21, 1)[5:11]", "words('Num', 7, 11)[4:10]", "words('Num', 17, 21)[8:14]", "words('Num', 13, 2)[12:17]", "words('Josh', 22, 14)[3:9]", "len(U('תקחו', books=T))", "aramaic(34, 18)[:5]", "aramaic(7, 11)[3:7]", "aramaic(17, 21)[8:11]", "aramaic(13, 2)[12:16]", "aramaic(34, 17)[3:7]", "aramaic(34, 18)[6]", "aramaic(34, 29)[4]",
 "[v for v, w in ROST.items() if not w[0].startswith('ו')]", "sorted(phrase(['כלב', 'בן', 'יפנה']) + phrase(['וכלב', 'בן', 'יפנה']))", "len(NPX('כלב'))", "sorted((SP_NP & PR_NP) - TRIBES)", "sorted((C1_NP & PR_NP) - TRIBES)", "words('Num', 1, 10)[2:6]", "NPX('עמיהוד')", "len(NPX('שמואל'))", "[s for s in NPX('שמואל') if not s.startswith('1Sam')]", "NPX('בקי')", "words('Josh', 15, 10)[10:15]", "NPX('יפנה')[:3]", "len(NPX('יפנה'))",
 "ORD34", "ORDERS['Num 1:5-15']", "ORDERS['Num 13:4-15']", "[k for k, o in ORDERS.items() if before(o, 'Manasseh', 'Ephraim')]", "[k for k, o in ORDERS.items() if before(o, 'Zebulun', 'Issachar')]", "[(c, v, words('Josh', c, v)[:4]) for c, v in ((19, 10), (19, 17), (19, 24), (19, 32))]", "words('Josh', 19, 10)[3:5]", "words('Josh', 19, 24)[4:6]", "words('Deut', 33, 18)[3:6]",
 "phrase(['הנהר', 'הגדל', 'נהר', 'פרת'])", "words('Deut', 34, 2)",
 "GT", "store.execute(\"SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss='inherit--mode-of-descent)' GROUP BY 1\").fetchall()",
 "[k for k, v in OVERRIDE_REF + OVERRIDE_GLOSS if f'\"{k}\": \"{v}\"' not in OV]",
]
for e in LEGS:
    try: print(f'{e}  =>  {eval(e, ns)!r}')
    except Exception as ex: print(f'{e}  =>  ERROR {ex!r}')
