#!/usr/bin/env python3
"""vayikra_rules.py — the round-10 exam's rule modules (2026-09-03,
the book of Leviticus' OPENING cycle). Seventeen modules on Lev 1-5
anchors, every rule compiled from the claims the same sitting's Sifra
reading seated. engine.py merges build(V) at its tail."""


def build(V):
    def _LV(mishnah, anchor, **extra):
        d = dict(mishnah=mishnah, leviticus_anchor=anchor)
        d.update(extra)
        return d

    CE = _LV("Mishnah Horayot 1:4-3:3",
             "Lev.4.13 (lev_04_inadvertence_case_tree, L04-13 court-error "
             "machine; L04-14 arithmetic; L04-16 epistemics; L04-17 fences)")

    def rule_court_error(case):
        q = case.get("query")
        cs = case.get("court_state")
        rs = case.get("ruling_scope")
        if q == "court_liability":
            if cs in ("one_dissented", "mufla_absent", "member_disqualified"):
                return [V("individuals_liable_court_exempt",
                          "the entire court must rule in error — a dissent, "
                          "an absent chief, or an unfit member voids the "
                          "communal trigger; the actors bear their own "
                          "offerings", machine_claim="L04-13", **CE)]
            if cs == "oath_or_tumah_ruling":
                return [V("court_exempt_graded_tier",
                          "the graded-tier triggers (hearing the voice, the "
                          "utterance, sanctuary tumah) sit outside the "
                          "court's bull — the chapter-4 domain excludes them",
                          machine_claim="L04-13", **CE)]
        if q == "hp_liability":
            if rs == "self_ruled_self_acted":
                return [V("own_bull", "he ruled for himself and acted on his "
                          "own ruling — his own bull atones",
                          machine_claim="L04-16", **CE)]
            if rs == "deed_without_ruling":
                return [V("exempt_hora_ah_required", "the anointed priest is "
                          "likened to the congregation: liable only for an "
                          "erroneous ruling acted on — a slip of deed alone "
                          "carries no bull", machine_claim="L04-13", **CE)]
            if rs == "removed_after_sin":
                return [V("still_brings_bull", "the obligation follows the "
                          "man who held the office", machine_claim="L04-17",
                          **CE)]
        if q == "leader_liability" and rs == "sinned_before_appointment":
            return [V("commoner_offering", "pre-appointment sins ride the "
                      "commoner's path", authority="the first tanna",
                      machine_claim="L04-17", **CE),
                    V("exempt_if_known_after", "R. Shimon: known before the "
                      "appointment — a commoner's offering; known after — "
                      "wholly exempt", authority="R. Shimon",
                      machine_claim="L04-17", **CE)]
        if q == "talui_liability":
            a = case.get("actor")
            if a == "king":
                return [V("liable", "the leader brings the suspended "
                          "guilt-offering ('and he be guilty')",
                          machine_claim="L04-17", **CE)]
            if a == "anointed_priest":
                return [V("exempt", "the anointed priest, like the court, "
                          "is outside the suspended offering",
                          machine_claim="L04-17", **CE)]
        return None

    TO = _LV("Mishnah Shevuot 4",
             "Lev.5.1 (lev_05_asham_graded, LV05A-01 witness-oath machinery)")

    def rule_testimony_oath(case):
        if case.get("query") != "testimony_oath":
            return None
        s = case.get("oath_scope")
        if s in ("blanket_congregation", "oath_before_knowledge",
                 "demanded_by_messenger", "promised_gift_claim"):
            why = {"blanket_congregation": "specificity — the adjuration "
                   "must single out its addressees",
                   "oath_before_knowledge": "the witnessing must precede "
                   "the oath",
                   "demanded_by_messenger": "the claim must be the "
                   "claimant's own",
                   "promised_gift_claim": "a promise is no present debt — "
                   "the class is monetary testimony"}[s]
            return [V("exempt", why, machine_claim="LV05A-01", **TO)]
        if s == "denial_in_court":
            return [V("liable", "the denial that counts is the one a court "
                      "hears", machine_claim="LV05A-01", **TO)]
        return None

    UO = _LV("Mishnah Shevuot 3",
             "Lev.5.4 (lev_05_asham_graded, LV05A-03 utterance oath)")

    def rule_utterance_oath(case):
        q = case.get("query")
        if q == "utterance_oath_count":
            return [V("two_that_are_four", "the future pair doubled by the "
                      "past — 'I ate / I did not eat' join 'I will eat / I "
                      "will not eat': the tense scope doubled by the "
                      "doubled verb", machine_claim="LV05A-03", **UO)]
        if q == "utterance_oath":
            s = case.get("oath_scope")
            if s == "others_concern_no_harm":
                return [V("liable", "matters of others are in where the act "
                          "is his option (good to others included; only "
                          "harm-to-others falls out)",
                          machine_claim="LV05A-03", **UO)]
            if s == "contradicts_known_fact":
                return [V("vain_oath_outside_offering", "the known-false "
                          "oath is the vain class — outside the forgotten-"
                          "oath offering entirely",
                          machine_claim="LV05A-03", **UO)]
        return None

    TA = _LV("Mishnah Shevuot 2",
             "Lev.5.2 (lev_05_asham_graded, LV05A-02 awareness state-machine)")

    def rule_tumah_awareness(case):
        q = case.get("query")
        if q == "tumah_awareness_count":
            return [V("two_that_are_four", "awareness of tumah crossed with "
                      "sanctuary and its foods: the aware-hidden-aware "
                      "brackets, two that are four",
                      machine_claim="LV05A-02", **TA)]
        if q == "tumah_in_courtyard_exit":
            return [V("shortest_way_or_liable", "became unclean INSIDE the "
                      "court: he must leave by the SHORTEST way — bowing, "
                      "lingering, or the long way out is its own "
                      "liability (the seated quick-exit rule LV05A-09)",
                      machine_claim="LV05A-09", **TA)]
        if q == "tumah_hidden_variable":
            return [V("hidden_tumah_suffices", "the hidden variable is the "
                      "tumah itself", authority="the first tanna (R. Akiva's "
                      "reading)", machine_claim="LV05A-02", **TA),
                    V("must_know_which_species", "R. Eliezer: he must know "
                      "WHICH unclean thing — the specificity demand at the "
                      "tumah tier", authority="R. Eliezer",
                      machine_claim="LV05A-02", **TA)]
        return None

    DO = _LV("Mishnah Shevuot 5:1",
             "Lev.5.21 (lev_05_asham_sancta, LV05B-04 deposit oath)")

    def rule_deposit_oath(case):
        if case.get("query") == "deposit_oath_scope":
            return [V("all_persons", "men and women, kin and non-kin — the "
                      "pledge section equates claimees wide (the a-fortiori "
                      "leg the witness oath borrowed)",
                      machine_claim="LV05B-04", **DO)]
        return None

    KO = _LV("Mishnah Keritot",
             "Lev.5.17 (lev_05_asham_sancta, LV05B-03 talui; LV05B-05 locks)")

    def rule_keritot_offerings(case):
        q = case.get("query")
        if q == "doubt_specificity" and \
                case.get("court_state") == "same_category_doubt":
            return [V("liable_both_agree", "one category (which vine, which "
                      "of one kind) — R. Eliezer and R. Yehoshua agree "
                      "liable; the dispute lives only at two names",
                      machine_claim="L04-16", **KO)]
        if q == "talui_for_meilah_doubt":
            return [V("liable_talui", "R. Akiva: doubt of sacrilege brings "
                      "the suspended offering", authority="R. Akiva",
                      machine_claim="LV05B-03", **KO),
                    V("exempt_talui", "the sages: the sacrilege class rides "
                      "its own definite ram, not the talui",
                      authority="the sages", machine_claim="LV05B-03", **KO)]
        if q == "offering_inheritance":
            return [V("no_discharge", "his son shall not bring it — not for "
                      "the father, not for himself, not even the same sin: "
                      "the dedication binds person and purpose",
                      machine_claim="L04-17", **KO)]
        if q == "offering_monies_conversion":
            return [V("permitted_across_tiers", "a goat from lamb-monies, "
                      "birds from beast-monies, the tenth from bird-monies "
                      "— the funds convert down and up the ladder, the "
                      "surplus to the gift fund", machine_claim="LV05A-05",
                      **KO)]
        return None

    MR = _LV("Mishnah Menachot",
             "Lev.2 (lev_02_minchah, LV02-04 floors; LV02-05 parser; "
             "LV02-07 leaven; LV02-09 omer; LV02-10 matrix)")

    def rule_minchah_rules(case):
        q = case.get("query")
        if q == "minchah_omission_validity":
            return [V("valid", "did not pour, mix, break, salt, wave, or "
                      "present — VALID: the criticality sort holds the "
                      "fistful as the gate and the rest advisory",
                      machine_claim="LV02-04", **MR)]
        if q == "leaven_liability_scope":
            return [V("violates_even_remainder", "the offering or even only "
                      "its remainder leavened — the ban covers the whole "
                      "and every step is its own transgression",
                      machine_claim="LV02-07", **MR)]
        if q == "adjunct_matrix_types":
            return [V("four_types", "oil+frankincense / oil only / "
                      "frankincense only / neither — the matrix closed "
                      "member by member", machine_claim="LV02-10", **MR)]
        if q == "communal_semichah_exception":
            return [V("court_bull_and_scapegoat", "no communal offering "
                      "takes hand-laying except the court's bull (the "
                      "elders) and the scapegoat (R. Shimon's pair)",
                      machine_claim="L04-15", **MR)]
        if q == "omer_parch_device":
            return [V("direct_fire", "singe the kernels on the stalks in "
                      "the fire — the mitzvah of parched grain",
                      authority="R. Meir", machine_claim="LV02-09", **MR),
                    V("perforated_tube", "the parching-merchants' "
                      "perforated tube, that the fire envelop the whole",
                      authority="the sages", machine_claim="LV02-09", **MR)]
        if q == "vow_normalization":
            return [V("bring_wheat_fine_flour", "vowed barley — brings "
                      "wheat; vowed coarse flour — brings fine: the "
                      "normalization table (R. Shimon's exemption "
                      "recorded beside)", machine_claim="LV02-05", **MR)]
        if q == "savor_equality":
            return [V("rich_poor_equal", "the beast, the bird, and the "
                      "meal-offering carry one formula — 'a fire-offering, "
                      "a savor pleasing': the one who brings much and the "
                      "one who brings little are equal when the heart is "
                      "to Heaven", machine_claim="LV01B-05", **MR)]
        return None

    AB = _LV("Mishnah Zevachim",
             "Lev.4.12 (lev_04_inadvertence_case_tree, L04-12; the "
             "no-return boundary of the cattle reading)")

    def rule_altar_boundary(case):
        q = case.get("query")
        if q == "altar_no_return":
            return [V("flesh_classes_descend", "what ascended does not "
                      "descend — except the classes never altar-fit: the "
                      "eaten flesh of the most sacred and the lesser "
                      "orders comes down", machine_claim="LV01B-05", **AB)]
        if q == "burned_bulls_site":
            return [V("outside_three_camps_defile_garments", "the burned "
                      "bulls and goats go outside the three camps and "
                      "their handlers' garments are defiled — the "
                      "disposal op with its tumah shadow",
                      machine_claim="L04-12", **AB)]
        return None

    BW = _LV("Mishnah Chullin 1:5",
             "Lev.1.14 (lev_01_olah_bird, LV01D-01 complementary windows)")

    def rule_bird_windows(case):
        if case.get("query") == "bird_age_validity":
            return [V("complementary_windows", "fit in doves is unfit in "
                      "pigeons and the reverse; the shining-neck stage "
                      "unfit in both — the two species' windows are "
                      "complements around a shared dead zone",
                      machine_claim="LV01D-01", **BW)]
        return None

    ES = _LV("Mishnah Sanhedrin 1:3",
             "Lev.4.15 (lev_04_inadvertence_case_tree, L04-15 quorum)")

    def rule_elders_semichah(case):
        if case.get("query") == "elders_semichah_count":
            return [V("five_elders", "'and they shall lay' two + 'elders' "
                      "two + no even court — five", authority="R. Yehudah",
                      machine_claim="L04-15", **ES),
                    V("three_elders", "R. Shimon's count — three",
                      authority="R. Shimon", machine_claim="L04-15", **ES)]
        return None

    JL = _LV("Mishnah Shabbat 10:5",
             "Lev.4.27 (lev_04_inadvertence_case_tree, L04-11 whole-doer)")

    def rule_joint_labor(case):
        if case.get("query") == "joint_labor_liability" and \
                case.get("court_state") == "neither_could_alone":
            return [V("liable_when_neither_could", "each is a whole doer "
                      "where neither could carry alone",
                      authority="R. Yehudah", machine_claim="L04-11", **JL),
                    V("exempt_even_so", "R. Shimon exempts even so — 'in "
                      "doing it, ONE'", authority="R. Shimon",
                      machine_claim="L04-11", **JL)]
        return None

    DM = _LV("Mishnah Shekalim 6:6",
             "Lev.1.7 + Lev.2.1 (LV01B-04 two logs; LV02-02 full fist)")

    def rule_donation_minimums(case):
        q = case.get("query")
        if q == "wood_donation_minimum":
            return [V("two_logs", "the wood vow's floor is the two logs of "
                      "the arrangement — the afternoon plural's own "
                      "quantity", machine_claim="LV01B-04", **DM)]
        if q == "frankincense_donation_minimum":
            return [V("one_handful", "no less than the handful the "
                      "meal-offering carries", machine_claim="LV02-02",
                      **DM)]
        return None

    AG = _LV("Mishnah Megillah 1:9",
             "Lev.4.3 (lev_04_inadvertence_case_tree, L04-16; the "
             "anointed-priest parse of the ledger's Section 2 6)")

    def rule_anointed_vs_garments(case):
        if case.get("query") == "anointed_vs_garments_difference":
            return [V("bull_of_the_sin_only_anointed", "the difference "
                      "between the oil-anointed and the many-garmented "
                      "high priest: the bull for all the commandments — "
                      "the anointed alone brings it ('the anointed' "
                      "excludes the many-garmented)",
                      machine_claim="L04-16", **AG)]
        return None

    OC = _LV("Mishnah Arakhin 5:6",
             "Lev.1.3 (lev_01_call_and_korban_opening, LV01A-06 coercion)")

    def rule_offering_coercion(case):
        if case.get("query") == "court_collection":
            return [V("not_repossessed_compelled", "valuations are "
                      "repossessed; sin- and guilt-offerings are not — "
                      "the atoner wants his atonement, and where he "
                      "delays, 'yakriv oto' compels him until he says I "
                      "am willing", machine_claim="LV01A-06", **OC)]
        return None

    RA = _LV("Mishnah Bava Kamma 9",
             "Lev.5.23-24 (lev_05_asham_sancta, LV05B-05 restore; "
             "LV05B-06 algebra)")

    def rule_restitution_algebra(case):
        q = case.get("query")
        if q == "restitution_delivery":
            return [V("bring_to_victim_even_media", "the sworn robber "
                      "returns principal and fifth to the victim himself, "
                      "even to Media — restitution first, addressed to "
                      "the owner", machine_claim="LV05B-05", **RA)]
        if q == "fifth_recursion":
            return [V("fifth_on_fifth", "swore falsely on the fifth — it "
                      "becomes principal and bears its own fifth, down to "
                      "the perutah floor", machine_claim="LV05B-06", **RA)]
        if q == "father_robbery_oath":
            return [V("principal_stands_own_oath_adds", "robbed the "
                      "father, swore, the father died: the principal is "
                      "owed the heirs; the fifth and the ram ride his own "
                      "oath — the matrix's rung", machine_claim="LV05B-05",
                      **RA)]
        return None

    FS = _LV("Mishnah Chagigah 2:3",
             "Lev.3.2 (lev_03_shelamim, LV03-02 shared semichah)")

    def rule_festival_semichah(case):
        if case.get("query") == "festival_offerings":
            return [V("shelamim_without_semichah", "Beit Shammai: "
                      "peace-offerings on the festival, hands NOT laid",
                      authority="Beit Shammai", machine_claim="LV03-02",
                      **FS),
                    V("both_with_semichah", "Beit Hillel: burnt- and "
                      "peace-offerings both, with hand-laying",
                      authority="Beit Hillel", machine_claim="LV03-02",
                      **FS)]
        return None

    PC = _LV("Mishnah Tamid 4:3 + Mishnah Yoma 2:5",
             "Lev.1.12 (lev_01_olah_flock, LV01C-03 roster; "
             "lev_03_shelamim LV03-05 anatomy)")

    def rule_procedure_census(case):
        q = case.get("query")
        if q == "lobe_attachment":
            return [V("lung_and_haunch_attached", "the lung left attached "
                      "to the neck, the lobe to the haunch — the anatomy "
                      "table's attachment column", machine_claim="LV03-05",
                      **PC)]
        if q == "daily_lamb_carriers":
            return [V("nine_priests", "the daily lamb's limbs by nine — "
                      "one priest per two limbs over the counted ten, "
                      "with the innards' bearers: the roster algebra's "
                      "own census", machine_claim="LV01C-03", **PC)]
        return None

    return {
        "court_error": {"fn": rule_court_error, "tractate": "Horayot"},
        "testimony_oath": {"fn": rule_testimony_oath, "tractate": "Shevuot"},
        "utterance_oath": {"fn": rule_utterance_oath, "tractate": "Shevuot"},
        "tumah_awareness": {"fn": rule_tumah_awareness, "tractate": "Shevuot"},
        "deposit_oath": {"fn": rule_deposit_oath, "tractate": "Shevuot"},
        "keritot_offerings": {"fn": rule_keritot_offerings, "tractate": "Keritot"},
        "minchah_rules": {"fn": rule_minchah_rules, "tractate": "Menachot"},
        "altar_boundary": {"fn": rule_altar_boundary, "tractate": "Zevachim"},
        "bird_windows": {"fn": rule_bird_windows, "tractate": "Chullin"},
        "elders_semichah": {"fn": rule_elders_semichah, "tractate": "Sanhedrin"},
        "joint_labor": {"fn": rule_joint_labor, "tractate": "Shabbat"},
        "donation_minimums": {"fn": rule_donation_minimums, "tractate": "Shekalim"},
        "anointed_vs_garments": {"fn": rule_anointed_vs_garments, "tractate": "Megillah"},
        "offering_coercion": {"fn": rule_offering_coercion, "tractate": "Arakhin"},
        "restitution_algebra": {"fn": rule_restitution_algebra, "tractate": "Bava Kamma"},
        "festival_semichah": {"fn": rule_festival_semichah, "tractate": "Chagigah"},
        "procedure_census": {"fn": rule_procedure_census, "tractate": "Tamid"},
    }
