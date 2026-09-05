# kindness_rules.py — round 41, KINDNESS, MOURNING, AND CHARITY
# (Genesis exam block 12 of 12, 2026-09-04 — the campaign finale).
# Read-source: logic/oral_triage/genesis_block_kindness_2026-09-04.md.


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    IK = _EX("Sotah 14a:3-5 (standing); 10b:5-7; Shabbat 127a:12-14",
             "Gen 3:21 (G11-24 standing) + 18:3 (gen_34, G34-27 / "
             "F-189) + 38:25 (gen_61, G61-21 / F-188)")
    MF = _EX("Shabbat 152a:14-16; Berakhot 18a:2-4; 64a:9-11; "
             "Ketubot 8b:9-11",
             "Gen 50:10 (gen_73, G73-31 / F-191) + 23:3-4 (gen_39, "
             "G39-37 / F-196) + 15:15 (gen_31, G31-22 / F-198) + "
             "18:19 (gen_34, G34-28 / F-190)")
    FP = _EX("Bava Kamma 92a:15-17; 93a:2-4; Yoma 87a:12-14",
             "Gen 20:17 + 21:1 (gen_36, G36-22 / F-193) + 50:17 "
             "(gen_73, G73-32 / F-192) + 16:5 + 23:2 (gen_32, "
             "G32-23 / F-194)")
    ZC = _EX("Pesachim 4a:5-7; Ketubot 50a:2-4",
             "Gen 22:3 (gen_38, G38-44 / F-195) + 28:22 (gen_48, "
             "G48-36 / F-199)")
    BS = _EX("Berakhot 54b:7-11",
             "Gen 19:26 + 19:29 (gen_35, G35-30 / F-197; G35-28 "
             "standing beside)")

    def rule_imitatio_kindness(case):
        q = case.get("query")
        if q == "imitatio_ladder":
            return [V("walk_after_his_attributes",
                      "walk after the Lord? He is consuming fire — "
                      "אלא להלך אחר מדותיו של הקב\"ה ('rather, to "
                      "WALK AFTER the ATTRIBUTES of the Holy One'): "
                      "He clothes the naked (Gen 3:21), visits the "
                      "sick — וירא אליו ה' באלוני ממרא ('the LORD "
                      "APPEARED to him at the oaks of Mamre,' Gen "
                      "18:1, the circumcision's third day) — "
                      "comforts mourners (25:11, blessing Isaac "
                      "after Abraham's death), buries the dead; "
                      "STANDING SEAT: G11-24's garments install has "
                      "cited Sotah 14a:4 since the derivation — "
                      "Sotah 14a:3-4",
                      authority="R. Chama b. Chanina",
                      machine_claim="G11-24 (standing)", **IK)]
        if q == "hospitality_rank":
            return [V("greater_than_the_presence",
                      "the rank ladder whole: equal to early study "
                      "(R. Yochanan), greater than it (Rav Dimi), "
                      "and Rav Yehuda in Rav's name — גדולה הכנסת "
                      "אורחין מהקבלת פני שכינה ('hospitality is "
                      "GREATER than RECEIVING the face of the "
                      "Presence'): אל נא תעבר ('do not PASS BY,' "
                      "Gen 18:3) — Abraham left the Presence "
                      "standing to run to the guests; the six-things "
                      "canon list follows with hospitality first — "
                      "Shabbat 127a:13-14",
                      authority="Rav Yehuda in Rav's name",
                      machine_claim="G34-27", **IK)]
        if q == "shaming_furnace":
            return [V("furnace_before_shaming",
                      "נוח לו לאדם שיפיל עצמו לתוך כבשן האש ואל "
                      "ילבין פני חבירו ברבים ('better for a man to "
                      "THROW HIMSELF INTO A FIERY FURNACE than to "
                      "WHITEN his fellow's face in public') — מנלן "
                      "מתמר ('whence? from TAMAR,' Gen 38:25: she "
                      "sent the pledges rather than name him); the "
                      "recognize-for-recognize echo beside (37:32 → "
                      "38:25) — Sotah 10b:6-7",
                      authority="four-link chain to R. Shimon "
                                "b. Yochai (or R. Yochanan)",
                      machine_claim="G61-21", **IK)]
        return None

    def rule_mourning_file(case):
        q = case.get("query")
        if q == "mourning_duration":
            return [V("seven_days_by_josephs_mourning",
                      "Rav Chisda: נפשו של אדם מתאבלת עליו כל שבעה "
                      "('a man's soul MOURNS for him all SEVEN') — "
                      "closing on ויעש לאביו אבל שבעת ימים ('he made "
                      "for his father a MOURNING OF SEVEN DAYS,' Gen "
                      "50:10): the institution's anchor; Rav "
                      "Yehuda's rider — no comforters, TEN men sit "
                      "in his place — Shabbat 152a:15-16",
                      authority="Rav Chisda with Rav Yehuda's rider",
                      machine_claim="G73-31", **MF)]
        if q == "premourner_exemption":
            return [V("exempt_until_burial",
                      "the mourner before burial: EXEMPT from the "
                      "Shema, the prayer, the tefillin, and every "
                      "obligation in the Torah — Rav Ashi: כיון "
                      "שמוטל עליו לקוברו כמוטל לפניו דמי ('since the "
                      "burial LIES UPON HIM, it is as if the dead "
                      "lies BEFORE HIM'): ויקם אברהם מעל פני מתו "
                      "('Abraham ROSE from before his DEAD,' Gen "
                      "23:3) with ואקברה מתי מלפני ('that I may BURY "
                      "my dead from BEFORE ME,' 23:4) — the doubled "
                      "from-before token as the duty-status — "
                      "Berakhot 18a:3",
                      authority="Rav Ashi",
                      machine_claim="G39-37", **MF)]
        if q == "parting_from_dead":
            return [V("in_peace_to_the_dead",
                      "R. Avin HaLevi: to the LIVING say לך לשלום "
                      "('go TO peace,' Jethro to Moses — he rose); "
                      "never לך בשלום ('go IN peace,' David to "
                      "Absalom — he hanged); from the DEAD the "
                      "reverse — only IN peace: ואתה תבוא אל אבתיך "
                      "בשלום ('you shall COME TO YOUR FATHERS IN "
                      "PEACE,' Gen 15:15) — Berakhot 64a:9-10",
                      authority="R. Avin HaLevi",
                      machine_claim="G31-22", **MF)]
        if q == "consolation_formula":
            return [V("covenant_holders_formula",
                      "the mourners' consolation on its feet: אחינו "
                      "גומלי חסדים בני גומלי חסדים המחזיקים בבריתו "
                      "של אברהם אבינו ('our brothers, DOERS OF "
                      "KINDNESS, sons of doers of kindness, who "
                      "HOLD THE COVENANT of Abraham our father') — "
                      "the proof: כי ידעתיו למען אשר יצוה את בניו "
                      "('for I have KNOWN him, that he will COMMAND "
                      "his children,' Gen 18:19) — Ketubot 8b:10",
                      authority="the recorded formula (the Rav Chiyya "
                                "bar Abba house call)",
                      machine_claim="G34-28", **MF)]
        return None

    def rule_forgiveness_prayer(case):
        q = case.get("query")
        if q == "pray_for_fellow_first":
            return [V("answered_first",
                      "who asks mercy for his fellow while needing "
                      "that same thing is ANSWERED FIRST — Rava: "
                      "מהכא ('from HERE'): ויתפלל אברהם ('Abraham "
                      "PRAYED,' Gen 20:17, for Abimelech's "
                      "household) and וה' פקד את שרה כאשר אמר ('the "
                      "LORD VISITED Sarah AS HE HAD SAID,' 21:1) — "
                      "as Abraham had said over Abimelech: the "
                      "answered-first receipt; beside G37-30's "
                      "standing remembrance-dispute seat — Bava "
                      "Kamma 92a:15-16",
                      authority="Rava (Rabbah bar Mari from Job "
                                "beside)",
                      machine_claim="G36-22", **FP)]
        if q == "forgiveness_ask_limit":
            return [V("three_times_then_stop",
                      "R. Yosei bar Chanina: אל יבקש ממנו יותר משלש "
                      "פעמים ('ask of him no MORE THAN THREE "
                      "TIMES'): אנא שא נא ועתה שא נא ('PLEASE... "
                      "FORGIVE now... and NOW forgive' — the "
                      "brothers' triple plea, Gen 50:17); if he "
                      "died — ten men at the grave with the "
                      "confession formula; a rider on gen_36's "
                      "forgiveness module (G36-18) — Yoma 87a:13",
                      authority="R. Yosei bar Chanina",
                      machine_claim="G73-32", **FP)]
        if q == "invoking_heaven":
            return [V("invoker_punished_first",
                      "Rav Chanan: המוסר דין על חבירו הוא נענש "
                      "תחילה ('who HANDS his fellow to Heaven's "
                      "JUDGMENT is punished FIRST'): Sarai's חמסי "
                      "עליך ('my WRONG be upon you,' Gen 16:5) — "
                      "answered at ויבא אברהם לספד לשרה ('Abraham "
                      "came to EULOGIZE Sarah,' 23:2); the "
                      "condition: only where earthly recourse "
                      "exists; R. Yitzchak's woe-to-the-crier "
                      "rider — Bava Kamma 93a:3-4",
                      authority="Rav Chanan",
                      machine_claim="G32-23", **FP)]
        return None

    def rule_zeal_and_charity(case):
        q = case.get("query")
        if q == "zealous_timing":
            return [V("early_by_abrahams_morning",
                      "all day is valid for circumcision, yet "
                      "זריזין מקדימין למצות ('the ZEALOUS are EARLY "
                      "to commandments'): וישכם אברהם בבקר "
                      "('Abraham ROSE EARLY in the morning,' Gen "
                      "22:3) — the binding's departure clause as "
                      "the timing rule's source — Pesachim 4a:6",
                      authority="the baraita",
                      machine_claim="G38-44", **ZC)]
        if q == "charity_cap":
            return [V("no_more_than_a_fifth",
                      "at USHA they ordained: המבזבז אל יבזבז יותר "
                      "מחומש ('the spender may not spend MORE THAN "
                      "A FIFTH,' lest he need the creatures); the "
                      "verse: וכל אשר תתן לי עשר אעשרנו לך ('all "
                      "You give me I will surely TITHE-TITHE to "
                      "You,' Gen 28:22) — Jacob's vow verb DOUBLED "
                      "= two tenths; Rav Ashi: the second like the "
                      "first — the doubled verb's grammar makes the "
                      "tenths equal, the cap exactly a fifth — "
                      "Ketubot 50a:2-4",
                      authority="the Usha ordinance; Rav Nachman's "
                                "verse; Rav Ashi's arithmetic",
                      machine_claim="G48-36", **ZC)]
        return None

    def rule_blessing_stations(case):
        if case.get("query") == "salt_pillar_blessing":
            return [V("two_blessings_judge_and_remembers",
                      "the station list holds ותהי נציב מלח ('and "
                      "she became a PILLAR OF SALT,' Gen 19:26); "
                      "the objection — a punishment among miracles! "
                      "— resolved: TWO blessings — on her, ברוך דיין "
                      "האמת ('Blessed... the TRUE JUDGE'); on Lot, "
                      "ברוך זוכר את הצדיקים ('Blessed... who "
                      "REMEMBERS the righteous'): ויזכר אלהים את "
                      "אברהם ('God REMEMBERED Abraham,' 19:29) and "
                      "sent Lot out; R. Yochanan — even in His "
                      "anger He remembers; beside standing G35-28 "
                      "(the pillar does not defile) — Berakhot "
                      "54b:8-10",
                      authority="the resolved teaching with R. "
                                "Yochanan's rider",
                      machine_claim="G35-30", **BS)]
        return None

    return {
        "imitatio_kindness": {"fn": rule_imitatio_kindness,
                              "tractate": "Sotah"},
        "mourning_file": {"fn": rule_mourning_file,
                          "tractate": "Shabbat"},
        "forgiveness_prayer": {"fn": rule_forgiveness_prayer,
                               "tractate": "Bava Kamma"},
        "zeal_and_charity": {"fn": rule_zeal_and_charity,
                             "tractate": "Pesachim"},
        "blessing_stations": {"fn": rule_blessing_stations,
                              "tractate": "Berakhot"},
    }
