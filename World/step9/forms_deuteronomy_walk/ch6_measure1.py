#!/usr/bin/env python3
# DEUTERONOMY CHAPTER 6, THE READING (sitting 4, 2026-09-17; the owner: "ok lets start the next chapter"; RUN 1 of four): THE SECOND MEASUREMENT PASS — every candidate ink fact PRINTED
# from the Tanakh DB, the store and the shelf's bytes, so that ch6_ink.py's asserts are typed FROM THE PRINT. THE KIN DIFFED token by token —
# the sign and the frontlets against Exodus 13:9, 16 and 11:18-20; the son's question and the answer against Exodus 12:26-27, 13:8, 13:14;
# Massah against Exodus 17:2-7; the frame against 4:1-40 and 5:29-33; fear-serve-swear against 10:20 — the phrase censuses over the whole DB;
# Onkelos's renderings' seats over the whole book (the export's chapter 6 = the DB's, identity); the English's bracketed supplements; the
# store's gloss families. Chapter 5's helpers (ch5_measure1.py lines 1-57 by sed); the sections chapter 6's own. Nothing asserted.
import json, os, re, html, sqlite3, subprocess, unicodedata, sys, io, contextlib
from collections import Counter
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
sys.path.insert(0, f'{ROOT}/World/step9')
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
def NF(s): return unicodedata.normalize('NFC', s)
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph, w.lemma, w.wtype FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by = {}
for b, c, v, he, m, lem, wt in rows: by.setdefault((b, c, v), []).append((plain(he), m, he, lem, wt))
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
def words(b, c, v): return [x for x, _, _, _, _ in by[(b, c, v)]]
def wm(b, c, v): return [(x, m) for x, m, _, _, _ in by[(b, c, v)]]
def base(l): return (l or '').split('/')[-1].strip()
def hits(sub, books=None, exact=True): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if (books is None or b in books) and any((x == sub) if exact else (sub in x) for x, _, _, _, _ in ws)})
def U(*toks, books=None): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if books is None or b in books for x, _, _, _, _ in ws if x in toks})
def phrase(seq, books=None):
    out = []
    for (b, c, v), ws in by.items():
        if books is not None and b not in books: continue
        w = [x for x, _, _, _, _ in ws]
        if any(w[i:i + len(seq)] == list(seq) for i in range(len(w) - len(seq) + 1)): out.append(f'{b} {c}:{v}')
    return sorted(out)
def P(*seq, books=None): return phrase(list(seq), books)
def LEMT(lem, books=None): return [(f'{b} {c}:{v}', x, m) for (b, c, v), ws in by.items() if (books is None or b in books) for x, m, _, l, _ in ws if base(l) == lem]
def LEMV(lem, books=None): return sorted({s for s, _, _ in LEMT(lem, books)})
def lemma_of(b, c, v, tok): return [base(l) for x, _, _, l, _ in by[(b, c, v)] if x == tok]
def PT(b, c, v, tok): return [NF(pointed(r)) for x, _, r, _, _ in by[(b, c, v)] if x == tok]
def FAM(sub, books=None): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if (books is None or b in books) for x, _, _, _, _ in ws if sub in x})
def DIFF(a, b_):
    A, B = words(*a), words(*b_)
    import difflib
    sm = difflib.SequenceMatcher(a=A, b=B)
    out = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal': out.append('=' + ' '.join(A[i1:i2]))
        else: out.append(f'[{tag}: {" ".join(A[i1:i2])!r} -> {" ".join(B[j1:j2])!r}]')
    return f'{a[0]} {a[1]}:{a[2]} ({len(A)}) vs {b_[0]} {b_[1]}:{b_[2]} ({len(B)}): ' + ' '.join(out)
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Deuteronomy/en.json', encoding='utf-8'))['text']
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Deuteronomy/he.json', encoding='utf-8'))['text']
def arm(c, v): return [plain(x).strip('.:') for x in clean(onk_he[c - 1][v - 1]).rstrip(':').split()]
def onk_seats(sub): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if sub in ' '.join(arm(c + 1, v + 1))]
def onk_tok(tok): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if tok in arm(c + 1, v + 1)]
CH = 6
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
EXP2DB = {e: [e] for e in range(1, 26)}   # typed from ch6_dump0's A0 print: 25 = 25, the identity (chapter 5 the book's one split)
DB2EXP = {d: e for e, ds in EXP2DB.items() for d in ds}
def L(label, val): print(f'  {label}: {val}')
V6 = lambda v: words('Deut', 6, v)
print('==== A. THE KIN DIFFED (the DB\'s tokens; backward seats and the book\'s later seats alike — a diff is a measurement, not a reading)')
for a, b_ in ((('Deut', 6, 1), ('Deut', 5, 31)), (('Deut', 6, 1), ('Deut', 4, 14)), (('Deut', 6, 1), ('Deut', 7, 11)), (('Deut', 6, 2), ('Deut', 5, 29)), (('Deut', 6, 2), ('Deut', 4, 40)),
              (('Deut', 6, 3), ('Deut', 4, 1)), (('Deut', 6, 3), ('Deut', 5, 1)), (('Deut', 6, 3), ('Deut', 5, 33)), (('Deut', 6, 4), ('Deut', 5, 1)), (('Deut', 6, 5), ('Deut', 11, 13)), (('Deut', 6, 5), ('Deut', 10, 12)),
              (('Deut', 6, 6), ('Deut', 11, 18)), (('Deut', 6, 7), ('Deut', 11, 19)), (('Deut', 6, 8), ('Exod', 13, 9)), (('Deut', 6, 8), ('Exod', 13, 16)), (('Deut', 6, 8), ('Deut', 11, 18)), (('Deut', 6, 9), ('Deut', 11, 20)),
              (('Deut', 6, 10), ('Deut', 1, 8)), (('Deut', 6, 10), ('Exod', 13, 5)), (('Deut', 6, 11), ('Deut', 8, 10)), (('Deut', 6, 11), ('Deut', 8, 12)), (('Deut', 6, 12), ('Deut', 8, 11)), (('Deut', 6, 12), ('Deut', 5, 6)), (('Deut', 6, 12), ('Exod', 13, 3)),
              (('Deut', 6, 13), ('Deut', 10, 20)), (('Deut', 6, 14), ('Deut', 5, 7)), (('Deut', 6, 14), ('Deut', 11, 28)), (('Deut', 6, 15), ('Deut', 4, 24)), (('Deut', 6, 15), ('Deut', 5, 9)), (('Deut', 6, 15), ('Deut', 11, 17)),
              (('Deut', 6, 16), ('Exod', 17, 7)), (('Deut', 6, 16), ('Exod', 17, 2)), (('Deut', 6, 16), ('Deut', 33, 8)), (('Deut', 6, 17), ('Deut', 11, 22)), (('Deut', 6, 17), ('Deut', 4, 45)), (('Deut', 6, 18), ('Deut', 12, 28)), (('Deut', 6, 18), ('Deut', 5, 33)),
              (('Deut', 6, 19), ('Deut', 9, 4)), (('Deut', 6, 20), ('Exod', 13, 14)), (('Deut', 6, 20), ('Exod', 12, 26)), (('Deut', 6, 20), ('Deut', 4, 45)), (('Deut', 6, 21), ('Exod', 13, 14)), (('Deut', 6, 21), ('Exod', 13, 3)), (('Deut', 6, 21), ('Exod', 13, 8)),
              (('Deut', 6, 22), ('Deut', 4, 34)), (('Deut', 6, 22), ('Deut', 7, 19)), (('Deut', 6, 23), ('Deut', 4, 37)), (('Deut', 6, 23), ('Deut', 4, 38)), (('Deut', 6, 24), ('Deut', 10, 13)), (('Deut', 6, 24), ('Deut', 4, 40)), (('Deut', 6, 25), ('Deut', 24, 13)), (('Deut', 6, 25), ('Deut', 5, 32))):
    print(' ', DIFF(a, b_))
print('==== B. THE PHRASE CENSUSES over the whole DB (Torah where marked)')
L('"hear, O Israel" (שמע ישראל)', P('שמע', 'ישראל'))
L('"the LORD is one" (יהוה אחד)', P('יהוה', 'אחד')); L('"one" beside the Name anywhere — אחד after יהוה within the verse', [f'{b} {c}:{v}' for (b, c, v), ws in by.items() if 'יהוה' in [x for x, *_ in ws] and 'אחד' in [x for x, *_ in ws]][:30])
L('"our God" (אלהינו) after "the LORD" in Deuteronomy', len(P('יהוה', 'אלהינו', books=('Deut',))), ), L('  the chapter\'s seats', [v for v in range(1, 26) for i in range(len(V6(v)) - 1) if V6(v)[i:i + 2] == ['יהוה', 'אלהינו']])
L('"and you shall love the LORD your God" (ואהבת את יהוה אלהיך)', P('ואהבת', 'את', 'יהוה', 'אלהיך')); L('"and you shall love" (ואהבת) seats', U('ואהבת'))
L('"with all your heart and with all your soul" (בכל לבבך ובכל נפשך)', P('בכל', 'לבבך', 'ובכל', 'נפשך')); L('the plural form (בכל לבבכם ובכל נפשכם)', P('בכל', 'לבבכם', 'ובכל', 'נפשכם'))
L('"and with all your might" (ובכל מאדך) — the token מאדך anywhere', U('מאדך', 'מאדכם', 'ומאדך')); L('"might" as a noun with a suffix over the Bible (מאד + suffix)', hits('מאדך', exact=False)[:12])
L('"these words" (הדברים האלה) in Deuteronomy', P('הדברים', 'האלה', books=('Deut',))); L('"which I command you today" (אשר אנכי מצוך היום) in Deuteronomy', len(P('אשר', 'אנכי', 'מצוך', 'היום', books=('Deut',))), ), L('  the chapter\'s', [v for v in range(1, 26) if 'מצוך' in V6(v)])
L('"upon your heart" (על לבבך)', P('על', 'לבבך')); L('"upon your heart" plural (על לבבכם)', P('על', 'לבבכם'))
L('"and you shall teach them diligently" (ושננתם) — the lemma 8150 seats', LEMV('8150')); L('  the token', U('ושננתם'))
L('"and you shall speak of them" (ודברת בם)', P('ודברת', 'בם')); L('"when you sit in your house … when you rise" (בשבתך בביתך ובלכתך בדרך ובשכבך ובקומך)', P('בשבתך', 'בביתך', 'ובלכתך', 'בדרך', 'ובשכבך', 'ובקומך'))
L('"for a sign upon your hand" (לאות על ידך / ידכה / ידכם)', [(s, [x for x in words(*[s.split()[0], *map(int, s.split()[1].split(':'))]) if x.startswith('יד')]) for s in P('לאות', 'על') if s in U('ידך', 'ידכה', 'ידכם')])
L('"frontlets" — every spelling of טטפת over the Bible', hits('טטפת', exact=False) + hits('טוטפת', exact=False)); L('  the tokens by seat', [(s, [x for x in words(*[s.split()[0], *map(int, s.split()[1].split(':'))]) if 'טפת' in x]) for s in hits('טפת', exact=False)])
L('"between your eyes" (בין עיניך / עיניכם)', P('בין', 'עיניך') + P('בין', 'עיניכם'))
L('"and you shall write them" (וכתבתם)', U('וכתבתם')); L('"doorposts" — מזוזת / מזזות / מזוזות seats', U('מזוזת', 'מזזות', 'מזוזות', 'המזוזת', 'המזוזות')); L('"and upon your gates" (ובשעריך)', U('ובשעריך'))
L('"which He swore to your fathers" (אשר נשבע לאבתיך) in Deuteronomy', P('אשר', 'נשבע', 'לאבתיך', books=('Deut',))); L('"to Abraham, to Isaac and to Jacob" (לאברהם ליצחק וליעקב)', P('לאברהם', 'ליצחק', 'וליעקב')); L('"which He swore to our fathers" (נשבע לאבתינו)', P('נשבע', 'לאבתינו'))
L('"swore" (נשבע) seats in Deuteronomy', U('נשבע', books=('Deut',)))
L('"great and good cities" (ערים גדלת וטבת)', P('ערים', 'גדלת', 'וטבת')); L('"houses full of all good" (ובתים מלאים כל טוב)', P('ובתים', 'מלאים', 'כל', 'טוב')); L('"hewn cisterns" (וברת חצובים)', P('וברת', 'חצובים')); L('"vineyards and olive trees" (כרמים וזיתים)', P('כרמים', 'וזיתים'))
L('"and you shall eat and be satisfied" (ואכלת ושבעת)', P('ואכלת', 'ושבעת')); L('"and be satisfied" plural (ואכלתם ושבעתם / ואכל ושבע)', P('ואכלתם', 'ושבעתם') + P('ואכל', 'ושבע'))
L('"take heed to yourself lest you forget" (השמר לך פן תשכח)', P('השמר', 'לך', 'פן', 'תשכח')); L('"lest you forget" (פן תשכח / תשכחו)', U('תשכח', 'תשכחו'))
L('"who brought you out of the land of Egypt, from the house of bondage" — הוציאך / הוצאתיך + מבית עבדים', [s for s in P('מבית', 'עבדים') if s in U('הוציאך', 'הוצאתיך', 'המוציאך')]); L('"house of bondage" (בית עבדים) seats', P('בית', 'עבדים') + P('מבית', 'עבדים'))
L('"the LORD your God you shall fear" (את יהוה אלהיך תירא)', P('את', 'יהוה', 'אלהיך', 'תירא')); L('"and by His name you shall swear" (ובשמו תשבע)', P('ובשמו', 'תשבע')); L('"Him you shall serve" (ואתו תעבד / אתו תעבד)', P('ואתו', 'תעבד') + P('אתו', 'תעבד'))
L('"after other gods" (אחרי אלהים אחרים)', P('אחרי', 'אלהים', 'אחרים')); L('"you shall not go" plural with the nun (לא תלכון)', P('לא', 'תלכון')); L('"of the gods of the peoples around you" (מאלהי העמים אשר סביבותיכם)', P('מאלהי', 'העמים', 'אשר', 'סביבותיכם'))
L('"a jealous God" (אל קנא)', P('אל', 'קנא')); L('"in your midst" (בקרבך) in Deuteronomy', U('בקרבך', books=('Deut',))); L('"lest the anger of the LORD be kindled against you" (פן יחרה אף יהוה)', P('פן', 'יחרה', 'אף', 'יהוה')); L('"and destroy you from the face of the ground" (והשמידך מעל פני האדמה)', P('והשמידך', 'מעל', 'פני', 'האדמה')); L('"from the face of the ground" (מעל פני האדמה)', P('מעל', 'פני', 'האדמה'))
L('"you shall not test" (לא תנסו / תנסה)', U('תנסו', 'תנסה', 'תנסון')); L('"Massah" (מסה / במסה / ומסה) seats', U('מסה', 'במסה', 'ומסה', 'המסה')); L('"as you tested" (נסיתם / נסיתו / נסיתי)', U('נסיתם', 'נסיתו', 'נסיתי')); L('the lemma 5254 "test" seats in the Torah', LEMV('5254', books=T))
L('"you shall surely keep" (שמור תשמרון)', P('שמור', 'תשמרון')); L('the infinitive absolute שמור seats (HVqa)', [(s, m) for s, x, m in LEMT('8104') if x == 'שמור' and m == 'HVqa'])
L('"the testimonies and the statutes and the judgments" (העדת והחקים והמשפטים)', P('העדת', 'והחקים', 'והמשפטים')); L('"testimonies" (עדת / העדת / עדתיו / ועדתיו) seats in the Torah', U('עדת', 'העדת', 'עדתיו', 'ועדתיו', 'עדותיו', 'ועדותיו', books=T))
L('"the commandments … His testimonies and His statutes" (ועדתיו וחקיו)', P('ועדתיו', 'וחקיו')); L('"the commandment, the statutes and the judgments" — the triad by order', [(s, [x for x in words(*[s.split()[0], *map(int, s.split()[1].split(':'))]) if x in ('המצוה', 'החקים', 'והחקים', 'והמשפטים', 'המשפטים', 'ואת', 'החקים')]) for s in U('המצוה', books=('Deut',)) if s in U('והמשפטים', 'המשפטים', books=('Deut',))])
L('"and you shall do what is right and good" (ועשית הישר והטוב)', P('ועשית', 'הישר', 'והטוב')); L('"the right and the good" / "the good and the right"', P('הישר', 'והטוב') + P('הטוב', 'והישר')); L('"right in the eyes of the LORD" (הישר בעיני יהוה) in the Torah', P('הישר', 'בעיני', 'יהוה', books=T))
L('"to thrust out all your enemies" (להדף את כל איביך)', P('להדף', 'את', 'כל', 'איביך')); L('the lemma 1920 "thrust" seats', LEMV('1920')); L('"as the LORD has spoken" (כאשר דבר יהוה) in Deuteronomy', P('כאשר', 'דבר', 'יהוה', books=('Deut',)))
L('"when your son asks you tomorrow" (כי ישאלך בנך מחר)', P('כי', 'ישאלך', 'בנך', 'מחר')); L('"your son … tomorrow" — ישאלך / ישאלון + מחר anywhere', [s for s in U('מחר') if s in U('ישאלך', 'ישאלון', 'ישאלו', 'בניכם', 'בנך')]); L('"what is this" (מה זאת) Exodus 13:14 / "what are the testimonies" (מה העדת)', P('מה', 'זאת') + P('מה', 'העדת'))
L('"and you shall say to your son" (ואמרת לבנך)', P('ואמרת', 'לבנך')); L('"and you shall tell your son" (והגדת לבנך)', P('והגדת', 'לבנך')); L('"we were slaves to Pharaoh" (עבדים היינו לפרעה)', P('עבדים', 'היינו', 'לפרעה')); L('"with a strong hand" (ביד חזקה) in the Torah', P('ביד', 'חזקה', books=T))
L('"signs and wonders" — אתת / אותת + ומפתים / ומופתים', [(s, [x for x in words(*[s.split()[0], *map(int, s.split()[1].split(':'))]) if x in ('אתת', 'אותת', 'ומפתים', 'ומופתים', 'ובמפתים', 'ובמופתים')]) for s in U('אתת', 'אותת', 'ואתת') if s in U('ומפתים', 'ומופתים', 'ובמפתים', 'ובמופתים')]); L('"great and grievous" (גדלים ורעים)', P('גדלים', 'ורעים')); L('"before our eyes" (לעינינו)', U('לעינינו'))
L('"and us He brought out from there" (ואותנו הוציא משם)', P('ואותנו', 'הוציא', 'משם')); L('"to bring us in, to give us the land" (הביא אתנו לתת לנו)', P('הביא', 'אתנו', 'לתת', 'לנו'))
L('"and the LORD commanded us" (ויצונו יהוה)', P('ויצונו', 'יהוה')); L('"to fear the LORD our God" (ליראה את יהוה אלהינו)', P('ליראה', 'את', 'יהוה', 'אלהינו')); L('"for our good always" (לטוב לנו כל הימים)', P('לטוב', 'לנו', 'כל', 'הימים')); L('"to keep us alive as at this day" (לחיתנו כהיום הזה)', P('לחיתנו', 'כהיום', 'הזה')); L('"as at this day" (כהיום הזה)', P('כהיום', 'הזה'))
L('"and it shall be righteousness for us" (וצדקה תהיה לנו)', P('וצדקה', 'תהיה', 'לנו')); L('"righteousness" (צדקה / וצדקה / לצדקה) seats in the Torah', U('צדקה', 'וצדקה', 'לצדקה', 'צדקתך', 'ובצדקתך', 'בצדקתי', 'בצדקתך', books=T)); L('"as He commanded us" (כאשר צונו)', P('כאשר', 'צונו')); L('"all this commandment" (כל המצוה הזאת)', P('כל', 'המצוה', 'הזאת'))
L('"that you may fear the LORD your God" (למען תירא את יהוה אלהיך)', P('למען', 'תירא', 'את', 'יהוה', 'אלהיך')); L('"you and your son and your son\'s son" (אתה ובנך ובן בנך)', P('אתה', 'ובנך', 'ובן', 'בנך')); L('"and your son\'s son" (ובן בנך)', P('ובן', 'בנך')); L('"all the days of your life" (כל ימי חייך)', P('כל', 'ימי', 'חייך')); L('"that your days may be prolonged" — יארכן / יאריכן / יאריך ימיך', U('יארכן', 'יאריכן', 'יארכון', 'יאריך', 'ולמען'), ), L('  the exact "and that your days may be long" (ולמען יארכן ימיך)', P('ולמען', 'יארכן', 'ימיך'))
L('"a land flowing with milk and honey" (ארץ זבת חלב ודבש) in the Torah', P('ארץ', 'זבת', 'חלב', 'ודבש', books=T)); L('"and you shall hear, O Israel" (ושמעת ישראל)', P('ושמעת', 'ישראל')); L('"and observe to do" (ושמרת לעשות)', P('ושמרת', 'לעשות')); L('"that it may be well with you" (אשר ייטב לך / למען ייטב לך) in Deuteronomy', P('ייטב', 'לך', books=('Deut',))); L('"that you may multiply greatly" (תרבון מאד)', P('תרבון', 'מאד'))
L('"and this is the commandment" (וזאת המצוה)', P('וזאת', 'המצוה')); L('"to teach you" (ללמד אתכם)', P('ללמד', 'אתכם')); L('"which you are crossing over to possess" (אשר אתם עברים שמה לרשתה)', P('אשר', 'אתם', 'עברים', 'שמה', 'לרשתה'))
L('the divine name by form in chapter 6', Counter(x for v in range(1, 26) for x in V6(v) if x in ('יהוה', 'ויהוה', 'ביהוה', 'כיהוה', 'ליהוה'))); L('"the LORD your God" singular (יהוה אלהיך) seats in ch 6', [v for v in range(1, 26) for i in range(len(V6(v)) - 1) if V6(v)[i:i + 2] == ['יהוה', 'אלהיך']]); L('plural (יהוה אלהיכם)', [v for v in range(1, 26) for i in range(len(V6(v)) - 1) if V6(v)[i:i + 2] == ['יהוה', 'אלהיכם']])
L('"God" (אלהים / אלהי) bare or construct in chapter 6', {v: [x for x in V6(v) if x in ('אלהים', 'האלהים', 'אלהי', 'מאלהי')] for v in range(1, 26) if any(x in ('אלהים', 'האלהים', 'אלהי', 'מאלהי') for x in V6(v))}); L('Moses named in chapter 6?', [v for v in range(1, 26) if 'משה' in V6(v)]); L('Israel named', [v for v in range(1, 26) if 'ישראל' in V6(v)])
print('==== C. THE NUMBER VERSE 6:4 and the seven-stem homographs — the parser\'s reading')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
for v in (4, 10, 11, 13, 18, 23):
    print(f'  6:{v} verse_words', CS.verse_words('Deut', 6, v), '| numbers', CS.ink_numbers(CS.verse_words('Deut', 6, v)), '| ordinals', CS.ink_ordinals(CS.verse_words('Deut', 6, v)))
for b, c, v in (('Zech', 14, 9), ('Deut', 4, 35), ('Deut', 4, 39), ('Deut', 32, 39), ('Exod', 20, 2), ('Deut', 5, 6), ('Gen', 2, 24), ('Deut', 17, 6), ('Deut', 19, 15), ('Mal', 2, 10)):
    if (b, c, v) in by: print(f'  {b} {c}:{v} verse_words', CS.verse_words(b, c, v), '| numbers', CS.ink_numbers(CS.verse_words(b, c, v)))
L('6:4 the DB row (token, morph, lemma)', [(x, m, base(l)) for x, m, _, l, _ in by[('Deut', 6, 4)]]); L('the pointed 6:4', [NF(pointed(r)) for _, _, r, _, _ in by[('Deut', 6, 4)]])
L('the lemma 259 "one" (אחד) count in the Torah by book', Counter(s.split()[0] for s in LEMV('259', books=T))); L('"one" (אחד) as a predicate of the Name — Zechariah 14:9 tokens', words('Zech', 14, 9))
L('6:11 ושבעת pointed / 6:10 נשבע pointed / 6:13 תשבע pointed', (PT('Deut', 6, 11, 'ושבעת'), PT('Deut', 6, 10, 'נשבע'), PT('Deut', 6, 13, 'תשבע'))); L('the lemma of ושבעת and of נשבע', (lemma_of('Deut', 6, 11, 'ושבעת'), lemma_of('Deut', 6, 10, 'נשבע'), lemma_of('Deut', 6, 13, 'תשבע')))
print('==== D. THE REGISTER — the second-person number by verse (2mp count, 2ms count), the first person, the verb forms')
NUM = {v: (sum(1 for _, m, _, _, _ in by[('Deut', 6, v)] if m and '2mp' in m), sum(1 for _, m, _, _, _ in by[('Deut', 6, v)] if m and '2ms' in m)) for v in range(1, 26)}
L('2mp / 2ms per verse', NUM); L('singular-only verses', [v for v, (p, s) in NUM.items() if s and not p]); L('plural-only', [v for v, (p, s) in NUM.items() if p and not s]); L('both', [v for v, (p, s) in NUM.items() if p and s]); L('neither', [v for v, (p, s) in NUM.items() if not p and not s])
L('first-person plural (1cp) per verse', {v: [(x, m) for x, m, _, _, _ in by[('Deut', 6, v)] if m and '1cp' in m] for v in range(1, 26) if any(m and '1cp' in m for _, m, _, _, _ in by[('Deut', 6, v)])}); L('first-person singular (1cs)', {v: [(x, m) for x, m, _, _, _ in by[('Deut', 6, v)] if m and '1cs' in m] for v in range(1, 26) if any(m and '1cs' in m for _, m, _, _, _ in by[('Deut', 6, v)])})
L('imperatives (HV.v / HV..v) per verse', {v: [(x, m) for x, m, _, _, _ in by[('Deut', 6, v)] if m and re.match(r'^HV.?.?v', m)] for v in range(1, 26) if any(m and re.match(r'^HV.?.?v', m) for _, m, _, _, _ in by[('Deut', 6, v)])})
L('infinitive absolutes (HV.a)', {v: [(x, m) for x, m, _, _, _ in by[('Deut', 6, v)] if m and re.match(r'^HV.a$', m)] for v in range(1, 26) if any(m and re.match(r'^HV.a$', m) for _, m, _, _, _ in by[('Deut', 6, v)])})
L('consecutive perfects (V.q) per verse — the law\'s form', {v: [x for x, m, _, _, _ in by[('Deut', 6, v)] if m and re.search(r'^HC/V.q', m)] for v in range(1, 26) if any(m and re.search(r'^HC/V.q', m) for _, m, _, _, _ in by[('Deut', 6, v)])})
L('imperfect second person (V.i2) per verse', {v: [(x, m) for x, m, _, _, _ in by[('Deut', 6, v)] if m and re.search(r'^HV.i2', m)] for v in range(1, 26) if any(m and re.search(r'^HV.i2', m) for _, m, _, _, _ in by[('Deut', 6, v)])})
L('narrative (wayyiqtol, V.w) per verse', {v: [x for x, m, _, _, _ in by[('Deut', 6, v)] if m and re.search(r'^HC/V.w', m)] for v in range(1, 26) if any(m and re.search(r'^HC/V.w', m) for _, m, _, _, _ in by[('Deut', 6, v)])})
L('prohibitions לא + imperfect', {v: [(by[('Deut', 6, v)][i + 1][0], by[('Deut', 6, v)][i + 1][1]) for i, (x, _, _, _, _) in enumerate(by[('Deut', 6, v)][:-1]) if x == 'לא' and by[('Deut', 6, v)][i + 1][1] and by[('Deut', 6, v)][i + 1][1].startswith('HV')] for v in range(1, 26) if any(x == 'לא' for x, _, _, _, _ in by[('Deut', 6, v)])})
L('case tokens per verse', {f'6:{v}': [x for x in V6(v) if x in ('כי', 'אם', 'ואם', 'או', 'פן')] for v in range(1, 26) if any(x in ('כי', 'אם', 'ואם', 'או', 'פן') for x in V6(v))}); L('"saying" (לאמר) seats', [v for v in range(1, 26) if 'לאמר' in V6(v)]); L('divine frames (ויאמר/וידבר יהוה)', [v for v in range(1, 26) if any(V6(v)[i] in ('ויאמר', 'וידבר') and V6(v)[i + 1] == 'יהוה' for i in range(len(V6(v)) - 1))])
L('tokens per verse', {v: len(V6(v)) for v in range(1, 26)}); L('the chapter\'s tokens and letters', (sum(len(V6(v)) for v in range(1, 26)), sum(len(x) for v in range(1, 26) for x in V6(v))))
L('6:4-9 tokens and letters (the six verses of the six piskaot)', (sum(len(V6(v)) for v in range(4, 10)), sum(len(x) for v in range(4, 10) for x in V6(v)))); L('6:4 letters', sum(len(x) for x in V6(4)))
L('wtype values in chapter 6', Counter(wt for v in range(1, 26) for _, _, _, _, wt in by[('Deut', 6, v)]))
print('==== E. ONKELOS chapter 6 — the renderings\' seats over the book (token → EXPORT seats; the export = the DB except chapter 5\'s 17+), the phrases')
for tok in ('חד', 'נכסך', 'נכסכון', 'תפלין', 'מזוזין', 'ותקבענון', 'בספי', 'דחלתא', 'שכנתיה', 'בנסיתא', 'זכותא', 'קדמוהי', 'תקים', 'טעות', 'דכשר', 'ודתקן', 'למתבר', 'סהדותא', 'ותתננון', 'ותרחם', 'ותקבל', 'קיים', 'אפקך', 'תפקדתא', 'קימיא', 'דיניא', 'עבדותא', 'לחדא', 'רגזא', 'וישצך', 'אנש', 'פתגמיא', 'ותמלל', 'תנשי', 'דילמא', 'ארי', 'למדחל', 'לקימותנא', 'תדחל', 'תפלח', 'מקדמך', 'דבבך', 'בסחרניכון', 'עממיא', 'לאלפא', 'למירתה'):
    s = onk_tok(tok); print(f'  {tok}: {len(s)} {s[:24]}')
print('---- phrases')
for sub in ('יי חד', 'ובכל נכסך', 'שכנתיה בינך', 'דחלתא דיי', 'ית דחלתא', 'קדם יי אלהך', 'קדם יי', 'קדמוהי תפלח', 'ובשמיה תקים', 'טעות עממיא', 'בתר טעות', 'דכשר ודתקן', 'סהדותא וקימיא ודיניא', 'תפקדתא קימיא ודיניא', 'קימיא ודיניא', 'למתבר ית כל', 'בעלי דבבך', 'זכותא תהי', 'וזכותא', 'ותקבענון בספי', 'על מזוזין', 'לתפלין בין עיניך', 'ותתננון לבניך', 'ועבדין הוינא', 'עבדין הוינא', 'בידא תקיפא', 'אתין ומופתין', 'אנש ביתיה', 'כל אנש', 'לחדא', 'עבדא חלב ודבש', 'כמא די מליל יי', 'כמא די פקדנא', 'כמא די'):
    s = onk_seats(sub); print(f'  {sub!r}: {len(s)} {s[:24]}')
L('the parenthesised variant in the export\'s 6:12 — the raw row', clean(onk_he[5][11])); L('rows in Onkelos Deuteronomy carrying a parenthesis (the export\'s variants) — chapter:verse', [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if '(' in clean(onk_he[c][v])][:40])
print('==== F. THE ENGLISH ONKELOS — the bracketed insertions per export verse (the translation\'s supplied words)')
for e in range(1, 26):
    en = clean(onk[5][e - 1]); br = re.findall(r'\[([^\]]+)\]', en)
    if br: print(f'  export 6:{e}: {br}')
print('==== G. THE STORE GLOSS FAMILIES for the candidate rewrites (every form of the gloss over the whole store)')
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
L('the store\'s "?" glosses in chapter 6 (token, verse, idx)', store.execute("SELECT v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=6 AND w.gloss='?' ORDER BY v.verse, w.idx").fetchall()); L('the store\'s "?" glosses over the Torah — count and the tokens', store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book IN ('Gen','Exod','Lev','Num','Deut') AND w.gloss='?' GROUP BY 1 ORDER BY 2 DESC").fetchall()[:12])
for g in ('to-goad', 'goad', 'and-goad', 'goad-them/their', '?', 'and-point-them/their', 'point', 'mislay', 'hinder', 'hind-part', 'strength', 'nose', 'glow', 'deferred', 'and-grave-them/their', 'grave', 'strike-in', 'and-pit-hole', 'and-have-affection-for', 'have-affection-for', 'very-you/your', 'living-being-you/your', 'to-fillet-for-the-forehead', 'and-rightness', 'rightness', 'hating-you/your', 'to-push-away', 'and-bad', 'and-miracle', 'circle-you/your (pl)', 'in-nearest-part-you/your', 'and-desolate-you/your', 'to-good--in-the-widest-sense', 'and-sate', 'cut', 'garden', 'multiply-suffix', 'flow-freely', 'be--long-suffix', 'go-suffix', 'keep/guard-suffix', 'to-set', 'come/bring-you/your', 'the-straight', 'work/serve', 'inquire-you/your', 'the-word/thing', 'pass-over', 'to-live-us/our', 'like-the-day', 'to-fear', 'and-tie-them/their', 'to-signs', 'door-post', 'in-Massah', 'test', 'and-son', 'to-say', 'be', 'to-make', 'in-dwell/sit-you/your', 'and-in-lie-down-you/your', 'and-in-arise-you/your', 'in-way/road', 'the-ground', 'from-over'):
    rr = store.execute("SELECT REPLACE(w.he_plain,'/',''), COUNT(*) FROM words w WHERE w.gloss=? GROUP BY 1 ORDER BY 2 DESC, 1", (g,)).fetchall()
    if rr and len(rr) <= 14 and sum(n for _, n in rr) <= 120: print(f'  gloss {g!r}: {len(rr)} forms, {sum(n for _, n in rr)} tokens: {rr}')
    elif rr: print(f'  gloss {g!r}: {len(rr)} forms, {sum(n for _, n in rr)} tokens (large): {rr[:6]}')
    else: print(f'  gloss {g!r}: ABSENT from the store')
import yaml
d = yaml.safe_load(open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8'))
L('by_gloss keys already present among the chapter\'s candidates', sorted(g for g in ('to-goad', 'goad', 'and-goad', 'goad-them/their', 'and-point-them/their', 'mislay', 'hinder', 'hind-part', 'strength', 'nose', 'glow', 'deferred', 'and-grave-them/their', 'strike-in', 'and-pit-hole', 'and-have-affection-for', 'very-you/your', 'living-being-you/your', 'to-fillet-for-the-forehead', 'and-rightness', 'hating-you/your', 'to-push-away', 'and-bad', 'and-miracle', 'circle-you/your (pl)', 'in-nearest-part-you/your', 'and-desolate-you/your', 'to-good--in-the-widest-sense', 'and-sate', 'cut', 'garden', 'multiply-suffix', 'flow-freely', 'be--long-suffix', 'go-suffix', 'keep/guard-suffix', 'to-set', 'come/bring-you/your', 'the-straight', 'work/serve', 'inquire-you/your', 'the-word/thing', 'pass-over', 'be--make-well', 'the-enactment', 'and-the-enactment', 'the-judgment', 'and-the-judgment', 'the-commandment') if g in d.get('by_gloss', {})))
L('by_gloss values for the keys the chapter shares', {k: d['by_gloss'].get(k) for k in ('goad', 'and-goad', 'goad-them/their', 'the-enactment', 'and-the-enactment', 'the-judgment', 'and-the-judgment', 'the-commandment', 'be--make-well', 'hinder', 'strength', 'nose', 'glow', 'cut', 'to-set', 'the-word/thing', 'pass-over', 'to-make', 'be')})
L('by_ref keys for Deut.6', [k for k in d.get('by_ref', {}) if k.startswith('Deut.6.')]); L('by_ref total, by_gloss total', (len(d.get('by_ref', {})), len(d.get('by_gloss', {}))))
