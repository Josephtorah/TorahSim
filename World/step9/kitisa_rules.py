#!/usr/bin/env python3
"""kitisa_rules.py — the Ki Tisa exam's rule modules (2026-09-01, the
rhythm's fifth cycle). Fourteen modules on Exod 30-34 anchors.
engine.py merges build(V) at its tail."""


def build(V):
    def _KT(mishnah, anchor, **extra):
        d = dict(mishnah=mishnah, exodus_anchor=anchor)
        d.update(extra)
        return d

    CAL = _KT("Mishnah Shekalim 1:1; Mishnah Megillah 3:4",
              "Exod.30.11-13 (exo_30, EX30-04 + EX30-08)")

    def rule_shekel_calendar(case):
        q = case.get("query")
        if q == "shekel_announcement":
            return [V("first_of_adar", "on the first of Adar they "
                      "announce the shekels", machine_claim="EX30-04",
                      **CAL)]
        if q == "shekalim_reading":
            return [V("adar_first_sabbath", "the four portions open "
                      "with Shekalim — this unit's own text on the "
                      "liturgical clock", machine_claim="EX30-08",
                      **CAL)]
        return None

    WHO = _KT("Mishnah Shekalim 1:3",
              "Exod.30.12-14 (exo_30, EX30-04 — twenty and up)")

    def rule_shekel_who_pays(case):
        if case.get("query") == "shekel_pledged":
            p = case.get("payer")
            if p in ("israelite", "levite", "convert", "freed_slave"):
                return [V("pledged", "the tables sit and pledges are "
                          "seized", machine_claim="EX30-04", **WHO)]
            if p in ("woman", "slave", "minor"):
                return [V("not_pledged", "not from women, slaves, or "
                          "minors", machine_claim="EX30-04", **WHO)]
            if p == "priest":
                return [V("not_pledged", "priests are not pledged, "
                          "for the ways of peace",
                          machine_claim="EX30-04", **WHO)]
        return None

    KAL = _KT("Mishnah Shekalim 1:6",
              "Exod.30.13 (exo_30, EX30-09 — the half-coin's "
              "friction)")

    def rule_kalbon_fees(case):
        if case.get("query") == "kalbon_owed":
            p = case.get("payment")
            if p == "joint_two":
                return [V("one_kalbon", "two paying jointly owe one",
                          authority="the first tanna",
                          machine_claim="EX30-09", **KAL),
                        V("two_kalbons", "each half generates its fee",
                          authority="R. Meir", machine_claim="EX30-09",
                          **KAL)]
            if p == "on_behalf_of_exempt":
                return [V("exempt", "paying for a priest, woman, "
                          "slave, or minor carries no kalbon",
                          machine_claim="EX30-09", **KAL)]
            if p == "sela_taking_shekel":
                return [V("two_kalbons", "a sela in and a shekel back "
                          "is two exchanges", machine_claim="EX30-09",
                          **KAL)]
        return None

    EQ = _KT("Mishnah Shekalim 2:4",
             "Exod.30.15 (exo_30, EX30-10 — rich no more, poor no "
             "less)")

    def rule_shekel_equality(case):
        q = case.get("query")
        if q == "shekel_invariant":
            return [V("all_hands_equal", "yad kulan shavah — the "
                      "equality holds at any denomination",
                      machine_claim="EX30-10", **EQ)]
        if q == "shekel_denominations":
            return [V("floated", "darkonot, selaim, teva'in, the "
                      "dinar proposal — the coin moved, the flatness "
                      "did not (the conversion-layer the received "
                      "translation performs at the verse)",
                      machine_claim="EX30-10", **EQ)]
        return None

    GRP = _KT("Mishnah Shabbat 7:1",
              "Exod.31.13-15 (exo_31, EX31-05 + EX31-03 — the Great "
              "Principle at the labors' own join)")

    def rule_shabbat_liability_grouping(case):
        if case.get("query") == "offering_count":
            f = case.get("forgot")
            table = {"principle": ("one_total", "forgot the very "
                                   "principle — one offering for all"),
                     "days": ("one_per_sabbath", "knew the principle, "
                              "forgot the days"),
                     "labors": ("one_per_category", "knew the day, "
                                "forgot the labors — one per av "
                                "melakhah"),
                     "none_same_kind": ("one_total", "many labors of "
                                        "one kind — one offering")}
            if f in table:
                v, b = table[f]
                return [V(v, b, machine_claim="EX31-05", **GRP)]
        return None

    RC = _KT("Mishnah Megillah 3:5",
             "Exod.34.1 (exo_34, EX34-01)")

    def rule_reading_calendar(case):
        if case.get("query") == "festival_readings":
            return [V("appointed_portions", "each festival its "
                      "appointed portion — Moses' own arrangement per "
                      "the spine", **RC)]
        return None

    TRG = _KT("Mishnah Megillah 4:10",
              "Exod.34.27 (exo_34, EX34-05 — the covenant by the "
              "saying; the law regulating the reading instrument)")

    def rule_targum_law(case):
        if case.get("query") == "targum_permitted":
            p = case.get("passage")
            if p == "calf_first_account":
                return [V("read_and_translated", "the first calf "
                          "account is read and translated",
                          machine_claim="EX34-05", **TRG)]
            if p == "calf_second_account":
                return [V("read_not_translated", "Aaron's own account "
                          "is read but NOT translated",
                          machine_claim="EX34-05", **TRG)]
            if p == "david_amnon":
                return [V("neither_read_nor_translated", "the David "
                          "and Amnon episodes are neither read nor "
                          "translated as haftarah", **TRG)]
        return None

    FS = _KT("Mishnah Bekhorot 1:2 + 1:4 + 1:7; Mishnah Eduyot 7:1",
             "Exod.34.19-20 (exo_34, EX34-04 + EX34-07)")

    def rule_firstling_species(case):
        q = case.get("query")
        if q == "firstling_liable":
            if case.get("born") == "donkey_like" and \
                    case.get("bearer") == "cow":
                return [V("exempt", "peter chamor said TWICE — bearer "
                          "and born must both be donkeys",
                          machine_claim="EX34-04", **FS)]
            if case.get("event") == "firstling_died":
                return [V("guarantor_liable", "liable as for the "
                          "son's five selas", authority="R. Eliezer",
                          **FS),
                        V("not_liable", "like second-tithe redemption",
                          authority="the sages", **FS)]
        if q == "redemption_lamb":
            return [V("any_seh", "sheep or goat, male or female, "
                      "large or small, even blemished — and one lamb "
                      "redeems many times", machine_claim="EX34-04",
                      **FS)]
        if q == "duty_precedence":
            pair = case.get("pair")
            if pair == "redeem_vs_break":
                return [V("redemption_first", "the redemption duty "
                          "precedes the breaking",
                          machine_claim="EX34-07", **FS)]
            if pair == "yibbum_vs_chalitzah":
                return [V("flipped_to_chalitzah", "formerly yibbum "
                          "first; when intention decayed the order "
                          "FLIPPED — a precedence with a recorded "
                          "history", machine_claim="EX34-07", **FS)]
        return None

    PH = _KT("Mishnah Sheviit 1:4",
             "Exod.34.21 (exo_34, EX34-04 — in plowing and in "
             "harvest you shall rest)")

    def rule_plow_harvest_rest(case):
        if case.get("query") == "plow_harvest_scope":
            return [V("sabbatical_eve", "the eve's plowing entering "
                      "the seventh and the seventh's harvest exiting",
                      authority="R. Akiva", machine_claim="EX34-04",
                      **PH),
                    V("sabbath_optional_acts", "plowing is optional, "
                      "so the harvest is optional — excluding the "
                      "omer", authority="R. Yishmael", **PH)]
        return None

    CF = _KT("Mishnah Yoma 4:2",
             "Exod.34.7 (exo_34, EX34-02 — the attributes' own "
             "vocabulary)")

    def rule_confession_formula(case):
        if case.get("query") == "confession_classes":
            return [V("three_classes", "aviti, pashati, chatati — "
                      "iniquity, transgression, sin as liturgy",
                      machine_claim="EX34-02", **CF)]
        return None

    YKD = _KT("Mishnah Yoma 4:4",
              "Exod.30.34-36 (exo_30, EX30-06)")

    def rule_yk_incense_deltas(case):
        if case.get("query") == "incense_grind" and \
                case.get("occasion") == "yom_kippur":
            return [V("finest_of_fine", "every day fine — today "
                      "finest of the fine", machine_claim="EX30-06",
                      **YKD)]
        return None

    CES = _KT("Mishnah Horayot 1:3",
              "Exod.34.14 (exo_34 — the bowing exemplar)")

    def rule_court_error_scope(case):
        if case.get("query") == "court_error_liability":
            s = case.get("error_scope")
            if s == "whole_principle":
                return [V("exempt", "uprooting the whole body is no "
                          "'hidden matter'", **CES)]
            if s == "partial":
                return [V("liable", "davar ve-lo kol ha-guf — there "
                          "IS idolatry but the bower exempt", **CES)]
        return None

    KC = _KT("Mishnah Keritot 1:1",
             "Exod.30.22-38 (exo_30, EX30-06 — the protected "
             "formulas)")

    def rule_karet_census(case):
        q = case.get("query")
        if q == "karet_count":
            return [V("thirty_six", "thirty-six cut-off crimes in "
                      "the Torah", machine_claim="EX30-06", **KC)]
        if q == "karet_listed":
            if case.get("offense") in ("compounding_oil",
                                       "compounding_incense",
                                       "anointing_with_oil"):
                return [V("on_the_census", "the oil-compounder, the "
                          "incense-compounder, and the anointer — "
                          "this chapter's three formula crimes",
                          machine_claim="EX30-06", **KC)]
        return None

    TP = _KT("Mishnah Pirkei Avot 4:18",
             "Exod.33.14 (exo_33, EX33-04 — wait until the face of "
             "anger passes)")

    def rule_timing_protocol(case):
        if case.get("query") == "timing_prohibited":
            m = case.get("moment")
            if m == "hour_of_anger":
                return [V("do_not_appease", "do not placate your "
                          "fellow in the hour of his anger",
                          machine_claim="EX33-04", **TP)]
            if m == "dead_before_him":
                return [V("do_not_comfort", "do not comfort while "
                          "his dead lies before him", **TP)]
        return None

    EF = _KT("Mishnah Pirkei Avot 6:2",
             "Exod.31.18 with 32:16 (exo_31, EX31-04)")

    def rule_engraving_freedom(case):
        if case.get("query") == "engraving_reading":
            return [V("freedom", "read not charut but cherut — none "
                      "free but the one engaged in Torah",
                      machine_claim="EX31-04", **EF)]
        return None

    return {
        "shekel_calendar": {"fn": rule_shekel_calendar,
                            "tractate": "Shekalim"},
        "shekel_who_pays": {"fn": rule_shekel_who_pays,
                            "tractate": "Shekalim"},
        "kalbon_fees": {"fn": rule_kalbon_fees, "tractate": "Shekalim"},
        "shekel_equality": {"fn": rule_shekel_equality,
                            "tractate": "Shekalim"},
        "shabbat_liability_grouping": {
            "fn": rule_shabbat_liability_grouping,
            "tractate": "Shabbat"},
        "reading_calendar": {"fn": rule_reading_calendar,
                             "tractate": "Megillah"},
        "targum_law": {"fn": rule_targum_law, "tractate": "Megillah"},
        "firstling_species": {"fn": rule_firstling_species,
                              "tractate": "Bekhorot"},
        "plow_harvest_rest": {"fn": rule_plow_harvest_rest,
                              "tractate": "Sheviit"},
        "confession_formula": {"fn": rule_confession_formula,
                               "tractate": "Yoma"},
        "yk_incense_deltas": {"fn": rule_yk_incense_deltas,
                              "tractate": "Yoma"},
        "court_error_scope": {"fn": rule_court_error_scope,
                              "tractate": "Horayot"},
        "karet_census": {"fn": rule_karet_census,
                         "tractate": "Keritot"},
        "timing_protocol": {"fn": rule_timing_protocol,
                            "tractate": "Avot"},
        "engraving_freedom": {"fn": rule_engraving_freedom,
                              "tractate": "Avot"},
    }
