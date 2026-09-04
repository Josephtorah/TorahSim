#!/usr/bin/env python3
"""egypt_rules.py — round 19: EGYPT AND THE GENERATIONS, the eighth
Exodus Talmud-first exam block (2026-09-04). Four modules over
Exodus 12:3-11, 12:43-49, 13:3-7 — the Passover family's closing
wing: the two-era export engine's derivation layer, the second
Passover's statute engine, the impure-Passover carve-outs, and
Egypt's own rite. engine.py merges build(V) at its tail.
Read-source record: logic/oral_triage/exodus_block_egypt_2026-09-04.md."""


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    # ------------------------------------ the two-era export engine
    TE = _EX("Pesachim 96a:7-25 (the export run, clause by clause) "
             "+ 96b:1-2 (the leaven-days resolution)",
             "Exod.12.3-11 (exo_12_passover_and_exodus, EX12-21 the "
             "two-era table + EX12-28 the surface engine — "
             "ANTICIPATED one round early; F-071 seats the export "
             "operator on exo_13's 13:5)")

    def rule_export(case):
        q = case.get("query")
        if q == "era_clause_taking":
            return [V("egypt_only_by_this", "'on the tenth of THIS "
                      "month' (12:3) — הַזֶּה ('this') pins the "
                      "tenth-day taking to Egypt's month alone; the "
                      "generations take no lamb on the tenth "
                      "(96a:7)", machine_claim="EX12-21", **TE)]
        if q == "era_clause_examination":
            return [V("generations_in_second_out", "the keeping "
                      "clause (12:6) would read Egypt-only — but "
                      "וְעָבַדְתָּ ('you shall perform this service "
                      "in this month,' 13:5) EXPORTS the month's "
                      "services to the generations, so the FOUR-DAY "
                      "EXAMINATION binds them too (96a:11; ben Bag "
                      "Bag exports it further to the daily offering "
                      "by the safeguard analogy, 96a:9); the "
                      "keeping-verse's own הַזֶּה then excludes THE "
                      "SECOND PASSOVER (96a:12) — no four-day "
                      "examination there",
                      machine_claim="EX12-28", **TE)]
        if q == "era_clause_night_eating":
            return [V("exported_zeh_to_midnight", "'they shall eat "
                      "the flesh on THIS night' (12:8): exported by "
                      "וְעָבַדְתָּ — the generations eat by night "
                      "too; the freed הַזֶּה is spent on the "
                      "MIDNIGHT dispute (R. Elazar ben Azaryah's "
                      "deadline vs R. Akiva's haste-hour — the "
                      "standing table EX12-21 carries both arms) "
                      "(96a:13-14)", machine_claim="EX12-21", **TE)]
        if q == "era_clause_arel":
            return [V("exported_bo_matza_owed", "'no uncircumcised "
                      "may eat OF IT' (12:48): exported — the ban "
                      "runs for the generations; the freed בּוֹ "
                      "('of it') teaches: OF THE LAMB he does not "
                      "eat, but he EATS MATZA AND BITTER HERBS "
                      "(96a:15-16) — the corollary EX12-29 already "
                      "seats as the lamb-barred owing the bread",
                      machine_claim="EX12-29 (ANTICIPATED)", **TE)]
        if q == "era_clause_foreigner":
            return [V("exported_bo_apostasy_boundary", "'no "
                      "foreigner may eat of it' (12:43) and "
                      "'sojourner and hireling' (12:45): exported; "
                      "each freed בּוֹ draws the same boundary — "
                      "APOSTASY disqualifies from the pesach and "
                      "does NOT disqualify from terumah (the "
                      "priest's due) (96a:17-20); both clauses "
                      "needed: the uncircumcised is repulsive, the "
                      "foreigner's heart is not toward Heaven — "
                      "neither derivable from the other (96a:19)",
                      machine_claim="EX12-28", **TE)]
        if q == "era_clause_circumcision_gate":
            return [V("exported_bo_bars_him_alone", "'you shall "
                      "circumcise him — THEN he eats of it' "
                      "(12:44): exported; the freed בּוֹ — the "
                      "circumcision of his males and slaves bars "
                      "him FROM THE PESACH alone, never from "
                      "terumah (96a:21)",
                      machine_claim="EX12-28", **TE)]
        if q == "era_clause_bone":
            return [V("exported_bo_valid_only", "'a bone they shall "
                      "not break IN IT' (12:46): exported; the "
                      "freed בּוֹ — IN A VALID lamb, not in a "
                      "disqualified one (96a:22) — the valid-only "
                      "route EX12-27 already holds (F-059)",
                      machine_claim="EX12-27 (ANTICIPATED)", **TE)]
        if q == "era_clause_raw":
            return [V("exported_mimennu_reassigned", "'eat not OF "
                      "IT raw' (12:9): exported; the freed "
                      "מִמֶּנּוּ ('of it') is reassigned to "
                      "Rabbah's teaching in R. Yitzchak's name "
                      "(96a:23)", machine_claim="EX12-28", **TE)]
        if q == "era_clause_haste":
            return [V("egypt_only_by_oto", "'you shall eat IT in "
                      "haste' (12:11) — אוֹתוֹ ('it'): IT is eaten "
                      "in haste and NO OTHER is eaten in haste — "
                      "the haste died with Egypt (96a:24)",
                      machine_claim="EX12-21", **TE)]
        if q == "era_clause_leaven_days":
            return [V("egypt_night_and_day_generations_seven",
                      "the mishnah's 'one night' resolved (96b:2): "
                      "Egypt's leaven ban ran the night AND ITS DAY "
                      "— R. Yosei HaGelili's juxtaposition ('no "
                      "leaven shall be eaten' beside 'TODAY you go "
                      "out,' 13:3-4) — and the generations' ban "
                      "runs all seven (96b:1-2); the leaven block's "
                      "egypt-days row stands in its final form",
                      machine_claim="EX12-28 + EX13-16", **TE)]
        return None

    # ------------------------------ the second Passover's statute
    SP = _EX("Pesachim 95a:1-95b:9 (the statute engine; the "
             "override table)",
             "Exod.12.8-10 + 12.46 as the engine's operands "
             "(exo_12_passover_and_exodus; F-070 seats the engine "
             "as EX12-30)")

    def rule_statute(case):
        q = case.get("query")
        if q == "second_pesach_criterion":
            return [V("in_body_applies", "'according to the entire "
                      "STATUTE of the Passover shall they do it' "
                      "(Num 9:12) — the text speaks of commands IN "
                      "ITS BODY (95a:2); the general's three stated "
                      "particulars type the includes: a positive "
                      "(matza-herbs), a negative-repaired-by-"
                      "positive (not-leave), a full negative (the "
                      "bone) (95a:11)", machine_claim="EX12-28",
                      **SP)]
        if q == "second_pesach_roast":
            return [V("included_by_matza_general", "roast-with-fire "
                      "rides in on the matza-herbs general — a "
                      "command in the lamb's own body (95a:12); the "
                      "reverse-challenge refused: מִצְוָה "
                      "דְגוּפֵיהּ עֲדִיף — the in-body command is "
                      "preferred", machine_claim="EX12-26", **SP)]
        if q == "second_pesach_carry_out":
            return [V("included_by_leftover_general", "the "
                      "carry-out ban (12:46) rides in on the "
                      "not-leave general — the resembling pair: "
                      "one invalidated as leftover, one as "
                      "taken-out (95a:13)",
                      machine_claim="EX12-27", **SP)]
        if q == "second_pesach_leaven_seen":
            return [V("excluded_in_body_preferred", "the seen/found "
                      "bans are OUT — though they resemble "
                      "not-leave in the lash class (both negatives "
                      "repaired by positives), the in-body "
                      "preference decides against them (95a:14); "
                      "the second keeps leaven and matza with him "
                      "in the house (95a:1)",
                      machine_claim="EX12-28", **SP)]
        if q == "second_pesach_leaven_removal":
            return [V("excluded_not_on_body", "leaven-REMOVAL is "
                      "OUT — not a command on the lamb's body "
                      "(95a:12)", machine_claim="EX12-28", **SP)]
        if q == "second_pesach_slaughter_over_leaven":
            return [V("excluded_off_body", "slaughter-over-leaven "
                      "(34:25) is OUT at the bone general — not of "
                      "the lamb's body — while the raw-ban (12:9) "
                      "is IN (95b:1)", machine_claim="EX12-28",
                      **SP)]
        if q == "second_pesach_individual":
            return [V("seek_company", "the Rabbis' spending of "
                      "'they shall do IT': the second Passover is "
                      "not slaughtered for an individual — "
                      "wherever company can be sought, it is "
                      "sought (95a:8)", machine_claim="EX12-25",
                      **SP)]
        if q == "second_pesach_shabbat":
            return [V("overrides", "both Passovers override the "
                      "Sabbath — the mishnah's own row (95a:1) and "
                      "the baraita's pair (95b:6)",
                      machine_claim="EX12-17", **SP)]
        if q == "second_pesach_impurity":
            return [V("not_done_in_impurity", "impurity PUSHED IT "
                      "OFF — shall it return and be done in "
                      "impurity? (95b:4-5)",
                      authority="the first authority (the mishnah)",
                      machine_claim="EX12-28", **SP),
                    V("done_in_impurity", "the Torah RETURNED for "
                      "it to be done in purity; not achieved — it "
                      "is done in impurity (95b:5-6)",
                      authority="R. Yehuda", **SP)]
        if q == "second_pesach_lodging":
            return [V("lodging_required", "the baraita's third "
                      "pair: first and second alike require "
                      "lodging (95b:6)",
                      authority="R. Yehuda (the baraita's tanna)",
                      machine_claim="EX12-28", **SP),
                    V("lodging_exempt_by_six", "'you shall turn in "
                      "the morning' + 'six days you shall eat "
                      "matza': eaten-for-six requires lodging; the "
                      "second, eaten one day, does not (95b:8) — "
                      "two tannaim within R. Yehuda (95b:9)",
                      authority="R. Yehuda (the derivation's "
                      "tanna)", **SP)]
        if q == "hallel_at_making":
            return [V("both_eras_required", "hallel at the MAKING "
                      "at both Passovers, two recorded routes: the "
                      "hallel verse excludes only the night; and "
                      "'is it possible that Israel slaughter their "
                      "Passovers or take their palm-branches "
                      "without hallel?' (95b:3)",
                      machine_claim="EX12-28", **SP)]
        return None

    # --------------------------- the impure-Passover carve-outs
    IP = _EX("Pesachim 95b:10-96a:3 (the carve-out mishnah and its "
             "derivations)",
             "Exod.12.4 + 12.47 (the congregation's lamb) — the "
             "karet engine rides Lev 7:19-20, the Tzav round's own "
             "flesh-purity verses (lev_07 units): CROSS-BOOK")

    def rule_carveouts(case):
        q = case.get("query")
        if q == "impure_pesach_flux_eaters":
            return [V("exempt_from_karet", "flux-bearers, "
                      "menstruants, and women after childbirth who "
                      "ATE of a Passover brought in impurity: "
                      "EXEMPT from karet (excision) — 'every PURE "
                      "one may eat flesh; the soul that eats with "
                      "his impurity on him is cut off' (Lev "
                      "7:19-20): eaten-BY-THE-PURE carries the "
                      "liability; a Passover not eaten by the pure "
                      "does not (95b:10-13) — the karet gate "
                      "computed by the Leviticus machinery",
                      machine_claim="EX12-17 (cross-book: the Tzav "
                      "round's flesh-purity file)", **IP)]
        if q == "impure_pesach_temple_entry":
            return [V("eating_only_exempt", "the mishnah's first "
                      "row exempts the EATING alone (95b:10)",
                      authority="the first authority (the mishnah)",
                      machine_claim="EX12-17", **IP),
                    V("entry_also_exempt", "R. Eliezer: even on "
                      "Temple ENTRY — 'they shall expel from the "
                      "camp every leper, every flux-bearer, every "
                      "corpse-impure' (Num 5:2): when the "
                      "corpse-impure are expelled, flux-bearers "
                      "are; when not, not (95b:11, 95b:14)",
                      authority="R. Eliezer", **IP)]
        if q == "impure_pesach_portions":
            return [V("follow_the_flesh", "Rava: the portions' "
                      "impurity was INCLUDED from the flesh's — "
                      "'which is TO THE LORD' (Lev 7:20) brought "
                      "the portions in — so where flesh-impurity "
                      "is permitted, portions-impurity is "
                      "permitted; the included never outruns its "
                      "includer (95b:18-96a:3)",
                      machine_claim="EX12-17 (cross-book)", **IP)]
        if q == "impure_pesach_part_camp":
            return [V("sanctuary_hall_barred", "Rav Yosef's "
                      "dilemma — flux-bearers pressed into the "
                      "sanctuary hall at an impure Passover — "
                      "answered by Rava both ways recorded: 'they "
                      "shall expel from the CAMP' — even PART of "
                      "the camp; and wherever 'outside the camp "
                      "you shall expel' is read, the expulsion is "
                      "read (95b:15-17): what was permitted was "
                      "permitted, the hall was not",
                      machine_claim="EX12-17", **IP)]
        return None

    # ------------------------------------------- Egypt's own rite
    ER = _EX("Pesachim 96a:4-6 (the portions question; Rav Yosef's "
             "altars; the two-era mishnah's sprinkling row)",
             "Exod.12.7 + 12.22 (exo_12_passover_and_exodus, the "
             "blood rite; F-072 seats the rite file as EX12-31)")

    def rule_egypt_rite(case):
        q = case.get("query")
        if q == "egypt_altars":
            return [V("three_doorway_altars", "Rav Yosef taught: "
                      "THREE ALTARS were there — on the lintel and "
                      "on the two doorposts — and nothing more "
                      "(96a:5): the doorway was the altar of the "
                      "Egypt rite; the blood of 12:7/12:22 landed "
                      "on altar surfaces",
                      machine_claim="EX12-31 (F-072)", **ER)]
        if q == "egypt_portions_fate":
            return [V("perhaps_roasted_whole", "R. Zeira: where "
                      "were Egypt's portions burned? Abaye: who "
                      "says they did not roast the lamb WHOLE "
                      "(שוויסקי — the whole-roast)? no altar "
                      "service to owe (96a:4)",
                      machine_claim="EX12-31 (F-072)", **ER)]
        if q == "egypt_sprinkling":
            return [V("hyssop_egypt_only", "the two-era mishnah's "
                      "row: Egypt's Passover required the "
                      "hyssop-bundle sprinkling on lintel and "
                      "doorposts; the generations' does not "
                      "(96a:6) — EX12-21's standing table",
                      machine_claim="EX12-21", **ER)]
        return None

    return {
        "two_era_export": {"fn": rule_export},
        "second_pesach_statute": {"fn": rule_statute},
        "impure_pesach_carveouts": {"fn": rule_carveouts},
        "egypt_rite": {"fn": rule_egypt_rite},
    }
