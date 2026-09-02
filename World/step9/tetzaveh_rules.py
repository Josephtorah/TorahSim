#!/usr/bin/env python3
"""tetzaveh_rules.py — the Tetzaveh exam's rule modules (2026-09-01,
the derive-then-examine rhythm's fourth cycle, run the same sitting
as the derivation).

Nine modules on Exod 28-29 anchors. Provenance mishnah +
exodus_anchor (the same-sitting Tetzaveh seats). engine.py calls
build(V) at its tail and merges the returned registry."""


def build(V):
    def _TZ(mishnah, anchor, **extra):
        d = dict(mishnah=mishnah, exodus_anchor=anchor)
        d.update(extra)
        return d

    # ------------------------------------------------ garment_census
    CENSUS = _TZ("Mishnah Yoma 7:5",
                 "Exod.28.4 (exo_28, EX28-02 — the six-list plus the "
                 "plate and the pants)")

    def rule_garment_census(case):
        if case.get("query") == "garment_count":
            b = case.get("bearer")
            if b == "high_priest":
                return [V("eight", "the four plus breastplate, ephod, "
                          "robe, and plate", machine_claim="EX28-02",
                          **CENSUS)]
            if b == "common_priest":
                return [V("four", "tunic, pants, turban, sash",
                          machine_claim="EX28-02", **CENSUS)]
        return None

    # ------------------------------------------------ oracle_consultation
    ORACLE = _TZ("Mishnah Yoma 7:5",
                 "Exod.28.30 (exo_28, EX28-09 + EX28-03 — the "
                 "judgment organ's access list)")
    QUALIFIED = {"king", "court", "community_need"}

    def rule_oracle_consultation(case):
        if case.get("query") == "oracle_access":
            p = case.get("petitioner")
            if p in QUALIFIED:
                return [V("consulted", "in the eight garments, for "
                          "the king, the court, or one whom the "
                          "community needs", machine_claim="EX28-09",
                          **ORACLE)]
            return [V("not_consulted", "the Urim and Tummim answer "
                      "no private petitioner",
                      machine_claim="EX28-09", **ORACLE)]
        return None

    # ------------------------------------------------ temple_officers
    OFFICERS = _TZ("Mishnah Shekalim 5:2",
                   "Exod.28.5 (exo_28, EX28-10 — the plural "
                   "take-verb: and THEY shall take the gold)")

    def rule_temple_officers(case):
        if case.get("query") == "fiscal_minimum":
            return [V("two_officers", "three treasurers, seven "
                      "trustees, never fewer than two over public "
                      "money — the recorded exceptions "
                      "majority-accepted", machine_claim="EX28-10",
                      **OFFICERS)]
        return None

    # ------------------------------------------------ plate_propitiation
    PLATE = _TZ("Mishnah Zevachim 8:12",
                "Exod.28.38 (exo_28, EX28-11 + EX28-06 — bearing the "
                "iniquity of the offerings, for acceptance)")

    def rule_plate_propitiation(case):
        q = case.get("query")
        if q == "plate_propitiates":
            d = case.get("offering_defect")
            if d == "impurity":
                return [V("propitiates", "ha-tzitz meratzeh al "
                          "ha-tame", machine_claim="EX28-11",
                          **PLATE)]
            if d == "exited":
                return [V("does_not_propitiate", "ve-eino meratzeh "
                          "al ha-yotze — exit is outside the plate's "
                          "jurisdiction", machine_claim="EX28-11",
                          **PLATE)]
        if q == "blood_two_cups" and \
                case.get("event") == "one_cup_exited":
            return [V("inner_fit", "the inner cup remains fit — the "
                      "exit disqualifies only what exited", **PLATE)]
        return None

    # ------------------------------------------------ stone_engraving
    SHAMIR = _TZ("Mishnah Pirkei Avot 5:6 (the twilight census, held "
                 "at EX16-15)",
                 "Exod.28.20 (exo_28, EX28-12 — be-miluotam, in "
                 "their fullness)",
                 talmud_bridge="Babylonian Talmud Sotah 48b — the "
                               "shamir wrote the ephod and "
                               "breastplate stones")

    def rule_stone_engraving(case):
        if case.get("query") == "stone_engraving_method":
            return [V("shamir", "the stones stay whole — in their "
                      "FULLNESS — written by the twilight-created "
                      "shamir", machine_claim="EX28-12", **SHAMIR)]
        return None

    # ------------------------------------------------ bell_adornment
    BELLS = _TZ("Mishnah Shabbat 6:9",
                "Exod.28.34 (exo_28, EX28-05 — the hem-bells' own "
                "zog token)")

    def rule_bell_adornment(case):
        if case.get("query") == "sabbath_wearing" and \
                case.get("item") == "bells":
            return [V("permitted", "princes' sons with bells — and "
                      "anyone: the sages spoke of the prevalent case "
                      "(the ba-hoveh canon)", machine_claim="EX28-05",
                      **BELLS)]
        return None

    # ------------------------------------------------ grooming_labors
    GROOM = _TZ("Mishnah Shabbat 10:6",
                "Exod.28.14 (exo_28, EX28-01's chapter — ovad "
                "gedilu, the braided-work token; the labor catalog "
                "wired to the tabernacle crafts)")

    def rule_grooming_labors(case):
        if case.get("query") == "grooming_liability" and \
                case.get("via") == "hand_or_teeth":
            return [V("liable", "nails, hair, or braiding by hand — "
                      "a labor", authority="R. Eliezer", **GROOM),
                    V("rabbinic_only", "forbidden as shevut, not "
                      "liable", authority="the sages", **GROOM)]
        return None

    # ------------------------------------------------ waving_procedure
    WAVE = _TZ("Mishnah Menachot 5:6",
               "Exod.29.27 (exo_29, EX29-13 + EX29-04 — asher hunaf "
               "va-asher huram, the verse's own two verbs)")

    def rule_waving_procedure(case):
        q = case.get("query")
        if q == "waving_motions":
            # COMPUTED: two verbs in the verse, each a doubled motion.
            verbs = {"hunaf": "forward_and_back",
                     "huram": "up_and_down"}
            return [V("four_motions", "COMPUTED: %d verbs -> %s — "
                      "the Mishnah's molikh-mevi maaleh-morid"
                      % (len(verbs), ", ".join(verbs.values())),
                      machine_claim="EX29-13", **WAVE)]
        if q == "waving_required":
            item = case.get("item")
            if item == "breast_thigh":
                return [V("required", "the breast and thigh of the "
                          "individual peace-offering — men and women "
                          "alike, Israel not others",
                          machine_claim="EX29-13", **WAVE)]
            if item == "showbread":
                return [V("not_required", "the showbread takes "
                          "neither waving nor bringing-near",
                          machine_claim="EX29-13", **WAVE)]
        if q == "waving_geography":
            return [V("east_then_west", "waving in the east, "
                      "bringing-near in the west, wavings precede",
                      machine_claim="EX29-13", **WAVE)]
        return None

    # ------------------------------------------------ sacred_eating_states
    EATING = _TZ("Mishnah Pesachim 8:8",
                 "Exod.29.33 (exo_29, EX29-06 — they eat what atoned "
                 "for them; the stranger banned)")

    def rule_sacred_eating_states(case):
        q = case.get("query")
        if q == "eating_eligibility" and case.get("state") == "onen":
            off = case.get("offering")
            if off == "pesach":
                return [V("permitted_evening", "the onen immerses "
                          "and eats his Passover at evening",
                          machine_claim="EX29-06", **EATING)]
            if off == "other_sacred":
                return [V("barred", "aval lo va-kodashim — the other "
                          "sacred food stays barred",
                          machine_claim="EX29-06", **EATING)]
        if q == "convert_pesach_eve":
            return [V("eats_at_evening", "immerses and eats his "
                      "Passover at evening",
                      authority="Beit Shammai", **EATING),
                    V("barred_seven_days", "one who separates from "
                      "the foreskin is as one who separates from the "
                      "grave", authority="Beit Hillel", **EATING)]
        return None

    return {
        "garment_census": {"fn": rule_garment_census,
                           "tractate": "Yoma"},
        "oracle_consultation": {"fn": rule_oracle_consultation,
                                "tractate": "Yoma"},
        "temple_officers": {"fn": rule_temple_officers,
                            "tractate": "Shekalim"},
        "plate_propitiation": {"fn": rule_plate_propitiation,
                               "tractate": "Zevachim"},
        "stone_engraving": {"fn": rule_stone_engraving,
                            "tractate": "Avot"},
        "bell_adornment": {"fn": rule_bell_adornment,
                           "tractate": "Shabbat"},
        "grooming_labors": {"fn": rule_grooming_labors,
                            "tractate": "Shabbat"},
        "waving_procedure": {"fn": rule_waving_procedure,
                             "tractate": "Menachot"},
        "sacred_eating_states": {"fn": rule_sacred_eating_states,
                                 "tractate": "Pesachim"},
    }
