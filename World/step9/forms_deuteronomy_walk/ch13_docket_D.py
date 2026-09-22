# THE DEUTERONOMY WALK 11b — THE EXAM DOCKET OF CHAPTER 13, part D: the dump's rows 422-565 — Menachot 42a:13-23 (the fringes' blessing — outside), Rosh
# Hashanah 28b, Eruvin 96a and Avodah Zarah 49b (CARRIED whole from chapters 4 and 7), Avodah Zarah 50a (MERCURY'S STONES — the benefit ban's edges), Bava
# Metzia 59b (CARRIED — the oven of Akhnai), Yevamot 90b (ELIJAH AT CARMEL — the temporary uprooting heeded), Shabbat 151b (the mercy row's range), the
# Tosefta and Sifrei whole-chapter rows. The credited rows CARRIED (CREDITED_SPEC); the uncredited READ WHOLE HERE (ch13_uncred_03.txt); the unresolved
# credited (the Sifrei's three, Tosefta Sanhedrin 11:1 and 11:3, Menachot 42a:18-19, Yevamot 90b:12-13, Shabbat 151b:9) in ch13_docket_U.py. The verdicts
# and the cells as in part A. 10b's form.
from ch13_docket_common import R, build, apply_whole, CREDITED_SPEC
from ch13_docket_U import OWN_U
OWN = [
 ('Menachot 42a:13', 'OUTSIDE', "Rav Nachman to Rav Adda bar Ahava: no blessing on making fringes (Rav): the fringes' blessing, outside the chapter."),
 ('Menachot 42a:14', 'OUTSIDE', "Rav Chisda's contradiction: a gentile's fringes unfit ('the children of Israel … shall make'): outside the chapter."),
 ('Menachot 42a:15', 'OUTSIDE', "Rav Yosef's principle: fit by a gentile — no blessing; unfit by a gentile — a blessing: outside the chapter."),
 ('Menachot 42a:16', 'OUTSIDE', "circumcision by a gentile valid (R. Meir / R. Yehuda on the Aramean and the Samaritan): outside the chapter."),
 ('Menachot 42a:17', 'OUTSIDE', "yet the Jew blesses on circumcision: outside the chapter."),
 ('Menachot 42a:20', 'OUTSIDE', "the booth supports Rav Chisda, the phylacteries refute him: outside the chapter."),
 ('Menachot 42a:21', 'OUTSIDE', "a booth by gentiles, women, cattle or Samaritans fit if roofed by the rule: outside the chapter."),
 ('Menachot 42a:22', 'OUTSIDE', "the builder blesses 'who has kept us alive', not 'to build a booth': outside the chapter."),
 ('Menachot 42a:23', 'OUTSIDE', "phylacteries by a gentile unfit (cut at the folio's end): outside the chapter."),
 ('Avodah Zarah 50a:1', 'DERIVATION', "stones near Mercury's pile that surely fell from it — all agree PROHIBITED; the dispute is the distant ones: F5 — the benefit ban's edge: idolatry's cast-off stones; devoted_thing_cleaving_barred's kin (Mishnah Avodah Zarah 4:1); a DATA row."),
 ('Avodah Zarah 50a:2', 'DERIVATION', "'at the side of Mercury' — within its four cubits: F5 — the proximity's measure a datum; a DATA row."),
 ('Avodah Zarah 50a:3', 'DERIVATION', "R. Yishmael: a small pile is built beside a large — three stones a pile, prohibited; two permitted; the Rabbis: no small pile — seen with it prohibited, not seen permitted: F5 — the stones' arms (three / seen with it); a DATA row."),
 ('Avodah Zarah 50a:4', 'DERIVATION', "R. Yochanan's baraita — 'fell from it' read 'found beside it' (Rava): F5 — the reading; a DATA row."),
 ('Avodah Zarah 50a:5', 'DERIVATION', "does R. Yishmael permit two beside it? his baraita: two in its area prohibited, three even far: F5 — a DATA row."),
 ('Avodah Zarah 50a:6', 'DERIVATION', "Rava: one area / two areas (an elevation between): F5 — a DATA row."),
 ('Avodah Zarah 50a:7', 'DERIVATION', "are adjacent stones a pile? the pile's form (one, one, one atop) is the main pile's; the added stones any way: F5 — a DATA row."),
 ('Avodah Zarah 50a:8', 'CONTEXT', "King Yannai's ruined house, Mercury's stones, the paths paved with them; some Rabbis withdrew, some not: F5 — the run's case; a DATA row."),
 ('Avodah Zarah 50a:9', 'CONTEXT', "R. Yochanan: the son of holy ones (R. Menachem son of R. Simai, who looked at no coin's image) walks on them: F5 — a DATA row."),
 ('Avodah Zarah 50a:10', 'DERIVATION', "the one who withdraws: Rav — AN IDOLATROUS OFFERING IS NEVER NULLIFIED, 'they ate the offerings of the dead' (Psalms 106:28) — as the dead is never released, so the offering: F5 — devoted_thing_cleaving_barred's PERMANENCE (no nullification of an offering to an idol); balak.peor by CALL for Baal Peor; a DATA row."),
 ('Avodah Zarah 50a:11', 'DERIVATION', "the one who does not withdraw: an idol's offering is only what has a parallel inside the Temple — stones are not offered: F5 — the offering's definition bounds the permanence; a DATA row."),
 ('Avodah Zarah 50a:12', 'CONTEXT', "Rabba bar Yirmeya's baraita: a gentile who paved paths and theaters with Mercury's stones — (cut at the folio's end): F5 — a DATA row."),
 ('Yevamot 90b:1', 'OUTSIDE', "Rav Chisda's list: the convert on Passover eve, the sprinkling on the Sabbath — decrees that neglect a Torah duty by 'sit and refrain': the Sages' power, outside the chapter."),
 ('Yevamot 90b:2', 'OUTSIDE', "the circumcision knife on the Sabbath, the linen cloak's fringes: outside the chapter."),
 ('Yevamot 90b:3', 'OUTSIDE', "the Shavuot lambs' blood, the ram's horn on the Sabbath: outside the chapter."),
 ('Yevamot 90b:4', 'OUTSIDE', "the palm branch on the Sabbath — all 'sit and refrain', no uprooting: outside the chapter."),
 ('Yevamot 90b:5', 'LAW', "'to him you shall listen' (18:15) — even if the prophet says TRANSGRESS ONE OF THE TORAH'S COMMANDMENTS, like ELIJAH AT CARMEL (an offering outside the Temple under the penalty of karet — excision), for the requirement of the hour: HEED HIM: F2 — 85:4 AT ITS BAVLI SEAT ('His voice' the prophets' — the true prophet's temporary uprooting heeded); the_signs_status's boundary (Sanhedrin 90a:10: heed except idolatry); Elijah the exam's exempt person; 18:15 ahead."),
 ('Yevamot 90b:6', 'LAW', "there it is different: 'to him you shall listen' a positive command overriding a prohibition; why not derive the Sages' power? SAFEGUARDING A MATTER is different — Elijah acted to keep Israel from idolatry: F2 — the uprooting's two grounds (the command to heed; the safeguard against idolatry the chapter's own matter); the exam's row."),
 ('Yevamot 90b:7', 'OUTSIDE', "the bill of divorce cancelled before a court without her knowledge — Rabbi / Rabban Shimon ben Gamliel: outside the chapter."),
 ('Yevamot 90b:8', 'OUTSIDE', "'what good is the court's power' — the betrothal on the Sages' authority: outside the chapter."),
 ('Yevamot 90b:9', 'OUTSIDE', "betrothal by money or by relations: outside the chapter."),
 ('Yevamot 90b:10', 'DERIVATION', "R. Elazar ben Yaakov: the court flogs and punishes beyond Torah law AS A SAFEGUARD — the man who rode a horse on the Sabbath in the Greeks' days STONED, 'because the hour required it': F2 — the hour's requirement the same ground as Elijah's (the court's emergency stoning a run citation outside the tape; mekoshesh by CALL for the rite); a DATA row."),
 ('Yevamot 90b:11', 'DERIVATION', "the man under the fig tree flogged, 'the hour required it'; the court can uproot by an act — safeguarding is different: F2 — the doublet; a DATA row."),
 ('Yevamot 90b:14', 'OUTSIDE', "her found articles — the enmity's reason: the mishnah's tail (the remarried woman), outside the chapter."),
 ('Yevamot 90b:15', 'OUTSIDE', "her earnings — she eats his food: outside the chapter."),
 ('Yevamot 90b:16', 'OUTSIDE', "her vows — let her be repulsive: outside the chapter."),
 ('Yevamot 90b:17', 'OUTSIDE', "an Israelite woman disqualified from the priesthood: outside the chapter."),
 ('Shabbat 151b:1', 'OUTSIDE', "the corpse's jaw tied, the broken beam supported — not raised: the range's matter before the mercy row, outside the chapter."),
 ('Shabbat 151b:2', 'OUTSIDE', "rinsing and oiling a corpse on the Sabbath — R. Meir's student in the bathhouse: outside the chapter."),
 ('Shabbat 151b:3', 'OUTSIDE', "'all the needs of the dead' — cold vessels on the stomach, the orifices sealed: outside the chapter."),
 ('Shabbat 151b:4', 'OUTSIDE', "Ecclesiastes 12:6 on the body's parts: outside the chapter."),
 ('Shabbat 151b:5', 'OUTSIDE', "Malachi 2:3's dung; the stomach bursts on the third day: outside the chapter."),
 ('Shabbat 151b:6', 'OUTSIDE', "MISHNAH: the eyes of the dead not shut on the Sabbath; shutting them as the soul departs — a murderer: outside the chapter."),
 ('Shabbat 151b:7', 'OUTSIDE', "the lamp about to go out; Rabban Shimon ben Gamliel's wine and oil: outside the chapter."),
 ('Shabbat 151b:8', 'OUTSIDE', "the Sabbath desecrated for a day-old child, not for dead David — 'free among the dead' (Psalms 88:6): outside the chapter."),
 ('Shabbat 151b:10', 'OUTSIDE', "a lion does not pounce on two; the animal and the man's honor (Psalms 49:13); sleeping alone: outside the chapter."),
 ('Shabbat 151b:11', 'OUTSIDE', "R. Shimon ben Elazar: perform commandments while you can; 'the evil days' (Ecclesiastes 12:1) the days of the Messiah: outside the chapter."),
 ('Shabbat 151b:12', 'OUTSIDE', "Shmuel: no difference but the subjugation — 'the poor will never cease' (15:11): 15:11's matter, outside the chapter."),
 ('Shabbat 151b:13', 'CONTEXT', "R. Elazar HaKappar: pray against poverty — 'due to this thing' (15:10) a WHEEL that turns (R. Yishmael's school); a scholar never begs at doors: F5 — the wheel the mercy row's frame (151b:14 quotes it); 15:10 ahead; a DATA row."),
 ('Shabbat 151b:15', 'OUTSIDE', "Ecclesiastes 12:2's sun, moon and clouds on the face; Shmuel on tears after forty: outside the chapter."),
 ('Shabbat 151b:16', 'OUTSIDE', "Rav Nachman on eye shadow after forty: outside the chapter."),
 ('Shabbat 151b:17', 'OUTSIDE', "R. Chanina's daughter and the six tears (cut at the folio's end): outside the chapter."),
 ('Tosefta Sanhedrin 11:2', 'OUTSIDE', "R. Akiva learned two things of magic from R. Eliezer's three hundred — the two cucumber gatherers (Mishnah Sanhedrin 7:11): the sorcerer's matter, outside the chapter (the row's English begins and ends in ellipses — the export's cut)."),
 ('Tosefta Sanhedrin 12:1', 'CONTEXT', "THE EXPORT'S ROW IS EMPTY (Tosefta Sanhedrin 12:1): read as empty; the chapter's matter (the honors — 91:4) reached through the Sifrei's note; a DATA row on the shelf."),
 ('Tosefta Sanhedrin 12:2', 'CONTEXT', "THE EXPORT'S ROW IS EMPTY (Tosefta Sanhedrin 12:2): read as empty; a DATA row on the shelf."),
 ('Tosefta Sanhedrin 12:3', 'CONTEXT', "THE EXPORT'S ROW IS EMPTY (Tosefta Sanhedrin 12:3): read as empty; a DATA row on the shelf."),
 ('Tosefta Sanhedrin 12:4', 'CONTEXT', "THE EXPORT'S ROW IS EMPTY (Tosefta Sanhedrin 12:4): read as empty; a DATA row on the shelf."),
 ('Tosefta Sanhedrin 12:5', 'OUTSIDE', "the Rabbis added to those without a share: one who casts off the yoke of the commandments, who voids the covenant, who misinterprets the Torah; R. Akiva: the one who sings the Song of Songs at a feast; the whisperer over a wound: Mishnah 10:1's list, outside the chapter ('casts off the yoke' the kin of 111b:15's 'without a yoke' — a DATA row)."),
]
SPEC = CREDITED_SPEC + OWN_U + OWN
ROWS = build(SPEC, 422, 566)
WHOLE = {}
ROWS, WHOLE_STATS = apply_whole(ROWS, WHOLE)
