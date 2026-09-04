#!/usr/bin/env python3
"""pesach_rules.py — round 16: THE PASCHAL OFFERING, the fifth
Exodus Talmud-first exam block (2026-09-04) and the map's largest.
Nine modules on Exodus 12:3-11, 12:21-27, 12:43-49, and 34:25 — the
derivation layer over the seated Mishnah tables (EX12-17/18/21).
engine.py merges build(V) at its tail. Read-source record:
logic/oral_triage/exodus_block_pesach_2026-09-04.md."""


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    # -------------------------------------------- registration
    RG = _EX("Pesachim 61a:8-11 (the doubled count-verbs; the "
             "takhosu lexicon) + 88a:6-7 (the household) + 89a:22-24 "
             "(the withdrawal window) + 90a:12-16 (sustain from the "
             "lamb) + 91b:2-4 (the women three-way) + 99a:2-3 (the "
             "intermingled lambs)",
             "Exod.12.3-4 (exo_12_passover_and_exodus, EX12-25 — "
             "seated F-057; EX12-17d the eater teleology)")

    def rule_registration(case):
        q = case.get("query")
        if q == "registration_indispensable":
            return [V("disqualifies", "'according to the NUMBER... "
                      "you shall make your COUNT' — the DOUBLED "
                      "formulation makes registration indispensable: "
                      "slaughtered for the unregistered, the offering "
                      "falls (Pesachim 61a:9)", machine_claim="EX12-25",
                      **RG)]
        if q == "takhosu_meaning":
            return [V("aramaic_slaughter", "Rebbi: takhosu is Aramaic "
                      "— 'slaughter [kos] me this lamb': the "
                      "count-verb itself says registration closes at "
                      "the slaughter (61a:10, the M-09 dictionary "
                      "family)", machine_claim="EX12-25", **RG)]
        if q == "withdrawal_window":
            return [V("until_slaughter", "the Rabbis: miheyot mi-seh "
                      "read me-CHAYUTEI — while the lamb LIVES",
                      authority="the Rabbis", machine_claim="EX12-25",
                      **RG),
                    V("until_sprinkling", "R. Shimon: me-HAVAYATEI — "
                      "through its happenings, to the blood",
                      authority="R. Shimon", machine_claim="EX12-25",
                      **RG)]
        if q == "sustain_from_lamb":
            return [V("festival_needs_only", "the Rabbis: ha-chayeihu "
                      "mi-seh — sell shares for food (and the "
                      "facilitators: matza and herbs ride the lamb "
                      "itself)", authority="the Rabbis",
                      machine_claim="EX12-25", **RG),
                    V("all_his_needs", "Rebbi: sustain YOURSELF from "
                      "the lamb — even a shirt, even a cloak; the "
                      "nation consecrates on that condition",
                      authority="Rebbi", machine_claim="EX12-25",
                      **RG)]
        if q == "household_registration":
            return [V("minors_without_consent", "'a lamb for a "
                      "HOUSEHOLD' — minors and Canaanite servants "
                      "ride the household without consent; adult "
                      "children, Hebrew servants, and the wife only "
                      "with consent (88a:6-7 — the orphan's guardians "
                      "answered without retroactive clarification)",
                      machine_claim="EX12-25", **RG)]
        if q == "women_pesach_duty":
            return [V("first_obligated_second_ancillary", "R. Yehuda: "
                      "'SOULS' includes her at the first; 'that MAN "
                      "shall bear his sin' excludes her at the "
                      "second — ancillary only",
                      authority="R. Yehuda", machine_claim="EX12-25",
                      **RG),
                    V("both_slaughtered_for_her", "R. Yosei: her own "
                      "lamb at both", authority="R. Yosei",
                      machine_claim="EX12-25", **RG),
                    V("first_ancillary_second_none", "R. Shimon: "
                      "ancillary at the first, nothing at the second",
                      authority="R. Shimon", machine_claim="EX12-25",
                      **RG)]
        if q == "intermingled_pesach":
            return [V("one_original_remains", "R. Yehuda: the group "
                      "may shrink so long as ONE original member "
                      "stands (and his no-individual-slaughter makes "
                      "the late joiner original — R. Yochanan, "
                      "99a:3)", authority="R. Yehuda",
                      machine_claim="EX12-25", **RG),
                    V("never_ownerless", "R. Yosei: so long as the "
                      "lamb is never left without a registrant",
                      authority="R. Yosei", machine_claim="EX12-25",
                      **RG)]
        return None

    # ------------------------------------------- window and gates
    WG = _EX("Pesachim 59a:1 (the order algorithm) + 61a:6 + 61b:6-7 "
             "(the rite-by-rite arel scope) + 78b:10 (R. Natan's one "
             "lamb)",
             "Exod.12.6 + 12.43-48 (exo_12_passover_and_exodus, "
             "EX12-17b the window; EX12-25)")

    def rule_window(case):
        q = case.get("query")
        if q == "pesach_slaughter_order":
            return [V("after_the_daily", "the ORDER ALGORITHM: the "
                      "offering carrying both 'in the evening' and "
                      "'in the afternoon' follows the offering "
                      "carrying 'in the afternoon' alone — the "
                      "paschal after the daily (Pesachim 59a:1)",
                      machine_claim="EX12-25", **WG)]
        if q == "uncircumcised_rite_scope":
            return [V("slaughter_not_sprinkling", "'THIS is the "
                      "ordinance': all-uncircumcised disqualifies "
                      "the SLAUGHTER; at the SPRINKLING even "
                      "all-uncircumcised does not — the gate is "
                      "rite-specific (61b:6-7)",
                      machine_claim="EX12-25", **WG)]
        if q == "one_lamb_nation":
            return [V("all_fulfill_after_fact", "R. Natan: 'the "
                      "whole assembly shall slaughter IT' — one lamb "
                      "can carry the nation after the fact, though "
                      "none can eat an olive-bulk (78b:10; eating is "
                      "a separate duty)", machine_claim="EX12-25",
                      **WG)]
        return None

    # --------------------------------------------- for its name
    FN = _EX("Zevachim 7b:17-18 (Rav Safra's verse map) + Pesachim "
             "62b:6-7 (it-as-is at its time) + 70b:7 (Rav Nachman)",
             "Exod.12.27 (exo_12_passover_and_exodus, EX12-17c; "
             "EX12-28 — seated F-060; the Tzav round's wrong-intent "
             "table already runs the fitness grid)")

    def rule_for_its_name(case):
        q = case.get("query")
        if q == "pesach_hu_assignments":
            return [V("three_verses_mapped", "Rav Safra's map: "
                      "Deuteronomy 16:2 — the leftover pesach is "
                      "offered as a PEACE OFFERING (Rav Nachman); "
                      "Deuteronomy 16:1 — no deviation of TYPE; our "
                      "12:27 — no deviation of OWNER, and 'IT IS' "
                      "makes the intent indispensable both ways, "
                      "slaughter's rule extending to every rite "
                      "(Zevachim 7b:17-18)", machine_claim="EX12-28",
                      **FN)]
        if q == "leftover_pesach_fate":
            return [V("peace_offering", "'of the flock AND THE HERD' "
                      "— but the pesach comes only from the flock: "
                      "the herd-word re-assigns the LEFTOVER pesach "
                      "to the peace offering (Rav Nachman; ben "
                      "Dortai's Shabbat reading of the same words "
                      "rejected and recorded)",
                      machine_claim="EX12-28", **FN)]
        return None

    # -------------------------------------------- lamb validity
    LV = _EX("Zevachim 25b:15 (it shall BE) + Pesachim 96a:8-12 + "
             "Arakhin 13b:1-2 (the examination and its export)",
             "Exod.12.5-6 (exo_12_passover_and_exodus, EX12-28)")

    def rule_validity(case):
        q = case.get("query")
        if q == "continuous_validity":
            return [V("all_four_rites", "'a lamb without blemish, a "
                      "male of the first year IT SHALL BE' — "
                      "unblemished and in-year at the slaughter, the "
                      "collection, the conveying, AND the sprinkling: "
                      "all its happenings (Zevachim 25b:15)",
                      machine_claim="EX12-28", **LV)]
        if q == "four_day_examination":
            return [V("generations_and_daily", "the FOUR-DAY "
                      "examination binds the generations too (13:5's "
                      "'you shall perform this service'), excludes "
                      "the second Passover ('this month'), and ben "
                      "Bag Bag EXPORTS it to the daily offering by "
                      "the safeguard-safeguard analogy — implemented "
                      "as the Chamber of the Lambs' six inspected "
                      "lambs (Arakhin 13b:1-2)",
                      machine_claim="EX12-28", **LV)]
        return None

    # ---------------------------------------------- the roast
    RM = _EX("Pesachim 41a:6-41b:18 (the liquid routes, the lash "
             "matrix, the time scope) + 74a:2-3 (fire-directness and "
             "the wood elimination) + 75a:4-5 (the swept oven) + "
             "76a:2-3 (the gravy)",
             "Exod.12.8-9 (exo_12_passover_and_exodus, EX12-18 the "
             "roast edges; EX12-26 — seated F-058)")

    def rule_roast(case):
        q = case.get("query")
        if q == "roast_liquid_route":
            return [V("a_fortiori_taste", "the first tanna: water, "
                      "which does not temper taste, is banned — "
                      "liquids that DO temper, all the more so",
                      authority="the first tanna",
                      machine_claim="EX12-26", **RM),
                    V("bashel_mevushal", "Rebbi: 'boiled IN ANY WAY' "
                      "— the doubled verb carries all liquids",
                      authority="Rebbi", machine_claim="EX12-26",
                      **RM)]
        if q == "roast_lash_matrix":
            return [V("two_two_three", "partially roasted: two sets "
                      "(the raw-ban + the roasted-positive); boiled: "
                      "two; partially-roasted-then-boiled: THREE "
                      "(41b:1 — the counts on the verse's own "
                      "clauses)", machine_claim="EX12-26", **RM)]
        if q == "roast_time_scope":
            return [V("when_arise_and_eat_binds", "the spare second "
                      "'roasted with fire': the raw-ban binds "
                      "exactly when the arise-and-eat duty binds — "
                      "and 12:8's 'on that night' holds it to the "
                      "night (41b:11+18)", machine_claim="EX12-26",
                      **RM)]
        if q == "roast_fire_directness":
            return [V("fire_not_through_another", "the metal spit "
                      "heats through and roasts BY THE SPIT — "
                      "roasted in fire, not through something else "
                      "(74a:2); the dripped gravy that returns "
                      "roasts by the earthenware — remove its place "
                      "(76a:2)", machine_claim="EX12-26", **RM)]
        if q == "spit_material":
            return [V("pomegranate_by_elimination", "the WOOD "
                      "ELIMINATION: palm sweats between its leaves, "
                      "fig is hollow with sap, oak, carob, and "
                      "sycamore weep at their cut knots — each "
                      "would COOK the meat at the contact line; "
                      "pomegranate alone roasts by fire only "
                      "(74a:2-3 — a materials run on the verse's "
                      "requirement)", machine_claim="EX12-26", **RM)]
        if q == "swept_oven_roast":
            return [V("excluded_by_doubling", "'roasted in fire' "
                      "written TWICE (12:8 + 12:9) — fire literally: "
                      "the swept oven's trapped heat does not "
                      "satisfy the pesach (75a:4-5; the M-14 "
                      "doubling family)", machine_claim="EX12-26",
                      **RM)]
        if q == "gravy_return":
            return [V("remove_its_place", "the mishnah's rule held "
                      "on both arms of the upper/lower dispute — "
                      "hot earthenware either way: the place is cut "
                      "away (76a:2-3)", machine_claim="EX12-26",
                      **RM)]
        return None

    # ------------------------------------------ the chagigah rider
    CH = _EX("Pesachim 70a:4-13 (ben Teima; the reach dilemmas) + "
             "70b:5-7 (ben Dortai recorded and dismissed)",
             "Exod.34.25 (exo_12_passover_and_exodus, EX12-28)")

    def rule_chagigah(case):
        q = case.get("query")
        if q == "chagigah_overnight":
            return [V("both_barred_overnight", "ben Teima: 'the "
                      "offering of the FEAST of the PASSOVER shall "
                      "not be left to the morning' — the festival "
                      "offering AND the pesach under one overnight "
                      "ban (70a:5)", machine_claim="EX12-28", **CH)]
        if q == "chagigah_comparison_reach":
            return [V("complete_comparison", "the reach dilemmas "
                      "(roasted too? the bone too?) land at "
                      "'we require everything' — the comparison "
                      "complete (70a:11), the bone dilemma still "
                      "argued on 'in IT' (70a:12)",
                      machine_claim="EX12-28", **CH)]
        if q == "ben_dortai_reading":
            return [V("rejected_recorded", "ben Dortai read 'flock "
                      "and herd' as pesach-and-chagigah slaughtered "
                      "together — hence Shabbat-override — and "
                      "seceded south over it; Rav Ashi dismisses, "
                      "and the verse goes to Rav Nachman's "
                      "leftover-pesach rule: the rejected reading "
                      "kept on the record (70b:5-7)",
                      machine_claim="EX12-28", **CH)]
        return None

    # -------------------------------------------- bone and carry
    BC = _EX("Pesachim 85a:1-3 (the marrow arms) + 83a:10 + 84a:14-15 "
             "(the three scope routes) + 84a:13-14 (the lash "
             "reasons) + 85b:1-2 (the carry grammar) + 86a:15-16 "
             "(the two groups)",
             "Exod.12.46 + 12.10 (exo_12_passover_and_exodus, "
             "EX12-18 the lash asymmetry; EX12-27 — seated F-059)")

    def rule_bone_carry(case):
        q = case.get("query")
        if q == "bone_marrow_scope":
            return [V("with_and_without", "the ban covers the bone "
                      "with marrow and without — the eat-meat "
                      "positive established on the OUTSIDE meat; "
                      "the rival establishment (positive overrides "
                      "at marrow) recorded beside it (85a:2-3)",
                      machine_claim="EX12-27", **BC)]
        if q == "bone_valid_scope":
            return [V("valid_only", "'in IT' — the valid pesach, "
                      "not the disqualified", authority="the first "
                      "tanna", machine_claim="EX12-27", **BC),
                    V("time_of_validity_counts", "R. Yaakov: "
                      "disqualified AFTER a time of validity keeps "
                      "the ban", authority="R. Yaakov",
                      machine_claim="EX12-27", **BC),
                    V("fit_for_eating", "Rebbi: 'in one house shall "
                      "it be EATEN... you shall not break' — "
                      "fit-for-eating keeps the ban",
                      authority="Rebbi", machine_claim="EX12-27",
                      **BC)]
        if q == "leftover_lash_reason":
            return [V("repaired_by_burn", "R. Yehuda: the "
                      "leave-over ban is REPAIRED by its own "
                      "burn-command — a ban a positive rectifies "
                      "draws no lashes", authority="R. Yehuda",
                      machine_claim="EX12-27", **BC),
                    V("actless_ban", "R. Yaakov: because it is a "
                      "ban WITHOUT AN ACT — the actless rule's "
                      "HOME seat (84a:14; the courts round cited "
                      "it at the false witness)",
                      authority="R. Yaakov", machine_claim="EX12-27",
                      **BC)]
        if q == "carry_between_groups":
            return [V("liable_on_placing", "'you shall not carry "
                      "out' — the Shabbat labor's own grammar "
                      "imported: no liability until LIFTING from "
                      "one group's place and PLACING in the "
                      "other's (R. Ami, 85b:2); group-to-group "
                      "inside one house included by 'to the "
                      "OUTSIDE' (85b:1)", machine_claim="EX12-27",
                      **BC)]
        if q == "two_groups_one_lamb":
            return [V("houses_yes_eater_one_place", "'upon the "
                      "HOUSES wherein they eat' — one lamb, two "
                      "groups; 'in one HOUSE shall it be eaten' — "
                      "one EATER, one place (86a:15; the attendant "
                      "who ate at the oven became his own group)",
                      machine_claim="EX12-27", **BC)]
        return None

    # --------------------------------------------- leftover burn
    LB = _EX("Pesachim 83b:12-14 (the three routes) + Zevachim "
             "36a:3 (the intent verse)",
             "Exod.12.10 + 12.16 (exo_12_passover_and_exodus, "
             "EX12-27)")

    def rule_leftover_burn(case):
        q = case.get("query")
        if q == "leftover_burn_day":
            return [V("second_morning", "'until morning... until "
                      "morning' — the doubling gives the leftover a "
                      "SECOND morning for its burning: never on the "
                      "Festival itself (Chizkiya, 83b:12)",
                      machine_claim="EX12-27", **LB)]
        if q == "burn_day_routes":
            return [V("three_routes_recorded", "Chizkiya's doubled "
                      "morning; Abaye's Shabbat-offering verse; "
                      "Rava's 12:16 — 'THAT alone may be done': the "
                      "food itself, not its facilitators (the same "
                      "clause R. Akiva's kindling proof rides at "
                      "the leaven block)", machine_claim="EX12-27",
                      **LB)]
        if q == "intent_to_leave":
            return [V("disqualifies_r_yehuda", "R. Yehuda's TWO "
                      "burn-verses (12:10 + Leviticus 7:15): the "
                      "spare one powers INTENT-to-leave-over as a "
                      "disqualifier (Zevachim 36a:3)",
                      authority="R. Yehuda", machine_claim="EX12-27",
                      **LB)]
        return None

    # ------------------------------------------------ two eras
    TE = _EX("Pesachim 96a:6-96b:1 (the this-token diff engine) + "
             "95b:1-2 (the second Passover's list; the hallel "
             "verse)",
             "Exod.12.3-11 (exo_12_passover_and_exodus, EX12-21 the "
             "two-era table; EX12-28)")

    def rule_two_eras(case):
        q = case.get("query")
        if q == "egypt_only_clauses":
            return [V("tenth_day_haste_one_night", "the THIS-token "
                      "diff engine: 'THIS month' — the tenth-day "
                      "taking Egypt's alone (96a:7); 'you shall eat "
                      "IT in haste' — the haste Egypt's alone "
                      "(96a:24); the leaven ban one night AND day "
                      "(96b:1); the raw-ban CARRIED to the "
                      "generations by 'you shall perform' (96a:23) "
                      "— each clause tagged by its own token",
                      machine_claim="EX12-21 + EX12-28", **TE)]
        if q == "second_pesach_includes":
            return [V("raw_in_leaven_out", "'according to the "
                      "entire statute of the pesach': what is OF "
                      "THE LAMB'S BODY comes in (the raw-ban); what "
                      "is not, stays out (slaughter-over-leaven) — "
                      "the inclusion-preference rule (95b:1)",
                      machine_claim="EX12-28", **TE)]
        if q == "pesach_hallel_at_eating":
            return [V("first_night_only", "'a song as in the night "
                      "when a Festival is sanctified' (Isaiah "
                      "30:29) — the sanctified night sings over the "
                      "eaten lamb; the second Passover's night does "
                      "not (95b:2)", machine_claim="EX12-28", **TE)]
        return None

    return {
        "pesach_registration_machine": {"fn": rule_registration},
        "pesach_window_and_gates": {"fn": rule_window},
        "pesach_for_its_name": {"fn": rule_for_its_name},
        "pesach_lamb_validity": {"fn": rule_validity},
        "pesach_roast_machine": {"fn": rule_roast},
        "pesach_chagigah_rider": {"fn": rule_chagigah},
        "pesach_bone_and_carry": {"fn": rule_bone_carry},
        "pesach_leftover_burn": {"fn": rule_leftover_burn},
        "pesach_two_eras": {"fn": rule_two_eras},
    }
