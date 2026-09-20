# the eight statements that fell on the first typed pass — every part printed (ch9_ink_diag.py's form)
import ast, sys, io, contextlib, re
path = sys.argv[1]; src = open(path, encoding='utf-8').read(); tree = ast.parse(src); ns = {'__name__': 'deu_ink', '__file__': path}
for node in tree.body:
    try: exec(compile(ast.Module([node], []), path, 'exec'), ns)
    except Exception as e: pass
g = ns
LED, P, U, words, LEMV = g['LED'], g['P'], g['U'], g['words'], g['LEMV']
T = g['T']
print('191:', [(k, s in LED[f]) for f, k in (('num_33_journeys_2026-09-12.md', 'Deut 10:6'), ('num_33_journeys_2026-09-12.md', 'Deuteronomy 10:6'), ('num_06_priest_blessing_2026-09-09.md', 'Deut 10:17'), ('lev_09_eighth_day_2026-09-05.md', 'Deut 10:8'), ('num_26_second_census_2026-09-11.md', 'Deut 10:22'), ('num_26_second_census_2026-09-11.md', 'Deuteronomy 10:22'), ('exodus_block_sanctuary_2026-09-04.md', 'Deut 10:1')) for s in [k]])
print('198:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Gen 46:', t, re.M)), sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (22|23):', t, re.M)), sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Lev 19:', t, re.M)), sorted(f for f, t in LED.items() if re.search(r'Onkelos Gen 46:', t))[:5], sorted(f for f, t in LED.items() if re.search(r'Onkelos Exod 2[23]:', t))[:6], sorted(f for f, t in LED.items() if re.search(r'Onkelos Lev 19:', t))[:5])
print('324:', P('ועלה', 'אלי', 'ההרה'), P('עלה', 'אלי', 'ההרה'), P('ארון', 'עץ'), P('ארון', 'עצי', 'שטים'), len(g['LEMT']('727', books=T)), len(g['LEMT']('727', books=('Deut',))), [s for s, x, _ in g['LEMT']('727', books=('Deut',))], 'Gen 50:26' in LEMV('727'))
print('325:', P('ארון', 'ברית', 'יהוה', books=T), P('ארון', 'ברית', 'יהוה', books=('Josh',)), P('ארון', 'העדת'), P('ארון', 'העדות'), len(P('ארון', 'הברית') + P('ארון', 'ברית')))
print('331:', P('ובני', 'ישראל', 'נסעו'), P('בני', 'יעקן'), U('יעקן', 'ויעקן'), U('מוסרה', 'מסרות', 'ממסרות', 'במסרות', 'מוסרות'), U('הגדגדה', 'הגדגד'), U('יטבתה', 'ביטבתה', 'מיטבתה'), P('ארץ', 'נחלי', 'מים'))
print('339:', U('לאהבה', 'ולאהבה', books=('Deut',)), P('ולעבד', 'את', 'יהוה', 'אלהיך'), P('בכל', 'לבבך', 'ובכל', 'נפשך', books=('Deut',)), P('בכל', 'לבבכם', 'ובכל', 'נפשכם', books=('Deut',)), len(P('בכל', 'לבבך', 'ובכל', 'נפשך')) + len(P('בכל', 'לבבכם', 'ובכל', 'נפשכם')), P('ובכל', 'מאדך'), P('ובכל', 'מאדו'))
print('341:', P('הן', 'ליהוה', 'אלהיך', 'השמים'), U('הן', books=('Deut',)), P('ושמי', 'השמים'), P('שמי', 'השמים'), P('הארץ', 'וכל', 'אשר', 'בה'), P('כי', 'לי', 'כל', 'הארץ'), P('הארץ', 'ומלואה'), P('הארץ', 'ומלאה'), P('ארץ', 'ומלאה'))
print('352:', P('בשבעים', 'נפש'), P('שבעים', 'נפש'), words('Gen', 46, 27)[6:9], words('Gen', 46, 27)[-1], words('Exod', 1, 5)[6:8], len(U('שבעים', 'בשבעים', 'ושבעים', books=T)), P('ככוכבי', 'השמים', 'לרב'), P('ככוכבי', 'השמים'), U('לרב', 'לרוב', books=('Deut',)))
