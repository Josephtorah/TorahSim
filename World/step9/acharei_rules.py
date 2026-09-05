# acharei_rules.py — round 44, THE ACHAREI MOT-KEDOSHIM EXAM
# (2026-09-05). Bare Mishnah rows citing Lev 16-20, graded after the
# derivation. Read-source:
# logic/oral_triage/acharei_exam_mishnah_2026-09-05.md.


def build(V):
    def _EX(mishnah, anchor, **extra):
        d = dict(talmud_source=mishnah, exodus_anchor=anchor)
        d.update(extra)
        return d

    YS = _EX("Mishnah Yoma 1:1-7:1; Sotah 7:7; Kelim 1:9; Menachot "
             "3:6; Parah 8:3; Megillah 3:5; Horayot 2:2; Tamid 6:3",
             "Lev 16:1-34 (lev_16 units, LV16A/LV16B claims — the "
             "Yom Kippur service machine)")
    AT = _EX("Mishnah Yoma 8:9; Shevuot 1:3; 1:6; Keritot 1:1; "
             "Makkot 3:15",
             "Lev 16:16-34 (lev_16_yk_goat_statute, LV16B-06/07 — "
             "the atonement routing table)")
    OS = _EX("Mishnah Zevachim 14:1; 14:2; Avodah Zarah 5:9; "
             "Kiddushin 2:9; Beitzah 1:2; Eduyot 4:2",
             "Lev 17:1-16 (lev_17_blood_center, LV17-01/07)")
    AS = _EX("Mishnah Sanhedrin 1:4; 7:2-7:7; 9:1; 11:1; Keritot "
             "3:6; Megillah 4:9; Avodah Zarah 2:1",
             "Lev 20:1-27 (lev_20_sanctions, LV20 claims)")
    LE = _EX("Mishnah Yevamot 1:1; 3:4; 11:1; Eduyot 4:8; Kiddushin "
             "2:7; Bikkurim 2:11; 4:2",
             "Lev 18:16-18 + 20:17-21 (lev_18_sexual_land + "
             "lev_20_sanctions, LV18-06/LV20-07 — the levirate "
             "window)")
    HC = _EX("Mishnah Nedarim 9:4; Sanhedrin 3:7; Bava Metzia 4:8; "
             "5:11; 9:11; 9:12; 10:5; Shevuot 4:13; Shabbat 6:10; "
             "Kiddushin 1:7; Keritot 2:2; 2:5; 6:9; Makkot 3:2-3:14; "
             "Bava Kamma 5:7; Zevachim 5:5",
             "Lev 19:1-37 (lev_19 units, LV19A/LV19B claims — the "
             "holiness charter)")
    PG = _EX("Mishnah Peah 7:3; 7:6; 7:7; Eduyot 4:3; 4:5; Niddah "
             "6:6; Terumot 3:9; 11:3; Meilah 4:6; Sukkah 1:4",
             "Lev 19:9-10; 19:23-25 (lev_19 units, LV19A-04/"
             "LV19B-03; the covering predicate LV17-07)")

    def rule_yoma_service_file(case):
        q = case.get("query")
        if q == "substitute_wife_condition":
            return [V("r_yehuda_ready_wife",
                      "a second wife readied lest his die — 'his "
                      "house, that is his wife'",
                      authority="R. Yehuda — Mishnah Yoma 1:1",
                      machine_claim="LV16B-07", **YS),
                    V("no_end_to_the_matter",
                      "the Sages: 'if so, THE MATTER HAS NO END' — "
                      "the induction limit, standing VERBATIM in the "
                      "Sifra exchange at the seat",
                      authority="the Sages — Mishnah Yoma 1:1",
                      machine_claim="LV16B-07", **YS)]
        if q == "unequal_goats_validity":
            return [V("equal_required_unequal_valid",
                      "equal in look, height, price, purchase — yet "
                      "valid unequal: the requirement/validity split "
                      "the Sifra reads off 'two' and the doubled "
                      "'goat... goat'",
                      authority="Mishnah Yoma 6:1",
                      machine_claim="LV16A-03", **YS)]
        if q == "two_goats_indispensable":
            return [V("they_block_each_other",
                      "the two goats of Yom Kippur block each other "
                      "— first in the blocking census",
                      authority="Mishnah Menachot 3:6",
                      machine_claim="LV16A-03", **YS)]
        if q == "goat_died_after_lottery":
            return [V("relot_pair_second_grazes",
                      "bring a new pair, re-lot with the standing "
                      "formula; the second grazes till blemished — "
                      "'no communal sin offering dies'",
                      authority="the Sages — Mishnah Yoma 6:1",
                      machine_claim="LV16A-05", **YS),
                    V("r_yehuda_second_dies",
                      "R. Yehuda: it dies — the Sifra's other arm",
                      authority="R. Yehuda — Mishnah Yoma 6:1",
                      machine_claim="LV16A-05", **YS)]
        if q == "blood_spilled_goat_link":
            return [V("both_restart_together",
                      "blood spilled — the dispatch goat dies; the "
                      "goat dead — the blood is spilled: R. Yehuda's "
                      "linked-failure law, the Sifra's own line",
                      authority="R. Yehuda — Mishnah Yoma 6:1",
                      machine_claim="LV16A-05", **YS)]
        if q == "first_confession_formula":
            return [V("his_own_and_his_house",
                      "the first confession — himself and his house, "
                      "the formula and the response verbatim",
                      authority="Mishnah Yoma 3:8",
                      machine_claim="LV16A-03", **YS)]
        if q == "second_confession_formula":
            return [V("adds_sons_of_aaron",
                      "the second — his house AND the sons of Aaron, "
                      "the holy people",
                      authority="Mishnah Yoma 4:2",
                      machine_claim="LV16B-01", **YS)]
        if q == "third_confession_formula":
            return [V("your_people_house_israel",
                      "the third, on the dispatch goat — 'Your "
                      "people the house of Israel,' the Explicit "
                      "Name, the prostration response",
                      authority="Mishnah Yoma 6:2",
                      machine_claim="LV16B-01", **YS)]
        if q == "bull_blood_holding":
            return [V("stirrer_fourth_terrace",
                      "handed to the one who stirs it on the fourth "
                      "terrace so it not congeal — the held process "
                      "variable, word for word",
                      authority="Mishnah Yoma 4:3",
                      machine_claim="LV16A-07", **YS)]
        if q == "coal_pan_today_vs_daily":
            return [V("gold_three_kav_today",
                      "daily silver-into-gold and four-into-three "
                      "kav; today gold throughout, three kav — the "
                      "transmitted quantities table",
                      authority="Mishnah Yoma 4:4",
                      machine_claim="LV16A-06", **YS),
                    V("r_yosei_seah_daily",
                      "R. Yosei: daily a se'ah into three kav — the "
                      "Sifra's variant row kept",
                      authority="R. Yosei — Mishnah Yoma 4:4",
                      machine_claim="LV16A-06", **YS)]
        if q == "sprinkle_geometry_count":
            return [V("one_up_seven_down_whip_count",
                      "one above seven below, aimed neither up nor "
                      "down but like a whip; counted one, "
                      "one-and-one... one-and-seven",
                      authority="Mishnah Yoma 5:4",
                      machine_claim="LV16A-07", **YS)]
        if q == "inner_altar_corner_order":
            return [V("ne_nw_sw_se_ends_where_outer_starts",
                      "northeast, northwest, southwest, southeast — "
                      "ending on the inner altar where the outer sin "
                      "offering begins",
                      authority="Mishnah Yoma 5:5",
                      machine_claim="LV16A-08", **YS),
                    V("r_eliezer_stands_in_place",
                      "R. Eliezer: he stands in place and applies to "
                      "all, bottom-up except the corner before him",
                      authority="R. Eliezer — Mishnah Yoma 5:5",
                      machine_claim="LV16A-08", **YS)]
        if q == "dispatcher_clothes_window":
            return [V("jerusalem_wall",
                      "clothes defile from leaving Jerusalem's wall",
                      authority="Mishnah Yoma 6:6",
                      machine_claim="LV16B-02", **YS),
                    V("r_shimon_at_the_push",
                      "R. Shimon: from the push at the cliff — the "
                      "Sifra's third arm (R. Yosei's cliff-arrival "
                      "the middle term)",
                      authority="R. Shimon — Mishnah Yoma 6:6",
                      machine_claim="LV16B-02", **YS)]
        if q == "burner_clothes_window":
            return [V("azarah_wall",
                      "the burnt pair's carriers defile from the "
                      "azarah wall",
                      authority="Mishnah Yoma 6:7",
                      machine_claim="LV16B-04", **YS),
                    V("r_shimon_fire_holds_most",
                      "R. Shimon: when the fire has caught most of "
                      "them — the Sifra's arm at the seat",
                      authority="R. Shimon — Mishnah Yoma 6:7",
                      machine_claim="LV16B-04", **YS)]
        if q == "goat_defiles_dispatcher_not_itself":
            return [V("handlers_defile_carcasses_do_not",
                      "the dispatcher and burners defile clothes; "
                      "goat and bulls themselves do not — 'my "
                      "defilers did not defile me and you defiled "
                      "me'",
                      authority="Mishnah Parah 8:3",
                      machine_claim="LV16B-04", **YS)]
        if q == "innermost_entry_gradient":
            return [V("high_priest_yk_service_only",
                      "the holy of holies entered only by the high "
                      "priest on Yom Kippur at the service — the "
                      "graded ban as the sanctity ladder's capstone",
                      authority="Mishnah Kelim 1:9",
                      machine_claim="LV16A-01", **YS)]
        if q == "yk_reading_protocol":
            return [V("acharei_mot_plus_tenth_by_heart",
                      "reads Acharei Mot and 'But on the tenth'; the "
                      "census-book tenth by heart; eight blessings",
                      authority="Mishnah Yoma 7:1; Sotah 7:7",
                      machine_claim="LV16B-03", **YS)]
        if q == "incense_start_warning":
            return [V("not_toward_yourself_lest_burned",
                      "'be careful not to begin toward yourself, "
                      "lest you be burned' — the daily incense "
                      "protocol beside the inside-only law",
                      authority="Mishnah Tamid 6:3",
                      machine_claim="LV16A-06", **YS)]
        return None

    def rule_yk_atonement_file(case):
        q = case.get("query")
        if q == "day_atones_fellow_sins":
            return [V("not_until_he_appeases",
                      "between man and God the day atones; between "
                      "man and his fellow not until he appeases him "
                      "— R. Elazar ben Azariah's derivation, the "
                      "Sifra's own row at the seat",
                      authority="Mishnah Yoma 8:9",
                      machine_claim="LV16B-06", **AT)]
        if q == "knowledge_end_only_route":
            return [V("outer_goat_and_day",
                      "no knowledge at start, knowledge at end — the "
                      "outer goat and the day atone ('what this "
                      "atones, that atones')",
                      authority="Mishnah Shevuot 1:3",
                      machine_claim="LV16B-07", **AT)]
        if q == "all_other_transgressions_route":
            return [V("dispatched_goat_atones",
                      "deliberate sanctuary defilement — the inner "
                      "goat and the day; ALL other transgressions, "
                      "light and severe — the dispatched goat: the "
                      "routing table's closing row word for word",
                      authority="Mishnah Shevuot 1:6",
                      machine_claim="LV16B-07", **AT)]
        if q == "karet_census_count":
            return [V("thirty_six_kritot",
                      "thirty-six karet classes — the unions, "
                      "Molech, the ghost-pit, blood, outside "
                      "slaughter and raising, the day's eating and "
                      "work: this span the census's spine",
                      authority="Mishnah Keritot 1:1",
                      machine_claim="LV18-07", **AT)]
        if q == "lashes_discharge_karet":
            return [V("lashed_is_your_brother",
                      "all karet-liable who were lashed are "
                      "discharged — 'when lashed, he is your "
                      "brother'",
                      authority="R. Chananya ben Gamliel — Mishnah "
                                "Makkot 3:15",
                      machine_claim="LV18-03", **AT),
                    V("r_shimon_live_by_them",
                      "R. Shimon from its own place — the doers cut "
                      "off, but 'which a man shall DO and LIVE': the "
                      "abstainer rewarded as a doer, read off our "
                      "18:5 and 18:29 clauses",
                      authority="R. Shimon — Mishnah Makkot 3:15",
                      machine_claim="LV18-03", **AT)]
        return None

    def rule_outside_slaughter_file(case):
        q = case.get("query")
        if q == "dispatched_goat_offered_outside":
            return [V("exempt_unfit_for_the_door",
                      "the dispatched goat offered outside — exempt: "
                      "'whatever is not fit to come to the tent door "
                      "carries no liability' — the Sifra's own "
                      "to-the-LORD carve at the seat",
                      authority="Mishnah Zevachim 14:1",
                      machine_claim="LV17-01", **OS)]
        if q == "unfit_animal_offered_outside":
            return [V("exempt_before_the_tabernacle",
                      "the unfit list offered outside — exempt "
                      "('before the tabernacle')",
                      authority="Mishnah Zevachim 14:2",
                      machine_claim="LV17-01", **OS),
                    V("r_shimon_deferred_negative",
                      "R. Shimon: the time-deferred stand under a "
                      "plain negative without karet — the Sifra's "
                      "dissent verbatim",
                      authority="R. Shimon — Mishnah Zevachim 14:2",
                      machine_claim="LV17-01", **OS)]
        if q == "dispatched_goat_benefit":
            return [V("forbidden_in_any_amount",
                      "the dispatched goat in the forbidden-in-any-"
                      "amount list — the live goat as prohibited "
                      "substance",
                      authority="Mishnah Avodah Zarah 5:9",
                      machine_claim="LV17-01", **OS)]
        if q == "betrothal_by_banned_fruit":
            return [V("void_but_proceeds_valid",
                      "betrothal by orlah or the vineyard mixture — "
                      "void; sold them and betrothed by the money — "
                      "valid: the benefit ban priced",
                      authority="Mishnah Kiddushin 2:9",
                      machine_claim="LV19B-03", **OS)]
        if q == "covering_blood_on_festival":
            return [V("shammai_dig_with_dibber",
                      "Beit Shammai: dig with the dibber and cover",
                      authority="Beit Shammai — Mishnah Beitzah 1:2",
                      machine_claim="LV17-07", **OS),
                    V("hillel_prepared_dust_only",
                      "Beit Hillel: no slaughter unless dust stood "
                      "prepared while yet day; both concede after "
                      "the fact",
                      authority="Beit Hillel — Mishnah Beitzah 1:2",
                      machine_claim="LV17-07", **OS)]
        if q == "festival_cover_in_leniency_list":
            return [V("registered_house_dispute",
                      "the same case in Eduyot's registry of the "
                      "houses' disputes — the record row",
                      authority="Mishnah Eduyot 4:2",
                      machine_claim="LV17-07", **OS)]
        return None

    def rule_arayot_sanctions_file(case):
        q = case.get("query")
        if q == "beast_partner_court_size":
            return [V("twenty_three_from_our_verses",
                      "the beast partners judged by twenty-three — "
                      "'you shall kill the woman and the beast'; "
                      "'and the beast you shall kill': Lev 20:15-16 "
                      "cited as the court-size source",
                      authority="Mishnah Sanhedrin 1:4",
                      machine_claim="LV20-06", **AS)]
        if q == "burning_procedure":
            return [V("lit_wick_into_the_mouth",
                      "the burning: dung to the knees, the scarves, "
                      "the lit wick poured in — and the bundled-"
                      "branches story refused ('that court was not "
                      "expert')",
                      authority="Mishnah Sanhedrin 7:2",
                      machine_claim="LV20-05", **AS)]
        if q == "strangulation_procedure":
            return [V("dung_scarves_two_pull",
                      "sunk in dung to the knees, hard scarf inside "
                      "soft, two pull until the soul departs — the "
                      "Sifra's own words at the seat",
                      authority="Mishnah Sanhedrin 7:3",
                      machine_claim="LV20-04", **AS)]
        if q == "stoned_list_membership":
            return [V("our_chapter_supplies_the_spine",
                      "the stoned census — father's wife, daughter-"
                      "in-law, the male, the beast, the woman with "
                      "it, Molech, ghost-pit and familiar, the "
                      "curser: Lev 20's rows as the list's spine",
                      authority="Mishnah Sanhedrin 7:4",
                      machine_claim="LV20-03", **AS)]
        if q == "mother_double_count":
            return [V("two_names_mother_and_fathers_wife",
                      "the mother carries mother AND father's-wife "
                      "liability",
                      authority="Mishnah Sanhedrin 7:4",
                      machine_claim="LV20-05", **AS),
                    V("r_yehuda_mother_only",
                      "R. Yehuda: qua mother alone — the Sifra's "
                      "single-count arm ('you make him liable for "
                      "the mother, not the father's wife')",
                      authority="R. Yehuda — Mishnah Sanhedrin 7:4",
                      machine_claim="LV20-05", **AS)]
        if q == "why_the_beast_dies":
            return [V("stumbling_through_it",
                      "'if the man sinned, what did the beast sin? "
                      "— the stumbling came to a man through it'",
                      authority="Mishnah Sanhedrin 7:4",
                      machine_claim="LV20-06", **AS),
                    V("market_would_name_the_sin",
                      "the second reason: that the beast not pass in "
                      "the market and they say 'this is the one...' "
                      "— the added arm beside the Sifra's",
                      authority="Mishnah Sanhedrin 7:4",
                      machine_claim="LV20-06", **AS)]
        if q == "molech_partial_acts":
            return [V("hand_and_pass_both_required",
                      "not liable until he HANDS OVER to Molech AND "
                      "PASSES through fire — handed-not-passed "
                      "exempt, passed-not-handed exempt: the four-"
                      "condition predicate verbatim",
                      authority="Mishnah Sanhedrin 7:7",
                      machine_claim="LV20-01", **AS)]
        if q == "woman_and_daughter_scope":
            return [V("nine_relations_by_zimah_analogy",
                      "'a woman and her daughter' spans nine "
                      "relations — daughter, granddaughters, her "
                      "line, mother-in-law and both grandmothers-"
                      "in-law: the zimah verbal analogy's yield",
                      authority="Mishnah Sanhedrin 9:1",
                      machine_claim="LV20-05", **AS)]
        if q == "curser_vs_striker_after_death":
            return [V("curser_liable_striker_exempt",
                      "the curser after death liable, the striker "
                      "after death exempt — the Sifra's dead-parent "
                      "curse at the seat",
                      authority="Mishnah Sanhedrin 11:1",
                      machine_claim="LV20-03", **AS)]
        if q == "mother_in_law_name_count":
            return [V("seven_liability_names",
                      "the mother-in-law carries seven names in one "
                      "act — the union machinery compounding",
                      authority="Mishnah Keritot 3:6",
                      machine_claim="LV20-07", **AS),
                    V("r_yochanan_three_names",
                      "R. Yochanan ben Nuri adds the two "
                      "grandmothers-in-law; answered 'the three are "
                      "one name'",
                      authority="R. Yochanan ben Nuri — Mishnah "
                                "Keritot 3:6",
                      machine_claim="LV20-07", **AS)]
        if q == "molech_verse_aramean_rendering":
            return [V("silenced_with_rebuke",
                      "rendering 18:21 'to pass in Aramean-ness' — "
                      "silenced WITH REBUKE: the tradition policing "
                      "the verse's translation layer",
                      authority="Mishnah Megillah 4:9",
                      machine_claim="LV18-01", **AS)]
        if q == "gentile_suspicion_triad":
            return [V("bestiality_unions_bloodshed",
                      "no lodging beasts, no seclusion — suspected "
                      "of the three defilement classes the Sifra "
                      "names at 16:16",
                      authority="Mishnah Avodah Zarah 2:1",
                      machine_claim="LV16A-08", **AS)]
        return None

    def rule_levirate_file(case):
        q = case.get("query")
        if q == "fifteen_women_rivals":
            return [V("exempt_to_the_end_of_the_world",
                      "fifteen women exempt their rivals and their "
                      "rivals' rivals from release and levirate TO "
                      "THE END OF THE WORLD — the Sifra's own "
                      "sentence at the seat",
                      authority="Mishnah Yevamot 1:1",
                      machine_claim="LV18-06", **LE)]
        if q == "two_brothers_two_sisters":
            return [V("release_not_levirate",
                      "three brothers, two wed to sisters — the "
                      "widows release and do not enter levirate; "
                      "the union-grade forks recorded",
                      authority="Mishnah Yevamot 3:4",
                      machine_claim="LV18-06", **LE)]
        if q == "marrying_raped_womans_kin":
            return [V("permitted_no_marriage_path",
                      "one marries the raped or seduced woman's kin "
                      "— liability runs on the marriage path only",
                      authority="Mishnah Yevamot 11:1",
                      machine_claim="LV20-05", **LE),
                    V("r_yehuda_bans_fathers_victim",
                      "R. Yehuda forbids the father's victim — the "
                      "dissent kept",
                      authority="R. Yehuda — Mishnah Yevamot 11:1",
                      machine_claim="LV20-05", **LE)]
        if q == "rivals_to_the_brothers":
            return [V("shammai_permit",
                      "Beit Shammai permit the rivals to the "
                      "brothers",
                      authority="Beit Shammai — Mishnah Eduyot 4:8",
                      machine_claim="LV18-06", **LE),
                    V("hillel_forbid",
                      "Beit Hillel forbid — the fifteen-women "
                      "table's hinge dispute, the houses' peace "
                      "kept on the record",
                      authority="Beit Hillel — Mishnah Eduyot 4:8",
                      machine_claim="LV18-06", **LE)]
        if q == "betrothing_woman_and_daughter_as_one":
            return [V("neither_betrothed",
                      "a woman and her daughter, or two sisters, as "
                      "one — neither betrothed: the ban voiding the "
                      "acquisition act (the basket-of-figs case)",
                      authority="Mishnah Kiddushin 2:7",
                      machine_claim="LV20-05", **LE)]
        if q == "koy_mixture_status":
            return [V("kilayim_with_both_classes",
                      "the koy — mixture-barred with beast and wild "
                      "animal both: the ban meeting the boundary "
                      "species",
                      authority="Mishnah Bikkurim 2:11",
                      machine_claim="LV19B-01", **LE)]
        if q == "double_sexed_male_duties":
            return [V("bound_to_levirate_like_men",
                      "the double-sexed 'like men' — defiles by "
                      "white discharge, bound to the levirate, "
                      "wraps and shears like men",
                      authority="Mishnah Bikkurim 4:2",
                      machine_claim="LV20-07", **LE)]
        return None

    def rule_holiness_conduct_file(case):
        q = case.get("query")
        if q == "vow_opened_by_our_verses":
            return [V("revenge_grudge_hate_love_stack",
                      "R. Meir opens vows from the written Torah — "
                      "'had you known you transgress lo tikom, lo "
                      "titor, lo tisna, and veahavta lereacha "
                      "kamocha' — the seat's own stack quoted as "
                      "the regret gate",
                      authority="R. Meir — Mishnah Nedarim 9:4",
                      machine_claim="LV19A-08", **HC)]
        if q == "judge_reveals_split_vote":
            return [V("talebearing_reveals_secrets",
                      "'I acquitted but my colleagues outnumbered "
                      "me' — of him: 'a talebearer reveals secrets' "
                      "— the Sifra's protocol and secrecy rows "
                      "verbatim",
                      authority="Mishnah Sanhedrin 3:7",
                      machine_claim="LV19A-08", **HC)]
        if q == "wage_collection_windows":
            return [V("day_all_night_night_all_day",
                      "day wages collectible all night, night wages "
                      "all day — with the hourly and term "
                      "extensions",
                      authority="Mishnah Bava Metzia 9:11",
                      machine_claim="LV19A-06", **HC)]
        if q == "unclaimed_wage_violation":
            return [V("no_claim_no_violation",
                      "only if he claimed — unclaimed, no violation",
                      authority="Mishnah Bava Metzia 9:12",
                      machine_claim="LV19A-06", **HC),
                    V("shopkeeper_assignment_clears",
                      "assigned to the shopkeeper or money-changer "
                      "— the employer clear",
                      authority="Mishnah Bava Metzia 9:12",
                      machine_claim="LV19A-06", **HC)]
        if q == "lender_stumbling_block":
            return [V("lifnei_iver_in_the_interest_list",
                      "the interest parties transgress — the lender "
                      "also under 'before the blind put no "
                      "stumbling block': the blind-in-the-matter "
                      "rule in finance",
                      authority="Mishnah Bava Metzia 5:11",
                      machine_claim="LV19A-07", **HC)]
        if q == "wage_paid_in_kind_refused":
            return [V("not_heeded_wage_stands",
                      "'take what you made as your wage' — not "
                      "heeded: the wage clause enforced",
                      authority="Mishnah Bava Metzia 10:5",
                      machine_claim="LV19A-06", **HC)]
        if q == "five_fifths_census":
            return [V("fourth_year_redeemer_among_them",
                      "the five fifths — the fourth-year redeemer "
                      "listed: the seat's fifth in the fractions "
                      "census",
                      authority="Mishnah Bava Metzia 4:8",
                      machine_claim="LV19B-03", **HC)]
        if q == "oath_by_substitute_names":
            return [V("all_names_bind",
                      "oaths by Alef-Dalet, Yod-He, Shaddai, "
                      "Tzevaot, the gracious-and-merciful — all "
                      "bind: 'every name I have'",
                      authority="Mishnah Shevuot 4:13",
                      machine_claim="LV19A-05", **HC),
                    V("curse_by_them_disputed",
                      "cursing (and the parents' curse) by them — "
                      "R. Meir liable, the Sages exempt",
                      authority="R. Meir vs the Sages — Mishnah "
                                "Shevuot 4:13",
                      machine_claim="LV20-03", **HC)]
        if q == "amulet_conduct_class":
            return [V("ways_of_the_amorite",
                      "the locust egg, fox tooth, crucifixion nail "
                      "— banned as the ways of the Amorite: the "
                      "register census applied",
                      authority="the Sages — Mishnah Shabbat 6:10",
                      machine_claim="LV18-01", **HC)]
        if q == "women_and_the_razor_bans":
            return [V("excepted_from_the_exemption",
                      "women bound by all negatives — and the three "
                      "named exceptions are our clauses: the "
                      "corners, the beard, the priestly defilement",
                      authority="Mishnah Kiddushin 1:7",
                      machine_claim="LV19B-06", **HC)]
        if q == "father_mother_precedence":
            return [V("both_equal_father_precedes_in_practice",
                      "'a man his MOTHER and father shall fear' — "
                      "both equal; the father precedes because he "
                      "and his mother owe the father's honor — the "
                      "Sifra's rows verbatim with the teacher "
                      "extension",
                      authority="Mishnah Keritot 6:9",
                      machine_claim="LV19A-02", **HC)]
        if q == "deliberate_as_error_census":
            return [V("maidservant_heads_the_four",
                      "the four who bring on the deliberate as the "
                      "erring — the designated maidservant first",
                      authority="Mishnah Keritot 2:2",
                      machine_claim="LV19B-02", **HC)]
        if q == "who_is_the_maidservant":
            return [V("akiva_half_free",
                      "half-slave-half-free — 'redeemed and not "
                      "redeemed'",
                      authority="R. Akiva — Mishnah Keritot 2:5",
                      machine_claim="LV19B-02", **HC),
                    V("yishmael_certain_maidservant",
                      "a certain maidservant",
                      authority="R. Yishmael — Mishnah Keritot 2:5",
                      machine_claim="LV19B-02", **HC),
                    V("elazar_only_case_left",
                      "all unions are stated — what remains? only "
                      "she",
                      authority="R. Elazar ben Azariah — Mishnah "
                                "Keritot 2:5",
                      machine_claim="LV19B-02", **HC)]
        if q == "carcass_eater_lashes":
            return [V("in_the_forty_list",
                      "the carcass-and-torn eater in the lashes "
                      "census — the garment-arm's forty generalized",
                      authority="Mishnah Makkot 3:2",
                      machine_claim="LV17-08", **HC)]
        if q == "gash_and_corner_multipliers":
            return [V("per_gash_per_dead",
                      "one gash on five dead, five gashes on one — "
                      "liable per each; head two, beard two-two-one",
                      authority="Mishnah Makkot 3:5",
                      machine_claim="LV19B-06", **HC),
                    V("r_eliezer_all_at_once_one",
                      "R. Eliezer: taken all at once — one; and his "
                      "tweezers-and-plane arm kept",
                      authority="R. Eliezer — Mishnah Makkot 3:5",
                      machine_claim="LV19B-06", **HC)]
        if q == "tattoo_partial_acts":
            return [V("write_and_engrave_both",
                      "wrote without engraving or engraved without "
                      "writing — exempt: both required, any marking "
                      "pigment",
                      authority="Mishnah Makkot 3:6",
                      machine_claim="LV19B-06", **HC),
                    V("shimon_ben_yehuda_the_name",
                      "R. Shimon ben Yehuda in R. Shimon's name: "
                      "only when he writes the Name — 'I am the "
                      "LORD'",
                      authority="R. Shimon ben Yehuda — Mishnah "
                                "Makkot 3:6",
                      machine_claim="LV19B-06", **HC)]
        if q == "repeat_warning_multiplier":
            return [V("per_warning_liability",
                      "all day one liability; warned each time — "
                      "liable per warning: the third multiplier "
                      "beside per-gash and per-dead",
                      authority="Mishnah Makkot 3:8",
                      machine_claim="LV19B-06", **HC)]
        if q == "one_furrow_ban_count":
            return [V("eight_bans_on_one_furrow",
                      "one furrow, eight bans — ox-and-donkey "
                      "consecrated, the vineyard mixture, the "
                      "seventh year, the festival, priest and "
                      "nazirite in impurity; Chananya ben "
                      "Chachinai's mixture-wearer arm argued",
                      authority="Mishnah Makkot 3:9",
                      machine_claim="LV19B-01", **HC)]
        if q == "flogging_reader_verses":
            return [V("procedure_row_kept",
                      "the reader's verses and the accident "
                      "exemptions — the procedure row beside the "
                      "forty",
                      authority="Mishnah Makkot 3:14",
                      machine_claim="LV17-08", **HC)]
        if q == "ox_or_donkey_scope":
            return [V("scripture_spoke_the_common_case",
                      "ox and donkey named, all beasts meant — 'the "
                      "Scripture spoke of the common case': the "
                      "register meta-rule's twin across pit, Sinai, "
                      "double payment, the mixture, the Sabbath",
                      authority="Mishnah Bava Kamma 5:7",
                      machine_claim="LV20-01", **HC)]
        if q == "maidservant_asham_in_table":
            return [V("north_slaughter_two_gifts_four",
                      "the maidservant's guilt offering in the "
                      "census — north slaughter, service-vessel "
                      "reception, two gifts that are four, eaten "
                      "within the hangings by priestly males",
                      authority="Mishnah Zevachim 5:5",
                      machine_claim="LV19B-02", **HC)]
        return None

    def rule_poor_gifts_orlah_file(case):
        q = case.get("query")
        if q == "basket_under_the_vine":
            return [V("robbing_the_poor",
                      "the basket under the vine at cutting time — "
                      "robbing the poor: 'move not the boundary' — "
                      "the Sifra's row verbatim, peret defined by "
                      "the cutting",
                      authority="Mishnah Peah 7:3",
                      machine_claim="LV19A-04", **PG)]
        if q == "fourth_year_vineyard_houses":
            return [V("shammai_poor_redeem_own",
                      "Beit Shammai — no fifth, no removal; the "
                      "poor redeem their own fallen grapes and "
                      "small clusters",
                      authority="Beit Shammai — Mishnah Peah 7:6",
                      machine_claim="LV19B-03", **PG),
                    V("hillel_all_to_the_press",
                      "Beit Hillel — all to the press; fifth and "
                      "removal apply",
                      authority="Beit Hillel — Mishnah Peah 7:6",
                      machine_claim="LV19B-03", **PG)]
        if q == "all_small_clusters_vineyard":
            return [V("r_eliezer_owner",
                      "the all-defective vineyard — the owner's "
                      "('if there is no harvest, whence small "
                      "clusters?')",
                      authority="R. Eliezer — Mishnah Peah 7:7",
                      machine_claim="LV19A-04", **PG),
                    V("r_akiva_poor",
                      "R. Akiva — the poor's ('your vineyard you "
                      "shall not glean-small' even all-small), with "
                      "the no-claim-before-harvest timing rule",
                      authority="R. Akiva — Mishnah Peah 7:7",
                      machine_claim="LV19A-04", **PG)]
        if q == "renunciation_to_poor_only":
            return [V("shammai_valid",
                      "renounced for the poor alone — renounced",
                      authority="Beit Shammai — Mishnah Eduyot 4:3",
                      machine_claim="LV19A-04", **PG),
                    V("hillel_needs_rich_too",
                      "not renounced until for the rich too, as "
                      "the seventh year",
                      authority="Beit Hillel — Mishnah Eduyot 4:3",
                      machine_claim="LV19A-04", **PG)]
        if q == "fourth_year_in_leniency_list":
            return [V("registered_house_dispute",
                      "the fourth-year vineyard row standing in "
                      "Eduyot's registry — the record row",
                      authority="Mishnah Eduyot 4:5",
                      machine_claim="LV19B-03", **PG)]
        if q == "peah_tithe_implication":
            return [V("peah_implies_tithes_not_converse",
                      "whatever owes the corner owes the tithes; "
                      "some owe tithes and not the corner — the "
                      "five-predicate classifier nested against "
                      "the tithe class",
                      authority="Mishnah Niddah 6:6",
                      machine_claim="LV19A-04", **PG)]
        if q == "gentile_fourth_year":
            return [V("r_yehuda_none",
                      "the gentile has no fourth-year vineyard",
                      authority="R. Yehuda — Mishnah Terumot 3:9",
                      machine_claim="LV19B-03", **PG),
                    V("sages_he_has_it",
                      "the Sages: he has it — the scope dispute "
                      "recorded",
                      authority="the Sages — Mishnah Terumot 3:9",
                      machine_claim="LV19B-03", **PG)]
        if q == "orlah_lashes_on_juice":
            return [V("olive_grape_outflow_only",
                      "the forty for orlah only on what flows from "
                      "olives and grapes — the total ban bounded "
                      "at the press",
                      authority="Mishnah Terumot 11:3",
                      machine_claim="LV19B-03", **PG)]
        if q == "orlah_kilayim_combination":
            return [V("they_combine",
                      "orlah and the vineyard mixture combine to "
                      "one measure",
                      authority="Mishnah Meilah 4:6",
                      machine_claim="LV19B-03", **PG),
                    V("r_shimon_splits",
                      "R. Shimon: they do not combine",
                      authority="R. Shimon — Mishnah Meilah 4:6",
                      machine_claim="LV19B-03", **PG)]
        if q == "sukkah_covering_class":
            return [V("no_impurity_and_land_grown",
                      "covers only with what receives no impurity "
                      "AND grows from the land — the grows-plants "
                      "predicate standing as the sukkah's own "
                      "classifier: one class rule at two machines",
                      authority="Mishnah Sukkah 1:4",
                      machine_claim="LV17-07", **PG)]
        return None

    return {
        "yoma_service_file": {"fn": rule_yoma_service_file,
                              "tractate": "Yoma"},
        "yk_atonement_file": {"fn": rule_yk_atonement_file,
                              "tractate": "Shevuot"},
        "outside_slaughter_file": {"fn": rule_outside_slaughter_file,
                                   "tractate": "Zevachim"},
        "arayot_sanctions_file": {"fn": rule_arayot_sanctions_file,
                                  "tractate": "Sanhedrin"},
        "levirate_file": {"fn": rule_levirate_file,
                          "tractate": "Yevamot"},
        "holiness_conduct_file": {"fn": rule_holiness_conduct_file,
                                  "tractate": "Bava Metzia"},
        "poor_gifts_orlah_file": {"fn": rule_poor_gifts_orlah_file,
                                  "tractate": "Peah"},
    }
