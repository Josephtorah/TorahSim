# emor_rules.py — round 45, THE EMOR EXAM (2026-09-05). Bare Mishnah
# rows citing Lev 21-24, graded after the derivation. Read-source:
# logic/oral_triage/emor_exam_mishnah_2026-09-05.md. Seven modules,
# 135 cells over 79 LAW rows; every dispute returned whole with its
# arms labeled.


def build(V):
    def _EX(mishnah, anchor, **extra):
        d = dict(talmud_source=mishnah, exodus_anchor=anchor)
        d.update(extra)
        return d

    PP = _EX("Mishnah Kiddushin 1:7; Makkot 3:5; 3:8; 3:9; Bava Metzia "
             "2:10; Sanhedrin 2:1; Horayot 3:4; Yevamot 6:4; 6:5; 10:3; "
             "Makkot 3:1; Sotah 8:3; Makkot 1:1; Sanhedrin 11:1",
             "Lev 21:1-15 (lev_21_priest_family, LV21A claims — the "
             "priests' purity and marriage file)")
    PB = _EX("Mishnah Bekhorot 7:2; 7:5; Eruvin 10:13",
             "Lev 21:16-24 (lev_21_priest_blemish, LV21B claims)")
    TE = _EX("Mishnah Berakhot 1:1; Chagigah 3:3; Ketubot 5:2; 5:3; "
             "Niddah 5:3; Yevamot 6:3; 7:2; 7:5; 9:5; 9:6; Pesachim 2:4; "
             "Terumot 3:9; 6:6; Makkot 3:2; Shabbat 19:6",
             "Lev 22:1-16 (lev_22_holy_food, LV22A claims — the terumah "
             "eaters)")
    AO = _EX("Mishnah Shekalim 1:5; 4:8; 7:6; Zevachim 14:2; Chullin 5:1; "
             "5:3; 5:5; Menachot 3:6",
             "Lev 22:17-33 (lev_22_acceptable_offerings, LV22B claims)")
    CS = _EX("Mishnah Rosh Hashanah 1:9; 2:7; 2:9; Chagigah 2:4; Megillah "
             "3:5; 3:6; Menachot 5:3; 5:6; 6:7; 10:5; Kiddushin 1:9; "
             "Sukkah 3:12; Rosh Hashanah 4:3; Sukkah 5:7",
             "Lev 23:1-22 (lev_23_spring_festivals, LV23A claims — the "
             "calendar and the omer)")
    FF = _EX("Mishnah Rosh Hashanah 4:5; Yoma 8:1; 8:2; Sukkah 1:1; 2:4; "
             "2:6; 2:8; 3:1; 3:3; 3:5; 3:13; 4:2; 4:6",
             "Lev 23:23-44 (lev_23_fall_festivals, LV23B claims)")
    LB = _EX("Mishnah Menachot 8:4; 8:5; 11:5; Sanhedrin 7:5; 6:1; 6:3; "
             "4:1; 11:1; Shevuot 4:13; Makkot 1:6; Bava Kamma 3:10; 8:2; "
             "8:3",
             "Lev 24:1-23 (lev_24_lamp_bread + lev_24_blasphemer_talion, "
             "LV24A/LV24B claims)")

    def one(verdict, basis, prov, claim, authority=None):
        return [V(verdict, basis, authority=authority,
                  machine_claim=claim, **prov)]

    def many(prov, claim, *arms):
        return [V(v, b, authority=a, machine_claim=claim, **prov)
                for v, b, a in arms]

    # ------------------------------------------------ priest_purity_file
    def rule_priest_purity_file(case):
        q = case.get("query")
        if q == "priestess_defiles_for_dead":
            return one("daughters_of_aaron_defile",
                       "'do not defile for the dead' binds men only — the "
                       "daughters of Aaron defile (LV21A-01, Sifra Emor "
                       "Section 1 1, VERBATIM)", PP, "LV21A-01",
                       "Mishnah Kiddushin 1:7")
        if q == "gash_count_liability":
            return one("liable_per_gash_and_per_dead",
                       "one gash for five dead or five for one — each "
                       "(LV21A-05 per gash; Sifra Chapter 1 1, 4)", PP,
                       "LV21A-05", "Mishnah Makkot 3:5")
        if q == "baldness_on_head_liable":
            return one("whole_head_liable",
                       "baldness on the head — the whole head, not only "
                       "between the eyes (LV21A-05, Sifra Chapter 1 2)",
                       PP, "LV21A-05", "Mishnah Makkot 3:5")
        if q == "defiling_all_day_unwarned":
            return one("one_liability",
                       "defiling for the dead all day — one liability "
                       "without repeated warning", PP, "LV21A-03",
                       "Mishnah Makkot 3:8")
        if q == "defiling_all_day_warned_each":
            return one("liable_for_each",
                       "'do not defile, do not defile' — warned each time, "
                       "liable each time", PP, "LV21A-03",
                       "Mishnah Makkot 3:8")
        if q == "priest_in_cemetery_furrow":
            return one("one_of_eight_prohibitions",
                       "the priest in the house of impurity — one of the "
                       "furrow's eight prohibitions", PP, "LV21A-01",
                       "Mishnah Makkot 3:9")
        if q == "lost_object_in_cemetery":
            return one("priest_does_not_defile",
                       "the lost object in the cemetery — the priest does "
                       "not defile himself for it", PP, "LV21A-01",
                       "Mishnah Bava Metzia 2:10")
        if q == "father_orders_defilement":
            return one("do_not_obey",
                       "his father said 'defile yourself' — he does not "
                       "obey (the Lev 19 override, LV19A-02, meeting the "
                       "priest's ban)", PP, "LV21A-01",
                       "Mishnah Bava Metzia 2:10")
        if q == "high_priest_follows_bier":
            return many(PP, "LV21A-11",
                ("r_meir_hidden_revealed_to_gate",
                 "they hidden and he revealed, alternating, to the city "
                 "gate (Sifra Section 2 5, VERBATIM)",
                 "R. Meir — Mishnah Sanhedrin 2:1"),
                ("r_yehuda_not_out_at_all",
                 "'from the sanctuary he shall not go out' — not at all",
                 "R. Yehuda — Mishnah Sanhedrin 2:1"))
        if q == "high_priest_levirate":
            return one("chalitzah_not_yibbum",
                       "he releases but does not marry the levirate widow "
                       "— forbidden the widow (LV21A-12/13)", PP,
                       "LV21A-12", "Mishnah Sanhedrin 2:1")
        if q == "many_garmented_priest_rules":
            return one("virgin_widow_relatives_hair_as_anointed",
                       "the anointed and the many-garmented alike: "
                       "commanded on the virgin, forbidden the widow, no "
                       "defiling for relatives, no wild hair or rending "
                       "(LV21A-10 the crown of the oil; Sifra Section 2 6)",
                       PP, "LV21A-10", "Mishnah Horayot 3:4")
        if q == "high_priest_widow_from_betrothal":
            return one("forbidden",
                       "a widow from betrothal as from marriage — "
                       "forbidden to the high priest", PP, "LV21A-13",
                       "Mishnah Yevamot 6:4")
        if q == "high_priest_bogeret":
            return many(PP, "LV21A-12",
                ("forbidden",
                 "'in her virginity' excludes the adult whose virginity "
                 "has ended (Sifra Section 2 7)",
                 "the Mishnah's first arm — Yevamot 6:4"),
                ("r_eliezer_r_shimon_permit",
                 "R. Eliezer and R. Shimon permit the adult (Sifra "
                 "Section 2 7, VERBATIM)",
                 "R. Eliezer and R. Shimon — Mishnah Yevamot 6:4"))
        if q == "betrothed_widow_then_appointed":
            return one("may_marry_her",
                       "betrothed a widow then appointed — he marries her: "
                       "Yehoshua ben Gamla and Marta bat Baitos (LV21A-12, "
                       "Sifra Chapter 2 6, VERBATIM)", PP, "LV21A-12",
                       "Mishnah Yevamot 6:4")
        if q == "yevamah_maamar_then_appointed":
            return one("may_not_marry",
                       "the levirate widow even after ma'amar — 'take a "
                       "WIFE' and not a yevamah (LV21A-12)", PP,
                       "LV21A-12", "Mishnah Yevamot 6:4")
        if q == "zonah_definition":
            return many(PP, "LV21A-07",
                ("r_yehuda_aylonit",
                 "the aylonit is the zonah of the Torah (Sifra Chapter 1 "
                 "7, VERBATIM)", "R. Yehuda — Mishnah Yevamot 6:5"),
                ("sages_convert_freed_illicit",
                 "the convert, the freed slavewoman, the one who had "
                 "illicit intercourse — Onkelos's 'strayer' on this arm",
                 "the Sages — Mishnah Yevamot 6:5"))
        if q == "husband_returned_after_second_betrothal":
            return one("permitted_to_first_second_get_no_bar",
                       "'divorced from her husband' — not from one who is "
                       "not her husband: R. Elazar ben Matya (LV21A-07, "
                       "Sifra Chapter 1 11, VERBATIM)", PP, "LV21A-07",
                       "Mishnah Yevamot 10:3")
        if q == "widow_and_divorcee_lashes":
            return one("two_names",
                       "a widow who is also a divorcee — liable under two "
                       "names", PP, "LV21A-13", "Mishnah Makkot 3:1")
        if q == "divorcee_and_chalutzah_lashes":
            return one("one_name",
                       "divorcee and chalutzah — one name only: the "
                       "chalutzah rides the divorcee's clause by "
                       "amplification, no verse of her own (LV21A-07)", PP,
                       "LV21A-07", "Mishnah Makkot 3:1")
        if q == "widow_to_high_priest_war":
            return one("does_not_return",
                       "the forbidden unions do not return from the war's "
                       "front", PP, "LV21A-13", "Mishnah Sotah 8:3")
        if q == "zomemim_son_of_divorcee":
            return one("lashes_not_status",
                       "perjured witnesses on 'son of a divorcee' — forty "
                       "lashes, the status not transferable", PP,
                       "LV21A-13", "Mishnah Makkot 1:1")
        if q == "priests_daughter_partner_and_zomemim":
            return one("strangled_she_burns",
                       "'SHE by fire' — she burns; her partner and the "
                       "perjured witnesses are strangled (LV21A-09, Sifra "
                       "Chapter 1 18, VERBATIM)", PP, "LV21A-09",
                       "Mishnah Sanhedrin 11:1")
        return None

    # ------------------------------------------------ priest_blemish_file
    def rule_priest_blemish_file(case):
        q = case.get("query")
        if q == "giben_definition":
            return many(PB, "LV21B-04",
                ("no_eyebrows_or_one",
                 "no eyebrows or one — the giben of the Torah (Sifra "
                 "Section 3 12, VERBATIM)", "the Mishnah — Bekhorot 7:2"),
                ("r_dosa_lying", "eyebrows that lie flat",
                 "R. Dosa — Mishnah Bekhorot 7:2"),
                ("r_chanina_two_backs", "two backs and two spines",
                 "R. Chanina ben Antigonus — Mishnah Bekhorot 7:2"))
        if q == "kereach_priest":
            return one("unfit_without_hair_ring",
                       "the bald priest unfit — no ring of hair ear to ear "
                       "(the 'blemish... blemish' amplification, LV21B-05)",
                       PB, "LV21B-05", "Mishnah Bekhorot 7:2")
        if q == "meroach_ashekh_definition":
            return many(PB, "LV21B-04",
                ("no_testicles_or_one",
                 "no testicles or one — the meroach ashekh of the Torah",
                 "the Mishnah — Bekhorot 7:5"),
                ("r_yishmael_crushed",
                 "crushed testicles — the arm Onkelos renders (LV21B-04)",
                 "R. Yishmael — Mishnah Bekhorot 7:5"),
                ("r_akiva_wind", "wind in the testicles",
                 "R. Akiva — Mishnah Bekhorot 7:5"),
                ("r_chanina_dark", "a dark complexion",
                 "R. Chanina ben Antigonus — Mishnah Bekhorot 7:5"))
        if q == "teeth_removed_priest":
            return one("unfit_by_appearance",
                       "teeth removed — unfit because of appearance "
                       "(LV21B-05's non-blemish unfits)", PB, "LV21B-05",
                       "Mishnah Bekhorot 7:5")
        if q == "cut_wart_in_temple_sabbath":
            return one("permitted_in_temple_not_province",
                       "a wart cut in the Temple on the Sabbath, not in "
                       "the province — the priest made fit to serve "
                       "(LV21B-02's blemish class)", PB, "LV21B-02",
                       "Mishnah Eruvin 10:13")
        return None

    # ------------------------------------------------ terumah_eaters_file
    def rule_terumah_eaters_file(case):
        q = case.get("query")
        if q == "priests_terumah_entry_time":
            return one("sunset",
                       "'from when the priests enter to eat their terumah' "
                       "= sunset — the gate of Lev 22:7 (LV22A-04, Sifra "
                       "Chapter 4 2, VERBATIM)", TE, "LV22A-04",
                       "Mishnah Berakhot 1:1")
        if q == "onen_mechusar_kippurim_terumah":
            return one("immersion_for_kodesh_not_terumah",
                       "the onen and the one lacking atonement immerse for "
                       "kodesh, not for terumah — the offering does not "
                       "gate terumah (LV22A-04's two gates)", TE,
                       "LV22A-04", "Mishnah Chagigah 3:3")
        if q == "betrothed_time_arrived_unmarried":
            return one("eats_terumah_from_his_food",
                       "the time arrived and they did not marry — she eats "
                       "of his and eats terumah (the feeder's clock, "
                       "LV22A-07)", TE, "LV22A-07", "Mishnah Ketubot 5:2")
        if q == "terumah_portion_for_betrothed":
            return many(TE, "LV22A-07",
                ("r_tarfon_all_terumah", "all of it terumah",
                 "R. Tarfon — Mishnah Ketubot 5:2"),
                ("r_akiva_half", "half common, half terumah",
                 "R. Akiva — Mishnah Ketubot 5:2"))
        if q == "yavam_feeds_terumah":
            return one("does_not_feed",
                       "the yavam does not feed terumah — the levirate-"
                       "bound widow excluded (LV22A-09, Sifra Chapter 6 1, "
                       "VERBATIM)", TE, "LV22A-09", "Mishnah Ketubot 5:3")
        if q == "betrothed_eats_terumah_when":
            return many(TE, "LV22A-07",
                ("first_mishnah_at_time",
                 "the first Mishnah — when the time arrives",
                 "the first Mishnah — Ketubot 5:3"),
                ("later_court_at_chuppah",
                 "the later court — not until she enters the canopy",
                 "the later court — Mishnah Ketubot 5:3"))
        if q == "day_old_son_terumah":
            return one("feeds_and_disqualifies",
                       "a day-old boy feeds terumah and disqualifies from "
                       "it (LV22A-07 the son feeds the mother, Sifra "
                       "Section 5 6, VERBATIM)", TE, "LV22A-07",
                       "Mishnah Niddah 5:3")
        if q == "forbidden_union_from_betrothal_eats":
            return many(TE, "LV22A-08",
                ("does_not_eat",
                 "widow to the high priest, divorcee and chalutzah to the "
                 "commoner — from betrothal they do not eat ('to a man "
                 "who feeds', LV22A-08)", "the Mishnah — Yevamot 6:3"),
                ("r_eliezer_r_shimon_permit", "permit from betrothal",
                 "R. Eliezer and R. Shimon — Mishnah Yevamot 6:3"))
        if q == "widowed_from_forbidden_marriage":
            return one("disqualified_from_marriage_fit_from_betrothal",
                       "widowed or divorced — from marriage disqualified, "
                       "from betrothal fit", TE, "LV22A-08",
                       "Mishnah Yevamot 6:3")
        if q == "wife_brought_slaves_to_priest":
            return one("they_eat",
                       "the acquisition of an acquisition eats (LV22A-07, "
                       "Sifra Section 5 1, VERBATIM)", TE, "LV22A-07",
                       "Mishnah Yevamot 7:2")
        if q == "priests_daughter_brought_slaves_to_israelite":
            return one("they_do_not_eat",
                       "the priest's daughter's slaves under an Israelite "
                       "husband do not eat", TE, "LV22A-08",
                       "Mishnah Yevamot 7:2")
        if q == "rapist_seducer_fool_effect":
            return one("neither_disqualify_nor_feed",
                       "the rapist, the seducer, the fool — neither "
                       "disqualify nor feed", TE, "LV22A-09",
                       "Mishnah Yevamot 7:5")
        if q == "slave_disqualifies_by":
            return one("intercourse_not_seed",
                       "the slave disqualifies by intercourse, not by seed "
                       "— the grandmother case of Sifra Chapter 5 5 "
                       "(LV22A-09, VERBATIM)", TE, "LV22A-09",
                       "Mishnah Yevamot 7:5")
        if q == "mamzer_grandson_effect":
            return one("disqualifies_and_feeds",
                       "the mamzer disqualifies and feeds — Sifra Chapter "
                       "5 4 (LV22A-09, VERBATIM)", TE, "LV22A-09",
                       "Mishnah Yevamot 7:5")
        if q == "israelite_woman_to_priest_widowed_with_son":
            return one("eats_terumah",
                       "the Israelite woman married to a priest, widowed "
                       "with a son by him — eats terumah (the son feeds)",
                       TE, "LV22A-07", "Mishnah Yevamot 9:5")
        if q == "priests_daughter_son_by_israelite_died":
            return one("returns_to_fathers_house",
                       "'and she returns to her father's house' — the verse "
                       "the Mishnah quotes (LV22A-09, Sifra Chapter 6 1)",
                       TE, "LV22A-09", "Mishnah Yevamot 9:6")
        if q == "leavened_terumah_passover_in_error":
            return one("principal_and_fifth",
                       "in error — principal and fifth (LV22A-10 'in "
                       "error, not deliberate')", TE, "LV22A-10",
                       "Mishnah Pesachim 2:4")
        if q == "leavened_terumah_passover_deliberate":
            return one("exempt_from_payment",
                       "deliberate — exempt from payment and from the "
                       "wood's value", TE, "LV22A-10",
                       "Mishnah Pesachim 2:4")
        if q == "fifth_on_gentiles_terumah":
            return many(TE, "LV22A-11",
                ("liable_fifth",
                 "the gentile's terumah — liable a fifth on it",
                 "the Mishnah — Terumot 3:9"),
                ("r_shimon_exempt",
                 "exempt — the Sifra's 'Israel's holy things, not "
                 "gentiles'' (Chapter 6 8) on this arm",
                 "R. Shimon — Mishnah Terumot 3:9"))
        if q == "restitution_kind":
            return many(TE, "LV22A-10",
                ("r_eliezer_any_kind_if_better",
                 "any kind, paying the better for the worse (Sifra "
                 "Chapter 6 6, VERBATIM)",
                 "R. Eliezer — Mishnah Terumot 6:6"),
                ("r_akiva_kind_for_kind",
                 "kind for kind — wait for the post-seventh cucumbers",
                 "R. Akiva — Mishnah Terumot 6:6"))
        if q == "tevel_eating_measure":
            return many(TE, "LV22A-06",
                ("r_shimon_any_amount", "any amount, like the ant",
                 "R. Shimon — Mishnah Makkot 3:2"),
                ("sages_olive",
                 "an olive-bulk — 'no eating less than an olive' (LV22A-"
                 "06, Sifra Chapter 4 16)", "the Sages — Mishnah Makkot 3:2"))
        if q == "uncircumcised_eats_terumah":
            return one("barred",
                       "'and he does not eat terumah' — the uncircumcised "
                       "barred by two recorded routes (LV22A-06, Sifra "
                       "Chapter 4 18)", TE, "LV22A-06",
                       "Mishnah Shabbat 19:6")
        return None

    # -------------------------------------------- acceptable_offerings_file
    def rule_acceptable_offerings_file(case):
        q = case.get("query")
        if q == "gentile_shekels":
            return one("not_accepted",
                       "no shekels from gentiles — 'from a foreigner's "
                       "hand do not offer' (LV22B-05, Sifra Chapter 7 12, "
                       "VERBATIM)", AO, "LV22B-05", "Mishnah Shekalim 1:5")
        if q == "gentile_vows_and_freewill":
            return one("accepted",
                       "whatever is vowed or offered freely is accepted — "
                       "gentiles vow like Israel (LV22B-01, Sifra Section "
                       "7 2)", AO, "LV22B-01", "Mishnah Shekalim 1:5")
        if q == "consecrated_property_altar_fit_items":
            return one("sold_for_burnt_offerings",
                       "altar-fit items in consecrated property — sold for "
                       "that kind, burnt offerings bought (the altar-vs-"
                       "upkeep split, LV22B-04)", AO, "LV22B-04",
                       "Mishnah Shekalim 4:8")
        if q == "gentile_olah_from_abroad_no_libations":
            return one("from_public_funds",
                       "the gentile's burnt offering from abroad without "
                       "libations — from the public (a court ordinance on "
                       "the gentile vower, LV22B-01)", AO, "LV22B-01",
                       "Mishnah Shekalim 7:6")
        if q == "blemished_offered_outside":
            return many(AO, "LV22B-06",
                ("exempt",
                 "blemished animals offered outside — exempt: not fit to "
                 "come before the sanctuary", "the Mishnah — Zevachim 14:2"),
                ("r_shimon_passing_blemish_prohibition",
                 "passing blemishes — a prohibition, since it may come "
                 "later", "R. Shimon — Mishnah Zevachim 14:2"))
        if q == "under_age_offered_outside":
            return many(AO, "LV22B-06",
                ("exempt", "the under-age and it-and-its-young — exempt",
                 "the Mishnah — Zevachim 14:2"),
                ("r_shimon_prohibition_no_karet",
                 "'whatever may come later is a prohibition without "
                 "karet'", "R. Shimon — Mishnah Zevachim 14:2"))
        if q == "oto_veet_beno_common_outside":
            return one("both_valid_second_lashed",
                       "common animals outside — both valid, the second "
                       "lashed (LV22B-07)", AO, "LV22B-07",
                       "Mishnah Chullin 5:1")
        if q == "oto_veet_beno_consecrated_outside":
            return one("first_karet_both_unfit_both_lashed",
                       "consecrated outside — the first karet (outside "
                       "slaughter), both unfit, both lashed", AO,
                       "LV22B-07", "Mishnah Chullin 5:1")
        if q == "slaughtered_found_terefah_oto_veet_beno":
            return many(AO, "LV22B-08",
                ("sages_liable",
                 "found torn, for idolatry, the red cow, the stoned ox, "
                 "the heifer — liable (the Sifra's R. Meir arm, Chapter 8 "
                 "6)", "the Sages — Mishnah Chullin 5:3"),
                ("r_shimon_exempt", "exempt",
                 "R. Shimon — Mishnah Chullin 5:3"))
        if q == "failed_slaughter_oto_veet_beno":
            return one("exempt",
                       "became a carcass in his hand, the stabber, the "
                       "tearer — exempt (LV22B-08, Sifra Chapter 8 5)", AO,
                       "LV22B-08", "Mishnah Chullin 5:3")
        if q == "two_bought_cow_and_calf":
            return one("first_buyer_slaughters_first",
                       "two who bought — the first buyer slaughters first; "
                       "if the second preceded, he gained", AO, "LV22B-08",
                       "Mishnah Chullin 5:3")
        if q == "cow_then_two_calves":
            return one("eighty_lashes",
                       "the mother then her two calves — eighty (each "
                       "calf a liability; Sifra Chapter 8 3)", AO,
                       "LV22B-07", "Mishnah Chullin 5:3")
        if q == "two_calves_then_cow":
            return one("forty_lashes",
                       "two calves then the mother — forty (one "
                       "liability)", AO, "LV22B-07", "Mishnah Chullin 5:3")
        if q == "cow_granddaughter_then_daughter":
            return many(AO, "LV22B-07",
                ("forty_lashes",
                 "her and her granddaughter, then her daughter — forty",
                 "the Mishnah — Chullin 5:3"),
                ("sumchos_eighty", "eighty",
                 "Sumchos in R. Meir's name — Mishnah Chullin 5:3"))
        if q == "seller_must_inform_periods":
            return one("four_periods_inform_mother_sold",
                       "the eve of Sukkot's last day, of Passover's first, "
                       "of Atzeret, of Rosh Hashanah — 'its mother I sold "
                       "to slaughter' (LV22B-08, Sifra Chapter 8 8, "
                       "VERBATIM)", AO, "LV22B-08", "Mishnah Chullin 5:3")
        if q == "seller_inform_condition":
            return one("r_yehuda_when_no_time_gap",
                       "R. Yehuda: only when there is no time gap between "
                       "the sales", AO, "LV22B-08", "Mishnah Chullin 5:3",
                       )
        if q == "mother_to_groom_daughter_to_bride":
            return one("must_inform",
                       "the mother to the groom and the daughter to the "
                       "bride — must inform, both known to slaughter the "
                       "same day", AO, "LV22B-08", "Mishnah Chullin 5:3")
        if q == "one_day_boundary_oto_veet_beno":
            return one("day_follows_night_ben_zoma",
                       "'one day' — the day follows the night, ben Zoma's "
                       "creation analogy (LV22B-08, Sifra Chapter 8 9, "
                       "VERBATIM)", AO, "LV22B-08", "Mishnah Chullin 5:5")
        if q == "two_atzeret_lambs_block":
            return one("they_block_each_other",
                       "the two Atzeret lambs block each other (LV23A-12; "
                       "the loaves, rows, and dishes likewise, LV24A-04)",
                       AO, "LV23A-12", "Mishnah Menachot 3:6")
        return None

    # ------------------------------------------------ calendar_spring_file
    def rule_calendar_spring_file(case):
        q = case.get("query")
        if q == "new_moon_witness_cannot_walk":
            return one("carried_even_on_bed",
                       "the witness who cannot walk is carried on a donkey, "
                       "even on a bed", CS, "LV23A-03",
                       "Mishnah Rosh Hashanah 1:9")
        if q == "profane_sabbath_for_moon_testimony":
            return one("permitted_in_their_season",
                       "'which you shall proclaim in their season' — the "
                       "Sabbath profaned for the testimony (LV23A-03, "
                       "Sifra Chapter 10 6, VERBATIM)", CS, "LV23A-03",
                       "Mishnah Rosh Hashanah 1:9")
        if q == "court_says_sanctified":
            return one("people_answer_sanctified",
                       "the head of the court says 'sanctified' and all "
                       "answer 'sanctified, sanctified' — the utterance is "
                       "the act (LV23A-01/03)", CS, "LV23A-03",
                       "Mishnah Rosh Hashanah 2:7")
        if q == "moon_not_seen_in_its_time":
            return many(CS, "LV23A-03",
                ("sanctify_it",
                 "seen in its time or not — they sanctify it",
                 "the Mishnah — Rosh Hashanah 2:7"),
                ("r_elazar_heaven_sanctified",
                 "not seen in its time — not sanctified: Heaven already "
                 "sanctified it",
                 "R. Elazar b. R. Tzadok — Mishnah Rosh Hashanah 2:7"))
        if q == "court_erred_festival_binding":
            return one("binding_no_festivals_but_these",
                       "'which you shall proclaim — in their time or not, "
                       "I have no festivals but these' (LV23A-01, Sifra "
                       "Section 9 3, VERBATIM)", CS, "LV23A-01",
                       "R. Akiva — Mishnah Rosh Hashanah 2:9")
        if q == "court_authority_like_moses":
            return one("every_three_as_moses_court",
                       "every three who stood as a court over Israel are as "
                       "the court of Moses", CS, "LV23A-01",
                       "R. Dosa ben Harkinas — Mishnah Rosh Hashanah 2:9")
        if q == "atzeret_on_friday_slaughter_day":
            return many(CS, "LV23A-07",
                ("beit_shammai_after_sabbath",
                 "the slaughter day is after the Sabbath",
                 "Beit Shammai — Mishnah Chagigah 2:4"),
                ("beit_hillel_none", "no slaughter day after the Sabbath",
                 "Beit Hillel — Mishnah Chagigah 2:4"))
        if q == "atzeret_on_sabbath":
            return one("slaughter_day_after_no_vestments_eulogy_permitted",
                       "on the Sabbath — the slaughter day after; the high "
                       "priest not in his vestments, eulogy and fasting "
                       "permitted — 'not to uphold those who say Atzeret "
                       "is after the Sabbath' (the morrow dispute, "
                       "LV23A-07)", CS, "LV23A-07", "Mishnah Chagigah 2:4")
        if q == "passover_torah_reading":
            return one("festivals_section_torat_kohanim",
                       "on Passover they read the festivals section of "
                       "Torat Kohanim — Lev 23 as the reading text", CS,
                       "LV23A-04", "Mishnah Megillah 3:5")
        if q == "festival_readings_rule":
            return one("each_read_in_its_time",
                       "'Moses declared the festivals' — each read in its "
                       "time (LV23B-12, Sifra Chapter 17 12, VERBATIM)",
                       CS, "LV23B-12", "Mishnah Megillah 3:6")
        if q == "omer_minchah_oil_frankincense":
            return one("requires_both",
                       "the omer's grain offering requires oil and "
                       "frankincense (LV23A-08)", CS, "LV23A-08",
                       "Mishnah Menachot 5:3")
        if q == "two_loaves_oil_frankincense":
            return one("neither",
                       "the two loaves — neither oil nor frankincense "
                       "(LV23A-11)", CS, "LV23A-11", "Mishnah Menachot 5:3")
        if q == "two_loaves_waving_placement":
            return one("loaves_on_lambs_hands_beneath",
                       "he puts the two loaves on the two lambs, hands "
                       "beneath — the Mishnah's geometry among the Sifra's "
                       "four (LV23A-12, Chapter 13 8)", CS, "LV23A-12",
                       "Mishnah Menachot 5:6")
        if q == "omer_minchah_waving_presenting":
            return one("both_waving_and_presenting",
                       "the omer's grain offering requires waving and "
                       "presenting (LV23A-07 the waving building block)",
                       CS, "LV23A-07", "Mishnah Menachot 5:6")
        if q == "omer_sieve_count":
            return many(CS, "LV24A-03",
                ("thirteen_sieves",
                 "the omer thirteen sieves, the loaves twelve, the "
                 "showbread eleven", "the Mishnah — Menachot 6:7"),
                ("r_shimon_no_fixed_number",
                 "'take fine flour and bake it' — sifted as needed, no "
                 "fixed number", "R. Shimon — Mishnah Menachot 6:7"))
        if q == "flour_market_after_omer":
            return many(CS, "LV23A-09",
                ("r_meir_against_sages",
                 "the markets full of flour — against the Sages' will "
                 "(Sifra Section 10 10, VERBATIM)",
                 "R. Meir — Mishnah Menachot 10:5"),
                ("r_yehuda_with_sages", "with the Sages' will",
                 "R. Yehuda — Mishnah Menachot 10:5"))
        if q == "new_grain_after_omer":
            return one("permitted_immediately_distant_from_midday",
                       "new grain permitted immediately after the omer; the "
                       "distant from midday — 'the court is not slack' "
                       "(LV23A-09, VERBATIM)", CS, "LV23A-09",
                       "Mishnah Menachot 10:5")
        if q == "waving_day_after_destruction":
            return many(CS, "LV23A-09",
                ("rybz_whole_day_forbidden",
                 "R. Yochanan ben Zakkai ordained the whole waving day "
                 "forbidden",
                 "R. Yochanan ben Zakkai — Mishnah Menachot 10:5"),
                ("r_yehuda_torah_until_this_day",
                 "'until this very day' — forbidden by the Torah itself",
                 "R. Yehuda — Mishnah Menachot 10:5"))
        if q == "land_laws_abroad":
            return many(CS, "LV23A-09",
                ("orlah_and_kilayim",
                 "land-dependent laws only in the land, except orlah and "
                 "kilayim (R. Shimon's three with their source labels, "
                 "Sifra Section 10 11)", "the Mishnah — Kiddushin 1:9"),
                ("r_eliezer_also_new_grain", "also the new grain",
                 "R. Eliezer — Mishnah Kiddushin 1:9"))
        if q == "lulav_in_provinces":
            return many(CS, "LV23B-09",
                ("temple_seven_province_one",
                 "at first — seven in the Temple, one in the provinces",
                 "the Mishnah — Sukkah 3:12 / Rosh Hashanah 4:3"),
                ("rybz_seven_remembrance",
                 "after the destruction — seven in the provinces as a "
                 "remembrance (Sifra Chapter 16 9, VERBATIM)",
                 "R. Yochanan ben Zakkai — Mishnah Sukkah 3:12"))
        if q == "watches_equal_at_atzeret":
            return one("matzah_and_leaven_offered",
                       "at Atzeret they say 'here is matzah, here is "
                       "leaven' — the leavened loaves beside the showbread "
                       "division (LV23A-11, LV24A-06)", CS, "LV23A-11",
                       "Mishnah Sukkah 5:7")
        return None

    # ------------------------------------------------ fall_festivals_file
    def rule_fall_festivals_file(case):
        q = case.get("query")
        if q == "rosh_hashanah_blessing_order":
            return many(FF, "LV23B-01",
                ("r_yochanan_ben_nuri_malkhuyot_no_blast",
                 "malkhuyot with the Name's holiness, no blast (Sifra "
                 "Section 11 3, VERBATIM)",
                 "R. Yochanan ben Nuri — Mishnah Rosh Hashanah 4:5"),
                ("r_akiva_malkhuyot_with_day_and_blast",
                 "'if no blast, why mention them?' — malkhuyot with the "
                 "day's holiness and blast",
                 "R. Akiva — Mishnah Rosh Hashanah 4:5"))
        if q == "yom_kippur_forbidden_list":
            return one("eating_drinking_washing_anointing_sandals_relations",
                       "the afflictions from 'shabbaton = shevut' (LV23B-"
                       "04, Sifra Chapter 14 4, VERBATIM)", FF, "LV23B-04",
                       "Mishnah Yoma 8:1")
        if q == "king_and_bride_wash_faces":
            return many(FF, "LV23B-04",
                ("r_eliezer_permit",
                 "the king and the bride wash their faces, the new mother "
                 "wears sandals", "R. Eliezer — Mishnah Yoma 8:1"),
                ("sages_forbid", "forbidden", "the Sages — Mishnah Yoma 8:1"))
        if q == "eating_measure_yom_kippur":
            return one("large_date",
                       "a large date with its stone — transmitted "
                       "quantity, the data channel", FF, "LV23B-04",
                       "Mishnah Yoma 8:2")
        if q == "drinking_measure_yom_kippur":
            return one("mouthful", "a mouthful — transmitted quantity", FF,
                       "LV23B-04", "Mishnah Yoma 8:2")
        if q == "food_and_drink_combine":
            return one("do_not_combine",
                       "foods combine, drinks combine, food and drink do "
                       "not", FF, "LV23B-04", "Mishnah Yoma 8:2")
        if q == "sukkah_above_twenty_cubits":
            return many(FF, "LV23B-11",
                ("invalid", "above twenty cubits — invalid",
                 "the Mishnah — Sukkah 1:1"),
                ("r_yehuda_valid", "valid", "R. Yehuda — Mishnah Sukkah 1:1"))
        if q == "old_sukkah":
            return many(FF, "LV23B-11",
                ("beit_shammai_invalid",
                 "made thirty days before the festival — invalid",
                 "Beit Shammai — Mishnah Sukkah 1:1"),
                ("beit_hillel_valid", "valid",
                 "Beit Hillel — Mishnah Sukkah 1:1"))
        if q == "sukkah_among_trees_walls":
            return one("valid",
                       "the trees as its walls — valid", FF, "LV23B-11",
                       "Mishnah Sukkah 2:4")
        if q == "agents_of_mitzvah_sick":
            return one("exempt",
                       "agents of a commandment, the sick and their "
                       "attendants — exempt ('dwell as you live', LV23B-11)",
                       FF, "LV23B-11", "Mishnah Sukkah 2:4")
        if q == "sukkah_meal_count":
            return many(FF, "LV23B-11",
                ("r_eliezer_fourteen",
                 "fourteen meals, one by day and one by night",
                 "R. Eliezer — Mishnah Sukkah 2:6"),
                ("sages_first_night_only",
                 "no fixed number except the first night",
                 "the Sages — Mishnah Sukkah 2:6"))
        if q == "missed_first_night_meal":
            return many(FF, "LV23B-11",
                ("r_eliezer_make_up_last_night",
                 "make it up on the last night",
                 "R. Eliezer — Mishnah Sukkah 2:6"),
                ("sages_no_make_up",
                 "no make-up — 'what is crooked cannot be made straight'",
                 "the Sages — Mishnah Sukkah 2:6"))
        if q == "women_slaves_minors_sukkah":
            return one("exempt_minor_not_needing_mother_obligated",
                       "women, slaves, minors exempt; a minor not needing "
                       "his mother obligated (LV23B-11, Sifra Chapter 17 "
                       "9, VERBATIM)", FF, "LV23B-11", "Mishnah Sukkah 2:8")
        if q == "stolen_or_dry_lulav":
            return one("invalid",
                       "the stolen or dry lulav invalid — 'yours, not the "
                       "stolen' (LV23B-09, Sifra Chapter 16 2)", FF,
                       "LV23B-09", "Mishnah Sukkah 3:1")
        if q == "lulav_leaves_split_or_spread":
            return many(FF, "LV23B-09",
                ("split_invalid_spread_valid",
                 "leaves split — invalid; spread apart — valid",
                 "the Mishnah — Sukkah 3:1"),
                ("r_yehuda_bind", "bind it at the top (Sifra Chapter 16 "
                 "5, R. Tarfon's binding)", "R. Yehuda — Mishnah Sukkah 3:1"))
        if q == "willow_of_field":
            return one("valid",
                       "the willow of the field valid — 'of the field and "
                       "the mountain too' (LV23B-09, Sifra Chapter 16 6, "
                       "VERBATIM)", FF, "LV23B-09", "Mishnah Sukkah 3:3")
        if q == "poplar_as_willow":
            return one("invalid", "the poplar — invalid", FF, "LV23B-09",
                       "Mishnah Sukkah 3:3")
        if q == "etrog_of_pure_terumah":
            return one("not_taken_but_valid",
                       "of pure terumah — not taken, but if taken valid",
                       FF, "LV23B-09", "Mishnah Sukkah 3:5")
        if q == "fellows_lulav_first_day":
            return one("not_discharged",
                       "the first day not discharged with a fellow's lulav "
                       "(LV23B-09, Sifra Chapter 16 2, VERBATIM)", FF,
                       "LV23B-09", "Mishnah Sukkah 3:13")
        if q == "fellows_lulav_other_days":
            return one("discharged",
                       "the other days — discharged with a fellow's", FF,
                       "LV23B-09", "Mishnah Sukkah 3:13")
        if q == "lulav_seven_days_when":
            return one("first_day_on_sabbath",
                       "lulav seven — when the first day falls on the "
                       "Sabbath; otherwise six (LV23B-09, Sifra Chapter 16 "
                       "3, VERBATIM)", FF, "LV23B-09", "Mishnah Sukkah 4:2")
        if q == "willow_rite_on_sabbath":
            return one("gathered_friday_golden_basins",
                       "gathered on Friday and kept in golden basins — the "
                       "Temple's willow (Abba Shaul's second willow, "
                       "LV23B-09)", FF, "LV23B-09", "Mishnah Sukkah 4:6")
        return None

    # ------------------------------------------ lamp_bread_blasphemer_file
    def rule_lamp_bread_blasphemer_file(case):
        q = case.get("query")
        if q == "three_olives_three_oils":
            return one("first_for_menorah_rest_for_menachot",
                       "three olives, three oils each — the first for the "
                       "menorah, the rest for the grain offerings (LV24A-"
                       "01, Sifra Section 13 1-3, VERBATIM)", LB, "LV24A-01",
                       "Mishnah Menachot 8:4")
        if q == "olive_pressing_method":
            return many(LB, "LV24A-01",
                ("mill_and_beam", "ground in the mill, pressed under the "
                 "beam", "the Mishnah — Menachot 8:4"),
                ("r_yehuda_mortar_and_stones",
                 "crushed in a mortar, pressed with stones, around the "
                 "basket (Sifra Section 13 4, VERBATIM)",
                 "R. Yehuda — Mishnah Menachot 8:4"))
        if q == "nine_grade_order":
            return one("first_of_first_top_third_of_third_bottom",
                       "the nine grades totally ordered (LV24A-01, Sifra "
                       "Section 13 5, VERBATIM)", LB, "LV24A-01",
                       "Mishnah Menachot 8:5")
        if q == "beaten_oil_for_menachot":
            return one("not_required_only_for_light",
                       "'pure beaten for the light' — not pure beaten for "
                       "the grain offerings (LV24A-01, Sifra Section 13 6, "
                       "VERBATIM)", LB, "LV24A-01", "Mishnah Menachot 8:5")
        if q == "showbread_table_dimensions":
            return many(LB, "LV24A-04",
                ("r_yehuda_ten_by_five", "the table ten by five",
                 "R. Yehuda — Mishnah Menachot 11:5"),
                ("r_meir_twelve_by_six", "twelve by six",
                 "R. Meir — Mishnah Menachot 11:5"))
        if q == "frankincense_dishes_place":
            return many(LB, "LV24A-04",
                ("on_the_row",
                 "'and put pure frankincense on the row' — the dishes on "
                 "the rows (LV24A-04's two dishes with rims)",
                 "the Sages — Mishnah Menachot 11:5"),
                ("abba_shaul_between_rows",
                 "the two dishes in the gap between the rows",
                 "Abba Shaul — Mishnah Menachot 11:5"))
        if q == "blasphemer_liability_condition":
            return one("pronounces_the_name",
                       "the blasphemer liable only when he pronounces the "
                       "Name (LV24B-01, Sifra Section 14 2, VERBATIM)", LB,
                       "LV24B-01", "Mishnah Sanhedrin 7:5")
        if q == "blasphemy_witness_procedure":
            return one("substitute_in_trial_explicit_at_verdict_judges_rend",
                       "'Yosi strike Yosi' in the trial; at the verdict the "
                       "eldest says it explicitly, the judges stand and "
                       "rend (LV24B-02, Sifra Section 14 3, VERBATIM)", LB,
                       "LV24B-02", "R. Yehoshua ben Korcha — Mishnah "
                       "Sanhedrin 7:5")
        if q == "stoning_place_location":
            return one("outside_the_court",
                       "'bring out the blasphemer' — the stoning place "
                       "outside the court (LV24B-03, Sifra Chapter 19 1, "
                       "VERBATIM)", LB, "LV24B-03", "Mishnah Sanhedrin 6:1")
        if q == "herald_before_execution":
            return one("announces_name_offense_witnesses",
                       "the herald: so-and-so goes out to be stoned for "
                       "such an offense, these his witnesses — whoever "
                       "knows a merit, come", LB, "LV24B-03",
                       "Mishnah Sanhedrin 6:1")
        if q == "stoned_clothing":
            return many(LB, "LV24B-03",
                ("r_yehuda_man_front_woman_both",
                 "the man covered in front, the woman front and back",
                 "R. Yehuda — Mishnah Sanhedrin 6:3"),
                ("sages_man_naked_woman_not",
                 "the man stoned naked, the woman not — 'stone him, not "
                 "his clothing' (Sifra Chapter 19 3)",
                 "the Sages — Mishnah Sanhedrin 6:3"))
        if q == "monetary_and_capital_inquiry":
            return one("both_by_inquiry_and_examination",
                       "'one judgment shall be for you' — both by inquiry "
                       "and examination (LV24B-07, Sifra Chapter 20 9, "
                       "VERBATIM)", LB, "LV24B-07", "Mishnah Sanhedrin 4:1")
        if q == "judge_count_monetary_vs_capital":
            return one("three_vs_twenty_three",
                       "monetary by three, capital by twenty-three — 'eye "
                       "for eye' amplifies the difference (LV24B-07)", LB,
                       "LV24B-07", "Mishnah Sanhedrin 4:1")
        if q == "parent_striker_liability":
            return one("only_with_a_wound",
                       "the parent-striker not liable until he wounds — as "
                       "the beast (LV24B-07, Sifra Chapter 20 8, VERBATIM)",
                       LB, "LV24B-07", "Mishnah Sanhedrin 11:1")
        if q == "parent_curser_vs_striker_after_death":
            return one("curser_liable_striker_exempt",
                       "the curser after death liable, the striker after "
                       "death exempt — 'in life' as the beast (LV24B-07)",
                       LB, "LV24B-07", "Mishnah Sanhedrin 11:1")
        if q == "cursing_with_substitute_names":
            return many(LB, "LV24B-04",
                ("r_meir_liable",
                 "cursing with the substitutes — liable (Sifra Chapter 19 "
                 "5, VERBATIM)", "R. Meir — Mishnah Shevuot 4:13"),
                ("sages_exempt", "exempt — the unique Name alone carries "
                 "death; Onkelos's 'explicitly utters' on this arm",
                 "the Sages — Mishnah Shevuot 4:13"))
        if q == "parent_curser_substitute_names":
            return many(LB, "LV24B-04",
                ("r_meir_liable", "the parent-curser with substitutes — "
                 "liable", "R. Meir — Mishnah Shevuot 4:13"),
                ("sages_exempt", "exempt — 'when he pronounces the Name' "
                 "(R. Menachem b. R. Yosei, Sifra Chapter 19 7)",
                 "the Sages — Mishnah Shevuot 4:13"))
        if q == "zomemim_execution_timing":
            return one("not_until_verdict_finished",
                       "'life for life' — the perjured executed only after "
                       "the verdict, against the Sadducees (the talion "
                       "clause's cousin, LV24B-05)", LB, "LV24B-05",
                       "Mishnah Makkot 1:6")
        if q == "ox_shamed_vs_man_shamed":
            return one("ox_exempt_man_liable",
                       "his ox that shamed — exempt; he who shamed — "
                       "liable (the shame class, LV24B-06)", LB,
                       "LV24B-06", "Mishnah Bava Kamma 3:10")
        if q == "ox_wounded_parents_vs_man":
            return one("ox_pays_man_exempt_capital",
                       "his ox wounded his parents — pays; he himself — "
                       "exempt from payment, being liable with his life",
                       LB, "LV24B-07", "Mishnah Bava Kamma 3:10")
        if q == "man_pays_for_injury":
            return one("damage_pain_healing_idleness_shame",
                       "man pays five — talion as payment (LV24B-06, Sifra "
                       "Chapter 20 7)", LB, "LV24B-06",
                       "Mishnah Bava Kamma 8:2")
        if q == "ox_pays_for_injury":
            return one("damage_only",
                       "the ox pays damage only, and not the value of "
                       "offspring", LB, "LV24B-06", "Mishnah Bava Kamma 8:2")
        if q == "struck_parents_without_wound":
            return one("liable_all_five",
                       "struck his parents without a wound — liable for all "
                       "five payments (no death without the wound, "
                       "LV24B-07)", LB, "LV24B-07", "Mishnah Bava Kamma 8:3")
        if q == "canaanite_slave_shame":
            return many(LB, "LV24B-06",
                ("liable_all", "wounding another's Canaanite slave — "
                 "liable for all", "the Mishnah — Bava Kamma 8:3"),
                ("r_yehuda_no_shame_for_slaves", "slaves have no shame "
                 "payment", "R. Yehuda — Mishnah Bava Kamma 8:3"))
        return None

    return {
        "priest_purity_file": {"fn": rule_priest_purity_file,
                               "tractate": "Yevamot"},
        "priest_blemish_file": {"fn": rule_priest_blemish_file,
                                "tractate": "Bekhorot"},
        "terumah_eaters_file": {"fn": rule_terumah_eaters_file,
                                "tractate": "Yevamot"},
        "acceptable_offerings_file": {"fn": rule_acceptable_offerings_file,
                                      "tractate": "Chullin"},
        "calendar_spring_file": {"fn": rule_calendar_spring_file,
                                 "tractate": "Rosh Hashanah"},
        "fall_festivals_file": {"fn": rule_fall_festivals_file,
                                "tractate": "Sukkah"},
        "lamp_bread_blasphemer_file": {"fn": rule_lamp_bread_blasphemer_file,
                                       "tractate": "Sanhedrin"},
    }
