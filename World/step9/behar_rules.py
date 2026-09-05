# behar_rules.py — round 46, THE BEHAR-BECHUKOTAI EXAM (2026-09-05,
# Leviticus's last round). Bare Mishnah rows citing Lev 25-27, graded
# after the derivation. Read-source:
# logic/oral_triage/behar_exam_mishnah_2026-09-05.md. Seven modules,
# 88 cells over 47 LAW rows; every dispute returned whole with its
# arms labeled.


def build(V):
    def _EX(mishnah, anchor, **extra):
        d = dict(talmud_source=mishnah, exodus_anchor=anchor)
        d.update(extra)
        return d

    SH = _EX("Mishnah Makkot 3:9; Rosh Hashanah 1:8; Sanhedrin 3:3; Shevuot "
             "7:4; Rosh Hashanah 3:2; 4:9",
             "Lev 25:1-22 (lev_25_shemittah, LV25A claims — the land's "
             "sabbath and the Jubilee)")
    ON = _EX("Mishnah Bava Metzia 4:3; 4:9; 4:10; Arakhin 9:1",
             "Lev 25:14-17 (lev_25_shemittah, LV25A-14..16)")
    GE = _EX("Mishnah Arakhin 9:2; 9:3; 9:4; 9:7; 9:8; Shekalim 4:9",
             "Lev 25:23-34 (lev_25_redeem_poor, LV25B claims)")
    RI = _EX("Mishnah Bava Metzia 5:1; 5:11; Nedarim 9:4; Bava Metzia 1:5; "
             "Kiddushin 1:3; 1:5; Makkot 2:8",
             "Lev 25:35-55 (lev_25_redeem_poor LV25B-14 + lev_25_slave_jubilee "
             "LV25C claims)")
    CV = _EX("Mishnah Megillah 3:3; 3:6; Taanit 3:5",
             "Lev 26 (lev_26_bless_curse, LV26 claims)")
    ER = _EX("Mishnah Arakhin 1:1; 3:1; 3:2; 4:1; 4:4; 7:1; 7:5; Megillah 4:3; "
             "Sanhedrin 1:3; Bekhorot 1:7; Bava Metzia 4:8",
             "Lev 27:1-25 (lev_27_vows_valuations, LV27-01..19)")
    TM = _EX("Mishnah Temurah 1:1; 1:2; 1:6; Arakhin 8:5; 8:6; 8:7; Challah "
             "4:9; Bekhorot 9:1; 9:7; Nazir 5:3",
             "Lev 27:9-34 (lev_27_vows_valuations, LV27-04..05, 18, 20, 23, 24)")

    def one(verdict, basis, prov, claim, authority=None):
        return [V(verdict, basis, authority=authority,
                  machine_claim=claim, **prov)]

    def many(prov, claim, *arms):
        return [V(v, b, authority=a, machine_claim=claim, **prov)
                for v, b, a in arms]

    # ------------------------------------------------ shemittah_land_file
    def rule_shemittah_land_file(case):
        q = case.get("query")
        if q == "shemittah_plowing_in_seventh":
            return one("banned_field_labor",
                       "plowing among the census from 'your field NOT' "
                       "(LV25A-04, Sifra Behar Section 1 4)", SH, "LV25A-04",
                       "Mishnah Makkot 3:9")
        if q == "shemittah_produce_trader_witness":
            return one("disqualified",
                       "'for eating' — not for commerce (LV25A-05, Sifra "
                       "Behar Chapter 1 6); the trader's witness barred", SH,
                       "LV25A-05", "Mishnah Rosh Hashanah 1:8")
        if q == "shemittah_trader_with_other_craft":
            return one("r_yehuda_fit",
                       "R. Yehuda: only when it is his sole trade (Sanhedrin "
                       "3:3) — the eating-not-commerce rule's recorded "
                       "qualifier (LV25A-05)", SH, "LV25A-05",
                       "R. Yehuda, Mishnah Sanhedrin 3:3")
        if q == "yovel_shofar_of_a_cow":
            return one("invalid_it_is_a_horn",
                       "the Jubilee's instrument is a shofar (LV25A-09, Sifra "
                       "Behar Section 2 3); the cow's is a horn — R. Yosei's "
                       "objection from 'the horn of the Jubilee' recorded", SH,
                       "LV25A-09", "Mishnah Rosh Hashanah 3:2")
        if q == "yovel_blast_order":
            return one("plain_broken_plain_three_times",
                       "a plain blast before and after the broken one "
                       "(LV25A-09, Sifra Behar Section 2 4)", SH, "LV25A-09",
                       "Mishnah Rosh Hashanah 4:9")
        if q == "yovel_blast_obligation_scope":
            return one("every_individual",
                       "'throughout your land' — every individual obligated "
                       "(LV25A-09, Sifra Behar Section 2 5, VERBATIM)", SH,
                       "LV25A-09", "Mishnah Rosh Hashanah 4:9")
        return None

    # ------------------------------------------------ overreaching_file
    def rule_overreaching_file(case):
        q = case.get("query")
        if q == "onaah_measure":
            return one("sixth_of_purchase",
                       "four silver of twenty-four to the sela (LV25A-14, "
                       "Sifra Behar Section 3 5, VERBATIM)", ON, "LV25A-14",
                       "Mishnah Bava Metzia 4:3")
        if q == "onaah_return_window":
            return one("until_shown_to_merchant_or_kinsman",
                       "the window until shown to a merchant or expert "
                       "(LV25A-14, Sifra Behar Section 3 5)", ON, "LV25A-14",
                       "Mishnah Bava Metzia 4:3")
        if q == "onaah_r_tarfon_at_lod":
            return one("third_then_reverted",
                       "R. Tarfon's third at Lod, recanted the same day "
                       "(LV25A-14, Sifra Behar Section 3 5)", ON, "LV25A-14",
                       "Mishnah Bava Metzia 4:3")
        if q == "onaah_slaves_documents_land_hekdesh":
            return one("no_overreaching",
                       "land by 'from the hand', slaves by the holding, "
                       "documents by 'sale', consecrated by 'his brother' "
                       "(LV25A-14, Sifra Behar Section 3 1-3)", ON, "LV25A-14",
                       "Mishnah Bava Metzia 4:9")
        if q in ("onaah_asking_price_without_buying",
                 "onaah_reminding_penitent"):
            return one("verbal_wronging",
                       "25:17's verbal wronging — the price without intent, "
                       "the penitent's past (LV25A-16, Sifra Behar Chapter 4 "
                       "2, VERBATIM)", ON, "LV25A-16",
                       "Mishnah Bava Metzia 4:10")
        if q == "geulah_field_sold_in_jubilee_year":
            return one("not_redeemed_under_two_years",
                       "'by the number of harvest years' — the two-year floor "
                       "(LV25A-15, Sifra Behar Section 3 10)", ON, "LV25A-15",
                       "Mishnah Arakhin 9:1")
        if q == "geulah_blight_year_count":
            return one("not_counted",
                       "blight, mildew, the seventh — not produce years "
                       "(LV25A-15)", ON, "LV25A-15", "Mishnah Arakhin 9:1")
        if q == "geulah_three_harvests_two_years":
            return one("r_elazar_allowed",
                       "sold before the New Year full of fruit — three "
                       "harvests in two years (LV25A-15, R. Elazar)", ON,
                       "LV25A-15", "R. Elazar, Mishnah Arakhin 9:1")
        return None

    # ------------------------------------------------ land_redemption_file
    def rule_land_redemption_file(case):
        q = case.get("query")
        if q == "geulah_resold_dearer":
            return one("reckon_with_first",
                       "'to whom he sold' — the first, the cheaper price "
                       "(LV25B-05, Sifra Behar Chapter 5 3)", GE, "LV25B-05",
                       "Mishnah Arakhin 9:2")
        if q == "geulah_resold_cheaper":
            return one("reckon_with_last",
                       "'to the MAN in it' — the last, the cheaper price "
                       "(LV25B-05, Rabbi)", GE, "LV25B-05",
                       "Mishnah Arakhin 9:2")
        if q == "geulah_layman_borrow_or_halves":
            return one("forbidden",
                       "'and finds', 'sufficient' — no borrowing, no halves "
                       "(LV25B-04, Sifra Behar Chapter 5 2)", GE, "LV25B-04",
                       "Mishnah Arakhin 9:2")
        if q == "geulah_hekdesh_borrow_or_halves":
            return one("permitted",
                       "'in the buyer's hand' — not the sanctuary's: the four "
                       "constraints inverted (LV25B-06, Sifra Behar Chapter 5 "
                       "6)", GE, "LV25B-06", "Mishnah Arakhin 9:2")
        if q == "walled_city_house_redemption_window":
            return one("at_once_through_twelve_months",
                       "'its redemption shall be' — at once; 'until the end "
                       "of the year' (LV25B-07, Sifra Behar Section 4 2)", GE,
                       "LV25B-07", "Mishnah Arakhin 9:3")
        if q == "walled_city_year_count_start":
            return one("from_the_sale",
                       "'until a full year is completed FOR HIM' — from the "
                       "first sale (LV25B-07, Sifra Behar Section 4 3)", GE,
                       "LV25B-07", "Mishnah Arakhin 9:3")
        if q == "walled_city_intercalated_year":
            return one("intercalated_for_the_seller",
                       "'a full year' — twelve months day for day, the "
                       "intercalation his (LV25B-08, Sifra Behar Section 4 4, "
                       "the Sages; Rabbi's year-and-its-intercalation "
                       "recorded)", GE, "LV25B-08", "Mishnah Arakhin 9:3")
        if q == "walled_city_buyer_hides":
            return one("hillel_deposit_in_chamber",
                       "Hillel's ordinance against the hiding buyer "
                       "(LV25B-08, Sifra Behar Section 4 8, VERBATIM)", GE,
                       "LV25B-08", "Mishnah Arakhin 9:4")
        if q == "walled_city_house_given_as_gift":
            return one("irrevocable_after_year",
                       "'in perpetuity' includes the gift recipient "
                       "(LV25B-08, Sifra Behar Section 4 8)", GE, "LV25B-08",
                       "Mishnah Arakhin 9:4")
        if q == "village_house_status":
            return one("best_of_both",
                       "at once like the house, Jubilee and deduction like "
                       "the field (LV25B-09, Sifra Behar Chapter 6 2-3)", GE,
                       "LV25B-09", "Mishnah Arakhin 9:7")
        if q == "village_house_definition":
            return one("two_courtyards_of_two_houses",
                       "'houses' two, 'villages' two (LV25B-09, Sifra Behar "
                       "Chapter 6 1)", GE, "LV25B-09", "Mishnah Arakhin 9:7")
        if q == "israelite_heir_of_levite_grandfather":
            return one("not_by_levite_order",
                       "'what one redeems FROM THE LEVITES' — until he is a "
                       "Levite (LV25B-11, Sifra Behar Chapter 6 8, Rabbi; the "
                       "Sages' cities-only arm recorded)", GE, "LV25B-11",
                       "Mishnah Arakhin 9:8")
        if q == "levite_city_field_to_pasture":
            return one("forbidden",
                       "the zoning rule in the Levites' cities (LV25B-12, "
                       "Sifra Behar Chapter 6 9)", GE, "LV25B-12",
                       "Mishnah Arakhin 9:8")
        if q == "israel_city_field_to_pasture":
            return one("permitted_upward_only",
                       "R. Eliezer: in Israel's cities field to pasture and "
                       "pasture to city, never the reverse (LV25B-12)", GE,
                       "LV25B-12", "R. Eliezer, Mishnah Arakhin 9:8")
        if q == "hekdesh_supplier_price_moved":
            return one("sanctuary_hand_on_top",
                       "the sanctuary-favoring asymmetry — what the layman "
                       "may not, the sanctuary may (LV25B-06; LV27-12 the "
                       "sanctuary reckons months)", GE, "LV25B-06",
                       "Mishnah Shekalim 4:9")
        return None

    # ------------------------------------------------ interest_and_slaves_file
    def rule_interest_and_slaves_file(case):
        q = case.get("query")
        if q == "ribbit_sela_for_five_dinars":
            return one("neshekh",
                       "the bite defined by the worked case (LV25B-14, Sifra "
                       "Behar Section 5 2, VERBATIM)", RI, "LV25B-14",
                       "Mishnah Bava Metzia 5:1")
        if q == "ribbit_wheat_price_rise_wine":
            return one("tarbit",
                       "the increase defined by the wheat-for-wine case "
                       "(LV25B-14, Sifra Behar Section 5 2, VERBATIM)", RI,
                       "LV25B-14", "Mishnah Bava Metzia 5:1")
        if q == "ribbit_who_transgresses":
            return one("lender_borrower_guarantor_witnesses",
                       "'do not give' (25:37), 'do not take from him' "
                       "(25:36) — the addressee list; the Sifra's permitted "
                       "guarantor is surety toward a third party (LV25B-14)",
                       RI, "LV25B-14", "Mishnah Bava Metzia 5:11")
        if q == "ribbit_scribe_liability":
            return one("sages_scribe_too",
                       "the Sages add the scribe (LV25B-14)", RI, "LV25B-14",
                       "the Sages, Mishnah Bava Metzia 5:11")
        if q == "neder_opening_by_brother_live_with_you":
            return one("vow_released",
                       "'that your brother live with you' as a vow's opening "
                       "(LV25B-14, R. Meir)", RI, "LV25B-14",
                       "R. Meir, Mishnah Nedarim 9:4")
        if q == "hebrew_slave_find":
            return one("belongs_to_slave",
                       "the Hebrew slave is a hireling — a hireling's finds "
                       "are his own (LV25C-02, Sifra Behar Chapter 7 3)", RI,
                       "LV25C-02", "Mishnah Bava Metzia 1:5")
        if q == "canaanite_slave_find":
            return one("belongs_to_master",
                       "the Canaanite slave is a holding (LV25C-08, Sifra "
                       "Behar Section 6 5-6)", RI, "LV25C-08",
                       "Mishnah Bava Metzia 1:5")
        if q == "canaanite_slave_acquisition":
            return one("money_deed_possession",
                       "'a holding for you' — as land, so slaves (LV25C-07, "
                       "Sifra Behar Section 6 4, VERBATIM)", RI, "LV25C-07",
                       "Mishnah Kiddushin 1:3")
        if q == "land_acquisition_modes":
            return one("money_deed_possession",
                       "the land's three modes — the premise LV25C-07 imports "
                       "to the slave", RI, "LV25C-07", "Mishnah Kiddushin 1:5")
        if q == "exile_returns_to_office":
            return many(RI, "LV25C-03",
                        ("r_meir_returns", "to what his family held (Sifra "
                         "Behar Chapter 7 4)", "R. Meir, Mishnah Makkot 2:8"),
                        ("r_yehuda_does_not", "not to his former office — "
                         "and so the exile (Sifra Behar Chapter 7 4)",
                         "R. Yehuda, Mishnah Makkot 2:8"))
        return None

    # ------------------------------------------------ covenant_curses_file
    def rule_covenant_curses_file(case):
        q = case.get("query")
        if q == "ruined_synagogue_sanctity":
            return one("remains_holy",
                       "'I will desolate your sanctuaries' — synagogues in "
                       "the doubled token, holy even desolate (LV26-20, "
                       "Sifra Bechukotai Chapter 6 4, VERBATIM)", CV,
                       "LV26-20", "Mishnah Megillah 3:3")
        if q == "tochacha_reading_interruption":
            return one("one_reader_whole",
                       "the Mishnah's own ordinance on the chapter's text — "
                       "no Sifra seat; read as one sequence beside LV26-13's "
                       "descent", CV, "none (answer sheet)",
                       "Mishnah Megillah 3:6")
        if q == "fast_day_torah_reading":
            return one("blessings_and_curses",
                       "the fast-day reading is Lev 26 (Mishnah Megillah "
                       "3:6; the chapter as LV26-03..29)", CV,
                       "none (answer sheet)", "Mishnah Megillah 3:6")
        if q == "alarm_for_evil_beast":
            return one("sound_alarm_everywhere",
                       "the evil beast of 26:6 — a spreading plague "
                       "(LV26-06)", CV, "LV26-06", "Mishnah Taanit 3:5")
        if q == "alarm_for_passing_army":
            return one("sound_alarm_everywhere",
                       "'no sword shall pass' = no armies in transit "
                       "(LV26-06, Sifra Bechukotai Chapter 2 3; Onkelos "
                       "26:6) — the alarm sounds for the passing army", CV,
                       "LV26-06", "Mishnah Taanit 3:5")
        return None

    # ------------------------------------------------ valuations_file
    def rule_valuations_file(case):
        q = case.get("query")
        if q == "erech_tumtum_androgynos":
            return one("vow_and_value_not_valued",
                       "'male'... 'if a female' — certain sexes only; they "
                       "value (R. Yehuda's width) (LV27-01, LV27-02, Sifra "
                       "Bechukotai Section 3 2, 9, VERBATIM)", ER, "LV27-01",
                       "Mishnah Arakhin 1:1")
        if q == "erech_deaf_mute_imbecile_minor":
            return one("valued_not_valuing",
                       "R. Meir's width — valued but not valuing (LV27-01, "
                       "Sifra Bechukotai Section 3 1)", ER, "LV27-01",
                       "Mishnah Arakhin 1:1")
        if q == "erech_under_a_month":
            return one("vowed_not_valued",
                       "'and it shall be' — in worth, out of valuation "
                       "(LV27-02, Sifra Bechukotai Section 3 8)", ER,
                       "LV27-02", "Mishnah Arakhin 1:1")
        if q == "erech_handsome_vs_ugly":
            return one("fifty_selas_each",
                       "the fixed sums — the whole, not limbs, not worth "
                       "(LV27-02)", ER, "LV27-02", "Mishnah Arakhin 3:1")
        if q == "erech_worth_vow":
            return one("his_worth",
                       "the worth class beside the valuation class "
                       "(LV27-02, Sifra Bechukotai Section 3 7-8)", ER,
                       "LV27-02", "Mishnah Arakhin 3:1")
        if q == "erech_field_sandy_vs_orchard":
            return one("fifty_per_homer_seed",
                       "THE KING'S DECREE (LV27-10, Sifra Bechukotai Chapter "
                       "10 3, VERBATIM)", ER, "LV27-10", "Mishnah Arakhin 3:2")
        if q == "erech_purchased_field_rate":
            return many(ER, "LV27-16",
                        ("sages_its_worth", "'the measure' — its worth "
                         "(Sifra Bechukotai Chapter 11 4)",
                         "the Sages, Mishnah Arakhin 3:2"),
                        ("r_eliezer_fifty_per_homer", "'reckon'-'reckon' — "
                         "fifty per homer here too (Sifra Bechukotai Chapter "
                         "11 5)", "R. Eliezer, Mishnah Arakhin 3:2"))
        if q == "erech_poor_values_rich":
            return one("poor_valuation",
                       "MEANS BY THE VOWER (LV27-03, Sifra Bechukotai Section "
                       "3 14, VERBATIM)", ER, "LV27-03", "Mishnah Arakhin 4:1")
        if q == "erech_child_values_old":
            return one("old_valuation",
                       "YEARS BY THE VALUED (LV27-03)", ER, "LV27-03",
                       "Mishnah Arakhin 4:4")
        if q == "erech_man_values_woman":
            return one("woman_valuation",
                       "VALUATIONS BY THE VALUED (LV27-03)", ER, "LV27-03",
                       "Mishnah Arakhin 4:4")
        if q == "erech_age_crossed_before_payment":
            return one("at_valuation_time",
                       "THE VALUATION AT ITS TIME (LV27-03)", ER, "LV27-03",
                       "Mishnah Arakhin 4:4")
        if q == "erech_year_five_or_twenty_boundary":
            return many(ER, "LV27-02",
                        ("sages_counts_below", "'year'-'year' from the "
                         "sixtieth (Sifra Bechukotai Section 3 9-11)",
                         "the Sages, Mishnah Arakhin 4:4"),
                        ("r_elazar_month_and_day_past", "'and upward' — a "
                         "month and a day (Sifra Bechukotai Section 3 11-12)",
                         "R. Elazar, Mishnah Arakhin 4:4"))
        if q == "erech_field_consecrated_near_jubilee":
            return one("not_less_than_two_years_before",
                       "the two-year floor before, one after (LV27-12, Sifra "
                       "Bechukotai Chapter 10 7, VERBATIM)", ER, "LV27-12",
                       "Mishnah Arakhin 7:1")
        if q == "erech_months_reckoned":
            return one("sanctuary_may_layman_not",
                       "months not reckoned against the sanctuary; the "
                       "sanctuary may (LV27-12, Sifra Bechukotai Chapter 10 "
                       "8, 10)", ER, "LV27-12", "Mishnah Arakhin 7:1")
        if q == "erech_field_crevices_ten_handbreadths":
            return one("not_measured",
                       "'his field' — crevices and rocks of ten excluded "
                       "(LV27-11, Sifra Bechukotai Chapter 10 4, 6)", ER,
                       "LV27-11", "Mishnah Arakhin 7:1")
        if q == "erech_field_per_year_rate":
            return one("sela_and_pundion",
                       "forty-nine and forty-nine — a sela and a pundion per "
                       "year (LV27-11, Sifra Bechukotai Chapter 10 5, 10)",
                       ER, "LV27-11", "Mishnah Arakhin 7:1")
        if q == "erech_field_pay_yearly":
            return one("refused_lump_sum",
                       "'year by year' not heard — all at once (LV27-12, "
                       "Sifra Bechukotai Chapter 10 9)", ER, "LV27-12",
                       "Mishnah Arakhin 7:1")
        if q == "erech_field_bought_father_died_then_consecrated":
            return one("holding_field",
                       "the father's death before consecration makes it a "
                       "holding (LV27-16, Sifra Bechukotai Chapter 11 4)", ER,
                       "LV27-16", "Mishnah Arakhin 7:5")
        if q == "erech_field_consecrated_then_father_died":
            return many(ER, "LV27-16",
                        ("r_meir_purchased_field", "a field that is not a "
                         "holding (Sifra Bechukotai Chapter 11 4)",
                         "R. Meir, Mishnah Arakhin 7:5"),
                        ("r_yehuda_r_shimon_holding_field", "fit to become "
                         "a holding — a holding (Sifra Bechukotai Chapter 11 "
                         "4)", "R. Yehuda and R. Shimon, Mishnah Arakhin 7:5"))
        if q == "erech_priests_levites_consecrate_redeem":
            return one("always",
                       "'perpetual redemption for the Levites' (LV25B-10, "
                       "Sifra Behar Chapter 6 4-5)", ER, "LV25B-10",
                       "Mishnah Arakhin 7:5")
        if q == "erech_land_assessors":
            return one("nine_and_a_priest",
                       "'the priest shall value' — the archetype (LV27-03); "
                       "the count of ten from the chapter's priest tokens is "
                       "the Talmud's census (Sanhedrin 15a), left to the "
                       "compile", ER, "LV27-03", "Mishnah Megillah 4:3")
        if q == "erech_movable_assessors":
            return one("three",
                       "movable valuations by three; R. Yehuda: one a priest "
                       "(LV27-07)", ER, "LV27-07", "Mishnah Sanhedrin 1:3")
        if q == "hekdesh_redemption_owner_precedence":
            return one("owner_first",
                       "'not redeemed' — by the owner; 'sold' — to anyone "
                       "(LV27-19); the owner's precedence (LV27-09)", ER,
                       "LV27-19", "Mishnah Bekhorot 1:7")
        if q == "hekdesh_redeemer_adds_fifth":
            return one("owner_adds_fifth",
                       "the owner adds, others do not (LV27-08, Sifra "
                       "Bechukotai Section 4 7)", ER, "LV27-08",
                       "Mishnah Bava Metzia 4:8")
        return None

    # ------------------------------------------------ temurah_herem_tithe_file
    def rule_temurah_herem_tithe_file(case):
        q = case.get("query")
        if q == "temurah_who_substitutes":
            return one("all_men_and_women",
                       "'if he substitutes' — the woman, the heir (LV27-05, "
                       "Sifra Bechukotai Chapter 9 6, VERBATIM)", TM,
                       "LV27-05", "Mishnah Temurah 1:1")
        if q == "temurah_penalty":
            return one("holds_and_lashes",
                       "'it and its substitute shall be holy' — holds; "
                       "lashes (LV27-24, Sifra Bechukotai Chapter 13 4)", TM,
                       "LV27-24", "Mishnah Temurah 1:1")
        if q == "temurah_priest_substitutes_firstborn":
            return one("not",
                       "holiness falls in the owner's house — R. Akiva's "
                       "verse against R. Yochanan b. Nuri's argument "
                       "(LV27-05, Sifra Bechukotai Chapter 9 10-12)", TM,
                       "LV27-05", "Mishnah Temurah 1:1")
        if q == "temurah_cattle_for_flock":
            return one("valid",
                       "'beast for beast' — kinds within the beast class "
                       "(LV27-05, Sifra Bechukotai Chapter 9 6)", TM,
                       "LV27-05", "Mishnah Temurah 1:2")
        if q == "temurah_whole_for_blemished":
            return one("valid",
                       "'good for bad' = whole for blemished (LV27-05)", TM,
                       "LV27-05", "Mishnah Temurah 1:2")
        if q == "temurah_one_for_a_hundred":
            return many(TM, "LV27-05",
                        ("sages_valid", "'beast for beast' — many beasts are "
                         "'beast' (Sifra Bechukotai Chapter 9 6)",
                         "the Sages, Mishnah Temurah 1:2"),
                        ("r_shimon_one_for_one", "'beast for beast' not "
                         "'beasts' (Sifra Bechukotai Chapter 9 6)",
                         "R. Shimon, Mishnah Temurah 1:2"))
        if q == "temurah_birds_meal_offerings":
            return one("no_substitution",
                       "'beast' — not birds, not meal offerings (LV27-05, "
                       "Sifra Bechukotai Chapter 9 7)", TM, "LV27-05",
                       "Mishnah Temurah 1:6")
        if q == "temurah_public_or_partners":
            return one("no_substitution",
                       "'he shall not substitute IT' — the individual alone "
                       "(LV27-04, Sifra Bechukotai Chapter 9 3)", TM,
                       "LV27-04", "Mishnah Temurah 1:6")
        if q == "temurah_temple_upkeep":
            return one("no_substitution",
                       "'offering' excludes upkeep (LV27-04, Sifra Bechukotai "
                       "Chapter 9 2)", TM, "LV27-04", "Mishnah Temurah 1:6")
        if q == "herem_son_or_hebrew_slave_or_purchased_field":
            return one("not_devoted",
                       "'of all he has' — only his own; 'of man' — Canaanite "
                       "slaves, not Hebrew (LV27-20, Sifra Bechukotai Chapter "
                       "12 3, VERBATIM)", TM, "LV27-20", "Mishnah Arakhin 8:5")
        if q == "herem_by_priests_levites":
            return many(TM, "LV27-20",
                        ("r_yehuda_neither", "'but' (Sifra Bechukotai "
                         "Chapter 12 6)", "R. Yehuda, Mishnah Arakhin 8:5"),
                        ("r_shimon_levites_only", "devotions are the "
                         "priests' (Sifra Bechukotai Chapter 12 6)",
                         "R. Shimon, Mishnah Arakhin 8:5"),
                        ("rabbi_land_vs_movables", "R. Yehuda for land, R. "
                         "Shimon for movables (Sifra Bechukotai Chapter 12 6)",
                         "Rabbi, Mishnah Arakhin 8:5"))
        if q == "herem_unspecified_destination":
            return many(TM, "LV27-20",
                        ("r_yehuda_b_betera_upkeep", "'most holy to the "
                         "LORD' (Sifra Bechukotai Chapter 12 5)",
                         "R. Yehuda b. Betera, Mishnah Arakhin 8:6"),
                        ("sages_priests", "'as the devoted field, the "
                         "priest's holding' — the answer sheet's arm",
                         "the Sages, Mishnah Arakhin 8:6"))
        if q == "herem_given_to_which_priest":
            return one("any_priest",
                       "27:21's 'to the priest' — any priest (LV27-20)", TM,
                       "LV27-20", "Mishnah Challah 4:9")
        if q == "firstborn_consecration_type":
            return one("value_not_altar",
                       "R. Yishmael: value-consecration falls on everything, "
                       "altar holiness does not (LV27-18, Sifra Bechukotai "
                       "Section 5 2, VERBATIM)", TM, "LV27-18",
                       "Mishnah Arakhin 8:7")
        if q in ("maaser_cattle_on_flock", "maaser_new_on_old"):
            return one("not_tithed_together",
                       "'tithe of cattle and flock' — kinds apart; 'tithe, "
                       "you shall tithe' — two tithes a year (LV27-23, Sifra "
                       "Bechukotai Chapter 12 11, 13, VERBATIM)", TM,
                       "LV27-23", "Mishnah Bekhorot 9:1")
        if q == "maaser_sheep_on_goats":
            return one("tithed_together",
                       "'and flock' — all flock is one (LV27-23, Sifra "
                       "Bechukotai Chapter 12 12)", TM, "LV27-23",
                       "Mishnah Bekhorot 9:1")
        if q == "maaser_counted_lying_or_standing":
            return one("tithed",
                       "'the tenth shall be holy' — counted any way "
                       "(LV27-23, Sifra Bechukotai Chapter 13 1)", TM,
                       "LV27-23", "Mishnah Bekhorot 9:7")
        if q == "maaser_took_ten_of_hundred":
            return many(TM, "LV27-23",
                        ("sages_not_tithe", "'THE tenth' — no tithe (Sifra "
                         "Bechukotai Chapter 13 1)",
                         "the Sages, Mishnah Bekhorot 9:7"),
                        ("r_yosei_b_yehuda_tithe", "a tithe (Sifra "
                         "Bechukotai Chapter 13 1)",
                         "R. Yosei b. R. Yehuda, Mishnah Bekhorot 9:7"))
        if q == "maaser_ninth_called_tenth":
            return one("all_three_sanctified",
                       "THE ERROR RULE — the misnamed neighbors sanctified "
                       "(LV27-23, Sifra Bechukotai Chapter 13 2-3, VERBATIM)",
                       TM, "LV27-23", "Mishnah Nazir 5:3")
        return None

    return {
        "shemittah_land_file": {"fn": rule_shemittah_land_file,
                                "tractate": "Rosh Hashanah"},
        "overreaching_file": {"fn": rule_overreaching_file,
                              "tractate": "Bava Metzia"},
        "land_redemption_file": {"fn": rule_land_redemption_file,
                                 "tractate": "Arakhin"},
        "interest_and_slaves_file": {"fn": rule_interest_and_slaves_file,
                                     "tractate": "Bava Metzia"},
        "covenant_curses_file": {"fn": rule_covenant_curses_file,
                                 "tractate": "Megillah"},
        "valuations_file": {"fn": rule_valuations_file,
                            "tractate": "Arakhin"},
        "temurah_herem_tithe_file": {"fn": rule_temurah_herem_tithe_file,
                                     "tractate": "Temurah"},
    }
