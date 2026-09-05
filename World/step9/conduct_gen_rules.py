# conduct_gen_rules.py — round 40, THE CONDUCT TORAH (Genesis exam
# block 11 of 12, 2026-09-04). Read-source:
# logic/oral_triage/genesis_block_conduct_2026-09-04.md.


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    RT = _EX("Avodah Zarah 25b:7-9; Bava Kamma 60b:5-7; Taanit "
             "10b:7-8; Shabbat 32a:3-5",
             "Gen 33:14 + 12:10 + 45:24 + 32:11 (gen_56 G56-31 / "
             "F-174; gen_28 G28-14 / F-175; gen_68 G68-30 / F-176; "
             "gen_55 G55-38 / F-177)")
    HC = _EX("Bava Metzia 87a:1-3, 59a:10-12; Berakhot 61a:18-25",
             "Gen 19:3 + 18:5-7 + 12:16 + 2:22 + 24:61 (gen_35 "
             "G35-29 / F-178; gen_34 G34-26 / F-179; gen_28 "
             "G28-14; gen_09 G09-21 / F-180; gen_41 G41-36 / "
             "F-181)")
    SC = _EX("Eruvin 18b:12-15; Berakhot 55b:16-18, 34b:2-4; "
             "Taanit 10b:5-6",
             "Gen 7:1 + 41:13 + 37:10 + 42:1 (gen_17 G17-21 / "
             "F-182; gen_64 G64-36 / F-183; gen_60 G60-24 / "
             "F-184; gen_65 G65-37 / F-185)")
    LM = _EX("Bava Metzia 93b:2-4, 106b:4-6",
             "Gen 31:40 + 8:22 (gen_54 G54-44 / F-186; gen_20 "
             "G20-21 / F-187)")
    CC = _EX("Arakhin 16b:17; Berakhot 25b:11; Shabbat 151b:9; "
             "Shabbat 95a:1 (standing)",
             "Gen 13:3 + 9:23 + 9:2 + 2:22 (standing seats)")

    def rule_road_torah(case):
        q = case.get("query")
        if q == "travelers_ruse":
            return [V("widen_the_road",
                      "asked where he is heading by a dangerous "
                      "escort, ירחיב לו את הדרך ('let him WIDEN the "
                      "road for him') — as Jacob to Esau: עד אשר "
                      "אבא אל אדני שעירה ('until I come to my lord "
                      "to SEIR,' Gen 33:14) — ויעקב נסע סכתה ('and "
                      "Jacob journeyed to SUKKOT,' 33:17): the "
                      "recorded ruse as survival law — Avodah "
                      "Zarah 25b:8-9",
                      authority="the baraita",
                      machine_claim="G56-31", **RT)]
        if q == "famine_scatter":
            return [V("leave_the_famine_city",
                      "רעב בעיר פזר רגליך ('FAMINE in the city — "
                      "SCATTER your feet'): ויהי רעב בארץ וירד "
                      "אברם מצרימה ('there was famine in the land, "
                      "and Abram went DOWN to Egypt to sojourn,' "
                      "Gen 12:10), with the second verse for the "
                      "mortal-doubt case — Bava Kamma 60b:6-7",
                      authority="the baraita",
                      machine_claim="G28-14", **RT)]
        if q == "road_engrossment_ban":
            return [V("study_yes_engross_no",
                      "אל תרגזו בדרך ('do not quarrel on the way,' "
                      "Gen 45:24) — R. Elazar: Joseph to his "
                      "brothers — do not ENGROSS yourselves in a "
                      "matter of law lest the road rage upon you; "
                      "reconciled with the "
                      "fit-to-burn-without-Torah row: recite yes, "
                      "delve no — Taanit 10b:7-8",
                      authority="R. Elazar",
                      machine_claim="G68-30", **RT)]
        if q == "miracle_reliance_ban":
            return [V("merit_deducted",
                      "R. Yannai: never stand in danger saying a "
                      "miracle will be done — perhaps none is done, "
                      "and if done, מנכין לו מזכיותיו ('they DEDUCT "
                      "it from his merits'): R. Chanin — the verse "
                      "is קטנתי מכל החסדים ('I am DIMINISHED by all "
                      "the kindnesses,' Gen 32:11): Jacob's own "
                      "accounting as the rule's source — Shabbat "
                      "32a:4",
                      authority="R. Yannai with R. Chanin's verse",
                      machine_claim="G55-38", **RT)]
        return None

    def rule_household_conduct(case):
        q = case.get("query")
        if q == "host_refusal_ladder":
            return [V("lesser_yes_greater_no",
                      "ויפצר בם מאד ('and he URGED them greatly,' "
                      "Gen 19:3) — R. Elazar: מכאן שמסרבין לקטן "
                      "ואין מסרבין לגדול ('from here: one refuses "
                      "the LESSER, and does not refuse the "
                      "GREATER') — the urging verb calibrating "
                      "refusal etiquette — Bava Metzia 87a:1",
                      authority="R. Elazar",
                      machine_claim="G35-29", **HC)]
        if q == "say_little_do_much":
            return [V("righteous_little_wicked_much",
                      "bread promised — ואקחה פת לחם ('and I will "
                      "take a MORSEL of bread,' Gen 18:5) — cattle "
                      "run for (18:7): צדיקים אומרים מעט ועושים "
                      "הרבה ('the RIGHTEOUS say little and do "
                      "much'); the wicked exemplar is EPHRON — "
                      "four hundred shekels spoken, centenaria "
                      "exacted (87a:3, the same currency row the "
                      "inheritance block seated) — Bava Metzia "
                      "87a:2-3",
                      authority="R. Elazar",
                      machine_claim="G34-26", **HC)]
        if q == "honor_your_wife":
            return [V("blessing_for_her_sake",
                      "R. Chelbo: blessing is found in a man's "
                      "house only for his WIFE'S sake — ולאברם "
                      "הטיב בעבורה ('and he did good to Abram FOR "
                      "HER SAKE,' Gen 12:16); Rava to the Mechoza "
                      "men: honor your wives that you may grow "
                      "rich — Bava Metzia 59a:11",
                      authority="R. Chelbo with Rava's practice",
                      machine_claim="G28-14", **HC)]
        if q == "escort_duty":
            return [V("greater_escorts_lesser",
                      "ויבאה אל האדם ('and He BROUGHT her to the "
                      "man,' Gen 2:22) — R. Yirmiya ben Elazar: "
                      "the Holy One became BEST MAN to the first "
                      "man: from here the Torah taught conduct — "
                      "the greater escorts the lesser and lets it "
                      "not trouble him — Berakhot 61a:19",
                      authority="R. Yirmiya ben Elazar",
                      machine_claim="G09-21", **HC)]
        if q == "riding_order":
            return [V("behind_not_before",
                      "Rav Ashi: ותלכנה אחרי האיש ('and they went "
                      "AFTER the man,' Gen 24:61 — Rebekah and her "
                      "maidens riding) — ולא לפני "
                      "האיש ('and NOT before the man'): the "
                      "behind-not-before ladder with R. Yochanan's "
                      "gradations beside — Berakhot 61a:24-25",
                      authority="Rav Ashi",
                      machine_claim="G41-36", **HC)]
        return None

    def rule_speech_conduct(case):
        q = case.get("query")
        if q == "praise_in_presence":
            return [V("partial_to_face_full_away",
                      "R. Yirmiya ben Elazar: מקצת שבחו של אדם "
                      "אומרים בפניו וכולו שלא בפניו ('PART of a "
                      "man's praise is said to his face, ALL of it "
                      "not to his face') — to his face: כי אתך "
                      "ראיתי צדיק ('for YOU I have seen righteous,' "
                      "Gen 7:1); away: 'a righteous man, PERFECT' "
                      "(6:9) — the narrator/address ink delta as "
                      "conduct law — Eruvin 18b:13-14",
                      authority="R. Yirmiya ben Elazar",
                      machine_claim="G17-21", **SC)]
        if q == "dreams_follow_mouth":
            return [V("interpretation_binds",
                      "R. Elazar: whence that כל החלומות הולכים אחר "
                      "הפה ('all DREAMS FOLLOW THE MOUTH')? — ויהי "
                      "כאשר פתר לנו כן היה ('as he INTERPRETED for "
                      "us, so it WAS,' Gen 41:13); Rava's cap: "
                      "only when the reading fits the dream ('each "
                      "per his dream he interpreted,' 41:12); R. "
                      "Bena'a's twenty-four interpreters beside — "
                      "Berakhot 55b:16-17",
                      authority="R. Elazar with Rava's cap",
                      machine_claim="G64-36", **SC)]
        if q == "bowing_taxonomy":
            return [V("prostration_spread_of_limbs",
                      "the baraita's taxonomy: kidah on the FACE; "
                      "keriah on the KNEES; השתחואה זו פשוט ידים "
                      "ורגלים ('PROSTRATION — the spreading of "
                      "hands and feet'): הבוא נבוא ('shall we "
                      "indeed COME') להשתחות לך ארצה ('to BOW to "
                      "you to the GROUND,' Gen 37:10) — Joseph's "
                      "dream "
                      "supplying the full-prostration definition — "
                      "Berakhot 34b:3",
                      authority="the baraita",
                      machine_claim="G60-24", **SC)]
        if q == "satiety_display_ban":
            return [V("do_not_show_yourselves",
                      "one who forgot and ate on a fast day — let "
                      "him not display it: למה תתראו ('WHY DO YOU "
                      "SHOW YOURSELVES?,' Gen 42:1) — Jacob to his "
                      "sons: do not show yourselves sated, not "
                      "before Esau nor before Ishmael, that they "
                      "not envy you — Taanit 10b:5-6",
                      authority="the baraita",
                      machine_claim="G65-37", **SC)]
        return None

    def rule_labor_measures(case):
        q = case.get("query")
        if q == "paid_keeper_standard":
            return [V("jacobs_extra_guarding_ceiling",
                      "how far must a paid keeper guard? עד כדי "
                      "הייתי ביום אכלני חרב וקרח בלילה ('as far as: "
                      "by day the HEAT consumed me, and the FROST "
                      "by night,' Gen 31:40); the challenge — was "
                      "Jacob a town watchman? — answered from his "
                      "own words: 'I guarded for you EXTRA "
                      "guarding, like the town watchmen' — Jacob's "
                      "clause as the care standard's recorded "
                      "ceiling — Bava Metzia 93b:3",
                      authority="the sugya",
                      machine_claim="G54-44", **LM)]
        if q == "six_seasons":
            return [V("six_two_month_seasons",
                      "the sharecropper law's calendar: R. Shimon "
                      "ben Gamliel in R. Meir's name — half "
                      "Tishrei, Marcheshvan, half Kislev SEED; "
                      "half Kislev, Tevet, half Shevat WINTER; "
                      "half Shevat, Adar, half Nisan COLD; half "
                      "Nisan, Iyar, half Sivan HARVEST; half "
                      "Sivan, Tammuz, half Av SUMMER; half Av, "
                      "Elul, half Tishrei HEAT — the six "
                      "two-month seasons implementing 'seedtime "
                      "and harvest, cold and heat, summer and "
                      "winter' (Gen 8:22) — Bava Metzia 106b:5-6",
                      authority="R. Shimon ben Gamliel in R. "
                                "Meir's name",
                      machine_claim="G20-21", **LM)]
        return None

    def rule_conduct_credits(case):
        q = case.get("query")
        if q == "lodging_loyalty":
            return [V("keep_your_lodging",
                      "do not change your lodging — אל המקום אשר "
                      "היה שם אהלה בתחלה ('to the place where his "
                      "tent had been AT FIRST,' Gen 13:3); "
                      "STANDING: gen_29's read holds the row — "
                      "Arakhin 16b:17",
                      authority="the gemara", **CC)]
        if q == "nakedness_bars_shema":
            return [V("bars_the_recitation",
                      "a gentile's nakedness bars the Shema — "
                      "וערות אביהם לא ראו ('and their father's "
                      "nakedness they did not SEE,' Gen 9:23); "
                      "STANDING: gen_23's read — Berakhot 25b:11",
                      authority="the gemara", **CC)]
        if q == "dread_grant_condition":
            return [V("live_only_condition",
                      "the dread-of-you grant read as a LIVE-ONLY "
                      "condition (a day-old alive needs no guard; "
                      "dead Og does) — Gen 9:2; STANDING: gen_21's "
                      "read — Shabbat 151b:9",
                      authority="the gemara", **CC)]
        if q == "hair_plaiting_building":
            return [V("building_by_the_build_verb",
                      "hair-plaiting on Shabbat is BUILDING — He "
                      "BUILT the rib and braided Eve's hair (Gen "
                      "2:22); STANDING SEAT: G09-17 holds the "
                      "labor category — Shabbat 95a:1",
                      authority="the gemara",
                      machine_claim="G09-17 (standing)", **CC)]
        return None

    return {
        "road_torah": {"fn": rule_road_torah,
                       "tractate": "Avodah Zarah"},
        "household_conduct": {"fn": rule_household_conduct,
                              "tractate": "Bava Metzia"},
        "speech_conduct": {"fn": rule_speech_conduct,
                           "tractate": "Berakhot"},
        "labor_measures": {"fn": rule_labor_measures,
                           "tractate": "Bava Metzia"},
        "conduct_credits": {"fn": rule_conduct_credits,
                            "tractate": "Arakhin"},
    }
