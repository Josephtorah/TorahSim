#!/usr/bin/env python3
"""backfill_rules.py — the Exodus 1-21 backfill exam's rule modules
(2026-09-01, owner: "lets run step 9 on exodus 1 - 21 again").

Part I: 25 modules on Exod 1-20 anchors (provenance mishnah +
exodus_anchor — the FWD-era units' new EXnn-14+ seats). Part II: 8
modules re-checking chapter 21 against the law-era claims (provenance
carries law_claims from manifests law01/law02/law03).

engine.py calls build(V) at its tail and merges the returned registry —
no circular import; V is engine's verdict constructor."""


def build(V):
    def _BF(mishnah, anchor, **extra):
        d = dict(mishnah=mishnah, exodus_anchor=anchor)
        d.update(extra)
        return d

    def _L21(mishnah, law, **extra):
        d = dict(mishnah=mishnah, law_claims=law,
                 exodus_anchor="Exod.21 (exo_21_the_ordinances + law-era "
                               "manifests law01/law02/law03)")
        d.update(extra)
        return d

    # ------------------------------------------------ Part I
    OFFER = _BF("Mishnah Pesachim 5:2 + 5:3 + 5:5 + 7:4; Kiddushin 2:1",
                "Exod.12.4-6+27 (exo_12, EX12-17)")

    def rule_passover_offering(case):
        q = case.get("query")
        if q == "offering_validity":
            if case.get("intent") == "not_for_its_name":
                return [V("invalid", "zevach pesach HU — its name is part "
                          "of the act (12:27)", machine_claim="EX12-17",
                          **OFFER)]
            if case.get("slaughtered_for") == "non_eaters_only":
                return [V("invalid", "le-fi okhlo — appointed by its "
                          "eaters (12:4)", machine_claim="EX12-17",
                          **OFFER)]
            if case.get("slaughtered_for") == "eaters_and_non":
                return [V("valid", "for eaters AND non-eaters — the "
                          "eater-clause is satisfied", **OFFER)]
            if case.get("slaughter_time") == "before_midday":
                return [V("invalid", "bein ha-arbayim — the window opens "
                          "at noon's decline (12:6)",
                          machine_claim="EX12-17", **OFFER)]
        if q == "slaughter_cohorts":
            return [V("three_cohorts", "kahal, edah, yisrael — three "
                      "nouns in 12:6, three cohorts (the ink-census)",
                      machine_claim="EX12-17", **OFFER)]
        if q == "communal_impurity" and case.get("offering") == "pesach":
            return [V("eaten_in_impurity", "it came from its start only "
                      "for eating (12:4)", **OFFER)]
        if q == "agency_source":
            return [V("agent_as_principal", "the whole assembly "
                      "slaughters and one slaughters — shlucho shel adam "
                      "kemoto (Kiddushin 41b on 12:6)",
                      machine_claim="EX12-17", **OFFER)]
        return None

    EAT = _BF("Mishnah Pesachim 2:8 + 7:1 + 10:9; Beitzah 2:7; "
              "Makkot 3:3", "Exod.12.8-10+46 (exo_12, EX12-18)")

    def rule_passover_eating(case):
        q = case.get("query")
        if q == "preparation_mode":
            if case.get("medium") == "fruit_juice":
                return [V("forbidden_as_cooked", "not in water and not "
                          "in ANY liquid — roast of fire only (12:9)",
                          machine_claim="EX12-18", **EAT)]
            if case.get("part") == "innards":
                return [V("inside_it", "R. Yose the Galilean — spitted "
                          "within", authority="R. Yose the Galilean",
                          **EAT),
                        V("hung_outside", "that is cooking from within",
                          authority="R. Akiva", **EAT)]
        if q == "imitation_offering":
            return [V("permitted", "the house of Rabban Gamliel made the "
                      "helmeted kid", authority="Rabban Gamliel", **EAT),
                    V("forbidden", "looks like eating an offering "
                      "outside", authority="the sages", **EAT)]
        if q == "bone_or_leftover":
            if case.get("act") == "broke_bone" and \
               case.get("state") == "pure":
                return [V("lashes_forty", "the bone-ban of 12:46 — held "
                          "as text in the unit; the impure offering "
                          "outside it", machine_claim="EX12-18 (the unit "
                          "holds the one-house clause as text)", **EAT)]
            if case.get("act") == "left_over" and \
               case.get("state") == "pure":
                return [V("no_lashes", "the leftover ban is repaired by "
                          "its own burn-command (12:10)",
                          machine_claim="EX12-18", **EAT)]
        if q == "eating_window":
            return [V("until_midnight_defiles_after", "after midnight it "
                      "is leftover and defiles the hands (10:9 on 12:8)",
                      **EAT)]
        return None

    LEAVEN = _BF("Mishnah Pesachim 1:1 + 2:2 + 3:3 + 9:3; Beitzah 1:1; "
                 "Makkot 3:2", "Exod.12.15+19 (exo_12, EX12-19)")

    def rule_leaven_ban(case):
        q = case.get("query")
        if q == "leaven_duty":
            if case.get("act") == "search_by_lamp":
                return [V("eve_of_fourteenth", "or le-arbaa asar — the "
                          "search implements lo yimatze (12:19)",
                          machine_claim="EX12-19 (the frontier debt "
                          "paid)", **LEAVEN)]
            if case.get("occasion") == "second_pesach":
                return [V("leaven_with_him_permitted", "the second — "
                          "matzah and leaven with him in the house "
                          "(Pesachim 9:3)", **LEAVEN)]
        if q == "leaven_after_pesach":
            o = case.get("owner")
            if o == "gentile":
                return [V("permitted", "lekha — yours, not another's "
                          "(13:7)", machine_claim="EX12-19", **LEAVEN)]
            if o == "israelite":
                return [V("forbidden", "lo yerae LEKHA seor — his own "
                          "violates the ban", machine_claim="EX12-19",
                          **LEAVEN)]
        if q == "leaven_measure":
            return [V("two_measures", "seor an olive's bulk, chametz a "
                      "date's bulk", authority="Beit Shammai", **LEAVEN),
                    V("olive_for_both", "this and that at an olive's "
                      "bulk", authority="Beit Hillel", **LEAVEN)]
        if q == "leaven_penalty" and case.get("act") == "ate_on_pesach":
            return [V("lashes_forty", "the eater of leaven on Passover "
                      "in the lash list (12:15)",
                      machine_claim="EX12-19", **LEAVEN)]
        return None

    SEDER = _BF("Mishnah Pesachim 10:5 + 2:5",
                "Exod.12.27+39 (exo_12, EX12-20)")

    def rule_seder_duties(case):
        q = case.get("query")
        if q == "seder_census":
            return [V("pesach_matzah_maror", "three duties, three "
                      "verse-reasons: passed-over (12:27), no time to "
                      "leaven (12:39), they embittered (1:14); the "
                      "telling at 13:8", machine_claim="EX12-20 + "
                      "EX01-14", **SEDER)]
        if q == "matzah_species":
            return [V("five_grains_only", "wheat, barley, spelt, rye, "
                      "oats — the species that leaven", **SEDER)]
        return None

    ERA = _BF("Mishnah Pesachim 9:5", "Exod.12.3+11+22 (exo_12, EX12-21)")

    def rule_egypt_vs_generations(case):
        if case.get("query") == "era_delta" and \
           case.get("statute") == "pesach":
            return [V("three_egypt_only_clauses", "taken from the tenth "
                      "(12:3); hyssop on lintel and posts (12:22); one "
                      "night in haste (12:11) — the generations' runs "
                      "seven days", machine_claim="EX12-21 (the two-era "
                      "table)", **ERA)]
        return None

    CAL = _BF("Mishnah Rosh Hashanah 1:7 + 3:1; Pesachim 4:9",
              "Exod.12.1-2 (exo_12, EX12-22)")

    def rule_calendar_court(case):
        q = case.get("query")
        if q == "month_sanctification" and \
           case.get("seen_by") == "court_itself":
            return [V("two_testify_before_rest", "even the seeing court "
                      "needs testimony-form — mekudash mekudash; the "
                      "individual is not trusted by himself",
                      machine_claim="EX12-22", **CAL)]
        if q == "month_witness" and \
           case.get("relation") == "father_and_son":
            return [V("both_go_join_others", "they go; each may join "
                      "with another", authority="the first teaching",
                      **CAL),
                    V("relatives_valid", "all relatives valid for "
                      "month-testimony", authority="R. Shimon", **CAL)]
        if q == "intercalation" and \
           case.get("month") == "nisan_in_nisan":
            return [V("not_approved", "ha-chodesh ha-ZE — one declared "
                      "head, not revisable (Hezekiah's un-approved "
                      "deed)", machine_claim="EX12-22", **CAL)]
        return None

    FBA = _BF("Mishnah Bekhorot 1:2 + 1:7 + 2:6 + 2:9; Avodah Zarah 5:9",
              "Exod.13.12-13 (exo_13, EX13-14)")

    def rule_firstborn_animal(case):
        q = case.get("query")
        if q == "donkey_firstling" and case.get("bearer") == "donkey" \
           and case.get("born") == "horse_like":
            return [V("exempt", "peter chamor said TWICE — until bearer "
                      "and born are both donkeys",
                      machine_claim="EX13-14 (the doubled-token "
                      "census)", **FBA)]
        if q == "duty_precedence" and \
           case.get("pair") == "redeem_vs_break_neck":
            return [V("redemption_first", "the clause order of 13:13 — "
                      "redeem; if not, break", machine_claim="EX13-14",
                      **FBA)]
        if q == "firstling_assignment":
            b = case.get("birth")
            if b == "two_males_together":
                return [V("both_to_priest", "ha-zekharim la-YHWH — the "
                          "plural", authority="R. Yose the Galilean",
                          **FBA),
                        V("one_to_priest", "impossible that both opened "
                          "the womb", authority="the sages", **FBA)]
            if b == "caesarean_and_next":
                return [V("neither_firstling", "the first no "
                          "womb-opener; the second preceded",
                          authority="R. Akiva", **FBA),
                        V("both_graze", "both graze until blemished",
                          authority="R. Tarfon", **FBA)]
        if q == "prohibition_class" and \
           case.get("item") == "donkey_firstling":
            return [V("forbids_any_amount", "in the asurin ve-osrin "
                      "be-khol she-hen class", **FBA)]
        return None

    FBH = _BF("Mishnah Bekhorot 8:1", "Exod.13.2 (exo_13, EX13-14)")

    def rule_firstborn_human(case):
        if case.get("query") == "firstborn_tracks" and \
           case.get("born_after") == "stillbirth":
            return [V("inheritance_not_priest", "the father-line track "
                      "holds, the womb was opened — peter kol rechem "
                      "bi-vne yisrael read to the mother",
                      machine_claim="EX13-14 (the dual track)", **FBH)]
        return None

    TEF = _BF("Mishnah Megillah 4:8; Sanhedrin 11:3",
              "Exod.13.9+16 (exo_13, EX13-15)")

    def rule_tefillin_form(case):
        if case.get("query") != "tefillin_form":
            return None
        if case.get("shape") == "round":
            return [V("danger_no_mitzvah", "sakana ve-en ba mitzvah",
                      machine_claim="EX13-15", **TEF)]
        if case.get("placement") == "forehead_or_palm":
            return [V("sectarian_way", "derekh ha-minut — against the "
                      "received placement (the weak arm, above the "
                      "hairline)", machine_claim="EX13-15 (beside the "
                      "EX13-04 crown)", **TEF)]
        if case.get("compartments") == "five":
            return [V("liable_adds_to_scribes", "chomer be-divre sofrim "
                      "— four is the received datum on totafot",
                      machine_claim="EX13-15", **TEF)]
        return None

    BOUND = _BF("Mishnah Eruvin 4:5; Shabbat 1:1 + 24:1; Horayot 1:3",
                "Exod.16.29 (exo_16, EX16-14 beside the EX16-10 crown)")

    def rule_sabbath_boundary(case):
        q = case.get("query")
        if q == "boundary_allowance" and \
           case.get("situation") == "asleep_at_nightfall":
            return [V("two_thousand_cubits", "alpayim ammah in every "
                      "direction", authority="R. Yochanan ben Nuri",
                      **BOUND),
                    V("four_cubits", "he has only four",
                      authority="the sages", **BOUND)]
        if q == "carrying_liability":
            if case.get("lifted") == "poor_man" and \
               case.get("placed") == "poor_man":
                return [V("poor_man_liable", "one person did both lift "
                          "and place — the two-that-are-four grid",
                          machine_claim="EX16-14", **BOUND)]
        if q == "court_error" and case.get("scope") == "carrying_only":
            return [V("liable", "there IS Sabbath but carrying exempt — "
                      "a matter, not the whole body (the carrying law's "
                      "seat at 16:29 presumed)",
                      machine_claim="EX16-14 + EX16-10", **BOUND)]
        if q == "rest_roster" and case.get("actor") == "gentile":
            return [V("outside_the_list", "the purse goes to the "
                      "gentile — outside 20:10's rest roster; the "
                      "donkey is IN it", machine_claim="EX20-16",
                      **BOUND)]
        return None

    CHAL = _BF("Mishnah Eduyot 1:2", "Exod.16.16 (exo_16, EX16-15)")

    def rule_challah_measure(case):
        if case.get("query") == "challah_threshold":
            return [V("kav_and_half", "the omer-per-head of 16:16 in "
                      "kav — Shammai one kav and Hillel two flank the "
                      "sages' figure", machine_claim="EX16-15", **CHAL)]
        return None

    TIERS = _BF("Mishnah Sanhedrin 1:5 + 4:1 + 4:2",
                "Exod.18.22 (exo_18, EX18-14 beside the EX18-13 routing)")

    def rule_court_tiers(case):
        q = case.get("query")
        if q == "court_size":
            ct = case.get("case_type")
            if ct == "tribe_or_high_priest":
                return [V("seventy_one", "the great-matter docket: "
                          "tribe, false prophet, high priest, wars of "
                          "choice", machine_claim="EX18-14", **TIERS)]
            if ct == "capital":
                return [V("twenty_three", "dine nefashot be-esrim "
                          "u-shlosha", machine_claim="EX18-14 (beside "
                          "the Mishpatim court_architecture holdings)",
                          **TIERS)]
        if q == "court_composition" and \
           case.get("case_type") == "capital":
            return [V("priests_levites_marriageable", "capital opens "
                      "from the side; only the marriageable seat",
                      machine_claim="EX18-14", **TIERS)]
        return None

    PLOT = _BF("Mishnah Makkot 1:2 + 1:3 + 1:6",
               "Exod.20.13 (exo_20, EX20-14) + Exod.21.23 (EX21-14)")

    def rule_plotting_witnesses(case):
        q = case.get("query")
        if q == "plotting_penalty":
            t = case.get("testified")
            if t == "money_debt":
                return [V("pay_not_lash", "kol ha-meshalem eino loke — "
                          "the sages against R. Meir's pay-and-lash",
                          machine_claim="EX20-14", **PLOT)]
            if t == "lashes":
                return [V("eighty", "one forty for lo taane, one for "
                          "as-he-plotted", authority="R. Meir", **PLOT),
                        V("forty", "one liability only",
                          authority="the sages", **PLOT)]
        if q == "plotting_timing":
            return [V("after_verdict_before_execution", "nefesh tachat "
                      "nefesh (21:23) — the verdict stands and the "
                      "brother is still alive", machine_claim="EX21-14",
                      **PLOT)]
        return None

    EQW = _BF("Mishnah Keritot 6:9", "Exod.20.12 (exo_20, EX20-15)")

    def rule_equal_weight(case):
        if case.get("query") == "honor_weight" and \
           case.get("pair") == "father_vs_mother":
            return [V("both_equal", "ish imo ve-aviv tirau reverses our "
                      "verse's order — both equal; the collision "
                      "tiebreak administrative",
                      machine_claim="EX20-15", **EQW)]
        return None

    ALTAR = _BF("Mishnah Middot 3:4; Chagigah 3:8",
                "Exod.20.21-22 (exo_20, EX20-12 + EX20-16)")

    def rule_altar_stones(case):
        q = case.get("query")
        if q == "altar_stone_fitness" and \
           case.get("touched_by") == "iron":
            return [V("invalidated", "the sword-profanes clause — the "
                      "shortener not waved over the lengthener",
                      machine_claim="EX20-12 (held before the exam)",
                      **ALTAR)]
        if q == "altar_immersion":
            return [V("like_ground", "the earthen altar of 20:21 — "
                      "ground-status", authority="R. Eliezer", **ALTAR),
                    V("because_plated", "they are plated",
                      authority="the sages", **ALTAR)]
        return None

    SINP = _BF("Mishnah Shabbat 9:3", "Exod.19.15 (exo_19, EX19-14)")

    def rule_sinai_purity(case):
        if case.get("query") == "emission_viability":
            return [V("impure_on_third_day", "heyu nekhonim li-shloshet "
                      "yamim — the readiness interval as the standing "
                      "window", machine_claim="EX19-14", **SINP)]
        return None

    SONG = _BF("Mishnah Sotah 5:4", "Exod.15.1 (exo_15, EX15-14)")

    def rule_song_performance(case):
        if case.get("query") == "song_mode":
            return [V("like_hallel", "answering after Moses phrase by "
                      "phrase — the doubled saying-token",
                      authority="R. Akiva", **SONG),
                    V("like_shema", "together after the opening",
                      authority="R. Nechemiah", **SONG)]
        return None

    INC = _BF("Mishnah Sanhedrin 10:1", "Exod.15.26 (exo_15, EX15-15)")

    def rule_incantation_ban(case):
        if case.get("query") == "verse_as_incantation":
            return [V("no_share_next_world", "R. Akiva's row — the "
                      "healing verse whispered over a wound",
                      machine_claim="EX15-15", **INC)]
        return None

    DISC = _BF("Mishnah Rosh Hashanah 3:8", "Exod.17.11 (exo_17, EX17-14)")

    def rule_public_discharge(case):
        q = case.get("query")
        if q == "hands_reading":
            return [V("instrument_not_cause", "while Israel looked "
                      "upward and subjected their heart they prevailed "
                      "(the Num 21 serpent its pair)",
                      machine_claim="EX17-14", **DISC)]
        if q == "discharge_capacity" and case.get("actor") == "minor":
            return [V("cannot_discharge", "whoever is not obligated "
                      "cannot discharge the many",
                      machine_claim="EX17-14", **DISC)]
        return None

    CEN = _BF("Pirkei Avot 5:4 + 5:6", "Exod.11.1 (exo_11, EX11-14)")

    def rule_census_tables(case):
        q = case.get("query")
        if q == "plague_census":
            return [V("ten_in_egypt_ten_at_sea", "od nega ECHAD "
                      "presupposes nine — the canonical table closes "
                      "the count", machine_claim="EX11-14 (the frontier "
                      "slot paid)", **CEN)]
        if q == "twilight_census" and case.get("member") == "manna":
            return [V("created_at_twilight", "the ten twilight-things "
                      "include the manna — the table gen_22 witnesses "
                      "for the rainbow (G22-09)",
                      machine_claim="EX16-15", **CEN)]
        return None

    DECA = _BF("Mishnah Tamid 5:1; Pirkei Avot 3:6",
               "Exod.20.2+21 (exo_20, EX20-16)")

    def rule_decalogue_standing(case):
        q = case.get("query")
        if q == "decalogue_liturgy":
            return [V("read_daily_in_temple", "the officer said: read "
                      "the ten utterances, with the Shema",
                      machine_claim="EX20-16", **DECA)]
        if q == "presence_quorum" and case.get("count") == "one":
            return [V("presence_rests", "be-khol ha-makom asher azkir "
                      "et shemi — the single student's warrant",
                      machine_claim="EX20-16", **DECA)]
        return None

    DOC = _BF("Mishnah Yadayim 4:8", "Exod.5.2 (exo_05, EX05-14)")

    def rule_document_precedent(case):
        if case.get("query") == "document_form" and \
           case.get("element") == "ruler_with_name":
            return [V("ruler_below_name", "Pharaoh wrote himself above "
                      "at 5:2 and confessed below at 9:27 — the "
                      "Pharisees' retort", machine_claim="EX05-14",
                      **DOC)]
        return None

    CIRC = _BF("Mishnah Nedarim 3:11 (R. Yehoshua ben Korcha)",
               "Exod.4.24-26 (exo_04, EX04-14)")

    def rule_circumcision_priority(case):
        if case.get("query") == "circumcision_delay":
            return [V("not_even_an_hour", "righteous Moses not "
                      "suspended over it a full hour — the lodging "
                      "episode as law", machine_claim="EX04-14",
                      **CIRC)]
        return None

    GOOD = _BF("Mishnah Sotah 1:9", "Exod.2.4 (exo_02, EX02-14)")

    def rule_good_measure(case):
        if case.get("query") == "measure_for_measure" and \
           case.get("direction") == "good":
            a = case.get("actor")
            if a == "miriam":
                return [V("waited_seven_days", "she stationed herself "
                          "one hour — Israel waited seven days for her "
                          "(Num 12:15)", machine_claim="EX02-14",
                          **GOOD)]
            if a == "moses":
                return [V("attended_by_the_presence", "he merited "
                          "Joseph's bones (13:19) — none greater dealt "
                          "with his own burial",
                          machine_claim="EX02-14 (riding EX13-01's "
                          "marquee)", **GOOD)]
        return None

    MAROR = _BF("Mishnah Pesachim 10:5 (the maror clause)",
                "Exod.1.14 (exo_01, EX01-14)")

    def rule_maror_reason(case):
        if case.get("query") == "duty_reason" and \
           case.get("duty") == "maror":
            return [V("they_embittered", "va-yemareru et chayehem — the "
                      "bitter herb's warrant is 1:14's own verb",
                      machine_claim="EX01-14", **MAROR)]
        return None

    # ------------------------------------------------ Part II
    SLAVE = _L21("Mishnah Kiddushin 1:2 + 3:12; Yevamot 2:5; "
                 "Bekhorot 1:7",
                 ["L2-01", "L2-03", "L2-05", "L4-02", "L5-01", "L6-01",
                  "L8-01", "L8-02", "L11-02", "L11-03"])

    def rule_slave_acquisition(case):
        q = case.get("query")
        if q == "slave_acquisition_modes":
            return [V("money_or_document", "eved ivri nikne be-khesef "
                      "u-vi-shtar (L2-01's entry paths behind it)",
                      **SLAVE)]
        if q == "slave_exit_events":
            return [V("years_yovel_deduction", "six years, the yovel, "
                      "prorated redemption; the amah adds signs — MIN "
                      "over exit events (L11-03)", **SLAVE)]
        if q == "pierced_exit":
            return [V("yovel_or_masters_death", "ha-nirtza nikne "
                      "bi-retziah ve-kone atzmo ba-yovel u-ve-mitat "
                      "ha-adon (L6's lock)", **SLAVE)]
        if q == "duty_precedence" and \
           case.get("pair") == "designate_vs_redeem":
            return [V("designation_first", "asher lo yeadah ve-hefdah — "
                      "designation is the verse's first option "
                      "(L8-01/02)", **SLAVE)]
        if q == "child_status" and case.get("mother") == "slave_woman":
            return [V("follows_mother", "ha-isha vi-ladeha tihye "
                      "la-adoneha — the matrilineal rule (L4-02)",
                      **SLAVE)]
        if q == "levirate_tie" and \
           case.get("brother_from") == "slave_woman":
            return [V("no_tie", "no brother for levirate — L4-02's "
                      "kinship consequence", **SLAVE)]
        return None

    ONAH = _L21("Mishnah Ketubot 5:6; Eduyot 4:10",
                ["L10-01", "L10-02"])

    def rule_onah_duty(case):
        q = case.get("query")
        if q == "intimacy_vow_limit":
            return [V("two_weeks", "shte shabatot",
                      authority="Beit Shammai", **ONAH),
                    V("one_week", "shabat achat",
                      authority="Beit Hillel", **ONAH)]
        if q == "onah_schedule" and \
           case.get("occupation") == "sailors":
            return [V("once_six_months", "the tannaitic quantification "
                      "of the triad's third field (L10-01)", **ONAH)]
        return None

    GORE = _L21("Mishnah Bava Kamma 1:4 + 3:8 + 3:9 + 4:3 + 4:9 + 5:7",
                ["L29-01", "L29-05", "L35-01", "L35-03", "L36-01",
                 "L36-02"])

    def rule_goring_liability(case):
        q = case.get("query")
        if q == "goring_payment":
            st = case.get("state")
            if case.get("victim_owner") == "temple":
                return [V("exempt", "shor REEHU — not the Temple's "
                          "(L36-02)", **GORE)]
            if st == "muad" and case.get("guarded") == "adequately":
                return [V("exempt", "ve-lo yishmerennu — and this one "
                          "WAS guarded (L29-05)",
                          authority="R. Yehudah", **GORE),
                        V("liable", "no guarding suffices but the "
                          "knife", authority="R. Eliezer", **GORE)]
            if st == "tam":
                return [V("half_from_body", "chatzi nezek mi-gufo "
                          "(L29-01/L35-03)", **GORE)]
            if st == "muad":
                return [V("full_from_estate", "nezek shalem min "
                          "ha-aliyah (L36-01)", **GORE)]
        if q == "split_verse_condition":
            return [V("equal_value_only", "you upheld sell-the-live but "
                      "not also-the-dead-they-halve (R. Yehudah, "
                      "L35-01)", **GORE)]
        if q == "species_scope" and case.get("animal") == "beast":
            return [V("same_as_ox", "dibber ha-katuv ba-hoveh — the "
                      "common case (Bava Kamma 5:7's list)", **GORE)]
        return None

    STONE = _L21("Mishnah Sanhedrin 1:4; Bava Kamma 4:4-4:8; Keritot "
                 "6:2; Kiddushin 2:9; Arakhin 3:3; Eduyot 6:1",
                 ["L28-02", "L28-03", "L28-04", "L28-05", "L30-01",
                  "L31-01", "L32-01", "L32-03"],
                 machine_claim="EX21-14 (the backfill's two new legs)")

    def rule_stoned_ox_process(case):
        q = case.get("query")
        if q == "ox_trial_size":
            return [V("twenty_three", "ka-mitat bealim kakh mitat "
                      "ha-shor (L28-03)", **STONE)]
        if q == "ox_death_liability":
            if case.get("provoked") == "by_men":
                return [V("exempt", "ki yigach — not that they make it "
                          "gore (the stadium ox)", **STONE)]
            if case.get("aimed_at") == "beast_killed_man":
                return [V("exempt", "et ish — the ox must intend THIS "
                          "victim (L28-04)", **STONE)]
        if q == "ransom_liability" and case.get("state") == "tam":
            return [V("exempt_from_kofer", "the tam pays no ransom; "
                      "both die (L30-01)", **STONE)]
        if q == "benefit_ban_start":
            m = case.get("moment")
            if m == "after_verdict":
                return [V("banned", "the ban rides the verdict "
                          "(L28-05)", **STONE)]
            if m == "verdict_voided":
                return [V("permitted", "the verdict that grounded the "
                          "ban is gone — L28-05 in reverse (Keritot "
                          "6:2)", **STONE)]
        if q == "betrothal_with_banned" and \
           case.get("item") == "stoned_ox":
            return [V("not_betrothed", "no value to convey; sold — the "
                      "proceeds betroth (Kiddushin 2:9)", **STONE)]
        if q == "gored_slave_tariff":
            return [V("thirty_flat", "fairest and ugliest alike thirty "
                      "sela, Tyrian maneh (L32-01/03)", **STONE)]
        if q == "stoning_scope" and case.get("animal") == "rooster":
            return [V("stoned_as_precedent", "R. Yehudah ben Bava's "
                      "testimony — the ba-hoveh canon executed in "
                      "Jerusalem (EX21-14)", **STONE)]
        return None

    PIT = _L21("Mishnah Bava Kamma 5:5 + 5:6 + 3:1",
               ["L33-01", "L33-02", "L33-03", "L33-04"])

    def rule_pit_liability(case):
        q = case.get("query")
        if q == "pit_death_liability":
            d = case.get("depth")
            if d == "ten_handbreadths":
                return [V("liable", "the death-depth — the missing "
                          "and-it-dies word (L33-01)", **PIT)]
            if d == "less_than_ten":
                return [V("exempt_death_liable_damage", "below the "
                          "death-depth — damage only", **PIT)]
        if q == "pit_victim":
            f = case.get("fell")
            if f == "ox_with_vessels":
                return [V("beast_yes_vessels_no", "chamor ve-lo kelim — "
                          "the decree exclusions (L33-02)", **PIT)]
            if f == "son_or_slave":
                return [V("exempt", "shor ve-lo adam (L33-02)", **PIT)]
        if q == "pit_ownership" and \
           case.get("holders") == "two_partners":
            return [V("last_leaver_liable", "the second who left it "
                      "open (L33-03's cover law)", **PIT)]
        return None

    FIVE = _L21("Mishnah Bava Kamma 8:1 + 8:2 + 3:10; Ketubot 3:2",
                ["L19-01", "L19-02", "L19-03", "L22-02", "L22-03",
                 "L12-05", "L26-05"])

    def rule_five_payments(case):
        q = case.get("query")
        if q == "injury_heads_census":
            return [V("five_heads", "nezek, tzaar, ripui, shevet, "
                      "boshet — per-head formulas (L19-01)", **FIVE)]
        if q == "injurer_comparison":
            return [V("man_stricter_than_ox", "man pays five heads and "
                      "fetus-values; the ox damage only (L22 + L19)",
                      **FIVE)]
        if q == "fine_with_capital":
            return [V("no_money_where_death", "ve-lo yihye ason anosh "
                      "yeanesh — the absorption rule's ink (L12-05, "
                      "L22-03)", **FIVE)]
        if q == "actor_vs_ox" and \
           case.get("act") == "blinded_own_slave":
            return [V("self_liable_ox_exempt", "HIS act frees the "
                      "slave, his ox's does not (L26 family)", **FIVE)]
        return None

    THEFT = _L21("Mishnah Bava Kamma 7:1 + 7:5; Sanhedrin 1:1",
                 ["L37-01", "L37-02", "L37-03", "L37-06"])

    def rule_theft_tariff(case):
        q = case.get("query")
        if q == "tariff_scope":
            return [V("ox_and_sheep_only", "double runs everywhere; "
                      "four-five only in the named pair (L37-01)",
                      **THEFT)]
        if q == "tariff_liability" and \
           case.get("sale") == "minus_one_hundredth":
            return [V("double_not_four_five", "u-tvacho — ALL of it "
                      "(L37-02)", **THEFT)]
        if q == "court_size" and case.get("case_type") == "fines":
            return [V("three_judges", "damage, double, four-five all by "
                      "three (Sanhedrin 1:1)", **THEFT)]
        return None

    CAP = _L21("Mishnah Sanhedrin 11:1 + 7:3",
               ["L12-04", "L15-01", "L16-01", "L17-01", "L20-03"])

    def rule_capital_modes(case):
        q = case.get("query")
        if q == "kidnap_elements":
            return [V("steal_domain_use", "steal + bring into his "
                      "domain + use — R. Yehudah's rider (L16-01)",
                      **CAP)]
        if q == "parent_striker" and case.get("wound") == "none":
            return [V("exempt", "capital only with a wound (L15-01); "
                      "the curser liable even after death (L17-01)",
                      **CAP)]
        if q == "execution_mode" and \
           case.get("offender") == "murderer":
            return [V("sword", "nakom yinakem — cherev (L12-04, "
                      "L20-03)", **CAP)]
        return None

    return {
        "passover_offering": {"fn": rule_passover_offering,
                              "tractate": "Pesachim"},
        "passover_eating": {"fn": rule_passover_eating,
                            "tractate": "Pesachim"},
        "leaven_ban": {"fn": rule_leaven_ban, "tractate": "Pesachim"},
        "seder_duties": {"fn": rule_seder_duties, "tractate": "Pesachim"},
        "egypt_vs_generations": {"fn": rule_egypt_vs_generations,
                                 "tractate": "Pesachim"},
        "calendar_court": {"fn": rule_calendar_court,
                           "tractate": "Rosh Hashanah"},
        "firstborn_animal": {"fn": rule_firstborn_animal,
                             "tractate": "Bekhorot"},
        "firstborn_human": {"fn": rule_firstborn_human,
                            "tractate": "Bekhorot"},
        "tefillin_form": {"fn": rule_tefillin_form,
                          "tractate": "Megillah"},
        "sabbath_boundary": {"fn": rule_sabbath_boundary,
                             "tractate": "Eruvin"},
        "challah_measure": {"fn": rule_challah_measure,
                            "tractate": "Eduyot"},
        "court_tiers": {"fn": rule_court_tiers, "tractate": "Sanhedrin"},
        "plotting_witnesses": {"fn": rule_plotting_witnesses,
                               "tractate": "Makkot"},
        "equal_weight": {"fn": rule_equal_weight, "tractate": "Keritot"},
        "altar_stones": {"fn": rule_altar_stones, "tractate": "Middot"},
        "sinai_purity": {"fn": rule_sinai_purity, "tractate": "Shabbat"},
        "song_performance": {"fn": rule_song_performance,
                             "tractate": "Sotah"},
        "incantation_ban": {"fn": rule_incantation_ban,
                            "tractate": "Sanhedrin"},
        "public_discharge": {"fn": rule_public_discharge,
                             "tractate": "Rosh Hashanah"},
        "census_tables": {"fn": rule_census_tables,
                          "tractate": "Pirkei Avot"},
        "decalogue_standing": {"fn": rule_decalogue_standing,
                               "tractate": "Tamid"},
        "document_precedent": {"fn": rule_document_precedent,
                               "tractate": "Yadayim"},
        "circumcision_priority": {"fn": rule_circumcision_priority,
                                  "tractate": "Nedarim"},
        "good_measure": {"fn": rule_good_measure, "tractate": "Sotah"},
        "maror_reason": {"fn": rule_maror_reason, "tractate": "Pesachim"},
        "slave_acquisition": {"fn": rule_slave_acquisition,
                              "tractate": "Kiddushin"},
        "onah_duty": {"fn": rule_onah_duty, "tractate": "Ketubot"},
        "goring_liability": {"fn": rule_goring_liability,
                             "tractate": "Bava Kamma"},
        "stoned_ox_process": {"fn": rule_stoned_ox_process,
                              "tractate": "Sanhedrin"},
        "pit_liability": {"fn": rule_pit_liability,
                          "tractate": "Bava Kamma"},
        "five_payments": {"fn": rule_five_payments,
                          "tractate": "Bava Kamma"},
        "theft_tariff": {"fn": rule_theft_tariff,
                         "tractate": "Bava Kamma"},
        "capital_modes": {"fn": rule_capital_modes,
                          "tractate": "Sanhedrin"},
    }
