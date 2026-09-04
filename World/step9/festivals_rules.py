#!/usr/bin/env python3
"""festivals_rules.py — round 24: FESTIVALS AND GIFTS, the
thirteenth Exodus Talmud-first exam block (2026-09-04). Five
modules — the appearing, the food-labor license, the feast
offering's fences, the firstborn engine, the rest clauses.
engine.py merges build(V) at its tail. Read-source:
logic/oral_triage/exodus_block_festivals_2026-09-04.md."""


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    # ---------------------------------------- the appearing's table
    AP = _EX("Chagigah 4a:3-10 + 7a:5-7b:2; Sanhedrin 4b:15; "
             "Arakhin 2b:11-12 + 19b:8-9; Yevamot 103a:11-12; "
             "Pesachim 8b:7-8",
             "Exod.23.14-17 (exo_23_justice_calendar, EX23-13 — "
             "F-086; the word-by-word table held at EX23-07 since "
             "derivation)")

    def rule_appearance(case):
        q = case.get("query")
        if q == "blind_one_eye_appearance":
            return [V("obligated_stam_inclusion", "the Mishnah's "
                      "'ALL are obligated in the appearing' comes "
                      "to INCLUDE the one blind in one eye — 'and "
                      "not like that tanna' (Arakhin 2b:11)",
                      authority="the anonymous Mishnah (Arakhin 2a)",
                      machine_claim="EX23-13", **AP),
                    V("exempt_two_eyes", "יראה יראה ('shall see / "
                      "shall be seen' — one skeleton, two "
                      "vocalizations, move M-16): as He comes to "
                      "SEE, so he comes to BE SEEN — as the seeing "
                      "is with two eyes, the being-seen is with two "
                      "eyes (Sanhedrin 4b:15 = Arakhin 2b:12); the "
                      "frame: the vocalization dispute runs even "
                      "where read and skeleton agree",
                      authority="Yochanan ben Dahavai in the name "
                      "of R. Yehuda ben Tema", **AP)]
        if q == "slave_appearance":
            return [V("exempt_one_master_only", "אל פני האדן ה' "
                      "('before the Master, the LORD,' 23:17) — "
                      "one who has only ONE Master; excluded is he "
                      "who has another master (Chagigah 4a:10)",
                      authority="Rav Huna",
                      machine_claim="EX23-13", **AP)]
        if q == "repulsive_trade_appearance":
            return [V("exempt_cannot_ascend_with_all", "the "
                      "dung-gatherer, the copper-smelter, the "
                      "tanner — exempt: כל זכורך ('ALL your males') "
                      "= one who can GO UP WITH all your males "
                      "(Chagigah 4a:9, the verse settled on this "
                      "at 7b:2)",
                      authority="Acherim",
                      machine_claim="EX23-13", **AP)]
        if q == "split_household_appearance":
            return [V("not_permitted_no_halves", "Rav Yosef's "
                      "ten-sons split (five today, five tomorrow) "
                      "killed by Abaye: 'which of them would you "
                      "make the negligent and which the diligent?' "
                      "(7a:17-7b:1) — with the baraita: NOT SEEN "
                      "BY HALVES, from 'all your males' (7a:10)",
                      authority="Abaye",
                      machine_claim="EX23-13", **AP)]
        if q == "appearance_requirement":
            return [V("courtyard_visit", "the appearing is "
                      "APPEARING IN THE COURTYARD — later visits "
                      "need no offering; 'they shall not appear "
                      "empty' (23:15) speaks at the FESTIVAL'S "
                      "CORE (7a:5-6)",
                      authority="R. Yochanan",
                      machine_claim="EX23-13", **AP),
                    V("offering_each_visit", "appearing WITH AN "
                      "OFFERING — each entry brings (7a:5); the "
                      "not-empty clause pressed three times, "
                      "answered 'the core' each time",
                      authority="Reish Lakish", **AP)]
        if q == "prosthesis_appearance":
            return [V("exempt_regalim_wants_feet", "רגלים פרט "
                      "לבעלי קבין ('regalim — excluding "
                      "prosthesis-wearers'): the pilgrimage word "
                      "asks for FEET (Yevamot 103a:11 = Arakhin "
                      "19b:8; the register table: vows follow "
                      "common speech, the Torah's word excludes — "
                      "19b:9)",
                      machine_claim="EX23-13", **AP)]
        if q == "pilgrimage_protection":
            return [V("property_and_return_guaranteed", "ולא יחמד "
                      "איש את ארצך ('no man shall covet your land "
                      "when you go up,' 34:24) — your cow grazes "
                      "and no beast harms it, your hen pecks and "
                      "no marten harms it (Pesachim 8b:7); the "
                      "a-fortiori to persons and the RETURN leg — "
                      "'you shall find your tent at peace' (8b:8)",
                      authority="Isi ben Yehuda",
                      machine_claim="EX34-10", **AP)]
        return None

    # ------------------------------------ the festival labor license
    FL = _EX("Pesachim 47a:5-7; Shabbat 24b:6-7; Chagigah 18a:2-6; "
             "Eruvin 96a:6-7",
             "Exod.12.10 + 12.16 (exo_12_passover_and_exodus, "
             "EX12-33 — F-091); Exod.13.10 (exo_13, EX13-08 held "
             "the days-not-all-days law since derivation)")

    def rule_labor(case):
        q = case.get("query")
        if q == "sacred_baking_on_festival":
            return [V("forbidden_for_you_not_most_high", "לכם "
                      "('for YOU,' 12:16) — for you and NOT FOR "
                      "THE MOST HIGH: the two loaves bake EREV "
                      "festival (47a:5-6); the other arm recorded: "
                      "Rabban Shimon b. Gamliel reads לכם 'not for "
                      "GENTILES' and lets sacred baking ride "
                      "(47a:7, Abba Shaul's reading)",
                      machine_claim="EX12-33", **FL)]
        if q == "burn_consecrated_on_festival":
            return [V("forbidden_second_morning_granted", "the "
                      "doubled עד בקר ('until morning,' 12:10) "
                      "GRANTS the leftover a second morning for "
                      "its burning — consecrated things are not "
                      "burned on the holy day (Shabbat 24b:6, "
                      "Chizkiyah and his school); Abaye's route: "
                      "'the burnt-offering of Shabbat on ITS "
                      "Shabbat' (24b:7)",
                      authority="Chizkiyah",
                      machine_claim="EX12-33", **FL)]
        if q == "intermediate_days_labor":
            return [V("forbidden_two_routes", "R. Yoshiyah: את חג "
                      "המצות תשמר שבעת ימים ('you shall KEEP the "
                      "feast seven days,' 23:15) — the keeping "
                      "spans all seven; R. Yonatan: a-fortiori "
                      "from the first and seventh — refuted "
                      "through creation-week and new-moon, "
                      "resolved on מקרא קדש ('a holy "
                      "convocation') (Chagigah 18a:5-6); both "
                      "hold the ban (18a:4)",
                      machine_claim="EX23-13", **FL)]
        if q == "tefillin_on_festival":
            return [V("exempt_days_not_all_days", "מימים ימימה "
                      "('from days to days,' 13:10): ימים not "
                      "nights; מימים not ALL days — excluding "
                      "Sabbaths and festivals (Eruvin 96a:6) — "
                      "EX13-08's Masorah chain held this arm "
                      "verbatim since derivation",
                      authority="R. Yosei HaGelili",
                      machine_claim="EX13-20", **FL),
                    V("statute_passover_only", "that statute "
                      "speaks only of the PASSOVER (96a:7) — the "
                      "exemption derived elsewhere",
                      authority="R. Akiva", **FL)]
        if q == "harvest_feast_naming":
            return [V("feast_at_harvest_time", "חג הקציר ('the "
                      "feast of HARVEST,' 23:16) — R. Yochanan "
                      "from the ingathering parallel: THE FEAST "
                      "THAT COMES AT HARVEST TIME (a season "
                      "stamp, no work license — 18a:3); Reish "
                      "Lakish's tashlumin arm recorded (18a:2)",
                      authority="R. Yochanan",
                      machine_claim="EX23-13", **FL)]
        return None

    # ------------------------------------- the feast offering fences
    FO = _EX("Chagigah 10b:4-5; Pesachim 59b:6-7 + 63b:10-11 + "
             "64a:5-6 + 71a:12-13",
             "Exod.23.18-19 + 34.25 (exo_23_justice_calendar, "
             "EX23-14 — F-088)")

    def rule_offering(case):
        q = case.get("query")
        if q == "chag_meaning":
            return [V("chag_is_an_offering", "if the wilderness "
                      "feast were eating and drinking, whence ולא "
                      "ילין חלב חגי ('the FAT of My feast,' 23:18) "
                      "— a banquet has no altar-fat: chag owns an "
                      "offering (Chagigah 10b:4; the pushback 'fat "
                      "at feast-time' recorded, 10b:5)",
                      machine_claim="EX23-14", **FO)]
        if q == "leaven_beside_scope":
            return [V("anyones_leaven_standing_parties", "לא תשחט "
                      "על חמץ ('over leaven,' 34:25) — not 'YOUR "
                      "leaven': ANYONE'S bars (63b:10); bounded by "
                      "the not-remain link — those standing over "
                      "the offering via לא ילין, not one at the "
                      "world's end (63b:11)",
                      authority="R. Ami",
                      machine_claim="EX23-14", **FO)]
        if q == "tamid_leaven_ban":
            return [V("tamid_included", "זבחי ('MY offering') — "
                      "the offering UNIQUE to Me: the daily "
                      "offering joins the ban (64a:5)",
                      authority="R. Yehuda",
                      machine_claim="EX23-14", **FO),
                    V("fourteenth_cases_read", "the doubled זבחי "
                      "(23:18 + 34:25) read זבח זבחיי ('the "
                      "offering — My offerings') — the "
                      "fourteenth's cases instead (64a:6)",
                      authority="R. Shimon", **FO)]
        if q == "fat_overnight_window":
            return [V("burn_all_night_day_is_the_rule", "Rav "
                      "Kahana's contradiction: 'until morning it "
                      "may not remain — all night it MAY' against "
                      "'ON IT complete all offerings by day' (Lev "
                      "6:5) — resolved by himself: the night "
                      "window is for what was LEFT OVER (59b:6-7)",
                      authority="Rav Kahana",
                      machine_claim="EX23-14", **FO)]
        if q == "chagigah_overnight":
            return [V("disqualified_first_morning", "the "
                      "fifteenth's chagigah parts disqualify "
                      "overnight: 'not remain until morning' with "
                      "ראשית ('the FIRST,' 23:19) JUXTAPOSED — "
                      "this morning is the FIRST morning (71a:12); "
                      "Rav Yosef's objection carried: flesh gone "
                      "at nightfall, parts to morning? (71a:13)",
                      authority="Rav Kahana",
                      machine_claim="EX23-14", **FO)]
        return None

    # ------------------------------------------ the firstborn engine
    FB = _EX("Bekhorot 4b:2-5a:3; Yoma 49b:7-8; Niddah 40a:14-17; "
             "Temurah 4a:3-4 + 5b:13 + 18b:4-5",
             "Exod.13.2 + 13.11-15 (exo_13_consecration_and_"
             "pillars, EX13-20 — F-087; the cluster held at "
             "EX13-14 since the compiler hunt)")

    def rule_firstborn(case):
        q = case.get("query")
        if q == "wilderness_sanctification":
            return [V("sanctified_in_wilderness", "קדש לי כל בכור "
                      "('sanctify to Me every firstborn,' 13:2) "
                      "sanctified them; the standing reason: לי "
                      "יהיו ('they SHALL BE Mine,' Num 3:13) — in "
                      "their being they remain (4b:12, 5a:3)",
                      authority="R. Yochanan",
                      machine_claim="EX13-20", **FB),
                    V("suspended_until_entry", "והיה כי יבאך "
                      "('when He BRINGS you,' 13:5/11) with "
                      "והעברת after it — beforehand NOT "
                      "sanctified: the when-brought clause "
                      "suspends until entry (4b:13); harmonized "
                      "by the three-sanctifications baraita read "
                      "as three COMMANDS — 'some sanctified, some "
                      "did not' (4b:22-23, Rav Nachman bar "
                      "Yitzchak)",
                      authority="Reish Lakish", **FB)]
        if q == "donkey_redemption_material":
            return [V("seh_only_any_seh", "no calf, wild beast, "
                      "slaughtered animal, terefah, kilayim, or "
                      "koy — only a SEH: שה שה from the PASSOVER "
                      "(Yoma 49b:7); and against importing the "
                      "passover's grade, תפדה תפדה ('redeem-"
                      "redeem,' 13:13 doubled) AMPLIFIES — any "
                      "seh: species imported, grade filtered "
                      "(49b:8)",
                      machine_claim="EX13-20", **FB)]
        if q == "levite_firstborn_swap":
            return [V("abrogated_for_generations", "'silver' said "
                      "for the generations and 'seh' said for the "
                      "generations: as the census silver redeemed "
                      "then and forward, so the seh — the Levite "
                      "swap's lamb clause runs forward (Bekhorot "
                      "4b:2-3)",
                      authority="Rav Chisda",
                      machine_claim="EX13-20", **FB)]
        if q == "caesarean_consecration":
            return [V("not_sacred_womb_opener_required", "R. "
                      "Shimon concedes for consecrated animals: "
                      "לידה לידה ('birth-birth') from the "
                      "FIRSTBORN — as there the womb-opener (פטר "
                      "רחם), so here (Niddah 40a:14); the "
                      "selection argued — 'its mother from its "
                      "mother' (22:29) vs man's ordinary-from-"
                      "ordinary — settled on the shared law-class "
                      "(40a:16-17, the analogy-selection rule's "
                      "second seat)",
                      authority="R. Yochanan",
                      machine_claim="EX13-20", **FB)]
        if q == "tithe_passing_export":
            return [V("derived_two_seats", "עברה עברה ('passing-"
                      "passing'): Lev 27:32's whatever-passes-"
                      "under-the-rod learns from 13:12's והעברת — "
                      "the tithe's no-redemption (Temurah 5b:13) "
                      "and the tithed animal's offspring (18b:4, "
                      "Ravina), with the edge-condition recorded: "
                      "lest one say the possible is not derived "
                      "from the impossible (18b:5)",
                      machine_claim="EX13-20", **FB)]
        if q == "gift_order_advance":
            return [V("forbidden_order_stands_lashes_disputed",
                      "מלאתך ודמעך לא תאחר ('your fullness and "
                      "your outflow you shall not delay,' 22:28) — "
                      "מלאה the FIRSTFRUITS, דמע the TERUMAH: the "
                      "pair's ORDER is the law (Temurah 4a:3); the "
                      "lashes disputed — one says lashed, one not "
                      "(4a:4) — EX22-10's do-not-reorder file "
                      "arrived answered",
                      authority="R. Yosei b. R. Chanina",
                      machine_claim="EX13-20", **FB)]
        return None

    # --------------------------------------------- the rest clauses
    RS = _EX("Sukkah 44b:7; Horayot 4b:8-10; Yevamot 48b:4-6; "
             "Sanhedrin 63b:5-6",
             "Exod.23.11-13 + 34.21 (exo_23_justice_calendar, "
             "EX23-15 — F-089; the border-status table held at "
             "EX23-06 since derivation)")

    def rule_rest(case):
        q = case.get("query")
        if q == "sabbatical_verbs_split":
            return [V("hoeing_and_stones_two_hoeings", "תשמטנה "
                      "('release it') from HOEING, ונטשתה ('let "
                      "it lie') from STONE-CLEARING (23:11); Rav "
                      "Ukva bar Chama's refinement: two hoeings — "
                      "sealing cracks permitted (survival), "
                      "strengthening trees forbidden "
                      "(cultivation) (Sukkah 44b:7)",
                      authority="Rav Ukva bar Chama",
                      machine_claim="EX23-15", **RS)]
        if q == "uncircumcised_slave_keeping":
            return [V("keeping_permitted", "וינפש בן אמתך ('the "
                      "son of your maidservant shall be "
                      "refreshed,' 23:12) — written of the "
                      "UNCIRCUMCISED slave: one may keep him "
                      "(Yevamot 48b:4-5)",
                      authority="R. Yishmael",
                      machine_claim="EX23-15", **RS),
                    V("keeping_forbidden", "the verse speaks of "
                      "one bought at TWILIGHT with no time to "
                      "circumcise (48b:4) — the narrowing read; "
                      "practice rider noted: twelve months, then "
                      "resold (48b:7, rabbinic layer)",
                      authority="R. Akiva", **RS)]
        if q == "resident_stranger_identity":
            return [V("resident_stranger", "והגר ('and the "
                      "stranger,' 23:12) = the RESIDENT stranger; "
                      "the righteous convert is already at 'your "
                      "stranger within your gates' (48b:6) — "
                      "EX23-06's border-status table arrived "
                      "answered",
                      machine_claim="EX23-15", **RS)]
        if q == "idol_name_mention":
            return [V("forbidden_four_channels", "ושם אלהים אחרים "
                      "לא תזכירו ('the name of other gods you "
                      "shall not mention,' 23:13): no appointments "
                      "by an idol landmark; לא ישמע על פיך — no "
                      "vowing by it, no affirming by it, no "
                      "causing OTHERS to (Sanhedrin 63b:5); the "
                      "second reading — the enticer's warning — "
                      "recorded to block 8's file (63b:6)",
                      machine_claim="EX23-15", **RS)]
        if q == "sabbatical_shabbat_error":
            return [V("partial_error_resolved", "the court ruling "
                      "'no Shabbat in the Sabbatical' errs in "
                      "בחריש ובקציר תשבת ('in plowing and in "
                      "harvest you shall rest,' 34:21) — R. "
                      "Zeira's dilemma (whole uprooting or "
                      "partial?) RESOLVED by Ravina from the "
                      "prophet baraita: partial nullification "
                      "with partial fulfillment (Horayot 4b:8-10) "
                      "— riding EX34-08's harvest-rest arm",
                      authority="Ravina",
                      machine_claim="EX34-10", **RS)]
        return None

    return {
        "appearance_exemptions": {"fn": rule_appearance},
        "festival_labor_license": {"fn": rule_labor},
        "feast_offering_machine": {"fn": rule_offering},
        "firstborn_sanctification": {"fn": rule_firstborn},
        "rest_scope": {"fn": rule_rest},
    }
