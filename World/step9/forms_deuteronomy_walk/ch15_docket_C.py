# THE DEUTERONOMY WALK 13b — THE EXAM DOCKET OF CHAPTER 15, part C (D1): GITTIN 36a-37b WHOLE (Hillel's prosbol — the court's writ — at its folio; the range's
# opening on the divorce's witnesses and its tail on the captured Canaanite slave OUTSIDE) and ARAKHIN 32b-33a WHOLE (the count renewed at Ezra's return, the
# jubilee's condition 'all its inhabitants', the fiftieth year counted for the sabbaticals' order; the walled cities and the courtyards' houses OUTSIDE) — READ
# WHOLE HERE (ch15_uncred_d1_00.txt's tail, ch15_uncred_d1_01.txt). Every D1 address whose first seat is a TOPIC row of Gittin or Arakhin. The verdicts and the
# cells as in part A. 12b's form (ch14_docket_C.py).
from ch15_docket_common import R, build_set, apply_whole, CREDITED_SPEC, D1_UNIQUE, KIND_FIRST
from ch15_docket_U import OWN_U
OUT_G = "the range's opening on Gittin's ordinances for the betterment of the world (the divorce's witnesses, the priest's vow) — no bearing on the release; a DATA row."
OUT_S = "the range's tail — MISHNAH GITTIN 4:4's captured Canaanite slave redeemed as a slave or a freeman (before or after the owner's despair — Abaye / Rava; R. Shimon ben Gamliel's 'a slave either way' by Chizkiya's reason; the gentile's acquisition of a gentile by labor, Leviticus 25:45): the Canaanite slave's law (yovel.sale_manner by CALL if asked), not the chapter's Hebrew; a DATA row."
OUT_W = "the walled cities from Joshua's days (Leviticus 25:29-30) — the range's opening; OUTSIDE the release (yovel by CALL if asked); a DATA row."
OUT_H = "MISHNAH ARAKHIN 9:7's houses of the unwalled courtyards (Leviticus 25:31) and the baraita's cases (Rav Huna's consecrated house, R. Oshaya, Rav Pappa, the Levite's consecration by 25:33) — the range's tail; OUTSIDE the release (yovel's houses' redemption); a DATA row."
OWN = [
 # Gittin 36a-37b
 (R('Gittin 36a', 1, 10), 'OUTSIDE', OUT_G),
 ('Gittin 36a:12', 'LAW', "THE PROSBOL'S TEXT at the Bavli — 'I transfer to you, so-and-so the judges of such a place, that I will collect any debt I am owed whenever I wish'; the judges or the witnesses sign; the court collects and gives: F1 — the_prozbul's VALUE (Mishnah Sheviit 10:4's words at the Gemara); the exam's row."),
 ('Gittin 36a:13', 'LAW', "how can Hillel override Torah law? Abaye: the sabbatical in the present is rabbinic, per Rabbi: F1 — the_prozbul's GROUND — the release rabbinic when the jubilee is not in force (the_release_territory's decree arm); the exam's row."),
 ('Gittin 36b:1', 'LAW', "the Sages instituted the release in the present in remembrance of the Torah's; Hillel's writ counters a rabbinic rule, not the Torah's: F1 — THE DECREE ARM STATED (the design's 'outside the Land and when the jubilee is not in force the release stands by decree'); the exam's row."),
 ('Gittin 36b:2', 'CONTEXT', "how can the Sages release what the Torah keeps — the debtors told to steal?: F1 — the decree's difficulty; a DATA row."),
 ('Gittin 36b:3', 'DERIVATION', "Abaye: sit and do nothing (a passive breach the Sages may order); Rava: property declared ownerless by the court is ownerless (R. Yitzchak from Ezra 10:8): F1 — the decree's two grounds — the court's power over property; a DATA row."),
 ('Gittin 36b:4', 'DERIVATION', "R. Eliezer's source — Joshua 19:51's heads beside the fathers: the heads transmit as fathers do: F1 — the doublet; a DATA row."),
 ('Gittin 36b:5', 'DISPUTE', "Hillel's writ for his generation alone, or for all generations?: F1 — the_prozbul's SCOPE: the arms; the exam's arm."),
 ('Gittin 36b:6', 'CONTEXT', "the difference — nullifying it: only a greater court in wisdom and number: a DATA row."),
 ('Gittin 36b:7', 'CONTEXT', "Shmuel: a prosbol written only in the courts of Sura and Nehardea — the proof for 'his generation': a DATA row."),
 ('Gittin 36b:8', 'CONTEXT', "rejected — courts like Hillel's, like Rav Ami's and Rav Asi's, that can remove money: a DATA row."),
 ('Gittin 36b:9', 'CONTEXT', "Shmuel: 'this prosbol is the judges' ulbena (their arrogance, or their convenience); if my strength increases I will nullify it' — read 'if I become greater than Hillel': a DATA row."),
 ('Gittin 36b:10', 'CONTEXT', "Rav Nachman: 'I will uphold it' — as though written for everyone, no writ needed: F1 — the writ's presumption's kin (37b:5); a DATA row."),
 ('Gittin 36b:11', 'CONTEXT', "ulbena — insolence or convenience? Ulla's insolent bride under her canopy (the calf after Sinai): the lore; a DATA row."),
 ('Gittin 36b:12', 'OUTSIDE', "Song of Songs 1:12 read of the calf — 'sent forth its fragrance', not 'reeked': the lore; no bearing."),
 ('Gittin 36b:13', 'OUTSIDE', "those insulted who do not insult — 'as the sun going forth in its might' (Judges 5:31): the lore; no bearing."),
 ('Gittin 36b:14', 'CONTEXT', "Rav Chisda: prosbol — an ordinance [pros] of bulei and butei (37a:1 the link row's continuation): the etymology; a DATA row."),
 ('Gittin 37a:2', 'LAW', "Shmuel: orphans need no prosbol — Rabban Gamliel and his court are the orphans' fathers: F1 — the writ's EXEMPTION (Mishnah Sheviit 10:6's guardian; the_prozbul's persons); the exam's row."),
 ('Gittin 37a:3', 'LAW', "Mishnah Sheviit 10:6 — a prosbol only on land; the creditor gives the debtor any amount: a cabbage stalk's ground (Rav), an oven's and a stove's place (Rav Yehuda): F1 — the LAND condition's minimum; the exam's row."),
 ('Gittin 37a:4', 'DERIVATION', "Hillel's perforated pot (Tosefta Sheviit 8:10) — as land; the unperforated not: F1 — the land condition's edge; a DATA row."),
 ('Gittin 37a:5', 'DERIVATION', "the pot resting on stakes — the case Hillel needed: a DATA row."),
 ('Gittin 37a:6', 'CONTEXT', "Rav Ashi's palm stump transferred to the borrower; the school of Rav Ashi by speech — 'you are a court, the debt is given over to you' — sufficient: F1 — the writ by speech (the_prozbul's form loosened); a DATA row."),
 ('Gittin 37a:7', 'LAW', "no land — the guarantor's land serves; neither — the land of one who owes the debtor (R. Natan's rule): F1 — the land condition's SUBSTITUTES; the exam's row."),
 ('Gittin 37a:9', 'DISPUTE', "Mishnah Sheviit 10:1's 'with a note / without' — Rav and Shmuel: with a property lien / without one, ALL released, the oral loan all the more: F1 — the_release_object's LIEN arm (a); the exam's arm."),
 ('Gittin 37a:10', 'DISPUTE', "R. Yochanan and Reish Lakish: 'with a note' — without a lien; 'without' — oral; the note WITH A LIEN NOT released — as though the land were already taken: F1 — the lien arm (b); the exam's arm."),
 ('Gittin 37a:11', 'LAW', "the baraita per R. Yochanan: the note with a lien not released; a field specified for repayment, or 'all my property pledged' — not released: F1 — the lien's rule (Tosefta Sheviit 8:7's twin); the exam's row."),
 ('Gittin 37a:12', 'CONTEXT', "R. Asi's relative with a lien note — R. Asi: not released; R. Yochanan: released: a DATA row."),
 ('Gittin 37a:13', 'CONTEXT', "R. Yochanan: 'because we think so should we act?'; the baraita perhaps Beit Shammai's ('a note standing to be collected is as collected'), not the ruling: the arm's status; a DATA row."),
 ('Gittin 37a:14', 'LAW', "Mishnah Sheviit 10:2 — the pledge-loan and the notes handed to the court not released; the court seizes the notes — but why the pledge?: F1 — the PLEDGE's exception asked (113:2); the exam's row."),
 ('Gittin 37a:15', 'DERIVATION', "Rava: the creditor holds the debtor's item — as collected; Abaye's courtyard objection: a DATA row."),
 ('Gittin 37a:16', 'DERIVATION', "the pledge ACQUIRED by the creditor — R. Yitzchak from 24:13's 'it shall be righteousness for you' (returning it a charity): F1 — the pledge's ground (ordinances.loan(pledge_sunset) by CALL — 24:13 ahead); a DATA row."),
 ('Gittin 37a:17', 'CONTEXT', "'we learned there (Sheviit 10:8)' — the citation's stub, the mishnah's text at 37b:1 (the link row): a DATA row."),
 ('Gittin 37b:2', 'LAW', "Rabba: the creditor may lift his eyes hopefully until the debtor says 'nevertheless'; the baraita: the debtor says 'my money, a gift', not 'my debt': F1 — the MANNER's edge (the initiative the debtor's; the creditor's hope permitted); the exam's row."),
 ('Gittin 37b:3', 'CONTEXT', "Abba bar Marta took the money and left at Rabba's 'I abrogate': the story; a DATA row."),
 ('Gittin 37b:4', 'CONTEXT', "Abaye teaches him 'nevertheless'; Rabba: 'not knowledgeable from the beginning': the story's end; a DATA row."),
 ('Gittin 37b:5', 'LAW', "Rav Nachman: one is credible to say 'I had a prosbol and lost it' — the writ easy to write, no one forgoes the permitted for the forbidden: F1 — the writ's PRESUMPTION; the exam's row."),
 ('Gittin 37b:6', 'CONTEXT', "Rav's 'did you have a prosbol and lose it?' — 'open your mouth for the mute' (Proverbs 31:8): a DATA row."),
 ('Gittin 37b:7', 'CONTEXT', "Mishnah Ketubot 9:9's objection — a note without a prosbol not collected: a DATA row."),
 ('Gittin 37b:8', 'DISPUTE', "a note presented after the seventh year — a prosbol needed with it (the first), not needed (the Rabbis — presumed written): F1 — the presumption's arms; the exam's arm."),
 (R('Gittin 37b', 9, 19), 'OUTSIDE', OUT_S),
 # Arakhin 32b-33a
 (R('Arakhin 32b', 1, 4), 'OUTSIDE', OUT_W),
 ('Arakhin 32b:5', 'CONTEXT', "R. Yishmael son of R. Yosei: the walled cities counted at the return from Babylonia — the first sanctification nullified with the exile: F1 — the_release_onset's kin (the Land's sanctity and the count renewed — 32b:10); a DATA row."),
 ('Arakhin 32b:7', 'CONTEXT', "the other baraita — any city with a tradition of a wall from Joshua's days: the first sanctification ETERNAL: the other arm; a DATA row."),
 ('Arakhin 32b:8', 'CONTEXT', "two tannaim (Mishnah-era teachers), or R. Elazar bar Yosei's 'which has [lo] a wall' with an alef — once walled, still walled: OUTSIDE (Leviticus 25:30's written form); a DATA row."),
 ('Arakhin 32b:9', 'CONTEXT', "'since the days of Joshua … had not made sukkot' (Nehemiah 8:17) — David's generations made none?: the question; a DATA row."),
 ('Arakhin 32b:10', 'LAW', "Ezra's arrival compared to Joshua's: as at Joshua's they COUNTED SABBATICAL AND JUBILEE YEARS and sanctified walled cities, so at Ezra's: F1 — the_release_onset's RENEWAL at the second entry (the count's epoch begun again — calendar_parameters' count era's form; the_release_onset a parameter with two entries); the exam's row."),
 ('Arakhin 32b:11', 'DERIVATION', "'the land your fathers possessed, you shall possess it' (30:5) — your possession with the renewal of the sabbatical, the jubilee, the heave-offerings and the tithes: F1 — the onset's ground (30:5 ahead); a DATA row."),
 ('Arakhin 32b:12', 'CONTEXT', "the eternal-sanctity tanna (a Mishnah-era teacher): Ezra prayed away idolatry's inclination — his merit a sukka: the lore; a DATA row."),
 ('Arakhin 32b:13', 'OUTSIDE', "Joshua's name written Yeshua — the criticism for not praying; the lore; no bearing."),
 ('Arakhin 32b:14', 'CONTEXT', "'your fathers possessed … you shall possess' per the eternal arm — no second sanctification needed: a DATA row."),
 ('Arakhin 32b:15', 'LAW', "did they count sabbaticals and jubilees in Ezra's days? — the jubilee's count NULLIFIED once Reuben, Gad and half Manasseh were exiled (I Chronicles 5:26): F1 — THE JUBILEE'S CONDITION on the count (yovel.jubilee by CALL; the_release_territory's decree arm's history); the exam's row."),
 ('Arakhin 32b:16', 'LAW', "the baraita: 'proclaim liberty to ALL ITS INHABITANTS' (Leviticus 25:10) — the jubilee only when all are in the Land: F1 — the jubilee's condition (yovel by CALL); the exam's row."),
 ('Arakhin 32b:17', 'LAW', "intermingled tribes — no jubilee: 'to all its inhabitants' in their arrangement: F1 — the condition's second clause; the exam's row."),
 ('Arakhin 32b:18', 'LAW', "Rav Nachman bar Yitzchak: they counted jubilee years TO SANCTIFY THE SABBATICALS — the fiftieth counted so the next cycle begins at the fifty-first, the jubilee's laws not in force: F1 — THE COUNT WITHOUT THE JUBILEE'S FORCE (yovel.cycle's arithmetic — the fiftieth counted for the sabbaticals' order; the_release_date's cycle); the exam's row."),
 ('Arakhin 33a:1', 'DISPUTE', "per the Rabbis the fiftieth outside the cycle — the count needed; per R. Yehuda (the fiftieth counted for both) — no need: F1 — the cycle's arithmetic, two arms (Rosh Hashanah 9a:1's twin); the exam's arm."),
 ('Arakhin 33a:2', 'DERIVATION', "'at the end of seven years you shall let go … served you six years' (Jeremiah 34:14) — the jubilee counted in Jeremiah's day?: F5 — Jeremiah 34:14 THE RUN'S CASE (the readback's VARIANT row's citation); 33a:3's two persons in the U file; a DATA row."),
 ('Arakhin 33a:4', 'DERIVATION', "Jeremiah's words a reproof, not a command — 'did you send free the pierced when the jubilee was observed?'; 'they listened and let them go' (34:10) — the present: F5 — the case's reading; a DATA row."),
 ('Arakhin 33a:5', 'CONTEXT', "R. Yochanan: the jubilee was not in force — Jeremiah brought back the tribes and Josiah ruled them (Ezekiel 7:13): the history; a DATA row."),
 ('Arakhin 33a:6', 'OUTSIDE', "Josiah at Bethel's altar (II Kings 23:16-17): the lore; no bearing."),
 ('Arakhin 33a:7', 'OUTSIDE', "Hosea 6:11's harvest for Judah: the lore; no bearing."),
 (R('Arakhin 33a', 8, 21), 'OUTSIDE', OUT_H),
]
SPEC = CREDITED_SPEC + OWN_U + OWN
ROWS = build_set(SPEC, [a for a in D1_UNIQUE if KIND_FIRST[a] == 'TOPIC' and (a.startswith('Gittin ') or a.startswith('Arakhin '))])
WHOLE = {}
ROWS, WHOLE_STATS = apply_whole(ROWS, WHOLE)
