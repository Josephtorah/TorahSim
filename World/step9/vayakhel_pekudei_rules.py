#!/usr/bin/env python3
"""vayakhel_pekudei_rules.py — the round-9 exam's rule modules
(2026-09-02, the book of Exodus' closing cycle). Four modules on
Exod 35-40 anchors. engine.py merges build(V) at its tail."""


def build(V):
    def _VP(mishnah, anchor, **extra):
        d = dict(mishnah=mishnah, exodus_anchor=anchor)
        d.update(extra)
        return d

    CS = _VP("Mishnah Sanhedrin 4:1",
             "Exod.35.3 (exo_35_shabbat_donate, EX35-01 — no fire in "
             "your dwellings on the Sabbath day)")

    def rule_capital_schedule(case):
        q = case.get("query")
        if q == "capital_trial_eve" and \
                case.get("day") == "eve_of_sabbath":
            return [V("not_tried", "capital verdicts of conviction "
                      "conclude only on the morrow — and the morrow "
                      "is Shabbat, where the fire-ban blocks the "
                      "court's execution: therefore no capital trial "
                      "opens on the eve of Shabbat or festival",
                      machine_claim="EX35-01", **CS)]
        if q == "verdict_conclusion" and \
                case.get("case_type") == "capital":
            return [V("acquit_same_day_convict_next", "concluded the "
                      "same day for acquittal, the day after for "
                      "conviction", machine_claim="EX35-01", **CS)]
        return None

    SC = _VP("Mishnah Shevuot 1:1",
             "Exod.36.6 (exo_35_36_work_start, EX36-05 — the "
             "camp-wide stop order, the carrying labor's anchor)")

    def rule_shabbat_carryings(case):
        if case.get("query") == "carrying_out_count":
            return [V("two_that_are_four", "the carryings-out of "
                      "Shabbat: two that are four — with the oaths, "
                      "the uncleanness-awarenesses, and the "
                      "leprosy-shades in the row's own census",
                      machine_claim="EX36-05", **SC)]
        return None

    PS = _VP("Mishnah Shekalim 1:4",
             "Exod.38.25-26 (exo_38_court_inventory, EX38-04 — every "
             "one passing the count from twenty up)")

    def rule_priest_shekel_duty(case):
        if case.get("query") == "priest_shekel":
            return [V("does_not_sin", "any priest who pays the shekel "
                      "does not sin — the priests exempt yet free to "
                      "volunteer", authority="Ben Buchri (testified "
                      "at Yavneh, via R. Yehudah)",
                      machine_claim="EX38-04", **PS),
                    V("sins_if_not_paying", "any priest who does NOT "
                      "pay sins — the priests expound the "
                      "wholly-burned meal-offering verse for their "
                      "own benefit", authority="Rabban Yochanan ben "
                      "Zakkai", machine_claim="EX38-04", **PS)]
        return None

    TW = _VP("Mishnah Shabbat 2:3",
             "Exod.40.19 (exo_40_erect_fill, EX40-04 — he spread the "
             "TENT over the tabernacle: the flax-tent lexicon)")

    def rule_tree_products_wicks(case):
        q = case.get("query")
        m = case.get("material")
        if q == "wick_permitted":
            if m == "tree_product":
                return [V("not_lit", "whatever comes from the tree is "
                          "not used as a wick", machine_claim="EX40-04",
                          **TW)]
            if m == "flax":
                return [V("lit", "except flax — the spread TENT of "
                          "the verse names the linen coverings a "
                          "tent, so flax is the tree-product that "
                          "wicks", machine_claim="EX40-04", **TW)]
            if m == "folded_unsinged_cloth":
                return [V("unclean_not_lit", "folded and not singed: "
                          "still a garment — unclean, and not lit",
                          authority="R. Eliezer",
                          machine_claim="EX40-04", **TW),
                        V("clean_and_lit", "the folding unmade it: "
                          "clean, and lit", authority="R. Akiva",
                          machine_claim="EX40-04", **TW)]
        if q == "tent_uncleanness":
            return [V("only_flax_susceptible", "no tree-product "
                      "contracts tent-uncleanness except flax — the "
                      "same tent-lexicon at the same verse",
                      machine_claim="EX40-04", **TW)]
        return None

    return {
        "capital_schedule": {"fn": rule_capital_schedule,
                             "tractate": "Sanhedrin"},
        "shabbat_carryings": {"fn": rule_shabbat_carryings,
                              "tractate": "Shevuot"},
        "priest_shekel_duty": {"fn": rule_priest_shekel_duty,
                               "tractate": "Shekalim"},
        "tree_products_wicks": {"fn": rule_tree_products_wicks,
                                "tractate": "Shabbat"},
    }
