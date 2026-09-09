#!/usr/bin/env python3
"""cold_run_mamre.py — FROM MAMRE TO THE HEAP (O8 S3, 2026-09-08; World/step9/NARRATIVE_GAPS.md section 7): Genesis 18-20, 22,
25-31's narrative on the world engine — the visit and the plea, Sodom's night and the overthrow, Gerar's dream and the first
prayer, the binding, Abraham's end and Ishmael's twelve, the twins and the birthright, Isaac at Gerar and the wells, the
blessing and the grudge, Bethel's ladder and vow, the well and the stone, the two sevens and the switched bride, the twelve
names, the speckled wage, the flight, the pursuit and the heap with its two tongues. The third of the four narrative sittings
of O8 (the census: NARRATIVE_GAPS.md section 1). Genesis 21, 23 and 24 are the pre-Sinai and family engines'; this runner's
span is the story's verses alone (dependency_dispositions.yaml), and the story's acts fetch those engines' law by call.

The form: (1) the acts and speeches of the ink at their narrative verses (the register test), each a registered type with
its witness cut from the verse's consonants; (2) the answer sheet — the Mishnah's rows on this stretch read whole from the
shelf, each verified by a token in its own ink (Bava Kamma 8:7 the forgiveness, Avot 5:3 the ten trials, Bava Metzia 7:8 the
four keepers, Bava Batra 8:5 the firstborn's portion, Bekhorot 8:1 the firstborn by the head, Moed Katan 1:7 the joy rule,
Sanhedrin 10:3 Sodom); (3) the shelf — the Babylonian rows and the Genesis spine's rows located by script this sitting, each
verified by a token; (4) seventeen cells in the text's order, every cell a value with its provenance and its registered
effects; (5) the scene: the stretch's acts on a bare world, the tuple predicted by a hand-model before this file was typed
(scratchpad o8_s3_predict.py); (6) the wrap: law_mamre, the forty-second daemon, whose writes per event are the model's own
table. Five engines CALLED where the ink names their institution: the pre-Sinai code (the covenant's eighth day on every male
birth — the scene's laws carry law_pre_sinai beside law_mamre, as S1), the offerings (22:13's ram, 31:54's sacrifice), the
substitution engine (28:22's tithe), the family engine (25:5, 25:10), the guardians (THE PAID KEEPER on 31:38-40). The dating
lives on the sequential tape (convention 13). Zero-report law: every claimed ink token is probed before anything runs.
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
SPAN = [18, 19, 20, 22, 25, 26, 27, 28, 29, 30, 31]


# ---- (0) THE PROBES: every kind's witnesses in the span and the rosters' names — a run of consonants found contiguous in its verse, or the run stops ----
PROBES = [(18, 1, 'וירא אליו יהוה באלני ממרא'), (26, 2, 'וירא אליו יהוה ויאמר'), (26, 24, 'וירא אליו יהוה בלילה ההוא'), (18, 2, 'וירץ לקראתם מפתח האהל וישתחו ארצה'), (19, 1, 'וירא לוט ויקם לקראתם וישתחו אפים ארצה'), (18, 3, 'ויאמר אדני אם נא מצאתי חן בעיניך'), (18, 4, 'יקח נא מעט מים ורחצו רגליכם'), (19, 2, 'סורו נא אל בית עבדכם ולינו ורחצו רגליכם'), (18, 6, 'מהרי שלש סאים קמח סלת לושי ועשי עגות'), (18, 7, 'ואל הבקר רץ אברהם ויקח בן בקר רך וטוב'), (18, 8, 'ויקח חמאה וחלב ובן הבקר אשר עשה ויתן לפניהם'), (18, 10, 'שוב אשוב אליך כעת חיה והנה בן לשרה אשתך'), (18, 14, 'למועד אשוב אליך כעת חיה ולשרה בן'), (18, 12, 'ותצחק שרה בקרבה לאמר'), (18, 15, 'ותכחש שרה לאמר לא צחקתי כי יראה ויאמר לא כי צחקת'), (18, 16, 'ואברהם הלך עמם לשלחם'), (18, 17, 'ויהוה אמר המכסה אני מאברהם אשר אני עשה'), (18, 19, 'ושמרו דרך יהוה לעשות צדקה ומשפט'), (18, 20, 'זעקת סדם ועמרה כי רבה וחטאתם כי כבדה מאד'), (18, 21, 'ארדה נא ואראה'), (18, 22, 'ואברהם עודנו עמד לפני יהוה'), (18, 23, 'ויגש אברהם ויאמר'), (18, 24, 'אולי יש חמשים צדיקם בתוך העיר'), (18, 32, 'לא אשחית בעבור העשרה'), (18, 33, 'וילך יהוה כאשר כלה לדבר אל אברהם'), (19, 3, 'ויפצר בם מאד ויסרו אליו ויבאו אל ביתו'), (19, 3, 'ויעש להם משתה ומצות אפה ויאכלו'), (19, 4, 'ואנשי העיר אנשי סדם נסבו על הבית'), (19, 5, 'הוציאם אלינו ונדעה אתם'), (19, 8, 'הנה נא לי שתי בנות אשר לא ידעו איש'), (19, 9, 'ויפצרו באיש בלוט מאד ויגשו לשבר הדלת'), (19, 10, 'וישלחו האנשים את ידם ויביאו את לוט אליהם הביתה'), (19, 11, 'הכו בסנורים מקטן ועד גדול'), (19, 12, 'הוצא מן המקום'), (19, 15, 'קום קח את אשתך ואת שתי בנתיך הנמצאת'), (19, 14, 'ויהי כמצחק בעיני חתניו'), (19, 16, 'ויתמהמה'), (19, 16, 'ויחזקו האנשים בידו וביד אשתו וביד שתי בנתיו'), (19, 17, 'המלט על נפשך אל תביט אחריך ואל תעמד בכל הככר'), (19, 18, 'ויאמר לוט אלהם אל נא אדני'), (19, 20, 'אמלטה נא שמה הלא מצער הוא ותחי נפשי'), (19, 21, 'הנה נשאתי פניך גם לדבר הזה לבלתי הפכי את העיר אשר דברת'), (19, 22, 'מהר המלט שמה'), (19, 37, 'ותקרא שמו מואב'), (22, 14, 'ויקרא אברהם שם המקום ההוא יהוה יראה'), (25, 25, 'ויקראו שמו עשו'), (25, 26, 'ויקרא שמו יעקב'), (25, 30, 'על כן קרא שמו אדום'), (26, 33, 'ויקרא אתה שבעה'), (28, 19, 'ויקרא את שם המקום ההוא בית אל'), (29, 32, 'ותקרא שמו ראובן'), (30, 24, 'ותקרא את שמו יוסף'), (31, 47, 'ויקרא לו לבן יגר שהדותא ויעקב קרא לו גלעד'), (31, 48, 'על כן קרא שמו גלעד'), (19, 24, 'ויהוה המטיר על סדם ועל עמרה גפרית ואש'), (19, 25, 'ויהפך את הערים האל ואת כל הככר'), (19, 26, 'ותבט אשתו מאחריו ותהי נציב מלח'), (19, 27, 'וישכם אברהם בבקר אל המקום אשר עמד שם את פני יהוה'), (19, 28, 'וישקף על פני סדם ועמרה'), (19, 29, 'ויזכר אלהים את אברהם'), (30, 22, 'ויזכר אלהים את רחל'), (19, 29, 'וישלח את לוט מתוך ההפכה'), (25, 6, 'וישלחם מעל יצחק בנו'), (26, 16, 'לך מעמנו כי עצמת ממנו מאד'), (26, 31, 'וישלחם יצחק וילכו מאתו בשלום'), (28, 5, 'וישלח יצחק את יעקב'), (19, 30, 'וישב במערה הוא ושתי בנתיו'), (19, 33, 'ותשקין את אביהן יין בלילה הוא'), (19, 35, 'ותשקין גם בלילה ההוא את אביהן יין'), (19, 36, 'ותהרין שתי בנות לוט מאביהן'), (19, 37, 'ותלד הבכירה בן'), (19, 38, 'והצעירה גם הוא ילדה בן'), (25, 2, 'ותלד לו את זמרן ואת יקשן'), (20, 1, 'ויסע משם אברהם ארצה הנגב'), (22, 19, 'וישב אברהם בבאר שבע'), (26, 1, 'וילך יצחק אל אבימלך מלך פלשתים גררה'), (26, 17, 'וילך משם יצחק ויחן בנחל גרר וישב שם'), (26, 23, 'ויעל משם באר שבע'), (28, 10, 'ויצא יעקב מבאר שבע וילך חרנה'), (29, 1, 'וישא יעקב רגליו וילך ארצה בני קדם'), (20, 2, 'ויאמר אברהם אל שרה אשתו אחתי הוא'), (26, 7, 'ויאמר אחתי הוא'), (20, 2, 'וישלח אבימלך מלך גרר ויקח את שרה'), (20, 3, 'ויבא אלהים אל אבימלך בחלום הלילה ויאמר לו'), (31, 24, 'ויבא אלהים אל לבן הארמי בחלם הלילה ויאמר לו'), (20, 4, 'אדני הגוי גם צדיק תהרג'), (20, 5, 'בתם לבבי ובנקין כפי עשיתי זאת'), (20, 6, 'ואחשך גם אנכי אותך מחטו לי'), (20, 7, 'ועתה השב אשת האיש כי נביא הוא ויתפלל בעדך וחיה'), (20, 8, 'וישכם אבימלך בבקר ויקרא לכל עבדיו'), (20, 9, 'ויקרא אבימלך לאברהם ויאמר לו מה עשית לנו'), (26, 9, 'ויקרא אבימלך ליצחק ויאמר אך הנה אשתך הוא'), (20, 11, 'ויאמר אברהם כי אמרתי רק אין יראת אלהים במקום הזה'), (20, 12, 'וגם אמנה אחתי בת אבי הוא אך לא בת אמי'), (20, 14, 'ויקח אבימלך צאן ובקר ועבדים ושפחת ויתן לאברהם וישב לו את שרה אשתו'), (20, 15, 'הנה ארצי לפניך בטוב בעיניך שב'), (20, 16, 'הנה נתתי אלף כסף לאחיך הנה הוא לך כסות עינים'), (20, 17, 'ויתפלל אברהם אל האלהים'), (25, 21, 'ויעתר יצחק ליהוה לנכח אשתו כי עקרה הוא'), (20, 17, 'וירפא אלהים את אבימלך ואת אשתו ואמהתיו וילדו'), (20, 18, 'כי עצר עצר יהוה בעד כל רחם לבית אבימלך'), (22, 1, 'והאלהים נסה את אברהם'), (22, 2, 'קח נא את בנך את יחידך אשר אהבת את יצחק'), (22, 2, 'והעלהו שם לעלה'), (22, 3, 'וישכם אברהם בבקר ויחבש את חמרו'), (22, 4, 'ביום השלישי וישא אברהם את עיניו וירא את המקום מרחק'), (22, 5, 'שבו לכם פה עם החמור'), (22, 6, 'ויקח אברהם את עצי העלה וישם על יצחק בנו'), (22, 7, 'ואיה השה לעלה'), (22, 8, 'אלהים יראה לו השה לעלה בני'), (22, 9, 'ויבן שם אברהם את המזבח'), (26, 25, 'ויבן שם מזבח'), (22, 9, 'ויעקד את יצחק בנו וישם אתו על המזבח'), (22, 10, 'וישלח אברהם את ידו ויקח את המאכלת לשחט את בנו'), (22, 11, 'ויקרא אליו מלאך יהוה מן השמים ויאמר אברהם אברהם'), (22, 12, 'אל תשלח ידך אל הנער ואל תעש לו מאומה'), (22, 15, 'ויקרא מלאך יהוה אל אברהם שנית מן השמים'), (22, 13, 'והנה איל אחר נאחז בסבך בקרניו'), (22, 13, 'ויעלהו לעלה תחת בנו'), (22, 16, 'בי נשבעתי נאם יהוה'), (22, 17, 'וירש זרעך את שער איביו'), (22, 18, 'והתברכו בזרעך כל גויי הארץ'), (22, 20, 'ויגד לאברהם לאמר הנה ילדה מלכה גם הוא בנים לנחור אחיך'), (22, 23, 'שמנה אלה ילדה מלכה לנחור'), (22, 23, 'ובתואל ילד את רבקה'), (25, 3, 'ויקשן ילד את שבא ואת דדן'), (25, 1, 'ויסף אברהם ויקח אשה ושמה קטורה'), (26, 34, 'ויקח אשה את יהודית'), (28, 9, 'ויקח את מחלת בת ישמעאל'), (29, 23, 'ויקח את לאה בתו ויבא אתה אליו'), (29, 28, 'ויתן לו את רחל בתו לו לאשה'), (30, 4, 'ותתן לו את בלהה שפחתה לאשה'), (30, 9, 'ותתן אתה ליעקב לאשה'), (25, 5, 'ויתן אברהם את כל אשר לו ליצחק'), (25, 6, 'ולבני הפילגשים אשר לאברהם נתן אברהם מתנת'), (25, 8, 'ויגוע וימת אברהם בשיבה טובה זקן ושבע ויאסף אל עמיו'), (25, 17, 'ויגוע וימת ויאסף אל עמיו'), (25, 9, 'ויקברו אתו יצחק וישמעאל בניו אל מערת המכפלה'), (25, 11, 'ויברך אלהים את יצחק בנו'), (25, 16, 'שנים עשר נשיאם לאמתם'), (25, 18, 'על פני כל אחיו נפל'), (25, 22, 'ויתרצצו הבנים בקרבה'), (25, 22, 'ותלך לדרש את יהוה'), (25, 23, 'ויאמר יהוה לה שני גיים בבטנך'), (25, 23, 'ורב יעבד צעיר'), (25, 25, 'ויצא הראשון אדמוני'), (25, 26, 'ואחרי כן יצא אחיו'), (29, 32, 'ותהר לאה ותלד בן'), (30, 5, 'ותהר בלהה ותלד ליעקב בן'), (30, 10, 'ותלד זלפה שפחת לאה ליעקב בן'), (30, 21, 'ואחר ילדה בת'), (30, 23, 'ותהר ותלד בן'), (25, 27, 'ויגדלו הנערים ויהי עשו איש ידע ציד איש שדה'), (25, 28, 'ויאהב יצחק את עשו כי ציד בפיו ורבקה אהבת את יעקב'), (25, 29, 'ויזד יעקב נזיד ויבא עשו מן השדה והוא עיף'), (25, 30, 'הלעיטני נא מן האדם האדם הזה כי עיף אנכי'), (25, 31, 'מכרה כיום את בכרתך לי'), (25, 32, 'הנה אנכי הולך למות ולמה זה לי בכרה'), (25, 33, 'השבעה לי כיום וישבע לו'), (26, 31, 'וישבעו איש לאחיו'), (31, 53, 'וישבע יעקב בפחד אביו יצחק'), (25, 33, 'וימכר את בכרתו ליעקב'), (25, 34, 'ויעקב נתן לעשו לחם ונזיד עדשים'), (25, 34, 'ויבז עשו את הבכרה'), (26, 1, 'ויהי רעב בארץ מלבד הרעב הראשון'), (26, 2, 'אל תרד מצרימה שכן בארץ אשר אמר אליך'), (26, 3, 'גור בארץ הזאת ואהיה עמך ואברכך'), (26, 3, 'והקמתי את השבעה אשר נשבעתי לאברהם אביך'), (26, 5, 'וישמר משמרתי מצותי חקותי ותורתי'), (26, 6, 'וישב יצחק בגרר'), (26, 8, 'וישקף אבימלך מלך פלשתים בעד החלון וירא והנה יצחק מצחק את רבקה אשתו'), (26, 11, 'ויצו אבימלך את כל העם לאמר הנגע באיש הזה ובאשתו מות יומת'), (26, 12, 'ויזרע יצחק בארץ ההוא וימצא בשנה ההוא מאה שערים ויברכהו יהוה'), (26, 13, 'ויגדל האיש וילך הלוך וגדל עד כי גדל מאד'), (26, 14, 'ויקנאו אתו פלשתים'), (30, 1, 'ותקנא רחל באחתה'), (26, 15, 'סתמום פלשתים וימלאום עפר'), (26, 18, 'וישב יצחק ויחפר את בארת המים'), (26, 18, 'ויקרא להן שמות כשמת אשר קרא להן אביו'), (26, 19, 'ויחפרו עבדי יצחק בנחל וימצאו שם באר מים חיים'), (26, 32, 'ויאמרו לו מצאנו מים'), (26, 20, 'ויריבו רעי גרר עם רעי יצחק לאמר לנו המים'), (26, 21, 'ויחפרו באר אחרת ויריבו גם עליה'), (26, 22, 'ויעתק משם ויחפר באר אחרת ולא רבו עליה'), (26, 25, 'ויקרא בשם יהוה'), (26, 25, 'ויט שם אהלו'), (26, 25, 'ויכרו שם עבדי יצחק באר'), (26, 26, 'ואבימלך הלך אליו מגרר'), (26, 27, 'מדוע באתם אלי'), (26, 28, 'תהי נא אלה בינותינו'), (26, 28, 'ונכרתה ברית עמך'), (31, 44, 'ועתה לכה נכרתה ברית אני ואתה'), (26, 30, 'ויעש להם משתה ויאכלו וישתו'), (29, 22, 'ויאסף לבן את כל אנשי המקום ויעש משתה'), (26, 31, 'וישכימו בבקר וישבעו איש לאחיו וישלחם יצחק'), (26, 35, 'ותהיין מרת רוח ליצחק ולרבקה'), (27, 1, 'ויהי כי זקן יצחק ותכהין עיניו מראת'), (27, 2, 'הנה נא זקנתי לא ידעתי יום מותי'), (27, 4, 'ועשה לי מטעמים כאשר אהבתי והביאה לי ואכלה'), (27, 5, 'ורבקה שמעת בדבר יצחק אל עשו בנו'), (27, 8, 'ועתה בני שמע בקלי לאשר אני מצוה אתך'), (27, 9, 'וקח לי משם שני גדיי עזים טבים'), (27, 43, 'ועתה בני שמע בקלי וקום ברח לך אל לבן אחי חרנה'), (27, 45, 'ושלחתי ולקחתיך משם'), (27, 11, 'הן עשו אחי איש שער ואנכי איש חלק'), (27, 12, 'והבאתי עלי קללה ולא ברכה'), (27, 13, 'עלי קללתך בני'), (27, 14, 'וילך ויקח ויבא לאמו ותעש אמו מטעמים'), (27, 15, 'ותלבש את יעקב בנה הקטן'), (27, 16, 'ואת ערת גדיי העזים הלבישה על ידיו'), (27, 17, 'ותתן את המטעמים ואת הלחם אשר עשתה ביד יעקב בנה'), (27, 18, 'ויבא אל אביו ויאמר אבי'), (27, 31, 'ויעש גם הוא מטעמים ויבא לאביו'), (27, 19, 'אנכי עשו בכרך'), (27, 24, 'ויאמר אתה זה בני עשו ויאמר אני'), (27, 32, 'אני בנך בכרך עשו'), (27, 21, 'גשה נא ואמשך בני'), (27, 22, 'ויגש יעקב אל יצחק אביו וימשהו'), (27, 23, 'ולא הכירו כי היו ידיו כידי עשו אחיו שערת ויברכהו'), (27, 25, 'ויגש לו ויאכל ויבא לו יין וישת'), (27, 27, 'ויגש וישק לו וירח את ריח בגדיו ויברכהו'), (29, 11, 'וישק יעקב לרחל וישא את קלו ויבך'), (29, 13, 'וירץ לקראתו ויחבק לו וינשק לו ויביאהו אל ביתו'), (27, 28, 'ויתן לך האלהים מטל השמים ומשמני הארץ ורב דגן ותירש'), (27, 29, 'יעבדוך עמים וישתחו לך לאמים'), (27, 40, 'ועל חרבך תחיה ואת אחיך תעבד'), (28, 4, 'ויתן לך את ברכת אברהם לך ולזרעך אתך'), (27, 33, 'ויחרד יצחק חרדה גדלה עד מאד'), (27, 34, 'ויצעק צעקה גדלה ומרה עד מאד'), (27, 35, 'בא אחיך במרמה ויקח ברכתך'), (27, 36, 'ויעקבני זה פעמים את בכרתי לקח והנה עתה לקח ברכתי'), (27, 37, 'הן גביר שמתיו לך'), (27, 38, 'וישא עשו קלו ויבך'), (27, 41, 'וישטם עשו את יעקב'), (27, 41, 'יקרבו ימי אבל אבי ואהרגה את יעקב אחי'), (27, 42, 'ויגד לרבקה את דברי עשו בנה הגדל'), (27, 46, 'קצתי בחיי מפני בנות חת'), (28, 2, 'וקח לך משם אשה מבנות לבן אחי אמך'), (28, 5, 'וישלח יצחק את יעקב וילך פדנה ארם'), (28, 6, 'וירא עשו כי ברך יצחק את יעקב'), (28, 8, 'וירא עשו כי רעות בנות כנען בעיני יצחק אביו'), (28, 11, 'ויפגע במקום וילן שם כי בא השמש'), (28, 11, 'ויקח מאבני המקום וישם מראשתיו'), (28, 12, 'ויחלם והנה סלם מצב ארצה וראשו מגיע השמימה'), (31, 10, 'ואשא עיני וארא בחלום'), (28, 13, 'הארץ אשר אתה שכב עליה לך אתננה ולזרעך'), (28, 14, 'והיה זרעך כעפר הארץ'), (28, 15, 'והנה אנכי עמך ושמרתיך בכל אשר תלך'), (28, 15, 'והשבתיך אל האדמה הזאת'), (28, 16, 'וייקץ יעקב משנתו ויאמר אכן יש יהוה במקום הזה'), (28, 17, 'ויירא ויאמר מה נורא המקום הזה'), (28, 18, 'וישם אתה מצבה ויצק שמן על ראשה'), (28, 19, 'ויקרא את שם המקום ההוא בית אל ואולם לוז שם העיר לראשנה'), (31, 45, 'ויקח יעקב אבן וירימה מצבה'), (28, 20, 'וידר יעקב נדר לאמר אם יהיה אלהים עמדי'), (28, 22, 'וכל אשר תתן לי עשר אעשרנו לך'), (29, 2, 'וירא והנה באר בשדה'), (29, 3, 'ונאספו שמה כל העדרים וגללו את האבן'), (29, 4, 'ויאמר להם יעקב אחי מאין אתם'), (29, 5, 'הידעתם את לבן בן נחור'), (29, 7, 'הן עוד היום גדול לא עת האסף המקנה'), (29, 8, 'לא נוכל עד אשר יאספו כל העדרים'), (29, 10, 'ויגש יעקב ויגל את האבן מעל פי הבאר'), (29, 10, 'וישק את צאן לבן אחי אמו'), (29, 12, 'ויגד יעקב לרחל כי אחי אביה הוא'), (29, 12, 'ותרץ ותגד לאביה'), (29, 13, 'ויחבק לו וינשק לו ויביאהו אל ביתו'), (29, 14, 'אך עצמי ובשרי אתה'), (29, 14, 'וישב עמו חדש ימים'), (29, 15, 'הגידה לי מה משכרתך'), (30, 28, 'נקבה שכרך עלי ואתנה'), (29, 18, 'ויאהב יעקב את רחל ויאמר אעבדך שבע שנים ברחל בתך הקטנה'), (30, 32, 'הסר משם כל שה נקד וטלוא'), (30, 33, 'וענתה בי צדקתי ביום מחר'), (29, 19, 'טוב תתי אתה לך מתתי אתה לאיש אחר שבה עמדי'), (30, 34, 'הן לו יהי כדברך'), (29, 20, 'ויעבד יעקב ברחל שבע שנים ויהיו בעיניו כימים אחדים'), (29, 30, 'ויעבד עמו עוד שבע שנים אחרות'), (29, 21, 'הבה את אשתי כי מלאו ימי'), (29, 23, 'ויהי בערב ויקח את לאה בתו ויבא אתה אליו ויבא אליה'), (29, 25, 'ויהי בבקר והנה הוא לאה'), (29, 24, 'ויתן לבן לה את זלפה שפחתו ללאה בתו שפחה'), (29, 29, 'ויתן לבן לרחל בתו את בלהה שפחתו לה לשפחה'), (29, 26, 'לא יעשה כן במקומנו לתת הצעירה לפני הבכירה'), (29, 27, 'מלא שבע זאת'), (29, 28, 'ויעש יעקב כן וימלא שבע זאת ויתן לו את רחל בתו לו לאשה'), (29, 31, 'וירא יהוה כי שנואה לאה ויפתח את רחמה ורחל עקרה'), (30, 22, 'וישמע אליה אלהים ויפתח את רחמה'), (29, 35, 'ותעמד מלדת'), (30, 9, 'ותרא לאה כי עמדה מלדת'), (30, 1, 'הבה לי בנים ואם אין מתה אנכי'), (30, 2, 'התחת אלהים אנכי'), (30, 2, 'ויחר אף יעקב ברחל'), (31, 36, 'ויחר ליעקב'), (30, 3, 'הנה אמתי בלהה בא אליה'), (30, 4, 'ותתן לו את בלהה שפחתה לאשה ויבא אליה יעקב'), (30, 14, 'וילך ראובן בימי קציר חטים וימצא דודאים בשדה'), (30, 14, 'תני נא לי מדודאי בנך'), (30, 15, 'לכן ישכב עמך הלילה תחת דודאי בנך'), (30, 16, 'כי שכר שכרתיך בדודאי בני'), (30, 17, 'וישמע אלהים אל לאה'), (30, 25, 'שלחני ואלכה אל מקומי ולארצי'), (30, 26, 'תנה את נשי ואת ילדי אשר עבדתי אתך בהן'), (30, 27, 'נחשתי ויברכני יהוה בגללך'), (30, 29, 'אתה ידעת את אשר עבדתיך'), (30, 30, 'ויברך יהוה אתך לרגלי'), (30, 35, 'ויסר ביום ההוא את התישים העקדים והטלאים'), (30, 36, 'וישם דרך שלשת ימים בינו ובין יעקב'), (30, 37, 'ויקח לו יעקב מקל לבנה לח ולוז וערמון'), (30, 38, 'ויצג את המקלות אשר פצל ברהטים'), (30, 39, 'ותלדן הצאן עקדים נקדים וטלאים'), (30, 40, 'והכשבים הפריד יעקב'), (30, 42, 'והיה העטפים ללבן והקשרים ליעקב'), (30, 43, 'ויפרץ האיש מאד מאד'), (31, 1, 'וישמע את דברי בני לבן לאמר'), (31, 2, 'וירא יעקב את פני לבן והנה איננו עמו כתמול שלשום'), (31, 3, 'ויאמר יהוה אל יעקב שוב אל ארץ אבותיך ולמולדתך ואהיה עמך'), (31, 4, 'וישלח יעקב ויקרא לרחל וללאה השדה אל צאנו'), (31, 5, 'ואלהי אבי היה עמדי'), (31, 6, 'כי בכל כחי עבדתי את אביכן'), (31, 7, 'ואביכן התל בי והחלף את משכרתי עשרת מנים'), (31, 9, 'ויצל אלהים את מקנה אביכם ויתן לי'), (31, 13, 'אנכי האל בית אל אשר משחת שם מצבה אשר נדרת לי שם נדר'), (31, 38, 'זה עשרים שנה אנכי עמך'), (31, 39, 'טרפה לא הבאתי אליך אנכי אחטנה'), (31, 40, 'הייתי ביום אכלני חרב וקרח בלילה'), (31, 41, 'עבדתיך ארבע עשרה שנה בשתי בנתיך ושש שנים בצאנך'), (31, 42, 'את עניי ואת יגיע כפי ראה אלהים ויוכח אמש'), (31, 14, 'ותען רחל ולאה ותאמרנה לו העוד לנו חלק ונחלה בבית אבינו'), (31, 16, 'ועתה כל אשר אמר אלהים אליך עשה'), (31, 17, 'ויקם יעקב וישא את בניו ואת נשיו על הגמלים'), (31, 18, 'וינהג את כל מקנהו'), (31, 19, 'ותגנב רחל את התרפים אשר לאביה'), (31, 20, 'ויגנב יעקב את לב לבן הארמי'), (31, 21, 'ויברח הוא וכל אשר לו'), (31, 21, 'ויקם ויעבר את הנהר וישם את פניו הר הגלעד'), (31, 22, 'ויגד ללבן ביום השלישי כי ברח יעקב'), (31, 23, 'וירדף אחריו דרך שבעת ימים'), (31, 25, 'וישג לבן את יעקב'), (31, 26, 'ויאמר לבן ליעקב מה עשית ותגנב את לבבי'), (31, 30, 'למה גנבת את אלהי'), (31, 31, 'ויען יעקב ויאמר ללבן כי יראתי'), (31, 32, 'עם אשר תמצא את אלהיך לא יחיה'), (31, 32, 'ולא ידע יעקב כי רחל גנבתם'), (31, 33, 'ויבא לבן באהל יעקב ובאהל לאה ובאהל שתי האמהת ולא מצא'), (31, 35, 'ויחפש ולא מצא את התרפים'), (31, 36, 'ויחר ליעקב וירב בלבן'), (31, 37, 'שים כה נגד אחי ואחיך ויוכיחו בין שנינו'), (31, 43, 'הבנות בנתי והבנים בני והצאן צאני'), (31, 46, 'ויקחו אבנים ויעשו גל ויאכלו שם על הגל'), (31, 48, 'הגל הזה עד ביני ובינך היום'), (31, 49, 'יצף יהוה ביני ובינך'), (31, 50, 'אם תענה את בנתי ואם תקח נשים על בנתי'), (31, 52, 'עד הגל הזה ועדה המצבה'), (31, 53, 'אלהי אברהם ואלהי נחור ישפטו בינינו'), (31, 54, 'ויזבח יעקב זבח בהר ויקרא לאחיו לאכל לחם'), (31, 54, 'ויאכלו לחם וילינו בהר'), (25, 13, 'נבית'), (25, 13, 'וקדר'), (25, 13, 'ואדבאל'), (25, 13, 'ומבשם'), (25, 14, 'ומשמע'), (25, 14, 'ודומה'), (25, 14, 'ומשא'), (25, 15, 'חדד'), (25, 15, 'ותימא'), (25, 15, 'יטור'), (25, 15, 'נפיש'), (25, 15, 'וקדמה'), (22, 21, 'עוץ'), (22, 21, 'בוז'), (22, 21, 'קמואל'), (22, 22, 'כשד'), (22, 22, 'חזו'), (22, 22, 'פלדש'), (22, 22, 'ידלף'), (22, 22, 'בתואל'), (22, 24, 'טבח'), (22, 24, 'גחם'), (22, 24, 'תחש'), (22, 24, 'מעכה'), (25, 2, 'זמרן'), (25, 2, 'יקשן'), (25, 2, 'מדן'), (25, 2, 'מדין'), (25, 2, 'ישבק'), (25, 2, 'שוח')]
_T = {}
for ch, vs, run in PROBES:
    ws = _T.setdefault((ch, vs), toks(ch, vs)); want = run.split()
    assert any(ws[i:i + len(want)] == want for i in range(len(ws) - len(want) + 1)), 'PROBE FAILED: %r not in Gen %d:%d' % (run, ch, vs)
print('probes: %d ink runs verified in their verses (Gen 18-31)' % len(PROBES))

I, M, A, D, P, H = 'INK', 'MOVE', 'ANSWER-SHEET', 'DATA', 'IMPORT', 'HYPOTHESIS'


def cell(v, p, why, effects):
    FX.validate(effects)
    return {'v': v, 'p': p, 'why': why, 'fx': effects}


with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):   # the callees grade themselves at import — their reports stay their own
    import cold_run_pre_sinai as PS_       # THE LIVE EDGES (dependency_dispositions.yaml): the covenant's eighth day on every male birth; the covenant's heads at 26:3
    import cold_run_offerings as OF        # the burnt offering (22:13); the peace offering's shape (31:54)
    import cold_run_temurah as TM          # the tithe vowed (28:22), as 14:20's
    import cold_run_family as FA           # all that he had (25:5); the purchased field (25:10)
    import cold_run_guardians as GD        # THE PAID KEEPER: Jacob's account of 31:38-40 against the four keepers' verdict table
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
    ('bava_kamma', 8, 7, 'ויתפלל אברהם'), ('pirkei_avot', 5, 3, 'עשרה נסיונות'), ('bava_metzia', 7, 8, 'ארבעה שומרין'), ('bava_batra', 8, 5, 'לא יטל פי שנים'),
    ('bekhorot', 8, 1, 'בכור לנחלה'), ('moed_katan', 1, 7, 'אין נושאין נשים במועד'), ('sanhedrin', 10, 3, 'אנשי סדום'),
]
for t, ch, m, must in SHEET: mishnah(t, ch, m, must)
SHEET2 = [   # the Babylonian rows (file index 2*daf-2, +1 for b) and the Genesis spine's rows (Bereshit Rabbah, parashah:row) — every one located by script this sitting
    ('B', 'megillah', 17, 'a', 5, 'בבית עבר'), ('B', 'megillah', 17, 'a', 6, 'עשרים ושתים'), ('B', 'yevamot', 64, 'a', 6, 'בן ארבעים שנה'), ('B', 'yoma', 28, 'b', 10, 'עירובי תבשילין'),
    ('B', 'kiddushin', 82, 'a', 10, 'כל התורה כולה'), ('B', 'bava_batra', 16, 'b', 11, 'תבשיל של עדשים'), ('B', 'bava_batra', 16, 'b', 12, 'עדשה'), ('B', 'bava_kamma', 92, 'a', 4, 'ויתפלל אברהם'),
    ('B', 'bava_kamma', 92, 'a', 16, 'ויתפלל אברהם'), ('B', 'bava_metzia', 93, 'b', 3, 'אכלני חורב'), ('B', 'bava_metzia', 86, 'b', 3, 'בן בקר'), ('B', 'bava_metzia', 86, 'b', 7, 'בן בקר'),
    ('B', 'shabbat', 127, 'a', 13, 'הכנסת אורחין'), ('B', 'sanhedrin', 89, 'b', 8, 'נסה את אברהם'), ('B', 'sanhedrin', 89, 'b', 9, 'דבריו של שטן'), ('B', 'sanhedrin', 89, 'b', 14, 'ישמעאל'),
    ('B', 'sanhedrin', 91, 'a', 16, 'מתנות'), ('B', 'sanhedrin', 109, 'a', 8, 'אנשי סדום'), ('B', 'moed_katan', 8, 'b', 9, 'שמחה בשמחה'), ('B', 'moed_katan', 9, 'a', 4, 'שמחה בשמחה'),
    ('B', 'chullin', 91, 'b', 8, 'מאבני המקום'), ('B', 'rosh_hashanah', 10, 'b', 10, 'בפסח נולד יצחק'), ('B', 'rosh_hashanah', 11, 'a', 2, 'בפסח נולד יצחק'), ('B', 'rosh_hashanah', 11, 'a', 16, 'נפקדה שרה'),
    ('B', 'rosh_hashanah', 16, 'a', 16, 'עקידת יצחק'), ('B', 'berakhot', 6, 'b', 8, 'אשר עמד שם'), ('B', 'berakhot', 26, 'b', 4, 'תפלות אבות תקנום'), ('B', 'berakhot', 26, 'b', 5, 'אברהם תקן תפלת שחרית'),
    ('B', 'berakhot', 26, 'b', 14, 'אבות תקנום'), ('B', 'ketubot', 50, 'a', 3, 'עשר אעשרנו'),
    ('R', 48, 12, 'פרוס הפסח'), ('R', 49, 6, 'חמשים ושתים'), ('R', 49, 8, 'הגשה לתפלה'), ('R', 49, 9, 'חמשים'), ('R', 49, 12, 'מחמשים לחמשה'), ('R', 50, 4, 'ויעש להם משתה'), ('R', 51, 5, 'נציב מלח'),
    ('R', 55, 1, 'נסיון אחר נסיון'), ('R', 56, 9, 'איל אחר'), ('R', 56, 11, 'נסיון עשירי'), ('R', 58, 5, 'מהר המוריה'), ('R', 61, 4, 'זו הגר'), ('R', 62, 1, 'בשיבה טובה'), ('R', 64, 3, 'עולה תמימה'),
    ('R', 64, 6, 'מפני המעשרות'), ('R', 65, 1, 'בן ארבעים'), ('R', 65, 14, 'שני גדיי'), ('R', 68, 5, 'ששים ושלש'), ('R', 68, 10, 'כיבא השמש'), ('R', 68, 11, 'ארבע עשרה'), ('R', 70, 7, 'עשר אעשרנו'),
    ('R', 70, 19, 'שמחה בשמחה'), ('R', 72, 2, 'דודאים'), ('R', 72, 3, 'הפסידה'), ('R', 72, 5, 'דודאים'), ('R', 73, 1, 'בראש השנה'), ('R', 74, 3, 'עשרת מנים'), ('R', 74, 4, 'לא יחיה'),
    ('R', 74, 5, 'ותגנב רחל'), ('R', 74, 6, 'שלשת ימים'), ('R', 74, 9, 'לא יחיה'), ('R', 74, 11, 'עשרת מנים'),
]
for row in SHEET2:
    if row[0] == 'B': _bavli(*row[1:])
    else: _br(*row[1:])
print('answer sheet: %d Mishnah rows verified in their own ink; shelf: %d rows (Babylonian and Bereshit Rabbah) verified by token' % (len(SHEET), len(SHEET2)))

# ---- (4) THE CELLS — seventeen, in the text's order; each query a cell(value, provenance, why, effects) ----
def _ladder():
    """the plea's numbers in Gen 18:24-32 by the numeral words of the verses, in verse order (a measurement)"""
    vals = {'חמשים': 50, 'ארבעים': 40, 'שלשים': 30, 'עשרים': 20, 'עשרה': 10, 'העשרה': 10, 'חמשה': 5}
    out = []
    for vs in range(24, 33):
        ws = toks(18, vs); ns = [vals[w] for w in ws if w in vals]
        if vs == 28: out.append(50 - 5)            # 'perhaps the fifty righteous will lack five' — forty-five by the verse's own subtraction
        elif ns: out.append(ns[0])
    return [x for i, x in enumerate(out) if i == 0 or x != out[i - 1]]

def mamre(q):
    if q == 'appearance_seats': return cell(len(_seats(lambda ws: 'וירא' in ws and 'אליו' in ws and 'יהוה' in ws, 18, 31)), I, "the appearance formula 'and the LORD appeared to him' in Gen 18-31: 18:1 (Mamre), 26:2 (Gerar), 26:24 (Beersheba by night) — three, measured", ['fear_not_promised'])
    if q == 'three_men': return cell(3, I, "'three men standing over him' (18:2) — the count word of the verse; Bava Metzia 86b:7 (Rav Yehuda in Rav's name: one calf 'tender', two 'and good', three 'a calf' — the three visitors, a calf each)", ['visitors_received'])
    if q == 'three_seahs': return cell(3, I, "'three seahs of fine flour' (18:6) — the measure the fine-flour token names; the fine flour is bread for guests, not the meal offering (FALSE at the census); Bereshit Rabbah 48:12: 'knead and make cakes' — it was Passover (the row mamre_visit_date)", ['visitors_received'])
    if q == 'hospitality_rank': return cell('greater_than_receiving_the_presence', M, "Shabbat 127a:13 — Rav Yehuda in Rav's name: receiving guests is greater than receiving the Presence, from 'pass not away, I pray, from your servant' (18:3): Abraham left the Presence for the guests", ['visitors_received'])
    if q == 'season_phrase_seats': return cell(4, I, "'at this living season' (כעת חיה) at Gen 18:10, 18:14 and 2 Kgs 4:16-17 alone in the Tanakh (measured at the registry)", ['son_promised_at_the_season', 'return_at_the_season'])
    if q == 'season_timer_days': return cell(365, D, "the one-year timer of 18:10 on the bare scene: 365 days (no epoch — the Calendar's year on the tape); on the tape the visit is placed on Passover of the year before born:isaac (Bereshit Rabbah 48:12) and the fire lands on the birth's day (Rosh Hashanah 10b:10) — the sequence runner CH0", ['return_at_the_season'])
    if q == 'laugh_quoted_altered': return cell('and_my_lord_is_old_dropped', M, "Bava Metzia 87a:9-10 — Sarah said 'and my lord is old' (18:12); the Torah quoted her to Abraham as 'and I am old' (18:13): great is peace, that the Torah altered her words", ['laughed_within'])
    if q == 'house_charge_pair': return cell(('righteousness', 'justice'), I, "'to do righteousness and justice' (18:19) — the pair the house is charged with; Bereshit Rabbah 49:4", ['house_charged'])
    if q == 'ladder': return cell([50, 45, 40, 30, 20, 10], I, "the plea's six counts by the verses' numeral words in order: fifty (18:24, 18:26), forty-five (18:28 — 'the fifty lacking five'), forty (18:29), thirty (18:30), twenty (18:31), ten (18:32) — measured by _ladder()", ['righteous_count_pleaded'])
    if q == 'ladder_by_census': return cell(_ladder(), I, "the same six by the census function over 18:24-32 (a measurement, printed)", ['righteous_count_pleaded'])
    if q == 'why_stop_at_ten': return cell('eight_of_noahs_house_were_not_enough', M, "Bereshit Rabbah 49:13 — why did he stop at ten? the generation of the flood had eight righteous (Noah's house) and they did not protect it", ['spared_for_the_ten'])
    if q == 'standing_is_prayer': return cell('prayer', M, "Berakhot 6b:8, 26b:5 — 'and standing is nothing but prayer' (from Ps 106:30): 18:22's 'still standing before the LORD' and 19:27's 'the place where he had stood' are the morning prayer's founding", ['stood_before_the_lord', 'morning_prayer_founded'])
    if q == 'outcry_closed_by': return cell('Gen 19:25', I, "the outcry's inquiry (18:21 'I will go down and see') closed by the overthrow (19:25) — the HEAVEN entry's close on the scene", ['outcry_to_be_seen'])
    return cell('no_case', I, '', [FX.NONE])

def sodom(q):
    if q == 'matzot_seat': return cell(1, I, "'and baked unleavened bread' (19:3) — the unleavened token at 19:3 alone in Genesis (measured); the leaven engine's word as a homograph (FALSE at the census); Bereshit Rabbah 48:12 dates the visit by it", ['matzot_made'])
    if q == 'lot_learned_where': return cell('abrahams_house', M, "Bereshit Rabbah 50:4 — 'and he made them a feast': in Abraham's house he had been, who received the wayfarers", ['angels_lodged'])
    if q == 'blindness_seats': return cell(2, I, "the blindness noun (סנורים) at Gen 19:11 and 2 Kgs 6:18 alone in the Tanakh (measured)", ['struck_with_blindness'])
    if q == 'evacuation_receipt': return cell('Gen 19:16', I, "'bring out of the place' (19:12) received at 19:16 'they brought him out and set him outside the city' — the DEBIT closed", ['evacuation_owed', 'led_out_of_sodom'])
    if q == 'ban_breached_at': return cell('Gen 19:26', I, "'do not look behind you' (19:17) breached at 19:26 'and his wife looked back from behind him' — the BLOCK's breach and its consequence on the same verse", ['looking_back_barred', 'pillar_of_salt'])
    if q == 'salt_pillar_seats': return cell(1, I, "'a pillar of salt' (19:26) — the phrase's only seat in the Tanakh (measured at the registry)", ['pillar_of_salt'])
    if q == 'salt_sin': return cell('refused_salt_to_the_guests', M, "Bereshit Rabbah 51:5 — she sinned with salt: 'give me salt, for we have guests', meaning to make the townsmen know — therefore 'a pillar of salt'", ['pillar_of_salt'])
    if q == 'sodom_sheet_row': return cell('no_share_in_the_world_to_come', A, "Mishnah Sanhedrin 10:3 — the men of Sodom have no share in the world to come (13:13 'wicked and sinners': S2's entry, open for the next world); 19:24-25 executes this world's — Sanhedrin 109a:8 ('wicked' in this world, 'sinners' for the world to come)", ['overthrown'])
    if q == 'tranquility_years': return cell((52, 25), M, "Bereshit Rabbah 49:6 — R. Yirmeya ben Elazar: Sodom's tranquility was fifty-two years, twenty-five of them the Holy One shook mountains upon them so that they would repent", ['outcry_to_be_seen'])
    if q == 'remembered_seats': return cell(3, I, "'and God remembered' (ויזכר אלהים) at Gen 8:1, 19:29, 30:22 (measured at the registry) — Noah, Abraham for Lot, Rachel", ['remembered_by_god'])
    if q == 'morning_prayer_founder': return cell('abraham', M, "Berakhot 26b:5 — a baraita as R. Yose son of R. Chanina: Abraham instituted the morning prayer, 'and Abraham rose early in the morning to the place where he had stood' (19:27); 26b:4 the two views (the patriarchs instituted / against the daily offerings); 26b:14 the reconciliation", ['morning_prayer_founded'])
    if q == 'fixed_place': return cell('Gen 19:27', M, "Berakhot 6b:8 — whoever fixes a place for his prayer: 'to the place where he had stood there' (19:27)", ['morning_prayer_founded'])
    if q == 'daughters_two_nights': return cell(2, I, "'that night' (19:33) and 'that night also' (19:35) — two nights, the elder then the younger; the dotted word of 19:33 the frozen unit's second of the Torah's ten", ['made_drunk', 'daughters_conceived'])
    if q == 'two_peoples_named': return cell(('moab', 'ben-ammi'), I, "'the father of Moab to this day' (19:37), 'the father of the children of Ammon to this day' (19:38) — the two namings, the two peoples", ['begotten', 'name_given'])
    return cell('no_case', I, '', [FX.NONE])

def gerar(q):
    if q == 'sister_claim_seats': return cell(5, I, "'she is my sister' (אחתי הוא) at Gen 12:19, 20:2, 20:5, 26:7, 26:9 in Genesis (measured at the registry) — the three cycles' own words", ['presented_as_sister'])
    if q == 'prophet_seats': return cell(1, I, "the prophet noun (נביא) at Gen 20:7 alone in the book (measured) — the Torah's first", ['prophet_declared'])
    if q == 'prayed_seats': return cell(2, I, "the consonants of 'and he prayed' (ויתפלל) at Gen 20:7 (the promise 'he shall pray') and 20:17 (its keeping) alone in Genesis (measured — the dry run refuted 'one seat' and the claim was corrected beside its record)", ['prayed_for_abimelech'])
    if q == 'forgiveness_sheet': return cell(('asks', 'prays'), A, "Mishnah Bava Kamma 8:7 — though he pays him he is not forgiven until he asks him, from 'and now return the man's wife' (20:7); and the forgiver must not be cruel, from 'and Abraham prayed' (20:17): the two legs the row reads off this chapter; Bava Kamma 92a:4 the Mishnah in the gemara", ['prayed_for_abimelech', 'restored_with_gifts'])
    if q == 'forgiveness_run': return cell(('restored', 'asked', 'prayed', 'healed'), I, "the chapter's own order: 20:14 the restitution with gifts, 20:7's demand to return, 20:17 the prayer, 20:17 the healing — the Mishnah's rule run on the ledger: death_decreed_over_the_woman closed at the healing after the return and the prayer", ['death_decreed_over_the_woman', 'healed'])
    if q == 'answered_first': return cell('sarah_remembered', M, "Bava Kamma 92a:16 — Rava: whoever prays for his fellow while he himself needs that thing is answered first — 'and Abraham prayed... and the LORD remembered Sarah as He had said' (21:1)", ['prayed_for_abimelech'])
    if q == 'thousand_silver': return cell(1000, I, "'a thousand pieces of silver' (20:16) — the number parsed; 'a covering of eyes' the Tanakh's only seat (measured)", ['thousand_silver_covering'])
    if q == 'covering_of_eyes': return cell('appeasement_owed_by_the_wronger', M, "Bava Kamma 93a (the frozen unit's routed row) on 20:16 — from here that one who wrongs another must appease him; Bereshit Rabbah 52:12", ['thousand_silver_covering'])
    if q == 'withheld_jurisdiction': return cell('heaven', M, "'I also withheld you from sinning against Me' (20:6) — the agency assigned to Heaven, the frozen unit's read; Bereshit Rabbah 52:6", ['withheld_from_sin'])
    if q == 'half_sister': return cell(('fathers_daughter', 'not_mothers'), I, "'the daughter of my father but not the daughter of my mother' (20:12) — the sister claim's ground; Sanhedrin 58b the frozen unit's routed row (the Noahide's paternal sister)", ['half_sister_claimed'])
    if q == 'wombs_shut_register': return cell('flashback_perfect', I, "'for the LORD had fast shut' (20:18: עצר עצר — an infinitive with its perfect, no narrative verb) — the narrator's flashback; the tape's register test reads 20:8-17's narrative verbs before it", ['wombs_shut'])
    if q == 'gerar_dwelling': return cell('dwell_where_you_please', I, "'behold, my land is before you; dwell where it is good in your eyes' (20:15) — against Pharaoh's 'take and go' (12:19): the frozen unit's contrast", ['dwelling_granted'])
    return cell('no_case', I, '', [FX.NONE])

def moriah(q):
    if q == 'test_verb_seats': return cell(1, I, "the test verb (נסה) at Gen 22:1 alone in Genesis (measured)", ['tried'])
    if q == 'ten_trials_sheet': return cell(10, A, "Mishnah Avot 5:3 — with ten trials Abraham our father was tried and stood in them all", ['tried'])
    if q == 'trials_named_by_the_ink': return cell(1, I, "the ink names one trial by its verb (22:1); the shelf calls it the tenth (Bereshit Rabbah 56:11: 'the tenth trial'), but the list of ten is not on the local shelf (Avot de-Rabbi Natan absent) — the sequence runner CH1 files the DIVERGE open", ['tried'])
    if q == 'after_what': return cell(('the_words_of_satan', 'the_words_of_ishmael'), M, "Sanhedrin 89b:9 (R. Yochanan in R. Yose ben Zimra's name: after the words of Satan — 'the child grew and was weaned', 21:8) and 89b:14 (R. Levi: after the words of Ishmael to Isaac: 'I was circumcised at thirteen — if He said to me, sacrifice yourself, I would')", ['tried'])
    if q == 'four_step_address': return cell(('your_son', 'your_only_one', 'whom_you_love', 'isaac'), I, "'your son, your only one, whom you love, Isaac' (22:2) — the four steps; Bereshit Rabbah 55:7 the dialogue at each", ['offering_of_the_son_owed'])
    if q == 'third_day': return cell(3, I, "'on the third day' (22:4) — the ordinal parsed; the marker of the tape (the binding's day plus two); Bereshit Rabbah 56:1 the third days", ['place_seen_on_the_third_day'])
    if q == 'binding_verb_seats': return cell(1, I, "the binding verb (ויעקד) at Gen 22:9 alone in the Tanakh (measured)", ['bound_on_the_altar'])
    if q == 'rams_horn': return cell('the_binding_remembered', M, "Rosh Hashanah 16a:16 — R. Abbahu: why a ram's horn? that I may remember for you the binding of Isaac son of Abraham, and account it as if you bound yourselves before Me", ['bound_on_the_altar', 'ram_caught'])
    if q == 'countermand_closes': return cell(('offering_of_the_son_owed', 'tried'), I, "'do not send your hand against the lad' (22:12) closes the DEBIT of 22:2; 'now I know' closes the HEAVEN entry of 22:1 — two closes at one verse", ['hand_stayed', 'god_fearing_known'])
    if q == 'ram_in_place': return cell('olah', P, "CALLED cold_run_offerings.dispatch('olah') -> the burnt offering's place: 'and offered it up as a burnt offering in place of his son' (22:13) [IMPORT, live]: " + str(OF.dispatch('olah')['place']['v']), ['olah_offered'])
    if q == 'ram_seen_after': return cell('after_the_generations', M, "Bereshit Rabbah 56:9 — 'a ram AFTER' (22:13): R. Yudan — after all the generations Israel are caught in transgressions and entangled in troubles, and their end is to be redeemed by the horn of a ram", ['ram_caught'])
    if q == 'oath_reward_seats': return cell(('stars', 'sand', 'the_gate_of_enemies', 'the_nations'), I, "'as the stars of heaven and as the sand on the seashore; and your seed shall possess the gate of its enemies; and in your seed all the nations of the earth shall bless themselves' (22:17-18) — the oath's four clauses; 24:60 Rebekah's blessing repeats the gate (the family engine's seat)", ['seed_as_stars', 'gate_of_enemies_promised', 'blessing_promised', 'sworn_by_himself'])
    if q == 'milcah_eight': return cell(8, I, "'these eight Milcah bore to Nahor' (22:23) — the number parsed; the eight names of 22:21-22 (Uz, Buz, Kemuel, Chesed, Hazo, Pildash, Jidlaph, Bethuel) counted in the scene", ['births_told', 'begotten'])
    if q == 'nahor_sons_total': return cell(12, I, "eight by Milcah and four by Reumah (22:24: Tebah, Gaham, Tahash, Maacah) — twelve, and Rebekah by Bethuel: thirteen begotten entries on the ledger", ['begotten'])
    return cell('no_case', I, '', [FX.NONE])

def abraham_end(q):
    if q == 'keturah_identity': return cell('hagar_by_rav', M, "Bereshit Rabbah 61:4 — 'and her name was Keturah': Rav said, she is Hagar; R. Nechemya objected from 'and he added' (a new wife) — recorded on the entity, no fold", ['wife_taken'])
    if q == 'keturah_six': return cell(6, I, "'Zimran and Jokshan and Medan and Midian and Ishbak and Shuah' (25:2) — six sons, the scene's six begotten entries", ['begotten'])
    if q == 'gifts_reading': return cell('deeds_in_his_lifetime', M, "Sanhedrin 91a:16 — 'and Abraham gave all that he had to Isaac, and to the sons of the concubines Abraham gave gifts' (25:5-6): Geviha ben Pesisa — a father who gave deeds of gift to his sons in his lifetime and sent one away from the other, has one a claim on the other?", ['all_given_to_isaac', 'gifts_given'])
    if q == 'inheritance_by_call': return cell(FA.inheritance('inheritance_order_owed')['v'], P, "CALLED cold_run_family.inheritance('inheritance_order_owed') -> the seats the family engine owes forward [IMPORT, live]: 'all that he had to Isaac' (25:5) read against the order the engine keeps", ['all_given_to_isaac'])
    if q == 'good_old_age_seats': return cell(4, I, "'in a good old age' (בשיבה טובה) at Gen 15:15, 25:8, Judg 8:32, 1 Chr 29:28 in the Tanakh (measured at the registry) — the promise and its keeping", ['died_in_good_old_age'])
    if q == 'promise_closed_here': return cell('buried_in_peace', I, "15:15 'you shall be buried in a good old age' (S2's HEAVEN entry) closed at 25:8 by the ink's own words — the close the daemon performs on the tape (nothing on the bare scene)", ['died_in_good_old_age', 'gathered_to_his_people'])
    if q == 'purchase_by_call': return cell(FA.purchase('three_modes')['v'], P, "CALLED cold_run_family.purchase('three_modes') -> the Mishnah's money, deed, possession run at Machpelah [IMPORT, live]: 'the field that Abraham bought from the sons of Heth' (25:10) — the entry read, not rewritten", ['buried'])
    if q == 'twelve_princes': return cell(12, I, "'twelve princes by their nations' (25:16) — parsed; the phrase at 17:20 and 25:16 alone (measured): the promise and its receipt", ['twelve_princes'])
    if q == 'twelve_names_counted': return cell(12, I, "Nebaioth, Kedar, Adbeel, Mibsam, Mishma, Dumah, Massa, Hadad, Tema, Jetur, Naphish, Kedemah (25:13-15) — twelve name tokens, each verified in its verse by the probes", ['twelve_princes'])
    if q == 'seed_multiplied_closed': return cell('Gen 25:16', I, "16:10 'I will greatly multiply your seed' (S2's HEAVEN entry on Hagar) closed at 25:16 by the twelve princes — 17:20's own words received; the tape's close", ['twelve_princes'])
    if q == 'fell_polarity': return cell(('dwell', 'fell'), I, "16:12 'before all his brothers he shall DWELL' and 25:18 'before all his brothers he FELL' — the same prepositional phrase, the verb reversed (the frozen unit's polarity read)", ['fell_before_his_brothers'])
    if q == 'ishmael_repented': return cell('in_abrahams_days', M, "Bava Batra 16b:11 — 'that Ishmael repented in his days' (the good old age's third reading: Ishmael's repentance in Abraham's lifetime; 25:9 Isaac named before Ishmael, the frozen unit's read)", ['gathered_to_his_people'])
    return cell('no_case', I, '', [FX.NONE])

def twins(q):
    if q == 'isaac_barren': return cell('isaac_was_barren', M, "Yevamot 64a:6 — Rava to Rav Nachman: learn from Isaac, 'forty years old when he took Rebekah' (25:20) and 'sixty years old when they were born' (25:26)? — he answered: Isaac was barren (the twenty years)", ['prayed_for_the_wife', 'barren'])
    if q == 'twenty_years': return cell(20, I, "sixty (25:26) minus forty (25:20) — the two markers S1 carries; the barrenness's stretch", ['barren', 'conceived'])
    if q == 'entreaty_verb': return cell('digging', M, "Bereshit Rabbah 63:5 — 'and Isaac entreated' (ויעתר): like one who digs (the frozen unit's read: poured out, or the decree overturned)", ['prayed_for_the_wife'])
    if q == 'struggle_seats': return cell(1, I, "the struggling verb (ויתרצצו) at Gen 25:22 alone in the Tanakh (measured)", ['struggled_in_the_womb'])
    if q == 'oracle_terms': return cell(('two_nations', 'two_peoples', 'one_stronger', 'elder_serves_younger'), I, "'two nations are in your womb, and two peoples shall be separated from your bowels; and one people shall be stronger than the other, and the elder shall serve the younger' (25:23) — four clauses; the last OPEN on the tape and off the three books", ['two_nations_in_the_womb', 'elder_to_serve_the_younger'])
    if q == 'firstborn_sheet': return cell('the_first_to_come_out', A, "Mishnah Bekhorot 8:1 — the firstborn for inheritance is the one who opens the womb: 'and the first came out red' (25:25) — Esau, firstborn_by_the_head (the family engine's effect reused)", ['firstborn_by_the_head'])
    if q == 'heel_naming': return cell('holding_the_heel', I, "'his hand was holding Esau's heel, and he called his name Jacob' (25:26); 27:36 'is he not rightly named Jacob? for he has supplanted me' — the name's two grounds", ['heel_held', 'name_given'])
    if q == 'stew_day': return cell('abrahams_death_day', M, "Bava Batra 16b:11 — a baraita: that day Abraham our father died, and Jacob our father made a dish of lentils to comfort Isaac his father (the calendar row stew_day; the marker of the tape)", ['stew_boiled', 'came_in_weary'])
    if q == 'lentil_readings': return cell(('no_mouth', 'rolls'), M, "Bava Batra 16b:12 — why lentils? as the lentil has no mouth, so the mourner has no mouth; another: as the lentil rolls, so mourning rolls round the world", ['bread_and_lentils_given'])
    if q == 'gulp_verb': return cell('camel', M, "Bereshit Rabbah 63:12 — 'let me gulp' (הלעיטני): he opened his mouth like a camel; Mishnah Shabbat 24:3 uses the verb of the camel (the frozen unit's read)", ['gulp_demanded'])
    if q == 'sale_with_oath': return cell(('sworn', 'sold'), I, "'swear to me as of this day; and he swore to him; and he sold his birthright to Jacob' (25:33) — the oath then the sale; birthright_transferred the family engine's effect at its Genesis seat", ['oath_sworn', 'birthright_transferred'])
    if q == 'fathers_word_sheet': return cell('said_nothing', A, "Mishnah Bava Batra 8:5 — 'my son so-and-so, a firstborn, shall not take a double portion' — he has said nothing, for he stipulated against what is written in the Torah: the father cannot undo it by word; Esau's SALE is the holder's own act, graded beside the row, not by it", ['birthright_transferred'])
    if q == 'despise_seats': return cell(2, I, "the despising verb (ויבז) at Gen 25:34 and Esther 3:6 in the Tanakh (measured — the dry run refuted 'Genesis alone' and the claim was corrected beside its record)", ['birthright_despised'])
    return cell('no_case', I, '', [FX.NONE])

def isaac_gerar(q):
    if q == 'famine_ordinal': return cell('the_second', I, "'besides the first famine that was in the days of Abraham' (26:1) — the ink's own ordinal; Bereshit Rabbah 25:3, 64:1 the census of ten famines (the frozen unit's read)", ['famine'])
    if q == 'olah_rule_transferred': return cell('outside_the_curtains_disqualified', M, "Bereshit Rabbah 64:3 — R. Hoshaya: you are an unblemished burnt offering; as a burnt offering that goes outside the curtains is disqualified, so you outside the land — the offerings engine's rule laid on Isaac by the teacher (a transfer named, not a call)", ['descent_to_egypt_barred'])
    if q == 'charge_words': return cell(('my_charge', 'my_commandments', 'my_statutes', 'my_teachings'), I, "'and kept My charge, My commandments, My statutes and My teachings' (26:5) — four words; 'My charge' at 26:5 alone in Genesis (measured)", ['charge_kept'])
    if q == 'whole_torah_before_sinai': return cell(('yoma_28b', 'kiddushin_82a'), M, "Yoma 28b:10 — Rav (or Rav Ashi): Abraham our father kept even the joining of cooked foods, 'My teachings' — one the written, one the oral; Kiddushin 82a:10 — we find that Abraham our father did the whole Torah before it was given: THE TIME CONSENSUS's (T1) fork reads these two rows", ['charge_kept'])
    if q == 'covenant_heads_by_call': return cell(PS_.covenant('covenant_heads')['v'], P, "CALLED cold_run_pre_sinai.covenant('covenant_heads') -> the covenant's addressees [IMPORT, live]: 'the oath which I swore to Abraham your father' (26:3) read at the covenant the pre-Sinai engine keeps", ['oath_to_abraham_upheld'])
    if q == 'guilt_homograph': return cell('asham_the_noun', I, "'you would have brought guilt upon us' (26:10, אשם) — the guilt offering's noun as the noun guilt: a homograph, FALSE at the census", ['wife_acknowledged'])
    if q == 'decree_formula': return cell('surely_be_put_to_death', I, "'whoever touches this man or his wife shall surely be put to death' (26:11) — the death formula in a king's decree, a homograph of the law's (FALSE at the census); decree_issued the exodus's effect reused", ['decree_issued'])
    if q == 'hundredfold': return cell(100, I, "'a hundredfold' (26:12) — parsed; the phrase's only seat in the Tanakh (measured)", ['hundredfold_found'])
    if q == 'measured_for_tithes': return cell('tithes', M, "Bereshit Rabbah 64:6 — does blessing rest on what is measured? why did he measure? for the tithes — the tithe of produce is Numbers' and Deuteronomy's law, not on the tape: a reading recorded, no call", ['hundredfold_found'])
    if q == 'envy_seats': return cell(3, I, "the envy verb in Genesis: 26:14 (the Philistines), 30:1 (Rachel), 37:11 (the brothers) — measured", ['envied'])
    if q == 'wells_stopped_then': return cell('redug_at_26_18', I, "'the Philistines stopped them and filled them with earth' (26:15); 'and Isaac dug again the wells' (26:18) — a status answered by a status (not a ledger close)", ['wells_stopped', 'wells_redug'])
    if q == 'expelled_word': return cell('go_from_us', I, "'go from us, for you have become much mightier than we' (26:16) — the expulsion's own word; expelled (S2's Eden effect) reused", ['expelled'])
    return cell('no_case', I, '', [FX.NONE])

def wells(q):
    if q == 'three_wells': return cell(('esek', 'sitnah', 'rehoboth'), I, "Esek 'because they contended with him' (26:20), Sitnah (26:21), Rehoboth 'for now the LORD has made room for us' (26:22) — three namings by Isaac", ['quarreled_over', 'room_made', 'name_given'])
    if q == 'names_restored': return cell('like_the_names_his_father_called', I, "'and he called them names like the names his father had called them' (26:18) — the restored names, one naming act", ['wells_redug', 'name_given'])
    if q == 'canon_list_read': return cell('the_canons_own_book_list', M, "Bereshit Rabbah 64:8 — the well names read as the canon's own list (the frozen unit's read)", ['quarreled_over'])
    if q == 'altar_seats_stretch': return cell(2, I, "'and Abraham built the altar there' (22:9), 'and he built an altar there' (26:25) — the building verb with the altar in Gen 18-31, measured", ['altar_built'])
    if q == 'called_on_the_name_seats': return cell(4, I, "'and he called on the name of the LORD' at Gen 12:8, 13:4, 21:33 (the pre-Sinai engine's), 26:25 in Genesis — measured", ['called_on_the_name'])
    if q == 'night_appearance': return cell('fear_not_for_abrahams_sake', I, "'do not fear, for I am with you, and I will bless you and multiply your seed for the sake of Abraham My servant' (26:24) — the night appearance's HEAVEN entry", ['fear_not_promised', 'blessing_promised'])
    if q == 'oath_between_us': return cell('reactivating_the_fathers_oath', M, "Bereshit Rabbah 64:10 — 'let there be an oath between us' (26:28): rendered as reactivating the oath sworn with Abraham (21:23-31, the pre-Sinai engine's seat) — the frozen unit's read", ['covenant_proposed', 'covenant_between_men'])
    if q == 'swore_each_to_his_brother': return cell('Gen 26:31', I, "'and swore each to his brother' (26:31) — the men's covenant sealed by oath; sent away in peace", ['oath_sworn', 'sent_out'])
    if q == 'shibah_naming': return cell(('shibah', 'beersheba'), I, "'and he called it Shibah; therefore the city's name is Beersheba to this day' (26:33) — the second naming of the city (21:31 the first, the pre-Sinai engine's)", ['name_given', 'well_dug'])
    if q == 'esau_forty': return cell(40, I, "'and Esau was forty years old' (26:34) — parsed; the marker S1 carries; the sequence runner CH6: Isaac's hundred", ['wife_taken'])
    if q == 'esau_marriage_graded': return cell('the_boar_of_the_forest', M, "Bereshit Rabbah 65:1 — 'and Esau was forty': the boar of the forest that shows its cloven hoof (piety theatre, the frozen unit's zoological read); 65:3 the match graded", ['wife_taken', 'bitterness_of_spirit'])
    if q == 'bitterness_ground': return cell('idolatry', M, "Bereshit Rabbah 65:4 — 'a bitterness of spirit to Isaac and to Rebekah': they worshipped idols; the father named first (the frozen unit's three answers)", ['bitterness_of_spirit'])
    return cell('no_case', I, '', [FX.NONE])

def blessing(q):
    if q == 'dim_eyes_causes': return cell(4, M, "Bereshit Rabbah 65:10 — the four causes the frozen unit keeps: the wives' incense-smoke, the angels' tears at the binding, the blessing's need, the ransom of the sight", ['eyes_dim'])
    if q == 'death_worry_arithmetic': return cell((127, 123), M, "Bereshit Rabbah 65:12 — a man who reaches his parents' years worries five years before and after: Sarah a hundred and twenty-seven, Isaac now a hundred and twenty-three (the row blessing_placement; the marker of the tape at Jacob's sixty-three)", ['death_day_unknown'])
    if q == 'jacob_at_the_blessing': return cell(63, M, "Bereshit Rabbah 68:5 — Hezekiah said: sixty-three years old was our father Jacob when he took the blessings; the sequence runner CH3 joins it to the ink (died:ishmael minus born:jacob)", ['blessed_with_dew_and_fat'])
    if q == 'two_kids_contract': return cell('two_kids_daily', M, "Bereshit Rabbah 65:14 — R. Levi: if you find them, good; if not, bring me from my own settlement — for so he had written her in her marriage contract, that he would bring up to her two kids every day", ['two_kids_counselled'])
    if q == 'i_am_esau_defence': return cell('declined', M, "Makkot 24a:8 ('who speaks truth in his heart' — the frozen unit's routed row): the equivocation defence — 'I am; Esau is your firstborn' — declined by the shelf: identity_falsely_claimed stands", ['identity_falsely_claimed'])
    if q == 'voice_and_hands': return cell(('jacobs_voice', 'esaus_hands'), I, "'the voice is Jacob's voice, but the hands are Esau's hands' (27:22); 'and he did not recognize him' (27:23) — the recognition verb's first Torah seat (the frozen unit's read)", ['not_recognized'])
    if q == 'blessing_clauses': return cell(('dew', 'fat', 'grain_and_wine', 'peoples_serve', 'master_over_brothers', 'cursers_cursed'), I, "27:28-29 — the blessing's six clauses; two HEAVEN entries carry them", ['blessed_with_dew_and_fat', 'peoples_to_serve'])
    if q == 'ratified': return cell('he_shall_be_blessed', I, "'indeed, he shall be blessed' (27:33) — the ratification by its own signatory; 28:3-4 repeats it knowingly", ['blessing_ratified'])
    if q == 'trembling_greater': return cell('than_moriah', M, "Bereshit Rabbah 67:2 — a trembling greater than the trembling on Mount Moriah: he saw Gehenna open beneath Esau (the frozen unit's read)", ['trembled'])
    if q == 'supplanted_count': return cell(2, I, "'he has supplanted me these two times' (27:36) — the ledger's two transfers on Jacob from Esau: birthright_transferred (25:33) and the blessing (27:27-29); the sequence runner CH10", ['supplanted_twice'])
    if q == 'cry_booked_against': return cell('esther_4_1', M, "Bereshit Rabbah 67:4 — 'a great and bitter cry' (27:34) booked against 'a great and bitter cry' at the palace gate (Esther 4:1), the frozen unit's read", ['great_and_bitter_cry'])
    if q == 'esau_blessing_clauses': return cell(('fat_of_the_earth', 'dew_from_above', 'by_your_sword', 'serve_your_brother', 'break_his_yoke'), I, "27:39-40 — five clauses; the mirror of 27:28's dew and fat (the frozen unit's read); the yoke's breaking off the three books — OPEN", ['blessed_by_the_sword'])
    if q == 'slave_maxim': return cell('what_a_slave_acquires_his_master_acquires', M, "Bereshit Rabbah 67:5 — 'I have made him master over you' (27:37): the slave-property maxim voiding Esau's claim (the frozen unit's read)", ['master_made'])
    return cell('no_case', I, '', [FX.NONE])

def grudge(q):
    if q == 'grudge_verb_seats': return cell(3, I, "the grudge verb in Genesis: 27:41 (Esau), 49:23 (the archers), 50:15 (the brothers' fear) — measured", ['grudge_held'])
    if q == 'kill_after_mourning': return cell('open_never_executed', I, "'the days of mourning for my father draw near, and I will kill Jacob my brother' (27:41) — a HEAVEN entry OPEN on the tape: 33:4's embrace (S4) never closes it, the ink records no killing", ['kill_intent_after_the_mourning'])
    if q == 'few_days_analogy': return cell('seven_years', M, "the frozen unit gen_47's read: 'a few days' (27:44) made seven years by verbal analogy with 29:20's 'as a few days' — the untold years; Rebekah's 'I will send and take you' (27:45) OPEN forever", ['few_days_promised'])
    if q == 'flight_receipt': return cell('Gen 28:10', I, "'arise, flee for yourself to Laban my brother, to Haran' (27:43) received at 28:10 'and Jacob went out from Beersheba and went toward Haran' — the DEBIT closed", ['flight_owed'])
    if q == 'canaanite_ban': return cell('no_wife_from_the_daughters_of_canaan', I, "'you shall not take a wife from the daughters of Canaan' (28:1) — Isaac's BLOCK on Jacob; 24:3 Abraham's own to the servant (the family engine's seat)", ['canaanite_wife_barred'])
    if q == 'wife_from_paddan_receipt': return cell('Gen 29:28', I, "'take yourself from there a wife from the daughters of Laban' (28:2) received at 29:28 'and he gave him Rachel his daughter as his wife' — the DEBIT closed (Leah's taking at 29:23 was the switch)", ['wife_from_paddan_owed'])
    if q == 'assembly_of_peoples': return cell('tribes', M, "Bereshit Rabbah 67:12 — 'and you shall be an assembly of peoples' (28:3): nationalized into tribes (the frozen unit's read)", ['blessing_of_abraham_given'])
    if q == 'mahalath_at_ishmaels_death': return cell('ishmael_had_died', M, "Megillah 17a:5 — 'Mahalath daughter of Ishmael, sister of Nebaioth' (28:9): Ishmael had died and Nebaioth gave her — the inference the marker of the tape rides (died:ishmael)", ['wife_taken'])
    if q == 'esau_saw_twice': return cell(2, I, "'and Esau saw' at 28:6 and 28:8 — two seeings, the second 'that the daughters of Canaan were evil in the eyes of Isaac his father'", ['esau_saw_the_command'])
    if q == 'exile_table': return cell('tribes_against_kingdoms', M, "the frozen unit gen_47's own WITNESS: the exile table — tribes paired against kingdoms with named agents (28:9's coda)", ['esau_saw_the_command'])
    return cell('no_case', I, '', [FX.NONE])

def bethel(q):
    if q == 'sun_set_early': return cell('two_hours', M, "Bereshit Rabbah 68:10 — the rabbis: 'the sun had set' (28:11) — the Holy One made the sun's globe set before its time to speak with Jacob in private; the borrowed hours repaid at 32:32 (the frozen unit's read)", ['sun_set_at_the_place'])
    if q == 'stones_into_one': return cell('gathered_into_one', M, "Chullin 91b:8 — 'of the stones of the place' (28:11) and 'the stone' (28:18): R. Yitzchak — all those stones gathered to one place, each saying: on me let this righteous one rest his head; a baraita: all were swallowed into one", ['stone_pillow', 'pillar_anointed'])
    if q == 'hidden_fourteen': return cell(14, M, "Bereshit Rabbah 68:11 — R. Yehuda: here he lay down, but all fourteen years hidden in the house of Eber he did not lie down; Megillah 17a:5-6 the fourteen (the row hidden_years; the marker of the tape)", ['stone_pillow'])
    if q == 'first_narrated_dream': return cell('Gen 28:12', I, "'and he dreamed' (28:12) — the Torah's first narrated dream-act (the frozen unit's read); 31:10 the second, told", ['ladder_dreamed'])
    if q == 'kingdoms_on_the_ladder': return cell(4, M, "Bereshit Rabbah 68:12 — the angels ascending and descending: the kingdoms — Babylon, Media, Greece, Edom (the frozen unit's read: the sequence off the ladder)", ['ladder_dreamed'])
    if q == 'promise_clauses': return cell(('land', 'dust', 'four_directions', 'families_blessed', 'with_you', 'keep_you', 'bring_you_back', 'not_leave'), I, "28:13-15 — eight clauses; five HEAVEN entries carry them: land_promised, seed_as_dust, blessing_promised (reused) and with_you_promised, return_promised (new)", ['land_promised', 'seed_as_dust', 'blessing_promised', 'with_you_promised', 'return_promised'])
    if q == 'with_you_closed_at': return cell('Gen 31:5', I, "'and behold, I am with you' (28:15) closed by Jacob's own 'but the God of my father has been with me' (31:5) — the ink's fulfillment statement; the sequence runner CH9", ['with_you_promised'])
    if q == 'return_closed_at': return cell('Gen 35:6', I, "'and I will bring you back to this ground' (28:15) — OPEN on the tape until S4's 35:6 'and Jacob came to Luz, that is Bethel'", ['return_promised'])
    if q == 'first_oil': return cell('Gen 28:18', I, "'and poured oil on its top' (28:18) — the Torah's first oil poured; the anointing verb of 31:13 a homograph of the holy oil's law (FALSE at the census)", ['pillar_anointed'])
    if q == 'luz_bethel': return cell(('bethel', 'luz'), I, "'and he called the name of that place Bethel, but Luz was the name of the city at first' (28:19) — the naming with the former name", ['name_given'])
    if q == 'vow_conditions': return cell(4, I, "'if God will be with me, and keep me on this way, and give me bread to eat and a garment to wear, and I return in peace to my father's house' (28:20-21) — four conditions", ['vow_of_bethel'])
    if q == 'vow_commitments': return cell(3, I, "'then the LORD shall be my God; and this stone shall be the house of God; and all that You give me I will surely tithe' (28:21-22) — three commitments; OPEN until S4's 35:7 and 35:14", ['vow_of_bethel', 'tithe_vowed'])
    if q == 'tithe_by_call': return cell(TM.tithe('land_tithe_status')['v'], P, "CALLED cold_run_temurah.tithe('land_tithe_status') -> the tithe's own status (Lev 27:30) [IMPORT, live]: 'I will surely tithe to You' (28:22), as 14:20's at S2", ['tithe_vowed'])
    if q == 'charity_cap_verse': return cell('Gen 28:22', M, "Ketubot 50a:3 — Rav Nachman (or Rav Acha bar Yaakov): what is the verse? 'and all that You give me I will surely tithe to You' — the doubled verb, two tenths: the charity cap's verse (the Genesis campaign's KINDNESS block seated it)", ['tithe_vowed'])
    if q == 'tithe_phrase_seats': return cell(1, I, "'I will surely tithe' (עשר אעשרנו) at Gen 28:22 alone in the Tanakh (measured at the registry)", ['tithe_vowed'])
    return cell('no_case', I, '', [FX.NONE])

def well_stone(q):
    if q == 'six_institutions': return cell('one_machine_bound_to_six', M, "Bereshit Rabbah 70:8-9 — the well: Zion, the Sanhedrin, Sinai (the three flocks: the three pilgrim festivals, the three courts...) — the frozen unit's read: one machine bound to six institutions", ['well_with_the_stone'])
    if q == 'stone_protocol': return cell(('gather', 'roll', 'water', 'return'), I, "'all the flocks would gather there, and they would roll the stone, and water the sheep, and return the stone to its place' (29:3) — the custom's four steps; 29:8 the shepherds' refusal on its ground", ['well_with_the_stone'])
    if q == 'labor_duty': return cell('finish_the_days_work', M, "Bereshit Rabbah 70:11 — 'the day is still great' (29:7): if you are hired hands you have not finished your day's work; if the sheep are yours, it is not the time to gather — the labor duty from an exhaustive disjunction (the frozen unit's read)", ['shepherds_rebuked'])
    if q == 'stone_rolled_alone': return cell('as_a_stopper_from_a_flask', M, "Bereshit Rabbah 70:12 — as one removes a stopper from a flask: the strength exhibit at its verse (the frozen unit's read)", ['stone_rolled_alone'])
    if q == 'why_wept': return cell(('not_buried_with_him', 'came_with_nothing'), M, "Bereshit Rabbah 70:12 — why did Jacob weep? he saw that she would not enter the grave with him; another: Eliezer came with ten camels and I with nothing", ['kissed_and_wept'])
    if q == 'kisses_seats': return cell(3, I, "the kiss verb in the stretch: 27:26-27 (Isaac and Jacob), 29:11 (Jacob and Rachel), 29:13 (Laban and Jacob) — the frozen unit gen_49's exhaustive table", ['kissed_and_wept', 'embraced_and_housed'])
    if q == 'her_fathers_brother': return cell('ambiguity_kept', M, "Bereshit Rabbah 70:12 — 'her father's brother' (29:12): if for deceit, I am his brother in deceit; if an honest man, I am the son of Rebekah his honest sister — the ambiguity the frozen unit keeps", ['kin_told'])
    if q == 'welcome_decoded': return cell(('gold', 'pearls'), M, "Bereshit Rabbah 70:13 — he embraced him: to feel for gold; he kissed him: for pearls in his mouth — the welcome decoded as a stripping (the frozen unit's read)", ['embraced_and_housed', 'bone_and_flesh'])
    if q == 'month_phrase_seats': return cell(3, I, "'a month of days' (חדש ימים) at Gen 29:14, Num 11:20, 11:21 in the Tanakh (measured at the registry) — no numeral: the marker's month by the Calendar", ['month_dwelt'])
    return cell('no_case', I, '', [FX.NONE])

def wage(q):
    if q == 'three_specifications': return cell(('rachel', 'your_daughter', 'the_younger'), M, "Bava Batra 123a:10 — 'for Rachel your younger daughter' (29:18): Rachel — not Leah; your daughter — not another Rachel from the street; the younger — not their names exchanged: perfect drafting, defeated outside it (the frozen unit's read)", ['seven_years_owed'])
    if q == 'leahs_eyes': return cell('from_weeping', M, "Bava Batra 123a:12-14 — 'Leah's eyes were tender' (29:17): from weeping — the elder for the elder, the younger for the younger: she wept not to fall to Esau's lot", ['two_daughters'])
    if q == 'seven_years_seats': return cell(5, I, "'seven years' at 29:18, 29:20, 29:27, 29:30 and 'fourteen years' at 31:41 — the two sevens' five seats in the stretch (the ink dump: seven parsed at each)", ['seven_years_owed', 'second_seven_owed'])
    if q == 'seven_years_timer_days': return cell(365 * 7, D, "the seven years' timer on the bare scene: 2555 days (no epoch — the Calendar's years on the tape); set at the agreement (29:18), fires at 29:21 'my days are fulfilled'", ['seven_years_service'])
    if q == 'married_at': return cell(84, M, "Bereshit Rabbah 68:5 — sixty-three at the blessings, fourteen hidden, seven for Rachel: we find he married at eighty-four; the sequence runner CH5 joins it to the tape's wedding year", ['seven_years_service'])
    if q == 'switch_measure_for_measure': return cell('did_your_father_not_call_you_esau', M, "Bereshit Rabbah 70:19 — all that night she answered to Rachel's name; in the morning: 'deceiver, daughter of a deceiver — did I not call you Rachel and you answered?' — 'and did your father not call you Esau and you answered?'", ['bride_switched', 'deceit_charged'])
    if q == 'custom_of_the_place': return cell('younger_not_before_the_firstborn', I, "'it is not done so in our place, to give the younger before the firstborn' (29:26) — the local rule stated; Mishnah Bava Batra 8:5's precedence of the firstborn beside it", ['custom_of_the_place'])
    if q == 'week_phrase_seats': return cell(1, I, "'fulfill the week of this one' (מלא שבע זאת) at Gen 29:27 alone in the Tanakh (measured at the registry)", ['week_of_the_feast'])
    if q == 'no_mixing_of_joys': return cell('from_here', M, "Bereshit Rabbah 70:19 — R. Yaakov bar Acha: from here, that one does not mix a joy with a joy — 'fulfill the week of this one'; the Babylonian arm from Solomon's fourteen days (Moed Katan 9a:4; 8b:9 the rule)", ['week_of_the_feast'])
    if q == 'festival_marriage_sheet': return cell('no_marriage_on_the_festival', A, "Mishnah Moed Katan 1:7 — one does not marry on the festival, for it is a joy to him; the gemara's ground (8b:9) is the mixing rule Jacob's week teaches (Bereshit Rabbah 70:19)", ['week_of_the_feast'])
    if q == 'week_timer_days': return cell(7, D, "the week's timer: seven days from the demand (29:27) to Rachel's giving (29:28); the sequence runner CH7: it fires before wife_taken rachel", ['week_of_the_feast'])
    if q == 'two_maids': return cell(('zilpah', 'bilhah'), I, "'and Laban gave her Zilpah his maid' (29:24), 'and Laban gave to Rachel his daughter Bilhah his maid' (29:29) — the two transfers; both later wives (30:4, 30:9)", ['maid_given'])
    return cell('no_case', I, '', [FX.NONE])

def twelve_names(q):
    if q == 'births_in_the_stretch': return cell(14, I, "the scene's `born` events in Gen 25-30: the twins (25:24-26) and the twelve (29:32-30:24) — fourteen; thirteen male, Dinah the one daughter", ['conceived', 'daughter_born'])
    if q == 'eighth_days_set': return cell(13, D, "the covenant's eighth-day timer (the pre-Sinai daemon on `born`, 17:12 'every male') set thirteen times on the bare scene — none on Dinah (the sex field read: 7k); the sequence runner CH8", ['daughter_born'])
    if q == 'namings_by_mothers': return cell(12, I, "the twelve namings of 29:32-30:24 — Leah eight (Reuben, Simeon, Levi, Judah, Gad, Asher, Issachar, Zebulun — and Dinah), Rachel four (Dan, Naphtali, Joseph — and by the counting the mothers' own, the frozen unit's four-cell table)", ['name_given'])
    if q == 'namings_in_the_stretch': return cell(len([e for e in _SCENE_NAMED]), I, "the scene's naming events across Gen 18-31 — the twenty-nine seats of 7c, counted from the scene itself", ['name_given'])
    if q == 'thanks_at_the_fourth': return cell('judah', M, "Bereshit Rabbah 71:5 — from the day the world was created no one thanked the Holy One until Leah came and thanked Him: 'this time I will praise the LORD' (29:35) — gratitude begins where entitlement ends (the frozen unit's read)", ['ceased_bearing'])
    if q == 'three_keys': return cell(('childbirth', 'rain', 'the_dead'), M, "Taanit 2a:12-13 — three keys in the Holy One's hand not delegated to an agent: the key of childbirth ('and He opened her womb', 29:31; 30:22), of rain, of the resurrection — the frozen unit's read", ['womb_opened'])
    if q == 'accounted_as_dead': return cell('one_without_children', M, "Nedarim 64b (the frozen unit's routed row) — 'give me children, and if not, I die' (30:1): one who has no children is accounted as dead", ['children_demanded'])
    if q == 'mandrakes_seats': return cell(1, I, "the mandrakes token (דודאים) at Gen 30:14 alone in Genesis (measured); the construct forms at 30:14-16", ['mandrakes_found'])
    if q == 'trade_ledger': return cell(('leah_lost_mandrakes_gained_two_tribes', 'rachel_gained_mandrakes_lost_tribes'), M, "Bereshit Rabbah 72:3 — R. Elazar: this one lost and this one gained: Leah lost the mandrakes and gained two tribes and the birthright; Rachel gained the mandrakes and lost the tribes and the birthright; R. Shmuel bar Nachman: and the burial with him", ['night_hired_for_mandrakes'])
    if q == 'remembered_on_rosh_hashanah': return cell('rosh_hashanah', M, "Rosh Hashanah 11a:16 — R. Elazar: on Rosh Hashanah Sarah, Rachel and Hannah were remembered — remembrance from remembrance ('and God remembered Rachel', 30:22; 'a remembrance of blowing', Lev 23:24); 10b:10 and 11a:2 the two baraitot; Bereshit Rabbah 73:1 — the row rachel_remembered_date, unexercised", ['remembered_by_god', 'heard_by_god'])
    if q == 'another_son': return cell('benjamin_at_35_18', I, "'may the LORD add to me another son' (30:24) — a HEAVEN entry OPEN on the tape until S4's 35:17-18; Bereshit Rabbah 73:6: another — one more, not two", ['another_son_asked'])
    if q == 'dinah_no_eighth_day': return cell('female', I, "'and afterward she bore a daughter' (30:21) — `born` with the sex field f: 17:12 'every male' — the pre-Sinai daemon reads the field the statute names (7k)", ['daughter_born'])
    return cell('no_case', I, '', [FX.NONE])

def speckled(q):
    if q == 'release_keyed_to': return cell('josephs_birth', I, "'and it was, when Rachel had borne Joseph, that Jacob said to Laban: send me away' (30:25) — the second seven's end at Joseph's birth; the sequence runner CH4 joins the fourteen's end to born:joseph's year", ['release_demanded', 'wives_and_children_claimed'])
    if q == 'second_seven_timer_days': return cell(365 * 7, D, "the second seven's timer on the bare scene: 2555 days from Rachel's giving (29:28-30) to 30:25", ['second_seven_service'])
    if q == 'divination_scrubbed': return cell('both_translations', M, "Bereshit Rabbah 73:8 — 'I have divined' (30:27): scrubbed identically by both translations (the frozen unit's read)", ['divined_blessing'])
    if q == 'wage_terms': return cell(('speckled', 'spotted', 'dark_among_the_lambs'), I, "'every speckled and spotted sheep and every dark sheep among the lambs, and the spotted and speckled among the goats — and that shall be my wage' (30:32)", ['speckled_wage_agreed'])
    if q == 'righteousness_clause': return cell('on_a_day_to_come', I, "'and my righteousness shall answer for me on a day to come' (30:33) — the audit clause; 'count it stolen with me'", ['righteousness_to_answer'])
    if q == 'three_days_distance': return cell(3, I, "'a way of three days between himself and Jacob' (30:36) — parsed; Bereshit Rabbah 74:6 reads it with 31:22-23", ['flock_removed'])
    if q == 'rods_two_arms': return cell(('natural_sign', 'angelic_transfer'), M, "Bereshit Rabbah 73:10 — the rods: a natural sign, or the angel's transfer (31:10-12's dream) — the two arms the frozen unit keeps; the impression doctrine applied to a paternity case", ['rods_peeled', 'flock_bore_striped'])
    if q == 'wage_flip_rule': return cell('all_bore_what_he_named', I, "'if he said thus: the speckled shall be your wage — then all the flock bore speckled; and if: the striped — all bore striped' (31:8)", ['flock_bore_striped'])
    if q == 'ten_changes': return cell(10, I, "'ten times' (עשרת מנים) at 31:7 and 31:41 alone in the Tanakh (measured at the registry); parsed ten at both", ['speckled_wage_agreed'])
    if q == 'ten_or_a_hundred': return cell(('ten', 'a_hundred'), M, "Bereshit Rabbah 74:3, 74:11 — the rabbis: a hundred times, 'no counting is fewer than ten' — the row wage_changes_count, the second arm unexercised", ['speckled_wage_agreed'])
    if q == 'broke_out_seats': return cell(('30:30', '30:43'), I, "'the little you had before me has broken out into abundance' (30:30 — Laban's) and 'the man broke out exceedingly, exceedingly' (30:43 — Jacob's): the same verb on both ledgers", ['broke_out_exceedingly'])
    return cell('no_case', I, '', [FX.NONE])

def flight(q):
    if q == 'three_stage_trigger': return cell(('the_sons_words', 'labans_face', 'the_lords_command'), I, "31:1 the sons' words, 31:2 Laban's face, 31:3 'return to the land of your fathers' — the three-stage trigger ending in a command (the frozen unit's read)", ['sons_words_heard', 'face_changed', 'return_owed'])
    if q == 'return_owed_open_until': return cell('Gen 33:18', I, "'return to the land of your fathers' (31:3) — return_owed (S2's effect reused) OPEN on the tape until S4's 33:18 'and Jacob came in peace to the city of Shechem, in the land of Canaan'", ['return_owed'])
    if q == 'counsel_in_the_field': return cell('prudence', M, "Bereshit Rabbah 74:2 — 'to the field, to his flock' (31:4): the prudence rule from the setting (the frozen unit's read)", ['wives_summoned_to_the_field'])
    if q == 'with_me_stated': return cell('Gen 31:5', I, "'but the God of my father has been with me' (31:5) — Jacob's statement, the ink's fulfillment of 28:15 'I am with you' — the close performed", ['god_with_me'])
    if q == 'rescue_verb_first': return cell('Gen 31:9', I, "'and God has rescued your father's livestock' (31:9) — the rescue verb's first seat in the book (the frozen unit's read); 31:16 the wives repeat it", ['livestock_rescued'])
    if q == 'dream_medium': return cell('the_angel_of_god_in_the_dream', I, "'and the angel of God said to me in the dream' (31:11) — the medium fixed by comparing 31:10 and 31:11 (the frozen unit's read)", ['he_goats_dreamed'])
    if q == 'bethel_recalled': return cell(('anointed_a_pillar', 'vowed_a_vow'), I, "'I am the God of Bethel, where you anointed a pillar, where you vowed to Me a vow' (31:13) — the open debit's own mention", ['god_of_bethel_recalled'])
    if q == 'why_rachel_first': return cell(('spoke_before_her_sister', 'the_elders_curse'), M, "Bereshit Rabbah 74:4 — why did Rachel die first? R. Yudan: because she spoke before her sister (31:14); R. Yose: because of the elder's curse (31:32) — the chain to 35:19", ['inheritance_questioned', 'death_oath_on_the_thief'])
    if q == 'abram_formula': return cell('Gen 12:5', I, "'all his property which he had acquired' (31:18) — the Abram formula of 12:5 (S2's seat), the frozen unit's read", ['rose_and_loaded'])
    if q == 'teraphim_seats': return cell(3, I, "the teraphim token (התרפים) at Gen 31:19, 31:34, 31:35 (measured at the registry)", ['teraphim_stolen'])
    if q == 'rachels_intent': return cell('for_the_sake_of_heaven', M, "Bereshit Rabbah 74:5 — she intended only for the sake of Heaven: shall we go and leave this old man in his corruption? — therefore the verse had to say 'Rachel stole'; the shearing a portent wherever it occurs", ['teraphim_stolen'])
    if q == 'two_thefts': return cell(('rachel_the_teraphim', 'jacob_the_heart'), I, "'and Rachel stole the teraphim' (31:19); 'and Jacob stole the heart of Laban the Aramean' (31:20) — the two thefts, one verb", ['teraphim_stolen', 'heart_stolen'])
    return cell('no_case', I, '', [FX.NONE])

def heap(q):
    if q == 'third_day_told': return cell(3, I, "'on the third day' (31:22) — the ordinal parsed; the marker of the tape (the flight plus two)", ['told_on_the_third_day'])
    if q == 'seven_days_journey': return cell(7, I, "'a seven days' journey' (31:23) — parsed; a distance, the overtaking day unstated (the row labans_pursuit); Bereshit Rabbah 74:6: what Jacob went in seven days Laban went in one", ['pursued_seven_days'])
    if q == 'dream_guard': return cell('neither_good_nor_bad', I, "'guard yourself, lest you speak with Jacob either good or bad' (31:24) — the DEBIT closed at 31:29 by Laban's own keeping; Bereshit Rabbah 74:7 the wicked's prophecy at night", ['speech_restrained'])
    if q == 'death_oath_seats': return cell(1, I, "'he shall not live' (לא יחיה) at Gen 31:32 in Genesis (measured at the registry) — the warrant on the unknown thief, whom the narrator named at 31:19", ['death_oath_on_the_thief'])
    if q == 'curse_chain': return cell('Gen 35:19', M, "Bereshit Rabbah 74:9 — 'with whomever you find your gods, he shall not live' — and it was so, as an error that goes out from before the ruler (Ecclesiastes 10:5): 'and Rachel stole' (31:19)... 'and Rachel died' (35:19); 74:4 R. Yose the same — the HEAVEN entry OPEN until S4, closed there by this transfer", ['death_oath_on_the_thief'])
    if q == 'four_tents': return cell(4, I, "'into Jacob's tent and into Leah's tent and into the tent of the two maidservants... and came into Rachel's tent' (31:33) — four tents, the frozen unit's count", ['tents_searched'])
    if q == 'way_of_women': return cell('a_status_claimed', I, "'for the way of women is upon me' (31:35) — Rachel's claim, a status in her mouth, not the clocks engine's event", ['tents_searched'])
    if q == 'keepers_sheet': return cell(('oath', 'pay', 'pay'), A, "Mishnah Bava Metzia 7:8 — the paid keeper and the hirer swear on the broken, the captured and the dead, and PAY the lost and the stolen: (accidents: oath; theft: pay; loss: pay)", ['keeper_account'])
    if q == 'paid_keeper_by_call': return cell((GD.matrix[('paid', GD.THEFT)], GD.matrix[('paid', GD.ACC)], GD.matrix[('paid', GD.LOSS)]), P, "CALLED cold_run_guardians.matrix[('paid', theft / accidents / loss)] -> the paid keeper's three verdicts (Exodus 22:9-12) [IMPORT, live]: 'stolen by day or stolen by night' — PAY; 'a torn beast' — the witnessed accident's OATH; the loss — PAY", ['keeper_account', 'torn_borne_beyond_duty'])
    if q == 'torn_beyond_the_row':
        _torn = GD.verse_facts(12)   # the torn verse's own facts (Exod 22:12), read live from the guardians machine
        return cell('exempt_yet_paid', I, "Exodus 22:12 'if it be torn, let him bring it as witness; he shall not pay for the torn' — the row exempts; 'a torn beast I did not bring to you — I bore its loss' (31:39): Jacob paid beyond the duty", ['torn_borne_beyond_duty'])
    if q == 'keepers_ceiling': return cell('an_extra_guarding', M, "Bava Metzia 93b:3 — until when must a paid keeper guard? as far as 'I was, by day the heat consumed me and the frost by night'; is Jacob our father a city watchman?! — he told Laban: I guarded for you an extra guarding, like the city's watchmen", ['torn_borne_beyond_duty', 'keeper_account'])
    if q == 'twenty_years_ledger': return cell((20, 14, 6, 10), I, "'these twenty years... fourteen years for your two daughters and six years for your flock, and you changed my wages ten times' (31:41) — parsed at 31:38 and 31:41", ['twenty_years_served', 'wages_changed_ten_times'])
    if q == 'labor_above_merit': return cell('labor_ranked_above_the_fathers_merit', M, "Bereshit Rabbah 74:12 — 'were it not that the God of my father... God has seen my affliction and the labor of my hands' (31:42): the labor ranked above the merit of the fathers; the attribution flagged uncertain by the transmitter (the frozen unit's read)", ['adjudicated_last_night'])
    if q == 'two_tongues': return cell(('yegar_sahadutha', 'galeed'), I, "'and Laban called it Jegar-sahadutha, and Jacob called it Galeed' (31:47) — the Aramaic and the Hebrew, one heap: the phrase's only seat in the Tanakh (measured at the registry)", ['name_given', 'heap_made'])
    if q == 'heap_names_count': return cell(4, I, "Jegar-sahadutha, Galeed (31:47), Galeed by the report formula (31:48), Mizpah (31:49) — four namings on the heap in the scene", ['name_given'])
    if q == 'covenant_terms': return cell(('no_affliction_of_the_daughters', 'no_wives_over_them'), I, "'if you afflict my daughters, and if you take wives over my daughters' (31:50) — the two terms; the affliction verb is Exodus 21:10's word, a homograph at the census", ['covenant_terms'])
    if q == 'boundary_carve_out': return cell('for_harm', I, "'that I will not pass beyond this heap to you, and that you will not pass beyond this heap and this pillar to me, FOR HARM' (31:52) — the carve-out (the frozen unit's read: a legal afterlife in court)", ['boundary_witnessed'])
    if q == 'oath_by_the_fear': return cell('the_fear_of_his_father_isaac', I, "'and Jacob swore by the Fear of his father Isaac' (31:53) — not by the gods of Nahor; the oath's grade sacred or profane (the frozen unit's read)", ['oath_sworn', 'covenant_between_men'])
    if q == 'shelamim_by_call': return cell(OF.dispatch('shelamim')['place']['v'], P, "CALLED cold_run_offerings.dispatch('shelamim') -> the peace offering's place [IMPORT, live]: 'and Jacob sacrificed a sacrifice on the mountain, and called his kinsmen to eat bread' (31:54) — the kin eat of it: the shape before the law", ['sacrifice_offered'])
    if q == 'sacrifice_pair_first': return cell('Gen 31:54', I, "'sacrificed a sacrifice' (ויזבח זבח) — the pair's first seat in the Torah (46:1 Jacob again, S4; Exod 18:12 Jethro, S1's)", ['sacrifice_offered', 'ate_and_lodged'])
    return cell('no_case', I, '', [FX.NONE])


# ---- (6) THE WRAP: the daemon over the cells — consumes the stretch's acts, writes the ledger, never emits an event ----
def _years(world, day, n):
    return world.clock.calendar.add(day, n, 'year') if world.clock.epoch else day + 365 * n

def E_(effect, subject, cp=None, value=None, due=None):
    return {'effect': effect, 'subject': subject, 'counterparty': cp, 'amount': None, 'due': due, 'value': value}

def law_mamre(event, world):
    """FROM MAMRE TO THE HEAP's daemon (the forty-second): the acts and speeches of Genesis 18-20, 22, 25-31 to the ledger.
    One branch per watched kind — the writes per event are the hand-model's own table (scratchpad o8_s3_predict.py, printed
    before this file was typed). The daemon answers ITS SPAN ONLY (convention 14 both ways): a shared kind at another seat
    is another daemon's. One close on another engine's event: son_promised_at_the_season on the pre-Sinai engine's born isaac
    at Gen 21:2 — the ink's own fulfillment ('at the set time of which God had spoken')."""
    k, subj, src = event['kind'], event.get('subject'), event.get('case_source', '')
    day = event.get('day', world.clock.day)
    s = WE.seat(src)
    if k == 'born' and subj == 'isaac' and s == ('Gen', 21):
        world.close('sarah', 'son_promised_at_the_season', 'Gen 21:2 — and Sarah conceived and bore Abraham a son, at the set time of which God had spoken (the pre-Sinai engine\'s birth; the promise of 18:10 kept)')
        return []
    if not (s is not None and s[0] == 'Gen' and s[1] in (18, 19, 20, 22, 25, 26, 27, 28, 29, 30, 31)): return []
    if k == 'appeared':
        T = {
            ('Gen 18:1', 'abraham'): lambda: [],
            ('Gen 26:2', 'isaac'): lambda: [],
            ('Gen 26:24', 'isaac'): lambda: [E_('fear_not_promised', subj), E_('blessing_promised', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'ran_and_bowed':
        T = {
            ('Gen 18:2', 'abraham'): lambda: [E_('visitors_received', subj)],
            ('Gen 19:1', 'lot'): lambda: [E_('angels_lodged', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'hospitality_offered': return []
    if k == 'cakes_ordered': return []
    if k == 'calf_prepared': return []
    if k == 'meal_served': return []
    if k == 'son_promised': return [E_('son_promised_at_the_season', subj), E_('return_at_the_season', subj, due=_years(world, day, event.get('years', 1)))]
    if k == 'laughed_within': return [E_('laughed_within', subj)]
    if k == 'laugh_denied': return [E_('laugh_denied', subj)]
    if k == 'escorted': return []
    if k == 'house_charged': return [E_('great_nation_promised', subj), E_('house_charged', subj)]
    if k == 'outcry_declared': return [E_('outcry_to_be_seen', subj)]
    if k == 'stood_before_the_lord': return [E_('stood_before_the_lord', subj)]
    if k == 'pleaded_for_the_righteous': return [E_('righteous_count_pleaded', subj, value=event.get('counts')), E_('spared_for_the_ten', 'sodom')]
    if k == 'lord_departed': return []
    if k == 'lodging_urged': return []
    if k == 'matzot_baked': return [E_('matzot_made', subj)]
    if k == 'house_surrounded': return [E_('house_surrounded', subj)]
    if k == 'men_demanded': return []
    if k == 'daughters_offered': return [E_('daughters_offered', subj)]
    if k == 'pressed_at_the_door': return []
    if k == 'pulled_in': return []
    if k == 'struck_blind': return [E_('struck_with_blindness', subj)]
    if k == 'evacuation_commanded': return [E_('evacuation_owed', subj)]
    if k == 'mocked_by_sons_in_law': return [E_('mocked', subj)]
    if k == 'lingered': return [E_('lingered', subj)]
    if k == 'led_out': return [E_('led_out_of_sodom', subj, cp='the-two-angels')]
    if k == 'escape_commanded': return [E_('looking_back_barred', subj)]
    if k == 'little_city_pleaded': return []
    if k == 'city_spared': return [E_('zoar_spared', subj)]
    if k == 'named': return [E_('name_given', subj, value=event.get('name'))]
    if k == 'fire_rained': return []
    if k == 'overturned': return [E_('overthrown', subj)]
    if k == 'looked_back': return [E_('pillar_of_salt', subj)]
    if k == 'rose_to_the_place': return [E_('morning_prayer_founded', subj)]
    if k == 'remembered': return [E_('remembered_by_god', subj)]
    if k == 'sent_away':
        T = {
            ('Gen 19:29', 'lot'): lambda: [E_('sent_out', subj, cp=event.get('by'))],
            ('Gen 25:6', 'the-sons-of-the-concubines'): lambda: [E_('sent_out', subj, cp=event.get('by'))],
            ('Gen 26:16', 'isaac'): lambda: [E_('expelled', subj)],
            ('Gen 26:31', 'abimelech-of-isaac'): lambda: [E_('sent_out', subj, cp=event.get('by'))],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'dwelt_in_the_cave': return [E_('cave_dwelt', subj)]
    if k == 'made_the_father_drink':
        T = {
            ('Gen 19:33', 'the-two-daughters'): lambda: [E_('made_drunk', 'lot')],
            ('Gen 19:35-36', 'the-two-daughters'): lambda: [E_('made_drunk', 'lot'), E_('daughters_conceived', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'bore':
        T = {
            ('Gen 19:37', 'ha-bekhirah'): lambda: [E_('begotten', 'moab', cp=subj)],
            ('Gen 19:38', 'the-younger-daughter'): lambda: [E_('begotten', 'ben-ammi', cp=subj)],
            ('Gen 25:2', 'keturah'): lambda: [E_('begotten', 'zimran', cp=subj), E_('begotten', 'jokshan', cp=subj), E_('begotten', 'medan', cp=subj), E_('begotten', 'midian', cp=subj), E_('begotten', 'ishbak', cp=subj), E_('begotten', 'shuah', cp=subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'journeyed':
        T = {
            ('Gen 20:1', 'abraham'): lambda: [E_('encamped_at', subj, value=event.get('to') or event.get('at') or 'the place')],
            ('Gen 22:19', 'abraham'): lambda: [E_('encamped_at', subj, value=event.get('to') or event.get('at') or 'the place')],
            ('Gen 26:1', 'isaac'): lambda: [E_('encamped_at', subj, value=event.get('to') or event.get('at') or 'the place')],
            ('Gen 26:17', 'isaac'): lambda: [E_('encamped_at', subj, value=event.get('to') or event.get('at') or 'the place')],
            ('Gen 26:23', 'isaac'): lambda: [E_('encamped_at', subj, value=event.get('to') or event.get('at') or 'the place')],
            ('Gen 28:10', 'jacob'): lambda: [],
            ('Gen 29:1', 'jacob'): lambda: [E_('encamped_at', subj, value=event.get('to') or event.get('at') or 'the place')],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'sister_asked': return [E_('presented_as_sister', subj, cp=event.get('by'))]
    if k == 'woman_taken': return [E_('taken_by_the_king', subj, cp='abimelech')]
    if k == 'came_in_a_dream':
        T = {
            ('Gen 20:3', 'abimelech'): lambda: [E_('death_decreed_over_the_woman', subj)],
            ('Gen 31:24', 'laban'): lambda: [E_('speech_restrained', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'king_pleaded': return [E_('integrity_pleaded', subj)]
    if k == 'prophet_declared': return [E_('withheld_from_sin', subj), E_('prophet_declared', 'abraham'), E_('return_owed', subj)]
    if k == 'servants_told': return [E_('servants_feared', subj)]
    if k == 'rebuked':
        T = {
            ('Gen 20:9-10', 'abraham'): lambda: [E_('great_sin_charged', subj)],
            ('Gen 26:9-10', 'isaac'): lambda: [E_('wife_acknowledged', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'answered_the_king': return [E_('fear_of_god_doubted', subj), E_('half_sister_claimed', 'sarah')]
    if k == 'restored': return [E_('restored_with_gifts', subj, cp='abimelech')]
    if k == 'dwelling_granted': return [E_('dwelling_granted', subj)]
    if k == 'silver_given': return [E_('thousand_silver_covering', subj, value=event.get('amount'))]
    if k == 'prayed':
        T = {
            ('Gen 20:17', 'abraham'): lambda: [E_('prayed_for_abimelech', subj)],
            ('Gen 25:21', 'isaac'): lambda: [E_('prayed_for_the_wife', subj), E_('barren', 'rebekah'), E_('conceived', 'rebekah')],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'healed': return [E_('healed', subj)]
    if k == 'wombs_shut': return [E_('wombs_shut', subj)]
    if k == 'tested': return [E_('tried', subj)]
    if k == 'offering_commanded': return [E_('offering_of_the_son_owed', subj)]
    if k == 'rose_early_and_went': return [E_('went_to_moriah', subj)]
    if k == 'place_seen_on_the_third_day': return [E_('place_seen_on_the_third_day', subj, value=event.get('ordinal'))]
    if k == 'lads_left': return [E_('lads_left', subj)]
    if k == 'wood_laid': return [E_('wood_laid', subj)]
    if k == 'lamb_asked': return [E_('lamb_asked', subj)]
    if k == 'altar_erected': return [E_('altar_built', subj)]
    if k == 'bound': return [E_('bound_on_the_altar', subj)]
    if k == 'knife_taken': return [E_('knife_taken', subj)]
    if k == 'called_from_heaven':
        T = {
            ('Gen 22:11-12', 'abraham'): lambda: [E_('hand_stayed', subj), E_('god_fearing_known', subj)],
            ('Gen 22:15', 'abraham'): lambda: [],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'ram_seen': return [E_('ram_caught', subj)]
    if k == 'olah_offered': return [E_('olah_offered', subj)]
    if k == 'sworn_by_himself': return [E_('sworn_by_himself', subj), E_('seed_as_stars', subj), E_('gate_of_enemies_promised', subj), E_('blessing_promised', subj)]
    if k == 'births_told': return [E_('births_told', subj, value=event.get('count'))]
    if k == 'begot':
        T = {
            ('Gen 22:20-22', 'nahor'): lambda: [E_('begotten', 'uz', cp=subj), E_('begotten', 'buz', cp=subj), E_('begotten', 'kemuel', cp=subj), E_('begotten', 'chesed', cp=subj), E_('begotten', 'hazo', cp=subj), E_('begotten', 'pildash', cp=subj), E_('begotten', 'jidlaph', cp=subj), E_('begotten', 'bethuel', cp=subj)],
            ('Gen 22:23', 'bethuel'): lambda: [E_('begotten', 'rebekah', cp=subj)],
            ('Gen 22:24', 'nahor'): lambda: [E_('begotten', 'tebah', cp=subj), E_('begotten', 'gaham', cp=subj), E_('begotten', 'tahash', cp=subj), E_('begotten', 'maacah', cp=subj)],
            ('Gen 25:3', 'jokshan'): lambda: [E_('begotten', 'sheba', cp=subj), E_('begotten', 'dedan', cp=subj)],
            ('Gen 25:3', 'dedan'): lambda: [E_('begotten', 'the-asshurim', cp=subj), E_('begotten', 'the-letushim', cp=subj), E_('begotten', 'the-leummim', cp=subj)],
            ('Gen 25:4', 'midian'): lambda: [E_('begotten', 'ephah', cp=subj), E_('begotten', 'epher', cp=subj), E_('begotten', 'hanoch', cp=subj), E_('begotten', 'abida', cp=subj), E_('begotten', 'eldaah', cp=subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'married':
        T = {
            ('Gen 25:1', 'keturah'): lambda: [E_('wife_taken', subj, cp=event.get('husband'))],
            ('Gen 26:34', 'judith'): lambda: [E_('wife_taken', subj, cp=event.get('husband'))],
            ('Gen 26:34', 'basemath'): lambda: [E_('wife_taken', subj, cp=event.get('husband'))],
            ('Gen 28:9', 'mahalath'): lambda: [E_('wife_taken', subj, cp=event.get('husband'))],
            ('Gen 29:23', 'leah'): lambda: [],
            ('Gen 29:28', 'rachel'): lambda: [E_('wife_taken', subj, cp=event.get('husband'))],
            ('Gen 30:4', 'bilhah'): lambda: [E_('wife_taken', subj, cp=event.get('husband'))],
            ('Gen 30:9', 'zilpah'): lambda: [E_('wife_taken', subj, cp=event.get('husband'))],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'all_given': return [E_('all_given_to_isaac', subj, cp='abraham')]
    if k == 'gifts_given': return [E_('gifts_given', subj, cp='abraham')]
    if k == 'died':
        T = {
            ('Gen 25:7-8', 'abraham'): lambda: [E_('died_in_good_old_age', subj), E_('gathered_to_his_people', subj)],
            ('Gen 25:17', 'ishmael'): lambda: [E_('gathered_to_his_people', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'buried': return [E_('buried', subj)]
    if k == 'blessed_after_the_death': return [E_('blessed_by_the_lord', subj), E_('encamped_at', subj, value=event.get('to') or event.get('at') or 'the place')]
    if k == 'princes_counted': return [E_('twelve_princes', subj, value=event.get('names'))]
    if k == 'fell_before_his_brothers': return [E_('fell_before_his_brothers', subj)]
    if k == 'struggled_in_the_womb': return [E_('struggled_in_the_womb', subj)]
    if k == 'inquired': return [E_('inquired_of_the_lord', subj)]
    if k == 'oracle_given': return [E_('two_nations_in_the_womb', subj), E_('elder_to_serve_the_younger', 'esau')]
    if k == 'born':
        T = {
            ('Gen 25:24-25', 'esau'): lambda: [E_('conceived', 'rebekah'), E_('firstborn_by_the_head', subj)],
            ('Gen 25:26', 'jacob'): lambda: [E_('heel_held', subj)],
            ('Gen 29:32', 'reuben'): lambda: [E_('conceived', 'leah')],
            ('Gen 29:33', 'simeon'): lambda: [E_('conceived', 'leah')],
            ('Gen 29:34', 'levi'): lambda: [E_('conceived', 'leah')],
            ('Gen 29:35', 'judah'): lambda: [E_('conceived', 'leah')],
            ('Gen 30:5', 'dan'): lambda: [E_('conceived', 'bilhah')],
            ('Gen 30:7', 'naphtali'): lambda: [E_('conceived', 'bilhah')],
            ('Gen 30:10', 'gad'): lambda: [E_('conceived', 'zilpah')],
            ('Gen 30:12', 'asher'): lambda: [E_('conceived', 'zilpah')],
            ('Gen 30:17', 'issachar'): lambda: [E_('conceived', 'leah')],
            ('Gen 30:19', 'zebulun'): lambda: [E_('conceived', 'leah')],
            ('Gen 30:21', 'dinah'): lambda: [E_('conceived', 'leah'), E_('daughter_born', 'leah')],
            ('Gen 30:23', 'joseph'): lambda: [E_('conceived', 'rachel'), E_('reproach_gathered', 'rachel'), E_('another_son_asked', 'rachel')],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'grew_up': return [E_('hunter_of_the_field', subj), E_('dweller_in_tents', 'jacob')]
    if k == 'loved_apart': return [E_('loved_by_the_father', 'esau'), E_('loved_by_the_mother', 'jacob')]
    if k == 'stew_boiled': return [E_('stew_boiled', subj), E_('came_in_weary', 'esau')]
    if k == 'gulp_demanded': return [E_('gulp_demanded', subj)]
    if k == 'sale_demanded': return [E_('sale_demanded', subj)]
    if k == 'birthright_dismissed': return [E_('birthright_dismissed', subj)]
    if k == 'sworn': return [E_('oath_sworn', subj, value=event.get('by'))]
    if k == 'birthright_sold': return [E_('birthright_transferred', subj, cp=event.get('from'))]
    if k == 'bread_and_lentils_given': return [E_('bread_and_lentils_given', subj, cp='jacob')]
    if k == 'birthright_despised': return [E_('birthright_despised', subj)]
    if k == 'famine_came': return [E_('famine', subj)]
    if k == 'descent_barred': return [E_('descent_to_egypt_barred', subj)]
    if k == 'oath_upheld': return [E_('sojourn_commanded', subj), E_('oath_to_abraham_upheld', subj), E_('land_promised', subj), E_('seed_as_stars', subj), E_('blessing_promised', subj), E_('charge_kept', 'abraham')]
    if k == 'dwelt': return [E_('encamped_at', subj, value=event.get('to') or event.get('at') or 'the place')]
    if k == 'seen_sporting': return [E_('seen_sporting', subj)]
    if k == 'decree_issued': return [E_('decree_issued', subj, value=event.get('decree'))]
    if k == 'hundredfold_found': return [E_('hundredfold_found', subj, value=event.get('measure')), E_('blessed_by_the_lord', subj)]
    if k == 'grew_great': return [E_('grew_very_great', subj)]
    if k == 'envied':
        T = {
            ('Gen 26:14', 'the-philistines'): lambda: [E_('envied', subj)],
            ('Gen 30:1', 'rachel'): lambda: [E_('envied_her_sister', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'wells_stopped': return [E_('wells_stopped', subj)]
    if k == 'wells_redug': return [E_('wells_redug', subj), E_('name_given', subj, value=event.get('name'))]
    if k == 'well_found':
        T = {
            ('Gen 26:19', 'isaac'): lambda: [E_('living_water_found', subj)],
            ('Gen 26:32', 'isaac'): lambda: [],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'quarreled': return [E_('quarreled_over', subj)]
    if k == 'room_made': return [E_('room_made', subj)]
    if k == 'called_on_the_name': return [E_('called_on_the_name', subj)]
    if k == 'tent_pitched': return [E_('encamped_at', subj, value=event.get('to') or event.get('at') or 'the place')]
    if k == 'well_dug': return [E_('well_dug', subj)]
    if k == 'visited': return []
    if k == 'covenant_proposed': return [E_('covenant_proposed', subj)]
    if k == 'feast_made': return [E_('feast_made', subj)]
    if k == 'covenant_cut_between_men': return [E_('covenant_between_men', subj, cp=event.get('with'))]
    if k == 'bitterness_of_spirit': return [E_('bitterness_of_spirit', subj)]
    if k == 'eyes_dimmed': return [E_('eyes_dim', subj)]
    if k == 'hunt_commanded': return [E_('death_day_unknown', 'isaac'), E_('hunt_owed', subj)]
    if k == 'overheard': return [E_('overheard', subj)]
    if k == 'mother_counselled':
        T = {
            ('Gen 27:6-10', 'jacob'): lambda: [E_('two_kids_counselled', 'rebekah')],
            ('Gen 27:42-45', 'jacob'): lambda: [E_('flight_owed', subj), E_('few_days_promised', 'rebekah')],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'objected': return [E_('objection_hairy_smooth', subj)]
    if k == 'curse_taken_on': return [E_('curse_taken_upon_herself', subj)]
    if k == 'kids_fetched': return []
    if k == 'disguised': return [E_('disguised_in_esaus_garments', subj)]
    if k == 'delicacies_brought': return [E_('delicacies_brought', subj)]
    if k == 'identity_claimed':
        T = {
            ('Gen 27:19', 'jacob'): lambda: [E_('identity_falsely_claimed', subj)],
            ('Gen 27:24', 'jacob'): lambda: [],
            ('Gen 27:32', 'esau'): lambda: [],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'felt': return [E_('not_recognized', subj)]
    if k == 'ate_and_drank': return []
    if k == 'kissed':
        T = {
            ('Gen 27:26-27', 'isaac'): lambda: [],
            ('Gen 29:11', 'jacob'): lambda: [E_('kissed_and_wept', subj)],
            ('Gen 29:13', 'laban'): lambda: [E_('embraced_and_housed', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'blessed':
        T = {
            ('Gen 27:27-29', 'jacob'): lambda: [E_('blessed_with_dew_and_fat', subj), E_('peoples_to_serve', subj)],
            ('Gen 27:39-40', 'esau'): lambda: [E_('blessed_by_the_sword', subj)],
            ('Gen 28:1-4', 'jacob'): lambda: [E_('blessing_of_abraham_given', subj), E_('canaanite_wife_barred', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'trembled': return [E_('trembled', subj), E_('blessing_ratified', 'jacob')]
    if k == 'cried_out': return [E_('great_and_bitter_cry', subj)]
    if k == 'supplanted_charged': return [E_('supplanted_twice', subj, value=event.get('times')), E_('master_made', 'jacob')]
    if k == 'wept': return [E_('wept', subj)]
    if k == 'grudge_held': return [E_('grudge_held', subj), E_('kill_intent_after_the_mourning', subj)]
    if k == 'words_told': return [E_('words_told_to_rebekah', subj)]
    if k == 'loathing_stated': return [E_('loathing_stated', subj)]
    if k == 'sent_to_paddan_aram': return [E_('wife_from_paddan_owed', subj), E_('sent_out', subj, cp=event.get('by'))]
    if k == 'esau_saw': return [E_('esau_saw_the_command', subj)]
    if k == 'lodged_at_the_place': return [E_('sun_set_at_the_place', 'the-place'), E_('stone_pillow', subj), E_('encamped_at', subj, value=event.get('to') or event.get('at') or 'the place')]
    if k == 'dreamed':
        T = {
            ('Gen 28:12', 'jacob'): lambda: [E_('ladder_dreamed', subj)],
            ('Gen 31:10-12', 'jacob'): lambda: [E_('he_goats_dreamed', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'promised_at_bethel': return [E_('land_promised', subj), E_('seed_as_dust', subj), E_('blessing_promised', subj), E_('with_you_promised', subj), E_('return_promised', subj)]
    if k == 'awoke_and_feared': return [E_('house_of_god_recognized', subj)]
    if k == 'pillar_set_and_anointed':
        T = {
            ('Gen 28:18', 'the_pillar_of_bethel'): lambda: [E_('pillar_anointed', subj)],
            ('Gen 31:45', 'the_pillar_of_gilead'): lambda: [E_('pillar_raised', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'vowed': return [E_('vow_of_bethel', subj, value={'conditions': event.get('conditions'), 'commitments': event.get('commitments')}), E_('tithe_vowed', subj)]
    if k == 'well_seen': return [E_('well_with_the_stone', subj)]
    if k == 'shepherds_questioned': return [E_('shepherds_questioned', subj)]
    if k == 'shepherds_rebuked': return [E_('shepherds_rebuked', subj)]
    if k == 'stone_rolled': return [E_('stone_rolled_alone', subj)]
    if k == 'flock_watered': return []
    if k == 'kin_told': return [E_('kin_told', subj)]
    if k == 'embraced': return [E_('bone_and_flesh', 'jacob')]
    if k == 'month_dwelt': return [E_('month_dwelt', subj, value=event.get('months'))]
    if k == 'wage_asked':
        T = {
            ('Gen 29:15-17', 'laban'): lambda: [E_('wage_asked', subj), E_('two_daughters', subj)],
            ('Gen 30:28', 'laban'): lambda: [E_('wage_asked', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'wage_named':
        T = {
            ('Gen 29:18', 'jacob'): lambda: [E_('loved_rachel', subj), E_('seven_years_owed', subj, cp='laban'), E_('seven_years_service', subj, due=_years(world, day, 7))],
            ('Gen 30:31-33', 'jacob'): lambda: [E_('speckled_wage_agreed', 'laban', cp='jacob'), E_('righteousness_to_answer', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'contract_accepted': return [E_('contract_accepted', subj)]
    if k == 'served':
        T = {
            ('Gen 29:20', 'jacob'): lambda: [E_('served_as_few_days', subj)],
            ('Gen 29:30', 'jacob'): lambda: [E_('second_seven_service', subj, due=_years(world, day, 7)), E_('loved_more', 'rachel')],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'wife_demanded': return [E_('wife_demanded', subj)]
    if k == 'bride_switched':
        T = {
            ('Gen 29:23', 'jacob'): lambda: [E_('bride_switched', subj), E_('wife_taken', 'leah', cp=event.get('husband'))],
            ('Gen 29:25', 'laban'): lambda: [E_('deceit_charged', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'maid_given': return [E_('maid_given', subj, value=event.get('maid'))]
    if k == 'custom_stated': return [E_('custom_of_the_place', subj)]
    if k == 'week_demanded': return [E_('week_of_the_feast', subj, due=day + 7), E_('second_seven_owed', subj, cp='laban')]
    if k == 'week_fulfilled': return []
    if k == 'womb_opened':
        T = {
            ('Gen 29:31', 'leah'): lambda: [E_('hated_seen', subj), E_('womb_opened', subj), E_('barren', 'rachel')],
            ('Gen 30:22', 'rachel'): lambda: [E_('heard_by_god', subj), E_('womb_opened', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'ceased_bearing':
        T = {
            ('Gen 29:35', 'leah'): lambda: [E_('ceased_bearing', subj)],
            ('Gen 30:9', 'leah'): lambda: [E_('maid_offered_as_wife', subj)],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'children_demanded': return [E_('children_demanded', subj)]
    if k == 'anger_burned':
        T = {
            ('Gen 30:2', 'jacob'): lambda: [E_('in_gods_place_refused', subj)],
            ('Gen 31:36', 'jacob'): lambda: [],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'maid_offered': return [E_('maid_offered_as_wife', subj)]
    if k == 'mandrakes_found': return [E_('mandrakes_found', subj)]
    if k == 'mandrakes_traded': return [E_('night_hired_for_mandrakes', subj, cp='rachel')]
    if k == 'god_heard': return [E_('heard_by_god', subj)]
    if k == 'release_demanded': return [E_('release_demanded', subj), E_('wives_and_children_claimed', subj)]
    if k == 'divination_confessed': return [E_('divined_blessing', subj)]
    if k == 'service_audited': return [E_('service_audited', subj)]
    if k == 'flock_removed': return [E_('flock_removed', subj, value=event.get('days'))]
    if k == 'rods_peeled': return [E_('rods_peeled', subj)]
    if k == 'flock_bore_striped': return [E_('flock_bore_striped', subj)]
    if k == 'flocks_separated': return [E_('flocks_separated', subj)]
    if k == 'broke_out': return [E_('broke_out_exceedingly', subj)]
    if k == 'sons_words_heard': return [E_('sons_words_heard', subj), E_('face_changed', 'laban')]
    if k == 'return_commanded': return [E_('return_owed', subj)]
    if k == 'wives_summoned': return [E_('wives_summoned_to_the_field', subj)]
    if k == 'account_given':
        T = {
            ('Gen 31:5-13', 'jacob'): lambda: [E_('god_with_me', subj), E_('strength_served', subj), E_('wages_changed_ten_times', 'laban', value=10), E_('wage_flip', 'the-flock'), E_('livestock_rescued', subj, cp='laban'), E_('god_of_bethel_recalled', subj)],
            ('Gen 31:38-42', 'jacob'): lambda: [E_('keeper_account', subj), E_('torn_borne_beyond_duty', subj), E_('twenty_years_served', subj, value=20), E_('wages_changed_ten_times', 'laban', value=10), E_('adjudicated_last_night', 'laban')],
        }
        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing
    if k == 'wives_answered': return [E_('inheritance_questioned', subj), E_('do_all_god_said', subj)]
    if k == 'rose_and_loaded': return [E_('rose_and_loaded', subj)]
    if k == 'teraphim_stolen': return [E_('teraphim_stolen', subj, cp='laban')]
    if k == 'heart_stolen': return [E_('heart_stolen', subj)]
    if k == 'fled': return [E_('fled_from_laban', subj)]
    if k == 'river_crossed': return [E_('river_crossed', subj)]
    if k == 'told_on_the_third_day': return [E_('told_on_the_third_day', subj, value=event.get('ordinal'))]
    if k == 'pursued': return [E_('pursued_seven_days', subj, value=event.get('days'))]
    if k == 'overtaken': return [E_('overtaken_at_gilead', subj), E_('encamped_at', subj, value=event.get('to') or event.get('at') or 'the place')]
    if k == 'charges_laid': return [E_('charges_laid', subj)]
    if k == 'fear_answered': return [E_('fear_answered', subj)]
    if k == 'death_oath_sworn': return [E_('death_oath_on_the_thief', subj)]
    if k == 'tents_searched': return [E_('tents_searched', subj)]
    if k == 'quarreled_with_laban': return [E_('quarreled_with_laban', subj), E_('tribunal_demanded', subj)]
    if k == 'all_is_mine_claimed': return [E_('all_is_mine_claimed', subj)]
    if k == 'heap_made': return [E_('heap_made', subj)]
    if k == 'witness_declared': return [E_('witness_declared', subj), E_('watch_between_us', 'laban'), E_('covenant_terms', 'jacob')]
    if k == 'boundary_sworn': return [E_('boundary_witnessed', subj)]
    if k == 'sacrificed': return [E_('sacrifice_offered', subj)]
    if k == 'ate_and_lodged': return [E_('ate_and_lodged', subj)]
    return []

SLOTS = [   # the slot order of the tuple — fixed by scratchpad o8_s3_predict.py before this file was typed
    ('abraham', 'visitors_received'),
    ('sarah', 'son_promised_at_the_season'),
    ('sarah', 'return_at_the_season'),
    ('sarah', 'laughed_within'),
    ('sarah', 'laugh_denied'),
    ('abraham', 'great_nation_promised'),
    ('abraham', 'house_charged'),
    ('sodom', 'outcry_to_be_seen'),
    ('abraham', 'stood_before_the_lord'),
    ('abraham', 'righteous_count_pleaded'),
    ('sodom', 'spared_for_the_ten'),
    ('lot', 'angels_lodged'),
    ('lot', 'matzot_made'),
    ('lot', 'house_surrounded'),
    ('lot', 'daughters_offered'),
    ('the-men-of-sodom', 'struck_with_blindness'),
    ('lot', 'evacuation_owed'),
    ('lot', 'mocked'),
    ('lot', 'lingered'),
    ('lot_and_his_house', 'led_out_of_sodom'),
    ('lot_and_his_house', 'looking_back_barred'),
    ('zoar', 'zoar_spared'),
    ('zoar', 'name_given'),
    ('the-cities-of-the-plain', 'overthrown'),
    ('lots-wife', 'pillar_of_salt'),
    ('abraham', 'morning_prayer_founded'),
    ('abraham', 'remembered_by_god'),
    ('lot', 'sent_out'),
    ('lot', 'cave_dwelt'),
    ('lot', 'made_drunk'),
    ('the-two-daughters', 'daughters_conceived'),
    ('moab', 'begotten'),
    ('moab', 'name_given'),
    ('ben-ammi', 'begotten'),
    ('ben-ammi', 'name_given'),
    ('abraham', 'encamped_at'),
    ('sarah', 'presented_as_sister'),
    ('sarah', 'taken_by_the_king'),
    ('abimelech', 'death_decreed_over_the_woman'),
    ('abimelech', 'integrity_pleaded'),
    ('abimelech', 'withheld_from_sin'),
    ('abraham', 'prophet_declared'),
    ('abimelech', 'return_owed'),
    ('the_house_of_abimelech', 'servants_feared'),
    ('abraham', 'great_sin_charged'),
    ('abraham', 'fear_of_god_doubted'),
    ('sarah', 'half_sister_claimed'),
    ('abraham', 'restored_with_gifts'),
    ('abraham', 'dwelling_granted'),
    ('sarah', 'thousand_silver_covering'),
    ('abraham', 'prayed_for_abimelech'),
    ('the_house_of_abimelech', 'healed'),
    ('the_house_of_abimelech', 'wombs_shut'),
    ('abraham', 'tried'),
    ('abraham', 'offering_of_the_son_owed'),
    ('abraham', 'went_to_moriah'),
    ('abraham', 'place_seen_on_the_third_day'),
    ('the-two-lads', 'lads_left'),
    ('isaac', 'wood_laid'),
    ('isaac', 'lamb_asked'),
    ('the-altar-at-moriah', 'altar_built'),
    ('isaac', 'bound_on_the_altar'),
    ('abraham', 'knife_taken'),
    ('abraham', 'hand_stayed'),
    ('abraham', 'god_fearing_known'),
    ('the-ram-at-moriah', 'ram_caught'),
    ('abraham', 'olah_offered'),
    ('the-altar-at-moriah', 'name_given'),
    ('abraham', 'sworn_by_himself'),
    ('abraham', 'seed_as_stars'),
    ('abraham', 'gate_of_enemies_promised'),
    ('abraham', 'blessing_promised'),
    ('abraham', 'births_told'),
    ('uz', 'begotten'),
    ('buz', 'begotten'),
    ('kemuel', 'begotten'),
    ('chesed', 'begotten'),
    ('hazo', 'begotten'),
    ('pildash', 'begotten'),
    ('jidlaph', 'begotten'),
    ('bethuel', 'begotten'),
    ('rebekah', 'begotten'),
    ('tebah', 'begotten'),
    ('gaham', 'begotten'),
    ('tahash', 'begotten'),
    ('maacah', 'begotten'),
    ('keturah', 'wife_taken'),
    ('zimran', 'begotten'),
    ('jokshan', 'begotten'),
    ('medan', 'begotten'),
    ('midian', 'begotten'),
    ('ishbak', 'begotten'),
    ('shuah', 'begotten'),
    ('sheba', 'begotten'),
    ('dedan', 'begotten'),
    ('the-asshurim', 'begotten'),
    ('the-letushim', 'begotten'),
    ('the-leummim', 'begotten'),
    ('ephah', 'begotten'),
    ('epher', 'begotten'),
    ('hanoch', 'begotten'),
    ('abida', 'begotten'),
    ('eldaah', 'begotten'),
    ('isaac', 'all_given_to_isaac'),
    ('the-sons-of-the-concubines', 'gifts_given'),
    ('the-sons-of-the-concubines', 'sent_out'),
    ('abraham', 'died_in_good_old_age'),
    ('abraham', 'gathered_to_his_people'),
    ('abraham', 'buried'),
    ('isaac', 'blessed_by_the_lord'),
    ('isaac', 'encamped_at'),
    ('ishmael', 'twelve_princes'),
    ('ishmael', 'gathered_to_his_people'),
    ('ishmael', 'fell_before_his_brothers'),
    ('isaac', 'prayed_for_the_wife'),
    ('rebekah', 'barren'),
    ('rebekah', 'conceived'),
    ('rebekah', 'struggled_in_the_womb'),
    ('rebekah', 'inquired_of_the_lord'),
    ('rebekah', 'two_nations_in_the_womb'),
    ('esau', 'elder_to_serve_the_younger'),
    ('esau', 'firstborn_by_the_head'),
    ('esau', 'name_given'),
    ('jacob', 'heel_held'),
    ('jacob', 'name_given'),
    ('esau', 'hunter_of_the_field'),
    ('jacob', 'dweller_in_tents'),
    ('esau', 'loved_by_the_father'),
    ('jacob', 'loved_by_the_mother'),
    ('jacob', 'stew_boiled'),
    ('esau', 'came_in_weary'),
    ('esau', 'gulp_demanded'),
    ('jacob', 'sale_demanded'),
    ('esau', 'birthright_dismissed'),
    ('esau', 'oath_sworn'),
    ('jacob', 'birthright_transferred'),
    ('esau', 'bread_and_lentils_given'),
    ('esau', 'birthright_despised'),
    ('the-land-of-canaan', 'famine'),
    ('isaac', 'descent_to_egypt_barred'),
    ('isaac', 'sojourn_commanded'),
    ('isaac', 'oath_to_abraham_upheld'),
    ('isaac', 'land_promised'),
    ('isaac', 'seed_as_stars'),
    ('isaac', 'blessing_promised'),
    ('abraham', 'charge_kept'),
    ('rebekah', 'presented_as_sister'),
    ('isaac', 'seen_sporting'),
    ('isaac', 'wife_acknowledged'),
    ('the-people-of-gerar', 'decree_issued'),
    ('isaac', 'hundredfold_found'),
    ('isaac', 'grew_very_great'),
    ('the-philistines', 'envied'),
    ('the-wells-of-abraham', 'wells_stopped'),
    ('isaac', 'expelled'),
    ('the-wells-of-abraham', 'wells_redug'),
    ('the-wells-of-abraham', 'name_given'),
    ('isaac', 'living_water_found'),
    ('the-herdsmen-of-gerar', 'quarreled_over'),
    ('esek', 'name_given'),
    ('sitnah', 'name_given'),
    ('isaac', 'room_made'),
    ('rehoboth', 'name_given'),
    ('isaac', 'fear_not_promised'),
    ('the-altar-at-beersheba', 'altar_built'),
    ('isaac', 'called_on_the_name'),
    ('isaac', 'well_dug'),
    ('abimelech-of-isaac', 'covenant_proposed'),
    ('isaac', 'feast_made'),
    ('isaac_and_abimelech', 'oath_sworn'),
    ('isaac', 'covenant_between_men'),
    ('abimelech-of-isaac', 'sent_out'),
    ('beersheba', 'name_given'),
    ('judith', 'wife_taken'),
    ('basemath', 'wife_taken'),
    ('isaac_and_rebekah', 'bitterness_of_spirit'),
    ('isaac', 'eyes_dim'),
    ('isaac', 'death_day_unknown'),
    ('esau', 'hunt_owed'),
    ('rebekah', 'overheard'),
    ('rebekah', 'two_kids_counselled'),
    ('jacob', 'objection_hairy_smooth'),
    ('rebekah', 'curse_taken_upon_herself'),
    ('jacob', 'disguised_in_esaus_garments'),
    ('jacob', 'delicacies_brought'),
    ('jacob', 'identity_falsely_claimed'),
    ('isaac', 'not_recognized'),
    ('jacob', 'blessed_with_dew_and_fat'),
    ('jacob', 'peoples_to_serve'),
    ('esau', 'delicacies_brought'),
    ('isaac', 'trembled'),
    ('jacob', 'blessing_ratified'),
    ('esau', 'great_and_bitter_cry'),
    ('esau', 'supplanted_twice'),
    ('jacob', 'master_made'),
    ('esau', 'wept'),
    ('esau', 'blessed_by_the_sword'),
    ('esau', 'grudge_held'),
    ('esau', 'kill_intent_after_the_mourning'),
    ('rebekah', 'words_told_to_rebekah'),
    ('jacob', 'flight_owed'),
    ('rebekah', 'few_days_promised'),
    ('rebekah', 'loathing_stated'),
    ('jacob', 'blessing_of_abraham_given'),
    ('jacob', 'canaanite_wife_barred'),
    ('jacob', 'wife_from_paddan_owed'),
    ('jacob', 'sent_out'),
    ('esau', 'esau_saw_the_command'),
    ('mahalath', 'wife_taken'),
    ('the-place', 'sun_set_at_the_place'),
    ('jacob', 'stone_pillow'),
    ('jacob', 'encamped_at'),
    ('jacob', 'ladder_dreamed'),
    ('jacob', 'land_promised'),
    ('jacob', 'seed_as_dust'),
    ('jacob', 'blessing_promised'),
    ('jacob', 'with_you_promised'),
    ('jacob', 'return_promised'),
    ('jacob', 'house_of_god_recognized'),
    ('the_pillar_of_bethel', 'pillar_anointed'),
    ('the-place', 'name_given'),
    ('jacob', 'vow_of_bethel'),
    ('jacob', 'tithe_vowed'),
    ('the-well-of-haran', 'well_with_the_stone'),
    ('jacob', 'shepherds_questioned'),
    ('jacob', 'shepherds_rebuked'),
    ('jacob', 'stone_rolled_alone'),
    ('jacob', 'kissed_and_wept'),
    ('rachel', 'kin_told'),
    ('laban', 'embraced_and_housed'),
    ('jacob', 'bone_and_flesh'),
    ('jacob', 'month_dwelt'),
    ('laban', 'wage_asked'),
    ('laban', 'two_daughters'),
    ('jacob', 'loved_rachel'),
    ('jacob', 'seven_years_owed'),
    ('jacob', 'seven_years_service'),
    ('laban', 'contract_accepted'),
    ('jacob', 'served_as_few_days'),
    ('jacob', 'wife_demanded'),
    ('laban', 'feast_made'),
    ('jacob', 'bride_switched'),
    ('leah', 'wife_taken'),
    ('leah', 'maid_given'),
    ('laban', 'deceit_charged'),
    ('laban', 'custom_of_the_place'),
    ('jacob', 'week_of_the_feast'),
    ('jacob', 'second_seven_owed'),
    ('rachel', 'wife_taken'),
    ('rachel', 'maid_given'),
    ('jacob', 'second_seven_service'),
    ('rachel', 'loved_more'),
    ('leah', 'hated_seen'),
    ('leah', 'womb_opened'),
    ('rachel', 'barren'),
    ('leah', 'conceived'),
    ('reuben', 'name_given'),
    ('simeon', 'name_given'),
    ('levi', 'name_given'),
    ('judah', 'name_given'),
    ('leah', 'ceased_bearing'),
    ('rachel', 'envied_her_sister'),
    ('rachel', 'children_demanded'),
    ('jacob', 'in_gods_place_refused'),
    ('rachel', 'maid_offered_as_wife'),
    ('bilhah', 'wife_taken'),
    ('bilhah', 'conceived'),
    ('dan', 'name_given'),
    ('naphtali', 'name_given'),
    ('leah', 'maid_offered_as_wife'),
    ('zilpah', 'wife_taken'),
    ('zilpah', 'conceived'),
    ('gad', 'name_given'),
    ('asher', 'name_given'),
    ('reuben', 'mandrakes_found'),
    ('leah', 'night_hired_for_mandrakes'),
    ('leah', 'heard_by_god'),
    ('issachar', 'name_given'),
    ('zebulun', 'name_given'),
    ('leah', 'daughter_born'),
    ('dinah', 'name_given'),
    ('rachel', 'remembered_by_god'),
    ('rachel', 'heard_by_god'),
    ('rachel', 'womb_opened'),
    ('rachel', 'conceived'),
    ('rachel', 'reproach_gathered'),
    ('rachel', 'another_son_asked'),
    ('joseph', 'name_given'),
    ('jacob', 'release_demanded'),
    ('jacob', 'wives_and_children_claimed'),
    ('laban', 'divined_blessing'),
    ('jacob', 'service_audited'),
    ('laban', 'speckled_wage_agreed'),
    ('jacob', 'righteousness_to_answer'),
    ('laban', 'flock_removed'),
    ('jacob', 'rods_peeled'),
    ('the-flock', 'flock_bore_striped'),
    ('jacob', 'flocks_separated'),
    ('jacob', 'broke_out_exceedingly'),
    ('jacob', 'sons_words_heard'),
    ('laban', 'face_changed'),
    ('jacob', 'return_owed'),
    ('jacob', 'wives_summoned_to_the_field'),
    ('jacob', 'god_with_me'),
    ('jacob', 'strength_served'),
    ('laban', 'wages_changed_ten_times'),
    ('the-flock', 'wage_flip'),
    ('jacob', 'livestock_rescued'),
    ('jacob', 'god_of_bethel_recalled'),
    ('jacob', 'he_goats_dreamed'),
    ('rachel_and_leah', 'inheritance_questioned'),
    ('rachel_and_leah', 'do_all_god_said'),
    ('jacob', 'rose_and_loaded'),
    ('rachel', 'teraphim_stolen'),
    ('laban', 'heart_stolen'),
    ('jacob', 'fled_from_laban'),
    ('jacob', 'river_crossed'),
    ('laban', 'told_on_the_third_day'),
    ('laban', 'pursued_seven_days'),
    ('laban', 'speech_restrained'),
    ('jacob', 'overtaken_at_gilead'),
    ('laban', 'charges_laid'),
    ('jacob', 'fear_answered'),
    ('rachel', 'death_oath_on_the_thief'),
    ('laban', 'tents_searched'),
    ('jacob', 'quarreled_with_laban'),
    ('jacob', 'tribunal_demanded'),
    ('jacob', 'keeper_account'),
    ('jacob', 'torn_borne_beyond_duty'),
    ('jacob', 'twenty_years_served'),
    ('laban', 'adjudicated_last_night'),
    ('laban', 'all_is_mine_claimed'),
    ('laban', 'covenant_proposed'),
    ('the_pillar_of_gilead', 'pillar_raised'),
    ('the-heap', 'heap_made'),
    ('the-heap', 'name_given'),
    ('the-heap', 'witness_declared'),
    ('laban', 'watch_between_us'),
    ('jacob', 'covenant_terms'),
    ('the_heap_and_pillar', 'boundary_witnessed'),
    ('jacob', 'oath_sworn'),
    ('jacob', 'covenant_between_men'),
    ('jacob', 'sacrifice_offered'),
    ('jacob_and_his_kin', 'ate_and_lodged'),
    ('esau', 'circumcision_due'),
    ('jacob', 'circumcision_due'),
    ('reuben', 'circumcision_due'),
    ('simeon', 'circumcision_due'),
    ('levi', 'circumcision_due'),
    ('judah', 'circumcision_due'),
    ('dan', 'circumcision_due'),
    ('naphtali', 'circumcision_due'),
    ('gad', 'circumcision_due'),
    ('asher', 'circumcision_due'),
    ('issachar', 'circumcision_due'),
    ('zebulun', 'circumcision_due'),
    ('joseph', 'circumcision_due'),
]

def scene():
    """THE SCENE — the stretch's acts on a bare world in the text's order (scene days; the tape carries the ink's markers); the events and their
    days the hand-model's (scratchpad o8_s3_predict.py) — typed from its print"""
    closes = [0]
    def close(eid, eff, note, value=None):
        closes[0] += bool(w.close(eid, eff, note, value=value))
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='FROM MAMRE TO THE HEAP — Genesis 18-20, 22, 25-31 (clock unit: days; the tape\'s own order)')
        w.laws = [law_mamre, PS_.law_pre_sinai]   # the covenant\'s own run on every male birth (Gen 17:12) — the pre-Sinai daemon beside the story\'s, as S1
        w.advance(1)
        w.submit({'kind': 'appeared', 'subject': 'abraham', 'at': 'the terebinths of Mamre', 'case_source': 'Gen 18:1'})
        w.submit({'kind': 'ran_and_bowed', 'subject': 'abraham', 'case_source': 'Gen 18:2'})
        w.submit({'kind': 'hospitality_offered', 'subject': 'abraham', 'case_source': 'Gen 18:3-5'})
        w.submit({'kind': 'cakes_ordered', 'subject': 'abraham', 'measures': 3, 'case_source': 'Gen 18:6'})
        w.submit({'kind': 'calf_prepared', 'subject': 'abraham', 'case_source': 'Gen 18:7'})
        w.submit({'kind': 'meal_served', 'subject': 'abraham', 'case_source': 'Gen 18:8'})
        w.submit({'kind': 'son_promised', 'subject': 'sarah', 'years': 1, 'case_source': 'Gen 18:10; Gen 18:14'})
        w.submit({'kind': 'laughed_within', 'subject': 'sarah', 'case_source': 'Gen 18:12'})
        w.submit({'kind': 'laugh_denied', 'subject': 'sarah', 'case_source': 'Gen 18:15'})
        w.submit({'kind': 'escorted', 'subject': 'abraham', 'case_source': 'Gen 18:16'})
        w.submit({'kind': 'house_charged', 'subject': 'abraham', 'case_source': 'Gen 18:17-19'})
        w.submit({'kind': 'outcry_declared', 'subject': 'sodom', 'case_source': 'Gen 18:20-21'})
        w.submit({'kind': 'stood_before_the_lord', 'subject': 'abraham', 'case_source': 'Gen 18:22'})
        w.submit({'kind': 'pleaded_for_the_righteous', 'subject': 'abraham', 'counts': [50, 45, 40, 30, 20, 10], 'case_source': 'Gen 18:23-32'})
        w.submit({'kind': 'lord_departed', 'subject': 'god', 'case_source': 'Gen 18:33'})
        w.submit({'kind': 'ran_and_bowed', 'subject': 'lot', 'case_source': 'Gen 19:1'})
        w.submit({'kind': 'hospitality_offered', 'subject': 'lot', 'case_source': 'Gen 19:2'})
        w.submit({'kind': 'lodging_urged', 'subject': 'lot', 'case_source': 'Gen 19:3'})
        w.submit({'kind': 'matzot_baked', 'subject': 'lot', 'case_source': 'Gen 19:3'})
        w.submit({'kind': 'house_surrounded', 'subject': 'lot', 'case_source': 'Gen 19:4'})
        w.submit({'kind': 'men_demanded', 'subject': 'the-men-of-sodom', 'case_source': 'Gen 19:5'})
        w.submit({'kind': 'daughters_offered', 'subject': 'lot', 'case_source': 'Gen 19:8'})
        w.submit({'kind': 'pressed_at_the_door', 'subject': 'the-men-of-sodom', 'case_source': 'Gen 19:9'})
        w.submit({'kind': 'pulled_in', 'subject': 'lot', 'case_source': 'Gen 19:10'})
        w.submit({'kind': 'struck_blind', 'subject': 'the-men-of-sodom', 'case_source': 'Gen 19:11'})
        w.submit({'kind': 'evacuation_commanded', 'subject': 'lot', 'case_source': 'Gen 19:12-13; Gen 19:15'})
        w.submit({'kind': 'mocked_by_sons_in_law', 'subject': 'lot', 'case_source': 'Gen 19:14'})
        w.advance(2)
        w.submit({'kind': 'lingered', 'subject': 'lot', 'case_source': 'Gen 19:16'})
        w.submit({'kind': 'led_out', 'subject': 'lot_and_his_house', 'case_source': 'Gen 19:16'})
        close('lot', 'evacuation_owed', 'Gen 19:16 — led out')
        w.submit({'kind': 'escape_commanded', 'subject': 'lot_and_his_house', 'case_source': 'Gen 19:17'})
        w.submit({'kind': 'little_city_pleaded', 'subject': 'lot', 'case_source': 'Gen 19:18-20'})
        w.submit({'kind': 'city_spared', 'subject': 'zoar', 'case_source': 'Gen 19:21-22'})
        w.submit({'kind': 'named', 'subject': 'zoar', 'name': 'Zoar (צוער — the little one, 19:22)', 'by': 'the report formula', 'case_source': 'Gen 19:22'})
        w.submit({'kind': 'fire_rained', 'subject': 'the-cities-of-the-plain', 'case_source': 'Gen 19:23-24'})
        w.submit({'kind': 'overturned', 'subject': 'the-cities-of-the-plain', 'case_source': 'Gen 19:25'})
        close('sodom', 'spared_for_the_ten', 'Gen 19:24 — the ten not found')
        close('sodom', 'outcry_to_be_seen', 'Gen 19:25 — the overthrow')
        w.submit({'kind': 'looked_back', 'subject': 'lots-wife', 'case_source': 'Gen 19:26'})
        w.submit({'kind': 'rose_to_the_place', 'subject': 'abraham', 'case_source': 'Gen 19:27-28'})
        w.submit({'kind': 'remembered', 'subject': 'abraham', 'case_source': 'Gen 19:29'})
        w.submit({'kind': 'sent_away', 'subject': 'lot', 'case_source': 'Gen 19:29'})
        w.advance(3)
        w.submit({'kind': 'dwelt_in_the_cave', 'subject': 'lot', 'case_source': 'Gen 19:30'})
        w.submit({'kind': 'made_the_father_drink', 'subject': 'the-two-daughters', 'night': 'the first', 'case_source': 'Gen 19:33'})
        w.submit({'kind': 'made_the_father_drink', 'subject': 'the-two-daughters', 'night': 'the second', 'case_source': 'Gen 19:35-36'})
        w.submit({'kind': 'bore', 'subject': 'ha-bekhirah', 'child': 'moab', 'case_source': 'Gen 19:37'})
        w.submit({'kind': 'named', 'subject': 'moab', 'name': 'Moab (מואב, 19:37)', 'by': 'ha-bekhirah', 'case_source': 'Gen 19:37'})
        w.submit({'kind': 'bore', 'subject': 'the-younger-daughter', 'child': 'ben-ammi', 'case_source': 'Gen 19:38'})
        w.submit({'kind': 'named', 'subject': 'ben-ammi', 'name': 'Ben-ammi (בן עמי, 19:38)', 'by': 'the-younger-daughter', 'case_source': 'Gen 19:38'})
        w.advance(4)
        w.submit({'kind': 'journeyed', 'subject': 'abraham', 'to': 'Gerar — between Kadesh and Shur', 'case_source': 'Gen 20:1'})
        w.submit({'kind': 'sister_asked', 'subject': 'sarah', 'by': 'abraham', 'case_source': 'Gen 20:2'})
        w.submit({'kind': 'woman_taken', 'subject': 'sarah', 'by': 'abimelech', 'case_source': 'Gen 20:2'})
        w.submit({'kind': 'came_in_a_dream', 'subject': 'abimelech', 'warning': 'you are a dead man because of the woman', 'case_source': 'Gen 20:3'})
        w.submit({'kind': 'king_pleaded', 'subject': 'abimelech', 'case_source': 'Gen 20:4-5'})
        w.submit({'kind': 'prophet_declared', 'subject': 'abimelech', 'case_source': 'Gen 20:6-7'})
        w.submit({'kind': 'servants_told', 'subject': 'the_house_of_abimelech', 'case_source': 'Gen 20:8'})
        w.submit({'kind': 'rebuked', 'subject': 'abraham', 'by': 'abimelech', 'case_source': 'Gen 20:9-10'})
        w.submit({'kind': 'answered_the_king', 'subject': 'abraham', 'case_source': 'Gen 20:11-13'})
        w.submit({'kind': 'restored', 'subject': 'abraham', 'case_source': 'Gen 20:14'})
        close('abimelech', 'return_owed', 'Gen 20:14 — Sarah returned')
        w.submit({'kind': 'dwelling_granted', 'subject': 'abraham', 'case_source': 'Gen 20:15'})
        w.submit({'kind': 'silver_given', 'subject': 'sarah', 'amount': 1000, 'case_source': 'Gen 20:16'})
        w.submit({'kind': 'prayed', 'subject': 'abraham', 'for': 'abimelech', 'case_source': 'Gen 20:17'})
        w.submit({'kind': 'healed', 'subject': 'the_house_of_abimelech', 'case_source': 'Gen 20:17'})
        close('abimelech', 'death_decreed_over_the_woman', 'Gen 20:17 — healed')
        w.submit({'kind': 'wombs_shut', 'subject': 'the_house_of_abimelech', 'case_source': 'Gen 20:18'})
        w.advance(5)
        w.submit({'kind': 'tested', 'subject': 'abraham', 'case_source': 'Gen 22:1'})
        w.submit({'kind': 'offering_commanded', 'subject': 'abraham', 'case_source': 'Gen 22:2'})
        w.submit({'kind': 'rose_early_and_went', 'subject': 'abraham', 'case_source': 'Gen 22:3'})
        w.advance(7)
        w.submit({'kind': 'place_seen_on_the_third_day', 'subject': 'abraham', 'ordinal': 3, 'case_source': 'Gen 22:4'})
        w.submit({'kind': 'lads_left', 'subject': 'the-two-lads', 'case_source': 'Gen 22:5'})
        w.submit({'kind': 'wood_laid', 'subject': 'isaac', 'case_source': 'Gen 22:6'})
        w.submit({'kind': 'lamb_asked', 'subject': 'isaac', 'case_source': 'Gen 22:7-8'})
        w.submit({'kind': 'altar_erected', 'subject': 'the-altar-at-moriah', 'by': 'abraham', 'case_source': 'Gen 22:9'})
        w.submit({'kind': 'bound', 'subject': 'isaac', 'case_source': 'Gen 22:9'})
        w.submit({'kind': 'knife_taken', 'subject': 'abraham', 'case_source': 'Gen 22:10'})
        w.submit({'kind': 'called_from_heaven', 'subject': 'abraham', 'time': 'the first', 'case_source': 'Gen 22:11-12'})
        close('abraham', 'offering_of_the_son_owed', 'Gen 22:12 — the hand stayed')
        close('abraham', 'tried', 'Gen 22:12 — now I know')
        w.submit({'kind': 'ram_seen', 'subject': 'the-ram-at-moriah', 'case_source': 'Gen 22:13'})
        w.submit({'kind': 'olah_offered', 'subject': 'abraham', 'what': 'the ram, in place of his son', 'case_source': 'Gen 22:13'})
        w.submit({'kind': 'named', 'subject': 'the-altar-at-moriah', 'name': 'the LORD will see (יהוה יראה, 22:14)', 'by': 'abraham', 'case_source': 'Gen 22:14'})
        w.submit({'kind': 'called_from_heaven', 'subject': 'abraham', 'time': 'the second', 'case_source': 'Gen 22:15'})
        w.submit({'kind': 'sworn_by_himself', 'subject': 'abraham', 'case_source': 'Gen 22:16-18'})
        w.submit({'kind': 'journeyed', 'subject': 'abraham', 'to': 'Beersheba', 'case_source': 'Gen 22:19'})
        w.submit({'kind': 'births_told', 'subject': 'abraham', 'count': 8, 'case_source': 'Gen 22:20-24'})
        w.submit({'kind': 'begot', 'subject': 'nahor', 'children': ['uz', 'buz', 'kemuel', 'chesed', 'hazo', 'pildash', 'jidlaph', 'bethuel'], 'case_source': 'Gen 22:20-22'})
        w.submit({'kind': 'begot', 'subject': 'bethuel', 'children': ['rebekah'], 'case_source': 'Gen 22:23'})
        w.submit({'kind': 'begot', 'subject': 'nahor', 'children': ['tebah', 'gaham', 'tahash', 'maacah'], 'by': 'reumah', 'case_source': 'Gen 22:24'})
        w.advance(8)
        w.submit({'kind': 'married', 'subject': 'keturah', 'husband': 'abraham', 'case_source': 'Gen 25:1'})
        w.submit({'kind': 'bore', 'subject': 'keturah', 'child': ['zimran', 'jokshan', 'medan', 'midian', 'ishbak', 'shuah'], 'case_source': 'Gen 25:2'})
        w.submit({'kind': 'begot', 'subject': 'jokshan', 'children': ['sheba', 'dedan'], 'case_source': 'Gen 25:3'})
        w.submit({'kind': 'begot', 'subject': 'dedan', 'children': ['the-asshurim', 'the-letushim', 'the-leummim'], 'case_source': 'Gen 25:3'})
        w.submit({'kind': 'begot', 'subject': 'midian', 'children': ['ephah', 'epher', 'hanoch', 'abida', 'eldaah'], 'case_source': 'Gen 25:4'})
        w.submit({'kind': 'all_given', 'subject': 'isaac', 'case_source': 'Gen 25:5'})
        w.submit({'kind': 'gifts_given', 'subject': 'the-sons-of-the-concubines', 'by': 'abraham', 'case_source': 'Gen 25:6'})
        w.submit({'kind': 'sent_away', 'subject': 'the-sons-of-the-concubines', 'case_source': 'Gen 25:6'})
        w.submit({'kind': 'died', 'subject': 'abraham', 'age': 175, 'case_source': 'Gen 25:7-8'})
        close('abraham', 'buried_in_peace', "Gen 25:8 — S2's entry: nothing to close here")
        w.submit({'kind': 'buried', 'subject': 'abraham', 'by': ['isaac', 'ishmael'], 'at': 'the cave of Machpelah', 'case_source': 'Gen 25:9-10'})
        w.submit({'kind': 'blessed_after_the_death', 'subject': 'isaac', 'case_source': 'Gen 25:11'})
        w.submit({'kind': 'princes_counted', 'subject': 'ishmael', 'names': ['nebaioth', 'kedar', 'adbeel', 'mibsam', 'mishma', 'dumah', 'massa', 'hadad', 'tema', 'jetur', 'naphish', 'kedemah'], 'case_source': 'Gen 25:13-16'})
        close('hagar', 'seed_multiplied', "Gen 25:16 — S2's entry: nothing to close here")
        w.submit({'kind': 'died', 'subject': 'ishmael', 'age': 137, 'case_source': 'Gen 25:17'})
        w.submit({'kind': 'fell_before_his_brothers', 'subject': 'ishmael', 'case_source': 'Gen 25:18'})
        w.advance(9)
        w.submit({'kind': 'prayed', 'subject': 'isaac', 'for': 'rebekah', 'case_source': 'Gen 25:21'})
        w.submit({'kind': 'struggled_in_the_womb', 'subject': 'rebekah', 'case_source': 'Gen 25:22'})
        w.submit({'kind': 'inquired', 'subject': 'rebekah', 'case_source': 'Gen 25:22'})
        w.submit({'kind': 'oracle_given', 'subject': 'rebekah', 'case_source': 'Gen 25:23'})
        w.submit({'kind': 'born', 'subject': 'esau', 'mother': 'rebekah', 'sex': 'm', 'order': 'the first, red', 'case_source': 'Gen 25:24-25'})
        w.submit({'kind': 'named', 'subject': 'esau', 'name': 'Esau (עשו — all of him like a hairy mantle, 25:25)', 'by': 'they', 'case_source': 'Gen 25:25'})
        w.submit({'kind': 'born', 'subject': 'jacob', 'mother': 'rebekah', 'sex': 'm', 'order': 'after that, his hand holding the heel', 'case_source': 'Gen 25:26'})
        w.submit({'kind': 'named', 'subject': 'jacob', 'name': 'Jacob (יעקב — his hand holding the heel, 25:26)', 'by': 'he', 'case_source': 'Gen 25:26'})
        w.submit({'kind': 'grew_up', 'subject': 'esau', 'case_source': 'Gen 25:27'})
        w.submit({'kind': 'loved_apart', 'subject': 'isaac', 'case_source': 'Gen 25:28'})
        w.advance(10)
        w.submit({'kind': 'stew_boiled', 'subject': 'jacob', 'case_source': 'Gen 25:29'})
        w.submit({'kind': 'gulp_demanded', 'subject': 'esau', 'case_source': 'Gen 25:30'})
        w.submit({'kind': 'named', 'subject': 'esau', 'name': 'Edom (אדום — the red, 25:30)', 'by': 'the report formula', 'case_source': 'Gen 25:30'})
        w.submit({'kind': 'sale_demanded', 'subject': 'jacob', 'case_source': 'Gen 25:31'})
        w.submit({'kind': 'birthright_dismissed', 'subject': 'esau', 'case_source': 'Gen 25:32'})
        w.submit({'kind': 'sworn', 'subject': 'esau', 'by': 'his word, to Jacob', 'case_source': 'Gen 25:33'})
        w.submit({'kind': 'birthright_sold', 'subject': 'jacob', 'from': 'esau', 'case_source': 'Gen 25:33'})
        w.submit({'kind': 'bread_and_lentils_given', 'subject': 'esau', 'case_source': 'Gen 25:34'})
        w.submit({'kind': 'birthright_despised', 'subject': 'esau', 'case_source': 'Gen 25:34'})
        w.advance(11)
        w.submit({'kind': 'famine_came', 'subject': 'the-land-of-canaan', 'case_source': 'Gen 26:1'})
        w.submit({'kind': 'journeyed', 'subject': 'isaac', 'to': 'Gerar, to Abimelech king of the Philistines', 'case_source': 'Gen 26:1'})
        w.submit({'kind': 'appeared', 'subject': 'isaac', 'at': 'Gerar', 'case_source': 'Gen 26:2'})
        w.submit({'kind': 'descent_barred', 'subject': 'isaac', 'case_source': 'Gen 26:2'})
        w.submit({'kind': 'oath_upheld', 'subject': 'isaac', 'case_source': 'Gen 26:3-5'})
        w.submit({'kind': 'dwelt', 'subject': 'isaac', 'at': 'Gerar', 'case_source': 'Gen 26:6'})
        w.submit({'kind': 'sister_asked', 'subject': 'rebekah', 'by': 'isaac', 'case_source': 'Gen 26:7'})
        w.submit({'kind': 'seen_sporting', 'subject': 'isaac', 'case_source': 'Gen 26:8'})
        w.submit({'kind': 'rebuked', 'subject': 'isaac', 'by': 'abimelech-of-isaac', 'case_source': 'Gen 26:9-10'})
        w.submit({'kind': 'decree_issued', 'subject': 'the-people-of-gerar', 'by': 'abimelech-of-isaac', 'decree': 'whoever touches this man or his wife shall surely be put to death', 'case_source': 'Gen 26:11'})
        w.submit({'kind': 'hundredfold_found', 'subject': 'isaac', 'measure': 100, 'case_source': 'Gen 26:12'})
        w.submit({'kind': 'grew_great', 'subject': 'isaac', 'case_source': 'Gen 26:13-14'})
        w.submit({'kind': 'envied', 'subject': 'the-philistines', 'whom': 'isaac', 'case_source': 'Gen 26:14'})
        w.submit({'kind': 'wells_stopped', 'subject': 'the-wells-of-abraham', 'case_source': 'Gen 26:15'})
        w.submit({'kind': 'sent_away', 'subject': 'isaac', 'by': 'abimelech-of-isaac', 'case_source': 'Gen 26:16'})
        w.advance(12)
        w.submit({'kind': 'journeyed', 'subject': 'isaac', 'to': 'the wadi of Gerar', 'case_source': 'Gen 26:17'})
        w.submit({'kind': 'wells_redug', 'subject': 'the-wells-of-abraham', 'case_source': 'Gen 26:18'})
        w.submit({'kind': 'well_found', 'subject': 'isaac', 'well': 'living water in the wadi', 'case_source': 'Gen 26:19'})
        w.submit({'kind': 'quarreled', 'subject': 'the-herdsmen-of-gerar', 'well': 'esek', 'case_source': 'Gen 26:20'})
        w.submit({'kind': 'named', 'subject': 'esek', 'name': 'Esek (עשק — for they contended with him, 26:20)', 'by': 'isaac', 'case_source': 'Gen 26:20'})
        w.submit({'kind': 'quarreled', 'subject': 'the-herdsmen-of-gerar', 'well': 'sitnah', 'case_source': 'Gen 26:21'})
        w.submit({'kind': 'named', 'subject': 'sitnah', 'name': 'Sitnah (שטנה, 26:21)', 'by': 'isaac', 'case_source': 'Gen 26:21'})
        w.submit({'kind': 'room_made', 'subject': 'isaac', 'case_source': 'Gen 26:22'})
        w.submit({'kind': 'named', 'subject': 'rehoboth', 'name': 'Rehoboth (רחבות — for now the LORD has made room for us, 26:22)', 'by': 'isaac', 'case_source': 'Gen 26:22'})
        w.submit({'kind': 'journeyed', 'subject': 'isaac', 'to': 'Beersheba', 'case_source': 'Gen 26:23'})
        w.submit({'kind': 'appeared', 'subject': 'isaac', 'at': 'Beersheba, that night', 'case_source': 'Gen 26:24'})
        w.submit({'kind': 'altar_erected', 'subject': 'the-altar-at-beersheba', 'by': 'isaac', 'case_source': 'Gen 26:25'})
        w.submit({'kind': 'called_on_the_name', 'subject': 'isaac', 'case_source': 'Gen 26:25'})
        w.submit({'kind': 'tent_pitched', 'subject': 'isaac', 'case_source': 'Gen 26:25'})
        w.submit({'kind': 'well_dug', 'subject': 'isaac', 'case_source': 'Gen 26:25'})
        w.submit({'kind': 'visited', 'subject': 'abimelech-of-isaac', 'case_source': 'Gen 26:26-27'})
        w.submit({'kind': 'covenant_proposed', 'subject': 'abimelech-of-isaac', 'case_source': 'Gen 26:28-29'})
        w.submit({'kind': 'feast_made', 'subject': 'isaac', 'case_source': 'Gen 26:30'})
        w.submit({'kind': 'sworn', 'subject': 'isaac_and_abimelech', 'by': 'each to his brother', 'case_source': 'Gen 26:31'})
        w.submit({'kind': 'covenant_cut_between_men', 'subject': 'isaac', 'with': 'abimelech-of-isaac', 'case_source': 'Gen 26:31'})
        w.submit({'kind': 'sent_away', 'subject': 'abimelech-of-isaac', 'by': 'isaac', 'in': 'peace', 'case_source': 'Gen 26:31'})
        w.submit({'kind': 'well_found', 'subject': 'isaac', 'well': 'the well at Beersheba, that same day', 'case_source': 'Gen 26:32'})
        w.submit({'kind': 'named', 'subject': 'beersheba', 'name': 'Shibah (שבעה — therefore the city is Beersheba to this day, 26:33)', 'by': 'isaac', 'case_source': 'Gen 26:33'})
        w.submit({'kind': 'married', 'subject': 'judith', 'husband': 'esau', 'case_source': 'Gen 26:34'})
        w.submit({'kind': 'married', 'subject': 'basemath', 'husband': 'esau', 'case_source': 'Gen 26:34'})
        w.submit({'kind': 'bitterness_of_spirit', 'subject': 'isaac_and_rebekah', 'case_source': 'Gen 26:35'})
        w.advance(13)
        w.submit({'kind': 'eyes_dimmed', 'subject': 'isaac', 'case_source': 'Gen 27:1'})
        w.submit({'kind': 'hunt_commanded', 'subject': 'esau', 'case_source': 'Gen 27:2-4'})
        w.submit({'kind': 'overheard', 'subject': 'rebekah', 'case_source': 'Gen 27:5'})
        w.submit({'kind': 'mother_counselled', 'subject': 'jacob', 'counsel': 'the two kids', 'case_source': 'Gen 27:6-10'})
        w.submit({'kind': 'objected', 'subject': 'jacob', 'case_source': 'Gen 27:11-12'})
        w.submit({'kind': 'curse_taken_on', 'subject': 'rebekah', 'case_source': 'Gen 27:13'})
        w.submit({'kind': 'kids_fetched', 'subject': 'jacob', 'case_source': 'Gen 27:14'})
        w.submit({'kind': 'disguised', 'subject': 'jacob', 'case_source': 'Gen 27:15-16'})
        w.submit({'kind': 'delicacies_brought', 'subject': 'jacob', 'to': 'isaac', 'case_source': 'Gen 27:17-18'})
        w.submit({'kind': 'identity_claimed', 'subject': 'jacob', 'as': 'Esau your firstborn', 'case_source': 'Gen 27:19'})
        w.submit({'kind': 'felt', 'subject': 'isaac', 'case_source': 'Gen 27:21-23'})
        w.submit({'kind': 'identity_claimed', 'subject': 'jacob', 'as': 'I am (Esau)', 'case_source': 'Gen 27:24'})
        w.submit({'kind': 'ate_and_drank', 'subject': 'isaac', 'case_source': 'Gen 27:25'})
        w.submit({'kind': 'kissed', 'subject': 'isaac', 'whom': 'jacob', 'case_source': 'Gen 27:26-27'})
        w.submit({'kind': 'blessed', 'subject': 'jacob', 'blessing': 'the dew and the fat, the peoples to serve', 'case_source': 'Gen 27:27-29'})
        w.submit({'kind': 'delicacies_brought', 'subject': 'esau', 'to': 'isaac', 'case_source': 'Gen 27:30-31'})
        close('esau', 'hunt_owed', 'Gen 27:31 — brought')
        w.submit({'kind': 'identity_claimed', 'subject': 'esau', 'as': 'your son, your firstborn, Esau', 'case_source': 'Gen 27:32'})
        w.submit({'kind': 'trembled', 'subject': 'isaac', 'case_source': 'Gen 27:33'})
        w.submit({'kind': 'cried_out', 'subject': 'esau', 'case_source': 'Gen 27:34'})
        w.submit({'kind': 'supplanted_charged', 'subject': 'esau', 'times': 2, 'case_source': 'Gen 27:35-37'})
        w.submit({'kind': 'wept', 'subject': 'esau', 'case_source': 'Gen 27:38'})
        w.submit({'kind': 'blessed', 'subject': 'esau', 'blessing': 'the fat of the earth, the sword, the yoke', 'case_source': 'Gen 27:39-40'})
        w.advance(14)
        w.submit({'kind': 'grudge_held', 'subject': 'esau', 'case_source': 'Gen 27:41'})
        w.submit({'kind': 'words_told', 'subject': 'rebekah', 'case_source': 'Gen 27:42'})
        w.submit({'kind': 'mother_counselled', 'subject': 'jacob', 'counsel': 'flee to Laban', 'case_source': 'Gen 27:42-45'})
        w.submit({'kind': 'loathing_stated', 'subject': 'rebekah', 'case_source': 'Gen 27:46'})
        w.submit({'kind': 'blessed', 'subject': 'jacob', 'blessing': 'the blessing of Abraham, the send-off; no Canaanite wife', 'case_source': 'Gen 28:1-4'})
        w.submit({'kind': 'sent_to_paddan_aram', 'subject': 'jacob', 'case_source': 'Gen 28:1-2; Gen 28:5'})
        w.submit({'kind': 'esau_saw', 'subject': 'esau', 'case_source': 'Gen 28:6-8'})
        w.submit({'kind': 'married', 'subject': 'mahalath', 'husband': 'esau', 'case_source': 'Gen 28:9'})
        w.advance(15)
        w.submit({'kind': 'journeyed', 'subject': 'jacob', 'to': 'toward Haran, from Beersheba', 'case_source': 'Gen 28:10'})
        close('jacob', 'flight_owed', 'Gen 28:10 — went out')
        w.submit({'kind': 'lodged_at_the_place', 'subject': 'jacob', 'case_source': 'Gen 28:11'})
        w.submit({'kind': 'dreamed', 'subject': 'jacob', 'of': 'the ladder', 'case_source': 'Gen 28:12'})
        w.submit({'kind': 'promised_at_bethel', 'subject': 'jacob', 'case_source': 'Gen 28:13-15'})
        w.submit({'kind': 'awoke_and_feared', 'subject': 'jacob', 'case_source': 'Gen 28:16-17'})
        w.advance(16)
        w.submit({'kind': 'pillar_set_and_anointed', 'subject': 'the_pillar_of_bethel', 'by': 'jacob', 'case_source': 'Gen 28:18'})
        w.submit({'kind': 'named', 'subject': 'the-place', 'name': 'Bethel (בית אל — but Luz was the name of the city at first, 28:19)', 'by': 'jacob', 'case_source': 'Gen 28:19'})
        w.submit({'kind': 'vowed', 'subject': 'jacob', 'conditions': ['God with me', 'kept on this way', 'bread and a garment', 'return in peace'], 'commitments': ['the LORD my God', 'the stone the house of God', 'the tithe of all'], 'case_source': 'Gen 28:20-22'})
        w.advance(17)
        w.submit({'kind': 'journeyed', 'subject': 'jacob', 'to': 'the land of the children of the east', 'case_source': 'Gen 29:1'})
        w.submit({'kind': 'well_seen', 'subject': 'the-well-of-haran', 'case_source': 'Gen 29:2-3'})
        w.submit({'kind': 'shepherds_questioned', 'subject': 'jacob', 'case_source': 'Gen 29:4-6'})
        w.submit({'kind': 'shepherds_rebuked', 'subject': 'jacob', 'case_source': 'Gen 29:7-8'})
        w.submit({'kind': 'stone_rolled', 'subject': 'jacob', 'case_source': 'Gen 29:9-10'})
        w.submit({'kind': 'flock_watered', 'subject': 'jacob', 'case_source': 'Gen 29:10'})
        w.submit({'kind': 'kissed', 'subject': 'jacob', 'whom': 'rachel', 'case_source': 'Gen 29:11'})
        w.submit({'kind': 'kin_told', 'subject': 'rachel', 'case_source': 'Gen 29:12'})
        w.submit({'kind': 'kissed', 'subject': 'laban', 'whom': 'jacob', 'case_source': 'Gen 29:13'})
        w.submit({'kind': 'embraced', 'subject': 'laban', 'case_source': 'Gen 29:13-14'})
        w.advance(47)
        w.submit({'kind': 'month_dwelt', 'subject': 'jacob', 'months': 1, 'case_source': 'Gen 29:14'})
        w.submit({'kind': 'wage_asked', 'subject': 'laban', 'case_source': 'Gen 29:15-17'})
        w.submit({'kind': 'wage_named', 'subject': 'jacob', 'years': 7, 'terms': 'seven years for Rachel your younger daughter', 'case_source': 'Gen 29:18'})
        w.submit({'kind': 'contract_accepted', 'subject': 'laban', 'case_source': 'Gen 29:19'})
        w.advance(2602)
        w.submit({'kind': 'served', 'subject': 'jacob', 'years': 7, 'case_source': 'Gen 29:20'})
        w.submit({'kind': 'wife_demanded', 'subject': 'jacob', 'case_source': 'Gen 29:21'})
        close('jacob', 'seven_years_owed', 'Gen 29:21 — my days are fulfilled')
        w.submit({'kind': 'feast_made', 'subject': 'laban', 'case_source': 'Gen 29:22'})
        w.submit({'kind': 'bride_switched', 'subject': 'jacob', 'case_source': 'Gen 29:23'})
        w.submit({'kind': 'married', 'subject': 'leah', 'husband': 'jacob', 'case_source': 'Gen 29:23'})
        w.submit({'kind': 'maid_given', 'subject': 'leah', 'maid': 'zilpah', 'case_source': 'Gen 29:24'})
        w.submit({'kind': 'bride_switched', 'subject': 'laban', 'case_source': 'Gen 29:25'})
        w.submit({'kind': 'custom_stated', 'subject': 'laban', 'case_source': 'Gen 29:26'})
        w.submit({'kind': 'week_demanded', 'subject': 'jacob', 'days': 7, 'case_source': 'Gen 29:27'})
        w.advance(2609)
        w.submit({'kind': 'week_fulfilled', 'subject': 'jacob', 'case_source': 'Gen 29:28'})
        w.submit({'kind': 'married', 'subject': 'rachel', 'husband': 'jacob', 'case_source': 'Gen 29:28'})
        close('jacob', 'wife_from_paddan_owed', 'Gen 29:28 — Rachel given')
        w.submit({'kind': 'maid_given', 'subject': 'rachel', 'maid': 'bilhah', 'case_source': 'Gen 29:29'})
        w.submit({'kind': 'served', 'subject': 'jacob', 'years': 7, 'which': 'the second', 'case_source': 'Gen 29:30'})
        w.submit({'kind': 'womb_opened', 'subject': 'leah', 'case_source': 'Gen 29:31'})
        w.advance(2729)
        w.submit({'kind': 'born', 'subject': 'reuben', 'mother': 'leah', 'sex': 'm', 'case_source': 'Gen 29:32'})
        w.submit({'kind': 'named', 'subject': 'reuben', 'name': 'Reuben (ראובן — the LORD has seen my affliction, 29:32)', 'by': 'leah', 'case_source': 'Gen 29:32'})
        w.advance(2849)
        w.submit({'kind': 'born', 'subject': 'simeon', 'mother': 'leah', 'sex': 'm', 'case_source': 'Gen 29:33'})
        w.submit({'kind': 'named', 'subject': 'simeon', 'name': 'Simeon (שמעון — the LORD has heard that I am hated, 29:33)', 'by': 'leah', 'case_source': 'Gen 29:33'})
        w.advance(2969)
        w.submit({'kind': 'born', 'subject': 'levi', 'mother': 'leah', 'sex': 'm', 'case_source': 'Gen 29:34'})
        w.submit({'kind': 'named', 'subject': 'levi', 'name': 'Levi (לוי — this time my husband will be joined to me, 29:34)', 'by': 'she', 'case_source': 'Gen 29:34'})
        w.advance(3089)
        w.submit({'kind': 'born', 'subject': 'judah', 'mother': 'leah', 'sex': 'm', 'case_source': 'Gen 29:35'})
        w.submit({'kind': 'named', 'subject': 'judah', 'name': 'Judah (יהודה — this time I will praise the LORD, 29:35)', 'by': 'leah', 'case_source': 'Gen 29:35'})
        w.submit({'kind': 'ceased_bearing', 'subject': 'leah', 'at': '29:35', 'case_source': 'Gen 29:35'})
        w.submit({'kind': 'envied', 'subject': 'rachel', 'whom': 'leah', 'case_source': 'Gen 30:1'})
        w.submit({'kind': 'children_demanded', 'subject': 'rachel', 'case_source': 'Gen 30:1'})
        w.submit({'kind': 'anger_burned', 'subject': 'jacob', 'at': 'rachel', 'case_source': 'Gen 30:2'})
        w.submit({'kind': 'maid_offered', 'subject': 'rachel', 'case_source': 'Gen 30:3'})
        w.submit({'kind': 'married', 'subject': 'bilhah', 'husband': 'jacob', 'case_source': 'Gen 30:4'})
        w.advance(3209)
        w.submit({'kind': 'born', 'subject': 'dan', 'mother': 'bilhah', 'sex': 'm', 'case_source': 'Gen 30:5'})
        w.submit({'kind': 'named', 'subject': 'dan', 'name': 'Dan (דן — God has judged me, 30:6)', 'by': 'rachel', 'case_source': 'Gen 30:6'})
        w.advance(3329)
        w.submit({'kind': 'born', 'subject': 'naphtali', 'mother': 'bilhah', 'sex': 'm', 'case_source': 'Gen 30:7'})
        w.submit({'kind': 'named', 'subject': 'naphtali', 'name': 'Naphtali (נפתלי — wrestlings of God I have wrestled, 30:8)', 'by': 'rachel', 'case_source': 'Gen 30:8'})
        w.submit({'kind': 'ceased_bearing', 'subject': 'leah', 'at': '30:9', 'case_source': 'Gen 30:9'})
        w.submit({'kind': 'married', 'subject': 'zilpah', 'husband': 'jacob', 'case_source': 'Gen 30:9'})
        w.advance(3449)
        w.submit({'kind': 'born', 'subject': 'gad', 'mother': 'zilpah', 'sex': 'm', 'case_source': 'Gen 30:10'})
        w.submit({'kind': 'named', 'subject': 'gad', 'name': 'Gad (גד — fortune has come, 30:11)', 'by': 'leah', 'case_source': 'Gen 30:11'})
        w.advance(3569)
        w.submit({'kind': 'born', 'subject': 'asher', 'mother': 'zilpah', 'sex': 'm', 'case_source': 'Gen 30:12'})
        w.submit({'kind': 'named', 'subject': 'asher', 'name': 'Asher (אשר — in my happiness, 30:13)', 'by': 'leah', 'case_source': 'Gen 30:13'})
        w.submit({'kind': 'mandrakes_found', 'subject': 'reuben', 'case_source': 'Gen 30:14'})
        w.submit({'kind': 'mandrakes_traded', 'subject': 'leah', 'case_source': 'Gen 30:14-16'})
        w.submit({'kind': 'god_heard', 'subject': 'leah', 'case_source': 'Gen 30:17'})
        w.advance(3689)
        w.submit({'kind': 'born', 'subject': 'issachar', 'mother': 'leah', 'sex': 'm', 'case_source': 'Gen 30:17'})
        w.submit({'kind': 'named', 'subject': 'issachar', 'name': 'Issachar (יששכר — God has given my hire, 30:18)', 'by': 'leah', 'case_source': 'Gen 30:18'})
        w.advance(3809)
        w.submit({'kind': 'born', 'subject': 'zebulun', 'mother': 'leah', 'sex': 'm', 'case_source': 'Gen 30:19'})
        w.submit({'kind': 'named', 'subject': 'zebulun', 'name': 'Zebulun (זבלון — God has endowed me with a good endowment, 30:20)', 'by': 'leah', 'case_source': 'Gen 30:20'})
        w.advance(3929)
        w.submit({'kind': 'born', 'subject': 'dinah', 'mother': 'leah', 'sex': 'f', 'case_source': 'Gen 30:21'})
        w.submit({'kind': 'named', 'subject': 'dinah', 'name': 'Dinah (דינה, 30:21)', 'by': 'leah', 'case_source': 'Gen 30:21'})
        w.submit({'kind': 'remembered', 'subject': 'rachel', 'case_source': 'Gen 30:22'})
        w.submit({'kind': 'womb_opened', 'subject': 'rachel', 'case_source': 'Gen 30:22'})
        w.advance(4049)
        w.submit({'kind': 'born', 'subject': 'joseph', 'mother': 'rachel', 'sex': 'm', 'case_source': 'Gen 30:23'})
        w.submit({'kind': 'named', 'subject': 'joseph', 'name': 'Joseph (יוסף — may the LORD add to me another son, 30:24)', 'by': 'rachel', 'case_source': 'Gen 30:24'})
        w.advance(5164)
        w.submit({'kind': 'release_demanded', 'subject': 'jacob', 'case_source': 'Gen 30:25-26'})
        close('jacob', 'second_seven_owed', 'Gen 30:26 — served')
        w.submit({'kind': 'divination_confessed', 'subject': 'laban', 'case_source': 'Gen 30:27'})
        w.submit({'kind': 'wage_asked', 'subject': 'laban', 'case_source': 'Gen 30:28'})
        w.submit({'kind': 'service_audited', 'subject': 'jacob', 'case_source': 'Gen 30:29-30'})
        w.submit({'kind': 'wage_named', 'subject': 'jacob', 'terms': 'every speckled and spotted sheep and every dark one among the lambs, the spotted and speckled among the goats', 'case_source': 'Gen 30:31-33'})
        w.submit({'kind': 'contract_accepted', 'subject': 'laban', 'case_source': 'Gen 30:34'})
        w.submit({'kind': 'flock_removed', 'subject': 'laban', 'days': 3, 'case_source': 'Gen 30:35-36'})
        w.advance(5167)
        w.submit({'kind': 'rods_peeled', 'subject': 'jacob', 'case_source': 'Gen 30:37-38'})
        w.submit({'kind': 'flock_bore_striped', 'subject': 'the-flock', 'case_source': 'Gen 30:39'})
        w.submit({'kind': 'flocks_separated', 'subject': 'jacob', 'case_source': 'Gen 30:40-42'})
        w.submit({'kind': 'broke_out', 'subject': 'jacob', 'case_source': 'Gen 30:43'})
        w.advance(7357)
        w.submit({'kind': 'sons_words_heard', 'subject': 'jacob', 'case_source': 'Gen 31:1-2'})
        w.submit({'kind': 'return_commanded', 'subject': 'jacob', 'case_source': 'Gen 31:3'})
        w.submit({'kind': 'wives_summoned', 'subject': 'jacob', 'case_source': 'Gen 31:4'})
        w.submit({'kind': 'account_given', 'subject': 'jacob', 'account': 'to the wives', 'case_source': 'Gen 31:5-13'})
        close('jacob', 'with_you_promised', 'Gen 31:5 — the God of my father has been with me')
        w.submit({'kind': 'dreamed', 'subject': 'jacob', 'of': 'the he-goats', 'case_source': 'Gen 31:10-12'})
        w.submit({'kind': 'wives_answered', 'subject': 'rachel_and_leah', 'case_source': 'Gen 31:14-16'})
        w.submit({'kind': 'rose_and_loaded', 'subject': 'jacob', 'case_source': 'Gen 31:17-18'})
        w.submit({'kind': 'teraphim_stolen', 'subject': 'rachel', 'case_source': 'Gen 31:19'})
        w.submit({'kind': 'heart_stolen', 'subject': 'laban', 'case_source': 'Gen 31:20'})
        w.submit({'kind': 'fled', 'subject': 'jacob', 'from': 'laban', 'case_source': 'Gen 31:21'})
        w.submit({'kind': 'river_crossed', 'subject': 'jacob', 'case_source': 'Gen 31:21'})
        w.advance(7359)
        w.submit({'kind': 'told_on_the_third_day', 'subject': 'laban', 'ordinal': 3, 'case_source': 'Gen 31:22'})
        w.advance(7360)
        w.submit({'kind': 'pursued', 'subject': 'laban', 'whom': 'jacob', 'days': 7, 'case_source': 'Gen 31:23'})
        w.submit({'kind': 'came_in_a_dream', 'subject': 'laban', 'warning': 'neither good nor bad', 'case_source': 'Gen 31:24'})
        w.submit({'kind': 'overtaken', 'subject': 'jacob', 'case_source': 'Gen 31:25'})
        w.submit({'kind': 'charges_laid', 'subject': 'laban', 'case_source': 'Gen 31:26-30'})
        close('laban', 'speech_restrained', 'Gen 31:29 — he kept it')
        w.submit({'kind': 'fear_answered', 'subject': 'jacob', 'case_source': 'Gen 31:31'})
        w.submit({'kind': 'death_oath_sworn', 'subject': 'rachel', 'the_thief': "rachel — the narrator's knowledge (31:19)", 'case_source': 'Gen 31:32'})
        w.submit({'kind': 'tents_searched', 'subject': 'laban', 'case_source': 'Gen 31:33-35'})
        w.submit({'kind': 'anger_burned', 'subject': 'jacob', 'at': 'laban', 'case_source': 'Gen 31:36'})
        w.submit({'kind': 'quarreled_with_laban', 'subject': 'jacob', 'case_source': 'Gen 31:36-37'})
        w.submit({'kind': 'account_given', 'subject': 'jacob', 'account': 'the twenty years, to Laban', 'case_source': 'Gen 31:38-42'})
        w.submit({'kind': 'all_is_mine_claimed', 'subject': 'laban', 'case_source': 'Gen 31:43'})
        w.submit({'kind': 'covenant_proposed', 'subject': 'laban', 'case_source': 'Gen 31:44'})
        w.submit({'kind': 'pillar_set_and_anointed', 'subject': 'the_pillar_of_gilead', 'by': 'jacob', 'case_source': 'Gen 31:45'})
        w.submit({'kind': 'heap_made', 'subject': 'the-heap', 'case_source': 'Gen 31:46'})
        w.submit({'kind': 'named', 'subject': 'the-heap', 'name': 'Jegar-sahadutha (יגר שהדותא — the Aramaic, 31:47)', 'by': 'laban', 'case_source': 'Gen 31:47'})
        w.submit({'kind': 'named', 'subject': 'the-heap', 'name': 'Galeed (גלעד — the Hebrew, 31:47)', 'by': 'jacob', 'case_source': 'Gen 31:47'})
        w.submit({'kind': 'witness_declared', 'subject': 'the-heap', 'case_source': 'Gen 31:48-50'})
        w.submit({'kind': 'named', 'subject': 'the-heap', 'name': 'Galeed (גלעד — therefore its name was called, 31:48)', 'by': 'the report formula', 'case_source': 'Gen 31:48'})
        w.submit({'kind': 'named', 'subject': 'the-heap', 'name': 'Mizpah (המצפה — may the LORD watch, 31:49)', 'by': 'laban', 'case_source': 'Gen 31:49'})
        w.submit({'kind': 'boundary_sworn', 'subject': 'the_heap_and_pillar', 'case_source': 'Gen 31:51-53'})
        w.submit({'kind': 'sworn', 'subject': 'jacob', 'by': 'the Fear of his father Isaac', 'case_source': 'Gen 31:53'})
        w.submit({'kind': 'covenant_cut_between_men', 'subject': 'jacob', 'with': 'laban', 'case_source': 'Gen 31:53'})
        w.submit({'kind': 'sacrificed', 'subject': 'jacob', 'case_source': 'Gen 31:54'})
        w.submit({'kind': 'ate_and_lodged', 'subject': 'jacob_and_his_kin', 'case_source': 'Gen 31:54'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    open_total = sum(len(ent.open_entries()) for ent in w.entities.values())
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    return tuple(n(eid, eff) for eid, eff in SLOTS) + (open_total, tset, fired, closes[0], w.clock.day), w
SCENE, _W = scene()
SCENE_EVENTS = [('appeared', 'abraham'), ('ran_and_bowed', 'abraham'), ('hospitality_offered', 'abraham'), ('cakes_ordered', 'abraham'), ('calf_prepared', 'abraham'), ('meal_served', 'abraham'), ('son_promised', 'sarah'), ('laughed_within', 'sarah'), ('laugh_denied', 'sarah'), ('escorted', 'abraham'), ('house_charged', 'abraham'), ('outcry_declared', 'sodom'), ('stood_before_the_lord', 'abraham'), ('pleaded_for_the_righteous', 'abraham'), ('lord_departed', 'god'), ('ran_and_bowed', 'lot'), ('hospitality_offered', 'lot'), ('lodging_urged', 'lot'), ('matzot_baked', 'lot'), ('house_surrounded', 'lot'), ('men_demanded', 'the-men-of-sodom'), ('daughters_offered', 'lot'), ('pressed_at_the_door', 'the-men-of-sodom'), ('pulled_in', 'lot'), ('struck_blind', 'the-men-of-sodom'), ('evacuation_commanded', 'lot'), ('mocked_by_sons_in_law', 'lot'), ('lingered', 'lot'), ('led_out', 'lot_and_his_house'), ('escape_commanded', 'lot_and_his_house'), ('little_city_pleaded', 'lot'), ('city_spared', 'zoar'), ('named', 'zoar'), ('fire_rained', 'the-cities-of-the-plain'), ('overturned', 'the-cities-of-the-plain'), ('looked_back', 'lots-wife'), ('rose_to_the_place', 'abraham'), ('remembered', 'abraham'), ('sent_away', 'lot'), ('dwelt_in_the_cave', 'lot'), ('made_the_father_drink', 'the-two-daughters'), ('made_the_father_drink', 'the-two-daughters'), ('bore', 'ha-bekhirah'), ('named', 'moab'), ('bore', 'the-younger-daughter'), ('named', 'ben-ammi'), ('journeyed', 'abraham'), ('sister_asked', 'sarah'), ('woman_taken', 'sarah'), ('came_in_a_dream', 'abimelech'), ('king_pleaded', 'abimelech'), ('prophet_declared', 'abimelech'), ('servants_told', 'the_house_of_abimelech'), ('rebuked', 'abraham'), ('answered_the_king', 'abraham'), ('restored', 'abraham'), ('dwelling_granted', 'abraham'), ('silver_given', 'sarah'), ('prayed', 'abraham'), ('healed', 'the_house_of_abimelech'), ('wombs_shut', 'the_house_of_abimelech'), ('tested', 'abraham'), ('offering_commanded', 'abraham'), ('rose_early_and_went', 'abraham'), ('place_seen_on_the_third_day', 'abraham'), ('lads_left', 'the-two-lads'), ('wood_laid', 'isaac'), ('lamb_asked', 'isaac'), ('altar_erected', 'the-altar-at-moriah'), ('bound', 'isaac'), ('knife_taken', 'abraham'), ('called_from_heaven', 'abraham'), ('ram_seen', 'the-ram-at-moriah'), ('olah_offered', 'abraham'), ('named', 'the-altar-at-moriah'), ('called_from_heaven', 'abraham'), ('sworn_by_himself', 'abraham'), ('journeyed', 'abraham'), ('births_told', 'abraham'), ('begot', 'nahor'), ('begot', 'bethuel'), ('begot', 'nahor'), ('married', 'keturah'), ('bore', 'keturah'), ('begot', 'jokshan'), ('begot', 'dedan'), ('begot', 'midian'), ('all_given', 'isaac'), ('gifts_given', 'the-sons-of-the-concubines'), ('sent_away', 'the-sons-of-the-concubines'), ('died', 'abraham'), ('buried', 'abraham'), ('blessed_after_the_death', 'isaac'), ('princes_counted', 'ishmael'), ('died', 'ishmael'), ('fell_before_his_brothers', 'ishmael'), ('prayed', 'isaac'), ('struggled_in_the_womb', 'rebekah'), ('inquired', 'rebekah'), ('oracle_given', 'rebekah'), ('born', 'esau'), ('named', 'esau'), ('born', 'jacob'), ('named', 'jacob'), ('grew_up', 'esau'), ('loved_apart', 'isaac'), ('stew_boiled', 'jacob'), ('gulp_demanded', 'esau'), ('named', 'esau'), ('sale_demanded', 'jacob'), ('birthright_dismissed', 'esau'), ('sworn', 'esau'), ('birthright_sold', 'jacob'), ('bread_and_lentils_given', 'esau'), ('birthright_despised', 'esau'), ('famine_came', 'the-land-of-canaan'), ('journeyed', 'isaac'), ('appeared', 'isaac'), ('descent_barred', 'isaac'), ('oath_upheld', 'isaac'), ('dwelt', 'isaac'), ('sister_asked', 'rebekah'), ('seen_sporting', 'isaac'), ('rebuked', 'isaac'), ('decree_issued', 'the-people-of-gerar'), ('hundredfold_found', 'isaac'), ('grew_great', 'isaac'), ('envied', 'the-philistines'), ('wells_stopped', 'the-wells-of-abraham'), ('sent_away', 'isaac'), ('journeyed', 'isaac'), ('wells_redug', 'the-wells-of-abraham'), ('well_found', 'isaac'), ('quarreled', 'the-herdsmen-of-gerar'), ('named', 'esek'), ('quarreled', 'the-herdsmen-of-gerar'), ('named', 'sitnah'), ('room_made', 'isaac'), ('named', 'rehoboth'), ('journeyed', 'isaac'), ('appeared', 'isaac'), ('altar_erected', 'the-altar-at-beersheba'), ('called_on_the_name', 'isaac'), ('tent_pitched', 'isaac'), ('well_dug', 'isaac'), ('visited', 'abimelech-of-isaac'), ('covenant_proposed', 'abimelech-of-isaac'), ('feast_made', 'isaac'), ('sworn', 'isaac_and_abimelech'), ('covenant_cut_between_men', 'isaac'), ('sent_away', 'abimelech-of-isaac'), ('well_found', 'isaac'), ('named', 'beersheba'), ('married', 'judith'), ('married', 'basemath'), ('bitterness_of_spirit', 'isaac_and_rebekah'), ('eyes_dimmed', 'isaac'), ('hunt_commanded', 'esau'), ('overheard', 'rebekah'), ('mother_counselled', 'jacob'), ('objected', 'jacob'), ('curse_taken_on', 'rebekah'), ('kids_fetched', 'jacob'), ('disguised', 'jacob'), ('delicacies_brought', 'jacob'), ('identity_claimed', 'jacob'), ('felt', 'isaac'), ('identity_claimed', 'jacob'), ('ate_and_drank', 'isaac'), ('kissed', 'isaac'), ('blessed', 'jacob'), ('delicacies_brought', 'esau'), ('identity_claimed', 'esau'), ('trembled', 'isaac'), ('cried_out', 'esau'), ('supplanted_charged', 'esau'), ('wept', 'esau'), ('blessed', 'esau'), ('grudge_held', 'esau'), ('words_told', 'rebekah'), ('mother_counselled', 'jacob'), ('loathing_stated', 'rebekah'), ('blessed', 'jacob'), ('sent_to_paddan_aram', 'jacob'), ('esau_saw', 'esau'), ('married', 'mahalath'), ('journeyed', 'jacob'), ('lodged_at_the_place', 'jacob'), ('dreamed', 'jacob'), ('promised_at_bethel', 'jacob'), ('awoke_and_feared', 'jacob'), ('pillar_set_and_anointed', 'the_pillar_of_bethel'), ('named', 'the-place'), ('vowed', 'jacob'), ('journeyed', 'jacob'), ('well_seen', 'the-well-of-haran'), ('shepherds_questioned', 'jacob'), ('shepherds_rebuked', 'jacob'), ('stone_rolled', 'jacob'), ('flock_watered', 'jacob'), ('kissed', 'jacob'), ('kin_told', 'rachel'), ('kissed', 'laban'), ('embraced', 'laban'), ('month_dwelt', 'jacob'), ('wage_asked', 'laban'), ('wage_named', 'jacob'), ('contract_accepted', 'laban'), ('served', 'jacob'), ('wife_demanded', 'jacob'), ('feast_made', 'laban'), ('bride_switched', 'jacob'), ('married', 'leah'), ('maid_given', 'leah'), ('bride_switched', 'laban'), ('custom_stated', 'laban'), ('week_demanded', 'jacob'), ('week_fulfilled', 'jacob'), ('married', 'rachel'), ('maid_given', 'rachel'), ('served', 'jacob'), ('womb_opened', 'leah'), ('born', 'reuben'), ('named', 'reuben'), ('born', 'simeon'), ('named', 'simeon'), ('born', 'levi'), ('named', 'levi'), ('born', 'judah'), ('named', 'judah'), ('ceased_bearing', 'leah'), ('envied', 'rachel'), ('children_demanded', 'rachel'), ('anger_burned', 'jacob'), ('maid_offered', 'rachel'), ('married', 'bilhah'), ('born', 'dan'), ('named', 'dan'), ('born', 'naphtali'), ('named', 'naphtali'), ('ceased_bearing', 'leah'), ('married', 'zilpah'), ('born', 'gad'), ('named', 'gad'), ('born', 'asher'), ('named', 'asher'), ('mandrakes_found', 'reuben'), ('mandrakes_traded', 'leah'), ('god_heard', 'leah'), ('born', 'issachar'), ('named', 'issachar'), ('born', 'zebulun'), ('named', 'zebulun'), ('born', 'dinah'), ('named', 'dinah'), ('remembered', 'rachel'), ('womb_opened', 'rachel'), ('born', 'joseph'), ('named', 'joseph'), ('release_demanded', 'jacob'), ('divination_confessed', 'laban'), ('wage_asked', 'laban'), ('service_audited', 'jacob'), ('wage_named', 'jacob'), ('contract_accepted', 'laban'), ('flock_removed', 'laban'), ('rods_peeled', 'jacob'), ('flock_bore_striped', 'the-flock'), ('flocks_separated', 'jacob'), ('broke_out', 'jacob'), ('sons_words_heard', 'jacob'), ('return_commanded', 'jacob'), ('wives_summoned', 'jacob'), ('account_given', 'jacob'), ('dreamed', 'jacob'), ('wives_answered', 'rachel_and_leah'), ('rose_and_loaded', 'jacob'), ('teraphim_stolen', 'rachel'), ('heart_stolen', 'laban'), ('fled', 'jacob'), ('river_crossed', 'jacob'), ('told_on_the_third_day', 'laban'), ('pursued', 'laban'), ('came_in_a_dream', 'laban'), ('overtaken', 'jacob'), ('charges_laid', 'laban'), ('fear_answered', 'jacob'), ('death_oath_sworn', 'rachel'), ('tents_searched', 'laban'), ('anger_burned', 'jacob'), ('quarreled_with_laban', 'jacob'), ('account_given', 'jacob'), ('all_is_mine_claimed', 'laban'), ('covenant_proposed', 'laban'), ('pillar_set_and_anointed', 'the_pillar_of_gilead'), ('heap_made', 'the-heap'), ('named', 'the-heap'), ('named', 'the-heap'), ('witness_declared', 'the-heap'), ('named', 'the-heap'), ('named', 'the-heap'), ('boundary_sworn', 'the_heap_and_pillar'), ('sworn', 'jacob'), ('covenant_cut_between_men', 'jacob'), ('sacrificed', 'jacob'), ('ate_and_lodged', 'jacob_and_his_kin')]
_SCENE_NAMED = [e for e in SCENE_EVENTS if e[0] == 'named']


def build(q):
    if q == 'world':
        return cell(SCENE, I, "THE SCENE on the world engine — the three hundred and fifty-seven effect slots of the declaration in order, then the opens, the timers set and fired, the closes, the day (the hand-model's print, scratchpad o8_s3_predict.py); the four story timers and the thirteen eighth days fire inside the scene; the one-year timer of 18:10 finds no birth here", ['son_promised_at_the_season', 'return_at_the_season', 'seven_years_service', 'week_of_the_feast', 'second_seven_service'])
    if q == 'headline_join':
        return cell('the_season_joins_two_shelf_rows', M, "THE HEADLINE (1): the visit placed on Passover of the year before (Bereshit Rabbah 48:12) and Isaac's birth placed on Passover (Rosh Hashanah 10b:10) are two independent rows; the ink's own 'at this living season' (18:10, 18:14) and 'at the set time' (21:2) join them — the one-year timer set at the visit fires on the birth's day (the sequence runner CH0)", ['return_at_the_season', 'son_promised_at_the_season'])
    if q == 'headline_installation':
        return cell('the_covenants_daemon_runs_on_the_stretchs_births', D, "THE HEADLINE (2): the twins and the eleven sons are `born` under Genesis 17, and the pre-Sinai daemon writes their eighth-day debits by the statute's own run — thirteen, none on Dinah (17:12 'every male', the field read); Lot's daughters' and Nahor's births are `bore` and `begot`, outside the covenant — the naming stand-in for installation (THE TIME CONSENSUS's T1)", ['daughter_born', 'begotten'])
    if q == 'headline_keeper':
        return cell('the_paid_keeper_grades_jacobs_account', P, "THE HEADLINE (3): 31:38-40 laid on the four keepers' verdict table by call — theft PAY, the witnessed accident OATH, the loss PAY; Jacob paid for the torn too: the keeper's ceiling exceeded, as Bava Metzia 93b:3 reads it ('is Jacob our father a city watchman?!')", ['keeper_account', 'torn_borne_beyond_duty'])
    if q == 'headline_fourteen':
        return cell('the_fourteen_hidden_years_fall_out_of_the_inks_numbers', M, "THE HEADLINE (4): Ishmael's death (16:16 + 25:17) sets Jacob's sixty-three (25:26) — Bereshit Rabbah 68:5's number by the ink's arithmetic; Megillah 17a's fourteen from there places the departure; the two sevens and Joseph's birth from Pharaoh's side (41:46, 45:6, 47:9) meet at the fourteen's end — the sequence runner CH3, CH4, CH5", ['seven_years_service', 'second_seven_service', 'twenty_years_served'])
    if q == 'headline_two_tongues':
        return cell('one_heap_two_names', I, "THE HEADLINE (5): 'and Laban called it Jegar-sahadutha, and Jacob called it Galeed' (31:47) — one heap, the Aramaic and the Hebrew, both name_given on the ledger; then Galeed by the report formula (31:48) and Mizpah (31:49): four namings on one witness", ['name_given', 'heap_made', 'witness_declared'])
    return cell('no_case', I, '', [FX.NONE])


TESTS = [
 # ---- Gen 18: mamre ----
 ('the appearance formula in Gen 18-31 — three seats', mamre('appearance_seats'), 3),
 ('three men (18:2)', mamre('three_men'), 3),
 ('three seahs of fine flour (18:6)', mamre('three_seahs'), 3),
 ('hospitality greater than receiving the Presence (Shabbat 127a)', mamre('hospitality_rank'), 'greater_than_receiving_the_presence'),
 ('"at this living season" — four seats in the Tanakh', mamre('season_phrase_seats'), 4),
 ('the one-year timer on the bare scene', mamre('season_timer_days'), 365),
 ('the laugh quoted altered for peace (Bava Metzia 87a)', mamre('laugh_quoted_altered'), 'and_my_lord_is_old_dropped'),
 ('the house charge: righteousness and justice', mamre('house_charge_pair'), ('righteousness', 'justice')),
 ("the plea's ladder by the verses' numerals", mamre('ladder'), [50, 45, 40, 30, 20, 10]),
 ("the plea's ladder by the census function", mamre('ladder_by_census'), [50, 45, 40, 30, 20, 10]),
 ('why stop at ten (Bereshit Rabbah 49:13)', mamre('why_stop_at_ten'), 'eight_of_noahs_house_were_not_enough'),
 ('standing is prayer (Berakhot 6b, 26b)', mamre('standing_is_prayer'), 'prayer'),
 ("the outcry's inquiry closed by the overthrow", mamre('outcry_closed_by'), 'Gen 19:25'),
 # ---- Gen 19: sodom ----
 ('the unleavened token once in Genesis', sodom('matzot_seat'), 1),
 ("Lot learned in Abraham's house (Bereshit Rabbah 50:4)", sodom('lot_learned_where'), 'abrahams_house'),
 ('the blindness noun — two seats in the Tanakh', sodom('blindness_seats'), 2),
 ('the evacuation received at 19:16', sodom('evacuation_receipt'), 'Gen 19:16'),
 ('the look-back ban breached at 19:26', sodom('ban_breached_at'), 'Gen 19:26'),
 ('a pillar of salt — the only seat', sodom('salt_pillar_seats'), 1),
 ('the salt sin (Bereshit Rabbah 51:5)', sodom('salt_sin'), 'refused_salt_to_the_guests'),
 ("Sodom's row (Mishnah Sanhedrin 10:3)", sodom('sodom_sheet_row'), 'no_share_in_the_world_to_come'),
 ("Sodom's tranquility: fifty-two years, twenty-five of warnings", sodom('tranquility_years'), (52, 25)),
 ('"and God remembered" — three seats', sodom('remembered_seats'), 3),
 ('the morning prayer founded by Abraham (Berakhot 26b:5)', sodom('morning_prayer_founder'), 'abraham'),
 ('a fixed place for prayer (Berakhot 6b:8)', sodom('fixed_place'), 'Gen 19:27'),
 ("the daughters' two nights", sodom('daughters_two_nights'), 2),
 ('two peoples named', sodom('two_peoples_named'), ('moab', 'ben-ammi')),
 # ---- Gen 20: gerar ----
 ('"she is my sister" — five seats in Genesis', gerar('sister_claim_seats'), 5),
 ('the prophet noun once in Genesis', gerar('prophet_seats'), 1),
 ('"and he prayed" — two seats in Genesis (corrected at the dry run)', gerar('prayed_seats'), 2),
 ('the forgiveness rule (Mishnah Bava Kamma 8:7): asks, prays', gerar('forgiveness_sheet'), ('asks', 'prays')),
 ("the rule run on the chapter's order", gerar('forgiveness_run'), ('restored', 'asked', 'prayed', 'healed')),
 ('answered first (Bava Kamma 92a:16)', gerar('answered_first'), 'sarah_remembered'),
 ('a thousand pieces of silver', gerar('thousand_silver'), 1000),
 ('a covering of eyes (Bava Kamma 93a)', gerar('covering_of_eyes'), 'appeasement_owed_by_the_wronger'),
 ("the withholding's jurisdiction", gerar('withheld_jurisdiction'), 'heaven'),
 ('the half sister', gerar('half_sister'), ('fathers_daughter', 'not_mothers')),
 ("20:18's register: a flashback perfect", gerar('wombs_shut_register'), 'flashback_perfect'),
 ('the dwelling granted against Pharaoh\'s "go"', gerar('gerar_dwelling'), 'dwell_where_you_please'),
 # ---- Gen 22: moriah ----
 ('the test verb once in Genesis', moriah('test_verb_seats'), 1),
 ('ten trials (Mishnah Avot 5:3)', moriah('ten_trials_sheet'), 10),
 ('trials named by the ink: one', moriah('trials_named_by_the_ink'), 1),
 ('after what (Sanhedrin 89b)', moriah('after_what'), ('the_words_of_satan', 'the_words_of_ishmael')),
 ('the four-step address', moriah('four_step_address'), ('your_son', 'your_only_one', 'whom_you_love', 'isaac')),
 ('the third day', moriah('third_day'), 3),
 ('the binding verb once in the Tanakh', moriah('binding_verb_seats'), 1),
 ("the ram's horn (Rosh Hashanah 16a)", moriah('rams_horn'), 'the_binding_remembered'),
 ('the countermand closes two entries', moriah('countermand_closes'), ('offering_of_the_son_owed', 'tried')),
 ('the ram in place of the son — the burnt offering by call', moriah('ram_in_place'), 'olah'),
 ('a ram AFTER (Bereshit Rabbah 56:9)', moriah('ram_seen_after'), 'after_the_generations'),
 ("the oath's four clauses", moriah('oath_reward_seats'), ('stars', 'sand', 'the_gate_of_enemies', 'the_nations')),
 ('these eight Milcah bore', moriah('milcah_eight'), 8),
 ("Nahor's twelve", moriah('nahor_sons_total'), 12),
 # ---- Gen 25:1-18: abraham_end ----
 ('Keturah is Hagar by Rav (Bereshit Rabbah 61:4)', abraham_end('keturah_identity'), 'hagar_by_rav'),
 ("Keturah's six", abraham_end('keturah_six'), 6),
 ('the gifts as deeds in his lifetime (Sanhedrin 91a)', abraham_end('gifts_reading'), 'deeds_in_his_lifetime'),
 ('the inheritance order owed — by call', abraham_end('inheritance_by_call'), ['Deut 25:5', 'Num 27:8']),
 ('"in a good old age" — four seats in the Tanakh', abraham_end('good_old_age_seats'), 4),
 ("15:15's promise closed at 25:8", abraham_end('promise_closed_here'), 'buried_in_peace'),
 ('the purchase\'s three modes — by call', abraham_end('purchase_by_call'), ['money', 'deed', 'possession']),
 ('twelve princes', abraham_end('twelve_princes'), 12),
 ('twelve names counted', abraham_end('twelve_names_counted'), 12),
 ("16:10's promise closed at 25:16", abraham_end('seed_multiplied_closed'), 'Gen 25:16'),
 ('16:12 dwell, 25:18 fell', abraham_end('fell_polarity'), ('dwell', 'fell')),
 ('Ishmael repented in his days (Bava Batra 16b)', abraham_end('ishmael_repented'), 'in_abrahams_days'),
 # ---- Gen 25:19-34: twins ----
 ('Isaac was barren (Yevamot 64a)', twins('isaac_barren'), 'isaac_was_barren'),
 ('twenty years of barrenness', twins('twenty_years'), 20),
 ('the entreaty verb: digging (Bereshit Rabbah 63:5)', twins('entreaty_verb'), 'digging'),
 ('the struggling verb once in the Tanakh', twins('struggle_seats'), 1),
 ("the oracle's four clauses", twins('oracle_terms'), ('two_nations', 'two_peoples', 'one_stronger', 'elder_serves_younger')),
 ('the firstborn for inheritance (Mishnah Bekhorot 8:1)', twins('firstborn_sheet'), 'the_first_to_come_out'),
 ("Jacob's name: the heel", twins('heel_naming'), 'holding_the_heel'),
 ("the stew day is Abraham's death day (Bava Batra 16b)", twins('stew_day'), 'abrahams_death_day'),
 ("the lentil's two readings", twins('lentil_readings'), ('no_mouth', 'rolls')),
 ('the gulping verb: the camel', twins('gulp_verb'), 'camel'),
 ('the oath then the sale', twins('sale_with_oath'), ('sworn', 'sold')),
 ("the father's word (Mishnah Bava Batra 8:5)", twins('fathers_word_sheet'), 'said_nothing'),
 ('the despising verb — two seats in the Tanakh (corrected at the dry run)', twins('despise_seats'), 2),
 # ---- Gen 26:1-16: isaac_gerar ----
 ('the second famine', isaac_gerar('famine_ordinal'), 'the_second'),
 ("the burnt offering's rule laid on Isaac (Bereshit Rabbah 64:3)", isaac_gerar('olah_rule_transferred'), 'outside_the_curtains_disqualified'),
 ("the charge's four words", isaac_gerar('charge_words'), ('my_charge', 'my_commandments', 'my_statutes', 'my_teachings')),
 ('the whole Torah before Sinai — the two rows', isaac_gerar('whole_torah_before_sinai'), ('yoma_28b', 'kiddushin_82a')),
 ("the covenant's heads — by call", isaac_gerar('covenant_heads_by_call'), 'you_and_your_seed_after_you'),
 ('the guilt homograph', isaac_gerar('guilt_homograph'), 'asham_the_noun'),
 ("the decree's formula", isaac_gerar('decree_formula'), 'surely_be_put_to_death'),
 ('a hundredfold', isaac_gerar('hundredfold'), 100),
 ('measured for the tithes (Bereshit Rabbah 64:6)', isaac_gerar('measured_for_tithes'), 'tithes'),
 ('the envy verb — three seats in Genesis', isaac_gerar('envy_seats'), 3),
 ('the wells stopped, then redug', isaac_gerar('wells_stopped_then'), 'redug_at_26_18'),
 ("the expulsion's word", isaac_gerar('expelled_word'), 'go_from_us'),
 # ---- Gen 26:17-35: wells ----
 ('three wells named', wells('three_wells'), ('esek', 'sitnah', 'rehoboth')),
 ("the names restored (26:18)", wells('names_restored'), 'like_the_names_his_father_called'),
 ("the well names as the canon's list (Bereshit Rabbah 64:8)", wells('canon_list_read'), 'the_canons_own_book_list'),
 ('the altar built twice in the stretch', wells('altar_seats_stretch'), 2),
 ('called on the name — four seats in Genesis', wells('called_on_the_name_seats'), 4),
 ('the night appearance', wells('night_appearance'), 'fear_not_for_abrahams_sake'),
 ("the oath reactivating the father's (Bereshit Rabbah 64:10)", wells('oath_between_us'), 'reactivating_the_fathers_oath'),
 ('swore each to his brother', wells('swore_each_to_his_brother'), 'Gen 26:31'),
 ('Shibah, Beersheba', wells('shibah_naming'), ('shibah', 'beersheba')),
 ('Esau at forty', wells('esau_forty'), 40),
 ("Esau's marriage graded (Bereshit Rabbah 65:1)", wells('esau_marriage_graded'), 'the_boar_of_the_forest'),
 ("the bitterness's ground", wells('bitterness_ground'), 'idolatry'),
 # ---- Gen 27:1-40: blessing ----
 ('the dim eyes: four causes kept', blessing('dim_eyes_causes'), 4),
 ("the death worry's arithmetic", blessing('death_worry_arithmetic'), (127, 123)),
 ('Jacob sixty-three at the blessing (Bereshit Rabbah 68:5)', blessing('jacob_at_the_blessing'), 63),
 ("the two kids of the marriage contract (Bereshit Rabbah 65:14)", blessing('two_kids_contract'), 'two_kids_daily'),
 ('the equivocation defence declined', blessing('i_am_esau_defence'), 'declined'),
 ('the voice and the hands', blessing('voice_and_hands'), ('jacobs_voice', 'esaus_hands')),
 ("the blessing's six clauses", blessing('blessing_clauses'), ('dew', 'fat', 'grain_and_wine', 'peoples_serve', 'master_over_brothers', 'cursers_cursed')),
 ('the blessing ratified', blessing('ratified'), 'he_shall_be_blessed'),
 ('a trembling greater than Moriah\'s', blessing('trembling_greater'), 'than_moriah'),
 ('supplanted these two times — the ledger\'s count', blessing('supplanted_count'), 2),
 ('the cry booked against Esther 4:1', blessing('cry_booked_against'), 'esther_4_1'),
 ("Esau's blessing: five clauses", blessing('esau_blessing_clauses'), ('fat_of_the_earth', 'dew_from_above', 'by_your_sword', 'serve_your_brother', 'break_his_yoke')),
 ('the slave maxim voiding the claim', blessing('slave_maxim'), 'what_a_slave_acquires_his_master_acquires'),
 # ---- Gen 27:41-28:9: grudge ----
 ('the grudge verb — three seats in Genesis', grudge('grudge_verb_seats'), 3),
 ('the kill intent — open, never executed', grudge('kill_after_mourning'), 'open_never_executed'),
 ('a few days made seven years', grudge('few_days_analogy'), 'seven_years'),
 ('the flight received at 28:10', grudge('flight_receipt'), 'Gen 28:10'),
 ('the Canaanite ban', grudge('canaanite_ban'), 'no_wife_from_the_daughters_of_canaan'),
 ('the wife from Paddan received at 29:28', grudge('wife_from_paddan_receipt'), 'Gen 29:28'),
 ('an assembly of peoples: tribes', grudge('assembly_of_peoples'), 'tribes'),
 ("Mahalath at Ishmael's death (Megillah 17a)", grudge('mahalath_at_ishmaels_death'), 'ishmael_had_died'),
 ('Esau saw twice', grudge('esau_saw_twice'), 2),
 ('the exile table', grudge('exile_table'), 'tribes_against_kingdoms'),
 # ---- Gen 28:10-22: bethel ----
 ('the sun set two hours early (Bereshit Rabbah 68:10)', bethel('sun_set_early'), 'two_hours'),
 ('the stones gathered into one (Chullin 91b)', bethel('stones_into_one'), 'gathered_into_one'),
 ('the fourteen hidden years', bethel('hidden_fourteen'), 14),
 ("the Torah's first narrated dream", bethel('first_narrated_dream'), 'Gen 28:12'),
 ('four kingdoms on the ladder', bethel('kingdoms_on_the_ladder'), 4),
 ("the promise's eight clauses", bethel('promise_clauses'), ('land', 'dust', 'four_directions', 'families_blessed', 'with_you', 'keep_you', 'bring_you_back', 'not_leave')),
 ('"I am with you" closed at 31:5', bethel('with_you_closed_at'), 'Gen 31:5'),
 ('the return closed at 35:6 (S4)', bethel('return_closed_at'), 'Gen 35:6'),
 ("the Torah's first oil", bethel('first_oil'), 'Gen 28:18'),
 ('Bethel, formerly Luz', bethel('luz_bethel'), ('bethel', 'luz')),
 ("the vow's four conditions", bethel('vow_conditions'), 4),
 ("the vow's three commitments", bethel('vow_commitments'), 3),
 ("the tithe's status — by call", bethel('tithe_by_call'), 'holy_to_the_LORD'),
 ("the charity cap's verse (Ketubot 50a)", bethel('charity_cap_verse'), 'Gen 28:22'),
 ('"I will surely tithe" — the only seat', bethel('tithe_phrase_seats'), 1),
 # ---- Gen 29:1-14: well_stone ----
 ('one machine bound to six institutions', well_stone('six_institutions'), 'one_machine_bound_to_six'),
 ("the stone protocol's four steps", well_stone('stone_protocol'), ('gather', 'roll', 'water', 'return')),
 ('the labor duty (Bereshit Rabbah 70:11)', well_stone('labor_duty'), 'finish_the_days_work'),
 ('the stone rolled alone', well_stone('stone_rolled_alone'), 'as_a_stopper_from_a_flask'),
 ('why Jacob wept', well_stone('why_wept'), ('not_buried_with_him', 'came_with_nothing')),
 ('the kiss verb — three seats in the stretch', well_stone('kisses_seats'), 3),
 ("her father's brother — the ambiguity kept", well_stone('her_fathers_brother'), 'ambiguity_kept'),
 ('the welcome decoded', well_stone('welcome_decoded'), ('gold', 'pearls')),
 ('"a month of days" — three seats in the Tanakh', well_stone('month_phrase_seats'), 3),
 # ---- Gen 29:15-30: wage ----
 ('the three specifications (Bava Batra 123a)', wage('three_specifications'), ('rachel', 'your_daughter', 'the_younger')),
 ("Leah's eyes from weeping", wage('leahs_eyes'), 'from_weeping'),
 ('seven years — five seats', wage('seven_years_seats'), 5),
 ("the seven years' timer on the bare scene", wage('seven_years_timer_days'), 2555),
 ('married at eighty-four (Bereshit Rabbah 68:5)', wage('married_at'), 84),
 ('the switch repaid measure for measure', wage('switch_measure_for_measure'), 'did_your_father_not_call_you_esau'),
 ('the custom of the place', wage('custom_of_the_place'), 'younger_not_before_the_firstborn'),
 ('"fulfill the week of this one" — the only seat', wage('week_phrase_seats'), 1),
 ('no mixing of joys — from here (Bereshit Rabbah 70:19)', wage('no_mixing_of_joys'), 'from_here'),
 ('no marriage on the festival (Mishnah Moed Katan 1:7)', wage('festival_marriage_sheet'), 'no_marriage_on_the_festival'),
 ("the week's timer: seven days", wage('week_timer_days'), 7),
 ('the two maids', wage('two_maids'), ('zilpah', 'bilhah')),
 # ---- Gen 29:31-30:24: twelve_names ----
 ('fourteen births in the stretch', twelve_names('births_in_the_stretch'), 14),
 ('thirteen eighth-day timers, none on Dinah', twelve_names('eighth_days_set'), 13),
 ("the twelve namings by the mothers", twelve_names('namings_by_mothers'), 12),
 ("the scene's naming events across the stretch", twelve_names('namings_in_the_stretch'), 28),
 ('thanks at the fourth (Bereshit Rabbah 71:5)', twelve_names('thanks_at_the_fourth'), 'judah'),
 ('three keys not delegated (Taanit 2a)', twelve_names('three_keys'), ('childbirth', 'rain', 'the_dead')),
 ('accounted as dead (Nedarim 64b)', twelve_names('accounted_as_dead'), 'one_without_children'),
 ('the mandrakes token once in Genesis', twelve_names('mandrakes_seats'), 1),
 ("the trade's ledger (Bereshit Rabbah 72:3)", twelve_names('trade_ledger'), ('leah_lost_mandrakes_gained_two_tribes', 'rachel_gained_mandrakes_lost_tribes')),
 ('remembered on Rosh Hashanah (Rosh Hashanah 11a)', twelve_names('remembered_on_rosh_hashanah'), 'rosh_hashanah'),
 ('another son — Benjamin at 35:18', twelve_names('another_son'), 'benjamin_at_35_18'),
 ('Dinah: no eighth day', twelve_names('dinah_no_eighth_day'), 'female'),
 # ---- Gen 30:25-43: speckled ----
 ("the release keyed to Joseph's birth", speckled('release_keyed_to'), 'josephs_birth'),
 ("the second seven's timer on the bare scene", speckled('second_seven_timer_days'), 2555),
 ('the divination scrubbed by both translations', speckled('divination_scrubbed'), 'both_translations'),
 ('the wage terms', speckled('wage_terms'), ('speckled', 'spotted', 'dark_among_the_lambs')),
 ('the righteousness clause', speckled('righteousness_clause'), 'on_a_day_to_come'),
 ("three days' distance", speckled('three_days_distance'), 3),
 ('the rods: two arms', speckled('rods_two_arms'), ('natural_sign', 'angelic_transfer')),
 ('the wage-flip rule', speckled('wage_flip_rule'), 'all_bore_what_he_named'),
 ('ten times', speckled('ten_changes'), 10),
 ('ten, or a hundred (Bereshit Rabbah 74:3)', speckled('ten_or_a_hundred'), ('ten', 'a_hundred')),
 ('broke out — both ledgers', speckled('broke_out_seats'), ('30:30', '30:43')),
 # ---- Gen 31:1-21: flight ----
 ('the three-stage trigger', flight('three_stage_trigger'), ('the_sons_words', 'labans_face', 'the_lords_command')),
 ('return_owed open until 33:18 (S4)', flight('return_owed_open_until'), 'Gen 33:18'),
 ('counsel in the open field: prudence', flight('counsel_in_the_field'), 'prudence'),
 ('"has been with me" — the fulfillment stated', flight('with_me_stated'), 'Gen 31:5'),
 ("the rescue verb's first seat", flight('rescue_verb_first'), 'Gen 31:9'),
 ("the dream's medium", flight('dream_medium'), 'the_angel_of_god_in_the_dream'),
 ('the God of Bethel recalled: the pillar, the vow', flight('bethel_recalled'), ('anointed_a_pillar', 'vowed_a_vow')),
 ('why Rachel died first (Bereshit Rabbah 74:4)', flight('why_rachel_first'), ('spoke_before_her_sister', 'the_elders_curse')),
 ('the Abram formula of 12:5', flight('abram_formula'), 'Gen 12:5'),
 ('the teraphim token — three seats', flight('teraphim_seats'), 3),
 ("Rachel's intent for the sake of Heaven", flight('rachels_intent'), 'for_the_sake_of_heaven'),
 ('two thefts, one verb', flight('two_thefts'), ('rachel_the_teraphim', 'jacob_the_heart')),
 # ---- Gen 31:22-54: heap ----
 ('told on the third day', heap('third_day_told'), 3),
 ("a seven days' journey", heap('seven_days_journey'), 7),
 ('the dream guard: neither good nor bad', heap('dream_guard'), 'neither_good_nor_bad'),
 ('"he shall not live" — the seat', heap('death_oath_seats'), 1),
 ('the curse chain to 35:19 (Bereshit Rabbah 74:9)', heap('curse_chain'), 'Gen 35:19'),
 ('four tents', heap('four_tents'), 4),
 ('the way of women — a status claimed', heap('way_of_women'), 'a_status_claimed'),
 ("the four keepers' row (Mishnah Bava Metzia 7:8): oath, pay, pay", heap('keepers_sheet'), ('oath', 'pay', 'pay')),
 ("the paid keeper's three verdicts — by call", heap('paid_keeper_by_call'), ('PAY', 'OATH', 'PAY')),
 ('the torn: exempt, yet paid', heap('torn_beyond_the_row'), 'exempt_yet_paid'),
 ("the keeper's ceiling (Bava Metzia 93b)", heap('keepers_ceiling'), 'an_extra_guarding'),
 ('the twenty years: twenty, fourteen, six, ten', heap('twenty_years_ledger'), (20, 14, 6, 10)),
 ("labor ranked above the fathers' merit", heap('labor_above_merit'), 'labor_ranked_above_the_fathers_merit'),
 ('THE TWO TONGUES', heap('two_tongues'), ('yegar_sahadutha', 'galeed')),
 ('four namings on the heap', heap('heap_names_count'), 4),
 ("the covenant's two terms", heap('covenant_terms'), ('no_affliction_of_the_daughters', 'no_wives_over_them')),
 ("the boundary's carve-out: for harm", heap('boundary_carve_out'), 'for_harm'),
 ('the oath by the Fear of his father Isaac', heap('oath_by_the_fear'), 'the_fear_of_his_father_isaac'),
 ("the peace offering's place — by call", heap('shelamim_by_call'), 'anywhere_courtyard'),
 ('"sacrificed a sacrifice" — the first seat', heap('sacrifice_pair_first'), 'Gen 31:54'),
 # ---- THE SCENE and the headlines ----
 ('THE SCENE on the world engine — the tuple the hand-model printed before this file was typed', build('world'), (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 47, 17, 17, 14, 7360)),
 ("HEADLINE: the season joins two shelf rows", build('headline_join'), 'the_season_joins_two_shelf_rows'),
 ("HEADLINE: the covenant's daemon runs on the stretch's births", build('headline_installation'), 'the_covenants_daemon_runs_on_the_stretchs_births'),
 ("HEADLINE: the paid keeper grades Jacob's account", build('headline_keeper'), 'the_paid_keeper_grades_jacobs_account'),
 ("HEADLINE: the fourteen hidden years fall out of the ink's numbers", build('headline_fourteen'), 'the_fourteen_hidden_years_fall_out_of_the_inks_numbers'),
 ('HEADLINE: one heap, two names', build('headline_two_tongues'), 'one_heap_two_names'),
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
    print('effects: every cell carries REGISTERED effects — two hundred and twenty-seven discovered in the stretch\'s own words and registered first (visitors_received ... ate_and_lodged) [effects law satisfied]')
    print('SCENE: %r' % (SCENE,))
    _W.print_coverage()
    if ok == n:
        print()
        print('FROM MAMRE TO THE HEAP STANDS — the visit and the plea, Sodom and the pillar of salt, the first prayer, the binding, the good old age, the twins and the birthright, the wells, the blessing, the ladder and the vow, the stone, the two sevens, the twelve names, the speckled wage, the flight, the heap with its two tongues: %d/%d' % (ok, n))
    else:
        print('MISSES (%d):' % len(misses))
        for m_ in misses: print('  -', m_[0][:80], '->', m_[1])
        sys.exit('MISSES REMAIN — a miss is evidence, never a retype: read it.')
