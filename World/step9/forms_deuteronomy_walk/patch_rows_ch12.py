# the fourteen cut misses of the ledger writer's first run retyped from the shelf's own consonants (the FAIL print): the Name token dropped from two cuts
# (67:2-3), Jerusalem's defective spelling (68:6, 74:3), "partition" without its yod (71:12, 72:8), "common" with its vav (75:6-10), 81:5's cut moved
import os
SP = os.path.dirname(os.path.abspath(__file__))
REPL = {
 'ch12_rows_sifrei_63_67.py': [('{SP_(67, 2, "משישב", "המלך", "על", "כסא", "ה׳")}', '{SP_(67, 2, "משישב", "המלך", "על", "כסא")}'), ('{SP_(67, 3, "וה׳", "הניח", "לו", "מסביב")}', '{SP_(67, 3, "הניח", "לו", "מסביב")}')],
 'ch12_rows_sifrei_68_71.py': [('"שניה", "לענין", "ירושלים"', '"שניה", "לענין", "ירושלם"'), ('{SP_(71, 12, "כשם", "שלא", "נתנה", "תורה", "מחיצה", "בין", "צבי", "לאיל")}', '{SP_(71, 12, "כשם", "שלא", "נתנה", "תורה", "מחצה", "בין", "צבי")}')],
 'ch12_rows_sifrei_72_74.py': [('"מחיצה", "בין", "קדשים", "לקדשים"', '"מחצה", "בין", "קדשים", "לקדשים"'), ('{SP_(74, 3, "זו", "ירושלים")}', '{SP_(74, 3, "זו", "ירושלם")}')],
 'ch12_rows_sifrei_75_76.py': [('"בשחיטה", "אף", "חלין", "בשחיטה"', '"בשחיטה", "אף", "חולין", "בשחיטה"'), ('"פרט", "לחלין", "שנשחטו", "בעזרה"', '"פרט", "לחולין", "שנשחטו", "בעזרה"'), ('"בזמן", "אף", "חלין", "בזמן"', '"בזמן", "אף", "חולין", "בזמן"'), ('"ביום", "אף", "חלין", "ביום"', '"ביום", "אף", "חולין", "ביום"')],
 'ch12_rows_sifrei_77_81.py': [('({SP_(81, 5, "יש", "כן", "לעבודה", "ויש", "כן", "למתעבד")} "there is a so for the service and a so for the thing served")', '({SP_(81, 5, "בדבר", "שמקריבים", "אותו", "למזבח")} "regarding a thing that is offered on the altar")')],
}
for f, reps in REPL.items():
    p = f'{SP}/{f}'; s = open(p, encoding='utf-8').read()
    for old, new in reps:
        assert s.count(old) == 1, ('ABSENT', f, old[:60]); s = s.replace(old, new)
    open(p, 'w', encoding='utf-8').write(s)
print('patched', sum(len(v) for v in REPL.values()))
