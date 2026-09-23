# THE DEUTERONOMY WALK 13b — THE EXAM DOCKET OF CHAPTER 15, part E (D1): BAVA METZIA 31b WHOLE (the doubled verbs of 15:8, 10, 11, 14 and their dissenters; the
# pledge and the finder OUTSIDE), BAVA METZIA 71a WHOLE (the precedence ladder, the convert and the woman as buyers of a Hebrew slave, the pierced slave's term
# the master's life; the interest OUTSIDE) and KETUBOT 67b WHOLE (the measure of need — Hillel's horse, the litra, the two persons; the secret givers) — READ WHOLE
# HERE (ch15_uncred_d1_01.txt's tail, ch15_uncred_d1_02.txt; the unresolved rows in the U file). Every D1 address whose first seat is a TOPIC row of Bava Metzia
# or Ketubot. The verdicts and the cells as in part A. 12b's form.
from ch15_docket_common import R, build_set, apply_whole, CREDITED_SPEC, D1_UNIQUE, KIND_FIRST
from ch15_docket_U import OWN_U
OWN = [
 # Bava Metzia 31b
 ('Bava Metzia 31b:1', 'OUTSIDE', "unloading and loading with the owner present — why both verses: the range's opening (22:4 ahead); no bearing on the chapter."),
 ('Bava Metzia 31b:4', 'DERIVATION', "'hashev tashiv' (24:13's doubled 'restore') — the pledge returned at night even when taken without the court: OUTSIDE the chapter (the pledge's law — ordinances.loan(pledge_sunset) by CALL; 24:13 ahead); a DATA row."),
 ('Bava Metzia 31b:6', 'DERIVATION', "the two verses (Exodus 22:25, 24:13) — the day's garment and the night's: OUTSIDE; a DATA row."),
 ('Bava Metzia 31b:10', 'DISPUTE', "R. Elazar ben Azarya: the gift only when the house was blessed because of him; the doubled 'furnish' — 'the Torah speaks in the language of men': F4 — furnishing_commanded's CONDITION — the arms (the Sages unconditional, 31b:9; R. Elazar ben Azarya conditional): the_gift_feature's kin; the exam's arm."),
 ('Bava Metzia 31b:12', 'DISPUTE', "R. Shimon: the one with means who will not use them — no obligation to lend; the doubled 'lend' the language of men: F3 — lending_is_obligation's REACH: the arms (Ketubot 67b:9's R. Shimon); the exam's arm."),
 ('Bava Metzia 31b:13', 'OUTSIDE', "the finder's wage 'as an idle laborer' (Tosefta Bava Metzia 2:11): no bearing."),
 ('Bava Metzia 31b:14', 'OUTSIDE', "Abaye's definition of the idle laborer's wage: no bearing."),
 ('Bava Metzia 31b:15', 'OUTSIDE', "Issur and Rav Safra's partnership dissolved before two — the court of three: no bearing."),
 # Bava Metzia 71a
 ('Bava Metzia 71a:1', 'CONTEXT', "interest lent to a resident alien only to the lender's livelihood, not as a business: OUTSIDE the release — the interest's law (yovel.interest_scope by CALL; 15:3's foreigner the kin); a DATA row."),
 ('Bava Metzia 71a:2', 'CONTEXT', "Ravina: Torah scholars may lend to a gentile at interest — the decree's reason 'lest he learn from him': OUTSIDE; a DATA row."),
 ('Bava Metzia 71a:4', 'LAW', "a Jew and a gentile come to borrow — the Jew first, even a free loan to him over an interest loan to the gentile: F3 — the_needy_ranks' FIRST RUNG at its seat (the ladder's ground 71a:3 in the U file); the exam's row."),
 ('Bava Metzia 71a:5', 'CONTEXT', "R. Yosei: the usurers' blindness — the witnesses and the scribe sign 'he denies the God of Israel': OUTSIDE (the interest's lore); a DATA row."),
 ('Bava Metzia 71a:6', 'CONTEXT', "R. Shimon ben Elazar: the usurer's property collapses and does not rise (Psalms 15:5): OUTSIDE; a DATA row."),
 ('Bava Metzia 71a:7', 'CONTEXT', "Habakkuk 1:13 — the more righteous swallowed for the moment: the lore; OUTSIDE."),
 ('Bava Metzia 71a:8', 'CONTEXT', "Rabbi: the convert at the Hebrew slave's sale and the resident alien at the interest — 'I do not know their meaning': F4 — the sale's persons asked (Leviticus 25:47 — the convert as buyer); a DATA row."),
 ('Bava Metzia 71a:9', 'DERIVATION', "'sold unto you' (Leviticus 25:39) — even to a convert, 'and sells himself to a stranger' (25:47): F4 — the buyer's persons (yovel.hebrew_slave by CALL); a DATA row."),
 ('Bava Metzia 71a:10', 'DERIVATION', "the sale to a resident alien, to a gentile, to idolatry's temple — Leviticus 25:47's clauses: F4 — the sale's ROAD's buyers (the_three_cases' kin — the court's sale here, the self-seller there); a DATA row."),
 ('Bava Metzia 71a:11', 'DERIVATION', "the contradiction — a convert not acquired as a Hebrew slave; A WOMAN OR A CONVERT MAY NOT ACQUIRE ONE: F4 — the institution's persons (15:12's 'Hebrew woman' the SOLD, never the buyer); a DATA row."),
 ('Bava Metzia 71a:12', 'LAW', "the convert has no family to return to (Leviticus 25:41); the woman barred for modesty; the convert by tradition — 'only one who can be acquired acquires': F4 — the_hebrew_slave's PERSONS (the buyer and the sold) at their seat; the exam's row."),
 ('Bava Metzia 71a:13', 'DERIVATION', "Rav Nachman bar Yitzchak: the convert acquires him as a gentile does, not as a Jew: F4 — the buyer's rank; a DATA row."),
 ('Bava Metzia 71a:14', 'LAW', "the baraita: the PIERCED slave and the slave sold to a gentile serve neither the master's son nor his daughter — freed at his death: F5 — serves_for_ever's TERM the master's life, not his heirs (122:8's 'the son not the daughter … the pierced no heir'; the_for_ever); the exam's row."),
 ('Bava Metzia 71a:15', 'CONTEXT', "the woman acquiring slaves — maidservants yes, male slaves no; R. Shimon ben Gamliel: male too — the Canaanite; the Hebrew barred: F4 — the woman as buyer, the arms; a DATA row."),
 ('Bava Metzia 71a:16', 'CONTEXT', "the Hebrew discreet in her eyes, the Canaanite indiscreet: a DATA row."),
 ('Bava Metzia 71a:17', 'OUTSIDE', "the widow's dog and the lodging student (Rav Yosef's baraita): no bearing."),
 ('Bava Metzia 71a:18', 'CONTEXT', "Rabbi's second difficulty — the resident alien at the interest (Leviticus 25:35-36) against the mishnah's permission: OUTSIDE the release — the interest's persons (yovel.interest_scope by CALL); a DATA row."),
 ('Bava Metzia 71a:19', 'DERIVATION', "'do not take from HIM' (singular) — from a Jew: OUTSIDE; a DATA row."),
 ('Bava Metzia 71a:20', 'DERIVATION', "'from him' — but one may be a guarantor for the alien's interest: OUTSIDE; a DATA row."),
 # Ketubot 67b
 ('Ketubot 67b:4', 'CONTEXT', "the Upper Galilee's poor nobleman of Tzippori — a litra (a weight) of meat daily: poultry, or a litra of coins, or an animal a day for him: F3 — the_measure_of_need's litra (116:17's Sifrei case at its Bavli seat); a DATA row."),
 ('Ketubot 67b:5', 'CONTEXT', "R. Nechemya's lentils killed the pampered pauper — 'woe to the one killed by Nechemya', the pauper to blame: F3 — the measure's edge (the pauper's own habit); a DATA row."),
 ('Ketubot 67b:6', 'CONTEXT', "Rava's pauper — a fattened hen and aged wine; 'from the Merciful One's support' (Psalms 145:15 'in its time'): a DATA row."),
 ('Ketubot 67b:7', 'CONTEXT', "Rava's sister's gift of the same — 'I have responded to you; arise and eat': a DATA row."),
 ('Ketubot 67b:8', 'DISPUTE', "the one without means who refuses charity — a loan then a gift (R. Meir); a gift then a loan (the Rabbis; Rava: begin as a gift, then a loan treated as a gift): F3 — the_measure_of_need's PERSON (a): the arms (Ketubot 67b:10's R. Yehuda the link row); the exam's arm."),
 ('Ketubot 67b:9', 'DISPUTE', "the one with means who refuses — a gift, then collected from his estate after death (Rav Pappa); R. Shimon: no involvement with him; the one without — 'bring a pledge' to raise his mind: F3 — the person (b)'s arms; the exam's arm."),
 ('Ketubot 67b:11', 'DISPUTE', "the Rabbis: the one with means — no involvement; the doubled 'ha'avet ta'avitenu' the language of men: F3 — the doubled verb's reading (Bava Metzia 31b:12's twin); the exam's arm."),
 ('Ketubot 67b:12', 'CONTEXT', "Mar Ukva's four dinars daily in the door's slot; the pauper's watch: F3 — THE SECRET GIFT (117:7's chamber of the silent — Mishnah Shekalim 5:6 carried); a DATA row."),
 ('Ketubot 67b:13', 'CONTEXT', "Mar Ukva and his wife in the furnace — her aid readier, food not money: a DATA row."),
 ('Ketubot 67b:15', 'CONTEXT', "the four hundred dinars on Yom Kippur eve — the old wine spilled for scent: 'he needs even more' — doubled: F3 — the measure by the man's habit (the_measure_of_need's edge); a DATA row."),
 ('Ketubot 67b:16', 'CONTEXT', "Mar Ukva dying gives half his money; Usha's fifth applies only in life: F3 — the giver's cap (OUTSIDE the chapter's write — the fund's rule); a DATA row."),
 ('Ketubot 67b:17', 'CONTEXT', "R. Abba's coins over the shoulder — the poor unembarrassed, the swindlers watched: F3 — the secret gift's second seat; a DATA row."),
 ('Ketubot 67b:18', 'CONTEXT', "R. Chanina's four dinars every Sabbath eve — 'the man does not need it' (the chunk's end at 68a:1, the link row): a DATA row."),
]
SPEC = CREDITED_SPEC + OWN_U + OWN
ROWS = build_set(SPEC, [a for a in D1_UNIQUE if KIND_FIRST[a] == 'TOPIC' and (a.startswith('Bava Metzia ') or a.startswith('Ketubot '))])
WHOLE = {}
ROWS, WHOLE_STATS = apply_whole(ROWS, WHOLE)
