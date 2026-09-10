# The second Passover's exam — the testing shelf for Num 9:1-14 (2026-09-09; THE TENT sitting 2,
# World/step9/THE_TENT.md section 2; the compile cold_run_pesach_sheni.py). Docket: the case-anchored rows
# routed BY TOPIC (logic/MISHNAH_TOPICS.md: Mishnah Pesachim chapter 9 "Second Passover", 11 rows; the
# Tosefta beside it, Tosefta Pesachim chapter 8, 8 rows) — the union rule of 2026-09-05 (a tractate that
# cites no verse is not a tractate that tests nothing). Every row opened; credits under the guards; the
# lost-lamb and intermingling rows ROUTED to the Passover engine's registration module (Exod 12:4's), whose
# rows they are. The Babylonian Talmud Pesachim 92b-96a is the bridge, opened PER GAP at the compile and
# named in the cells — not a docket row. Append-only.

## Mishnah Pesachim 9 (11 rows)
- Mishnah Pesachim 9:1 — MATERIAL (fresh). The rule's rows: the unclean and the distant who missed the
  first keep the second on the fourteenth of Iyyar; the unwitting and the forced too; the two named cases
  are named to teach WHO IS EXEMPT FROM KARET when the second is missed (the unclean and the distant) and
  who is liable (the rest). → second_passover(who_keeps, karet)
- Mishnah Pesachim 9:2 — MATERIAL (fresh). THE DISTANCE: from Modi'im and beyond, and its radius around
  Jerusalem — R. Akiva; from the threshold of the court and beyond — R. Eliezer; R. Yose: therefore the heh
  of "distant" is DOTTED — not really distant, from the threshold outward. The parameter row distant_way
  (the Sifrei 69:1's attributions differ: R. Akiva and the sages Modi'im, R. Eliezer the city's entrance by
  the tithe's analogy, R. Yehuda the court — recorded beside the Mishnah's). → second_passover(distance)
- Mishnah Pesachim 9:3 — MATERIAL (CREDIT: read at the Exodus backfill ledger 2026-09-01, quick-looked
  against this span's cells per the credit guards). THE DIFFERENCE TABLE: the first bound by "shall not be
  seen / shall not be found", the second — leaven and matzah with him in the house; the first needs hallel
  at the eating, the second not; both: hallel at the making, roasted with matzah and bitter herbs, override
  the Sabbath. → second_passover(scope, sabbath_override)
- Mishnah Pesachim 9:4 — MATERIAL (CREDIT: the Tzav exam 2026-09-03 and the Exodus backfill). A Passover
  in impurity (the majority unclean): the flow-impure and the menstruant may not eat; if they ate — exempt
  from karet; R. Eliezer exempts their entry too. The CONGREGATION's Passover in impurity is the first,
  not a second (Sifrei 70:1: individuals keep the second, the congregation never). →
  second_passover(congregation)
- Mishnah Pesachim 9:5 — CONTEXT (CREDIT: the Exodus backfill's two-era table). Egypt's Passover against
  the generations' — the Passover engine's chapter (Exod 12), not this span's. → ROUTED pesach
- Mishnah Pesachim 9:6 — NOT-BEARING here (fresh). The lost Paschal lamb and its substitute — R. Yehoshua's
  two rulings, R. Akiva's explanation (lost and found before or after the slaughter: grazes till blemished
  / offered as peace offerings). The Passover's substitute — Exod 12 and Lev 27's engines. → ROUTED pesach
- Mishnah Pesachim 9:7 — NOT-BEARING here (fresh). A female or a second-year animal set aside; the owner
  who died — peace offerings. → ROUTED pesach
- Mishnah Pesachim 9:8 — NOT-BEARING here (fresh). The Paschal lamb intermingled with other offerings or
  with firstborn animals — grazing, the choicest, R. Shimon's priests' groups. → ROUTED pesach / offerings
- Mishnah Pesachim 9:9 — NOT-BEARING here (fresh) — but ONE CLAUSE bears: a group whose lamb was lost and
  slaughtered twice, the uncertain order — "they are EXEMPT from the second Passover" (three times): the
  registration decides the second Passover's exemption. The registration module's rows (Exod 12:4);
  the exemption clause noted for the eligibility cell: one included in a slaughter is not "one who did
  not keep the first". → ROUTED pesach (registration), the exemption noted
- Mishnah Pesachim 9:10 — NOT-BEARING here (fresh). Two groups' lambs intermingled — the exchange formula.
  → ROUTED pesach (registration)
- Mishnah Pesachim 9:11 — NOT-BEARING here (fresh). Two individuals' lambs intermingled — each registers a
  man from the market. → ROUTED pesach (registration)

## Tosefta Pesachim 8 (8 rows)
- Tosefta Pesachim 8:1 — MATERIAL (fresh). THE LIST of who keeps the second: zavim and zavot, menstruants,
  women after childbirth, the forced, the unwitting, the DELIBERATE, lepers, those who lay with a
  menstruant — and whoever was unclean or far. The Sifrei's binyan av (69:1) as a roster; the deliberate
  named outright (the Talmud's Rav Nachman, 92b:8). → second_passover(who_keeps)
- Tosefta Pesachim 8:2 — MATERIAL (fresh). THE CONVERT BETWEEN THE PASSOVERS: needs to keep the second —
  Rebbi; R. Natan: no, never obligated in the first (his analogy: the building of the chosen house). The
  Sifrei's R. Shimon b. Elazar excludes him (71:1). The parameter row second_passover_nature (Pesachim
  93a:8-10 ties this to the karet dispute). → proselyte
- Tosefta Pesachim 8:3 — MATERIAL (fresh). THE DIFFERENCES: three groups at the first, none at the second;
  the first overrides impurity, the second not; KARET — the shelf's printed English reads "the first
  renders liable for excision, but the first does not — the words of Rebbi; R. Natan: even the second
  renders liable; R. Chananya b. Akavya: if they kept the second they are not liable for the first, if not
  they are" — A DISCREPANCY: the Babylonian Talmud's baraita (Pesachim 93a:7) and the Sifrei (70:1) give
  Rebbi karet for BOTH and R. Natan the FIRST ALONE; the Tosefta's printed line (its second "Rishon" a
  slip for "Sheni") inverts the first two names. The code follows the Talmud's and the Sifrei's
  attribution, the Tosefta's variant recorded here. The festival offering at the first, not the second;
  seven days at the first, one at the second. → second_passover(impurity_override, karet)
- Tosefta Pesachim 8:4 — MATERIAL (fresh). THE SIMILARITIES: "an unblemished year-old male" at both; "not
  raw nor boiled" at both; both override the Sabbath; both require staying overnight — R. Yehuda: the
  second does not (he slaughters in the court and mourns his fathers at Beit Pagi). The body statutes by
  CALL into the Passover engine; the overnight a recorded dispute (Pesachim 95b:8-9). →
  second_passover(scope, sabbath_override)
- Tosefta Pesachim 8:5 — CONTEXT (CREDIT: the Tzav exam's 9:4 row). The Passover in impurity: the
  corpse-unclean enter and eat, the flow-impure may not — liable if they entered; R. Eliezer exempts by
  Num 5:2; the slaughter by the flow-impure — R. Shimon in R. Yehoshua's name exempts by Lev 7:19-20. The
  congregation's first Passover, not this span's second. → ROUTED tzav / offerings
- Tosefta Pesachim 8:6 — MATERIAL (fresh). THE WOMAN at the second: slaughtered for her alone at the first,
  at the second she joins others — R. Yehuda; R. Yose: for her alone at the second too; R. Elazar b. R.
  Shimon: she joins others at the first and does NOT keep the second (the story of Yosef the priest's
  daughter sent back). The Sifrei (70:1): the woman included by "that soul", a man not a minor. A recorded
  three-arm dispute; the code's cell: the minor exempt (the ink's "that man"), the woman's obligation
  carried as the dispute. → second_passover(who_keeps: minor, woman)
- Tosefta Pesachim 8:7 — CONTEXT (CREDIT: the Exodus backfill's two-era table, Mishnah 9:5). Egypt's
  Passover against the generations' — the Passover engine's. → ROUTED pesach
- Tosefta Pesachim 8:8 — CONTEXT (CREDIT: as 8:7). The similarities of Egypt's and the generations'; R. Yosei
  HaGelili's one-day leaven ban in Egypt. → ROUTED pesach

## CITE INDEX — every source opened, each fully named
Mishnah Pesachim 9:1
Mishnah Pesachim 9:2
Mishnah Pesachim 9:3
Mishnah Pesachim 9:4
Mishnah Pesachim 9:5
Mishnah Pesachim 9:6
Mishnah Pesachim 9:7
Mishnah Pesachim 9:8
Mishnah Pesachim 9:9
Mishnah Pesachim 9:10
Mishnah Pesachim 9:11
Tosefta Pesachim 8:1
Tosefta Pesachim 8:2
Tosefta Pesachim 8:3
Tosefta Pesachim 8:4
Tosefta Pesachim 8:5
Tosefta Pesachim 8:6
Tosefta Pesachim 8:7
Tosefta Pesachim 8:8

**read: 19 of 19 — COMPLETE** (11 Mishnah rows + 8 Tosefta rows; 14 opened fresh, 5 credited under the
guards to the Exodus backfill ledger of 2026-09-01 and the Tzav exam of 2026-09-03; verdicts MATERIAL 8 /
CONTEXT 4 / NOT-BEARING here 7 — of which ROUTED to the Passover engine 10, to the offerings 1; the
Tosefta 8:3 attribution discrepancy recorded)
