# retype the fallen legs FROM THE PRINT (midian_legs.py's output) — each old string must occur exactly once
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
FIX = [
 ("assert morphs('Num', 31, 28)[11:13] == ['HR/Acfsa', 'HTd/Acbpa'] and words('Num', 31, 28)[10:13] == ['נפש', 'מחמש', 'המאות'] and words('Num', 31, 30)[4:8] == ['אחד', 'אחז', 'מן', 'החמשים'] and accents(byraw[('Num', 31, 28)][10]) == ['ZAQEF QATAN']",
  "assert morphs('Num', 31, 28)[10:12] == ['HR/Acfsa', 'HTd/Acbpa'] and words('Num', 31, 28)[8:12] == ['אחד', 'נפש', 'מחמש', 'המאות'] and words('Num', 31, 30)[4:8] == ['אחד', 'אחז', 'מן', 'החמשים'] and accents(byraw[('Num', 31, 28)][9]) == ['ZAQEF QATAN'] and accents(byraw[('Num', 31, 28)][10]) == ['TIPEHA']"),
 ("and words('Lev', 10, 16)[-6:-3] == ['ויקצף', 'על', 'אלעזר']", "and words('Lev', 10, 16)[words('Lev', 10, 16).index('ויקצף'):][:3] == ['ויקצף', 'על', 'אלעזר'] and words('Lev', 10, 16)[-6:-3] == ['ועל', 'איתמר', 'בני']"),
 ("assert sum(1 for v in range(1, 43) for x, _ in by[('Num', 32, v)] if re.match(r'^(ו|נ|ת)?חל(ו|)צ', x) and 'חלצה' not in x) >= 7 and U('חלציך') == ['Gen 35:11'] and words('Lev', 14, 40)[1] == 'וחלצו'",
  "assert Counter(x for v in range(1, 43) for x, _ in by[('Num', 32, v)] if x in ('נחלץ', 'תחלצו', 'חלוץ', 'חלוצים')) == Counter({'חלוץ': 3, 'חלוצים': 2, 'נחלץ': 1, 'תחלצו': 1}) and U('מחלציך') == ['Gen 35:11'] and words('Lev', 14, 40)[2] == 'וחלצו'   # the final tsadi is its own letter: 'חלוץ' is not 'חלוצ'"),
 ("and words('Judg', 8, 12)[7:12] == ['את', 'שני', 'מלכי', 'מדין', 'את']", "and words('Judg', 8, 12)[6:11] == ['את', 'שני', 'מלכי', 'מדין', 'את']"),
 ("assert words('Josh', 13, 21)[16:31] == ['ואת', 'נשיאי', 'מדין', 'את', 'אוי', 'ואת', 'רקם', 'ואת', 'צור', 'ואת', 'חור', 'ואת', 'רבע', 'נסיכי', 'סיחון']", "assert words('Josh', 13, 21)[15:30] == ['ואת', 'נשיאי', 'מדין', 'את', 'אוי', 'ואת', 'רקם', 'ואת', 'צור', 'ואת', 'חור', 'ואת', 'רבע', 'נסיכי', 'סיחון']"),
 ("and aramaic(31, 16)[4:7] == ['בעצת', 'בלעם', 'לשקרא']", "and aramaic(31, 16)[5:8] == ['בעצת', 'בלעם', 'לשקרא']"),
 ("assert words('Judg', 21, 10)[6:9] == ['שנים', 'עשר', 'אלף'] and words('Judg', 21, 11)[4:12] == ['כל', 'זכר', 'וכל', 'אשה', 'ידעת', 'משכב', 'זכר', 'תחרימו'] and words('Judg', 21, 12)[5:11] == ['ארבע', 'מאות', 'נערה', 'בתולה', 'אשר', 'לא']",
  "assert words('Judg', 21, 10)[3:6] == ['שנים', 'עשר', 'אלף'] and words('Judg', 21, 11)[4:12] == ['כל', 'זכר', 'וכל', 'אשה', 'ידעת', 'משכב', 'זכר', 'תחרימו'] and words('Judg', 21, 12)[4:10] == ['ארבע', 'מאות', 'נערה', 'בתולה', 'אשר', 'לא']"),
 ("and morphs('Num', 31, 43)[9] == 'HAcmsc'", "and morphs('Num', 31, 43)[10] == 'HAcmsc' and words('Num', 31, 43)[10] == 'שבעת'"),
 ("assert U('בדיל', books=T) == ['Num 31:22'] and U('הבדיל', books=T) == ['Deut 10:8', 'Num 16:9'] and morphs('Deut', 10, 8)[0] == 'HVhp3ms'",
  "assert U('בדיל', books=T) == [] and U('הבדיל', books=T) == ['Deut 10:8', 'Num 16:9', 'Num 31:22'] and morphs('Deut', 10, 8)[words('Deut', 10, 8).index('הבדיל')].startswith('HVh') and morphs('Num', 16, 9)[words('Num', 16, 9).index('הבדיל')].startswith('HVh') and morphs('Num', 31, 22)[10] == 'HTd/Ncmsa'   # tin only with its article; its two look-alikes the verb"),
 ("and U('וממחצית', 'ממחציתם') == ['Num 31:29', 'Num 31:42']", "and U('וממחצית', 'ממחציתם') == ['1Chr 6:55', 'Josh 21:25', 'Num 31:29', 'Num 31:42'] and U('מחצית') == ['1Kgs 16:9', 'Exod 30:13', 'Exod 38:26', 'Neh 8:3']   # the Levite cities' 'half-tribe' the homographs"),
 ("assert words('Num', 31, 28)[13:] == ['מן', 'האדם', 'ומן', 'הבקר', 'ומן', 'החמרים', 'ומן', 'הצאן']", "assert words('Num', 31, 28)[12:] == ['מן', 'האדם', 'ומן', 'הבקר', 'ומן', 'החמרים', 'ומן', 'הצאן']"),
 ("and U('צמיד', 'וצמיד') == ['Ezek 16:11', 'Ezek 23:42', 'Gen 24:22', 'Num 19:15', 'Num 31:50']", "and U('צמיד', 'וצמיד', 'צמידים', 'וצמידים') == ['Ezek 16:11', 'Ezek 23:42', 'Gen 24:22', 'Num 19:15', 'Num 31:50']"),
 ("and U('עגיל') == ['Ezek 16:12', 'Num 31:50']", "and U('עגיל', 'ועגיל', 'עגילים', 'ועגילים') == ['Ezek 16:12', 'Num 31:50']"),
 ("and aramaic(31, 52)[13] == 'סלעין' and aramaic(31, 54)[13:16] == ['למשכן', 'זמנא', 'דכרנא']", "and aramaic(31, 52)[13:15] == ['וחמשין', 'סלעין'] and aramaic(31, 54)[12:15] == ['למשכן', 'זמנא', 'דכרנא']"),
 ("assert words('Esth', 2, 22)[-5:] == ['אסתר', 'למלך', 'בשם', 'מרדכי']", "assert words('Esth', 2, 22)[-4:] == ['אסתר', 'למלך', 'בשם', 'מרדכי']"),
]
for old, new in FIX:
    assert s.count(old) == 1, (s.count(old), old[:80])
    s = s.replace(old, new)
open(p, 'w', encoding='utf-8').write(s); print('patched', len(FIX))
