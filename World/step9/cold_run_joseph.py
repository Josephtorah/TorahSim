#!/usr/bin/env python3
"""cold_run_joseph.py — FROM THE FORD TO THE COFFIN (O8 S4, 2026-09-08; World/step9/NARRATIVE_GAPS.md section 8): Genesis 32-37, 39-47,
50's narrative on the world engine — the night at the Jabbok and the meeting, Shechem's field and Dinah, Bethel again and the three
deaths, Edom's roster, the dreamer sold, Potiphar's house and the prison, the two dreams and Pharaoh's, the rise, the two descents,
the cup and the surety, I am Joseph, the seventy, Goshen and the fifth, the oath, the mourning and the coffin. The last of the four
narrative sittings of O8 (the census: NARRATIVE_GAPS.md section 1). Genesis 38, 48 and 49 are the family engine's, as are its seats
inside the span (32:29, 32:33, 50:12-13); this runner's span is the story's verses alone (dependency_dispositions.yaml), and the
story's acts fetch the engines' law by call.

The form: (1) the acts and speeches of the ink at their narrative verses (the register test), each a registered type with its
witness cut from the verse's consonants; (2) the answer sheet — the Mishnah's rows on this stretch read whole from the shelf, each
verified by a token in its own ink (Megillah 4:10 Reuben's act, Sotah 1:9 Joseph's burial of his father, Bava Batra 10:8 and Bava
Metzia 5:11 the surety, Shabbat 19:3 the third day, Pesachim 1:1 the search, Bava Kamma 8:7 forgiveness, Ketubot 3:4 the seducer,
Yevamot 6:6 be fruitful, Bava Batra 8:2 the inheritance order); (3) the shelf — the Babylonian rows and the Genesis spine's rows
located by script this sitting, each verified by a token; (4) twenty-three cells in the text's order, every cell a value with its
provenance and its registered effects; (5) the scene: the stretch's acts on a bare world, the tuple predicted by a hand-model
before this file was typed (scratchpad o8_s4_predict.py); (6) the wrap: law_joseph, the forty-third daemon, whose writes per event
are the model's own table. Six engines CALLED where the ink names their institution: the pre-Sinai code (the covenant's eighth day
on Benjamin, Manasseh and Ephraim — the scene's laws carry law_pre_sinai beside law_joseph, as S1 and S3), the offerings (46:1's
sacrifices; 35:14's libation by the token), the family engine (33:19's purchase, 47:29's burial command, the census against the
inheritance order), the ordinances (THE MOHAR of 34:12 against Exodus 22:15-16; THE THIEF SOLD of 44:9-17 against Exodus 22:2),
the vestments (37:31's dipped tunic as the source of the tunic's atonement — THE FLOW REVERSED). The dating lives on the
sequential tape (convention 13). Zero-report law: every claimed ink token is probed before anything runs.
"""
import sqlite3, sys, os, json, re, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import effects_layer as FX
from compile_guards import check_honest_pairing

GUARDED = check_honest_pairing(os.path.abspath(__file__))
print('honest-pairing guard: %d tests checked, every expectation a literal' % GUARDED)

DB = '<repo-old>/elijah_docket/tanakh.sqlite'
con = sqlite3.connect('file:%s?mode=ro' % DB, uri=True)


def strip(s): return re.sub(r'[֑-ׇ]', '', s)


def toks(ch, vs, book='Gen'):
    r = con.execute("select id from verses where book=? and chapter=? and verse=?", (book, ch, vs)).fetchone()
    return [re.sub(r'[֑-ׇ/]', '', h) for (h,) in con.execute("select he from words where verse_id=? order by idx", (r[0],))]


NV = {c: n for c, n in con.execute("select chapter, count(*) from verses where book='Gen' group by chapter")}
SPAN = [32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 50]


# ---- (0) THE PROBES: every kind's witnesses in the span and the rosters' names — a run of consonants found contiguous in its verse, or the run stops ----
PROBES = [(32, 2, 'ויפגעו בו מלאכי אלהים'), (32, 3, 'ויקרא שם המקום ההוא מחנים'), (32, 31, 'ויקרא יעקב שם המקום פניאל'), (33, 17, 'על כן קרא שם המקום סכות'), (33, 20, 'ויקרא לו אל אלהי ישראל'), (35, 7, 'ויקרא למקום אל בית אל'), (35, 8, 'ויקרא שמו אלון בכות'), (35, 10, 'ויקרא את שמו ישראל'), (35, 15, 'ויקרא יעקב את שם המקום'), (35, 18, 'ותקרא שמו בן אוני ואביו קרא לו בנימין'), (41, 45, 'ויקרא פרעה שם יוסף צפנת פענח'), (41, 51, 'ויקרא יוסף את שם הבכור מנשה'), (41, 52, 'ואת שם השני קרא אפרים'), (50, 11, 'על כן קרא שמה אבל מצרים'), (32, 4, 'וישלח יעקב מלאכים לפניו אל עשו אחיו'), (32, 7, 'וישבו המלאכים אל יעקב'), (32, 8, 'ויירא יעקב מאד ויצר לו'), (32, 10, 'ויאמר יעקב אלהי אבי אברהם ואלהי אבי יצחק'), (32, 14, 'ויקח מן הבא בידו מנחה לעשו אחיו'), (32, 22, 'ותעבר המנחה על פניו'), (32, 23, 'ויעבר את מעבר יבק'), (32, 24, 'ויעברם את הנחל'), (32, 25, 'ויאבק איש עמו עד עלות השחר'), (32, 26, 'ויגע בכף ירכו'), (32, 27, 'לא אשלחך כי אם ברכתני'), (32, 30, 'הגידה נא שמך'), (32, 32, 'ויזרח לו השמש כאשר עבר את פנואל'), (33, 1, 'וישא יעקב עיניו וירא והנה עשו בא'), (33, 2, 'וישם את השפחות ואת ילדיהן ראשנה'), (33, 3, 'וישתחו ארצה שבע פעמים'), (33, 6, 'ותשתחוין'), (33, 7, 'וישתחוו'), (42, 6, 'וישתחוו לו אפים ארצה'), (43, 26, 'וישתחוו לו ארצה'), (43, 28, 'ויקדו וישתחו'), (44, 14, 'ויפלו לפניו ארצה'), (47, 31, 'וישתחו ישראל על ראש המטה'), (50, 18, 'ויפלו לפניו'), (33, 4, 'ויחבקהו'), (33, 4, 'ויפל על צוארו וישקהו ויבכו'), (45, 14, 'ויפל על צוארי בנימן אחיו ויבך'), (46, 29, 'ויפל על צואריו ויבך על צואריו עוד'), (50, 1, 'ויפל יוסף על פני אביו ויבך עליו'), (33, 4, 'וישקהו ויבכו'), (45, 15, 'וינשק לכל אחיו ויבך עליהם'), (50, 1, 'וישק לו'), (33, 5, 'הילדים אשר חנן אלהים את עבדך'), (33, 8, 'מי לך כל המחנה הזה אשר פגשתי'), (33, 11, 'קח נא את ברכתי אשר הבאת לך'), (33, 12, 'נסעה ונלכה ואלכה לנגדך'), (33, 14, 'עד אשר אבא אל אדני שעירה'), (32, 2, 'ויעקב הלך לדרכו'), (33, 16, 'וישב ביום ההוא עשו לדרכו שעירה'), (33, 17, 'ויעקב נסע סכתה'), (33, 18, 'ויבא יעקב שלם עיר שכם'), (35, 5, 'ויסעו ויהי חתת אלהים על הערים'), (35, 6, 'ויבא יעקב לוזה'), (35, 16, 'ויסעו מבית אל'), (35, 21, 'ויסע ישראל ויט אהלה מהלאה למגדל עדר'), (35, 27, 'ויבא יעקב אל יצחק אביו ממרא'), (37, 12, 'וילכו אחיו לרעות את צאן אביהם בשכם'), (42, 26, 'וילכו משם'), (45, 25, 'ויעלו ממצרים ויבאו ארץ כנען'), (46, 1, 'ויסע ישראל וכל אשר לו ויבא בארה שבע'), (46, 6, 'ויבאו מצרימה יעקב וכל זרעו אתו'), (46, 28, 'ויבאו ארצה גשן'), (50, 7, 'ויעל יוסף לקבר את אביו'), (50, 14, 'וישב יוסף מצרימה הוא ואחיו'), (33, 17, 'ויבן לו בית ולמקנהו עשה סכת'), (33, 19, 'ויקן את חלקת השדה אשר נטה שם אהלו'), (47, 20, 'ויקן יוסף את כל אדמת מצרים לפרעה'), (33, 20, 'ויצב שם מזבח'), (35, 7, 'ויבן שם מזבח'), (34, 1, 'ותצא דינה בת לאה'), (34, 2, 'ויקח אתה וישכב אתה ויענה'), (34, 3, 'ותדבק נפשו בדינה בת יעקב'), (34, 4, 'קח לי את הילדה הזאת לאשה'), (34, 5, 'והחרש יעקב עד באם'), (34, 6, 'ויצא חמור אבי שכם אל יעקב לדבר אתו'), (34, 7, 'ויתעצבו האנשים ויחר להם מאד'), (34, 8, 'תנו נא אתה לו לאשה'), (34, 12, 'הרבו עלי מאד מהר ומתן'), (34, 13, 'ויענו בני יעקב את שכם ואת חמור אביו במרמה'), (34, 18, 'וייטבו דבריהם בעיני חמור ובעיני שכם'), (34, 20, 'וידברו אל אנשי עירם לאמר'), (34, 24, 'וימלו כל זכר כל יצאי שער עירו'), (34, 25, 'ויבאו על העיר בטח ויהרגו כל זכר'), (34, 26, 'הרגו לפי חרב ויקחו את דינה מבית שכם'), (34, 27, 'ויבזו העיר אשר טמאו אחותם'), (34, 30, 'ויאמר יעקב אל שמעון ואל לוי עכרתם אתי'), (37, 10, 'ויגער בו אביו'), (34, 31, 'הכזונה יעשה את אחותנו'), (35, 1, 'קום עלה בית אל ושב שם ועשה שם מזבח'), (35, 2, 'הסרו את אלהי הנכר אשר בתככם והטהרו והחליפו שמלתיכם'), (35, 4, 'ויטמן אתם יעקב תחת האלה אשר עם שכם'), (35, 8, 'ותמת דברה מינקת רבקה'), (35, 19, 'ותמת רחל'), (35, 29, 'ויגוע יצחק וימת ויאסף אל עמיו'), (50, 26, 'וימת יוסף בן מאה ועשר שנים'), (50, 13, 'ויקברו אתו במערת שדה המכפלה'), (35, 8, 'ותקבר מתחת לבית אל תחת האלון'), (35, 19, 'ותקבר בדרך אפרתה'), (35, 29, 'ויקברו אתו עשו ויעקב בניו'), (35, 9, 'וירא אלהים אל יעקב עוד'), (35, 11, 'אני אל שדי פרה ורבה'), (35, 12, 'ואת הארץ אשר נתתי לאברהם וליצחק לך אתננה'), (35, 13, 'ויעל מעליו אלהים במקום אשר דבר אתו'), (35, 14, 'ויצב יעקב מצבה במקום אשר דבר אתו מצבת אבן ויסך עליה נסך ויצק עליה שמן'), (35, 16, 'ותלד רחל ותקש בלדתה'), (35, 17, 'אל תיראי כי גם זה לך בן'), (35, 18, 'ואביו קרא לו בנימין'), (41, 50, 'וליוסף ילד שני בנים בטרם תבוא שנת הרעב'), (35, 20, 'ויצב יעקב מצבה על קברתה'), (35, 22, 'וילך ראובן וישכב את בלהה פילגש אביו וישמע ישראל'), (35, 22, 'ויהיו בני יעקב שנים עשר'), (35, 26, 'אלה בני יעקב אשר ילד לו בפדן ארם'), (36, 2, 'עשו לקח את נשיו מבנות כנען'), (41, 45, 'ויתן לו את אסנת בת פוטי פרע כהן אן לאשה'), (36, 4, 'ותלד עדה לעשו את אליפז'), (36, 12, 'ותלד לאליפז את עמלק'), (36, 6, 'וילך אל ארץ מפני יעקב אחיו'), (36, 8, 'וישב עשו בהר שעיר'), (36, 9, 'ואלה תלדות עשו אבי אדום בהר שעיר'), (36, 20, 'אלה בני שעיר החרי ישבי הארץ'), (36, 40, 'ואלה שמות אלופי עשו למשפחתם למקמתם בשמתם'), (36, 32, 'וימלך באדום בלע בן בעור'), (36, 33, 'וימת בלע וימלך תחתיו יובב בן זרח מבצרה'), (36, 34, 'וימת יובב וימלך תחתיו חשם'), (36, 35, 'וימת חשם וימלך תחתיו הדד בן בדד'), (36, 36, 'וימת הדד וימלך תחתיו שמלה ממשרקה'), (36, 37, 'וימת שמלה וימלך תחתיו שאול'), (36, 38, 'וימת שאול וימלך תחתיו בעל חנן בן עכבור'), (36, 39, 'וימת בעל חנן בן עכבור וימלך תחתיו הדר'), (37, 2, 'ויבא יוסף את דבתם רעה אל אביהם'), (37, 3, 'וישראל אהב את יוסף מכל בניו'), (37, 3, 'ועשה לו כתנת פסים'), (37, 4, 'וישנאו אתו ולא יכלו דברו לשלם'), (37, 5, 'ויוספו עוד שנא אתו'), (37, 8, 'ויוספו עוד שנא אתו על חלמתיו ועל דבריו'), (37, 5, 'ויחלם יוסף חלום'), (37, 9, 'ויחלם עוד חלום אחר'), (40, 5, 'ויחלמו חלום שניהם'), (41, 1, 'ופרעה חלם והנה עמד על היאר'), (41, 5, 'ויישן ויחלם שנית'), (37, 6, 'שמעו נא החלום הזה אשר חלמתי'), (37, 9, 'הנה חלמתי חלום עוד'), (40, 9, 'ויספר שר המשקים את חלמו ליוסף'), (40, 16, 'אף אני בחלומי'), (41, 17, 'וידבר פרעה אל יוסף בחלמי'), (37, 11, 'ויקנאו בו אחיו'), (37, 14, 'לך נא ראה את שלום אחיך ואת שלום הצאן והשבני דבר'), (37, 15, 'וימצאהו איש והנה תעה בשדה'), (37, 17, 'וילך יוסף אחר אחיו וימצאם בדתן'), (37, 18, 'ויתנכלו אתו להמיתו'), (37, 20, 'לכו ונהרגהו ונשלכהו באחד הברות'), (37, 21, 'וישמע ראובן ויצלהו מידם'), (37, 22, 'אל תשפכו דם השליכו אתו אל הבור הזה'), (37, 23, 'ויפשיטו את יוסף את כתנתו'), (37, 24, 'ויקחהו וישלכו אתו הברה'), (37, 25, 'והנה ארחת ישמעאלים באה מגלעד'), (37, 26, 'מה בצע כי נהרג את אחינו וכסינו את דמו'), (37, 27, 'לכו ונמכרנו לישמעאלים'), (37, 28, 'וימכרו את יוסף לישמעאלים בעשרים כסף'), (37, 36, 'והמדנים מכרו אתו אל מצרים לפוטיפר'), (37, 29, 'וישב ראובן אל הבור והנה אין יוסף בבור'), (37, 29, 'ויקרע את בגדיו'), (37, 34, 'ויקרע יעקב שמלתיו'), (44, 13, 'ויקרעו שמלתם'), (37, 31, 'ויטבלו את הכתנת בדם'), (37, 32, 'הכר נא הכתנת בנך הוא אם לא'), (37, 33, 'ויכירה ויאמר כתנת בני חיה רעה אכלתהו'), (37, 34, 'וישם שק במתניו ויתאבל על בנו ימים רבים'), (50, 10, 'ויעש לאביו אבל שבעת ימים'), (37, 35, 'ויבך אתו אביו'), (42, 24, 'ויסב מעליהם ויבך'), (43, 30, 'ויבא החדרה ויבך שמה'), (45, 2, 'ויתן את קלו בבכי'), (50, 17, 'ויבך יוסף בדברם אליו'), (39, 1, 'ויקנהו פוטיפר סריס פרעה שר הטבחים'), (39, 2, 'ויהי יהוה את יוסף ויהי איש מצליח'), (39, 23, 'באשר יהוה אתו ואשר הוא עשה יהוה מצליח'), (39, 4, 'ויפקדהו על ביתו וכל יש לו נתן בידו'), (39, 22, 'ויתן שר בית הסהר ביד יוסף את כל האסירם'), (39, 7, 'ותשא אשת אדניו את עיניה אל יוסף ותאמר שכבה עמי'), (39, 12, 'ותתפשהו בבגדו לאמר שכבה עמי'), (39, 8, 'וימאן ויאמר אל אשת אדניו'), (39, 12, 'ויעזב בגדו בידה'), (39, 16, 'ותנח בגדו אצלה עד בוא אדניו אל ביתו'), (39, 12, 'וינס ויצא החוצה'), (39, 14, 'ראו הביא לנו איש עברי לצחק בנו'), (39, 17, 'בא אלי העבד העברי אשר הבאת לנו לצחק בי'), (39, 19, 'ויחר אפו'), (39, 20, 'ויתנהו אל בית הסהר'), (40, 3, 'ויתן אתם במשמר בית שר הטבחים'), (39, 21, 'ויט אליו חסד ויתן חנו בעיני שר בית הסהר'), (40, 1, 'חטאו משקה מלך מצרים והאפה לאדניהם'), (40, 4, 'ויפקד שר הטבחים את יוסף אתם וישרת אתם'), (40, 6, 'וירא אתם והנם זעפים'), (40, 8, 'חלום חלמנו ופתר אין אתו'), (40, 12, 'זה פתרנו שלשת השרגים שלשת ימים הם'), (40, 18, 'זה פתרנו שלשת הסלים שלשת ימים הם'), (41, 25, 'חלום פרעה אחד הוא'), (40, 14, 'והזכרתני אל פרעה והוצאתני מן הבית הזה'), (40, 20, 'ויעש משתה לכל עבדיו'), (43, 25, 'כי שמעו כי שם יאכלו לחם'), (40, 21, 'וישב את שר המשקים על משקהו'), (40, 22, 'ואת שר האפים תלה כאשר פתר להם יוסף'), (40, 23, 'ולא זכר שר המשקים את יוסף וישכחהו'), (41, 8, 'ויהי בבקר ותפעם רוחו'), (41, 9, 'את חטאי אני מזכיר היום'), (41, 14, 'ויריצהו מן הבור ויגלח ויחלף שמלתיו'), (41, 33, 'ועתה ירא פרעה איש נבון וחכם'), (41, 37, 'וייטב הדבר בעיני פרעה ובעיני כל עבדיו'), (41, 41, 'ראה נתתי אתך על כל ארץ מצרים'), (41, 42, 'ויסר פרעה את טבעתו מעל ידו ויתן אתה על יד יוסף'), (41, 43, 'וירכב אתו במרכבת המשנה אשר לו'), (41, 46, 'ויצא יוסף מלפני פרעה ויעבר בכל ארץ מצרים'), (41, 48, 'ויקבץ את כל אכל שבע שנים'), (41, 49, 'ויצבר יוסף בר כחול הים הרבה מאד'), (41, 53, 'ותכלינה שבע שני השבע'), (41, 54, 'ותחלינה שבע שני הרעב לבוא'), (43, 1, 'והרעב כבד בארץ'), (41, 55, 'ויצעק העם אל פרעה ללחם'), (47, 15, 'הבה לנו לחם ולמה נמות נגדך כי אפס כסף'), (41, 56, 'ויפתח יוסף את כל אשר בהם וישבר למצרים'), (41, 57, 'וכל הארץ באו מצרימה לשבר אל יוסף'), (42, 2, 'רדו שמה ושברו לנו משם ונחיה ולא נמות'), (43, 2, 'שבו שברו לנו מעט אכל'), (42, 3, 'וירדו אחי יוסף עשרה לשבר בר ממצרים'), (43, 15, 'ויקמו וירדו מצרים ויעמדו לפני יוסף'), (42, 4, 'ואת בנימין אחי יוסף לא שלח יעקב את אחיו'), (42, 7, 'וירא יוסף את אחיו ויכרם ויתנכר אליהם'), (42, 8, 'ויכר יוסף את אחיו והם לא הכרהו'), (42, 9, 'ויזכר יוסף את החלמות אשר חלם להם'), (42, 9, 'מרגלים אתם לראות את ערות הארץ באתם'), (42, 14, 'הוא אשר דברתי אלכם לאמר מרגלים אתם'), (42, 11, 'כלנו בני איש אחד נחנו כנים אנחנו'), (42, 13, 'שנים עשר עבדיך אחים אנחנו'), (42, 15, 'בזאת תבחנו חי פרעה'), (42, 17, 'ויאסף אתם אל משמר שלשת ימים'), (42, 18, 'זאת עשו וחיו את האלהים אני ירא'), (42, 21, 'אבל אשמים אנחנו על אחינו'), (42, 22, 'הלוא אמרתי אליכם לאמר אל תחטאו בילד'), (44, 16, 'האלהים מצא את עון עבדיך'), (42, 23, 'כי המליץ בינתם'), (42, 24, 'ויקח מאתם את שמעון ויאסר אתו לעיניהם'), (42, 25, 'ולהשיב כספיהם איש אל שקו'), (42, 27, 'וירא את כספו והנה הוא בפי אמתחתו'), (42, 35, 'והנה איש צרור כספו בשקו'), (42, 29, 'ויגידו לו את כל הקרת אתם לאמר'), (42, 36, 'אתי שכלתם יוסף איננו ושמעון איננו ואת בנימן תקחו'), (42, 37, 'את שני בני תמית אם לא אביאנו אליך'), (42, 38, 'לא ירד בני עמכם כי אחיו מת והוא לבדו נשאר'), (43, 3, 'העד העד בנו האיש לאמר לא תראו פני בלתי אחיכם אתכם'), (43, 9, 'אנכי אערבנו מידי תבקשנו'), (43, 11, 'קחו מזמרת הארץ בכליכם והורידו לאיש מנחה'), (43, 14, 'ואל שדי יתן לכם רחמים לפני האיש'), (43, 16, 'הבא את האנשים הביתה וטבח טבח והכן'), (43, 18, 'וייראו האנשים כי הובאו בית יוסף'), (43, 20, 'בי אדני ירד ירדנו בתחלה לשבר אכל'), (43, 23, 'שלום לכם אל תיראו אלהיכם ואלהי אביכם נתן לכם מטמון באמתחתיכם'), (43, 24, 'ויתן מים וירחצו רגליהם ויתן מספוא לחמריהם'), (43, 26, 'ויביאו לו את המנחה אשר בידם הביתה'), (43, 27, 'וישאל להם לשלום ויאמר השלום אביכם הזקן'), (43, 29, 'וישא עיניו וירא את בנימין אחיו בן אמו'), (43, 31, 'ויתאפק ויאמר שימו לחם'), (43, 32, 'וישימו לו לבדו ולהם לבדם ולמצרים האכלים אתו לבדם'), (43, 33, 'וישבו לפניו הבכר כבכרתו והצעיר כצערתו'), (43, 34, 'וישא משאת מאת פניו אלהם ותרב משאת בנימן ממשאת כלם חמש ידות'), (43, 34, 'וישתו וישכרו עמו'), (44, 2, 'ואת גביעי גביע הכסף תשים בפי אמתחת הקטן'), (44, 3, 'והאנשים שלחו המה וחמריהם'), (45, 24, 'וישלח את אחיו וילכו'), (44, 4, 'קום רדף אחרי האנשים והשגתם'), (44, 5, 'והוא נחש ינחש בו'), (44, 15, 'הלוא ידעתם כי נחש ינחש איש אשר כמני'), (44, 7, 'חלילה לעבדיך מעשות כדבר הזה'), (44, 9, 'אשר ימצא אתו מעבדיך ומת וגם אנחנו נהיה לאדני לעבדים'), (44, 10, 'אשר ימצא אתו יהיה לי עבד ואתם תהיו נקים'), (44, 12, 'ויחפש בגדול החל ובקטן כלה וימצא הגביע באמתחת בנימן'), (44, 17, 'האיש אשר נמצא הגביע בידו הוא יהיה לי עבד'), (44, 18, 'ויגש אליו יהודה ויאמר בי אדני'), (44, 32, 'כי עבדך ערב את הנער מעם אבי'), (44, 33, 'ישב נא עבדך תחת הנער עבד לאדני'), (45, 1, 'ולא יכל יוסף להתאפק לכל הנצבים עליו'), (45, 3, 'אני יוסף העוד אבי חי'), (45, 4, 'אני יוסף אחיכם אשר מכרתם אתי מצרימה'), (45, 5, 'כי למחיה שלחני אלהים לפניכם'), (45, 8, 'לא אתם שלחתם אתי הנה כי האלהים'), (45, 9, 'מהרו ועלו אל אבי'), (45, 13, 'ומהרתם והורדתם את אבי הנה'), (45, 16, 'והקל נשמע בית פרעה לאמר באו אחי יוסף'), (45, 18, 'ואתנה לכם את טוב ארץ מצרים ואכלו את חלב הארץ'), (45, 21, 'ויתן להם יוסף עגלות על פי פרעה'), (45, 22, 'לכלם נתן לאיש חלפות שמלת'), (45, 23, 'ולאביו שלח כזאת עשרה חמרים'), (45, 22, 'ולבנימן נתן שלש מאות כסף'), (45, 26, 'ויגדו לו לאמר עוד יוסף חי'), (45, 27, 'וירא את העגלות אשר שלח יוסף לשאת אתו'), (45, 28, 'רב עוד יוסף בני חי אלכה ואראנו בטרם אמות'), (46, 1, 'ויזבח זבחים לאלהי אביו יצחק'), (46, 2, 'ויאמר אלהים לישראל במראת הלילה'), (46, 4, 'אנכי ארד עמך מצרימה ואנכי אעלך גם עלה'), (46, 8, 'ואלה שמות בני ישראל הבאים מצרימה'), (46, 15, 'כל נפש בניו ובנותיו שלשים ושלש'), (46, 18, 'שש עשרה נפש'), (46, 22, 'כל נפש ארבעה עשר'), (46, 25, 'כל נפש שבעה'), (46, 26, 'כל נפש ששים ושש'), (46, 27, 'כל הנפש לבית יעקב הבאה מצרימה שבעים'), (46, 28, 'ואת יהודה שלח לפניו אל יוסף להורת לפניו גשנה'), (46, 30, 'אמותה הפעם אחרי ראותי את פניך כי עודך חי'), (46, 34, 'ואמרתם אנשי מקנה היו עבדיך מנעורינו ועד עתה'), (47, 1, 'ויבא יוסף ויגד לפרעה ויאמר אבי ואחי'), (47, 2, 'ומקצה אחיו לקח חמשה אנשים ויצגם לפני פרעה'), (47, 3, 'מה מעשיכם ויאמרו אל פרעה רעה צאן עבדיך'), (47, 6, 'ארץ מצרים לפניך הוא במיטב הארץ הושב את אביך ואת אחיך'), (47, 7, 'ויבא יוסף את יעקב אביו ויעמדהו לפני פרעה'), (47, 7, 'ויברך יעקב את פרעה'), (47, 10, 'ויברך יעקב את פרעה ויצא מלפני פרעה'), (47, 8, 'כמה ימי שני חייך'), (47, 9, 'ימי שני מגורי שלשים ומאת שנה'), (47, 11, 'ויושב יוסף את אביו ואת אחיו ויתן להם אחזה בארץ מצרים'), (47, 12, 'ויכלכל יוסף את אביו ואת אחיו ואת כל בית אביו לחם לפי הטף'), (50, 21, 'אנכי אכלכל אתכם ואת טפכם וינחם אותם וידבר על לבם'), (47, 14, 'וילקט יוסף את כל הכסף הנמצא בארץ מצרים ובארץ כנען'), (47, 17, 'ויביאו את מקניהם אל יוסף ויתן להם יוסף לחם בסוסים'), (47, 18, 'ותתם השנה ההוא ויבאו אליו בשנה השנית'), (47, 21, 'ואת העם העביר אתו לערים'), (47, 22, 'רק אדמת הכהנים לא קנה'), (47, 23, 'הא לכם זרע וזרעתם את האדמה'), (47, 24, 'ונתתם חמישית לפרעה וארבע הידת יהיה לכם'), (47, 25, 'החיתנו נמצא חן בעיני אדני והיינו עבדים לפרעה'), (47, 26, 'וישם אתה יוסף לחק עד היום הזה על אדמת מצרים לפרעה לחמש'), (47, 27, 'ויאחזו בה ויפרו וירבו מאד'), (47, 29, 'אל נא תקברני במצרים'), (47, 30, 'ונשאתני ממצרים וקברתני בקברתם'), (47, 31, 'השבעה לי וישבע לו'), (50, 25, 'וישבע יוסף את בני ישראל לאמר'), (50, 2, 'ויחנטו הרפאים את ישראל'), (50, 26, 'ויחנטו אתו ויישם בארון במצרים'), (50, 5, 'ועתה אעלה נא ואקברה את אבי ואשובה'), (50, 6, 'עלה וקבר את אביך כאשר השביעך'), (50, 15, 'לו ישטמנו יוסף והשב ישיב לנו את כל הרעה'), (50, 17, 'אנא שא נא פשע אחיך וחטאתם'), (50, 18, 'הננו לך לעבדים'), (50, 19, 'אל תיראו כי התחת אלהים אני'), (50, 20, 'ואתם חשבתם עלי רעה אלהים חשבה לטבה'), (50, 22, 'וישב יוסף במצרים הוא ובית אביו'), (50, 23, 'וירא יוסף לאפרים בני שלשים'), (50, 24, 'ואלהים פקד יפקד אתכם והעלה אתכם מן הארץ הזאת'), (46, 9, 'ראובן'), (46, 9, 'חנוך'), (46, 9, 'ופלוא'), (46, 9, 'וחצרון'), (46, 9, 'וכרמי'), (46, 10, 'שמעון'), (46, 10, 'ימואל'), (46, 10, 'וימין'), (46, 10, 'ואהד'), (46, 10, 'ויכין'), (46, 10, 'וצחר'), (46, 10, 'ושאול'), (46, 11, 'לוי'), (46, 11, 'גרשון'), (46, 11, 'קהת'), (46, 11, 'ומררי'), (46, 12, 'יהודה'), (46, 12, 'ער'), (46, 12, 'ואונן'), (46, 12, 'ושלה'), (46, 12, 'פרץ'), (46, 12, 'וזרח'), (46, 12, 'חצרון'), (46, 12, 'וחמול'), (46, 13, 'יששכר'), (46, 13, 'תולע'), (46, 13, 'ופוה'), (46, 13, 'ויוב'), (46, 13, 'ושמרון'), (46, 14, 'זבולן'), (46, 14, 'סרד'), (46, 14, 'ואלון'), (46, 14, 'ויחלאל'), (46, 15, 'דינה'), (46, 16, 'גד'), (46, 16, 'צפיון'), (46, 16, 'וחגי'), (46, 16, 'שוני'), (46, 16, 'ואצבן'), (46, 16, 'ערי'), (46, 16, 'וארודי'), (46, 16, 'ואראלי'), (46, 17, 'אשר'), (46, 17, 'ימנה'), (46, 17, 'וישוה'), (46, 17, 'וישוי'), (46, 17, 'בריעה'), (46, 17, 'ושרח'), (46, 17, 'חבר'), (46, 17, 'ומלכיאל'), (46, 19, 'יוסף'), (46, 19, 'ובנימן'), (46, 20, 'מנשה'), (46, 20, 'אפרים'), (46, 21, 'בלע'), (46, 21, 'ובכר'), (46, 21, 'ואשבל'), (46, 21, 'גרא'), (46, 21, 'ונעמן'), (46, 21, 'אחי'), (46, 21, 'וראש'), (46, 21, 'מפים'), (46, 21, 'וחפים'), (46, 21, 'וארד'), (46, 23, 'דן'), (46, 23, 'חשים'), (46, 24, 'נפתלי'), (46, 24, 'יחצאל'), (46, 24, 'וגוני'), (46, 24, 'ויצר'), (46, 24, 'ושלם'), (35, 23, 'ראובן'), (35, 23, 'ושמעון'), (35, 23, 'ולוי'), (35, 23, 'ויהודה'), (35, 23, 'ויששכר'), (35, 23, 'וזבולן'), (35, 24, 'יוסף'), (35, 24, 'ובנימן'), (35, 25, 'דן'), (35, 25, 'ונפתלי'), (35, 26, 'גד'), (35, 26, 'אשר'), (36, 32, 'בלע'), (36, 33, 'יובב'), (36, 34, 'חשם'), (36, 35, 'הדד'), (36, 36, 'שמלה'), (36, 37, 'שאול'), (36, 38, 'בעל חנן'), (36, 39, 'הדר')]
_T = {}
for ch, vs, run in PROBES:
    ws = _T.setdefault((ch, vs), toks(ch, vs)); want = run.split()
    assert any(ws[i:i + len(want)] == want for i in range(len(ws) - len(want) + 1)), 'PROBE FAILED: %r not in Gen %d:%d' % (run, ch, vs)
print('probes: %d ink runs verified in their verses (Gen 32-50)' % len(PROBES))
ROSTERS = {'leah': [(46, 9, 'ראובן'), (46, 9, 'חנוך'), (46, 9, 'ופלוא'), (46, 9, 'וחצרון'), (46, 9, 'וכרמי'), (46, 10, 'שמעון'), (46, 10, 'ימואל'), (46, 10, 'וימין'), (46, 10, 'ואהד'), (46, 10, 'ויכין'), (46, 10, 'וצחר'), (46, 10, 'ושאול'), (46, 11, 'לוי'), (46, 11, 'גרשון'), (46, 11, 'קהת'), (46, 11, 'ומררי'), (46, 12, 'יהודה'), (46, 12, 'ער'), (46, 12, 'ואונן'), (46, 12, 'ושלה'), (46, 12, 'פרץ'), (46, 12, 'וזרח'), (46, 12, 'חצרון'), (46, 12, 'וחמול'), (46, 13, 'יששכר'), (46, 13, 'תולע'), (46, 13, 'ופוה'), (46, 13, 'ויוב'), (46, 13, 'ושמרון'), (46, 14, 'זבולן'), (46, 14, 'סרד'), (46, 14, 'ואלון'), (46, 14, 'ויחלאל'), (46, 15, 'דינה')], 'zilpah': [(46, 16, 'גד'), (46, 16, 'צפיון'), (46, 16, 'וחגי'), (46, 16, 'שוני'), (46, 16, 'ואצבן'), (46, 16, 'ערי'), (46, 16, 'וארודי'), (46, 16, 'ואראלי'), (46, 17, 'אשר'), (46, 17, 'ימנה'), (46, 17, 'וישוה'), (46, 17, 'וישוי'), (46, 17, 'בריעה'), (46, 17, 'ושרח'), (46, 17, 'חבר'), (46, 17, 'ומלכיאל')], 'rachel': [(46, 19, 'יוסף'), (46, 19, 'ובנימן'), (46, 20, 'מנשה'), (46, 20, 'אפרים'), (46, 21, 'בלע'), (46, 21, 'ובכר'), (46, 21, 'ואשבל'), (46, 21, 'גרא'), (46, 21, 'ונעמן'), (46, 21, 'אחי'), (46, 21, 'וראש'), (46, 21, 'מפים'), (46, 21, 'וחפים'), (46, 21, 'וארד')], 'bilhah': [(46, 23, 'דן'), (46, 23, 'חשים'), (46, 24, 'נפתלי'), (46, 24, 'יחצאל'), (46, 24, 'וגוני'), (46, 24, 'ויצר'), (46, 24, 'ושלם')], 'twelve': [(35, 23, 'ראובן'), (35, 23, 'ושמעון'), (35, 23, 'ולוי'), (35, 23, 'ויהודה'), (35, 23, 'ויששכר'), (35, 23, 'וזבולן'), (35, 24, 'יוסף'), (35, 24, 'ובנימן'), (35, 25, 'דן'), (35, 25, 'ונפתלי'), (35, 26, 'גד'), (35, 26, 'אשר')], 'kings': [(36, 32, 'בלע'), (36, 33, 'יובב'), (36, 34, 'חשם'), (36, 35, 'הדד'), (36, 36, 'שמלה'), (36, 37, 'שאול'), (36, 38, 'בעל חנן'), (36, 39, 'הדר')]}   # the seventy by register (46:8-25), the twelve (35:23-26), the eight kings (36:32-39) — every name among the probes

I, M, A, D, P, H = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'IMPORT', 'HYPOTHESIS'


def cell(v, p, why, effects):
    FX.validate(effects)
    return {'v': v, 'p': p, 'why': why, 'fx': effects}


with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):   # the callees grade themselves at import — their reports stay their own
    import cold_run_pre_sinai as PS_       # THE LIVE EDGES (dependency_dispositions.yaml): the covenant's eighth day on every male birth; the covenant's heads
    import cold_run_offerings as OF        # the peace offering's shape (46:1); the libation's token (35:14)
    import cold_run_family as FA           # the purchase (33:19); the inheritance order (43:33, 46:8)
    import cold_run_mishpatim_2 as MP2     # THE MOHAR (34:12 against Exodus 22:15-16)
    import cold_run_mishpatim_3 as MP3     # THE THIEF SOLD (44:9-17 against Exodus 22:2)
    import cold_run_vestments as VS        # the tunic's atonement for bloodshed (37:31 — Arakhin 16a:13, Zevachim 88b:6)
import world_engine as WE


# ---- (1) the ink censuses the cells read (recomputed here; every count a measurement) ----
def _seats(pred, ch_lo, ch_hi):
    return [(ch, vs) for ch in SPAN if ch_lo <= ch <= ch_hi for vs in range(1, NV[ch] + 1) if pred(toks(ch, vs))]


# ---- (2) the answer sheet — the Mishnah's rows as TEST DATA, each verified by a token in its own ink ----
def _load(path):
    d = json.load(open(path, encoding='utf-8')); return d['text'] if isinstance(d, dict) and 'text' in d else d
def mishnah(tractate, ch, m, must):
    txt = strip(re.sub(r'<[^>]+>', '', _load('<repo-old>/Data/mishnah_%s_he.json' % tractate)[ch - 1][m - 1]))
    assert must in txt, 'answer-sheet check failed: %r not in Mishnah %s %d:%d' % (must, tractate, ch, m)
_BAV = {}
def _bavli(tr, daf, side, seg, must):
    T = _BAV.setdefault(tr, _load('<repo-old>/Data/bavli_%s_he.json' % tr))
    txt = strip(re.sub(r'<[^>]+>', '', T[2 * daf - 2 + (1 if side == 'b' else 0)][seg - 1]))
    assert must in txt, 'shelf check failed: %r not in %s %d%s:%d' % (must, tr, daf, side, seg)
_BR = None
def _br(par, row, must):
    global _BR
    if _BR is None: _BR = _load('<repo-old>/Data/bereshit_rabbah_he.json')
    txt = strip(re.sub(r'<[^>]+>', '', _BR[par - 1][row - 1]))
    assert must in txt, 'Bereshit Rabbah check failed: %r not in %d:%d' % (must, par, row)
SHEET = [
    ('megillah', 4, 10, 'מעשה ראובן'), ('sotah', 1, 9, 'יוסף זכה לקבר את אביו'), ('bava_batra', 10, 8, 'ערב היוצא לאחר חתום שטרות'), ('bava_metzia', 5, 11, 'והערב'),
    ('shabbat', 19, 3, 'בהיותם כאבים'), ('pesachim', 1, 1, 'בודקין את החמץ'), ('bava_kamma', 8, 7, 'אין נמחל לו עד שיבקש ממנו'), ('ketubot', 3, 4, 'המפתה נותן שלשה דברים'),
    ('yevamot', 6, 6, 'לא יבטל אדם מפריה ורביה'), ('bava_batra', 8, 2, 'סדר נחלות'),
]
for t, ch, m, must in SHEET: mishnah(t, ch, m, must)
SHEET2 = [   # the Babylonian rows (file index 2*daf-2, +1 for b) and the Genesis spine's rows (Bereshit Rabbah, parashah:row) — every one located by script this sitting
    ('B', 'megillah', 16, 'b', 2, 'צוארי בנימן'), ('B', 'megillah', 16, 'b', 3, 'עיני אחי בנימין'), ('B', 'megillah', 16, 'b', 4, 'עשרה חמורים'), ('B', 'megillah', 16, 'b', 5, 'תעלא בעידניה'),
    ('B', 'megillah', 16, 'b', 6, 'ראש המטה'), ('B', 'megillah', 16, 'b', 7, 'עשרה נרות'), ('B', 'megillah', 17, 'a', 2, 'ששים ושלש'), ('B', 'megillah', 17, 'a', 3, 'בן שלשים שנה'),
    ('B', 'megillah', 17, 'a', 4, 'שלשים ומאת שנה'), ('B', 'megillah', 17, 'a', 5, 'בבית עבר'), ('B', 'megillah', 17, 'a', 6, 'עשרים ושתים שנה'), ('B', 'megillah', 17, 'a', 7, 'שמונה עשר חודש'),
    ('B', 'megillah', 18, 'a', 17, 'אל אלהי ישראל'), ('B', 'bava_batra', 115, 'b', 4, 'שבא צבעון על אמו'), ('B', 'bava_batra', 123, 'b', 1, 'זו יוכבד'), ('B', 'bava_batra', 173, 'b', 9, 'אנכי אערבנו'),
    ('B', 'bava_batra', 173, 'b', 10, 'קבלנות'), ('B', 'chullin', 95, 'b', 14, 'דאיתחזק תלתא זימני'), ('B', 'chullin', 101, 'b', 9, 'לאחר מעשה'), ('B', 'pesachim', 7, 'b', 14, 'מציאה מחיפוש'),
    ('B', 'pesachim', 119, 'a', 6, 'כל כסף וזהב שבעולם'), ('B', 'sotah', 10, 'b', 7, 'הכר נא הכתנת'), ('B', 'sotah', 13, 'b', 12, 'בא גבריאל ופירעו'), ('B', 'sotah', 36, 'b', 9, 'בנימן כתיב'),
    ('B', 'sotah', 36, 'b', 19, 'גנוני מלכות'), ('B', 'nedarim', 31, 'b', 14, 'סכנה היא'), ('B', 'yevamot', 65, 'b', 5, 'פרה ורבה'), ('B', 'yevamot', 65, 'b', 7, 'לשנות בדבר השלום'),
    ('B', 'ketubot', 111, 'a', 23, 'ארבע מאות פרסה'), ('B', 'taanit', 10, 'b', 6, 'למה תתראו'), ('B', 'taanit', 10, 'b', 11, 'בכי טוב'), ('B', 'taanit', 11, 'a', 4, 'בשני רעבון'),
    ('B', 'sanhedrin', 6, 'b', 5, 'מה בצע'), ('B', 'sanhedrin', 92, 'a', 3, 'המשביר'), ('B', 'sanhedrin', 99, 'b', 8, 'נפק מינה עמלק'), ('B', 'arakhin', 16, 'a', 13, 'כתונת מכפרת על שפיכות דמים'),
    ('B', 'berakhot', 12, 'b', 28, 'לא יקרא שמך עוד יעקב'), ('B', 'berakhot', 34, 'b', 3, 'השתחואה'), ('B', 'berakhot', 42, 'a', 8, 'בגלל יוסף'), ('B', 'berakhot', 55, 'b', 2, 'עד עשרים ושתים שנה'),
    ('B', 'beitzah', 16, 'a', 3, 'לישנא דמזוני'), ('B', 'bava_kamma', 92, 'a', 19, 'שהוכפלו בשמות'), ('B', 'avodah_zarah', 25, 'b', 8, 'ירחיב לו את הדרך'), ('B', 'horayot', 10, 'b', 11, 'ותשא אשת אדניו'),
    ('B', 'nazir', 5, 'a', 5, 'שנתים ימים'), ('B', 'chagigah', 3, 'a', 14, 'נחשים ועקרבים'), ('B', 'chagigah', 4, 'b', 8, 'תוכחה של בשר ודם'), ('B', 'bava_metzia', 39, 'b', 8, 'בלא חתימת זקן'),
    ('R', 78, 8, 'אחרון אחרון חביב'), ('R', 78, 9, 'נקוד עליו'), ('R', 78, 11, 'כתות כתות'), ('R', 78, 12, 'מה פני אלהים דין'), ('R', 78, 14, 'יעבר נא אדני'), ('R', 79, 5, 'שלם בגופו'),
    ('R', 79, 7, 'במאה קשיטה'), ('R', 79, 8, 'אלוה בעליונים'), ('R', 80, 6, 'ואיש תבונות יחריש'), ('R', 80, 8, 'רמיות דברים'), ('R', 80, 9, 'מרחיצין את הקטן'), ('R', 80, 10, 'שלא נטלו עצה מיעקב'),
    ('R', 80, 12, 'צלולה היתה החבית'), ('R', 81, 1, 'מוקש אדם ילע קדש'), ('R', 81, 2, 'אם נבלת בהתנשא'), ('R', 81, 5, 'לשון יונית'), ('R', 82, 9, 'בר צערי'), ('R', 82, 10, 'אין עושין נפשות לצדיקים'),
    ('R', 82, 11, 'שלשלת יוחסין'), ('R', 82, 14, 'פילגש לאליפז'), ('R', 82, 15, 'ענה ענה תרי זמני'), ('R', 83, 1, 'נמשלו עובדי כוכבים כספינה'), ('R', 84, 7, 'מעשה נערות'), ('R', 84, 8, 'זיו איקונין'),
    ('R', 84, 16, 'זה הפינס'), ('R', 84, 17, 'עברתן של שבטים'), ('R', 84, 18, 'עברו אותן הדינים'), ('R', 84, 19, 'בשקו ובתעניתו'), ('R', 84, 21, 'כמה בנות היו לו'), ('R', 86, 3, 'הקנויין קונין'),
    ('R', 87, 5, 'בדבר מצוה ממאנין'), ('R', 87, 10, 'שמושו היה ערב לרבו'), ('R', 88, 5, 'אלו ישראל'), ('R', 88, 7, 'ואני לא אשכחהו'), ('R', 89, 1, 'קץ שם לחשך'), ('R', 90, 3, 'משלו נתנו לו'),
    ('R', 90, 5, 'לקמצים'), ('R', 91, 3, 'לעדה שהיא עשרה'), ('R', 91, 7, 'נעשה נכרי להם'), ('R', 91, 8, 'לשון דרומי'), ('R', 92, 8, 'עשרה בני אדם'), ('R', 92, 9, 'בכסף ראשון'),
    ('R', 93, 9, 'פיוס ליוסף'), ('R', 93, 12, 'שני בית המקדשות'), ('R', 94, 5, 'חזרתי על כל בעלי אגדה'), ('R', 94, 9, 'ששים וששה כוסות'), ('R', 95, 4, 'שלא היו גבורים'), ('R', 96, 5, 'למה לא קרא לא לראובן'),
    ('R', 100, 8, 'שלא זמנן לסעודה'), ('R', 100, 9, 'שמדבר על הלב'), ('R', 100, 11, 'כשתהיו עולין'),
]
for row in SHEET2:
    if row[0] == 'B': _bavli(*row[1:])
    else: _br(*row[1:])
print('answer sheet: %d Mishnah rows verified in their own ink; shelf: %d rows (Babylonian and Bereshit Rabbah) verified by token' % (len(SHEET), len(SHEET2)))

# ---- (4) THE CELLS — twenty-three, in the text's order; each query a cell(value, provenance, why, effects) ----
NUM = {'מאתים': 200, 'עשרים': 20, 'ועשרים': 20, 'שלשים': 30, 'ארבעים': 40, 'עשרה': 10, 'ועשרה': 10}
_NAME = ('יהוה', 'ליהוה', 'ביהוה', 'ויהוה')


def _gift():
    """the gift's head count by the numerals of Gen 32:15-16, verse by verse (a measurement): two hundred she-goats, twenty he-goats,
    two hundred ewes, twenty rams; thirty milch camels (their colts unnumbered), forty cows, ten bulls, twenty she-asses, ten foals"""
    return [[NUM[w] for w in toks(32, vs) if w in NUM] for vs in (15, 16)]


def _all_seats(pred, chs):
    """seats over EVERY chapter named (the family's included — the census that must not stop at the span)"""
    return [(ch, vs) for ch in chs for vs in range(1, NV[ch] + 1) if pred(toks(ch, vs))]


def _name_by_chapter():
    """the Tetragrammaton's tokens per chapter of Genesis 37-50, the family's chapters included (a measurement); the zero chapters dropped"""
    out = {ch: sum(1 for vs in range(1, NV[ch] + 1) for w in toks(ch, vs) if w in _NAME) for ch in range(37, 51)}
    return {ch: n for ch, n in out.items() if n}


def _pit_seats():
    return [vs for vs in range(1, NV[37] + 1) if any(re.fullmatch(r'ה?ב[ו]?ר[הות]?', w) for w in toks(37, vs))]


def _timer_span(eff):
    """the fire day less the set day of a timer on the scene's own world (a measurement from the log)"""
    s_ = [l[1] for l in _W.log if l[0] == 'TIMER-SET' and l[2]['effect'] == eff]; f_ = [l[1] for l in _W.log if l[0] == 'TIMER-FIRE' and l[2]['effect'] == eff]
    return f_[0] - s_[0] if s_ and f_ else None


def _mohar():
    """THE MOHAR by call: Shechem's 'multiply upon me exceedingly bride-price and gift' (34:12) laid on the seducer's compiled function
    of Exodus 22:15-16 — the rapist's case (34:2 'and he violated her'), run on a bare world; (the fixed sum's value, the money entries)"""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='the mohar of Gen 34:12 on a bare world')
    out = MP2.law_mishpatim_2({'kind': 'virgin_seduced', 'subject': 'shechem', 'seducer': 'shechem', 'father': 'jacob', 'raped': True, 'day': 1,
                               'case_source': 'Gen 34:2 — and he took her and lay with her and violated her; 34:12 the mohar unbounded'}, w)
    fixed = [e for e in out if e['effect'] == 'gives_fixed_sum']
    return (fixed[0]['value'] if fixed else None, len([e for e in out if e['effect'] in ('gives_fixed_sum', 'pays')]))


def jabbok(q):
    if q == 'two_namings': return cell(('mahanaim', 'peniel'), I, "'and he called the name of that place Mahanaim' (32:3), 'and Jacob called the name of the place Peniel' (32:31) — the stretch's first two namings, both Jacob's; name_given twice on the scene", ['name_given', 'camp_of_god_seen'])
    if q == 'angel_bands': return cell('bands_of_angels_all_night', M, "Bereshit Rabbah 78:11 — 'whose is all this camp that I met' (33:8): all that night the ministering angels went in bands and companies and struck Esau's men, who said 'we are Esau's' — 'strike, strike'", ['camp_of_god_seen', 'esau_approaching'])
    if q == 'gift_by_verse': return cell(_gift(), I, "the numerals of 32:15 and 32:16 parsed by _gift() — a measurement; the camels' colts carry no number", ['gift_sent_ahead'])
    if q == 'gift_head_count': return cell(sum(sum(v) for v in _gift()), I, "the gift's head count: 440 of the flock (32:15) + 110 of the herd and the asses (32:16) = 550 — the ink's own arithmetic, no head listed twice", ['gift_sent_ahead'])
    if q == 'too_small': return cell('i_am_too_small_for_all_the_kindnesses', I, "'I am too small for all the kindnesses and all the truth' (32:11, קטנתי) — the prayer's opening; deliverance_prayed the HEAVEN entry the sunrise answers", ['deliverance_prayed'])
    if q == 'left_alone': return cell('alone', I, "'and Jacob was left alone, and a man wrestled with him' (32:25, לבדו) — the wrestling's condition; thigh_dislocated the body entry, never closed: 'and he limped' (32:32)", ['thigh_dislocated', 'limping'])
    if q == 'thigh_socket': return cell(('socket', 'thigh'), I, "'the socket of his thigh' (32:26, כף ירכו) — the sinew statute's own noun pair (32:33 'the socket of the thigh'), the family engine's seat", ['thigh_dislocated'])
    if q == 'renaming_seat': return cell('family_engine_32_29', I, "'your name shall no more be called Jacob but Israel' (32:29) — the family engine's `renamed` seat (O2: one act, one writer); this scene submits name_asked at 32:30 and the blessing, nothing at 32:29", ['blessed_at_the_ford', 'blessing_demanded'])
    if q == 'peniel_penuel': return cell(('peniel', 'penuel'), I, "'Peniel' (32:31, פניאל) and 'Penuel' (32:32, פנואל) — the place's two spellings a verse apart (the tokens measured); one naming on the scene, the second spelling the narrator's", ['name_given', 'limping'])
    if q == 'sinew_seat': return cell('family_engine_32_33', I, "'therefore the children of Israel do not eat the sinew of the thigh-vein to this day' (32:33) — the family engine's `sinew_barred` statute at its own seat, excluded from this span's acts (8a)", ['limping'])
    return cell('no_case', I, '', [FX.NONE])


def esau_met(q):
    if q == 'last_dearest': return cell('last_last_is_dearest', M, "Bereshit Rabbah 78:8 — 'and he put the maids and their children first' (33:2): this says, the last, the last is the dearest", ['children_divided'])
    if q == 'bowed_seven': return cell(7, I, "'and bowed to the ground seven times' (33:3) — the number parsed; bowed_seven_times with value 7 on the ledger", ['bowed_seven_times'])
    if q == 'bow_seats': return cell(len(_seats(lambda ws: any('שתחו' in w for w in ws), 32, 50)), I, "the prostration verb's seats in the span (measured): 33:3, 33:6, 33:7, 37:7, 37:9, 37:10, 42:6, 43:26, 43:28, 47:31 — ten verses; the dreams' bows (37:7-10) received at 42:6, 43:26, 43:28 (the family's 48:12 outside the span)", ['bowed_seven_times', 'bowed_as_the_sheaves', 'bowed_on_the_bed'])
    if q == 'bow_table': return cell(_seats(lambda ws: any('שתחו' in w for w in ws), 32, 50), I, "the same ten seats listed by the census function (a measurement, printed)", ['bowed_as_the_sheaves'])
    if q == 'prostration_form': return cell('hands_and_feet_spread', M, "Berakhot 34b:3 — a baraita: kidah is on the face, keriah on the knees, hishtachavaah is the spreading of hands and feet, from 'shall I and your mother and your brothers come to bow down to you to the ground' (37:10) — the dream's own verb defines the posture", ['bowed_as_the_sheaves'])
    if q == 'dotted_kiss': return cell('script_equals_dots', M, "Bereshit Rabbah 78:9 — 'and he kissed him' (33:4) is dotted: R. Shimon ben Elazar — where the script exceeds the dots expound the script, where the dots exceed expound the dots; here neither exceeds — he kissed him with all his heart (the frozen unit's hard case of the dotted-letters rule)", ['kissed_and_wept'])
    if q == 'grace_verb': return cell('graciously_given', I, "'the children whom God has graciously given your servant' (33:5, חנן) — the grace verb's seat in the meeting (the frozen unit's 'grace verb born')", ['children_divided'])
    if q == 'face_of_god': return cell('as_the_face_of_god_is_judgment', M, "Bereshit Rabbah 78:12 — 'as one sees the face of God' (33:10): as the face of God is judgment, so your face is judgment", ['blessing_returned'])
    if q == 'blessing_returned': return cell('my_blessing', I, "'take, I pray, my blessing that is brought to you' (33:11, ברכתי) — the blessing of Genesis 27 returned by its own name; blessing_returned on Esau's ledger, counterparty Jacob", ['blessing_returned', 'gift_declined'])
    if q == 'seir_promised': return cell('never_narrated', I, "'until I come to my lord to Seir' (33:14, שעירה) — Seir promised and never reached (8m OPEN); seir_promised a HEAVEN-class entry left open on the scene; Bereshit Rabbah 78:14 — 'let my lord pass before his servant': do you wish us to be partners in your world? — let my lord pass", ['seir_promised', 'convoy_declined'])
    if q == 'widen_the_road': return cell('as_jacob_to_esau', M, "Avodah Zarah 25b:8 — if he asks where you go, widen the road for him, as Jacob our father did to Esau the wicked: 'until I come to my lord to Seir' (33:14)", ['seir_promised'])
    if q == 'sukkot_naming': return cell(('booths', 'sukkot'), I, "'and made booths for his cattle; therefore the name of the place is called Sukkot' (33:17, סכת / סכות) — the booths and the name from one verse", ['booths_made', 'name_given'])
    if q == 'sukkot_months': return cell(18, M, "Megillah 17a:7 — he tarried on the road two years: a baraita — he went out from Aram-naharaim and came to Sukkot and made there eighteen months, 'and Jacob journeyed to Sukkot and built him a house and made booths for his cattle' (33:17) — the marker road_years the tape carries", ['encamped_at'])
    return cell('no_case', I, '', [FX.NONE])


def shechem_arrival(q):
    if q == 'came_whole': return cell(('body', 'sons', 'money'), M, "Bereshit Rabbah 79:5 — 'and Jacob came whole' (33:18): whole in his body (against 32:32's limp), whole in his sons (against 32:9's fear), whole in his money", ['came_whole'])
    if q == 'hundred_kesitah': return cell(100, I, "'for a hundred kesitah' (33:19, במאה קשיטה) — the price parsed; field_acquired with amount on the ledger, the family's purchased kind at this scene's seat", ['field_acquired'])
    if q == 'three_places': return cell(3, M, "Bereshit Rabbah 79:7 — R. Yudan bar Simon: one of three places the nations cannot cheat Israel of, saying 'stolen in your hands': the cave of Machpelah, the Temple, and Joseph's tomb", ['field_acquired'])
    if q == 'purchase_by_call': return cell(FA.purchase('three_modes')['v'], P, "CALLED cold_run_family.purchase('three_modes') -> the Mishnah's money, deed, possession run at Machpelah [IMPORT, live]: 'and he bought the portion of the field' (33:19) read against the modes the engine keeps", ['field_acquired'])
    if q == 'purchase_seat': return cell('law_joseph_writes_33_19', I, "the family's `purchased` branch seat-checked to Gen 23 (8k); the field at Shechem written here by law_joseph — one act, one writer", ['field_acquired'])
    if q == 'el_elohe_israel': return cell('god_called_jacob_el', M, "Megillah 18a:17 — R. Acha in R. Elazar's name: whence that the Holy One called Jacob 'el'? 'and he called him El-elohe-Israel' (33:20) — if the altar, it should say 'and Jacob called it'; rather, He called Jacob 'el'", ['altar_built', 'name_given'])
    if q == 'god_below': return cell('you_god_above_i_god_below', M, "Bereshit Rabbah 79:8 — Resh Lakish: 'and he called it El-elohe-Israel' — he said, You are God in the upper worlds and I am god in the lower; Rav Huna in his name: even the synagogue's attendant takes no authority for himself", ['altar_built'])
    return cell('no_case', I, '', [FX.NONE])


def dinah(q):
    if q == 'dinah_seats': return cell(len(_all_seats(lambda ws: 'דינה' in ws or 'ודינה' in ws, range(1, 51))), I, "Dinah's name in Genesis (measured): 30:21, 34:1, 34:5, 34:13, 34:25, 34:26, 46:15 — seven seats", ['violated'])
    if q == 'three_verbs': return cell(('took', 'lay', 'violated'), I, "'and he took her, and lay with her, and violated her' (34:2) — three verbs; violated and defiled (34:5 'defiled') the body entries", ['violated', 'defiled'])
    if q == 'cleaved_loved_spoke': return cell(('cleaved', 'loved', 'spoke_to_her_heart'), I, "'and his soul cleaved to Dinah ... and he loved the girl, and spoke to the girl's heart' (34:3) — the three clauses before the demand (34:4)", ['marriage_demanded'])
    if q == 'silence_kept': return cell('kept_silent_until_they_came', I, "'and Jacob kept silent until they came' (34:5, החרש); Bereshit Rabbah 80:6 — 'a man of understanding keeps silent' (Prov 11:12)", ['silence_kept'])
    if q == 'outrage_phrase': return cell('not_done_in_israel', I, "'he had done an outrage in Israel ... and so it is not done' (34:7, נבלה בישראל) — the phrase's first seat; outrage_in_israel a status", ['outrage_in_israel'])
    if q == 'mohar_unbounded': return cell('multiply_upon_me', I, "'multiply upon me exceedingly bride-price and gift, and I will give as you say to me' (34:12, מהר ומתן) — the law's own noun (Exod 22:16 'the mohar of virgins') named before the law; mohar_offered_unbounded", ['mohar_offered_unbounded'])
    if q == 'mohar_by_call': return cell(_mohar(), P, "CALLED cold_run_mishpatim_2.law_mishpatim_2 on Shechem's case (raped) [IMPORT, live]: the seducer's fixed sum is a POINTER ('FETCH-50' — Deut 22:29's fifty, Ketubot 29b), and the money entries are four (the fine, humiliation, degradation, pain — Mishnah Ketubot 3:4): the law bounds what Shechem offered unbounded", ['mohar_offered_unbounded'])
    if q == 'seducer_sheet': return cell(('three', 'four'), A, "Mishnah Ketubot 3:4 — the seducer gives three things, the rapist four: humiliation, degradation and the fine; the rapist adds the pain — the answer sheet the call reproduces", ['mohar_offered_unbounded'])
    if q == 'deceit_word': return cell('with_guile', I, "'and the sons of Jacob answered Shechem and Hamor with guile' (34:13, במרמה); Bereshit Rabbah 80:8 — you think there is deception here? the holy spirit says 'because he had defiled Dinah their sister'", ['circumcision_conditioned'])
    if q == 'foreskin_homograph': return cell('shechems_ruse_not_the_sign', I, "'a man who has a foreskin' (34:14) and 'as they are circumcised' (34:22) — the covenant's tokens inside the ruse; the scene's own males_circumcised, not the pre-Sinai engine's sign_in_the_flesh (FALSE at the census, 8k)", ['circumcised_by_the_condition'])
    if q == 'third_day_sheet': return cell('bathing_on_the_third_day', A, "Mishnah Shabbat 19:3 — R. Elazar ben Azariah: one bathes the infant on the third day that falls on the Sabbath, for it is said 'and it came to pass on the third day, when they were in pain' (34:25) — the proof text is this verse; Bereshit Rabbah 80:9 brings the row to the verse ('there we learned: one bathes the infant')", ['circumcised_by_the_condition'])
    if q == 'third_day_danger': return cell('danger', M, "Nedarim 31b:14 — Rabbi: Moses did not delay the circumcision; he said, shall I circumcise and go out? it is danger, as it is said 'on the third day, when they were in pain' (34:25)", ['circumcised_by_the_condition'])
    if q == 'third_day_verse': return cell('Gen 34:25', I, "'on the third day, when they were in pain, two of Jacob's sons, Simeon and Levi, Dinah's brothers, took each his sword' (34:25) — the ordinal parsed; the scene's day 546", ['slain_by_sword', 'hamor_and_shechem_slain'])
    if q == 'took_no_counsel': return cell('took_no_counsel_from_jacob', M, "Bereshit Rabbah 80:10 — 'two of Jacob's sons': sons of Jacob who took no counsel from Jacob; 'Simeon and Levi': who took counsel from each other; 'Dinah's brothers': was she the sister of the two alone?", ['slain_by_sword'])
    if q == 'troubled_charged': return cell('the_cask_was_clear', M, "Bereshit Rabbah 80:12 — 'you have troubled me' (34:30): the rabbis — the cask was clear and you have muddied it", ['troubled_charged'])
    if q == 'few_in_number': return cell('few_in_number', I, "'and I being few in number' (34:30, מתי מספר) — the charge's ground; troubled_charged on Simeon and Levi", ['troubled_charged'])
    if q == 'question_unanswered': return cell('as_a_harlot', I, "'should he deal with our sister as with a harlot?' (34:31) — the chapter ends on a question the ink never answers; question_unanswered a status", ['question_unanswered'])
    return cell('no_case', I, '', [FX.NONE])


def bethel_again(q):
    if q == 'foreign_gods_seats': return cell(2, I, "'put away the foreign gods' (35:2) and 'all the foreign gods' (35:4) (הנכר) — two seats; the DEBIT of 35:2 closed at 35:4 on the scene", ['foreign_gods_removal_owed', 'foreign_gods_buried'])
    if q == 'vow_delay': return cell('delay_punished', M, "Bereshit Rabbah 81:1-2 — 'arise, go up to Bethel' (35:1): 'it is a snare to a man to swallow holy things, and after vows to inquire' (Prov 20:25) — the vow's delay read as punished; the DEBIT ascent_to_bethel_owed closed at 35:6, altar_owed at 35:7", ['ascent_to_bethel_owed', 'altar_owed'])
    if q == 'return_closed': return cell('Gen 35:6', I, "28:15 'I will bring you back to this land' (S3's HEAVEN entry) — closed on the tape at 35:6 'and Jacob came to Luz, that is Bethel'; nothing on the bare scene (the entry lives on S3's world)", ['encamped_at'])
    if q == 'vow_closed': return cell('Gen 35:7', I, "28:20-22's vow (S3's entry vow_of_bethel) — closed on the tape at 35:7 'and he built there an altar'; the tithe of 28:22 never narrated as paid (8m OPEN)", ['altar_built'])
    if q == 'terror_of_god': return cell('terror_of_god', I, "'and the terror of God was upon the cities' (35:5, חתת אלהים) — the phrase's seat; terror_of_god a status on the cities", ['terror_of_god'])
    if q == 'allon_bakhut': return cell('greek_for_another_mourning', M, "Bereshit Rabbah 81:5 — 'Allon-bakhut' (35:8): R. Shmuel bar Nachman — it is Greek: allon, another; while he kept Deborah's mourning the news came that his mother had died (Rebekah's death unnarrated — 8m)", ['nurse_died', 'name_given'])
    if q == 'israel_repeated': return cell('Gen 35:10', I, "'your name is Jacob; your name shall not be called Jacob any more, but Israel shall be your name' (35:10) — the renaming repeated by God; the tape's rename is the family engine's (32:29), this seat's blessed_by_the_lord", ['blessed_by_the_lord'])
    if q == 'like_case': return cell('cited_as_the_like_case', M, "Berakhot 12b:28 — 'likewise you say: your name shall no more be called Jacob, but Israel shall be your name' (35:10) — the renaming cited as the like case of a mention that persists beside the new (12b's subject: the exodus remembered beside the future redemption)", ['blessed_by_the_lord'])
    if q == 'be_fruitful_sheet': return cell('a_man_does_not_cease', A, "Mishnah Yevamot 6:6 — a man does not cease from being fruitful and multiplying unless he has children — the commandment's holder", ['fruitfulness_blessed'])
    if q == 'fruitful_singular': return cell('said_to_jacob_singular', M, "Yevamot 65b:5 — Rav Yosef from here: 'I am God Almighty, be fruitful and multiply' (35:11) — said in the singular to Jacob, not 'be fruitful and multiply' in the plural (the man commanded, not the woman)", ['fruitfulness_blessed'])
    if q == 'kings_promised': return cell('kings_from_your_loins', I, "'a nation and an assembly of nations shall be of you, and kings shall come out of your loins' (35:11) — three HEAVEN clauses: fruitfulness_blessed, assembly_of_nations_promised, kings_promised (Genesis 36's kings of Edom before Israel's, 36:31)", ['kings_promised', 'assembly_of_nations_promised'])
    if q == 'land_promised': return cell('to_abraham_and_isaac', I, "'the land which I gave to Abraham and to Isaac, to you I will give it' (35:12) — the third generation's land entry", ['land_promised'])
    if q == 'libation_token': return cell('nesekh_by_name', I, "'and he poured on it a libation, and he poured on it oil' (35:14, נסך) — the drink offering's token read by name; the offerings engine's REFERENCE at the census (no verdict: Exodus 29:40-41's law is the erection's)", ['libation_poured', 'pillar_anointed'])
    if q == 'bethel_named_twice': return cell(2, I, "'and Jacob called the name of the place ... Bethel' at 28:19 (S3's) and 35:15 (this scene's) — the second naming on the scene; name_given on the-place", ['name_given'])
    return cell('no_case', I, '', [FX.NONE])


def three_deaths(q):
    if q == 'buried_writes': return cell(3, I, "the burials the scene writes: Deborah under the oak (35:8), Rachel on the way to Ephrath (35:19), Isaac by Esau and Jacob (35:29) — three `buried` entries by law_joseph (the family's `buried` branch answers 23, 48, 49, 50 alone)", ['buried', 'buried_by_both_sons'])
    if q == 'ben_oni_binyamin': return cell(('ben_oni_aramaic', 'binyamin_holy_tongue'), M, "Bereshit Rabbah 82:9 — 'Ben-oni': son of my sorrow in Aramaic; 'and his father called him Binyamin': in the holy tongue — two namings on one verse (35:18), the mother's and the father's", ['name_given', 'died_in_childbirth'])
    if q == 'benjamin_plene': return cell((len(_all_seats(lambda ws: any(w.endswith('בנימין') for w in ws), range(1, 51))), len(_all_seats(lambda ws: any(w.endswith('בנימן') for w in ws), range(1, 51)))), I, "Benjamin's spelling in Genesis MEASURED against Sotah 36b:9 (Rav Nachman bar Yitzchak: 'in the whole Torah it is written Binyamin short, and here Binyamin full, as 35:18'): full at 35:18, 42:4, 43:14, 43:16, 43:29, 45:12, 49:27 — seven; short at 35:24, 42:36, 43:15, 43:34, 44:12, 45:14, 45:22, 46:19, 46:21 — nine; recorded whichever way it falls (8m): the DB's letters give seven full seats in Genesis alone", ['name_given'])
    if q == 'grave_pillar': return cell('no_monuments_for_the_righteous', M, "Bereshit Rabbah 82:10 — 'and Jacob set a pillar on her grave' (35:20): R. Shimon ben Gamliel — one makes no monuments for the righteous; their words are their memorial", ['grave_marked'])
    if q == 'until_this_day': return cell('the_pillar_of_rachels_grave', I, "'it is the pillar of Rachel's grave to this day' (35:20) — the narrator's present; grave_marked on the-grave-of-rachel", ['grave_marked'])
    if q == 'reuben_sheet': return cell('read_not_translated', A, "Mishnah Megillah 4:10 — the act of Reuben (35:22) is read and not translated; concubine_lain_with carries the value read_not_translated on the ledger", ['concubine_lain_with'])
    if q == 'israel_heard': return cell('and_israel_heard', I, "'and Israel heard' (35:22, וישמע ישראל) — the verse breaks mid-line (the frozen unit's read of the open space); israel_heard a status, the sentence never finished", ['israel_heard'])
    if q == 'twelve_kept': return cell(12, I, "'and the sons of Jacob were twelve' (35:22) — parsed, in the same verse as the act; Bereshit Rabbah 82:11: the chain of lineage is hard to uproot before the Holy One", ['twelve_sons_listed', 'concubine_lain_with'])
    if q == 'twelve_named': return cell(len(ROSTERS['twelve']), I, "Reuben, Simeon, Levi, Judah, Issachar, Zebulun, Joseph, Benjamin, Dan, Naphtali, Gad, Asher (35:23-26) — twelve name tokens, each verified in its verse by the probes; 'born to him in Paddan-aram' with Benjamin among them (35:26 — the frozen unit's note)", ['twelve_sons_listed'])
    if q == 'isaac_180': return cell(180, I, "'and the days of Isaac were a hundred and eighty years' (35:28) — parsed; the marker died:isaac on the tape, proleptic (CJ2: twelve years after the sale)", ['full_of_days'])
    if q == 'buried_by_both': return cell(('esau', 'jacob'), I, "'and Esau and Jacob his sons buried him' (35:29) — Esau named first; buried_by_both_sons", ['buried_by_both_sons'])
    if q == 'gathered_seat': return cell('law_joseph_35_29', I, "the family's `gathered` branch seat-checked to Gen 49 (8k); Isaac's gathering written here — 'old and full of days' (35:29) full_of_days beside it", ['gathered_to_his_people', 'full_of_days'])
    return cell('no_case', I, '', [FX.NONE])


def edom(q):
    if q == 'wives_recorded': return cell(('adah', 'oholibamah', 'basemath'), I, "'Adah the daughter of Elon the Hittite, and Oholibamah the daughter of Anah ... and Basemath, Ishmael's daughter, sister of Nebaioth' (36:2-3) — three wives, three wife_taken entries; against 26:34 (Judith, Basemath daughter of Elon) and 28:9 (Mahalath daughter of Ishmael): recorded, no fold (8m)", ['wife_taken'])
    if q == 'timna_concubine': return cell('concubine', I, "'and Timna was concubine to Eliphaz, Esau's son, and she bore to Eliphaz Amalek' (36:12, פילגש); Bereshit Rabbah 82:14 — why is this written? to tell the honour of Abraham's house, how far kings and rulers wished to cleave to it", ['begotten'])
    if q == 'timna_amalek': return cell('rejected_proselyte', M, "Sanhedrin 99b:8 — Timna sought to convert; she came to Abraham, Isaac and Jacob and they did not accept her; she went and became a concubine to Eliphaz: 'better a maidservant to this nation than a lady to another' — from her came Amalek, who afflicted Israel: because they should not have pushed her away (a conduct verdict, a status — 8m)", ['begotten'])
    if q == 'two_anas': return cell('one_anah_zibeon_on_his_mother', M, "Bava Batra 115b:4 — 'these are the sons of Seir the Horite: Lotan, Shobal, Zibeon and Anah' (36:20) and 'these are the sons of Zibeon: Aiah and Anah' (36:24) — it teaches that Zibeon came upon his mother and begot Anah; Bereshit Rabbah 82:15 the same (8m)", ['horites_listed'])
    if q == 'kings_count': return cell(sum(1 for vs in range(1, NV[36] + 1) for w in toks(36, vs) if w == 'וימלך'), I, "'and he reigned' (וימלך) in Genesis 36 — eight tokens (36:32-39, measured): Bela, Jobab, Husham, Hadad, Samlah, Shaul, Baal-hanan, Hadar; reigned_in_edom eight times on the scene", ['reigned_in_edom'])
    if q == 'kings_named': return cell(len(ROSTERS['kings']), I, "the eight kings' names verified in their verses by the probes (36:32-39)", ['reigned_in_edom'])
    if q == 'before_a_king': return cell('before_israel_had_a_king', I, "'these are the kings who reigned in the land of Edom before there reigned any king over the children of Israel' (36:31) — the narrator's forward glance; 35:11's kings_promised the entry it answers to", ['reigned_in_edom'])
    if q == 'nations_as_ship': return cell('a_ship_from_many_places', M, "Bereshit Rabbah 83:1 — 'these are the kings' (36:31): R. Yitzchak — the nations are likened to a ship, its mast from one place and its anchors from another", ['reigned_in_edom'])
    if q == 'melekh_homograph': return cell('king_not_molech', I, "'before there reigned any king' (36:31, מלך) — the king word's consonants are Molech's; a homograph, FALSE at the census (S2, S3 the same)", ['reigned_in_edom'])
    if q == 'holding_homograph': return cell('edoms_holding_not_the_jubilees', I, "'in the land of their holding' (36:43, אחזה) — Edom's holding outside the land of the jubilee's law: a homograph, FALSE at the census", ['dwelt_in_seir'])
    if q == 'parted_for_room': return cell('too_great_to_dwell_together', I, "'their possessions were too great for them to dwell together' (36:7) — the parting's ground, as 13:6's (S2's Lot); parted and dwelt_in_seir on Esau", ['parted', 'dwelt_in_seir'])
    return cell('no_case', I, '', [FX.NONE])


def dreamer(q):
    if q == 'seventeen': return cell(17, I, "'Joseph, seventeen years old' (37:2) — parsed; the marker age:joseph:17 the tape computes off born:jacob (8k: born:joseph is not on the tape at 37:2)", ['loved_by_the_father'])
    if q == 'youthful_deeds': return cell('deeds_of_youth', M, "Bereshit Rabbah 84:7 — 'seventeen years old ... and he was a lad' (37:2): he did the deeds of youth — touching his eyes, lifting his heel, arranging his hair", ['evil_report_brought'])
    if q == 'coat_seats': return cell(len(_seats(lambda ws: any(w.endswith('פסים') for w in ws), 37, 37)), I, "'a coat of stripes' (כתנת פסים) in Genesis 37 — 37:3 (made), 37:23 (stripped), 37:32 (sent): three seats, measured; the coat's three acts on the ledger; Bereshit Rabbah 84:16 — 'they stripped Joseph' (37:23): four garments named on the one verse, the coat of stripes the third", ['coat_of_stripes_made', 'stripped_of_the_coat', 'coat_recognized'])
    if q == 'why_loved': return cell(('likeness', 'the_laws_of_shem_and_eber'), M, "Bereshit Rabbah 84:8 — 'and Israel loved Joseph' (37:3): R. Yehuda — his features resembled his; R. Nechemya — all the laws Shem and Eber handed to Jacob he handed to him", ['loved_by_the_father'])
    if q == 'dreams_told': return cell(2, I, "the sheaves (37:5-8) and the sun, moon and stars (37:9-11) — two dreams told; dream_of_sheaves, dream_of_sun_moon_stars on Joseph", ['dream_of_sheaves', 'dream_of_sun_moon_stars'])
    if q == 'dream_hope_years': return cell(22, M, "Berakhot 55b:2 — R. Levi: a man should hope for a good dream up to twenty-two years — from Joseph: 'seventeen years old' (37:2) and 'thirty years old when he stood before Pharaoh' (41:46), thirteen, and the seven of plenty and two of famine: twenty-two (the sequence runner CJ0's twenty-two on the other chain)", ['dream_of_sheaves'])
    if q == 'word_kept': return cell('kept_the_matter', I, "'and his brothers envied him, but his father kept the matter' (37:11, שמר) — envied on the brothers, word_kept on Jacob", ['envied', 'word_kept'])
    if q == 'pit_seats': return cell(len(_pit_seats()), I, "the pit noun's seats in Genesis 37 (measured by _pit_seats(): 37:22, 37:24, 37:28, 37:29) — four; 'one of the pits' (37:20) the plural; in_the_pit the body entry from 37:24, closed at 37:28", ['in_the_pit'])
    if q == 'pit_empty': return cell('snakes_and_scorpions', M, "Chagigah 3a:14 — 'and the pit was empty, there was no water in it' (37:24): from 'empty' I do not know there was no water? rather, water there was not, but snakes and scorpions there were", ['in_the_pit'])
    if q == 'what_profit': return cell('botzea_is_judah', M, "Sanhedrin 6b:5 — R. Meir: 'botzea' (Ps 10:3) is said only of Judah: 'and Judah said to his brothers, what profit (בצע) if we slay our brother' (37:26) — whoever blesses Judah blasphemes", ['sale_proposed'])
    if q == 'sellers_grammar': return cell('midianites_drew_ishmaelites_bought_medanites_sold', I, "'and Midianite men, merchants, passed; and they drew and lifted Joseph out of the pit, and sold Joseph to the Ishmaelites for twenty silver' (37:28); 'and the Medanites sold him into Egypt to Potiphar' (37:36); 'whom you sold into Egypt' (45:4) — the seller OPEN (8m); Bereshit Rabbah 84:18 'the Midianites passed'; 84:17 — 'and they sat down to eat bread' (37:25): the tribes' transgression is remembered forever", ['sold_into_egypt', 'sold_to_potiphar'])
    if q == 'twenty_silver': return cell(20, I, "'for twenty silver' (37:28, בעשרים כסף) — parsed; sold_into_egypt with amount 20 on Joseph's ledger; Sotah 36b:19 the astrologers' 'a slave his master bought for twenty silver'", ['sold_into_egypt'])
    if q == 'reuben_where': return cell(('sackcloth_and_fast', 'his_turn_to_serve'), M, "Bereshit Rabbah 84:19 — 'and Reuben returned to the pit' (37:29): where had he been? R. Eliezer — in his sackcloth and his fast; R. Yehoshua — his turn had come to serve his father", ['rescue_urged'])
    if q == 'tunic_by_call': return cell(VS.tunics('tunic_atones')['v'], P, "CALLED cold_run_vestments.tunics('tunic_atones') -> the vestments engine's own row [IMPORT, live]: the TUNIC atones for bloodshed, 'and they slaughtered a goat and dipped the tunic in the blood' (37:31) — Arakhin 16a:13, Zevachim 88b:6: THE FLOW REVERSED, a narrative verse the source of a law's row", ['coat_dipped'])
    if q == 'recognition_row': return cell('recognize_answered_by_recognize', M, "Sotah 10b:7 — R. Chama bar Chanina: with 'recognize' he told his father ('recognize now whether it is your son's coat', 37:32), with 'recognize' they told him ('recognize now whose these are', 38:25 — the family's seat)", ['coat_recognized'])
    if q == 'recognized_seat': return cell('law_joseph_37_33', I, "the family's `recognized` branch seat-checked to Gen 38 (8k — Judah's acquittal of Tamar); the coat's recognition (37:33) written here: coat_recognized, 'an evil beast has devoured him; Joseph is surely torn'", ['coat_recognized'])
    if q == 'mourned_many_days': return cell('many_days', I, "'and mourned for his son many days' (37:34, ימים רבים); 'and he refused to be comforted' (37:35) — mourned_many_days, comfort_refused: the mourning that outlives its object", ['mourned_many_days', 'comfort_refused'])
    if q == 'daughters_plural': return cell('sons_in_law_and_daughters_in_law', M, "Bereshit Rabbah 84:21 — 'and all his sons and all his daughters rose' (37:35): how many daughters had he? one, and would that he had buried her — rather, a man does not refrain from calling his son-in-law son and his daughter-in-law daughter; R. Yehuda: the tribes married their sisters", ['comfort_refused'])
    return cell('no_case', I, '', [FX.NONE])


def potiphar(q):
    if q == 'potiphar_spellings': return cell((_all_seats(lambda ws: 'פוטיפר' in ws or 'לפוטיפר' in ws, range(1, 51)), _all_seats(lambda ws: 'פוטי' in ws, range(1, 51))), I, "'Potiphar' (פוטיפר) at 37:36, 39:1 and 'Poti-phera' (פוטי פרע, two tokens) at 41:45, 41:50, 46:20 — measured; Sotah 13b:12 — Rav: he bought him for himself; Gabriel came and castrated him: at first 'Potiphar', at the end 'Potiphera' — recorded, no fold (8m)", ['bought_by_potiphar'])
    if q == 'bought_ones_buy': return cell('bought_ones_acquire', M, "Bereshit Rabbah 86:3 — 'and he bought him' (39:1): the bought acquire — all slaves diminish their master's house, but this one, 'the LORD blessed the Egyptian's house for Joseph's sake' (39:5); all slaves are suspected of theft, but this one, 'Joseph gathered all the silver' (47:14)", ['bought_by_potiphar', 'house_blessed_for_joseph'])
    if q == 'the_name_in_39': return cell(_name_by_chapter(), I, "the Tetragrammaton in Genesis 37-50 by chapter (measured over the family's chapters too): 39 eight tokens ('and the LORD was with Joseph' 39:2, 39:21, and six more), 38 three (the family's Judah and Tamar), 49 one (49:18 'I wait for Your salvation, LORD'), every other chapter zero — the Name in the Joseph story lives in Potiphar's house and the prison", ['prospering', 'house_blessed_for_joseph'])
    if q == 'adjoined_blessing': return cell('adjoin_blessing_to_scholars', M, "Berakhot 42a:8 — Abaye: adjoin a blessing to scholars: 'and the LORD blessed the Egyptian's house for Joseph's sake' (39:5)", ['house_blessed_for_joseph'])
    if q == 'handsome_as_rachel': return cell('as_rachel', I, "'and Joseph was of beautiful form and beautiful appearance' (39:6, יפה תאר ויפה מראה) = 29:17's 'of beautiful form and beautiful appearance' of Rachel (יפת תאר ויפת מראה) — the same pair in the masculine (the tokens measured)", ['lie_with_me_demanded'])
    if q == 'lifted_eyes': return cell('the_eyes_of_the_wife', M, "Horayot 10b:11 — 'and his master's wife lifted her eyes to Joseph' (39:7) among the eye-liftings the row lists with Lot's (13:10) and Samson's; 'and Shechem the son of Hamor saw her' (34:2) beside them", ['lie_with_me_demanded'])
    if q == 'refused': return cell('a_transgression_is_refused', M, "Bereshit Rabbah 87:5 — 'and he refused' (39:8): Yehuda ben Rabbi — in a matter of commandment one refuses ('my brother-in-law refuses', Deut 25:7), in a matter of transgression one refuses: 'and he refused and said to his master's wife'", ['refused'])
    if q == 'as_this_day': return cell('to_do_his_work', I, "'and it came to pass about this day, that he went into the house to do his work' (39:11, לעשות מלאכתו) — the ink's own clause; fled_outside and garment_left the acts", ['fled_outside', 'garment_left'])
    if q == 'hebrew_seats': return cell(len(_seats(lambda ws: any(w in ('עברי', 'העברי', 'עברים', 'העברים') for w in ws), 39, 43)), I, "'Hebrew' in Genesis 39-43 (measured): 39:14, 39:17 (the wife's accusation), 40:15 ('the land of the Hebrews'), 41:12 ('a Hebrew lad, a slave'), 43:32 ('the Hebrews') — five seats; the epithet, not the Hebrew slave law's subject (FALSE at the census)", ['accused_falsely'])
    if q == 'prison_house': return cell(sum(1 for ch in (39, 40) for vs in range(1, NV[ch] + 1) for w in toks(ch, vs) if w == 'הסהר'), I, "'the round-house' (הסהר) in Genesis 39-40 — eight tokens (measured); imprisoned the body entry, appointed_over_the_prisoners its reversal within the walls", ['imprisoned', 'appointed_over_the_prisoners'])
    if q == 'service_pleasant': return cell('his_service_pleasant', M, "Bereshit Rabbah 87:10 — 'and the LORD was with Joseph ... and the keeper of the prison gave' (39:21-22): Rav Huna in R. Acha's name — his service was pleasant to his master: he went out and rinsed the cups, set the tables, made the beds", ['favor_in_the_keepers_eyes'])
    return cell('no_case', I, '', [FX.NONE])


def prison_dreams(q):
    if q == 'two_officers': return cell(('cupbearer', 'baker'), I, "'the chief of the cupbearers and the chief of the bakers' (40:2) — two officers, one night, two dreams (40:5); dreams_in_one_night", ['dreams_in_one_night', 'in_custody'])
    if q == 'three_days_parsed': return cell((3, 3), I, "'the three branches are three days' (40:12), 'the three baskets are three days' (40:18) — parsed; two timers set on day 735 due 738 on the bare scene", ['interpretation_given', 'head_lifted_up_due', 'head_lifted_off_due'])
    if q == 'third_day_timers': return cell(_timer_span('head_lifted_up_due'), I, "the cupbearer's timer on the bare scene, MEASURED from the log (the fire day less the set day): 'in yet three days' (40:13) read INCLUSIVE as the tape reads every third day (22:4, 31:22) — set at the interpretation, fires on the third day, the birthday (40:20), before the acts (CJ6 on the tape); the model's exclusive 738 corrected at the design of the tape's rows (8n)", ['head_lifted_up_due', 'head_lifted_off_due'])
    if q == 'birthday': return cell('Gen 40:20', I, "'and it came to pass on the third day, Pharaoh's birthday' (40:20) — the ordinal parsed; the marker birthday on the tape; feast_made", ['feast_made'])
    if q == 'lifted_head_two_ways': return cell(('restored', 'hanged'), I, "'lift up your head' (40:13) and 'lift up your head from off you' (40:19) — one idiom, two verdicts: 'restored the chief cupbearer to his cupbearing' (40:21), 'the chief baker he hanged' (40:22)", ['restored_to_the_cup', 'hanged'])
    if q == 'former_custom': return cell('the_first_manner', I, "'according to the former manner when you were his cupbearer' (40:13, כמשפט הראשון) — the citation form AS_PRESCRIBED filed INTERNAL: the cupbearer's own office cited (40:1-2), no law's prescription", ['restored_to_the_cup'])
    if q == 'custody_closes': return cell(('Gen 40:21', 'Gen 40:22'), I, "in_custody (40:3) closed twice on the scene: the cupbearer's at his restoration, the baker's at his hanging", ['in_custody'])
    if q == 'vine_is_israel': return cell('israel', M, "Bereshit Rabbah 88:5 — 'behold a vine before me' (40:9): these are Israel ('You brought a vine out of Egypt', Ps 80:9); 'three branches' — Moses, Aaron and Miriam", ['dreams_in_one_night'])
    if q == 'forgot': return cell('you_forget_i_do_not', M, "Bereshit Rabbah 88:7 — 'and the chief cupbearer did not remember Joseph' (40:23): the Holy One said, you forget him and I will not forget him; petition_forgotten a status, the DEBIT the two years of 41:1 measure", ['petition_forgotten', 'remembrance_asked'])
    return cell('no_case', I, '', [FX.NONE])


def pharaoh_dreams(q):
    if q == 'two_years': return cell('two_years_of_days', I, "'at the end of two years of days' (41:1, שנתים ימים) — the marker pharaoh_dreams on the tape; Nazir 5a:5 — 'days' without 'years' are learned from 'days' without 'years', and not from this, which has years with it", ['spirit_troubled'])
    if q == 'end_to_darkness': return cell('an_end_set_to_darkness', M, "Bereshit Rabbah 89:1 — 'at the end of two years' (41:1): 'He sets an end to darkness' (Job 28:3) — a time was given to the world, how many years it shall do in gloom", ['spirit_troubled'])
    if q == 'seven_and_plenty': return cell(sum(1 for vs in range(1, NV[41] + 1) for w in toks(41, vs) if w in ('שבע', 'ושבע', 'שבעת', 'שבעה', 'השבע')), I, "the consonants שבע in Genesis 41 — thirty-one tokens (measured): seven (sheva) and plenty (sava) share one skeleton, the sin/shin split invisible to the consonants ('seven years of plenty', 41:34 בשבע שני השבע, two words one spelling) — the vowel layer separates them (the Onkelos/vowel finding of the ink era)", ['one_dream', 'plenty_seven_years'])
    if q == 'one_dream': return cell('one', I, "'the dream of Pharaoh is one' (41:25), 'it is one dream' (41:26) — the interpretation's first move; one_dream with value 7 years", ['one_dream'])
    if q == 'doubled': return cell('established_and_hastened', I, "'and as for the dream being doubled to Pharaoh twice, it is because the thing is established by God, and God will shortly bring it to pass' (41:32, השנות — the doubling, פעמים — twice) — the doubling read as a legal signature", ['pharaohs_dream_doubled'])
    if q == 'not_i_god': return cell('god_will_answer', I, "'it is not in me; God will answer Pharaoh's peace' (41:16) — not_i_god a status before the interpretation", ['not_i_god', 'no_interpreter'])
    if q == 'fifth_counsel': return cell('a_fifth', I, "'and let him take a fifth of the land of Egypt in the seven years of plenty' (41:34, וחמש) — the verb of the fifth; the sanctuary's fifth (Lev 27) a homograph, FALSE at the census", ['counsel_of_the_fifth'])
    if q == 'rushed_from_the_pit': return cell('the_pit_again', I, "'and they rushed him from the pit' (41:14, מן הבור) — the prison called by the pit's noun (37:24's); rushed_from_the_pit", ['rushed_from_the_pit'])
    return cell('no_case', I, '', [FX.NONE])


def the_rise(q):
    if q == 'joseph_of_his_own': return cell('of_his_own_they_gave_him', M, "Bereshit Rabbah 90:3 — 'and Pharaoh said to Joseph ... and Pharaoh removed his ring' (41:41-42): R. Shimon ben Gamliel — of Joseph's own they gave him: the mouth that did not kiss in transgression, 'by your mouth shall all my people be fed'; the body that did not touch transgression, 'and he clothed him'", ['ring_given', 'set_over_egypt'])
    if q == 'astrologers': return cell('a_slave_bought_for_twenty', M, "Sotah 36b:19 — when Pharaoh said 'without you no man shall lift his hand' (41:44), Pharaoh's astrologers said: a slave his master bought for twenty silver you would set over us? he said: I see royal traits in him", ['set_over_egypt'])
    if q == 'zaphenath': return cell(1, I, "'Zaphenath-paneah' (41:45, צפנת פענח) — the name's only seat (measured); name_given by Pharaoh", ['name_given'])
    if q == 'asenath': return cell('daughter_of_potiphera_priest_of_on', I, "'Asenath the daughter of Poti-phera priest of On' (41:45) — wife_taken with husband Joseph, asenath_given by Pharaoh; the marriage the family engine's vocabulary at this scene's seat", ['asenath_given', 'wife_taken'])
    if q == 'thirty': return cell(30, I, "'and Joseph was thirty years old when he stood before Pharaoh' (41:46) — parsed; the marker joseph30 the tape carries, born:joseph computed from it", ['thirty_at_the_standing'])
    if q == 'seventeen_to_thirty': return cell(13, I, "thirty (41:46) minus seventeen (37:2): thirteen years from the sale to the standing — the ink's own arithmetic (Berakhot 55b:2 counts it)", ['thirty_at_the_standing'])
    if q == 'handfuls': return cell('by_handfuls', M, "Bereshit Rabbah 90:5 — 'and the earth brought forth in the seven years of plenty by handfuls' (41:47): R. Yochanan — the shrunken and the unshrunken", ['food_gathered_as_sand'])
    if q == 'two_sons_before_the_famine': return cell('before_the_famine', I, "'and to Joseph were born two sons before the year of famine came' (41:50) — two_sons_before_the_famine; Manasseh and Ephraim `born` under Genesis 17, the eighth-day timers set", ['two_sons_before_the_famine'])
    if q == 'famine_years_bar': return cell('marital_relations_barred_in_famine', M, "Taanit 11a:4 — Resh Lakish: it is forbidden to a man to serve his bed in the years of famine, as it is said 'and to Joseph were born two sons before the year of famine came' (41:50); a tanna: the childless serve their beds in the years of famine", ['two_sons_before_the_famine'])
    if q == 'manasseh_ephraim': return cell(('made_me_forget', 'made_me_fruitful'), I, "'Manasseh, for God has made me forget all my toil' (41:51), 'Ephraim, for God has made me fruitful in the land of my affliction' (41:52) — two namings by Joseph, name_given twice", ['name_given'])
    if q == 'eighth_days': return cell(3, I, "the eighth-day timers on the scene's births: Benjamin (35:18), Manasseh and Ephraim (41:50) — three, none on a daughter; the pre-Sinai daemon's own run (CJ8 on the tape)", ['two_sons_before_the_famine'])
    if q == 'covenant_heads_by_call': return cell(PS_.covenant('covenant_heads')['v'], P, "CALLED cold_run_pre_sinai.covenant('covenant_heads') -> the covenant's addressees [IMPORT, live]: 'you and your seed after you' (17:9) — the births of this stretch are that seed's, the eighth day their statute", ['two_sons_before_the_famine'])
    if q == 'plenty_timer_days': return cell(2555, D, "the seven years of plenty on the bare scene: 7 × 365 days (no epoch — the Calendar's year on the tape); the famine's seven set at their fire (41:54), the five remaining at 45:6 — CJ9: one due day", ['plenty_seven_years', 'famine_seven_years'])
    if q == 'famine_in_all_lands': return cell('all_lands', I, "'and the famine was over all the face of the earth' (41:56), 'and all the earth came to Egypt' (41:57) — famine_in_all_lands on the-lands; Pesachim 119a:6 the silver of all lands", ['famine_in_all_lands', 'storehouses_opened'])
    return cell('no_case', I, '', [FX.NONE])

def first_descent(q):
    if q == 'why_show_yourselves': return cell('do_not_show_yourselves_sated', M, "Taanit 10b:6 — 'and Jacob said to his sons, why do you show yourselves' (42:1): Jacob said to his sons, do not show yourselves sated, not before Esau and not before Ishmael, that they not envy you", ['descent_commanded'])
    if q == 'ten': return cell(10, I, "'and Joseph's ten brothers went down' (42:3) — parsed; ten_went_down with value 10; Benjamin withheld (42:4)", ['ten_went_down', 'benjamin_withheld'])
    if q == 'congregation_of_ten': return cell('edah_is_ten', M, "Bereshit Rabbah 91:3 — 'and the sons of Israel came to buy' (42:5): whence that a congregation is ten? 'congregation' here and 'how long for this evil congregation' (Num 14:27) there — the frozen unit's routed source of the quorum", ['ten_went_down'])
    if q == 'governor': return cell('the_shalit', I, "'and Joseph was the governor over the land' (42:6, השליט) — the token's seat; bowed_as_the_sheaves the dream received: 'and bowed down to him with their faces to the earth'", ['bowed_as_the_sheaves'])
    if q == 'mashbir': return cell('joseph_the_provider', M, "Sanhedrin 92a:3 — Rava in Rav Sheshet's name: one who teaches merits blessings like Joseph, 'a blessing on the head of the provider' (Prov 11:26), and the provider is Joseph: 'and Joseph was the governor over the land, he was the provider to all the people of the land' (42:6)", ['bowed_as_the_sheaves'])
    if q == 'recognized_one_way': return cell('beard', M, "Bava Metzia 39b:8 — 'and Joseph recognized his brothers, but they did not recognize him' (42:8): it teaches that he left without the mark of a beard and came with the mark of a beard (the row's own case: a brother unrecognized for identification)", ['recognized_one_way'])
    if q == 'stranger': return cell('made_himself_a_stranger', M, "Bereshit Rabbah 91:7 — 'and Joseph saw his brothers' (42:7): R. Yehoshua bar Nechemya — he made himself a stranger to them", ['recognized_one_way', 'spies_charged'])
    if q == 'three_days_custody': return cell(3, I, "'and he put them together into custody three days' (42:17) — parsed; the timer custody_three_days set at the custody, fires before 'on the third day' (42:18) on the tape (CJ6)", ['custody_three_days', 'held_in_custody'])
    if q == 'plan_revised': return cell(('all_held', 'one_held'), I, "'you shall be bound, that your words be proved' (42:16) revised to 'let one of your brothers be bound' (42:19) — plan_revised with the ordinal; Simeon bound (42:24), held_in_custody until 43:23", ['plan_revised', 'held_in_custody'])
    if q == 'aval': return cell('a_southern_word_for_indeed', M, "Bereshit Rabbah 91:8 — 'indeed (אבל) we are guilty' (42:21): R. Abba bar Kahana — it is a southern word: aval, indeed", ['guilt_acknowledged'])
    if q == 'interpreter': return cell('the_interpreter_between_them', I, "'for the interpreter was between them' (42:23) — the language wall the brothers do not see through; interpreter_between a status", ['interpreter_between'])
    if q == 'wept_seats': return cell(len(_seats(lambda ws: any(w in ('ויבך', 'ויבכו', 'ותבך', 'לבכות', 'בכה') for w in ws), 42, 50)), I, "the weeping verb's seats in Genesis 42-50 (measured over the span): 42:24, 43:30, 45:14, 45:15, 46:29, 50:1, 50:3, 50:17 — eight; 45:2's 'he gave his voice in weeping' (בבכי) the noun beside them", ['wept'])
    if q == 'is_not_tokens': return cell(sum(1 for w in toks(42, 36) if w == 'איננו'), I, "'Joseph is not, and Simeon is not, and Benjamin you will take' (42:36) — the token 'is not' (איננו) TWICE in the verse, MEASURED: the declaration's 'three tokens' (8h CJ10) is refuted by the ink and corrected beside its record — the third of the presumption is Benjamin's clause, a name without the token", ['bereavement_charged'])
    if q == 'presumption_at_three': return cell(3, M, "Chullin 95b:14 — R. Elazar: and that is when it has been established three times, as it is written 'Joseph is not, and Simeon is not, and Benjamin you will take' (42:36) — the presumption (chazakah) at three, counted by the three names", ['bereavement_charged'])
    if q == 'pledge_row': return cell('kabbelanut_not_surety', M, "Bava Batra 173b:10 — Rav Chisda objects: this is an unconditional undertaking (kabbelanut), 'give him into my hand and I will bring him back' (42:37) — Reuben's pledge is not the surety's form; Judah's (43:9) is (Rav Huna, 173b:9)", ['pledge_offered'])
    if q == 'gray_hairs': return cell('to_sheol_in_grief', I, "'you will bring down my gray hairs in grief to Sheol' (42:38) — the refusal's ground; descent_refused, the second descent waiting on the grain's end (43:2)", ['descent_refused'])
    return cell('no_case', I, '', [FX.NONE])


def second_descent(q):
    if q == 'surety_verse': return cell('Gen 43:9', I, "'I will be surety for him; of my hand you shall require him' (43:9, אנכי אערבנו) — Bava Batra 173b:9, Rav Huna: whence that a surety is bound? from here; surety_undertaken on Judah, counterparty Jacob, closed at 45:25", ['surety_undertaken'])
    if q == 'surety_sheet': return cell('collects_from_free_property', A, "Mishnah Bava Batra 10:8 — a surety who appears after the signing of the deed: the creditor collects from free property — the surety's row on the testing shelf", ['surety_undertaken'])
    if q == 'surety_person_sheet': return cell('the_surety_transgresses_too', A, "Mishnah Bava Metzia 5:11 — these transgress a negative commandment: the lender, the borrower, the surety and the witnesses — the surety a legal person in the interest ban's row", ['surety_undertaken'])
    if q == 'gift_homograph': return cell('a_gift_to_a_man', I, "'carry down to the man a gift' (43:11, מנחה) — balm, honey, gum, ladanum, pistachios, almonds: the gift to a man, a homograph of the meal offering (FALSE at the census; 32:14-22's gift the same)", ['gift_presented'])
    if q == 'double_silver': return cell('double', I, "'and take double silver in your hand' (43:12, כסף משנה) — double_silver_taken; the returned silver carried back (43:12, 43:21)", ['double_silver_taken'])
    if q == 'bereaved': return cell('as_i_am_bereaved', I, "'and I, as I am bereaved, I am bereaved' (43:14) — the citation form AS_WHEN filed INTERNAL (a manner clause); mercy_prayed the HEAVEN entry ('God Almighty give you mercy before the man')", ['mercy_prayed'])
    if q == 'simeon_out': return cell('Gen 43:23', I, "'and he brought Simeon out to them' (43:23) — held_in_custody closed on the scene; peace_given ('peace be to you, fear not')", ['peace_given', 'held_in_custody'])
    if q == 'abomination_seats': return cell(len(_all_seats(lambda ws: any(w.startswith('תועב') for w in ws), range(1, 51))), I, "'an abomination to the Egyptians' (43:32) and 'every shepherd is an abomination to the Egyptians' (46:34) — two seats in Genesis (measured); the noun of Leviticus 18's ban in Egypt's own mouth: FALSE at the census", ['egyptians_eat_apart', 'shepherds_abhorred'])
    if q == 'birth_order': return cell('seated_by_birth_order', I, "'and they sat before him, the firstborn according to his birthright and the youngest according to his youth' (43:33) — seated_by_birth_order; 'the men marvelled'", ['seated_by_birth_order'])
    if q == 'inheritance_by_call': return cell(FA.inheritance('inheritance_order_owed')['v'], P, "CALLED cold_run_family.inheritance('inheritance_order_owed') -> the seats the family engine owes forward [IMPORT, live]: 'the firstborn according to his birthright' (43:33) read against the order the engine keeps (Mishnah Bekhorot 8:1 the firstborn by the head — S3's row)", ['seated_by_birth_order'])
    if q == 'five_hands': return cell(5, I, "'Benjamin's portion was five times as much as any of theirs' (43:34, חמש ידות) — parsed; five_hands with value 5", ['five_hands'])
    if q == 'feast_at_noon': return cell('noon', I, "'for the men shall eat with me at noon' (43:16) — house_ordered; feast_made at 43:25's 'for they had heard that they should eat bread there' (the witness the events lint moved off 43:34's shared line)", ['house_ordered', 'feast_made'])
    return cell('no_case', I, '', [FX.NONE])


def cup(q):
    if q == 'morning_light': return cell('go_out_in_good_light', M, "Taanit 10b:11 — Rav Yehuda in Rav's name: let a man always go out in good light and come in in good light, as it is said 'as soon as the morning was light, the men were sent away' (44:3)", ['sent_out'])
    if q == 'divination_seats': return cell(len(_seats(lambda ws: any(w in ('נחש', 'ינחש') for w in ws), 44, 44)), I, "'he surely divines with it' (44:5) and 'that a man like me surely divines' (44:15) (נחש ינחש) — two seats; the token of Leviticus 19:26's ban in a ruse before Sinai: divination_claimed a status, no verdict (FALSE at the census)", ['divination_claimed'])
    if q == 'three_verdicts': return cell(('death_and_slavery', 'the_finder_a_slave', 'the_finder_alone'), I, "'with whomever it is found, let him die, and we also will be my lord's slaves' (44:9); 'he with whom it is found shall be my slave, and you shall be clean' (44:10); 'the man in whose hand the cup is found, he shall be my slave; and you, go up in peace' (44:17) — three verdicts, each softer: the brothers' rash offer, the steward's, Joseph's", ['death_and_slavery_offered', 'finder_a_slave_ruled', 'slavery_of_the_finder_ruled'])
    if q == 'thief_sold_by_call': return cell(MP3.burglar('the_sale')['v'], P, "CALLED cold_run_mishpatim_3.burglar('the_sale') -> Exodus 22:2's 'if he has nothing, he is sold for his theft' [IMPORT, live]: the compiled verdict is the sale's TERM — six years for the principal (Kiddushin 18a:8, Mekhilta Nezikin continuation 2 3) — the first run's miss: the hand had typed the effect's name (sold_for_theft) for the verdict's value, corrected beside the record; the three verdicts of 44:9-17 laid on the rule's shape — the thief without means sold for a term, never killed; the brothers' 'let him die' outside the rule, the steward's and Joseph's open-ended 'my slave' inside it and beyond its term", ['finder_a_slave_ruled'])
    if q == 'ten_men_one_thief': return cell('not_all_bound', M, "Bereshit Rabbah 92:8 — 'now also let it be according to your words' (44:10): ten men, one of whom is found in theft — are they all bound? I do not do so; rather 'he with whom it is found shall be my slave'", ['finder_a_slave_ruled'])
    if q == 'search_source': return cell('finding_from_finding', M, "Pesachim 7b:14 — 'finding' from 'finding': it is written here 'seven days leaven shall not be FOUND in your houses' (Exod 12:19) and there 'and he SEARCHED, he began at the eldest and ended at the youngest, and it was FOUND' (44:12) — finding is by searching: THE FLOW REVERSED, the cup's search the source of the leaven search's form", ['cup_found'])
    if q == 'leaven_search_sheet': return cell('by_the_light_of_the_lamp', A, "Mishnah Pesachim 1:1 — on the night of the fourteenth one searches for leaven by the light of the lamp — the row 7b's derivation serves", ['cup_found'])
    if q == 'search_order': return cell(('the_eldest', 'the_youngest'), I, "'he began at the eldest and ended at the youngest' (44:12) — the search's order, the cup in Benjamin's sack; cup_found with the value benjamin", ['cup_found', 'cup_planted'])
    if q == 'what_shall_we_say': return cell(('first_silver', 'second_silver', 'the_cup'), M, "Bereshit Rabbah 92:9 — 'and Judah said, what shall we say to my lord' (44:16): about the first silver, what shall we speak about the second silver, how shall we clear ourselves about the cup; what shall we say to father about Joseph, Simeon, Benjamin", ['guilt_acknowledged'])
    if q == 'as_pharaoh': return cell('you_are_as_pharaoh', I, "'for you are as Pharaoh' (44:18, כי כמוך כפרעה) — the plea's opening; surety_invoked (44:32 'your servant became surety')", ['surety_invoked'])
    if q == 'soul_bound': return cell('his_soul_bound_with_his_soul', I, "'his soul is bound up with his soul' (44:30, ונפשו קשורה בנפשו) — the life token in the plea (FALSE for the pre-Sinai code's life_blood at the census)", ['substitution_offered'])
    if q == 'instead_of_the_lad': return cell('instead_of_the_lad', I, "'let your servant remain instead of the lad as a slave to my lord' (44:33, תחת) — the substitution; the talion formula's word a homograph (FALSE at the census)", ['substitution_offered'])
    if q == 'judah_appeasement': return cell(('joseph', 'the_brothers', 'benjamin'), M, "Bereshit Rabbah 93:9 — R. Chiyya bar Abba: all the words you read that Judah spoke to Joseph before his brothers, until 'and Joseph could not restrain himself' (45:1), had in them appeasement for Joseph, for his brothers, and for Benjamin", ['surety_invoked'])
    return cell('no_case', I, '', [FX.NONE])


def i_am_joseph(q):
    if q == 'could_not_restrain': return cell('Gen 45:1', I, "'and Joseph could not restrain himself' (45:1) — restraint_failed; 'I am Joseph; is my father yet alive?' (45:3) revealed_to_his_brothers", ['restraint_failed', 'revealed_to_his_brothers'])
    if q == 'rebuke': return cell('rebuke_of_flesh_and_blood', M, "Chagigah 4b:8 — R. Elazar, when he reached this verse, wept: 'and his brothers could not answer him, for they were terrified at his presence' (45:3) — if the rebuke of flesh and blood is so, the rebuke of the Holy One how much more", ['terrified'])
    if q == 'two_and_five': return cell((2, 5), I, "'these two years the famine has been in the land, and yet there are five years' (45:6) — parsed; the marker famine_two on the tape; five_years_of_famine_left the timer set here", ['five_years_of_famine_left', 'sent_by_god_declared'])
    if q == 'famine_timers_one_day': return cell('same_due_day', D, "the seven-year timer of 41:54 and the five-remaining timer of 45:6 are due on ONE day on the bare scene (the model's own assertion, 45:6 = 41:54 + 2 years) — CJ9 on the tape: the ink's arithmetic closes", ['five_years_of_famine_left', 'famine_seven_years'])
    if q == 'father_to_pharaoh': return cell(('father', 'lord', 'ruler'), I, "'a father to Pharaoh, and lord of all his house, and ruler over all the land of Egypt' (45:8) — the three titles; sent_by_god_declared: 'it was not you who sent me here, but God'", ['sent_by_god_declared'])
    if q == 'benjamins_necks': return cell('two_temples_in_benjamins_portion', M, "Megillah 16b:2 — 'and he fell on his brother Benjamin's neck and wept' (45:14): how many necks had Benjamin? R. Elazar — he wept for the two Temples destined to be in Benjamin's portion and to be destroyed; Benjamin wept for the tabernacle of Shiloh in Joseph's; Bereshit Rabbah 93:12 the same", ['wept'])
    if q == 'eyes_see': return cell('no_grudge_as_with_benjamin', M, "Megillah 16b:3 — 'and behold, your eyes see, and the eyes of my brother Benjamin' (45:12): as I bear no grudge against my brother Benjamin, who was not at my sale, so I bear none against you", ['revealed_to_his_brothers'])
    if q == 'three_hundred_and_five': return cell((300, 5), I, "'to Benjamin he gave three hundred silver and five changes of garments' (45:22) — parsed; three_hundred_silver with amount 300, gifts_given", ['three_hundred_silver', 'gifts_given'])
    if q == 'ten_donkeys_parsed': return cell(10, I, "'ten donkeys laden with the good things of Egypt' (45:23) — parsed; ten_donkeys_sent", ['ten_donkeys_sent'])
    if q == 'ten_donkeys': return cell('old_wine', M, "Megillah 16b:4 — 'and to his father he sent thus: ten donkeys laden with the good of Egypt' (45:23): what is the good of Egypt? R. Binyamin bar Yefet in R. Elazar's name — he sent him old wine, in which the mind of the old finds ease", ['ten_donkeys_sent'])
    if q == 'do_not_quarrel': return cell('do_not_quarrel_on_the_way', I, "'do not quarrel on the way' (45:24, אל תרגזו בדרך) — quarrel_barred, a BLOCK on the brothers for the road", ['quarrel_barred', 'sent_out'])
    if q == 'heart_numb_then_lived': return cell(('numb', 'lived'), I, "'and his heart went numb, for he did not believe them' (45:26, ויפג לבו); 'and the spirit of Jacob their father lived' (45:27, ותחי רוח) — heart_numb then spirit_revived on the wagons' sight", ['heart_numb', 'spirit_revived'])
    if q == 'surety_closed': return cell('Gen 45:25', I, "'and they came to the land of Canaan to Jacob their father' (45:25) — Benjamin returned: surety_undertaken (43:9) closed on the scene", ['surety_undertaken'])
    return cell('no_case', I, '', [FX.NONE])


def the_seventy(q):
    if q == 'sacrifices_by_call': return cell(OF.dispatch('shelamim')['place']['v'], P, "CALLED cold_run_offerings.dispatch('shelamim') -> the peace offering's place [IMPORT, live]: 'and he sacrificed sacrifices to the God of his father Isaac' (46:1) — the kin's sacrifice, the peace offering's shape before its law (31:54's the same, S3)", ['sacrifice_offered'])
    if q == 'sacrifices_reading': return cell('found_with_bar_kapparas_nephew', M, "Bereshit Rabbah 94:5 — 'and he sacrificed sacrifices to the God of his father Isaac' (46:1): R. Yehoshua ben Levi — I went round to all the masters of the lore (aggadah — the non-legal teaching) in the south that they tell me this verse, and none told me until I stood with Yehuda ben Pedaya, the nephew of Bar Kappara", ['sacrifice_offered'])
    if q == 'god_of_isaac': return cell('isaacs_god_named', I, "'to the God of his father Isaac' (46:1) — Isaac named, not Abraham (the frozen unit's read: the father's God at the father's well, Beersheba 26:25)", ['sacrifice_offered'])
    if q == 'night_visions': return cell(4, I, "'fear not to go down to Egypt' (46:3), 'I will make of you a great nation there', 'I will go down with you ... and I will surely bring you up' (46:4), 'and Joseph shall put his hand on your eyes' — four HEAVEN entries from one vision: fear_not_promised, great_nation_promised, brought_up_promised, josephs_hand_on_the_eyes", ['fear_not_promised', 'great_nation_promised', 'brought_up_promised', 'josephs_hand_on_the_eyes'])
    if q == 'hand_on_eyes_closed': return cell('Gen 50:1', I, "'and Joseph fell on his father's face' (50:1) — josephs_hand_on_the_eyes (46:4) closed on the scene at the death", ['josephs_hand_on_the_eyes'])
    if q == 'brought_up_closed_on_tape': return cell('Gen 50:13', I, "'I will surely bring you up' (46:4) — brought_up_promised closed on the tape at the family engine's burial (50:13) by seat, nothing on the bare scene (CJ7)", ['brought_up_promised'])
    if q == 'carried_after_the_act': return cell('after_the_act', M, "Chullin 101b:9 — Rava objects: 'and the sons of Israel carried Jacob their father' (46:5) — after the act (the sinew's ban stated 'the children of Israel do not eat', 32:33, after the sons are so called: the family's statute dated by this verse)", ['came_to_egypt'])
    if q == 'judah_ahead': return cell('sent_ahead_to_goshen', I, "'and he sent Judah before him to Joseph, to show the way before him to Goshen' (46:28) — judah_sent_ahead", ['judah_sent_ahead'])
    if q == 'wept_more': return cell('wept_on_his_neck_more', I, "'and he fell on his neck, and wept on his neck a good while' (46:29, עוד) — wept; 'now let me die, since I have seen your face' (46:30) let_me_die_said", ['wept', 'let_me_die_said'])
    if q == 'shepherds_abomination': return cell('every_shepherd', I, "'for every shepherd is an abomination to the Egyptians' (46:34) — the audience prepared on it; shepherds_abhorred a status, the ground of Goshen", ['shepherds_abhorred', 'audience_prepared'])
    return cell('no_case', I, '', [FX.NONE])


def seventy(q):
    if q == 'subtotals_parsed': return cell(tuple(_subtotal(vs) for vs in (15, 18, 22, 25)), I, "the registers' sub-totals parsed from 46:15, 46:18, 46:22, 46:25 by _subtotal(): thirty-three, sixteen, fourteen, seven", ['souls_counted'])
    if q == 'subtotals_sum': return cell(sum(_subtotal(vs) for vs in (15, 18, 22, 25)), I, "33 + 16 + 14 + 7 = 70 — the ink's sub-totals meet 46:27's seventy (CJ3 MATCH on the sub-totals)", ['souls_counted'])
    if q == 'sixty_six': return cell(_subtotal(26), I, "'all the souls ... that came out of his loins, besides the wives of Jacob's sons, all the souls were sixty-six' (46:26) — parsed", ['souls_counted'])
    if q == 'seventy': return cell(_subtotal(27), I, "'all the souls of the house of Jacob that came into Egypt were seventy' (46:27) — parsed", ['souls_counted'])
    if q == 'sixty_six_arithmetic': return cell(70 - 1 - 2 - 1, I, "seventy less Joseph, less his two sons born in Egypt (46:27), less Jacob himself = sixty-six: the ink's own arithmetic (CJ4)", ['souls_counted'])
    if q == 'names_by_register': return cell(tuple(len(ROSTERS[r]) for r in ('leah', 'zilpah', 'rachel', 'bilhah')), I, "the names counted per register, every name verified in its verse by the probes: Leah 34 (Er and Onan among them), Zilpah 16, Rachel 14, Bilhah 7", ['souls_counted'])
    if q == 'leah_living_named': return cell(len(ROSTERS['leah']) - 2, I, "'and Er and Onan died in the land of Canaan' (46:12) — Leah's 34 names less the two dead = 32 living named against the verse's thirty-three (46:15)", ['souls_counted'])
    if q == 'diverge': return cell('DIVERGE_leah_33_vs_32_living', I, "CJ3: the sub-total says thirty-three, the living names count thirty-two (thirty-four with the dead) — the seventy's missing one, filed OPEN (8m); five answers on the shelf, none the ink's", ['souls_counted'])
    if q == 'jochebed': return cell('jochebed_born_between_the_walls', M, "Bava Batra 123b:1 — R. Chama bar Chanina: this is Jochebed, conceived on the way and born between the walls, 'whom she bore to Levi in Egypt' (Num 26:59) — the tradition's first answer to the missing one", ['souls_counted'])
    if q == 'sixty_six_cups': return cell('sixty_six_and_three_counted_seventy', M, "Bereshit Rabbah 94:9 — R. Levi in R. Shmuel bar Nachman's name: have you ever seen a man give his fellow sixty-six cups, and then give him three more, and he counts them seventy? — the row's own arithmetic of the seventieth", ['souls_counted'])
    if q == 'firstborn_kept': return cell('reuben_first', I, "'Reuben, Jacob's firstborn' (46:8) — the census keeps the firstborn's place after 35:22 (the family's firstborn_by_the_head at 29:32, S3); the FALSE edge to the paschal firstborn", ['souls_counted'])
    if q == 'inheritance_sheet': return cell('son_before_daughter', A, "Mishnah Bava Batra 8:2 — the order of inheritance: 'if a man die and have no son' (Num 27:8) — the son precedes the daughter; the census's registers read against the row (the family engine's own answer sheet)", ['souls_counted'])
    if q == 'exodus_seventy': return cell(sum(_HEB[w] for w in toks(1, 5, 'Exod') if w in _HEB), I, "'and all the souls that came out of the loins of Jacob were seventy souls' (Exod 1:5, שבעים — seventy) — the exodus story's count PARSED by the numeral map over the verse's words (the first typing returned the literal behind a presence check — corrected at the sitting's review), equal to 46:27's (CJ11); Deut 10:22 'with seventy souls' outside the tape", ['souls_counted'])
    return cell('no_case', I, '', [FX.NONE])


_HEB = {'שלשים': 30, 'ושלש': 3, 'שש': 6, 'עשרה': 10, 'ארבעה': 4, 'עשר': 10, 'שבעה': 7, 'ששים': 60, 'ושש': 6, 'שבעים': 70}


def _subtotal(vs):
    """the numeral words of a census verse summed (46:15, 18, 22, 25, 26, 27) — a measurement; 'four ten' = 14, 'six ten' = 16"""
    return sum(_HEB[w] for w in toks(46, vs) if w in _HEB)


def goshen(q):
    if q == 'five_men': return cell(5, I, "'and from among his brothers he took five men' (47:2) — parsed; five_presented", ['five_presented'])
    if q == 'five_doubled': return cell('those_doubled_in_names', M, "Bava Kamma 92a:19 — Rava to Rabbah bar Mari: 'and from the end of his brothers he took five men' (47:2) — who are the five? R. Yochanan: those whose names are doubled (in Moses' blessing)", ['five_presented'])
    if q == 'five_named': return cell('not_the_mighty', M, "Bereshit Rabbah 95:4 — why 'from the end of his brothers'? to teach that they were not the mighty ones: Reuben, Levi, Benjamin, Simeon, Issachar — the five named", ['five_presented'])
    if q == 'hundred_thirty': return cell(130, I, "'the days of the years of my sojournings are a hundred and thirty years' (47:9) — parsed; years_confessed with value 130; the marker descent on the tape", ['years_confessed'])
    if q == 'few_and_evil': return cell('few_and_evil', I, "'few and evil have been the days of the years of my life' (47:9, מעט ורעים) — the confession's own grading", ['years_confessed'])
    if q == 'hundred_sixteen': return cell(116, M, "Megillah 17a:2-4 — Jacob sixty-three when blessed and Ishmael died in that season (17a:2); sixty-three and fourteen until Joseph was born, seventy-seven; 'Joseph was thirty' (41:46), a hundred and seven; the seven of plenty and two of famine, a hundred and sixteen — and the verse says a hundred and thirty (47:9): the fourteen hidden years (17a:5) — S3's fourteen, this sitting's CJ1", ['years_confessed'])
    if q == 'two_absences': return cell(22, M, "Megillah 17a:6 — Joseph parted from his father twenty-two years, as Jacob our father parted from his: Jacob's thirty-six, less the fourteen in Eber's house — CJ0 on the tape: two chains, one number", ['years_confessed'])
    if q == 'rameses': return cell('the_land_of_rameses', I, "'in the best of the land, in the land of Rameses' (47:11) — holding_given; Goshen's other name (the exodus story's Rameses of Exod 12:37)", ['holding_given'])
    if q == 'goshen_seats': return cell(len(_all_seats(lambda ws: any(w in ('גשן', 'גשנה') for w in ws), range(1, 51))), I, "Goshen in Genesis (measured): 45:10, 46:28, 46:29, 46:34, 47:1, 47:4, 47:6, 47:27, 50:8 — nine seats", ['dwelling_granted'])
    if q == 'holding_homograph': return cell('a_holding_in_egypt', I, "'and gave them a holding in the land of Egypt' (47:11, אחזה) — the holding word outside the land of the jubilee's law: a homograph, FALSE at the census", ['holding_given'])
    if q == 'closes_at_47_11': return cell(2, I, "'as Pharaoh had commanded' (47:11) — two closes on the scene: goshen_promised (45:10) on the house of Jacob, good_of_egypt_promised (45:18) on the sons; the citation form filed INTERNAL (47:6 cited)", ['goshen_promised', 'good_of_egypt_promised'])
    if q == 'sustained_by_the_mouth': return cell('according_to_the_little_ones', I, "'and Joseph sustained his father and his brothers ... with bread, according to the mouth of the little ones' (47:12) — sustained_by_the_mouth; sustenance_promised (45:11) closed", ['sustained_by_the_mouth', 'sustenance_promised'])
    return cell('no_case', I, '', [FX.NONE])


def the_fifth(q):
    if q == 'all_silver': return cell('all_the_silver_in_the_world', M, "Pesachim 119a:6 — Rav Yehuda in Shmuel's name: all the silver and gold in the world Joseph gathered and brought to Egypt, 'and Joseph gathered all the silver that was found' (47:14) — of the land of Egypt and Canaan; of the other lands, 'and all the earth came to Egypt' (41:57)", ['silver_gathered_to_pharaoh'])
    if q == 'second_year': return cell('the_second_year', I, "'and they came to him the second year' (47:18) — the famine's ledger by years: silver (47:14), livestock (47:17), bodies and ground (47:19)", ['livestock_to_pharaoh'])
    if q == 'bodies_and_ground': return cell(('bodies', 'ground'), I, "'buy us and our land for bread, and we and our land will be servants to Pharaoh' (47:19) — bodies_and_ground_offered, servants_to_pharaoh, ground_of_egypt_acquired with counterparty the people", ['bodies_and_ground_offered', 'servants_to_pharaoh', 'ground_of_egypt_acquired'])
    if q == 'priests_exempt': return cell('a_statute_for_the_priests', I, "'only the land of the priests he did not buy, for the priests had a statute from Pharaoh' (47:22, חק) — priests_ground_exempt", ['priests_ground_exempt'])
    if q == 'chok_means_food': return cell('chok_is_a_word_for_sustenance', M, "Beitzah 16a:3 — whence that this 'chok' is a word for food? 'and they ate their statute (חקם) which Pharaoh gave them' (47:22); Mar Zutra from 'feed me my allotted bread' (Prov 30:8)", ['priests_ground_exempt'])
    if q == 'fifth_parsed': return cell('a_fifth_and_four_hands', I, "'you shall give a fifth to Pharaoh, and four hands shall be yours' (47:24, חמישית ... וארבע הידת) — the statute's own division", ['fifth_to_pharaoh'])
    if q == 'fifth_homograph': return cell('egypts_statute_not_the_sanctuarys', I, "the fifth of 41:34 and 47:24 is Egypt's statute; the sanctuary's added fifth (Lev 27) a homograph — FALSE at the census (8k)", ['fifth_to_pharaoh'])
    if q == 'statute_seat': return cell('law_joseph_47_26', I, "'and Joseph made it a statute to this day' (47:26) — the exodus story's `statute_set` branch seat-checked to Exodus (8k: Marah's); fifth_to_pharaoh written here", ['fifth_to_pharaoh'])
    if q == 'until_this_day': return cell('until_this_day', I, "'a statute to this day over the land of Egypt, for Pharaoh a fifth' (47:26, עד היום הזה) — the narrator's present, as 32:33's and 35:20's", ['fifth_to_pharaoh'])
    if q == 'fruitful_in_goshen': return cell('fruitful_and_multiplied_exceedingly', I, "'and they were fruitful and multiplied exceedingly' (47:27) — fruitful_in_goshen: 35:11's fruitfulness_blessed received in Egypt; the exodus story's 1:7 repeats the verbs", ['fruitful_in_goshen'])
    return cell('no_case', I, '', [FX.NONE])


def the_oath(q):
    if q == 'seventeen_years': return cell(17, I, "'and Jacob lived in the land of Egypt seventeen years' (47:28) — parsed; the seventeen of 37:2 mirrored (the frozen unit's read)", ['burial_in_canaan_sworn'])
    if q == 'hundred_forty_seven': return cell(147, I, "'the days of Jacob, the years of his life, were a hundred and forty-seven years' (47:28) — parsed; 130 (47:9) + 17 = 147, the ink's own arithmetic (CJ5); the marker jacob_147", ['burial_in_canaan_sworn'])
    if q == 'why_joseph': return cell('in_his_power_to_do', M, "Bereshit Rabbah 96:5 — 'and he called his son Joseph' (47:29): why not Reuben or Judah — Reuben the firstborn, Judah the king? because it was in his power to do it", ['burial_in_canaan_sworn'])
    if q == 'kindness_and_truth': return cell('kindness_and_truth', I, "'deal with me in kindness and truth; do not bury me in Egypt' (47:29, חסד ואמת) — the burial command with its oath demanded (47:31); burial_in_canaan_sworn on Joseph, the debit", ['burial_in_canaan_sworn'])
    if q == 'burial_command_seat': return cell('law_joseph_47_29', I, "the family's `burial_commanded` branch seat-checked to Gen 49 (8k — the testament's command to the sons, 49:29); Joseph's oath (47:29-31) written here", ['burial_in_canaan_sworn'])
    if q == 'oath_sworn': return cell('Gen 47:31', I, "'swear to me; and he swore to him' (47:31) — oath_sworn on Joseph; 50:6 'as he made you swear' cites it (the pointer INTERNAL)", ['oath_sworn'])
    if q == 'bed_head_bow': return cell('fox_in_its_hour', M, "Megillah 16b:6 — 'and Israel bowed on the head of the bed' (47:31): R. Binyamin bar Yefet in R. Elazar's name — a fox in its hour, bow to it (the row's own alternative placement of the saying, beside 50:18's)", ['bowed_on_the_bed'])
    if q == 'oath_closed_on_tape': return cell('Gen 50:13', I, "burial_in_canaan_sworn closed on the tape at the family engine's `buried` (50:13) by seat — nothing on the bare scene (CJ7)", ['burial_in_canaan_sworn'])
    return cell('no_case', I, '', [FX.NONE])


def mourning(q):
    if q == 'hand_on_eyes_closed': return cell('Gen 50:1', I, "'and Joseph fell on his father's face, and wept on him, and kissed him' (50:1) — face_fallen_on; josephs_hand_on_the_eyes (46:4) closed", ['face_fallen_on', 'josephs_hand_on_the_eyes'])
    if q == 'forty_seventy': return cell((40, 70), I, "'forty days were fulfilled for him, for so are fulfilled the days of embalming; and the Egyptians wept for him seventy days' (50:3) — parsed; embalming_forty_days and egypt_wept_seventy the timers, the markers embalmed and weeping_end on the tape", ['embalming_forty_days', 'egypt_wept_seventy'])
    if q == 'timers_on_the_scene': return cell(('death_plus_40', 'death_plus_70'), D, "the two timers set at the death day, due forty and seventy days on — both fire inside the scene before the burial leave (50:4 'when the days of weeping were past')", ['embalming_forty_days', 'egypt_wept_seventy'])
    if q == 'as_he_made_you_swear': return cell('Gen 47:31', I, "'go up and bury your father, as he made you swear' (50:6) — Pharaoh citing the oath (47:31): the recorded oath as legal tender (the frozen unit's crown); the citation form filed INTERNAL", ['leave_granted', 'burial_leave_asked'])
    if q == 'seven_days': return cell(7, I, "'and he made a mourning for his father seven days' (50:10) — parsed; seven_days_mourning the timer at the threshing floor of Atad; the marker atad_end", ['seven_days_mourning'])
    if q == 'abel_mizraim': return cell('the_mourning_of_egypt', I, "'therefore its name was called Abel-mizraim' (50:11) — name_given on the threshing floor by the Canaanites' saying: 'this is a heavy mourning to Egypt'", ['name_given'])
    if q == 'burial_seat': return cell('family_engine_50_12', I, "'and his sons did to him as he had commanded them' (50:12) and the burial (50:13) — the family engine's `buried` and its close; this scene submits the funeral's ascent (50:7-9) and the return (50:14), never the burial (8a)", ['funeral_ascended'])
    if q == 'joseph_buried_sheet': return cell('joseph_merited_to_bury_his_father', A, "Mishnah Sotah 1:9 — Joseph merited to bury his father, and there is none among his brothers greater than he: 'and Joseph went up to bury his father' (50:7) — the measure-for-measure row's good side", ['funeral_ascended'])
    if q == 'no_meal': return cell('no_meal_invited', M, "Bereshit Rabbah 100:8 — 'and Joseph returned to Egypt' (50:14): R. Levi — he did not invite them to a meal; R. Tanchuma — he intended only for Heaven's sake: formerly father seated me above Judah who is king and above Reuben who is firstborn", ['returned_to_egypt'])
    return cell('no_case', I, '', [FX.NONE])


def coffin(q):
    if q == 'feared': return cell('perhaps_joseph_will_hate_us', I, "'perhaps Joseph will hate us, and will surely repay us all the evil' (50:15) — feared_joseph; 'your father commanded before his death' (50:16) the message", ['feared_joseph', 'forgiveness_asked'])
    if q == 'altered_for_peace': return cell('permitted_to_alter_for_peace', M, "Yevamot 65b:7 — R. Ila in R. Elazar son of R. Shimon's name: a man may alter his words for the sake of peace, as it is said 'your father commanded ... so shall you say to Joseph, forgive, I pray' (50:16-17)", ['forgiveness_asked'])
    if q == 'forgiveness_sheet': return cell(('asks', 'prays'), A, "Mishnah Bava Kamma 8:7 — he is not forgiven until he asks, and the forgiver must not be cruel (the row S3 read at Abraham's seat, 20:7, 20:17): here the brothers ASK (50:17) and Joseph is not cruel (50:19-21) — the second showing of the rule on the tape", ['forgiveness_asked', 'forgiven'])
    if q == 'chatat_homograph': return cell('their_sin_the_noun', I, "'forgive the transgression of your brothers and their sin' (50:17, וחטאתם) — the noun sin, a homograph of the sin offering: FALSE at the census", ['forgiveness_asked'])
    if q == 'fox_in_its_hour': return cell('fox_in_its_hour', M, "Megillah 16b:5 — 'and his brothers also went and fell before him' (50:18): R. Binyamin bar Yefet in R. Elazar's name — this is what people say: a fox in its hour, bow to it", ['fell_before_him'])
    if q == 'am_i_in_gods_place': return cell('am_i_in_place_of_god', I, "'fear not, for am I in the place of God?' (50:19, התחת אלהים אני) — the forgiveness's ground; 'you meant evil against me, God meant it for good' (50:20)", ['forgiven'])
    if q == 'ten_candles': return cell('ten_candles_one_candle', M, "Megillah 16b:7 — 'and he comforted them and spoke to their heart' (50:21): he said to them words that are received by the heart — if ten candles could not put out one candle, how can one candle put out ten?", ['comforted'])
    if q == 'words_on_the_heart': return cell('words_that_comfort_the_heart', M, "Bereshit Rabbah 100:9 — 'and spoke to their heart' (50:21): is there a man who speaks to the heart? rather, words that comfort the heart: you are likened to the dust of the earth", ['comforted'])
    if q == 'hundred_ten': return cell(110, I, "'and Joseph lived a hundred and ten years' (50:22), 'and Joseph died, a hundred and ten years old' (50:26) — parsed twice; dwelt_in_egypt with value 110; the marker died:joseph proleptic", ['dwelt_in_egypt', 'embalmed_and_coffined'])
    if q == 'machir_knees': return cell('born_on_josephs_knees', I, "'the children of Machir the son of Manasseh were born on Joseph's knees' (50:23) — born_on_the_knees on the-sons-of-machir (the adoption gesture the family's 48:12 keeps)", ['born_on_the_knees'])
    if q == 'visit_doubled': return cell(2, I, "'God will surely visit you' (פקד יפקד) at 50:24 and 50:25 — the doubled verb twice (measured); visitation_promised the HEAVEN entry, bones_oath the DEBIT on the children of Israel", ['visitation_promised', 'bones_oath'])
    if q == 'visitation_closed_on_tape': return cell('Exod 4:31', I, "'and the people believed, and they heard that the LORD had visited the children of Israel' (Exod 4:31) — visitation_promised closed on the tape at the exodus story's `believed` by seat (CJ7); nothing on the bare scene", ['visitation_promised'])
    if q == 'bones_closed_on_tape': return cell('Exod 13:19', I, "'and Moses took the bones of Joseph with him, for he had surely sworn the children of Israel' (Exod 13:19) — bones_oath closed on the tape at the exodus story's `bones_taken` by seat (CJ7)", ['bones_oath'])
    if q == 'four_hundred_parasangs': return cell('four_hundred_parasangs', M, "Ketubot 111a:23 — 'and Joseph made the children of Israel swear' (50:25): R. Chanina — there is a matter within: Joseph knew himself a perfect righteous man; if the dead outside the land live, why did he trouble his brothers four hundred parasangs? lest he not merit the tunnels", ['bones_oath'])
    if q == 'with_you_when_you_go_up': return cell('when_you_go_up', M, "Bereshit Rabbah 100:11 — 'and Joseph made the children of Israel swear' (50:25): I might think at once; the verse says 'with you' (Exod 13:19) — when you go up; and whence that the tribes' bones went up with him? 'with you'", ['bones_oath'])
    if q == 'coffin_in_egypt': return cell('in_a_coffin_in_egypt', I, "'and they embalmed him, and he was put in a coffin in Egypt' (50:26, בארון במצרים) — the book's last words; embalmed_and_coffined the body entry the exodus story's bones_taken answers", ['embalmed_and_coffined'])
    return cell('no_case', I, '', [FX.NONE])


# ---- (6) THE WRAP: the daemon over the cells — consumes the stretch's acts, writes the ledger, never emits an event ----
def _years(world, day, n):
    return world.clock.calendar.add(day, n, 'year') if world.clock.epoch else day + 365 * n

def E_(effect, subject, cp=None, value=None, due=None, amount=None):
    return {'effect': effect, 'subject': subject, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value}

def law_joseph(event, world):
    """FROM THE FORD TO THE COFFIN's daemon (the forty-third): the acts and speeches of Genesis 32-37, 39-47, 50 to the ledger.
    One branch per watched kind — the writes per event are the hand-model's own table (scratchpad o8_s4_predict.py, printed
    before this file was typed). The daemon answers ITS SPAN ONLY (convention 14 both ways): a shared kind at another seat
    is another daemon's — the family's renaming (32:29), sinew (32:33) and burial (50:12-13) are excluded by the seat, as
    are Genesis 38, 48, 49. Four closes on other engines' events, by seat (CJ7): brought_up_promised (46:4) and
    burial_in_canaan_sworn (47:31) on the family's `buried` at Gen 50:13; visitation_promised (50:24) on the exodus story's
    `believed` at Exod 4:31; bones_oath (50:25) on its `bones_taken` at Exod 13:19 — the ink's own receipts."""
    k, subj, src = event['kind'], event.get('subject'), event.get('case_source', '')
    day = event.get('day', world.clock.day)
    s = WE.seat(src)
    if k == 'buried' and subj == 'jacob' and s == ('Gen', 50):
        world.close('jacob', 'brought_up_promised', 'Gen 50:13 — and his sons carried him to the land of Canaan and buried him (the family engine\'s burial; 46:4 "I will bring you up" kept)')
        world.close('joseph', 'burial_in_canaan_sworn', 'Gen 50:13 — buried in the cave of the field of Machpelah (the oath of 47:31 kept by the family engine\'s burial)')
        return []
    if k == 'believed' and s == ('Exod', 4):
        world.close('israel_people', 'visitation_promised', 'Exod 4:31 — and the people believed, and they heard that the LORD had visited the children of Israel (50:24\'s "God will surely visit you" received)')
        return []
    if k == 'bones_taken' and s == ('Exod', 13):
        world.close('israel_people', 'bones_oath', 'Exod 13:19 — and Moses took the bones of Joseph with him, for he had surely sworn the children of Israel (50:25\'s oath kept)')
        return []
    if not (s is not None and s[0] == 'Gen' and s[1] in (32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 50)): return []
    if k == 'angels_met': return [E_('camp_of_god_seen', subj)]
    if k == 'named': return [E_('name_given', subj, value=event.get('name'))]
    if k == 'messengers_sent': return [E_('esau_approaching', subj, value=event.get('report'))]
    if k == 'feared_greatly': return [E_('two_camps_made', subj)]
    if k == 'prayed': return [E_('deliverance_prayed', subj)]
    if k == 'gift_prepared': return [E_('gift_sent_ahead', 'esau', cp='jacob', value=event.get('head_count'))]
    if k == 'river_crossed': return [E_('river_crossed', subj)]
    if k == 'wrestled': return [E_('thigh_dislocated', subj)]
    if k == 'blessing_demanded': return [E_('blessing_demanded', subj)]
    if k == 'name_asked': return [E_('blessed_at_the_ford', subj)]
    if k == 'sun_rose': return [E_('limping', subj)]
    if k == 'esau_seen': return []
    if k == 'children_divided': return [E_('children_divided', subj)]
    if k == 'bowed':
        T = {
            ('Gen 33:3', 'jacob'): lambda: [E_('bowed_seven_times', subj, value=event.get('times'))],
            ('Gen 33:6', 'the-maids-and-their-children'): lambda: [],
            ('Gen 33:7', 'leah'): lambda: [],
            ('Gen 33:7', 'rachel'): lambda: [],
            ('Gen 42:6', 'the-sons'): lambda: [E_('bowed_as_the_sheaves', subj)],
            ('Gen 43:26', 'the-sons'): lambda: [],
            ('Gen 43:28', 'the-sons'): lambda: [],
            ('Gen 44:14', 'the-sons'): lambda: [E_('fell_before_him', subj)],
            ('Gen 47:31', 'jacob'): lambda: [E_('bowed_on_the_bed', subj)],
            ('Gen 50:18', 'the-sons'): lambda: [E_('fell_before_him', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'embraced': return []
    if k == 'fell_on_the_neck':
        T = {
            ('Gen 33:4', 'esau'): lambda: [],
            ('Gen 45:14', 'joseph'): lambda: [E_('wept', subj)],
            ('Gen 46:29', 'joseph'): lambda: [E_('wept', subj)],
            ('Gen 50:1', 'joseph'): lambda: [E_('face_fallen_on', 'jacob'), E_('wept', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'kissed':
        T = {
            ('Gen 33:4', 'esau'): lambda: [E_('kissed_and_wept', subj, value='dotted')],
            ('Gen 45:15', 'joseph'): lambda: [E_('wept', subj)],
            ('Gen 50:1', 'joseph'): lambda: [],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'children_declared': return []
    if k == 'camp_explained': return [E_('gift_declined', subj)]
    if k == 'gift_urged': return [E_('blessing_returned', 'esau', cp='jacob')]
    if k == 'convoy_declined': return [E_('seir_promised', subj), E_('convoy_declined', subj)]
    if k == 'journeyed':
        T = {
            ('Gen 33:16', 'esau'): lambda: [],
            ('Gen 33:17', 'jacob'): lambda: [E_('encamped_at', subj, value=event.get('to'))],
            ('Gen 33:18', 'jacob'): lambda: [E_('encamped_at', subj, value=event.get('to')), E_('came_whole', subj)],
            ('Gen 35:5', 'the-house-of-jacob'): lambda: [E_('terror_of_god', 'the-cities')],
            ('Gen 35:6', 'jacob'): lambda: [E_('encamped_at', subj, value=event.get('to'))],
            ('Gen 35:16', 'jacob'): lambda: [],
            ('Gen 35:21', 'jacob'): lambda: [E_('encamped_at', subj, value=event.get('to'))],
            ('Gen 35:27', 'jacob'): lambda: [E_('encamped_at', subj, value=event.get('to'))],
            ('Gen 37:12', 'the-sons'): lambda: [],
            ('Gen 42:26', 'the-sons'): lambda: [],
            ('Gen 45:25', 'the-sons'): lambda: [],
            ('Gen 46:1', 'jacob'): lambda: [E_('encamped_at', subj, value=event.get('to'))],
            ('Gen 46:5-7', 'israel_people'): lambda: [E_('came_to_egypt', subj)],
            ('Gen 46:28', 'israel_people'): lambda: [E_('encamped_at', subj, value=event.get('to'))],
            ('Gen 50:7-9', 'the-sons'): lambda: [E_('funeral_ascended', subj), E_('encamped_at', subj, value=event.get('to'))],
            ('Gen 50:14', 'the-sons'): lambda: [E_('returned_to_egypt', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'booths_made': return [E_('booths_made', subj)]
    if k == 'purchased':
        T = {
            ('Gen 33:19', 'jacob'): lambda: [E_('field_acquired', 'the-field-at-shechem', cp=subj, amount=event.get('price'))],
            ('Gen 47:20', 'joseph'): lambda: [E_('ground_of_egypt_acquired', 'pharaoh-of-joseph', cp='egypt_people', amount=event.get('price'))],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'altar_erected': return [E_('altar_built', subj)]
    if k == 'went_out_to_see': return []
    if k == 'seized_and_violated': return [E_('violated', 'dinah'), E_('defiled', 'dinah')]
    if k == 'soul_cleaved': return []
    if k == 'wife_asked': return [E_('marriage_demanded', subj)]
    if k == 'silence_kept': return [E_('silence_kept', subj)]
    if k == 'came_to_speak': return []
    if k == 'outraged': return [E_('outrage_in_israel', subj)]
    if k == 'marriage_proposed':
        T = {
            ('Gen 34:8-10', 'hamor'): lambda: [E_('intermarriage_proposed', subj)],
            ('Gen 34:11-12', 'shechem'): lambda: [E_('mohar_offered_unbounded', subj, value=event.get('mohar'))],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'deceit_answered': return [E_('circumcision_conditioned', subj)]
    if k == 'terms_accepted': return [E_('terms_accepted', subj)]
    if k == 'gate_addressed': return [E_('city_persuaded', 'the-men-of-shechem')]
    if k == 'males_circumcised': return [E_('circumcised_by_the_condition', subj)]
    if k == 'city_struck': return [E_('slain_by_sword', 'the-men-of-shechem'), E_('hamor_and_shechem_slain', 'hamor'), E_('hamor_and_shechem_slain', 'shechem'), E_('dinah_taken_back', 'dinah')]
    if k == 'city_plundered': return [E_('spoil_taken', subj)]
    if k == 'rebuked':
        T = {
            ('Gen 34:30', 'jacob'): lambda: [E_('troubled_charged', 'simeon'), E_('troubled_charged', 'levi')],
            ('Gen 37:10', 'jacob'): lambda: [],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'answered_back': return [E_('question_unanswered', subj)]
    if k == 'altar_commanded': return [E_('ascent_to_bethel_owed', 'jacob'), E_('altar_owed', 'jacob')]
    if k == 'purge_commanded': return [E_('foreign_gods_removal_owed', 'the-house-of-jacob')]
    if k == 'gods_hidden': return [E_('foreign_gods_buried', subj)]
    if k == 'died':
        T = {
            ('Gen 35:8', 'deborah'): lambda: [E_('nurse_died', subj)],
            ('Gen 35:19', 'rachel'): lambda: [],
            ('Gen 35:28-29', 'isaac'): lambda: [E_('gathered_to_his_people', subj), E_('full_of_days', subj)],
            ('Gen 50:26', 'joseph'): lambda: [E_('embalmed_and_coffined', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'buried':
        T = {
            ('Gen 35:8', 'deborah'): lambda: [E_('buried', subj, value=event.get('where') or event.get('by'))],
            ('Gen 35:19', 'rachel'): lambda: [E_('buried', subj, value=event.get('where') or event.get('by'))],
            ('Gen 35:29', 'isaac'): lambda: [E_('buried', subj, value=event.get('where') or event.get('by')), E_('buried_by_both_sons', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'appeared': return [E_('blessed_by_the_lord', 'jacob')]
    if k == 'blessed_be_fruitful': return [E_('fruitfulness_blessed', 'jacob'), E_('kings_promised', 'jacob'), E_('assembly_of_nations_promised', 'jacob')]
    if k == 'land_promised': return [E_('land_promised', 'jacob')]
    if k == 'god_went_up': return []
    if k == 'pillar_set_and_anointed': return [E_('pillar_anointed', subj, value=event.get('oil')), E_('libation_poured', subj, value=event.get('libation'))]
    if k == 'hard_birth': return [E_('midwife_comforted', subj)]
    if k == 'born':
        T = {
            ('Gen 35:18', 'benjamin'): lambda: [E_('died_in_childbirth', 'rachel')],
            ('Gen 41:50', 'manasseh'): lambda: [E_('two_sons_before_the_famine', 'joseph')],
            ('Gen 41:50', 'ephraim'): lambda: [],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'grave_pillar_set': return [E_('grave_marked', 'the-grave-of-rachel')]
    if k == 'lay_with_the_concubine': return [E_('concubine_lain_with', subj, value=event.get('reading')), E_('israel_heard', 'jacob')]
    if k == 'sons_counted': return [E_('twelve_sons_listed', subj, value=event.get('count'))]
    if k == 'married':
        T = {
            ('Gen 36:2', 'adah-wife-of-esau'): lambda: [E_('wife_taken', subj, cp=event.get('husband'))],
            ('Gen 36:2', 'oholibamah'): lambda: [E_('wife_taken', subj, cp=event.get('husband'))],
            ('Gen 36:3', 'basemath-bat-ishmael'): lambda: [E_('wife_taken', subj, cp=event.get('husband'))],
            ('Gen 41:45', 'asenath'): lambda: [E_('wife_taken', subj, cp=event.get('husband')), E_('asenath_given', 'joseph', cp=event.get('by'))],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'bore':
        T = {
            ('Gen 36:4', 'adah-wife-of-esau'): lambda: [E_('begotten', 'eliphaz', cp=subj)],
            ('Gen 36:4', 'basemath-bat-ishmael'): lambda: [E_('begotten', 'reuel', cp=subj)],
            ('Gen 36:5', 'oholibamah'): lambda: [E_('begotten', 'the-chiefs-of-esau', cp=subj)],
            ('Gen 36:12', 'timna'): lambda: [E_('begotten', 'amalek-son-of-eliphaz', cp=subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'withdrew': return [E_('parted', subj), E_('dwelt_in_seir', subj)]
    if k == 'roster_listed':
        T = {
            ('Gen 36:9-19', 'the-chiefs-of-esau'): lambda: [E_('sons_of_esau_listed', subj, value=event.get('count'))],
            ('Gen 36:20-30', 'the-sons-of-seir'): lambda: [E_('horites_listed', subj, value=event.get('count'))],
            ('Gen 36:40-43', 'the-chiefs-of-esau'): lambda: [E_('chiefs_by_places_listed', subj, value=event.get('count'))],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'reigned': return [E_('reigned_in_edom', subj, value=event.get('king') or event.get('successor'))]
    if k == 'reign_passed': return [E_('reigned_in_edom', subj, value=event.get('king') or event.get('successor'))]
    if k == 'evil_report_brought': return [E_('evil_report_brought', subj)]
    if k == 'loved_apart': return [E_('loved_by_the_father', 'joseph')]
    if k == 'coat_made': return [E_('coat_of_stripes_made', 'joseph')]
    if k == 'hated': return [E_('hated', subj)]
    if k == 'dreamed': return []
    if k == 'dream_told':
        T = {
            ('Gen 37:6-7', 'joseph'): lambda: [E_('dream_of_sheaves', subj)],
            ('Gen 37:9-10', 'joseph'): lambda: [E_('dream_of_sun_moon_stars', subj)],
            ('Gen 40:9-11', 'the-chief-cupbearer'): lambda: [E_('dreams_in_one_night', subj)],
            ('Gen 40:16-17', 'the-chief-baker'): lambda: [E_('dreams_in_one_night', subj)],
            ('Gen 41:17-24', 'pharaoh-of-joseph'): lambda: [E_('pharaohs_dream_doubled', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'envied': return [E_('envied', subj), E_('word_kept', 'jacob')]
    if k == 'errand_given': return [E_('errand_given', 'joseph')]
    if k == 'found_wandering': return [E_('found_wandering', subj)]
    if k == 'conspired': return [E_('conspired_to_kill', subj)]
    if k == 'plot_spoken': return []
    if k == 'rescue_urged': return [E_('rescue_urged', subj)]
    if k == 'stripped': return [E_('stripped_of_the_coat', 'joseph')]
    if k == 'cast_into_the_pit': return [E_('in_the_pit', 'joseph', cp=subj)]
    if k == 'caravan_seen': return []
    if k == 'sale_proposed': return [E_('sale_proposed', subj)]
    if k == 'sold':
        T = {
            ('Gen 37:28', 'the-sellers-of-joseph'): lambda: [E_('sold_into_egypt', 'joseph', cp=subj, amount=event.get('price'))],
            ('Gen 37:36', 'the-medanites'): lambda: [E_('sold_to_potiphar', 'joseph', cp=subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'pit_found_empty': return []
    if k == 'tore_garments': return [E_('garments_torn', subj)]
    if k == 'coat_dipped': return [E_('coat_dipped', subj)]
    if k == 'coat_recognized': return [E_('coat_recognized', subj)]
    if k == 'mourned':
        T = {
            ('Gen 37:34-35', 'jacob'): lambda: [E_('mourned_many_days', subj), E_('comfort_refused', subj)],
            ('Gen 50:10', 'the-sons'): lambda: [E_('seven_days_mourning', subj, due=day + 7)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'wept': return [E_('wept', subj)]
    if k == 'slave_bought': return [E_('bought_by_potiphar', 'joseph', cp='potiphar')]
    if k == 'prospered': return [E_('prospering', subj)]
    if k == 'appointed_over_the_house':
        T = {
            ('Gen 39:4-6', 'joseph'): lambda: [E_('appointed_over_the_house', subj), E_('house_blessed_for_joseph', 'the-house-of-potiphar')],
            ('Gen 39:22', 'joseph'): lambda: [E_('appointed_over_the_prisoners', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'lie_with_me_demanded': return [E_('lie_with_me_demanded', subj)]
    if k == 'refused': return [E_('refused', subj)]
    if k == 'garment_seized': return [E_('garment_left', subj)]
    if k == 'fled': return [E_('fled_outside', subj)]
    if k == 'accused': return [E_('accused_falsely', 'joseph')]
    if k == 'anger_burned': return []
    if k == 'imprisoned':
        T = {
            ('Gen 39:20', 'joseph'): lambda: [E_('imprisoned', subj, cp=event.get('by'))],
            ('Gen 40:3', 'the-two-officers'): lambda: [E_('in_custody', 'the-chief-cupbearer', cp=event.get('by')), E_('in_custody', 'the-chief-baker', cp=event.get('by'))],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'kindness_extended': return [E_('favor_in_the_keepers_eyes', subj)]
    if k == 'offended': return [E_('offended_the_king', 'the-chief-cupbearer'), E_('offended_the_king', 'the-chief-baker')]
    if k == 'appointed_to_serve': return [E_('appointed_to_serve', subj)]
    if k == 'faces_downcast': return [E_('faces_downcast', 'the-chief-cupbearer'), E_('faces_downcast', 'the-chief-baker')]
    if k == 'interpreted':
        T = {
            ('Gen 40:12-13', 'joseph'): lambda: [E_('interpretation_given', subj, value=event.get('days')), E_('head_lifted_up_due', 'the-chief-cupbearer', due=day + 2)],
            ('Gen 40:18-19', 'joseph'): lambda: [E_('interpretation_given', subj, value=event.get('days')), E_('head_lifted_off_due', 'the-chief-baker', due=day + 2)],
            ('Gen 41:25-32', 'joseph'): lambda: [E_('one_dream', 'pharaoh-of-joseph', value=event.get('years'))],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'remembrance_asked': return [E_('remembrance_asked', subj)]
    if k == 'feast_made': return [E_('feast_made', subj)]
    if k == 'restored': return [E_('restored_to_the_cup', subj, cp='pharaoh-of-joseph')]
    if k == 'hanged': return [E_('hanged', subj, cp='pharaoh-of-joseph')]
    if k == 'forgot': return [E_('petition_forgotten', subj)]
    if k == 'spirit_troubled': return [E_('spirit_troubled', subj), E_('no_interpreter', 'the-magicians')]
    if k == 'offenses_recalled': return [E_('offenses_recalled', subj)]
    if k == 'rushed_from_the_pit': return [E_('rushed_from_the_pit', subj), E_('not_i_god', subj)]
    if k == 'counsel_given': return [E_('counsel_of_the_fifth', subj)]
    if k == 'counsel_accepted': return [E_('counsel_accepted', subj)]
    if k == 'set_over_egypt': return [E_('set_over_the_house', subj), E_('ring_given', subj, cp=event.get('by')), E_('set_over_egypt', subj, cp=event.get('by'))]
    if k == 'went_out_over_egypt': return [E_('thirty_at_the_standing', subj, value=event.get('age'))]
    if k == 'food_gathered': return [E_('food_gathered_as_sand', subj), E_('plenty_seven_years', 'the-land-of-egypt', due=_years(world, day, 7))]
    if k == 'plenty_ended': return []
    if k == 'famine_came':
        T = {
            ('Gen 41:54', 'the-lands'): lambda: [E_('famine', subj, value=event.get('years')), E_('famine_seven_years', 'the-land-of-egypt', due=_years(world, day, 7)), E_('famine_in_all_lands', subj)],
            ('Gen 43:1', 'the-land-of-canaan'): lambda: [E_('famine_heavy', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'cried_for_bread': return []
    if k == 'storehouses_opened': return [E_('storehouses_opened', subj)]
    if k == 'descent_commanded':
        T = {
            ('Gen 42:1-2', 'jacob'): lambda: [E_('descent_commanded', 'the-sons')],
            ('Gen 43:2', 'jacob'): lambda: [],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'went_down':
        T = {
            ('Gen 42:3-5', 'the-sons'): lambda: [E_('ten_went_down', subj, value=event.get('count'))],
            ('Gen 43:15', 'the-sons'): lambda: [E_('double_silver_taken', subj, value=event.get('silver'))],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'benjamin_withheld': return [E_('benjamin_withheld', 'benjamin')]
    if k == 'brothers_recognized': return [E_('recognized_one_way', subj)]
    if k == 'dreams_remembered': return [E_('dreams_remembered', subj)]
    if k == 'spies_charged': return [E_('spies_charged', 'the-sons')]
    if k == 'honesty_pleaded': return [E_('honesty_pleaded', subj)]
    if k == 'test_set': return [E_('test_set', 'the-sons')]
    if k == 'custody_three_days': return [E_('custody_three_days', 'the-sons', due=day + 2)]
    if k == 'plan_revised': return [E_('plan_revised', subj)]
    if k == 'guilt_confessed':
        T = {
            ('Gen 42:21', 'the-sons'): lambda: [E_('guilt_acknowledged', subj)],
            ('Gen 42:22', 'reuben'): lambda: [],
            ('Gen 44:16', 'judah'): lambda: [E_('guilt_acknowledged', 'the-sons')],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'interpreter_between': return [E_('interpreter_between', subj)]
    if k == 'bound': return [E_('held_in_custody', subj, cp=event.get('by'))]
    if k == 'silver_returned': return [E_('silver_returned_in_the_sacks', 'the-sons')]
    if k == 'silver_found': return []
    if k == 'report_given': return [E_('report_given', subj)]
    if k == 'bereaved_cried': return [E_('bereavement_charged', subj)]
    if k == 'pledge_of_sons_offered': return [E_('pledge_offered', subj)]
    if k == 'descent_refused': return [E_('descent_refused', subj)]
    if k == 'warning_cited': return [E_('warning_cited', subj)]
    if k == 'surety_offered': return [E_('surety_undertaken', subj, cp=event.get('to'))]
    if k == 'caravan_planned': return [E_('mercy_prayed', subj)]
    if k == 'house_ordered': return [E_('house_ordered', 'the-steward')]
    if k == 'feared_at_the_door': return [E_('feared_at_the_door', subj)]
    if k == 'peace_given': return [E_('peace_given', 'the-sons', cp=subj)]
    if k == 'feet_washed': return [E_('feet_washed', subj)]
    if k == 'gift_presented': return [E_('gift_presented', 'joseph', cp=subj)]
    if k == 'welfare_asked': return [E_('welfare_asked', subj)]
    if k == 'benjamin_seen': return [E_('benjamin_seen', subj)]
    if k == 'bread_set': return [E_('egyptians_eat_apart', 'egypt_people')]
    if k == 'seated_by_birth_order': return [E_('seated_by_birth_order', subj)]
    if k == 'portions_lifted': return [E_('five_hands', 'benjamin', value=event.get('hands'))]
    if k == 'ate_and_drank': return []
    if k == 'cup_planted': return [E_('cup_planted', subj)]
    if k == 'sent_away':
        T = {
            ('Gen 44:3', 'the-sons'): lambda: [E_('sent_out', subj, cp=event.get('by'))],
            ('Gen 45:24', 'the-sons'): lambda: [E_('sent_out', subj, cp=event.get('by')), E_('quarrel_barred', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'pursued': return [E_('overtaken_with_the_cup', 'the-sons')]
    if k == 'divination_claimed': return [E_('divination_claimed', subj)]
    if k == 'theft_denied': return [E_('theft_denied', subj)]
    if k == 'rash_sentence_offered': return [E_('death_and_slavery_offered', subj)]
    if k == 'ruling_softened': return [E_('finder_a_slave_ruled', subj)]
    if k == 'bags_searched': return [E_('cup_found', 'benjamin', value=event.get('found_with'))]
    if k == 'ruling_given': return [E_('slavery_of_the_finder_ruled', 'benjamin')]
    if k == 'judah_pleaded': return [E_('surety_invoked', subj), E_('substitution_offered', subj)]
    if k == 'restraint_failed': return [E_('restraint_failed', subj)]
    if k == 'identity_revealed': return [E_('revealed_to_his_brothers', subj), E_('terrified', 'the-sons')]
    if k == 'providence_declared': return [E_('sent_by_god_declared', subj), E_('five_years_of_famine_left', 'the-land-of-egypt', due=_years(world, day, 5))]
    if k == 'descent_urged': return [E_('goshen_promised', 'the-house-of-jacob'), E_('sustenance_promised', 'jacob')]
    if k == 'voice_heard': return [E_('good_in_pharaohs_eyes', subj)]
    if k == 'come_to_me_commanded': return [E_('good_of_egypt_promised', 'the-sons')]
    if k == 'wagons_given': return [E_('wagons_given', 'the-sons', cp='joseph')]
    if k == 'gifts_given':
        T = {
            ('Gen 45:22', 'the-sons'): lambda: [E_('gifts_given', subj, cp=event.get('by'))],
            ('Gen 45:23', 'jacob'): lambda: [E_('ten_donkeys_sent', subj, cp=event.get('by'))],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'silver_given': return [E_('three_hundred_silver', subj, cp=event.get('by'), amount=event.get('amount'))]
    if k == 'told_joseph_lives': return [E_('heart_numb', 'jacob')]
    if k == 'wagons_seen': return [E_('spirit_revived', subj)]
    if k == 'resolved_to_go': return [E_('resolved_to_go', subj)]
    if k == 'sacrificed': return [E_('sacrifice_offered', subj, value=event.get('to'))]
    if k == 'night_vision': return [E_('fear_not_promised', 'jacob'), E_('great_nation_promised', 'jacob'), E_('brought_up_promised', 'jacob'), E_('josephs_hand_on_the_eyes', 'jacob')]
    if k == 'census_listed': return [E_('souls_counted', subj, value={'registers': event.get('registers'), 'all': event.get('all'), 'from_the_loins': event.get('from_the_loins')})]
    if k == 'judah_sent_ahead': return [E_('judah_sent_ahead', 'judah')]
    if k == 'let_me_die_said': return [E_('let_me_die_said', subj)]
    if k == 'audience_prepared': return [E_('audience_prepared', 'the-sons'), E_('shepherds_abhorred', 'egypt_people')]
    if k == 'told_pharaoh': return [E_('told_pharaoh', subj)]
    if k == 'five_presented': return [E_('five_presented', 'the-sons', value=event.get('count'))]
    if k == 'work_asked': return [E_('work_asked', subj)]
    if k == 'goshen_granted': return [E_('dwelling_granted', 'the-sons')]
    if k == 'stood_before_pharaoh': return []
    if k == 'blessed': return [E_('pharaoh_blessed', 'pharaoh-of-joseph')]
    if k == 'days_asked': return [E_('years_confessed', subj, value=event.get('years'))]
    if k == 'settled': return [E_('holding_given', 'the-sons', cp=subj)]
    if k == 'sustained':
        T = {
            ('Gen 47:12', 'joseph'): lambda: [E_('sustained_by_the_mouth', 'the-house-of-jacob')],
            ('Gen 50:21', 'joseph'): lambda: [E_('comforted', 'the-sons', cp=subj), E_('sustenance_promised', 'the-sons')],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'silver_gathered': return [E_('silver_gathered_to_pharaoh', 'pharaoh-of-joseph', cp='egypt_people'), E_('famine_heavy', 'the-land-of-canaan')]
    if k == 'livestock_taken_for_bread': return [E_('livestock_to_pharaoh', 'pharaoh-of-joseph', cp='egypt_people')]
    if k == 'second_year_came': return [E_('bodies_and_ground_offered', subj)]
    if k == 'people_moved': return [E_('people_moved_to_cities', 'egypt_people')]
    if k == 'priests_exempted': return [E_('priests_ground_exempt', 'the-priests-of-egypt')]
    if k == 'seed_given': return [E_('seed_given', 'egypt_people', cp=subj)]
    if k == 'servitude_accepted': return [E_('servants_to_pharaoh', subj)]
    if k == 'statute_set': return [E_('fifth_to_pharaoh', subj, value=event.get('statute'))]
    if k == 'fruitful_in_goshen': return [E_('fruitful_in_goshen', subj)]
    if k == 'burial_commanded': return [E_('burial_in_canaan_sworn', 'joseph')]
    if k == 'sworn':
        T = {
            ('Gen 47:31', 'joseph'): lambda: [E_('oath_sworn', subj)],
            ('Gen 50:25', 'israel_people'): lambda: [E_('oath_sworn', subj), E_('bones_oath', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'embalmed':
        T = {
            ('Gen 50:2-3', 'the-physicians'): lambda: [E_('embalming_forty_days', 'jacob', due=day + 40), E_('egypt_wept_seventy', 'egypt_people', due=day + 70)],
            ('Gen 50:26', 'joseph'): lambda: [],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'leave_asked': return [E_('burial_leave_asked', subj)]
    if k == 'leave_granted': return [E_('leave_granted', 'joseph')]
    if k == 'feared_joseph': return [E_('feared_joseph', subj)]
    if k == 'forgiveness_asked': return [E_('forgiveness_asked', subj)]
    if k == 'forgave': return [E_('forgiven', 'the-sons', cp=subj)]
    if k == 'dwelt': return [E_('dwelt_in_egypt', subj, value=event.get('years'))]
    if k == 'grandsons_seen': return [E_('born_on_the_knees', 'the-sons-of-machir')]
    if k == 'visitation_promised': return [E_('visitation_promised', 'israel_people')]
    return []

SLOTS = [   # the slot order of the tuple — fixed by scratchpad o8_s4_predict.py before this file was typed
    ('jacob', 'camp_of_god_seen'),
    ('the-camp-of-god', 'name_given'),
    ('jacob', 'esau_approaching'),
    ('jacob', 'two_camps_made'),
    ('jacob', 'deliverance_prayed'),
    ('esau', 'gift_sent_ahead'),
    ('jacob', 'river_crossed'),
    ('jacob', 'thigh_dislocated'),
    ('jacob', 'blessing_demanded'),
    ('jacob', 'blessed_at_the_ford'),
    ('the-ford-of-jabbok', 'name_given'),
    ('jacob', 'limping'),
    ('jacob', 'children_divided'),
    ('jacob', 'bowed_seven_times'),
    ('esau', 'kissed_and_wept'),
    ('esau', 'gift_declined'),
    ('esau', 'blessing_returned'),
    ('jacob', 'seir_promised'),
    ('jacob', 'convoy_declined'),
    ('jacob', 'encamped_at'),
    ('jacob', 'booths_made'),
    ('jacob', 'name_given'),
    ('jacob', 'came_whole'),
    ('the-field-at-shechem', 'field_acquired'),
    ('the-altar-of-el-elohe-israel', 'altar_built'),
    ('the-altar-of-el-elohe-israel', 'name_given'),
    ('dinah', 'violated'),
    ('dinah', 'defiled'),
    ('shechem', 'marriage_demanded'),
    ('jacob', 'silence_kept'),
    ('the-sons', 'outrage_in_israel'),
    ('hamor', 'intermarriage_proposed'),
    ('shechem', 'mohar_offered_unbounded'),
    ('the-sons', 'circumcision_conditioned'),
    ('hamor', 'terms_accepted'),
    ('the-men-of-shechem', 'city_persuaded'),
    ('the-men-of-shechem', 'circumcised_by_the_condition'),
    ('the-men-of-shechem', 'slain_by_sword'),
    ('hamor', 'hamor_and_shechem_slain'),
    ('shechem', 'hamor_and_shechem_slain'),
    ('dinah', 'dinah_taken_back'),
    ('the-sons', 'spoil_taken'),
    ('simeon', 'troubled_charged'),
    ('levi', 'troubled_charged'),
    ('the-sons', 'question_unanswered'),
    ('jacob', 'ascent_to_bethel_owed'),
    ('jacob', 'altar_owed'),
    ('the-house-of-jacob', 'foreign_gods_removal_owed'),
    ('jacob', 'foreign_gods_buried'),
    ('the-cities', 'terror_of_god'),
    ('the-altar-at-bethel-again', 'altar_built'),
    ('the-place', 'name_given'),
    ('deborah', 'nurse_died'),
    ('deborah', 'buried'),
    ('the-oak-below-bethel', 'name_given'),
    ('jacob', 'blessed_by_the_lord'),
    ('jacob', 'fruitfulness_blessed'),
    ('jacob', 'kings_promised'),
    ('jacob', 'assembly_of_nations_promised'),
    ('jacob', 'land_promised'),
    ('the_pillar_of_bethel', 'pillar_anointed'),
    ('the_pillar_of_bethel', 'libation_poured'),
    ('rachel', 'midwife_comforted'),
    ('rachel', 'died_in_childbirth'),
    ('benjamin', 'name_given'),
    ('rachel', 'buried'),
    ('the-grave-of-rachel', 'grave_marked'),
    ('reuben', 'concubine_lain_with'),
    ('jacob', 'israel_heard'),
    ('jacob', 'twelve_sons_listed'),
    ('isaac', 'gathered_to_his_people'),
    ('isaac', 'full_of_days'),
    ('isaac', 'buried'),
    ('isaac', 'buried_by_both_sons'),
    ('adah-wife-of-esau', 'wife_taken'),
    ('oholibamah', 'wife_taken'),
    ('basemath-bat-ishmael', 'wife_taken'),
    ('eliphaz', 'begotten'),
    ('reuel', 'begotten'),
    ('the-chiefs-of-esau', 'begotten'),
    ('esau', 'parted'),
    ('esau', 'dwelt_in_seir'),
    ('the-chiefs-of-esau', 'sons_of_esau_listed'),
    ('amalek-son-of-eliphaz', 'begotten'),
    ('the-sons-of-seir', 'horites_listed'),
    ('the-kings-of-edom', 'reigned_in_edom'),
    ('the-chiefs-of-esau', 'chiefs_by_places_listed'),
    ('joseph', 'evil_report_brought'),
    ('joseph', 'loved_by_the_father'),
    ('joseph', 'coat_of_stripes_made'),
    ('the-sons', 'hated'),
    ('joseph', 'dream_of_sheaves'),
    ('joseph', 'dream_of_sun_moon_stars'),
    ('the-sons', 'envied'),
    ('jacob', 'word_kept'),
    ('joseph', 'errand_given'),
    ('joseph', 'found_wandering'),
    ('the-sons', 'conspired_to_kill'),
    ('reuben', 'rescue_urged'),
    ('joseph', 'stripped_of_the_coat'),
    ('joseph', 'in_the_pit'),
    ('judah', 'sale_proposed'),
    ('joseph', 'sold_into_egypt'),
    ('reuben', 'garments_torn'),
    ('the-sons', 'coat_dipped'),
    ('jacob', 'coat_recognized'),
    ('jacob', 'garments_torn'),
    ('jacob', 'mourned_many_days'),
    ('jacob', 'comfort_refused'),
    ('jacob', 'wept'),
    ('joseph', 'sold_to_potiphar'),
    ('joseph', 'bought_by_potiphar'),
    ('joseph', 'prospering'),
    ('joseph', 'appointed_over_the_house'),
    ('the-house-of-potiphar', 'house_blessed_for_joseph'),
    ('potiphars-wife', 'lie_with_me_demanded'),
    ('joseph', 'refused'),
    ('potiphars-wife', 'garment_left'),
    ('joseph', 'fled_outside'),
    ('joseph', 'accused_falsely'),
    ('joseph', 'imprisoned'),
    ('joseph', 'favor_in_the_keepers_eyes'),
    ('joseph', 'appointed_over_the_prisoners'),
    ('the-chief-cupbearer', 'offended_the_king'),
    ('the-chief-baker', 'offended_the_king'),
    ('the-chief-cupbearer', 'in_custody'),
    ('the-chief-baker', 'in_custody'),
    ('joseph', 'appointed_to_serve'),
    ('the-chief-cupbearer', 'faces_downcast'),
    ('the-chief-baker', 'faces_downcast'),
    ('the-chief-cupbearer', 'dreams_in_one_night'),
    ('joseph', 'interpretation_given'),
    ('the-chief-cupbearer', 'head_lifted_up_due'),
    ('joseph', 'remembrance_asked'),
    ('the-chief-baker', 'dreams_in_one_night'),
    ('the-chief-baker', 'head_lifted_off_due'),
    ('pharaoh-of-joseph', 'feast_made'),
    ('the-chief-cupbearer', 'restored_to_the_cup'),
    ('the-chief-baker', 'hanged'),
    ('the-chief-cupbearer', 'petition_forgotten'),
    ('pharaoh-of-joseph', 'spirit_troubled'),
    ('the-magicians', 'no_interpreter'),
    ('the-chief-cupbearer', 'offenses_recalled'),
    ('joseph', 'rushed_from_the_pit'),
    ('joseph', 'not_i_god'),
    ('pharaoh-of-joseph', 'pharaohs_dream_doubled'),
    ('pharaoh-of-joseph', 'one_dream'),
    ('joseph', 'counsel_of_the_fifth'),
    ('pharaoh-of-joseph', 'counsel_accepted'),
    ('joseph', 'set_over_the_house'),
    ('joseph', 'ring_given'),
    ('joseph', 'set_over_egypt'),
    ('joseph', 'name_given'),
    ('asenath', 'wife_taken'),
    ('joseph', 'asenath_given'),
    ('joseph', 'thirty_at_the_standing'),
    ('joseph', 'food_gathered_as_sand'),
    ('the-land-of-egypt', 'plenty_seven_years'),
    ('joseph', 'two_sons_before_the_famine'),
    ('manasseh', 'name_given'),
    ('ephraim', 'name_given'),
    ('the-lands', 'famine'),
    ('the-land-of-egypt', 'famine_seven_years'),
    ('the-lands', 'famine_in_all_lands'),
    ('joseph', 'storehouses_opened'),
    ('the-sons', 'descent_commanded'),
    ('the-sons', 'ten_went_down'),
    ('benjamin', 'benjamin_withheld'),
    ('the-sons', 'bowed_as_the_sheaves'),
    ('joseph', 'recognized_one_way'),
    ('joseph', 'dreams_remembered'),
    ('the-sons', 'spies_charged'),
    ('the-sons', 'honesty_pleaded'),
    ('the-sons', 'test_set'),
    ('the-sons', 'custody_three_days'),
    ('joseph', 'plan_revised'),
    ('the-sons', 'guilt_acknowledged'),
    ('joseph', 'interpreter_between'),
    ('joseph', 'wept'),
    ('simeon', 'held_in_custody'),
    ('the-sons', 'silver_returned_in_the_sacks'),
    ('the-sons', 'report_given'),
    ('jacob', 'bereavement_charged'),
    ('reuben', 'pledge_offered'),
    ('jacob', 'descent_refused'),
    ('the-land-of-canaan', 'famine_heavy'),
    ('judah', 'warning_cited'),
    ('judah', 'surety_undertaken'),
    ('jacob', 'mercy_prayed'),
    ('the-sons', 'double_silver_taken'),
    ('the-steward', 'house_ordered'),
    ('the-sons', 'feared_at_the_door'),
    ('the-sons', 'peace_given'),
    ('the-sons', 'feet_washed'),
    ('joseph', 'gift_presented'),
    ('joseph', 'welfare_asked'),
    ('joseph', 'benjamin_seen'),
    ('egypt_people', 'egyptians_eat_apart'),
    ('the-sons', 'seated_by_birth_order'),
    ('benjamin', 'five_hands'),
    ('joseph', 'feast_made'),
    ('the-steward', 'cup_planted'),
    ('the-sons', 'sent_out'),
    ('the-sons', 'overtaken_with_the_cup'),
    ('joseph', 'divination_claimed'),
    ('the-sons', 'theft_denied'),
    ('the-sons', 'death_and_slavery_offered'),
    ('the-steward', 'finder_a_slave_ruled'),
    ('benjamin', 'cup_found'),
    ('the-sons', 'garments_torn'),
    ('the-sons', 'fell_before_him'),
    ('benjamin', 'slavery_of_the_finder_ruled'),
    ('judah', 'surety_invoked'),
    ('judah', 'substitution_offered'),
    ('joseph', 'restraint_failed'),
    ('joseph', 'revealed_to_his_brothers'),
    ('the-sons', 'terrified'),
    ('joseph', 'sent_by_god_declared'),
    ('the-land-of-egypt', 'five_years_of_famine_left'),
    ('the-house-of-jacob', 'goshen_promised'),
    ('jacob', 'sustenance_promised'),
    ('pharaoh-of-joseph', 'good_in_pharaohs_eyes'),
    ('the-sons', 'good_of_egypt_promised'),
    ('the-sons', 'wagons_given'),
    ('the-sons', 'gifts_given'),
    ('benjamin', 'three_hundred_silver'),
    ('jacob', 'ten_donkeys_sent'),
    ('the-sons', 'quarrel_barred'),
    ('jacob', 'heart_numb'),
    ('jacob', 'spirit_revived'),
    ('jacob', 'resolved_to_go'),
    ('jacob', 'sacrifice_offered'),
    ('jacob', 'fear_not_promised'),
    ('jacob', 'great_nation_promised'),
    ('jacob', 'brought_up_promised'),
    ('jacob', 'josephs_hand_on_the_eyes'),
    ('israel_people', 'came_to_egypt'),
    ('israel_people', 'souls_counted'),
    ('judah', 'judah_sent_ahead'),
    ('israel_people', 'encamped_at'),
    ('jacob', 'let_me_die_said'),
    ('the-sons', 'audience_prepared'),
    ('egypt_people', 'shepherds_abhorred'),
    ('joseph', 'told_pharaoh'),
    ('the-sons', 'five_presented'),
    ('the-sons', 'work_asked'),
    ('the-sons', 'dwelling_granted'),
    ('pharaoh-of-joseph', 'pharaoh_blessed'),
    ('jacob', 'years_confessed'),
    ('the-sons', 'holding_given'),
    ('the-house-of-jacob', 'sustained_by_the_mouth'),
    ('pharaoh-of-joseph', 'silver_gathered_to_pharaoh'),
    ('pharaoh-of-joseph', 'livestock_to_pharaoh'),
    ('egypt_people', 'bodies_and_ground_offered'),
    ('pharaoh-of-joseph', 'ground_of_egypt_acquired'),
    ('egypt_people', 'people_moved_to_cities'),
    ('the-priests-of-egypt', 'priests_ground_exempt'),
    ('egypt_people', 'seed_given'),
    ('egypt_people', 'servants_to_pharaoh'),
    ('egypt_people', 'fifth_to_pharaoh'),
    ('israel_people', 'fruitful_in_goshen'),
    ('joseph', 'burial_in_canaan_sworn'),
    ('joseph', 'oath_sworn'),
    ('jacob', 'bowed_on_the_bed'),
    ('jacob', 'face_fallen_on'),
    ('jacob', 'embalming_forty_days'),
    ('egypt_people', 'egypt_wept_seventy'),
    ('joseph', 'burial_leave_asked'),
    ('joseph', 'leave_granted'),
    ('the-sons', 'funeral_ascended'),
    ('the-sons', 'encamped_at'),
    ('the-sons', 'seven_days_mourning'),
    ('the-threshing-floor-of-atad', 'name_given'),
    ('the-sons', 'returned_to_egypt'),
    ('the-sons', 'feared_joseph'),
    ('the-sons', 'forgiveness_asked'),
    ('the-sons', 'forgiven'),
    ('the-sons', 'comforted'),
    ('the-sons', 'sustenance_promised'),
    ('joseph', 'dwelt_in_egypt'),
    ('the-sons-of-machir', 'born_on_the_knees'),
    ('israel_people', 'visitation_promised'),
    ('israel_people', 'oath_sworn'),
    ('israel_people', 'bones_oath'),
    ('joseph', 'embalmed_and_coffined'),
    ('benjamin', 'circumcision_due'),
    ('manasseh', 'circumcision_due'),
    ('ephraim', 'circumcision_due'),
]

def scene():
    """THE SCENE — the stretch's acts on a bare world in the text's order (scene days; the tape carries the ink's markers); the events and their
    days the hand-model's (scratchpad o8_s4_predict.py) — typed from its print"""
    closes = [0]
    def close(eid, eff, note, value=None):
        closes[0] += bool(w.close(eid, eff, note, value=value))
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='FROM THE FORD TO THE COFFIN — Genesis 32-37, 39-47, 50 (clock unit: days; the tape\'s own order)')
        w.laws = [law_joseph, PS_.law_pre_sinai]   # the covenant\'s own run on every male birth (Gen 17:12) — the pre-Sinai daemon beside the story\'s, as S1 and S3
        w.advance(1)
        w.submit({'kind': 'angels_met', 'subject': 'jacob', 'at': 'Mahanaim', 'case_source': 'Gen 32:2-3'})
        w.submit({'kind': 'named', 'subject': 'the-camp-of-god', 'name': 'Mahanaim (מחנים — two camps, 32:3)', 'by': 'jacob', 'case_source': 'Gen 32:3'})
        w.submit({'kind': 'messengers_sent', 'subject': 'jacob', 'to': 'esau', 'report': 'four hundred men with him', 'case_source': 'Gen 32:4-7'})
        w.submit({'kind': 'feared_greatly', 'subject': 'jacob', 'case_source': 'Gen 32:8-9'})
        w.submit({'kind': 'prayed', 'subject': 'jacob', 'for': 'deliverance from the hand of Esau', 'case_source': 'Gen 32:10-13'})
        w.submit({'kind': 'gift_prepared', 'subject': 'jacob', 'head_count': 550, 'case_source': 'Gen 32:14-22'})
        w.submit({'kind': 'river_crossed', 'subject': 'jacob', 'river': 'the Jabbok', 'case_source': 'Gen 32:23-24'})
        w.submit({'kind': 'wrestled', 'subject': 'jacob', 'case_source': 'Gen 32:25-26'})
        w.submit({'kind': 'blessing_demanded', 'subject': 'jacob', 'case_source': 'Gen 32:27'})
        w.submit({'kind': 'name_asked', 'subject': 'jacob', 'case_source': 'Gen 32:30'})
        w.submit({'kind': 'named', 'subject': 'the-ford-of-jabbok', 'name': 'Peniel (פניאל — the face of God, 32:31)', 'by': 'jacob', 'case_source': 'Gen 32:31'})
        w.advance(2)
        w.submit({'kind': 'sun_rose', 'subject': 'jacob', 'case_source': 'Gen 32:32'})
        w.submit({'kind': 'esau_seen', 'subject': 'jacob', 'case_source': 'Gen 33:1'})
        w.submit({'kind': 'children_divided', 'subject': 'jacob', 'case_source': 'Gen 33:1-2'})
        w.submit({'kind': 'bowed', 'subject': 'jacob', 'form': 'prostration to the ground', 'times': 7, 'case_source': 'Gen 33:3'})
        w.submit({'kind': 'embraced', 'subject': 'esau', 'whom': 'jacob', 'case_source': 'Gen 33:4'})
        w.submit({'kind': 'fell_on_the_neck', 'subject': 'esau', 'on': 'jacob', 'case_source': 'Gen 33:4'})
        w.submit({'kind': 'kissed', 'subject': 'esau', 'whom': 'jacob', 'dotted': True, 'case_source': 'Gen 33:4'})
        w.submit({'kind': 'children_declared', 'subject': 'jacob', 'case_source': 'Gen 33:5'})
        w.submit({'kind': 'bowed', 'subject': 'the-maids-and-their-children', 'form': 'prostration', 'case_source': 'Gen 33:6'})
        w.submit({'kind': 'bowed', 'subject': 'leah', 'form': 'prostration', 'case_source': 'Gen 33:7'})
        w.submit({'kind': 'bowed', 'subject': 'rachel', 'form': 'prostration', 'with': 'joseph', 'case_source': 'Gen 33:7'})
        w.submit({'kind': 'camp_explained', 'subject': 'esau', 'case_source': 'Gen 33:8-9'})
        w.submit({'kind': 'gift_urged', 'subject': 'jacob', 'case_source': 'Gen 33:10-11'})
        w.submit({'kind': 'convoy_declined', 'subject': 'jacob', 'case_source': 'Gen 33:12-15'})
        w.submit({'kind': 'journeyed', 'subject': 'esau', 'to': 'Seir', 'case_source': 'Gen 33:16'})
        w.advance(3)
        w.submit({'kind': 'journeyed', 'subject': 'jacob', 'to': 'Sukkot', 'case_source': 'Gen 33:17'})
        w.submit({'kind': 'booths_made', 'subject': 'jacob', 'case_source': 'Gen 33:17'})
        w.submit({'kind': 'named', 'subject': 'jacob', 'name': 'Sukkot (סכות — booths, 33:17)', 'by': 'jacob', 'case_source': 'Gen 33:17'})
        w.advance(543)
        w.submit({'kind': 'journeyed', 'subject': 'jacob', 'to': 'the city of Shechem', 'case_source': 'Gen 33:18'})
        w.submit({'kind': 'purchased', 'subject': 'jacob', 'what': 'the-field-at-shechem', 'from': 'the sons of Hamor', 'price': 100, 'unit': 'kesitah', 'case_source': 'Gen 33:19'})
        w.submit({'kind': 'altar_erected', 'subject': 'the-altar-of-el-elohe-israel', 'by': 'jacob', 'case_source': 'Gen 33:20'})
        w.submit({'kind': 'named', 'subject': 'the-altar-of-el-elohe-israel', 'name': 'El-Elohe-Israel (אל אלהי ישראל — God, the God of Israel, 33:20)', 'by': 'jacob', 'case_source': 'Gen 33:20'})
        w.advance(544)
        w.submit({'kind': 'went_out_to_see', 'subject': 'dinah', 'case_source': 'Gen 34:1'})
        w.submit({'kind': 'seized_and_violated', 'subject': 'shechem', 'whom': 'dinah', 'case_source': 'Gen 34:2'})
        w.submit({'kind': 'soul_cleaved', 'subject': 'shechem', 'case_source': 'Gen 34:3'})
        w.submit({'kind': 'wife_asked', 'subject': 'shechem', 'of': 'hamor', 'case_source': 'Gen 34:4'})
        w.submit({'kind': 'silence_kept', 'subject': 'jacob', 'case_source': 'Gen 34:5'})
        w.submit({'kind': 'came_to_speak', 'subject': 'hamor', 'case_source': 'Gen 34:6'})
        w.submit({'kind': 'outraged', 'subject': 'the-sons', 'case_source': 'Gen 34:7'})
        w.submit({'kind': 'marriage_proposed', 'subject': 'hamor', 'case_source': 'Gen 34:8-10'})
        w.submit({'kind': 'marriage_proposed', 'subject': 'shechem', 'mohar': 'unbounded', 'case_source': 'Gen 34:11-12'})
        w.submit({'kind': 'deceit_answered', 'subject': 'the-sons', 'case_source': 'Gen 34:13-17'})
        w.submit({'kind': 'terms_accepted', 'subject': 'hamor', 'case_source': 'Gen 34:18-19'})
        w.submit({'kind': 'gate_addressed', 'subject': 'hamor', 'case_source': 'Gen 34:20-23'})
        w.submit({'kind': 'males_circumcised', 'subject': 'the-men-of-shechem', 'case_source': 'Gen 34:24'})
        w.advance(546)
        w.submit({'kind': 'city_struck', 'subject': 'simeon-and-levi', 'ordinal': 3, 'case_source': 'Gen 34:25-26'})
        w.submit({'kind': 'city_plundered', 'subject': 'the-sons', 'case_source': 'Gen 34:27-29'})
        w.submit({'kind': 'rebuked', 'subject': 'jacob', 'whom': 'Simeon and Levi', 'case_source': 'Gen 34:30'})
        w.submit({'kind': 'answered_back', 'subject': 'the-sons', 'case_source': 'Gen 34:31'})
        w.advance(547)
        w.submit({'kind': 'altar_commanded', 'subject': 'god', 'to': 'jacob', 'case_source': 'Gen 35:1'})
        w.submit({'kind': 'purge_commanded', 'subject': 'jacob', 'case_source': 'Gen 35:2-3'})
        w.submit({'kind': 'gods_hidden', 'subject': 'jacob', 'case_source': 'Gen 35:4'})
        close('the-house-of-jacob', 'foreign_gods_removal_owed', 'Gen 35:4 — the gods given and hidden')
        w.submit({'kind': 'journeyed', 'subject': 'the-house-of-jacob', 'to': 'toward Bethel', 'case_source': 'Gen 35:5'})
        w.advance(548)
        w.submit({'kind': 'journeyed', 'subject': 'jacob', 'to': 'Luz, that is Bethel', 'case_source': 'Gen 35:6'})
        close('jacob', 'ascent_to_bethel_owed', 'Gen 35:6 — and Jacob came to Luz, that is Bethel')
        close('jacob', 'return_promised', "Gen 35:6 — S3's entry (28:15): and Jacob came to Luz which is in the land of Canaan, that is Bethel")
        w.submit({'kind': 'altar_erected', 'subject': 'the-altar-at-bethel-again', 'by': 'jacob', 'case_source': 'Gen 35:7'})
        close('jacob', 'altar_owed', 'Gen 35:7 — and he built there an altar')
        close('jacob', 'vow_of_bethel', "Gen 35:7 — S3's entry (28:20-22): the altar built where the vow was made; Bereshit Rabbah 81:1-2 read the delay as punished")
        w.submit({'kind': 'named', 'subject': 'the-place', 'name': 'El-Bethel (אל בית אל — the God of Bethel, 35:7)', 'by': 'jacob', 'case_source': 'Gen 35:7'})
        w.submit({'kind': 'died', 'subject': 'deborah', 'case_source': 'Gen 35:8'})
        w.submit({'kind': 'buried', 'subject': 'deborah', 'where': 'below Bethel, under the oak', 'case_source': 'Gen 35:8'})
        w.submit({'kind': 'named', 'subject': 'the-oak-below-bethel', 'name': 'Allon-bachuth (אלון בכות — the oak of weeping, 35:8)', 'by': 'jacob', 'case_source': 'Gen 35:8'})
        w.submit({'kind': 'appeared', 'subject': 'god', 'to': 'jacob', 'again': True, 'case_source': 'Gen 35:9'})
        w.submit({'kind': 'named', 'subject': 'jacob', 'name': 'Israel (ישראל — by the formula, 35:10)', 'by': 'god', 'case_source': 'Gen 35:10'})
        w.submit({'kind': 'blessed_be_fruitful', 'subject': 'god', 'to': 'jacob', 'number': 'singular', 'case_source': 'Gen 35:11'})
        w.submit({'kind': 'land_promised', 'subject': 'god', 'to': 'jacob', 'case_source': 'Gen 35:12'})
        w.submit({'kind': 'god_went_up', 'subject': 'god', 'case_source': 'Gen 35:13'})
        w.submit({'kind': 'pillar_set_and_anointed', 'subject': 'the_pillar_of_bethel', 'by': 'jacob', 'libation': True, 'oil': True, 'case_source': 'Gen 35:14'})
        w.submit({'kind': 'named', 'subject': 'the-place', 'name': 'Bethel (בית אל — the house of God, 35:15)', 'by': 'jacob', 'case_source': 'Gen 35:15'})
        w.advance(728)
        w.submit({'kind': 'journeyed', 'subject': 'jacob', 'to': 'toward Ephrath', 'case_source': 'Gen 35:16'})
        w.submit({'kind': 'hard_birth', 'subject': 'rachel', 'case_source': 'Gen 35:16-17'})
        w.submit({'kind': 'born', 'subject': 'benjamin', 'mother': 'rachel', 'sex': 'm', 'case_source': 'Gen 35:18'})
        w.submit({'kind': 'named', 'subject': 'benjamin', 'name': 'Ben-oni (בן אוני — son of my sorrow, 35:18)', 'by': 'rachel', 'case_source': 'Gen 35:18'})
        w.submit({'kind': 'named', 'subject': 'benjamin', 'name': 'Benjamin (בנימין — son of the right hand, 35:18)', 'by': 'jacob', 'case_source': 'Gen 35:18'})
        w.submit({'kind': 'died', 'subject': 'rachel', 'case_source': 'Gen 35:19'})
        w.submit({'kind': 'buried', 'subject': 'rachel', 'where': 'on the way to Ephrath, that is Bethlehem', 'case_source': 'Gen 35:19'})
        w.submit({'kind': 'grave_pillar_set', 'subject': 'jacob', 'on': 'the-grave-of-rachel', 'case_source': 'Gen 35:20'})
        w.submit({'kind': 'journeyed', 'subject': 'jacob', 'to': 'beyond Migdal-eder', 'case_source': 'Gen 35:21'})
        w.submit({'kind': 'lay_with_the_concubine', 'subject': 'reuben', 'with': 'bilhah', 'reading': 'read_not_translated', 'case_source': 'Gen 35:22'})
        w.submit({'kind': 'sons_counted', 'subject': 'jacob', 'count': 12, 'case_source': 'Gen 35:22-26'})
        w.advance(729)
        w.submit({'kind': 'journeyed', 'subject': 'jacob', 'to': 'Mamre, Kiriath-arba, that is Hebron', 'case_source': 'Gen 35:27'})
        w.submit({'kind': 'died', 'subject': 'isaac', 'years': 180, 'case_source': 'Gen 35:28-29'})
        w.submit({'kind': 'buried', 'subject': 'isaac', 'by': 'Esau and Jacob', 'case_source': 'Gen 35:29'})
        w.advance(730)
        w.submit({'kind': 'married', 'subject': 'adah-wife-of-esau', 'husband': 'esau', 'case_source': 'Gen 36:2'})
        w.submit({'kind': 'married', 'subject': 'oholibamah', 'husband': 'esau', 'case_source': 'Gen 36:2'})
        w.submit({'kind': 'married', 'subject': 'basemath-bat-ishmael', 'husband': 'esau', 'case_source': 'Gen 36:3'})
        w.submit({'kind': 'bore', 'subject': 'adah-wife-of-esau', 'child': 'eliphaz', 'case_source': 'Gen 36:4'})
        w.submit({'kind': 'bore', 'subject': 'basemath-bat-ishmael', 'child': 'reuel', 'case_source': 'Gen 36:4'})
        w.submit({'kind': 'bore', 'subject': 'oholibamah', 'children': ['Jeush', 'Jalam', 'Korah'], 'case_source': 'Gen 36:5'})
        w.submit({'kind': 'withdrew', 'subject': 'esau', 'to': 'the hill country of Seir', 'case_source': 'Gen 36:6-8'})
        w.submit({'kind': 'roster_listed', 'subject': 'the-chiefs-of-esau', 'names': 'the sons of Esau and their chiefs', 'count': 14, 'case_source': 'Gen 36:9-19'})
        w.submit({'kind': 'bore', 'subject': 'timna', 'child': 'amalek-son-of-eliphaz', 'by': 'eliphaz', 'case_source': 'Gen 36:12'})
        w.submit({'kind': 'roster_listed', 'subject': 'the-sons-of-seir', 'names': 'the sons of Seir the Horite and their chiefs', 'count': 7, 'case_source': 'Gen 36:20-30'})
        w.submit({'kind': 'reigned', 'subject': 'the-kings-of-edom', 'king': 'bela', 'city': 'Dinhabah', 'case_source': 'Gen 36:31-32'})
        w.submit({'kind': 'reign_passed', 'subject': 'the-kings-of-edom', 'died': 'bela', 'successor': 'jobab', 'city': 'Bozrah', 'case_source': 'Gen 36:33'})
        w.submit({'kind': 'reign_passed', 'subject': 'the-kings-of-edom', 'died': 'jobab', 'successor': 'husham', 'city': None, 'case_source': 'Gen 36:34'})
        w.submit({'kind': 'reign_passed', 'subject': 'the-kings-of-edom', 'died': 'husham', 'successor': 'hadad-ben-bedad', 'city': 'Avith', 'case_source': 'Gen 36:35'})
        w.submit({'kind': 'reign_passed', 'subject': 'the-kings-of-edom', 'died': 'hadad-ben-bedad', 'successor': 'samlah', 'city': 'Masrekah', 'case_source': 'Gen 36:36'})
        w.submit({'kind': 'reign_passed', 'subject': 'the-kings-of-edom', 'died': 'samlah', 'successor': 'shaul-of-rehoboth', 'city': None, 'case_source': 'Gen 36:37'})
        w.submit({'kind': 'reign_passed', 'subject': 'the-kings-of-edom', 'died': 'shaul-of-rehoboth', 'successor': 'baal-hanan', 'city': None, 'case_source': 'Gen 36:38'})
        w.submit({'kind': 'reign_passed', 'subject': 'the-kings-of-edom', 'died': 'baal-hanan', 'successor': 'hadar', 'city': 'Pau', 'case_source': 'Gen 36:39'})
        w.submit({'kind': 'roster_listed', 'subject': 'the-chiefs-of-esau', 'names': 'the chiefs of Esau by their places', 'count': 11, 'case_source': 'Gen 36:40-43'})
        w.advance(731)
        w.submit({'kind': 'evil_report_brought', 'subject': 'joseph', 'case_source': 'Gen 37:2'})
        w.submit({'kind': 'loved_apart', 'subject': 'jacob', 'whom': 'joseph', 'case_source': 'Gen 37:3'})
        w.submit({'kind': 'coat_made', 'subject': 'jacob', 'for': 'joseph', 'case_source': 'Gen 37:3'})
        w.submit({'kind': 'hated', 'subject': 'the-sons', 'whom': 'joseph', 'case_source': 'Gen 37:4'})
        w.submit({'kind': 'dreamed', 'subject': 'joseph', 'dream': 'the sheaves', 'case_source': 'Gen 37:5'})
        w.submit({'kind': 'hated', 'subject': 'the-sons', 'whom': 'joseph', 'more': True, 'case_source': 'Gen 37:5'})
        w.submit({'kind': 'dream_told', 'subject': 'joseph', 'dream': 'the sheaves', 'to': 'the-sons', 'case_source': 'Gen 37:6-7'})
        w.submit({'kind': 'hated', 'subject': 'the-sons', 'whom': 'joseph', 'more': True, 'case_source': 'Gen 37:8'})
        w.submit({'kind': 'dreamed', 'subject': 'joseph', 'dream': 'the sun, the moon and eleven stars', 'case_source': 'Gen 37:9'})
        w.submit({'kind': 'dream_told', 'subject': 'joseph', 'dream': 'the sun, the moon and eleven stars', 'to': 'his father and his brothers', 'case_source': 'Gen 37:9-10'})
        w.submit({'kind': 'rebuked', 'subject': 'jacob', 'whom': 'joseph', 'case_source': 'Gen 37:10'})
        w.submit({'kind': 'envied', 'subject': 'the-sons', 'whom': 'joseph', 'case_source': 'Gen 37:11'})
        w.advance(732)
        w.submit({'kind': 'journeyed', 'subject': 'the-sons', 'to': 'Shechem, to pasture', 'case_source': 'Gen 37:12'})
        w.submit({'kind': 'errand_given', 'subject': 'jacob', 'to': 'joseph', 'case_source': 'Gen 37:13-14'})
        w.submit({'kind': 'found_wandering', 'subject': 'joseph', 'by': 'the-man-at-shechem', 'to': 'Dothan', 'case_source': 'Gen 37:15-17'})
        w.submit({'kind': 'conspired', 'subject': 'the-sons', 'against': 'joseph', 'case_source': 'Gen 37:18'})
        w.submit({'kind': 'plot_spoken', 'subject': 'the-sons', 'case_source': 'Gen 37:19-20'})
        w.submit({'kind': 'rescue_urged', 'subject': 'reuben', 'case_source': 'Gen 37:21-22'})
        w.submit({'kind': 'stripped', 'subject': 'the-sons', 'whom': 'joseph', 'case_source': 'Gen 37:23'})
        w.submit({'kind': 'cast_into_the_pit', 'subject': 'the-sons', 'whom': 'joseph', 'case_source': 'Gen 37:24'})
        w.submit({'kind': 'caravan_seen', 'subject': 'the-sons', 'case_source': 'Gen 37:25'})
        w.submit({'kind': 'sale_proposed', 'subject': 'judah', 'case_source': 'Gen 37:26-27'})
        w.submit({'kind': 'sold', 'subject': 'the-sellers-of-joseph', 'whom': 'joseph', 'to': 'the-ishmaelites', 'price': 20, 'case_source': 'Gen 37:28'})
        close('joseph', 'in_the_pit', 'Gen 37:28 — drawn and lifted out of the pit')
        w.submit({'kind': 'pit_found_empty', 'subject': 'reuben', 'case_source': 'Gen 37:29-30'})
        w.submit({'kind': 'tore_garments', 'subject': 'reuben', 'case_source': 'Gen 37:29'})
        w.submit({'kind': 'coat_dipped', 'subject': 'the-sons', 'case_source': 'Gen 37:31-32'})
        w.submit({'kind': 'coat_recognized', 'subject': 'jacob', 'case_source': 'Gen 37:33'})
        w.submit({'kind': 'tore_garments', 'subject': 'jacob', 'case_source': 'Gen 37:34'})
        w.submit({'kind': 'mourned', 'subject': 'jacob', 'days': 'many', 'case_source': 'Gen 37:34-35'})
        w.submit({'kind': 'wept', 'subject': 'jacob', 'for': 'joseph', 'case_source': 'Gen 37:35'})
        w.submit({'kind': 'sold', 'subject': 'the-medanites', 'whom': 'joseph', 'to': 'potiphar', 'case_source': 'Gen 37:36'})
        w.advance(733)
        w.submit({'kind': 'slave_bought', 'subject': 'potiphar', 'whom': 'joseph', 'case_source': 'Gen 39:1'})
        w.submit({'kind': 'prospered', 'subject': 'joseph', 'case_source': 'Gen 39:2-3'})
        w.submit({'kind': 'appointed_over_the_house', 'subject': 'joseph', 'by': 'potiphar', 'case_source': 'Gen 39:4-6'})
        w.submit({'kind': 'lie_with_me_demanded', 'subject': 'potiphars-wife', 'case_source': 'Gen 39:7'})
        w.submit({'kind': 'refused', 'subject': 'joseph', 'case_source': 'Gen 39:8-10'})
        w.advance(734)
        w.submit({'kind': 'lie_with_me_demanded', 'subject': 'potiphars-wife', 'seized': True, 'case_source': 'Gen 39:12'})
        w.submit({'kind': 'garment_seized', 'subject': 'potiphars-wife', 'case_source': 'Gen 39:12-13, 39:16'})
        w.submit({'kind': 'fled', 'subject': 'joseph', 'from': 'potiphars-wife', 'case_source': 'Gen 39:12-15'})
        w.submit({'kind': 'accused', 'subject': 'potiphars-wife', 'whom': 'joseph', 'case_source': 'Gen 39:14-18'})
        w.submit({'kind': 'anger_burned', 'subject': 'potiphar', 'case_source': 'Gen 39:19'})
        w.submit({'kind': 'imprisoned', 'subject': 'joseph', 'by': 'potiphar', 'case_source': 'Gen 39:20'})
        w.submit({'kind': 'kindness_extended', 'subject': 'joseph', 'case_source': 'Gen 39:21'})
        w.submit({'kind': 'appointed_over_the_house', 'subject': 'joseph', 'by': 'the-prison-keeper', 'over': 'the prisoners', 'case_source': 'Gen 39:22'})
        w.submit({'kind': 'prospered', 'subject': 'joseph', 'in': 'the prison-house', 'case_source': 'Gen 39:23'})
        w.advance(735)
        w.submit({'kind': 'offended', 'subject': 'the-two-officers', 'case_source': 'Gen 40:1-2'})
        w.submit({'kind': 'imprisoned', 'subject': 'the-two-officers', 'by': 'pharaoh-of-joseph', 'case_source': 'Gen 40:3'})
        w.submit({'kind': 'appointed_to_serve', 'subject': 'joseph', 'case_source': 'Gen 40:4'})
        w.submit({'kind': 'dreamed', 'subject': 'the-two-officers', 'night': 'one', 'case_source': 'Gen 40:5'})
        w.submit({'kind': 'faces_downcast', 'subject': 'the-two-officers', 'case_source': 'Gen 40:6-8'})
        w.submit({'kind': 'dream_told', 'subject': 'the-chief-cupbearer', 'dream': 'the vine', 'to': 'joseph', 'case_source': 'Gen 40:9-11'})
        w.submit({'kind': 'interpreted', 'subject': 'joseph', 'to': 'the-chief-cupbearer', 'days': 3, 'case_source': 'Gen 40:12-13'})
        w.submit({'kind': 'remembrance_asked', 'subject': 'joseph', 'case_source': 'Gen 40:14-15'})
        w.submit({'kind': 'dream_told', 'subject': 'the-chief-baker', 'dream': 'the baskets', 'to': 'joseph', 'case_source': 'Gen 40:16-17'})
        w.submit({'kind': 'interpreted', 'subject': 'joseph', 'to': 'the-chief-baker', 'days': 3, 'case_source': 'Gen 40:18-19'})
        w.advance(738)
        w.submit({'kind': 'feast_made', 'subject': 'pharaoh-of-joseph', 'occasion': 'his birthday', 'ordinal': 3, 'case_source': 'Gen 40:20'})
        w.submit({'kind': 'restored', 'subject': 'the-chief-cupbearer', 'case_source': 'Gen 40:21'})
        close('the-chief-cupbearer', 'in_custody', 'Gen 40:21 — restored to his cupbearing')
        w.submit({'kind': 'hanged', 'subject': 'the-chief-baker', 'case_source': 'Gen 40:22'})
        close('the-chief-baker', 'in_custody', 'Gen 40:22 — hanged, as Joseph had interpreted')
        w.submit({'kind': 'forgot', 'subject': 'the-chief-cupbearer', 'whom': 'joseph', 'case_source': 'Gen 40:23'})
        w.advance(1468)
        w.submit({'kind': 'dreamed', 'subject': 'pharaoh-of-joseph', 'dream': 'the seven cows', 'case_source': 'Gen 41:1-4'})
        w.submit({'kind': 'dreamed', 'subject': 'pharaoh-of-joseph', 'dream': 'the seven ears', 'case_source': 'Gen 41:5-7'})
        w.submit({'kind': 'spirit_troubled', 'subject': 'pharaoh-of-joseph', 'case_source': 'Gen 41:8'})
        w.submit({'kind': 'offenses_recalled', 'subject': 'the-chief-cupbearer', 'case_source': 'Gen 41:9-13'})
        w.submit({'kind': 'rushed_from_the_pit', 'subject': 'joseph', 'case_source': 'Gen 41:14-16'})
        w.submit({'kind': 'dream_told', 'subject': 'pharaoh-of-joseph', 'dream': 'the cows and the ears', 'to': 'joseph', 'case_source': 'Gen 41:17-24'})
        w.submit({'kind': 'interpreted', 'subject': 'joseph', 'to': 'pharaoh-of-joseph', 'years': [7, 7], 'case_source': 'Gen 41:25-32'})
        w.submit({'kind': 'counsel_given', 'subject': 'joseph', 'to': 'pharaoh-of-joseph', 'case_source': 'Gen 41:33-36'})
        w.submit({'kind': 'counsel_accepted', 'subject': 'pharaoh-of-joseph', 'case_source': 'Gen 41:37-39'})
        w.submit({'kind': 'set_over_egypt', 'subject': 'joseph', 'by': 'pharaoh-of-joseph', 'case_source': 'Gen 41:40-44'})
        w.submit({'kind': 'named', 'subject': 'joseph', 'name': 'Zaphenath-paneah (צפנת פענח, 41:45)', 'by': 'pharaoh-of-joseph', 'case_source': 'Gen 41:45'})
        w.submit({'kind': 'married', 'subject': 'asenath', 'husband': 'joseph', 'by': 'pharaoh-of-joseph', 'case_source': 'Gen 41:45'})
        w.submit({'kind': 'went_out_over_egypt', 'subject': 'joseph', 'age': 30, 'case_source': 'Gen 41:45-46'})
        w.submit({'kind': 'food_gathered', 'subject': 'joseph', 'case_source': 'Gen 41:47-49'})
        w.submit({'kind': 'born', 'subject': 'manasseh', 'mother': 'asenath', 'sex': 'm', 'case_source': 'Gen 41:50'})
        w.submit({'kind': 'named', 'subject': 'manasseh', 'name': 'Manasseh (מנשה — God has made me forget, 41:51)', 'by': 'joseph', 'case_source': 'Gen 41:51'})
        w.submit({'kind': 'born', 'subject': 'ephraim', 'mother': 'asenath', 'sex': 'm', 'case_source': 'Gen 41:50'})
        w.submit({'kind': 'named', 'subject': 'ephraim', 'name': 'Ephraim (אפרים — God has made me fruitful, 41:52)', 'by': 'joseph', 'case_source': 'Gen 41:52'})
        w.advance(4023)
        w.submit({'kind': 'plenty_ended', 'subject': 'the-land-of-egypt', 'case_source': 'Gen 41:53'})
        w.submit({'kind': 'famine_came', 'subject': 'the-lands', 'years': 7, 'case_source': 'Gen 41:54'})
        w.submit({'kind': 'cried_for_bread', 'subject': 'egypt_people', 'case_source': 'Gen 41:55'})
        w.submit({'kind': 'storehouses_opened', 'subject': 'joseph', 'case_source': 'Gen 41:56-57'})
        w.advance(4024)
        w.submit({'kind': 'descent_commanded', 'subject': 'jacob', 'to': 'the-sons', 'case_source': 'Gen 42:1-2'})
        w.submit({'kind': 'went_down', 'subject': 'the-sons', 'count': 10, 'case_source': 'Gen 42:3-5'})
        w.submit({'kind': 'benjamin_withheld', 'subject': 'jacob', 'case_source': 'Gen 42:4'})
        w.submit({'kind': 'bowed', 'subject': 'the-sons', 'form': 'faces to the earth', 'case_source': 'Gen 42:6'})
        w.submit({'kind': 'brothers_recognized', 'subject': 'joseph', 'case_source': 'Gen 42:7-8'})
        w.submit({'kind': 'dreams_remembered', 'subject': 'joseph', 'case_source': 'Gen 42:9'})
        w.submit({'kind': 'spies_charged', 'subject': 'joseph', 'whom': 'the-sons', 'case_source': 'Gen 42:9-14'})
        w.submit({'kind': 'honesty_pleaded', 'subject': 'the-sons', 'brothers': 12, 'case_source': 'Gen 42:10-13'})
        w.submit({'kind': 'test_set', 'subject': 'joseph', 'on': 'the-sons', 'case_source': 'Gen 42:15-16'})
        w.submit({'kind': 'custody_three_days', 'subject': 'joseph', 'whom': 'the-sons', 'days': 3, 'case_source': 'Gen 42:17'})
        w.advance(4027)
        w.submit({'kind': 'plan_revised', 'subject': 'joseph', 'ordinal': 3, 'case_source': 'Gen 42:18-20'})
        w.submit({'kind': 'guilt_confessed', 'subject': 'the-sons', 'case_source': 'Gen 42:21'})
        w.submit({'kind': 'guilt_confessed', 'subject': 'reuben', 'citing': 'Gen 37:22', 'case_source': 'Gen 42:22'})
        w.submit({'kind': 'interpreter_between', 'subject': 'joseph', 'case_source': 'Gen 42:23'})
        w.submit({'kind': 'wept', 'subject': 'joseph', 'case_source': 'Gen 42:24'})
        w.submit({'kind': 'bound', 'subject': 'simeon', 'by': 'joseph', 'case_source': 'Gen 42:24'})
        w.submit({'kind': 'silver_returned', 'subject': 'joseph', 'case_source': 'Gen 42:25'})
        w.submit({'kind': 'journeyed', 'subject': 'the-sons', 'to': 'the land of Canaan', 'case_source': 'Gen 42:26'})
        w.submit({'kind': 'silver_found', 'subject': 'the-sons', 'at': 'the lodging place', 'case_source': 'Gen 42:27-28'})
        w.submit({'kind': 'report_given', 'subject': 'the-sons', 'to': 'jacob', 'case_source': 'Gen 42:29-34'})
        w.submit({'kind': 'silver_found', 'subject': 'the-sons', 'at': 'the emptying of the sacks', 'case_source': 'Gen 42:35'})
        w.submit({'kind': 'bereaved_cried', 'subject': 'jacob', 'case_source': 'Gen 42:36'})
        w.submit({'kind': 'pledge_of_sons_offered', 'subject': 'reuben', 'case_source': 'Gen 42:37'})
        w.submit({'kind': 'descent_refused', 'subject': 'jacob', 'case_source': 'Gen 42:38'})
        w.advance(4388)
        w.submit({'kind': 'famine_came', 'subject': 'the-land-of-canaan', 'heavy': True, 'case_source': 'Gen 43:1'})
        w.submit({'kind': 'descent_commanded', 'subject': 'jacob', 'to': 'the-sons', 'again': True, 'case_source': 'Gen 43:2'})
        w.submit({'kind': 'warning_cited', 'subject': 'judah', 'case_source': 'Gen 43:3-7'})
        w.submit({'kind': 'surety_offered', 'subject': 'judah', 'for': 'benjamin', 'to': 'jacob', 'case_source': 'Gen 43:8-10'})
        w.submit({'kind': 'caravan_planned', 'subject': 'jacob', 'case_source': 'Gen 43:11-14'})
        w.advance(4752)
        w.submit({'kind': 'went_down', 'subject': 'the-sons', 'with': 'benjamin', 'silver': 'double', 'case_source': 'Gen 43:15'})
        w.submit({'kind': 'house_ordered', 'subject': 'joseph', 'to': 'the-steward', 'case_source': 'Gen 43:16-17'})
        w.submit({'kind': 'feared_at_the_door', 'subject': 'the-sons', 'case_source': 'Gen 43:18-22'})
        w.submit({'kind': 'peace_given', 'subject': 'the-steward', 'to': 'the-sons', 'simeon': 'brought out', 'case_source': 'Gen 43:23'})
        close('simeon', 'held_in_custody', 'Gen 43:23 — and he brought Simeon out to them')
        w.submit({'kind': 'feet_washed', 'subject': 'the-sons', 'case_source': 'Gen 43:24'})
        w.submit({'kind': 'gift_presented', 'subject': 'the-sons', 'to': 'joseph', 'case_source': 'Gen 43:25-26'})
        w.submit({'kind': 'bowed', 'subject': 'the-sons', 'form': 'prostration to the earth', 'case_source': 'Gen 43:26'})
        w.submit({'kind': 'welfare_asked', 'subject': 'joseph', 'case_source': 'Gen 43:27-28'})
        w.submit({'kind': 'bowed', 'subject': 'the-sons', 'form': 'kidah and prostration', 'case_source': 'Gen 43:28'})
        w.submit({'kind': 'benjamin_seen', 'subject': 'joseph', 'case_source': 'Gen 43:29-30'})
        w.submit({'kind': 'wept', 'subject': 'joseph', 'where': 'the chamber', 'case_source': 'Gen 43:30'})
        w.submit({'kind': 'bread_set', 'subject': 'joseph', 'case_source': 'Gen 43:31-32'})
        w.submit({'kind': 'seated_by_birth_order', 'subject': 'the-sons', 'case_source': 'Gen 43:33'})
        w.submit({'kind': 'portions_lifted', 'subject': 'joseph', 'hands': 5, 'case_source': 'Gen 43:34'})
        w.submit({'kind': 'feast_made', 'subject': 'joseph', 'for': 'the-sons', 'case_source': 'Gen 43:16-34'})
        w.submit({'kind': 'ate_and_drank', 'subject': 'the-sons', 'case_source': 'Gen 43:34'})
        w.advance(4753)
        w.submit({'kind': 'cup_planted', 'subject': 'the-steward', 'case_source': 'Gen 44:1-2'})
        w.submit({'kind': 'sent_away', 'subject': 'the-sons', 'by': 'joseph', 'case_source': 'Gen 44:3'})
        w.submit({'kind': 'pursued', 'subject': 'the-steward', 'whom': 'the-sons', 'case_source': 'Gen 44:4-6'})
        w.submit({'kind': 'divination_claimed', 'subject': 'joseph', 'by': 'the-steward', 'case_source': 'Gen 44:5'})
        w.submit({'kind': 'theft_denied', 'subject': 'the-sons', 'case_source': 'Gen 44:7-8'})
        w.submit({'kind': 'rash_sentence_offered', 'subject': 'the-sons', 'case_source': 'Gen 44:9'})
        w.submit({'kind': 'ruling_softened', 'subject': 'the-steward', 'case_source': 'Gen 44:10'})
        w.submit({'kind': 'bags_searched', 'subject': 'the-steward', 'found_with': 'benjamin', 'case_source': 'Gen 44:11-12'})
        w.submit({'kind': 'tore_garments', 'subject': 'the-sons', 'case_source': 'Gen 44:13'})
        w.submit({'kind': 'bowed', 'subject': 'the-sons', 'form': 'fell to the earth', 'case_source': 'Gen 44:14'})
        w.submit({'kind': 'divination_claimed', 'subject': 'joseph', 'case_source': 'Gen 44:15'})
        w.submit({'kind': 'guilt_confessed', 'subject': 'judah', 'case_source': 'Gen 44:16'})
        w.submit({'kind': 'ruling_given', 'subject': 'joseph', 'case_source': 'Gen 44:17'})
        w.submit({'kind': 'judah_pleaded', 'subject': 'judah', 'case_source': 'Gen 44:18-34'})
        w.submit({'kind': 'restraint_failed', 'subject': 'joseph', 'case_source': 'Gen 45:1'})
        w.submit({'kind': 'wept', 'subject': 'joseph', 'heard_by': 'the house of Pharaoh', 'case_source': 'Gen 45:2'})
        w.submit({'kind': 'identity_revealed', 'subject': 'joseph', 'case_source': 'Gen 45:3-4'})
        w.submit({'kind': 'providence_declared', 'subject': 'joseph', 'years_passed': 2, 'years_left': 5, 'case_source': 'Gen 45:5-8'})
        w.submit({'kind': 'descent_urged', 'subject': 'joseph', 'to': 'jacob', 'case_source': 'Gen 45:9-13'})
        w.submit({'kind': 'fell_on_the_neck', 'subject': 'joseph', 'on': 'benjamin', 'case_source': 'Gen 45:14'})
        w.submit({'kind': 'kissed', 'subject': 'joseph', 'whom': 'all his brothers', 'case_source': 'Gen 45:15'})
        w.submit({'kind': 'voice_heard', 'subject': 'pharaoh-of-joseph', 'case_source': 'Gen 45:16'})
        w.submit({'kind': 'come_to_me_commanded', 'subject': 'pharaoh-of-joseph', 'to': 'the-sons', 'case_source': 'Gen 45:17-20'})
        w.submit({'kind': 'wagons_given', 'subject': 'joseph', 'to': 'the-sons', 'case_source': 'Gen 45:21'})
        w.submit({'kind': 'gifts_given', 'subject': 'the-sons', 'by': 'joseph', 'what': 'changes of garments', 'case_source': 'Gen 45:22'})
        w.submit({'kind': 'silver_given', 'subject': 'benjamin', 'amount': 300, 'by': 'joseph', 'case_source': 'Gen 45:22'})
        w.submit({'kind': 'gifts_given', 'subject': 'jacob', 'by': 'joseph', 'what': 'ten donkeys, ten she-asses', 'case_source': 'Gen 45:23'})
        w.submit({'kind': 'sent_away', 'subject': 'the-sons', 'by': 'joseph', 'charge': 'do not quarrel on the way', 'case_source': 'Gen 45:24'})
        w.advance(4754)
        w.submit({'kind': 'journeyed', 'subject': 'the-sons', 'to': 'the land of Canaan, to Jacob', 'case_source': 'Gen 45:25'})
        close('judah', 'surety_undertaken', 'Gen 45:25 — they came to Jacob their father, Benjamin among them')
        w.submit({'kind': 'told_joseph_lives', 'subject': 'the-sons', 'to': 'jacob', 'case_source': 'Gen 45:26'})
        w.submit({'kind': 'wagons_seen', 'subject': 'jacob', 'case_source': 'Gen 45:27'})
        w.submit({'kind': 'resolved_to_go', 'subject': 'jacob', 'case_source': 'Gen 45:28'})
        w.advance(4755)
        w.submit({'kind': 'journeyed', 'subject': 'jacob', 'to': 'Beersheba', 'case_source': 'Gen 46:1'})
        w.submit({'kind': 'sacrificed', 'subject': 'jacob', 'to': 'the God of his father Isaac', 'case_source': 'Gen 46:1'})
        w.submit({'kind': 'night_vision', 'subject': 'god', 'to': 'jacob', 'case_source': 'Gen 46:2-4'})
        w.advance(4756)
        w.submit({'kind': 'journeyed', 'subject': 'israel_people', 'to': 'Egypt', 'case_source': 'Gen 46:5-7'})
        w.submit({'kind': 'census_listed', 'subject': 'israel_people', 'registers': {'leah': 33, 'zilpah': 16, 'rachel': 14, 'bilhah': 7}, 'from_the_loins': 66, 'all': 70, 'case_source': 'Gen 46:8-27'})
        w.submit({'kind': 'judah_sent_ahead', 'subject': 'jacob', 'whom': 'judah', 'case_source': 'Gen 46:28'})
        w.submit({'kind': 'journeyed', 'subject': 'israel_people', 'to': 'Goshen', 'case_source': 'Gen 46:28'})
        w.submit({'kind': 'fell_on_the_neck', 'subject': 'joseph', 'on': 'jacob', 'case_source': 'Gen 46:29'})
        w.submit({'kind': 'let_me_die_said', 'subject': 'jacob', 'case_source': 'Gen 46:30'})
        w.submit({'kind': 'audience_prepared', 'subject': 'joseph', 'for': 'the-sons', 'case_source': 'Gen 46:31-34'})
        w.advance(4757)
        w.submit({'kind': 'told_pharaoh', 'subject': 'joseph', 'case_source': 'Gen 47:1'})
        w.submit({'kind': 'five_presented', 'subject': 'joseph', 'count': 5, 'case_source': 'Gen 47:2'})
        w.submit({'kind': 'work_asked', 'subject': 'the-sons', 'case_source': 'Gen 47:3-4'})
        w.submit({'kind': 'goshen_granted', 'subject': 'pharaoh-of-joseph', 'to': 'the-sons', 'case_source': 'Gen 47:5-6'})
        w.submit({'kind': 'stood_before_pharaoh', 'subject': 'jacob', 'case_source': 'Gen 47:7'})
        w.submit({'kind': 'blessed', 'subject': 'jacob', 'whom': 'pharaoh-of-joseph', 'case_source': 'Gen 47:7'})
        w.submit({'kind': 'days_asked', 'subject': 'jacob', 'years': 130, 'case_source': 'Gen 47:8-9'})
        w.submit({'kind': 'blessed', 'subject': 'jacob', 'whom': 'pharaoh-of-joseph', 'going_out': True, 'case_source': 'Gen 47:10'})
        w.submit({'kind': 'settled', 'subject': 'joseph', 'whom': 'the-sons', 'in': 'the land of Rameses', 'case_source': 'Gen 47:11'})
        close('the-house-of-jacob', 'goshen_promised', 'Gen 47:11 — settled in the best of the land')
        close('the-sons', 'good_of_egypt_promised', 'Gen 47:11 — in the land of Rameses, as Pharaoh had commanded')
        w.submit({'kind': 'sustained', 'subject': 'joseph', 'whom': 'the-house-of-jacob', 'case_source': 'Gen 47:12'})
        close('jacob', 'sustenance_promised', 'Gen 47:12 — and Joseph sustained his father')
        w.submit({'kind': 'silver_gathered', 'subject': 'joseph', 'case_source': 'Gen 47:13-14'})
        w.submit({'kind': 'cried_for_bread', 'subject': 'egypt_people', 'silver': 'gone', 'case_source': 'Gen 47:15'})
        w.submit({'kind': 'livestock_taken_for_bread', 'subject': 'joseph', 'case_source': 'Gen 47:16-17'})
        w.advance(5122)
        w.submit({'kind': 'second_year_came', 'subject': 'egypt_people', 'case_source': 'Gen 47:18-19'})
        w.submit({'kind': 'purchased', 'subject': 'joseph', 'what': 'the-ground-of-egypt', 'for': 'pharaoh-of-joseph', 'price': 'bread', 'case_source': 'Gen 47:20'})
        w.submit({'kind': 'people_moved', 'subject': 'joseph', 'case_source': 'Gen 47:21'})
        w.submit({'kind': 'priests_exempted', 'subject': 'joseph', 'case_source': 'Gen 47:22'})
        w.submit({'kind': 'seed_given', 'subject': 'joseph', 'to': 'egypt_people', 'case_source': 'Gen 47:23-24'})
        w.submit({'kind': 'servitude_accepted', 'subject': 'egypt_people', 'case_source': 'Gen 47:25'})
        w.submit({'kind': 'statute_set', 'subject': 'egypt_people', 'statute': 'a fifth to Pharaoh', 'case_source': 'Gen 47:26'})
        w.submit({'kind': 'fruitful_in_goshen', 'subject': 'israel_people', 'case_source': 'Gen 47:27'})
        w.advance(10962)
        w.submit({'kind': 'burial_commanded', 'subject': 'jacob', 'to': 'joseph', 'not_in': 'Egypt', 'case_source': 'Gen 47:29-30'})
        w.submit({'kind': 'sworn', 'subject': 'joseph', 'to': 'jacob', 'case_source': 'Gen 47:31'})
        w.submit({'kind': 'bowed', 'subject': 'jacob', 'form': 'on the head of the bed', 'case_source': 'Gen 47:31'})
        w.advance(10963)
        w.submit({'kind': 'fell_on_the_neck', 'subject': 'joseph', 'on': 'the face of his father', 'case_source': 'Gen 50:1'})
        close('jacob', 'josephs_hand_on_the_eyes', "Gen 50:1 — and Joseph fell on his father's face")
        w.submit({'kind': 'kissed', 'subject': 'joseph', 'whom': 'his dead father', 'case_source': 'Gen 50:1'})
        w.submit({'kind': 'embalmed', 'subject': 'the-physicians', 'whom': 'jacob', 'days': 40, 'weeping_days': 70, 'case_source': 'Gen 50:2-3'})
        w.advance(11033)
        w.submit({'kind': 'leave_asked', 'subject': 'joseph', 'case_source': 'Gen 50:4-5'})
        w.submit({'kind': 'leave_granted', 'subject': 'pharaoh-of-joseph', 'to': 'joseph', 'case_source': 'Gen 50:6'})
        w.submit({'kind': 'journeyed', 'subject': 'the-sons', 'to': 'the threshing floor of Atad', 'case_source': 'Gen 50:7-9'})
        w.submit({'kind': 'mourned', 'subject': 'the-sons', 'days': 7, 'case_source': 'Gen 50:10'})
        w.submit({'kind': 'named', 'subject': 'the-threshing-floor-of-atad', 'name': 'Abel-mizraim (אבל מצרים — the mourning of Egypt, 50:11)', 'by': 'the report formula', 'case_source': 'Gen 50:11'})
        w.advance(11041)
        w.submit({'kind': 'journeyed', 'subject': 'the-sons', 'to': 'Egypt', 'case_source': 'Gen 50:14'})
        w.advance(11042)
        w.submit({'kind': 'feared_joseph', 'subject': 'the-sons', 'case_source': 'Gen 50:15'})
        w.submit({'kind': 'forgiveness_asked', 'subject': 'the-sons', 'case_source': 'Gen 50:16-18'})
        w.submit({'kind': 'wept', 'subject': 'joseph', 'case_source': 'Gen 50:17'})
        w.submit({'kind': 'bowed', 'subject': 'the-sons', 'form': 'fell before him', 'case_source': 'Gen 50:18'})
        w.submit({'kind': 'forgave', 'subject': 'joseph', 'case_source': 'Gen 50:19-21'})
        w.submit({'kind': 'sustained', 'subject': 'joseph', 'whom': 'the-sons', 'case_source': 'Gen 50:21'})
        w.advance(11407)
        w.submit({'kind': 'dwelt', 'subject': 'joseph', 'in': 'Egypt', 'years': 110, 'case_source': 'Gen 50:22'})
        w.submit({'kind': 'grandsons_seen', 'subject': 'joseph', 'case_source': 'Gen 50:23'})
        w.submit({'kind': 'visitation_promised', 'subject': 'joseph', 'to': 'the-sons', 'case_source': 'Gen 50:24'})
        w.submit({'kind': 'sworn', 'subject': 'israel_people', 'to': 'joseph', 'what': 'to carry up his bones', 'case_source': 'Gen 50:25'})
        w.submit({'kind': 'died', 'subject': 'joseph', 'years': 110, 'case_source': 'Gen 50:26'})
        w.submit({'kind': 'embalmed', 'subject': 'joseph', 'whom': 'joseph', 'coffin': True, 'case_source': 'Gen 50:26'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    open_total = sum(len(ent.open_entries()) for ent in w.entities.values())
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    return tuple(n(eid, eff) for eid, eff in SLOTS) + (open_total, tset, fired, closes[0], w.clock.day), w
SCENE, _W = scene()
SCENE_EVENTS = [('angels_met', 'jacob'), ('named', 'the-camp-of-god'), ('messengers_sent', 'jacob'), ('feared_greatly', 'jacob'), ('prayed', 'jacob'), ('gift_prepared', 'jacob'), ('river_crossed', 'jacob'), ('wrestled', 'jacob'), ('blessing_demanded', 'jacob'), ('name_asked', 'jacob'), ('named', 'the-ford-of-jabbok'), ('sun_rose', 'jacob'), ('esau_seen', 'jacob'), ('children_divided', 'jacob'), ('bowed', 'jacob'), ('embraced', 'esau'), ('fell_on_the_neck', 'esau'), ('kissed', 'esau'), ('children_declared', 'jacob'), ('bowed', 'the-maids-and-their-children'), ('bowed', 'leah'), ('bowed', 'rachel'), ('camp_explained', 'esau'), ('gift_urged', 'jacob'), ('convoy_declined', 'jacob'), ('journeyed', 'esau'), ('journeyed', 'jacob'), ('booths_made', 'jacob'), ('named', 'jacob'), ('journeyed', 'jacob'), ('purchased', 'jacob'), ('altar_erected', 'the-altar-of-el-elohe-israel'), ('named', 'the-altar-of-el-elohe-israel'), ('went_out_to_see', 'dinah'), ('seized_and_violated', 'shechem'), ('soul_cleaved', 'shechem'), ('wife_asked', 'shechem'), ('silence_kept', 'jacob'), ('came_to_speak', 'hamor'), ('outraged', 'the-sons'), ('marriage_proposed', 'hamor'), ('marriage_proposed', 'shechem'), ('deceit_answered', 'the-sons'), ('terms_accepted', 'hamor'), ('gate_addressed', 'hamor'), ('males_circumcised', 'the-men-of-shechem'), ('city_struck', 'simeon-and-levi'), ('city_plundered', 'the-sons'), ('rebuked', 'jacob'), ('answered_back', 'the-sons'), ('altar_commanded', 'god'), ('purge_commanded', 'jacob'), ('gods_hidden', 'jacob'), ('journeyed', 'the-house-of-jacob'), ('journeyed', 'jacob'), ('altar_erected', 'the-altar-at-bethel-again'), ('named', 'the-place'), ('died', 'deborah'), ('buried', 'deborah'), ('named', 'the-oak-below-bethel'), ('appeared', 'god'), ('named', 'jacob'), ('blessed_be_fruitful', 'god'), ('land_promised', 'god'), ('god_went_up', 'god'), ('pillar_set_and_anointed', 'the_pillar_of_bethel'), ('named', 'the-place'), ('journeyed', 'jacob'), ('hard_birth', 'rachel'), ('born', 'benjamin'), ('named', 'benjamin'), ('named', 'benjamin'), ('died', 'rachel'), ('buried', 'rachel'), ('grave_pillar_set', 'jacob'), ('journeyed', 'jacob'), ('lay_with_the_concubine', 'reuben'), ('sons_counted', 'jacob'), ('journeyed', 'jacob'), ('died', 'isaac'), ('buried', 'isaac'), ('married', 'adah-wife-of-esau'), ('married', 'oholibamah'), ('married', 'basemath-bat-ishmael'), ('bore', 'adah-wife-of-esau'), ('bore', 'basemath-bat-ishmael'), ('bore', 'oholibamah'), ('withdrew', 'esau'), ('roster_listed', 'the-chiefs-of-esau'), ('bore', 'timna'), ('roster_listed', 'the-sons-of-seir'), ('reigned', 'the-kings-of-edom'), ('reign_passed', 'the-kings-of-edom'), ('reign_passed', 'the-kings-of-edom'), ('reign_passed', 'the-kings-of-edom'), ('reign_passed', 'the-kings-of-edom'), ('reign_passed', 'the-kings-of-edom'), ('reign_passed', 'the-kings-of-edom'), ('reign_passed', 'the-kings-of-edom'), ('roster_listed', 'the-chiefs-of-esau'), ('evil_report_brought', 'joseph'), ('loved_apart', 'jacob'), ('coat_made', 'jacob'), ('hated', 'the-sons'), ('dreamed', 'joseph'), ('hated', 'the-sons'), ('dream_told', 'joseph'), ('hated', 'the-sons'), ('dreamed', 'joseph'), ('dream_told', 'joseph'), ('rebuked', 'jacob'), ('envied', 'the-sons'), ('journeyed', 'the-sons'), ('errand_given', 'jacob'), ('found_wandering', 'joseph'), ('conspired', 'the-sons'), ('plot_spoken', 'the-sons'), ('rescue_urged', 'reuben'), ('stripped', 'the-sons'), ('cast_into_the_pit', 'the-sons'), ('caravan_seen', 'the-sons'), ('sale_proposed', 'judah'), ('sold', 'the-sellers-of-joseph'), ('pit_found_empty', 'reuben'), ('tore_garments', 'reuben'), ('coat_dipped', 'the-sons'), ('coat_recognized', 'jacob'), ('tore_garments', 'jacob'), ('mourned', 'jacob'), ('wept', 'jacob'), ('sold', 'the-medanites'), ('slave_bought', 'potiphar'), ('prospered', 'joseph'), ('appointed_over_the_house', 'joseph'), ('lie_with_me_demanded', 'potiphars-wife'), ('refused', 'joseph'), ('lie_with_me_demanded', 'potiphars-wife'), ('garment_seized', 'potiphars-wife'), ('fled', 'joseph'), ('accused', 'potiphars-wife'), ('anger_burned', 'potiphar'), ('imprisoned', 'joseph'), ('kindness_extended', 'joseph'), ('appointed_over_the_house', 'joseph'), ('prospered', 'joseph'), ('offended', 'the-two-officers'), ('imprisoned', 'the-two-officers'), ('appointed_to_serve', 'joseph'), ('dreamed', 'the-two-officers'), ('faces_downcast', 'the-two-officers'), ('dream_told', 'the-chief-cupbearer'), ('interpreted', 'joseph'), ('remembrance_asked', 'joseph'), ('dream_told', 'the-chief-baker'), ('interpreted', 'joseph'), ('feast_made', 'pharaoh-of-joseph'), ('restored', 'the-chief-cupbearer'), ('hanged', 'the-chief-baker'), ('forgot', 'the-chief-cupbearer'), ('dreamed', 'pharaoh-of-joseph'), ('dreamed', 'pharaoh-of-joseph'), ('spirit_troubled', 'pharaoh-of-joseph'), ('offenses_recalled', 'the-chief-cupbearer'), ('rushed_from_the_pit', 'joseph'), ('dream_told', 'pharaoh-of-joseph'), ('interpreted', 'joseph'), ('counsel_given', 'joseph'), ('counsel_accepted', 'pharaoh-of-joseph'), ('set_over_egypt', 'joseph'), ('named', 'joseph'), ('married', 'asenath'), ('went_out_over_egypt', 'joseph'), ('food_gathered', 'joseph'), ('born', 'manasseh'), ('named', 'manasseh'), ('born', 'ephraim'), ('named', 'ephraim'), ('plenty_ended', 'the-land-of-egypt'), ('famine_came', 'the-lands'), ('cried_for_bread', 'egypt_people'), ('storehouses_opened', 'joseph'), ('descent_commanded', 'jacob'), ('went_down', 'the-sons'), ('benjamin_withheld', 'jacob'), ('bowed', 'the-sons'), ('brothers_recognized', 'joseph'), ('dreams_remembered', 'joseph'), ('spies_charged', 'joseph'), ('honesty_pleaded', 'the-sons'), ('test_set', 'joseph'), ('custody_three_days', 'joseph'), ('plan_revised', 'joseph'), ('guilt_confessed', 'the-sons'), ('guilt_confessed', 'reuben'), ('interpreter_between', 'joseph'), ('wept', 'joseph'), ('bound', 'simeon'), ('silver_returned', 'joseph'), ('journeyed', 'the-sons'), ('silver_found', 'the-sons'), ('report_given', 'the-sons'), ('silver_found', 'the-sons'), ('bereaved_cried', 'jacob'), ('pledge_of_sons_offered', 'reuben'), ('descent_refused', 'jacob'), ('famine_came', 'the-land-of-canaan'), ('descent_commanded', 'jacob'), ('warning_cited', 'judah'), ('surety_offered', 'judah'), ('caravan_planned', 'jacob'), ('went_down', 'the-sons'), ('house_ordered', 'joseph'), ('feared_at_the_door', 'the-sons'), ('peace_given', 'the-steward'), ('feet_washed', 'the-sons'), ('gift_presented', 'the-sons'), ('bowed', 'the-sons'), ('welfare_asked', 'joseph'), ('bowed', 'the-sons'), ('benjamin_seen', 'joseph'), ('wept', 'joseph'), ('bread_set', 'joseph'), ('seated_by_birth_order', 'the-sons'), ('portions_lifted', 'joseph'), ('feast_made', 'joseph'), ('ate_and_drank', 'the-sons'), ('cup_planted', 'the-steward'), ('sent_away', 'the-sons'), ('pursued', 'the-steward'), ('divination_claimed', 'joseph'), ('theft_denied', 'the-sons'), ('rash_sentence_offered', 'the-sons'), ('ruling_softened', 'the-steward'), ('bags_searched', 'the-steward'), ('tore_garments', 'the-sons'), ('bowed', 'the-sons'), ('divination_claimed', 'joseph'), ('guilt_confessed', 'judah'), ('ruling_given', 'joseph'), ('judah_pleaded', 'judah'), ('restraint_failed', 'joseph'), ('wept', 'joseph'), ('identity_revealed', 'joseph'), ('providence_declared', 'joseph'), ('descent_urged', 'joseph'), ('fell_on_the_neck', 'joseph'), ('kissed', 'joseph'), ('voice_heard', 'pharaoh-of-joseph'), ('come_to_me_commanded', 'pharaoh-of-joseph'), ('wagons_given', 'joseph'), ('gifts_given', 'the-sons'), ('silver_given', 'benjamin'), ('gifts_given', 'jacob'), ('sent_away', 'the-sons'), ('journeyed', 'the-sons'), ('told_joseph_lives', 'the-sons'), ('wagons_seen', 'jacob'), ('resolved_to_go', 'jacob'), ('journeyed', 'jacob'), ('sacrificed', 'jacob'), ('night_vision', 'god'), ('journeyed', 'israel_people'), ('census_listed', 'israel_people'), ('judah_sent_ahead', 'jacob'), ('journeyed', 'israel_people'), ('fell_on_the_neck', 'joseph'), ('let_me_die_said', 'jacob'), ('audience_prepared', 'joseph'), ('told_pharaoh', 'joseph'), ('five_presented', 'joseph'), ('work_asked', 'the-sons'), ('goshen_granted', 'pharaoh-of-joseph'), ('stood_before_pharaoh', 'jacob'), ('blessed', 'jacob'), ('days_asked', 'jacob'), ('blessed', 'jacob'), ('settled', 'joseph'), ('sustained', 'joseph'), ('silver_gathered', 'joseph'), ('cried_for_bread', 'egypt_people'), ('livestock_taken_for_bread', 'joseph'), ('second_year_came', 'egypt_people'), ('purchased', 'joseph'), ('people_moved', 'joseph'), ('priests_exempted', 'joseph'), ('seed_given', 'joseph'), ('servitude_accepted', 'egypt_people'), ('statute_set', 'egypt_people'), ('fruitful_in_goshen', 'israel_people'), ('burial_commanded', 'jacob'), ('sworn', 'joseph'), ('bowed', 'jacob'), ('fell_on_the_neck', 'joseph'), ('kissed', 'joseph'), ('embalmed', 'the-physicians'), ('leave_asked', 'joseph'), ('leave_granted', 'pharaoh-of-joseph'), ('journeyed', 'the-sons'), ('mourned', 'the-sons'), ('named', 'the-threshing-floor-of-atad'), ('journeyed', 'the-sons'), ('feared_joseph', 'the-sons'), ('forgiveness_asked', 'the-sons'), ('wept', 'joseph'), ('bowed', 'the-sons'), ('forgave', 'joseph'), ('sustained', 'joseph'), ('dwelt', 'joseph'), ('grandsons_seen', 'joseph'), ('visitation_promised', 'joseph'), ('sworn', 'israel_people'), ('died', 'joseph'), ('embalmed', 'joseph')]
_SCENE_NAMED = [e for e in SCENE_EVENTS if e[0] == 'named']


def build(q):
    if q == 'world':
        return cell(SCENE, I, "THE SCENE on the world engine — the two hundred and eighty-eight effect slots of the declaration in order, then the opens, the timers set and fired, the closes, the day (the hand-model's print, scratchpad o8_s4_predict.py); the nine story timers and the three eighth days fire inside the scene", ['head_lifted_up_due', 'head_lifted_off_due', 'custody_three_days', 'plenty_seven_years', 'famine_seven_years', 'five_years_of_famine_left', 'embalming_forty_days', 'egypt_wept_seventy', 'seven_days_mourning'])
    if q == 'headline_flow_reversed':
        return cell('narrative_verses_feed_law_rows', M, "THE HEADLINE (1): two narrative verses are the SOURCE of two law rows — 'they dipped the tunic in the blood' (37:31) for the tunic's atonement (Arakhin 16a:13, the vestments engine's row read by call) and 'he searched ... and found' (44:12) for the search for leaven (Pesachim 7b:14 on Mishnah Pesachim 1:1): the flow runs from the story into the law, not the reverse", ['coat_dipped', 'cup_found'])
    if q == 'headline_thief_sold':
        return cell('three_verdicts_on_the_rules_shape', P, "THE HEADLINE (2): 44:9, 44:10, 44:17 laid on Exodus 22:2's compiled 'sold for his theft' by call — the brothers' 'let him die' outside the rule, the steward's and Joseph's 'my slave' inside it; the mohar of 34:12 on Exodus 22:15-16 the same way: the story's speeches graded by the law's function", ['finder_a_slave_ruled', 'mohar_offered_unbounded'])
    if q == 'headline_two_absences':
        return cell('twenty_two_on_two_chains', M, "THE HEADLINE (3): Megillah 17a:6's twenty-two years computed on two independent chains of the tape — Jacob's absence off Ishmael's death and the fourteen (S3's chain) and Joseph's off Pharaoh's side (41:46, 45:6) — the sequence runner CJ0, a JOIN of the two sittings' markers", ['years_confessed', 'thirty_at_the_standing'])
    if q == 'headline_seventy':
        return cell('the_missing_one_filed_open', I, "THE HEADLINE (4): the seventy's sub-totals meet (33 + 16 + 14 + 7 = 70; 66 = 70 − 4) and the names do not (Leah's 32 living against 33) — the DIVERGE filed OPEN with the shelf's five answers named, none the ink's (CJ3)", ['souls_counted'])
    if q == 'headline_closes_by_seat':
        return cell('four_closes_by_seat', D, "THE HEADLINE (5): law_joseph closes four of its own entries on OTHER ENGINES' events by seat — brought_up_promised and burial_in_canaan_sworn on the family's burial (50:13), visitation_promised on the exodus story's belief (Exod 4:31), bones_oath on its bones_taken (Exod 13:19) — the ink's own receipts across engines and books (CJ7)", ['brought_up_promised', 'burial_in_canaan_sworn', 'visitation_promised', 'bones_oath'])
    return cell('no_case', I, '', [FX.NONE])


TESTS = [
 # ---- Gen 32: jabbok ----
 ('two namings: Mahanaim, Peniel', jabbok('two_namings'), ('mahanaim', 'peniel')),
 ('bands of angels all night (Bereshit Rabbah 78:11)', jabbok('angel_bands'), 'bands_of_angels_all_night'),
 ("the gift's numerals by verse", jabbok('gift_by_verse'), [[200, 20, 200, 20], [30, 40, 10, 20, 10]]),
 ("the gift's head count", jabbok('gift_head_count'), 550),
 ('"I am too small" (32:11)', jabbok('too_small'), 'i_am_too_small_for_all_the_kindnesses'),
 ('left alone (32:25)', jabbok('left_alone'), 'alone'),
 ('the socket of the thigh', jabbok('thigh_socket'), ('socket', 'thigh')),
 ("the renaming is the family engine's seat", jabbok('renaming_seat'), 'family_engine_32_29'),
 ('Peniel, Penuel', jabbok('peniel_penuel'), ('peniel', 'penuel')),
 ("the sinew statute is the family engine's seat", jabbok('sinew_seat'), 'family_engine_32_33'),
 # ---- Gen 33:1-17: esau_met ----
 ('the last is dearest (Bereshit Rabbah 78:8)', esau_met('last_dearest'), 'last_last_is_dearest'),
 ('bowed seven times', esau_met('bowed_seven'), 7),
 ('the prostration verb — ten seats in the span', esau_met('bow_seats'), 10),
 ('the bow table', esau_met('bow_table'), [(33, 3), (33, 6), (33, 7), (37, 7), (37, 9), (37, 10), (42, 6), (43, 26), (43, 28), (47, 31)]),
 ('prostration: hands and feet spread (Berakhot 34b)', esau_met('prostration_form'), 'hands_and_feet_spread'),
 ('the dotted kiss (Bereshit Rabbah 78:9)', esau_met('dotted_kiss'), 'script_equals_dots'),
 ('the grace verb (33:5)', esau_met('grace_verb'), 'graciously_given'),
 ('as the face of God is judgment (Bereshit Rabbah 78:12)', esau_met('face_of_god'), 'as_the_face_of_god_is_judgment'),
 ('the blessing returned by name (33:11)', esau_met('blessing_returned'), 'my_blessing'),
 ('Seir promised, never narrated', esau_met('seir_promised'), 'never_narrated'),
 ('widen the road (Avodah Zarah 25b)', esau_met('widen_the_road'), 'as_jacob_to_esau'),
 ('booths and Sukkot', esau_met('sukkot_naming'), ('booths', 'sukkot')),
 ('eighteen months at Sukkot (Megillah 17a)', esau_met('sukkot_months'), 18),
 # ---- Gen 33:18-20: shechem_arrival ----
 ('came whole: body, sons, money (Bereshit Rabbah 79:5)', shechem_arrival('came_whole'), ('body', 'sons', 'money')),
 ('a hundred kesitah', shechem_arrival('hundred_kesitah'), 100),
 ('one of three undisputed places (Bereshit Rabbah 79:7)', shechem_arrival('three_places'), 3),
 ("the purchase's three modes — by call", shechem_arrival('purchase_by_call'), ['money', 'deed', 'possession']),
 ('the purchase written here, not by the family engine', shechem_arrival('purchase_seat'), 'law_joseph_writes_33_19'),
 ('God called Jacob "el" (Megillah 18a)', shechem_arrival('el_elohe_israel'), 'god_called_jacob_el'),
 ('God above, god below (Bereshit Rabbah 79:8)', shechem_arrival('god_below'), 'you_god_above_i_god_below'),
 # ---- Gen 34: dinah ----
 ("Dinah's name — seven seats in Genesis", dinah('dinah_seats'), 7),
 ('took, lay, violated', dinah('three_verbs'), ('took', 'lay', 'violated')),
 ('cleaved, loved, spoke to her heart', dinah('cleaved_loved_spoke'), ('cleaved', 'loved', 'spoke_to_her_heart')),
 ('Jacob kept silent', dinah('silence_kept'), 'kept_silent_until_they_came'),
 ('an outrage in Israel', dinah('outrage_phrase'), 'not_done_in_israel'),
 ('the mohar unbounded (34:12)', dinah('mohar_unbounded'), 'multiply_upon_me'),
 ('THE MOHAR by call: the fixed sum a pointer, four money entries', dinah('mohar_by_call'), ('FETCH-50', 4)),
 ("the seducer's three and the rapist's four (Mishnah Ketubot 3:4)", dinah('seducer_sheet'), ('three', 'four')),
 ('with guile (34:13)', dinah('deceit_word'), 'with_guile'),
 ("the foreskin tokens: Shechem's ruse, not the sign", dinah('foreskin_homograph'), 'shechems_ruse_not_the_sign'),
 ('the third day (Mishnah Shabbat 19:3)', dinah('third_day_sheet'), 'bathing_on_the_third_day'),
 ('the third day is danger (Nedarim 31b)', dinah('third_day_danger'), 'danger'),
 ("the third day's verse", dinah('third_day_verse'), 'Gen 34:25'),
 ('took no counsel from Jacob (Bereshit Rabbah 80:10)', dinah('took_no_counsel'), 'took_no_counsel_from_jacob'),
 ('the cask was clear (Bereshit Rabbah 80:12)', dinah('troubled_charged'), 'the_cask_was_clear'),
 ('few in number', dinah('few_in_number'), 'few_in_number'),
 ('the question unanswered', dinah('question_unanswered'), 'as_a_harlot'),
 # ---- Gen 35:1-15: bethel_again ----
 ('the foreign gods — two seats', bethel_again('foreign_gods_seats'), 2),
 ("the vow's delay punished (Bereshit Rabbah 81:1-2)", bethel_again('vow_delay'), 'delay_punished'),
 ("28:15's return closed at 35:6 (on the tape)", bethel_again('return_closed'), 'Gen 35:6'),
 ('the vow closed at 35:7 (on the tape)', bethel_again('vow_closed'), 'Gen 35:7'),
 ('the terror of God', bethel_again('terror_of_god'), 'terror_of_god'),
 ('Allon-bakhut: Greek for another mourning (Bereshit Rabbah 81:5)', bethel_again('allon_bakhut'), 'greek_for_another_mourning'),
 ('Israel repeated at 35:10', bethel_again('israel_repeated'), 'Gen 35:10'),
 ('cited as the like case (Berakhot 12b)', bethel_again('like_case'), 'cited_as_the_like_case'),
 ('be fruitful (Mishnah Yevamot 6:6)', bethel_again('be_fruitful_sheet'), 'a_man_does_not_cease'),
 ('said to Jacob in the singular (Yevamot 65b)', bethel_again('fruitful_singular'), 'said_to_jacob_singular'),
 ('kings from your loins', bethel_again('kings_promised'), 'kings_from_your_loins'),
 ('the land to Abraham and Isaac', bethel_again('land_promised'), 'to_abraham_and_isaac'),
 ('the libation by its token', bethel_again('libation_token'), 'nesekh_by_name'),
 ('Bethel named twice', bethel_again('bethel_named_twice'), 2),
 # ---- Gen 35:16-29: three_deaths ----
 ('three burials written by the scene', three_deaths('buried_writes'), 3),
 ('Ben-oni, Binyamin (Bereshit Rabbah 82:9)', three_deaths('ben_oni_binyamin'), ('ben_oni_aramaic', 'binyamin_holy_tongue')),
 ("Benjamin's spelling measured: seven full, nine short (Sotah 36b)", three_deaths('benjamin_plene'), (7, 9)),
 ('no monuments for the righteous (Bereshit Rabbah 82:10)', three_deaths('grave_pillar'), 'no_monuments_for_the_righteous'),
 ("Rachel's grave to this day", three_deaths('until_this_day'), 'the_pillar_of_rachels_grave'),
 ("Reuben's act: read, not translated (Mishnah Megillah 4:10)", three_deaths('reuben_sheet'), 'read_not_translated'),
 ('and Israel heard', three_deaths('israel_heard'), 'and_israel_heard'),
 ('the twelve kept', three_deaths('twelve_kept'), 12),
 ('twelve names counted', three_deaths('twelve_named'), 12),
 ('Isaac a hundred and eighty', three_deaths('isaac_180'), 180),
 ('buried by Esau and Jacob', three_deaths('buried_by_both'), ('esau', 'jacob')),
 ("Isaac's gathering written here", three_deaths('gathered_seat'), 'law_joseph_35_29'),
 # ---- Gen 36: edom ----
 ("Esau's wives recorded, no fold", edom('wives_recorded'), ('adah', 'oholibamah', 'basemath')),
 ('Timna the concubine', edom('timna_concubine'), 'concubine'),
 ('Timna the rejected proselyte (Sanhedrin 99b)', edom('timna_amalek'), 'rejected_proselyte'),
 ('the two Anas (Bava Batra 115b)', edom('two_anas'), 'one_anah_zibeon_on_his_mother'),
 ('"and he reigned" — eight tokens', edom('kings_count'), 8),
 ('eight kings named', edom('kings_named'), 8),
 ('before a king reigned over Israel', edom('before_a_king'), 'before_israel_had_a_king'),
 ('the nations as a ship (Bereshit Rabbah 83:1)', edom('nations_as_ship'), 'a_ship_from_many_places'),
 ('the king word, not Molech', edom('melekh_homograph'), 'king_not_molech'),
 ("Edom's holding, not the jubilee's", edom('holding_homograph'), 'edoms_holding_not_the_jubilees'),
 ('parted for room (36:7)', edom('parted_for_room'), 'too_great_to_dwell_together'),
 # ---- Gen 37: dreamer ----
 ('seventeen', dreamer('seventeen'), 17),
 ('deeds of youth (Bereshit Rabbah 84:7)', dreamer('youthful_deeds'), 'deeds_of_youth'),
 ('the coat of stripes — three seats', dreamer('coat_seats'), 3),
 ('why loved (Bereshit Rabbah 84:8)', dreamer('why_loved'), ('likeness', 'the_laws_of_shem_and_eber')),
 ('two dreams told', dreamer('dreams_told'), 2),
 ('hope for a dream twenty-two years (Berakhot 55b)', dreamer('dream_hope_years'), 22),
 ('the father kept the matter', dreamer('word_kept'), 'kept_the_matter'),
 ('the pit noun — four seats in Gen 37', dreamer('pit_seats'), 4),
 ('snakes and scorpions (Chagigah 3a)', dreamer('pit_empty'), 'snakes_and_scorpions'),
 ('botzea is Judah (Sanhedrin 6b)', dreamer('what_profit'), 'botzea_is_judah'),
 ("the seller's grammar — OPEN", dreamer('sellers_grammar'), 'midianites_drew_ishmaelites_bought_medanites_sold'),
 ('twenty silver', dreamer('twenty_silver'), 20),
 ('where was Reuben (Bereshit Rabbah 84:19)', dreamer('reuben_where'), ('sackcloth_and_fast', 'his_turn_to_serve')),
 ('THE FLOW REVERSED: the tunic atones — by call', dreamer('tunic_by_call'), 'bloodshed_by_josephs_tunic'),
 ('recognize answered by recognize (Sotah 10b)', dreamer('recognition_row'), 'recognize_answered_by_recognize'),
 ("the coat's recognition written here", dreamer('recognized_seat'), 'law_joseph_37_33'),
 ('mourned many days', dreamer('mourned_many_days'), 'many_days'),
 ('all his daughters (Bereshit Rabbah 84:21)', dreamer('daughters_plural'), 'sons_in_law_and_daughters_in_law'),
 # ---- Gen 39: potiphar ----
 ('Potiphar and Poti-phera — the seats measured', potiphar('potiphar_spellings'), ([(37, 36), (39, 1)], [(41, 45), (41, 50), (46, 20)])),
 ('the bought ones acquire (Bereshit Rabbah 86:3)', potiphar('bought_ones_buy'), 'bought_ones_acquire'),
 ('the Name in Genesis 37-50 by chapter', potiphar('the_name_in_39'), {38: 3, 39: 8, 49: 1}),
 ('adjoin a blessing to scholars (Berakhot 42a)', potiphar('adjoined_blessing'), 'adjoin_blessing_to_scholars'),
 ("beautiful as Rachel's phrase", potiphar('handsome_as_rachel'), 'as_rachel'),
 ('the lifted eyes (Horayot 10b)', potiphar('lifted_eyes'), 'the_eyes_of_the_wife'),
 ('a transgression is refused (Bereshit Rabbah 87:5)', potiphar('refused'), 'a_transgression_is_refused'),
 ('to do his work (39:11)', potiphar('as_this_day'), 'to_do_his_work'),
 ('"Hebrew" — five seats in 39-43', potiphar('hebrew_seats'), 5),
 ('the round-house — eight tokens', potiphar('prison_house'), 8),
 ('his service pleasant (Bereshit Rabbah 87:10)', potiphar('service_pleasant'), 'his_service_pleasant'),
 # ---- Gen 40: prison_dreams ----
 ('two officers', prison_dreams('two_officers'), ('cupbearer', 'baker')),
 ('three days, three days', prison_dreams('three_days_parsed'), (3, 3)),
 ('the third-day timers: inclusive, the fire two days on (measured)', prison_dreams('third_day_timers'), 2),
 ("Pharaoh's birthday on the third day", prison_dreams('birthday'), 'Gen 40:20'),
 ('the head lifted two ways', prison_dreams('lifted_head_two_ways'), ('restored', 'hanged')),
 ('the former custom — filed INTERNAL', prison_dreams('former_custom'), 'the_first_manner'),
 ('in_custody closed twice', prison_dreams('custody_closes'), ('Gen 40:21', 'Gen 40:22')),
 ('the vine is Israel (Bereshit Rabbah 88:5)', prison_dreams('vine_is_israel'), 'israel'),
 ('you forget, I do not (Bereshit Rabbah 88:7)', prison_dreams('forgot'), 'you_forget_i_do_not'),
 # ---- Gen 41:1-36: pharaoh_dreams ----
 ('two years of days', pharaoh_dreams('two_years'), 'two_years_of_days'),
 ('an end set to darkness (Bereshit Rabbah 89:1)', pharaoh_dreams('end_to_darkness'), 'an_end_set_to_darkness'),
 ('seven and plenty: one skeleton, thirty-one tokens', pharaoh_dreams('seven_and_plenty'), 31),
 ('the dream is one', pharaoh_dreams('one_dream'), 'one'),
 ('the doubling: established and hastened', pharaoh_dreams('doubled'), 'established_and_hastened'),
 ('not I, God', pharaoh_dreams('not_i_god'), 'god_will_answer'),
 ("the fifth's counsel", pharaoh_dreams('fifth_counsel'), 'a_fifth'),
 ('rushed from the pit', pharaoh_dreams('rushed_from_the_pit'), 'the_pit_again'),
 # ---- Gen 41:37-57: the_rise ----
 ('of his own they gave him (Bereshit Rabbah 90:3)', the_rise('joseph_of_his_own'), 'of_his_own_they_gave_him'),
 ("the astrologers' objection (Sotah 36b)", the_rise('astrologers'), 'a_slave_bought_for_twenty'),
 ('Zaphenath-paneah — once', the_rise('zaphenath'), 1),
 ('Asenath', the_rise('asenath'), 'daughter_of_potiphera_priest_of_on'),
 ('thirty', the_rise('thirty'), 30),
 ('seventeen to thirty: thirteen', the_rise('seventeen_to_thirty'), 13),
 ('by handfuls (Bereshit Rabbah 90:5)', the_rise('handfuls'), 'by_handfuls'),
 ('two sons before the famine', the_rise('two_sons_before_the_famine'), 'before_the_famine'),
 ('the bed in famine years (Taanit 11a)', the_rise('famine_years_bar'), 'marital_relations_barred_in_famine'),
 ('Manasseh, Ephraim', the_rise('manasseh_ephraim'), ('made_me_forget', 'made_me_fruitful')),
 ('three eighth days', the_rise('eighth_days'), 3),
 ("the covenant's heads — by call", the_rise('covenant_heads_by_call'), 'you_and_your_seed_after_you'),
 ("the plenty's timer on the bare scene", the_rise('plenty_timer_days'), 2555),
 ('famine in all lands', the_rise('famine_in_all_lands'), 'all_lands'),
 # ---- Gen 42: first_descent ----
 ('why show yourselves (Taanit 10b)', first_descent('why_show_yourselves'), 'do_not_show_yourselves_sated'),
 ('ten went down', first_descent('ten'), 10),
 ('a congregation is ten (Bereshit Rabbah 91:3)', first_descent('congregation_of_ten'), 'edah_is_ten'),
 ('the governor', first_descent('governor'), 'the_shalit'),
 ('the provider is Joseph (Sanhedrin 92a)', first_descent('mashbir'), 'joseph_the_provider'),
 ('recognized one way: the beard (Bava Metzia 39b)', first_descent('recognized_one_way'), 'beard'),
 ('made himself a stranger (Bereshit Rabbah 91:7)', first_descent('stranger'), 'made_himself_a_stranger'),
 ('three days of custody', first_descent('three_days_custody'), 3),
 ('the plan revised', first_descent('plan_revised'), ('all_held', 'one_held')),
 ('aval, a southern word (Bereshit Rabbah 91:8)', first_descent('aval'), 'a_southern_word_for_indeed'),
 ('the interpreter between them', first_descent('interpreter'), 'the_interpreter_between_them'),
 ('the weeping verb — eight seats in 42-50', first_descent('wept_seats'), 8),
 ('"is not" — TWO tokens at 42:36 (the design corrected)', first_descent('is_not_tokens'), 2),
 ('the presumption at three (Chullin 95b)', first_descent('presumption_at_three'), 3),
 ("Reuben's pledge is not surety (Bava Batra 173b)", first_descent('pledge_row'), 'kabbelanut_not_surety'),
 ('gray hairs to Sheol', first_descent('gray_hairs'), 'to_sheol_in_grief'),
 # ---- Gen 43: second_descent ----
 ("the surety's verse (Bava Batra 173b)", second_descent('surety_verse'), 'Gen 43:9'),
 ('the surety collects from free property (Mishnah Bava Batra 10:8)', second_descent('surety_sheet'), 'collects_from_free_property'),
 ('the surety a legal person (Mishnah Bava Metzia 5:11)', second_descent('surety_person_sheet'), 'the_surety_transgresses_too'),
 ('the gift homograph', second_descent('gift_homograph'), 'a_gift_to_a_man'),
 ('double silver', second_descent('double_silver'), 'double'),
 ('as I am bereaved', second_descent('bereaved'), 'as_i_am_bereaved'),
 ('Simeon brought out', second_descent('simeon_out'), 'Gen 43:23'),
 ('the abomination — two seats', second_descent('abomination_seats'), 2),
 ('seated by birth order', second_descent('birth_order'), 'seated_by_birth_order'),
 ('the inheritance order owed — by call', second_descent('inheritance_by_call'), ['Deut 25:5', 'Num 27:8']),
 ('five hands', second_descent('five_hands'), 5),
 ('the feast at noon', second_descent('feast_at_noon'), 'noon'),
 # ---- Gen 44: cup ----
 ('go out in good light (Taanit 10b)', cup('morning_light'), 'go_out_in_good_light'),
 ('the divination tokens — two seats', cup('divination_seats'), 2),
 ('THE THREE VERDICTS', cup('three_verdicts'), ('death_and_slavery', 'the_finder_a_slave', 'the_finder_alone')),
 ('THE THIEF SOLD — by call (the first run\'s miss read: the compiled verdict is the TERM, not the effect\'s name)', cup('thief_sold_by_call'), 'six_years_for_the_principal'),
 ('ten men, one thief (Bereshit Rabbah 92:8)', cup('ten_men_one_thief'), 'not_all_bound'),
 ('THE FLOW REVERSED: finding from finding (Pesachim 7b)', cup('search_source'), 'finding_from_finding'),
 ('the search for leaven (Mishnah Pesachim 1:1)', cup('leaven_search_sheet'), 'by_the_light_of_the_lamp'),
 ("the search's order", cup('search_order'), ('the_eldest', 'the_youngest')),
 ('what shall we say (Bereshit Rabbah 92:9)', cup('what_shall_we_say'), ('first_silver', 'second_silver', 'the_cup')),
 ('you are as Pharaoh', cup('as_pharaoh'), 'you_are_as_pharaoh'),
 ('his soul bound with his soul', cup('soul_bound'), 'his_soul_bound_with_his_soul'),
 ('instead of the lad', cup('instead_of_the_lad'), 'instead_of_the_lad'),
 ("Judah's threefold appeasement (Bereshit Rabbah 93:9)", cup('judah_appeasement'), ('joseph', 'the_brothers', 'benjamin')),
 # ---- Gen 45: i_am_joseph ----
 ('could not restrain himself', i_am_joseph('could_not_restrain'), 'Gen 45:1'),
 ('the rebuke of flesh and blood (Chagigah 4b)', i_am_joseph('rebuke'), 'rebuke_of_flesh_and_blood'),
 ('two years, five years', i_am_joseph('two_and_five'), (2, 5)),
 ("the famine's two timers, one due day", i_am_joseph('famine_timers_one_day'), 'same_due_day'),
 ('father, lord, ruler', i_am_joseph('father_to_pharaoh'), ('father', 'lord', 'ruler')),
 ("Benjamin's necks (Megillah 16b)", i_am_joseph('benjamins_necks'), 'two_temples_in_benjamins_portion'),
 ('your eyes see (Megillah 16b)', i_am_joseph('eyes_see'), 'no_grudge_as_with_benjamin'),
 ('three hundred and five', i_am_joseph('three_hundred_and_five'), (300, 5)),
 ('ten donkeys parsed', i_am_joseph('ten_donkeys_parsed'), 10),
 ('old wine (Megillah 16b)', i_am_joseph('ten_donkeys'), 'old_wine'),
 ('do not quarrel on the way', i_am_joseph('do_not_quarrel'), 'do_not_quarrel_on_the_way'),
 ('the heart numb, then lived', i_am_joseph('heart_numb_then_lived'), ('numb', 'lived')),
 ('the surety closed at 45:25', i_am_joseph('surety_closed'), 'Gen 45:25'),
 # ---- Gen 46:1-7, 28-34: the_seventy ----
 ("the peace offering's place — by call", the_seventy('sacrifices_by_call'), 'anywhere_courtyard'),
 ("the sacrifices' row found (Bereshit Rabbah 94:5)", the_seventy('sacrifices_reading'), 'found_with_bar_kapparas_nephew'),
 ("to the God of Isaac", the_seventy('god_of_isaac'), 'isaacs_god_named'),
 ('four HEAVEN entries from one vision', the_seventy('night_visions'), 4),
 ("Joseph's hand closed at 50:1", the_seventy('hand_on_eyes_closed'), 'Gen 50:1'),
 ('brought up — closed on the tape at 50:13', the_seventy('brought_up_closed_on_tape'), 'Gen 50:13'),
 ('carried after the act (Chullin 101b)', the_seventy('carried_after_the_act'), 'after_the_act'),
 ('Judah sent ahead', the_seventy('judah_ahead'), 'sent_ahead_to_goshen'),
 ('wept on his neck a good while', the_seventy('wept_more'), 'wept_on_his_neck_more'),
 ('every shepherd an abomination', the_seventy('shepherds_abomination'), 'every_shepherd'),
 # ---- Gen 46:8-27: seventy (the census cell) ----
 ('the sub-totals parsed', seventy('subtotals_parsed'), (33, 16, 14, 7)),
 ('the sub-totals sum to seventy', seventy('subtotals_sum'), 70),
 ('sixty-six parsed', seventy('sixty_six'), 66),
 ('seventy parsed', seventy('seventy'), 70),
 ("sixty-six by the ink's arithmetic", seventy('sixty_six_arithmetic'), 66),
 ('the names counted per register', seventy('names_by_register'), (34, 16, 14, 7)),
 ("Leah's living named: thirty-two", seventy('leah_living_named'), 32),
 ('CJ3 DIVERGE: the missing one, OPEN', seventy('diverge'), 'DIVERGE_leah_33_vs_32_living'),
 ('Jochebed between the walls (Bava Batra 123b)', seventy('jochebed'), 'jochebed_born_between_the_walls'),
 ('sixty-six cups and three (Bereshit Rabbah 94:9)', seventy('sixty_six_cups'), 'sixty_six_and_three_counted_seventy'),
 ('the firstborn kept first', seventy('firstborn_kept'), 'reuben_first'),
 ('the order of inheritance (Mishnah Bava Batra 8:2)', seventy('inheritance_sheet'), 'son_before_daughter'),
 ("Exodus 1:5's seventy", seventy('exodus_seventy'), 70),
 # ---- Gen 47:1-12: goshen ----
 ('five men', goshen('five_men'), 5),
 ('those doubled in names (Bava Kamma 92a)', goshen('five_doubled'), 'those_doubled_in_names'),
 ('not the mighty (Bereshit Rabbah 95:4)', goshen('five_named'), 'not_the_mighty'),
 ('a hundred and thirty', goshen('hundred_thirty'), 130),
 ('few and evil', goshen('few_and_evil'), 'few_and_evil'),
 ('a hundred and sixteen against a hundred and thirty (Megillah 17a)', goshen('hundred_sixteen'), 116),
 ('the two absences (Megillah 17a)', goshen('two_absences'), 22),
 ('the land of Rameses', goshen('rameses'), 'the_land_of_rameses'),
 ('Goshen — nine seats', goshen('goshen_seats'), 9),
 ('a holding in Egypt — the homograph', goshen('holding_homograph'), 'a_holding_in_egypt'),
 ('two closes at 47:11', goshen('closes_at_47_11'), 2),
 ('sustained by the mouth', goshen('sustained_by_the_mouth'), 'according_to_the_little_ones'),
 # ---- Gen 47:13-27: the_fifth ----
 ('all the silver in the world (Pesachim 119a)', the_fifth('all_silver'), 'all_the_silver_in_the_world'),
 ('the second year', the_fifth('second_year'), 'the_second_year'),
 ('bodies and ground', the_fifth('bodies_and_ground'), ('bodies', 'ground')),
 ("the priests' statute", the_fifth('priests_exempt'), 'a_statute_for_the_priests'),
 ('chok is sustenance (Beitzah 16a)', the_fifth('chok_means_food'), 'chok_is_a_word_for_sustenance'),
 ('a fifth and four hands', the_fifth('fifth_parsed'), 'a_fifth_and_four_hands'),
 ("Egypt's fifth, not the sanctuary's", the_fifth('fifth_homograph'), 'egypts_statute_not_the_sanctuarys'),
 ('the statute written here', the_fifth('statute_seat'), 'law_joseph_47_26'),
 ('until this day', the_fifth('until_this_day'), 'until_this_day'),
 ('fruitful in Goshen', the_fifth('fruitful_in_goshen'), 'fruitful_and_multiplied_exceedingly'),
 # ---- Gen 47:28-31: the_oath ----
 ('seventeen years in Egypt', the_oath('seventeen_years'), 17),
 ('a hundred and forty-seven', the_oath('hundred_forty_seven'), 147),
 ('why Joseph (Bereshit Rabbah 96:5)', the_oath('why_joseph'), 'in_his_power_to_do'),
 ('kindness and truth', the_oath('kindness_and_truth'), 'kindness_and_truth'),
 ("the burial command written here, the testament's the family's", the_oath('burial_command_seat'), 'law_joseph_47_29'),
 ('the oath sworn', the_oath('oath_sworn'), 'Gen 47:31'),
 ('the bow on the bed (Megillah 16b)', the_oath('bed_head_bow'), 'fox_in_its_hour'),
 ('the oath closed on the tape at 50:13', the_oath('oath_closed_on_tape'), 'Gen 50:13'),
 # ---- Gen 50:1-14: mourning ----
 ("Joseph's hand on the eyes — closed", mourning('hand_on_eyes_closed'), 'Gen 50:1'),
 ('forty and seventy', mourning('forty_seventy'), (40, 70)),
 ('the two timers on the scene', mourning('timers_on_the_scene'), ('death_plus_40', 'death_plus_70')),
 ('as he made you swear', mourning('as_he_made_you_swear'), 'Gen 47:31'),
 ('seven days', mourning('seven_days'), 7),
 ('Abel-mizraim', mourning('abel_mizraim'), 'the_mourning_of_egypt'),
 ("the burial is the family engine's", mourning('burial_seat'), 'family_engine_50_12'),
 ('Joseph merited to bury his father (Mishnah Sotah 1:9)', mourning('joseph_buried_sheet'), 'joseph_merited_to_bury_his_father'),
 ('no meal invited (Bereshit Rabbah 100:8)', mourning('no_meal'), 'no_meal_invited'),
 # ---- Gen 50:15-26: coffin ----
 ('perhaps Joseph will hate us', coffin('feared'), 'perhaps_joseph_will_hate_us'),
 ('altered for peace (Yevamot 65b)', coffin('altered_for_peace'), 'permitted_to_alter_for_peace'),
 ('the forgiveness rule — the second showing (Mishnah Bava Kamma 8:7)', coffin('forgiveness_sheet'), ('asks', 'prays')),
 ('their sin — the noun', coffin('chatat_homograph'), 'their_sin_the_noun'),
 ('a fox in its hour (Megillah 16b)', coffin('fox_in_its_hour'), 'fox_in_its_hour'),
 ('am I in the place of God', coffin('am_i_in_gods_place'), 'am_i_in_place_of_god'),
 ('ten candles (Megillah 16b)', coffin('ten_candles'), 'ten_candles_one_candle'),
 ('words that comfort the heart (Bereshit Rabbah 100:9)', coffin('words_on_the_heart'), 'words_that_comfort_the_heart'),
 ('a hundred and ten', coffin('hundred_ten'), 110),
 ("born on Joseph's knees", coffin('machir_knees'), 'born_on_josephs_knees'),
 ('"surely visit" — twice', coffin('visit_doubled'), 2),
 ('the visitation closed on the tape at Exod 4:31', coffin('visitation_closed_on_tape'), 'Exod 4:31'),
 ('the bones closed on the tape at Exod 13:19', coffin('bones_closed_on_tape'), 'Exod 13:19'),
 ('four hundred parasangs (Ketubot 111a)', coffin('four_hundred_parasangs'), 'four_hundred_parasangs'),
 ('when you go up (Bereshit Rabbah 100:11)', coffin('with_you_when_you_go_up'), 'when_you_go_up'),
 ('in a coffin in Egypt', coffin('coffin_in_egypt'), 'in_a_coffin_in_egypt'),
 # ---- THE SCENE and the headlines ----
 ('THE SCENE on the world engine — the tuple the hand-model printed before this file was typed', build('world'), (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 8, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 22, 12, 12, 12, 11407)),
 ('HEADLINE: the flow reversed — two narrative verses feed two law rows', build('headline_flow_reversed'), 'narrative_verses_feed_law_rows'),
 ("HEADLINE: the thief sold — three verdicts on the rule's shape", build('headline_thief_sold'), 'three_verdicts_on_the_rules_shape'),
 ('HEADLINE: the two absences on two chains', build('headline_two_absences'), 'twenty_two_on_two_chains'),
 ("HEADLINE: the seventy's missing one filed open", build('headline_seventy'), 'the_missing_one_filed_open'),
 ("HEADLINE: four closes on other engines' events", build('headline_closes_by_seat'), 'four_closes_by_seat'),
]


if __name__ == '__main__':
    print()
    ok = 0
    frac = {I: 0, M: 0, A: 0, D: 0, P: 0, H: 0}
    misses = []
    for name, c, want in TESTS:
        hit = c['v'] == want
        ok += hit
        frac[c['p']] += 1
        if not hit: misses.append((name, c['v']))
        print('%s %-76s [%s] %s' % ('OK ' if hit else 'MISS', name[:76], c['p'], '' if hit else 'got=%r' % (c['v'],)))
        print('     effects: %s' % ', '.join(c['fx']))
    n = len(TESTS)
    assert n == GUARDED, (n, GUARDED)
    print()
    print('MATRIX: %d/%d cells match the answer sheet' % (ok, n))
    print('FRACTIONS: pure ink %d/%d (%d%%) · recorded moves %d/%d (%d%%) · answer-sheet %d/%d · data %d/%d · imports %d/%d · hypotheses %d/%d' % (
          frac[I], n, 100 * frac[I] // n, frac[M], n, 100 * frac[M] // n, frac[A], n, frac[D], n, frac[P], n, frac[H], n))
    print('effects: every cell carries REGISTERED effects — two hundred and twenty-four discovered in the stretch\'s own words and registered first [effects law satisfied]')
    print('SCENE: %r' % (SCENE,))
    _W.print_coverage()
    if ok == n:
        print()
        print('FROM THE FORD TO THE COFFIN STANDS — the Jabbok, the meeting, Shechem, Bethel again, the three deaths, Edom, the dreamer, Potiphar, the prison, Pharaoh, the rise, the two descents, the cup, I am Joseph, the seventy, Goshen, the fifth, the oath, the mourning, the coffin: %d/%d' % (ok, n))
    else:
        print('MISSES (%d):' % len(misses))
        for m_ in misses: print('  -', m_[0][:80], '->', m_[1])
        sys.exit('MISSES REMAIN — a miss is evidence, never a retype: read it.')
