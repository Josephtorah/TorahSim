# THE DEUTERONOMY WALK 13b — THE EXAM DOCKET OF CHAPTER 15, part D (D1): MAKKOT 3b WHOLE (the ten-year loan's two versions, the stipulation against the release,
# the thirty days from 15:9; the Shabbat and the ritual bath OUTSIDE) and ROSH HASHANAH 8b-9a WHOLE (the New Year of the jubilee, the slaves crowned till Yom
# Kippur, the fiftieth alone; the judgment day and the extensions OUTSIDE) — READ WHOLE HERE (ch15_uncred_d1_01.txt; the unresolved rows in the U file). Every
# D1 address whose first seat is a TOPIC row of Makkot or Rosh Hashanah. The verdicts and the cells as in part A. 12b's form.
from ch15_docket_common import R, build_set, apply_whole, CREDITED_SPEC, D1_UNIQUE, KIND_FIRST
from ch15_docket_U import OWN_U
OWN = [
 # Makkot 3b
 ('Makkot 3b:2', 'DERIVATION', "Rav Kahana's objection from the mishnah's estimate (the conspiring witnesses on a ten-year loan — the difference between thirty days and ten years): if released, the whole sum: F1 — the term edge's arm (a) tested on Mishnah Makkot 1:1's calculation; a DATA row."),
 ('Makkot 3b:3', 'DERIVATION', "Rava: the mishnah's loan is one on a pledge, or notes handed to the court (Mishnah Sheviit 10:2) — not released: F1 — the exceptions applied; a DATA row."),
 ('Makkot 3b:4', 'DISPUTE', "the other version — Shmuel: the ten-year loan is NOT released, since 'he shall not exact' is not read of it now: F1 — the_release_object's term edge, arm (b) (Makkot 3a:15 the link row's arm (a)); the exam's arm."),
 ('Makkot 3b:5', 'DERIVATION', "Rav Kahana: the mishnah proves it — the witnesses do not pay the whole sum: a DATA row."),
 ('Makkot 3b:6', 'DERIVATION', "Rava: no proof — the mishnah's loan on a pledge or the court's notes: a DATA row."),
 ('Makkot 3b:7', 'LAW', "Shmuel: 'on the condition that the seventh year will not abrogate my debt' — abrogated nonetheless: a stipulation against what is written in the Torah?: F1 — THE RELEASE NOT WAIVABLE BY A STIPULATION IN ITS FORM (3b:10 the split); the exam's row."),
 ('Makkot 3b:8', 'CONTEXT', "Rav and Shmuel on 'no claim of exploitation against me' — Shmuel: a monetary waiver valid: the objection; a DATA row."),
 ('Makkot 3b:9', 'DERIVATION', "Rav Anan: the formulation decides — 'no claim against me' valid, 'no exploitation in this sale' void: a DATA row."),
 ('Makkot 3b:10', 'LAW', "'on the condition that YOU will not abrogate the debt' — valid (the borrower waives his money); 'that the seventh year will not abrogate' — void: F1 — debt_release_owed's WAIVER RULE (the debtor's waiver a data row; the year's law unmovable — the code/data line at the Bavli); the exam's row."),
 ('Makkot 3b:11', 'LAW', "the unspecified loan — no demand within thirty days, with a note or oral (R. Chiyya to Rav): F1 — the loan's MINIMUM TERM (15:9's derivation at 3b:14 — the link row); the loan's law by CALL to ordinances.loan; the exam's row."),
 ('Makkot 3b:12', 'DERIVATION', "the baraita the same — thirty days, note or oral: a DATA row."),
 ('Makkot 3b:13', 'CONTEXT', "Shmuel to Rav Mattana: 'do not sit until you explain it' — the question 3b:14 answers from 15:9: a DATA row."),
 ('Makkot 3b:15', 'OUTSIDE', "the shirt's neck opening on Shabbat (a sin-offering); the barrel's stopper: the range's tail — Rav Yehuda's sayings; no bearing."),
 ('Makkot 3b:16', 'OUTSIDE', "three log of drawn water with a kortov (a small measure) of wine — the ritual bath not invalidated: no bearing."),
 ('Makkot 3b:17', 'OUTSIDE', "R. Chiyya's baraita on the bath — per R. Yochanan ben Nuri or the Rabbis (Mikvaot 7:5): no bearing."),
 # Rosh Hashanah 8b-9a
 (R('Rosh Hashanah 8b', 1, 5), 'OUTSIDE', "the New Year as the day of judgment (Psalms 81:4-5 — the moon covered; the heavenly court after the earthly's sanctification; the nations judged too, Israel first; the king before the community, I Kings 8:59): the range's opening on Mishnah Rosh Hashanah 1:1's judgment; OUTSIDE the release (calendar by CALL); a DATA row."),
 ('Rosh Hashanah 8b:8', 'LAW', "the New Year for jubilees on the first of Tishri? — Yom Kippur's shofar (Leviticus 25:9-10)?: F1 — the cycle's NEW YEAR asked (yovel.jubilee by CALL; Mishnah Rosh Hashanah 1:1's sabbaticals and jubilees the count's form); the exam's row."),
 ('Rosh Hashanah 8b:9', 'LAW', "R. Yishmael son of R. Yochanan ben Beroka: 'you shall hallow the fiftieth year' — sanctified from its beginning, the first of Tishri: F1 — the jubilee's ONSET (Arakhin 28b:7's opinion at its seat); the exam's row."),
 ('Rosh Hashanah 8b:10', 'LAW', "from the New Year to Yom Kippur of the jubilee the slaves neither released nor enslaved — eating, drinking, crowned like free men; at the shofar released, the fields returned: F5 — serves_for_ever's END BY THE JUBILEE with its ten-day interval (jubilee_release by CALL — the timer's fall); the interval a DATA row; the exam's row."),
 ('Rosh Hashanah 8b:11', 'DERIVATION', "the Rabbis: 'you shall hallow the fiftieth' — years sanctified by the court's proclamation, not months: a DATA row."),
 ('Rosh Hashanah 8b:12', 'DERIVATION', "'it shall be a jubilee, the fiftieth year' (Leviticus 25:11) — the fiftieth alone, the fifty-first not even partly (no adding at the end): F1 — the cycle's edge (9a:1's arm in the U file); a DATA row."),
 ('Rosh Hashanah 9a:6', 'OUTSIDE', "Yom Kippur extended at its end — 'from evening to evening' (Leviticus 23:32): the extensions; no bearing."),
 ('Rosh Hashanah 9a:7', 'OUTSIDE', "Shabbat and the festivals extended — 'you shall rest', 'your Shabbat': no bearing."),
 ('Rosh Hashanah 9a:8', 'OUTSIDE', "R. Akiva's use of 'the ninth in the evening' — eating on the ninth credited as fasting: no bearing."),
]
SPEC = CREDITED_SPEC + OWN_U + OWN
ROWS = build_set(SPEC, [a for a in D1_UNIQUE if KIND_FIRST[a] == 'TOPIC' and (a.startswith('Makkot ') or a.startswith('Rosh Hashanah '))])
WHOLE = {}
ROWS, WHOLE_STATS = apply_whole(ROWS, WHOLE)
