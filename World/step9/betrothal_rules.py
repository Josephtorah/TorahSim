# betrothal_rules.py — round 32, BETROTHAL AND THE HOUSE (Genesis
# exam block 3 of 12, 2026-09-04). The money machine from Ephron's
# field, the bride's year, the household standing rules, the times.
# Read-source: logic/oral_triage/genesis_block_betrothal_2026-09-04.md.


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    BM = _EX("Kiddushin 2a:3-5, 4b:3-4, 11b:4-6",
             "Gen 23:13 + 25:10 (gen_39, G39-34 / F-118)")
    BY = _EX("Ketubot 57b:1-4; Yevamot 61b:12-14",
             "Gen 24:55 + 24:16 (gen_41, G41-35 / F-119)")
    HS = _EX("Ketubot 61a:2-4, 67b:1-3",
             "Gen 20:3 + 3:20 + 2:18 (gen_36 G36-20 / F-120; "
             "gen_09 G09-20 / F-123)")
    MT = _EX("Taanit 11a:3-5; Yoma 77a:13-14",
             "Gen 41:50 + 31:50 (gen_64 G64-35 / F-122; gen_54 "
             "G54-42 / F-121)")

    def rule_betrothal_money(case):
        q = case.get("query")
        if q == "money_betrothal_source":
            return [V("kichah_kichah_ephron",
                      "money betrothal — גמר קיחה קיחה משדה עפרון "
                      "('taking-taking derived from the FIELD OF "
                      "EPHRON'): 'when a man TAKES a wife' beside "
                      "נתתי כסף השדה קח ממני ('I have given the "
                      "silver of the field — TAKE from me,' Gen "
                      "23:13) — Kiddushin 2a:4, with the baraita's "
                      "route ('there is no taking except with "
                      "silver') and the deflectable a-fortiori that "
                      "made the verse necessary — Kiddushin 4b:3-4",
                      authority="the gemara with the baraita",
                      machine_claim="G39-34", **BM)]
        if q == "taking_as_acquisition":
            return [V("field_abraham_acquired",
                      "וקיחה איקרי קניין ('and TAKING is called "
                      "ACQUISITION') — דכתיב השדה אשר קנה אברהם ('as "
                      "it is written: the field that Abraham "
                      "ACQUIRED,' Gen 25:10): the tractate's opening "
                      "verb-equation, both legs on our purchase — "
                      "Kiddushin 2a:5",
                      authority="the gemara",
                      machine_claim="G39-34", **BM)]
        if q == "betrothal_amount_floor":
            return [V("peruta_medium_not_amount",
                      "the challenge: betrothal money is learned "
                      "from Ephron's field — yet Beit Hillel say "
                      "בפרוטה ובשוה פרוטה ('with a peruta or a "
                      "peruta's worth')! Resolved: Ephron's verse "
                      "powers the MEDIUM (silver acquires), never "
                      "the AMOUNT — the fixed-sum rule was restated "
                      "for named Torah sums only — Kiddushin 11b:5-6",
                      authority="the sugya's restatement of Rav "
                                "Asi",
                      machine_claim="G39-34", **BM)]
        if q == "silver_grades":
            return [V("fixed_tyrian_rabbinic_provincial",
                      "Rav Yehuda citing Rav Asi: כל כסף קצוב האמור "
                      "בתורה כסף צורי ('every FIXED silver stated in "
                      "the Torah is TYRIAN silver') ושל דבריהם כסף "
                      "מדינה ('and that of the sages, PROVINCIAL "
                      "silver') — the two-grade currency table — "
                      "Kiddushin 11b:6",
                      authority="Rav Yehuda citing Rav Asi",
                      machine_claim="G39-34", **BM)]
        return None

    def rule_bride_year(case):
        q = case.get("query")
        if q == "bride_preparation_days":
            return [V("year_from_redemption_days",
                      "Rav Chisda: תשב הנערה אתנו ימים או עשור ('let "
                      "the maiden remain with us DAYS or ten,' Gen "
                      "24:55) — and what is 'days'? A YEAR, as "
                      "written ימים תהיה גאלתו ('DAYS shall its "
                      "redemption be,' Lev 25:29); not two days "
                      "(people do not speak so — the negotiation "
                      "ladder), not a month (plain 'days' is "
                      "derived from plain 'days,' never from days "
                      "said with 'month') — the virgin's twelve "
                      "months of preparation — Ketubot 57b:2-4",
                      authority="Rav Chisda",
                      machine_claim="G41-35", **BY)]
        if q == "maiden_virgin_definition":
            return [V("naarah_by_rebekah",
                      "אין בתולה אלא נערה ('virgin means only a "
                      "MAIDEN') — וכן הוא אומר והנערה טבת מראה מאד "
                      "בתולה ('and so it says: the MAIDEN, very "
                      "fair, a virgin,' Gen 24:16): Rebekah's verse "
                      "as the definitional seat — Yevamot 61b:13",
                      authority="the baraita Rav Nachman bar Yitzchak adduces",
                      machine_claim="G41-35", **BY)]
        return None

    def rule_household_standing(case):
        q = case.get("query")
        if q == "rises_not_descends":
            return [V("rises_with_husband",
                      "עולה עמו ואינה יורדת עמו ('she RISES with him "
                      "and does not descend with him') — Rav Huna "
                      "from והיא בעלת בעל ('and she is married to a "
                      "MASTER,' Gen 20:3): in the master's rising, "
                      "not his descent; R. Elazar from כי היא היתה "
                      "אם כל חי ('for she was the mother of all "
                      "LIVING,' Gen 3:20): given for LIFE, not for "
                      "pain — two recorded routes, one standing — "
                      "Ketubot 61a:3",
                      authority="Rav Huna and R. Elazar, both "
                                "routes recorded",
                      machine_claim="G36-20", **HS)]
        if q == "orphan_groom_order":
            return [V("house_bed_then_wife",
                      "the orphan who comes to marry: they RENT him "
                      "a house, ARRANGE him a bed and his utensils, "
                      "and only then marry him to a wife — 'sufficient "
                      "for his lack which he lacks, for him' (Deut "
                      "15:8) parsed word by word: the lack = the "
                      "house, lacks = bed and table, 'for him' = a "
                      "wife — וכן הוא אומר אעשה לו עזר כנגדו ('and "
                      "so it says: I will make FOR HIM a helper,' "
                      "Gen 2:18): our verse closes the parse — "
                      "Ketubot 67b:2; beside the standing G09-13 "
                      "(the community marries him off on the same "
                      "token; the orphan girl first)",
                      authority="the baraita",
                      machine_claim="G09-20", **HS)]
        return None

    def rule_marriage_times(case):
        q = case.get("query")
        if q == "famine_relations_ban":
            return [V("forbidden_childless_excepted",
                      "Reish Lakish: אסור לאדם לשמש מטתו בשני רעבון "
                      "('it is FORBIDDEN to have marital relations "
                      "in famine years') — וליוסף ילד שני בנים בטרם "
                      "תבוא שנת הרעב ('to Joseph were born two sons "
                      "BEFORE the famine year came,' Gen 41:50); "
                      "the baraita's rider: the CHILDLESS may — "
                      "Taanit 11a:4",
                      authority="Reish Lakish with the baraita's "
                                "rider",
                      machine_claim="G64-35", **MT)]
        if q == "marital_affliction_token":
            return [V("deprivation_is_affliction",
                      "whence that marital deprivation is called "
                      "AFFLICTION (innuy)? — אם תענה את בנתי ('if "
                      "you AFFLICT my daughters — and if you take "
                      "wives,' Gen 31:50, Laban's oath clause): the "
                      "Yom Kippur affliction roster's recorded "
                      "source — Yoma 77a:14",
                      authority="the gemara",
                      machine_claim="G54-42", **MT)]
        return None

    return {
        "betrothal_money": {"fn": rule_betrothal_money,
                            "tractate": "Kiddushin"},
        "bride_year": {"fn": rule_bride_year,
                       "tractate": "Ketubot"},
        "household_standing": {"fn": rule_household_standing,
                               "tractate": "Ketubot"},
        "marriage_times": {"fn": rule_marriage_times,
                           "tractate": "Taanit"},
    }
