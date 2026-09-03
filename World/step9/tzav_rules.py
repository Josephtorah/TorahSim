#!/usr/bin/env python3
"""tzav_rules.py — the round-11 exam's rule modules (2026-09-03, the
derive-then-examine rhythm's eighth cycle). Sixteen modules on Lev 6-8
anchors, every rule compiled from the claims the same sitting's Sifra
Tzav reading seated. engine.py merges build(V) at its tail."""


def build(V):
    def _LV(mishnah, anchor, **extra):
        d = dict(mishnah=mishnah, leviticus_anchor=anchor)
        d.update(extra)
        return d

    # ---------------------------------------------------- wrong intent
    WI = _LV("Mishnah Zevachim 1:1",
             "Lev.7.5 (lev_07_asham_procedure, LV07A-03 word-position "
             "argument: the guilt-offering's restrictive 'it' sits after "
             "the smoking — wrong intent leaves it fit)")

    def rule_wrong_intent(case):
        off = case.get("offering")
        if case.get("query") != "wrong_intent_fitness":
            return None
        if off == "pesach":
            return [V("unfit_at_its_time", "the Pesach carries its "
                      "restrictive 'it' at the slaughter — unfit when "
                      "sacrificed not for its sake at its appointed time",
                      machine_claim="LV07A-03", **WI)]
        if off == "chatat":
            return [V("unfit_any_time", "the sin-offering's 'it' rides the "
                      "slaughter clause — unfit not-for-its-sake at all "
                      "times", machine_claim="LV07A-03", **WI)]
        if off == "asham":
            return [V("fit_owner_unaccredited", "the first tanna: the "
                      "guilt-offering's 'it' sits after the smoking, and "
                      "even unsmoked portions leave it kasher — fit, the "
                      "owner unaccredited (Sifra Tzav Section 5 8)",
                      authority="tanna kamma", machine_claim="LV07A-03",
                      **WI),
                    V("unfit_any_time", "R. Eliezer: the guilt-offering "
                      "comes for transgression like the sin-offering — "
                      "unfit not-for-its-sake (Sifra Tzav Section 5 6, the "
                      "same recorded analogy)", authority="R. Eliezer",
                      machine_claim="LV07A-03", **WI)]
        return [V("fit_owner_unaccredited", "all other offerings "
                  "slaughtered not for their sake are FIT but do not "
                  "satisfy the owner", machine_claim="LV07A-03", **WI)]

    # ---------------------------------------------------- piggul scope
    PG = _LV("Mishnah Zevachim 2:2-4:5; Menachot 3:1",
             "Lev.7.18 (lev_07_shelamim_types, LV07B-06 rejection machine; "
             "LV07B-10 the two-machine comparison)")

    def rule_piggul(case):
        q = case.get("query")
        if q == "bad_intent_effect":
            item = case.get("item")
            intent = case.get("intent")
            if item == "hide_bones_gravy":
                return [V("fit_no_karet", "hide, gravy, spices, tendons, "
                          "bones, horns, hooves are not 'flesh' — no "
                          "rejection, no karet (the flesh-only rule, Sifra "
                          "Tzav Chapter 12 15)", machine_claim="LV07B-05",
                          **PG)]
            if intent == "out_of_place":
                return [V("disqualified_no_karet", "out-of-place thought "
                          "disqualifies but karet rides time only ('shall "
                          "bear its sin' restricted — Sifra Tzav Chapter "
                          "13 2)", machine_claim="LV07B-06", **PG)]
            if intent == "out_of_time":
                return [V("piggul_karet", "out-of-time thought is the "
                          "rejection with karet — the thought, not the "
                          "deed (Sifra Tzav Section 8 1)",
                          machine_claim="LV07B-06", **PG)]
            if intent == "leave_blood_tomorrow":
                return [V("unfit", "R. Yehuda: leaving-intent is an "
                          "out-of-time thought", authority="R. Yehuda",
                          machine_claim="LV07B-06", **PG),
                        V("fit", "the Rabbis: intent to leave, not to eat "
                          "or burn tomorrow — outside the thought classes",
                          authority="the Rabbis", machine_claim="LV07B-06",
                          **PG)]
            if intent == "wrong_manner":
                return [V("fit", "intent to eat the uneatable or burn the "
                          "unburnable does not reject — the typical-manner "
                          "criterion", authority="tanna kamma",
                          machine_claim="LV07B-06", **PG),
                        V("unfit", "R. Eliezer unfits",
                          authority="R. Eliezer", machine_claim="LV07B-06",
                          **PG)]
        if q == "piggul_liability":
            if case.get("offering") == "gentile_offering":
                return [V("exempt", "R. Shimon: gentiles' offerings carry "
                          "no rejection, leftover, or impure-eating "
                          "liability", authority="R. Shimon",
                          machine_claim="LV07B-06", **PG),
                        V("liable", "R. Yosei deems liable",
                          authority="R. Yosei", machine_claim="LV07B-06",
                          **PG)]
            if case.get("item") in ("fistful", "the_blood"):
                return [V("no_piggul", "the no-permitters list: the "
                          "fistful, incense, frankincense, the wholly-"
                          "burnt meal-offerings, the blood — nothing else "
                          "permits them, so the rejection cannot attach "
                          "(Sifra Tzav Chapter 13 5)",
                          machine_claim="LV07B-06", **PG)]
        if q == "notar_tumah_liability":
            if case.get("item") == "the_blood":
                return [V("exempt", "the one exception: the blood — "
                          "forbidden in itself, outside the leftover and "
                          "impurity liabilities (Sifra Tzav Chapter 15 6)",
                          machine_claim="LV07B-10", **PG)]
            return [V("liable", "no-permitter items still carry leftover "
                      "and impure-eating liability — the tumah machine "
                      "reaches them through Lev 22:3 where the rejection "
                      "machine cannot (Sifra Tzav Chapter 15 4)",
                      machine_claim="LV07B-10", **PG)]
        return None

    # ------------------------------------------------- altar retention
    AR = _LV("Mishnah Zevachim 9:1, 9:6",
             "Lev.6.2 (lev_06_olah_minchah_torah, LV06-01 the one-way "
             "altar; LV06-04 the midnight boundary)")

    def rule_altar_retention(case):
        q = case.get("query")
        if q == "altar_retention_criterion":
            return [V("fire_fit_stays", "R. Yehoshua: what is suited to "
                      "the fire, once up, does not come down ('It is the "
                      "olah on its pyre')", authority="R. Yehoshua",
                      machine_claim="LV06-01", **AR),
                    V("altar_fit_stays", "Rabban Gamliel: what is suited "
                      "to the altar does not come down — their recorded "
                      "delta is unfit blood and libations (Sifra Tzav "
                      "Chapter 1 6)", authority="Rabban Gamliel",
                      machine_claim="LV06-01", **AR)]
        if q == "dislodged_limb":
            if case.get("item") == "disqualified_item":
                return [V("not_restored", "the stays-up class, once "
                          "dislodged, is not returned to the fire",
                          machine_claim="LV06-01", **AR)]
            m = case.get("moment")
            if m == "before_midnight":
                return [V("restore_with_sacrilege_liability", "fit limbs "
                          "dislodged before midnight are returned and "
                          "still carry sacrilege — the fire's claim runs "
                          "to midnight (Sifra Tzav Chapter 2 5)",
                          machine_claim="LV06-04", **AR)]
            if m == "after_midnight":
                return [V("not_restored", "after midnight the fire's "
                          "claim has lapsed", machine_claim="LV06-04",
                          **AR)]
        return None

    # ---------------------------------------------- washing / scouring
    WS = _LV("Mishnah Zevachim 11:1-11:8",
             "Lev.6.20 (lev_06_olah_minchah_torah, LV06-14 one law of "
             "washing; LV06-15 the washing machine; LV06-16 the vessel "
             "purge)")

    def rule_washing(case):
        q = case.get("query")
        if q == "garment_laundering" and case.get("offering") == "inner_chatat":
            return [V("requires_laundering", "'the law of the sin-"
                      "offering' — one law for eaten and inner burnt "
                      "alike (Sifra Tzav Section 4 1, the a-fortiori "
                      "defeated)", machine_claim="LV06-14", **WS)]
        if q == "purge_venue":
            return [V("sacred_place", "washing, breaking, scouring and "
                      "rinsing all happen in the holy place — the "
                      "juxtaposition extends the venue (Sifra Tzav "
                      "Chapter 6 7)", machine_claim="LV06-15", **WS)]
        if q == "scour_rinse_scope" and case.get("offering") == "lesser_sanctity":
            return [V("required", "cooked or poured, most-sacred or "
                      "lesser — scour and rinse", authority="tanna kamma",
                      machine_claim="LV06-16", **WS),
                    V("exempt", "R. Shimon exempts lesser sanctity — the "
                      "fit-phase criterion pair (Sifra Tzav Chapter 7 4)",
                      authority="R. Shimon", machine_claim="LV06-16",
                      **WS)]
        if q == "mixture_rule" and case.get("mixture") == "imparts_taste":
            return [V("eaten_as_stringent", "where the stringent imparts "
                      "taste the lenient is eaten under its stringencies "
                      "(Sifra Tzav Chapter 7 6)", machine_claim="LV06-16",
                      **WS)]
        return None

    # ------------------------------------------------------- chavitin
    CH = _LV("Mishnah Menachot 4:5, 6:5",
             "Lev.6.13 (lev_06_olah_minchah_torah, LV06-11 the halving "
             "invariant with its failure modes)")

    def rule_chavitin(case):
        q = case.get("query")
        if q == "chavitin_halves_from_house":
            return [V("barred_whole_divided", "'its half' means half of a "
                      "whole tenth — he brings a complete tenth and "
                      "divides it (Sifra Tzav Section 3 6)",
                      machine_claim="LV06-11", **CH)]
        if q == "chavitin_successor":
            return [V("new_whole_two_lost", "the replacement brings a new "
                      "whole and offers its half — two halves offered, "
                      "two lost (Sifra Tzav Section 3 8-9)",
                      machine_claim="LV06-11", **CH)]
        if q == "chavitin_no_successor":
            return [V("community_funds", "R. Shimon: from the community's "
                      "property ('a statute olam — from the olam')",
                      authority="R. Shimon", machine_claim="LV06-11",
                      **CH),
                    V("heirs_funds", "R. Yehuda: from the heirs' property "
                      "— the same recorded pair as Sifra Tzav Chapter 5 3",
                      authority="R. Yehuda", machine_claim="LV06-11",
                      **CH)]
        if q == "chavitin_loaf_count":
            return [V("twelve", "twelve loaves — the count is the data "
                      "channel's constant (with the show-bread, the two "
                      "exceptions to ten-per-tenth, Mishnah Menachot 6:5)",
                      machine_claim="LV06-11 (count as transmitted data)",
                      **CH)]
        return None

    # ---------------------------------------------------- todah loaves
    TL = _LV("Mishnah Menachot 5:1, 7:1, 7:3, 7:4; Temurah 3:2; "
             "Challah 1:6",
             "Lev.7.13 (lev_07_shelamim_types, LV07B-03 the forty-loaf "
             "compute; LV07B-04 the bread's commit point)")

    def rule_todah_loaves(case):
        q = case.get("query")
        if q == "todah_leavened_count":
            return [V("ten_of_forty", "ten leavened among the forty — the "
                      "extra yod's ten against the thirty matzah (Sifra "
                      "Tzav Section 7 8-9)", machine_claim="LV07B-03",
                      **TL)]
        if q == "todah_flour_total":
            return [V("twenty_tenths", "five Jerusalem se'im = six "
                      "wilderness se'im = two ephahs = twenty tenths: ten "
                      "leavened + ten matzah — the answer sheet running "
                      "the conversion layer itself",
                      machine_claim="LV07B-03", **TL)]
        if q == "loaf_consecration":
            ls = case.get("loaf_state")
            if ls in ("outside_wall", "pre_crust", "tereifah_found"):
                return [V("not_consecrated", "the bread consecrates only "
                          "crusted, inside the wall, by a valid slaughter "
                          "(Sifra Tzav Chapter 11 10)",
                          machine_claim="LV07B-04", **TL)]
            if ls == "blemish_found":
                return [V("consecrated", "R. Eliezer: the blemished, if "
                          "it ascended, is sacrificed — the ascend-not-"
                          "descend hinge consecrates",
                          authority="R. Eliezer",
                          machine_claim="LV07B-04", **TL),
                        V("not_consecrated", "the Rabbis: not sacrificed "
                          "ab initio — not consecrated",
                          authority="the Rabbis",
                          machine_claim="LV07B-04", **TL)]
        if q == "todah_offspring":
            return [V("sacrificed_without_loaves", "offspring, exchanges, "
                      "and substitutes to the end of time are like the "
                      "thanks offering — only without loaves (Sifra Tzav "
                      "Chapter 11 2 verbatim)", machine_claim="LV07B-04",
                      **TL)]
        if q == "todah_loaf_challah":
            if case.get("made_for") == "market_sale":
                return [V("liable", "made to sell in the market — subject "
                          "to the dough-gift; for oneself — exempt (the "
                          "consecration boundary)",
                          machine_claim="LV07B-04", **TL)]
        return None

    # ---------------------------------------------- minchah procedures
    MP = _LV("Mishnah Menachot 5:8, 6:4; Sotah 3:2, 3:7",
             "Lev.6.7 (lev_06_olah_minchah_torah, LV06-07 the corner "
             "algorithm; LV06-12 the folding spec; LV06-13 the priest's "
             "own minchah)")

    def rule_minchah_proc(case):
        q = case.get("query")
        if q == "pan_vow_substitution":
            return [V("barred", "a pan vow may not be discharged in the "
                      "deep pan nor the reverse — the vessel types are "
                      "distinct (Onkelos's two terms; the no-trades "
                      "lattice at the vow layer)",
                      machine_claim="LV07A-06", **MP)]
        if q == "folding_spec":
            off = case.get("offering")
            if off == "israelite_minchah":
                return [V("folded_and_separated", "one into two, two into "
                          "four, and separated (Sifra Tzav Chapter 4 6 "
                          "with the answer sheet's separation delta)",
                          machine_claim="LV06-12", **MP)]
            if off == "priest_minchah":
                return [V("folded_not_separated", "folded but not "
                          "separated — no fistful is taken",
                          machine_claim="LV06-12", **MP)]
        if q == "priest_minchah_eating":
            p = case.get("person")
            if p == "priest_daughter":
                return [V("eaten", "the priest's daughter's meal-offering "
                          "is eaten — the class boundary runs on the "
                          "priest (Sifra Tzav Chapter 5 4 verbatim)",
                          machine_claim="LV06-13", **MP)]
            if p == "priest":
                return [V("burned", "a priest's own meal-offering is "
                          "never eaten — wholly smoked",
                          machine_claim="LV06-13", **MP)]
        if q == "sotah_minchah_rite":
            return [V("waved_brought_near_southwest", "waved and brought "
                      "near at the southwest corner, the fistful taken — "
                      "the corner algorithm's resolution at the sotah's "
                      "seat (Sifra Tzav Section 2 4-5)",
                      machine_claim="LV06-07", **MP)]
        return None

    # ---------------------------------------------- eating windows
    EW = _LV("Mishnah Zevachim 5:6; Megillah 2:6; Nazir 4:4",
             "Lev.7.15 (lev_07_shelamim_types, LV07B-05 the windows with "
             "the midnight fence)")

    def rule_eating_windows(case):
        q = case.get("query")
        if q == "eating_window" and case.get("offering") == "todah":
            return [V("day_night_until_midnight", "one day and a night by "
                      "the ink; the sages' midnight — the self-labeled "
                      "fence in the answer sheet's own row (Sifra Tzav "
                      "Chapter 12 5)", machine_claim="LV07B-05", **EW)]
        if q == "fat_burning_window":
            return [V("all_night", "fats and limbs burn all night — the "
                      "night window (Sifra Tzav Chapter 1 13)",
                      machine_claim="LV06-01", **EW)]
        if q == "nullified_nazirite_shelamim":
            return [V("one_day_no_loaves", "her peace-offering is eaten "
                      "for one day and needs no loaves — the window and "
                      "the loaf rules riding a nullification case",
                      machine_claim="LV07B-05", **EW)]
        return None

    # ---------------------------------------------------- tumah karet
    TK = _LV("Mishnah Zevachim 13:2; Pesachim 9:4",
             "Lev.7.20 (lev_07_shelamim_types, LV07B-08 the sprinkling "
             "gate; LV07B-09 the body's tumah)")

    def rule_tumah_karet(case):
        if case.get("query") != "tamei_ate":
            return None
        fs = case.get("food_state")
        if fs == "pure_sacrificial":
            return [V("liable", "the impure person who ate pure "
                      "sacrificial food — karet (unwitting: the "
                      "sliding-scale offering)", machine_claim="LV07B-08",
                      **TK)]
        if fs == "impure_sacrificial":
            return [V("liable", "the Rabbis: even impure food — liable",
                      authority="the Rabbis", machine_claim="LV07B-08",
                      **TK),
                    V("exempt", "R. Yosei Haglili: he merely ate an "
                      "impure item — the ban rides pure food",
                      authority="R. Yosei Haglili",
                      machine_claim="LV07B-08", **TK)]
        if fs == "slaughtered_for_unclean":
            return [V("exempt", "what was slaughtered for the unclean "
                      "(the congregational-tumah Pesach) carries no karet "
                      "for its unclean eaters (Sifra Tzav Chapter 14 1)",
                      machine_claim="LV07B-08", **TK)]
        return None

    # ------------------------------------------------- dues and gifts
    DG = _LV("Mishnah Zevachim 12:1, 12:2; Chullin 10:1, 10:4; "
             "Sukkah 5:7",
             "Lev.7.33 (lev_07_fat_blood_dues, LV07C-06 the dues' gates; "
             "lev_07_asham_procedure, LV07A-05 hide follows flesh)")

    def rule_dues(case):
        q = case.get("query")
        if q == "dues_share" and case.get("priest_state") == "tvul_yom":
            return [V("no_share", "the day-immersed and the atonement-"
                      "lacking do not share for the evening — the Sifra's "
                      "dialogue as a rule row (Sifra Tzav Chapter 17)",
                      machine_claim="LV07C-06", **DG)]
        if q == "hide_acquisition":
            st = case.get("offering_state")
            if st == "disqualified_before_sprinkling":
                return [V("priests_no_hide", "no altar acquisition of the "
                          "flesh, no priestly acquisition of the hide "
                          "('a MAN's olah')", machine_claim="LV07A-05",
                          **DG)]
            if st == "not_for_its_sake":
                return [V("priests_acquire_hide", "the unaccredited olah "
                          "still yields its hide to the priests (Sifra "
                          "Tzav Chapter 9 2 verbatim)",
                          machine_claim="LV07A-05", **DG)]
        if q == "foreleg_jaw_maw":
            ac = case.get("animal_class")
            if ac == "sacrificial":
                return [V("exempt_chullin_only", "the gifts ride mundane "
                          "animals only — the a-fortiori refuted from "
                          "'and I have GIVEN them' (Sifra Tzav Chapter "
                          "17 6)", machine_claim="LV07C-06", **DG)]
            if ac == "convert_uncertain":
                return [V("exempt_burden_of_proof", "uncertain whether "
                          "slaughtered before the conversion — exempt: "
                          "the burden of proof rests on the claimant",
                          machine_claim="LV07C-06", **DG)]
        if q == "festival_watch_shares":
            return [V("all_watches_equal", "at the three festivals all "
                      "twenty-four watches share equally in the offerings "
                      "and the show-bread — the calendar exception to the "
                      "household apportionment",
                      machine_claim="LV07A-06", **DG)]
        return None

    # ------------------------------------------------------ fat blood
    FB = _LV("Mishnah Chullin 8:6; Keritot 5:1",
             "Lev.7.23 (lev_07_fat_blood_dues, LV07C-01 the fat ban's "
             "scope; LV07C-02 the inversion; LV07C-04 the blood's "
             "species test)")

    def rule_fat_blood(case):
        q = case.get("query")
        if q == "fat_vs_blood":
            d = case.get("dimension_asked")
            if d == "meilah_piggul_notar_tamei":
                return [V("fat_only", "sacrilege, rejection, leftover, "
                          "and impurity apply to the fat of offerings and "
                          "not to the blood — the blood's exception "
                          "register (Sifra Tzav Chapter 15 6)",
                          machine_claim="LV07C-02", **FB)]
            if d == "species_breadth":
                return [V("blood_all_species", "the blood ban covers "
                          "beast, animal, and bird alike; the fat ban "
                          "rides ox, sheep, and goat only (Sifra Tzav "
                          "Section 10 2-3)", machine_claim="LV07C-01",
                          **FB)]
        if q == "blood_karet":
            src = case.get("blood_source")
            if src == "lifeblood":
                return [V("liable", "the blood with which the soul "
                          "departs — karet at an olive-bulk",
                          machine_claim="LV07C-04", **FB)]
            if src == "spleen_heart_eggs":
                return [V("exempt", "organ blood and the excluded "
                          "species' bloods — outside the karet (Sifra "
                          "Tzav Section 10 11's exclusion list)",
                          machine_claim="LV07C-04", **FB)]
        return None

    # -------------------------------------------------- perpetual fire
    PF = _LV("Mishnah Yoma 4:6; Tamid 1:4; Pesachim 5:1, 6:1",
             "Lev.6.5 (lev_06_olah_minchah_torah, LV06-06 the perpetual "
             "fire machine; LV06-04 the ash protocol)")

    def rule_perpetual_fire(case):
        q = case.get("query")
        if q == "wood_pile_count":
            return [V("two_daily", "R. Yehuda: two piles daily, three on "
                      "Yom Kippur", authority="R. Yehuda",
                      machine_claim="LV06-06", **PF),
                    V("three_daily", "R. Yosei: three daily, four on Yom "
                      "Kippur", authority="R. Yosei",
                      machine_claim="LV06-06", **PF),
                    V("four_daily", "R. Meir: four daily, five on Yom "
                      "Kippur — the same three names as Sifra Tzav "
                      "Chapter 2 11", authority="R. Meir",
                      machine_claim="LV06-06", **PF)]
        if q == "ash_removal_gate":
            return [V("sanctify_hands_feet_first", "no service before "
                      "laving hands and feet from the basin — the gate "
                      "on the ash rite", machine_claim="LV06-04", **PF)]
        if q == "afternoon_tamid_schedule":
            return [V("slaughtered_8_5_offered_9_5", "slaughtered at "
                      "eight and a half hours, offered at nine and a "
                      "half — the day bracket's afternoon anchor "
                      "(earlier on Passover eves)",
                      machine_claim="LV06-06", **PF)]
        if q == "pesach_shabbat_override":
            s = case.get("service")
            if s == "slaughter_sprinkle_fats":
                return [V("overrides", "the day-bound services override "
                          "Shabbat — the continuous-service logic at the "
                          "Pesach seat", machine_claim="LV06-06", **PF)]
            if s == "roasting_washing":
                return [V("does_not_override", "what need not happen by "
                          "day waits for the night",
                          machine_claim="LV06-06", **PF)]
        return None

    # ------------------------------------------------ corner and north
    CN = _LV("Mishnah Zevachim 6:1, 6:2, 6:5",
             "Lev.6.18 (lev_06_olah_minchah_torah, LV06-14 the north; "
             "LV06-07 the corner algorithm)")

    def rule_corner(case):
        q = case.get("query")
        if q == "slaughter_atop_altar":
            return [V("as_north", "R. Yosei: the altar's top counts as "
                      "the north", authority="R. Yosei",
                      machine_claim="LV06-14", **CN),
                    V("half_north_half_south", "R. Yosei b. R. Yehuda: "
                      "only the northern half counts",
                      authority="R. Yosei b. R. Yehuda",
                      machine_claim="LV06-14", **CN)]
        if q == "bird_rite_corner":
            off = case.get("offering")
            if off == "bird_chatat":
                return [V("southwest", "the bird sin-offering at the "
                          "southwest corner — the minchah's own corner "
                          "(Sifra Tzav Section 2 4's resolution)",
                          machine_claim="LV06-07", **CN)]
            if off == "bird_olah":
                return [V("southeast", "the bird burnt-offering at the "
                          "southeast horn", machine_claim="LV06-07",
                          **CN)]
        return None

    # ---------------------------------------------- installation week
    IW = _LV("Mishnah Yoma 1:1; Menachot 7:2, 3:6",
             "Lev.8.33 (lev_08_milluim, LV08-06 the atomic transaction; "
             "LV08-07 the calendar; LV08-08 the separation template)")

    def rule_installation(case):
        q = case.get("query")
        if q == "yom_kippur_hp_preparation":
            return [V("seven_days_separated", "seven days before Yom "
                      "Kippur the high priest is separated to the "
                      "Parhedrin chamber with a substitute appointed — "
                      "the milluim week instantiated (Sifra Tzav "
                      "Mekhilta DeMiluim I 37, 'as He has done this "
                      "day')", machine_claim="LV08-08", **IW)]
        if q == "milluim_loaf_kinds":
            return [V("three_matzah_kinds_no_leaven", "the installation "
                      "loaves parallel the thanksgiving's three matzah "
                      "kinds without the leavened bread (Lev 8:26 in the "
                      "answer sheet's own citation)",
                      machine_claim="LV08-06", **IW)]
        if q == "paired_components":
            return [V("each_prevents_the_other", "the paired components "
                      "(the two goats, the two lambs, the two loaves, "
                      "the arrangements) each prevent the other — the "
                      "atomicity frame (the milluim's bullock-rams-"
                      "basket rule at the answer sheet's scale)",
                      machine_claim="LV08-06", **IW)]
        return None

    # ------------------------------------------- yotzei and mixtures
    YM = _LV("Mishnah Pesachim 3:8; Zevachim 8:11",
             "Lev.6.23 (lev_06_olah_minchah_torah, LV06-17 the entry "
             "boundary; LV06-15 the return table)")

    def rule_yotzei(case):
        q = case.get("query")
        if q == "meat_left_city":
            m = case.get("moment")
            if m == "past_scopus":
                return [V("burn_in_place", "past Mount Scopus — burn "
                          "where he stands", machine_claim="LV06-15",
                          **YM)]
            if m == "before_scopus":
                return [V("return_and_burn", "not yet past Scopus — "
                          "return and burn before the Temple: the return "
                          "table at city scale (Sifra Tzav Chapter 6 8's "
                          "pattern)", machine_claim="LV06-15", **YM)]
        if q == "inner_outer_blood_mix":
            return [V("poured_to_drain", "inner-blood mixed with "
                      "outer-blood is poured to the courtyard drain — "
                      "the entry boundary's mixture rule (Sifra Tzav "
                      "Chapter 8 2's two-cups table beside it)",
                      machine_claim="LV06-17", **YM)]
        return None

    # ------------------------------------------------------ bamah eras
    BE = _LV("Mishnah Zevachim 14:4, 14:10",
             "Lev.7.37 (lev_07_fat_blood_dues, LV07C-07 the Sinai "
             "colophon with R. Shimon's firstborn timeline)")

    def rule_bamah(case):
        q = case.get("query")
        if q == "pre_tabernacle_service":
            return [V("firstborn_officiated", "until the tabernacle "
                      "stood, the bamot were permitted and the FIRSTBORN "
                      "served — R. Shimon's timeline in the answer sheet "
                      "(Sifra Tzav Chapter 18 2: the dues stood with the "
                      "firstborn from Sinai until the anointment)",
                      machine_claim="LV07C-07", **BE)]
        if q == "bamah_offering_scope":
            oc = case.get("offering_class")
            if oc == "communal":
                return [V("tabernacle_only", "communal offerings ride "
                          "the tabernacle only",
                          machine_claim="LV07C-07", **BE)]
            if oc == "individual":
                return [V("bamah_valid", "an individual's offerings are "
                          "valid on a private altar (no waving, no dues "
                          "there)", machine_claim="LV07C-07", **BE)]
        return None

    return {
        "wrong_intent_tzav": {"fn": rule_wrong_intent},
        "piggul_scope": {"fn": rule_piggul},
        "altar_retention": {"fn": rule_altar_retention},
        "washing_scouring": {"fn": rule_washing},
        "chavitin": {"fn": rule_chavitin},
        "todah_loaves": {"fn": rule_todah_loaves},
        "minchah_procedures": {"fn": rule_minchah_proc},
        "eating_windows_tzav": {"fn": rule_eating_windows},
        "tumah_karet_tzav": {"fn": rule_tumah_karet},
        "dues_and_gifts": {"fn": rule_dues},
        "fat_blood": {"fn": rule_fat_blood},
        "perpetual_fire": {"fn": rule_perpetual_fire},
        "corner_and_north": {"fn": rule_corner},
        "installation_week": {"fn": rule_installation},
        "yotzei_and_mixtures": {"fn": rule_yotzei},
        "bamah_eras": {"fn": rule_bamah},
    }
