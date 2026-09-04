#!/usr/bin/env python3
"""calendar_rules.py — round 22: THE CALENDAR, the eleventh Exodus
Talmud-first exam block (2026-09-04). Four modules — the calendar's
machinery on Exodus's ink. engine.py merges build(V) at its tail.
Read-source: logic/oral_triage/exodus_block_calendar_2026-09-04.md."""


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    # -------------------------------------------- Nisan for kings
    NK = _EX("Rosh Hashanah 3a:2-13 (the chronology chain, ten "
             "rungs)",
             "Exod.40.17 + 19.1 (exo_40_erect_fill, EX40-07 — "
             "F-082: the erection date as the chain's load-bearing "
             "rung)")

    def rule_kings(case):
        q = case.get("query")
        if q == "kings_year_head":
            return [V("nisan_by_verse_ladder", "kings are counted "
                      "only from NISAN — R. Yochanan's baraita "
                      "walks a TEN-RUNG verse ladder (the 480th "
                      "year, Aaron's ascent, the fortieth-year "
                      "eleventh month, after-Sihon, the Canaanite "
                      "heard, the congregation saw, the ERECTION "
                      "verse, the cloud verse, the THIRD-MONTH "
                      "verse, the Chronicles reign-verse) — a "
                      "chronology proof assembled across five "
                      "books (3a:11-13)",
                      machine_claim="EX40-07", **NK)]
        if q == "chain_exodus_rungs":
            return [V("year_label_unmoved", "the two Exodus rungs "
                      "kill the alternatives: 'in the FIRST month "
                      "of the SECOND year the tabernacle was "
                      "erected' (40:17) beside 'in the SECOND year "
                      "in the SECOND month the cloud lifted' (Num "
                      "10:11) — the year-label did NOT flip "
                      "between Nisan and Iyar, so Iyar heads no "
                      "year (3a:5); and 'in the THIRD month of the "
                      "going-out' (19:1) lacks a year-clause — "
                      "were Sivan a head it would need one (3a:6): "
                      "one rung by a label that held, one by a "
                      "clause that is absent",
                      machine_claim="EX40-07", **NK)]
        return None

    # -------------------------------------- the intercalation machine
    IM = _EX("Sanhedrin 12b:6-13b:4 (only Adar; the equinox arms) "
             "+ Rosh Hashanah 13a:1-4 (the seam)",
             "Exod.34.21-22 + 12.2 + 23.16 (exo_34_second_tablets, "
             "EX34-08 — F-081; the 23:16 seam row named for "
             "exo_23)")

    def rule_intercalation(case):
        q = case.get("query")
        if q == "only_adar_intercalated":
            return [V("this_is_nisan_no_other", "ONLY ADAR is "
                      "intercalated — 'THIS month is for you' "
                      "(12:2): THIS one is Nisan and NO OTHER is "
                      "Nisan; the recorded royal violation: "
                      "Hezekiah intercalated Nisan-in-Nisan and "
                      "prayed for mercy — his error at Shmuel's "
                      "thirtieth-of-Adar rule (fit-to-be-Nisan "
                      "already bars it) (12b:8-9); R. Shimon's "
                      "alternative charge kept beside (the second "
                      "Passover he led, 12b:10)",
                      machine_claim="EX12-22 (the court "
                      "commission) + EX12-32", **IM)]
        if q == "equinox_rule":
            return [V("whole_festival_sixteen", "'the festival of "
                      "the ingathering at the TURN of the year' "
                      "(34:22): the WHOLE festival must fall in "
                      "the new season — a sixteen-day shortfall "
                      "intercalates (13a:1; the equinox day "
                      "COMPLETES the season, 13a:3)",
                      authority="R. Yehuda",
                      machine_claim="EX34-08", **IM),
                    V("part_festival_twentyone", "PART of the "
                      "festival suffices — twenty-one days; the "
                      "equinox day BEGINS the season (13a:1-3)",
                      authority="R. Yosei", **IM),
                    V("fourteen_days_two_placements", "fourteen "
                      "days — read either at NISAN's equinox "
                      "('keep the month of the SPRING,' Deut 16:1: "
                      "the spring turning must fall in Nisan, Rav "
                      "Shmuel bar Yitzchak) or at Tishrei with the "
                      "whole festival plus its first day (Ravina) "
                      "— both placements preserved (13b:2-4)",
                      authority="Acherim (the others)", **IM)]
        if q == "year_seam_third":
            return [V("third_before_rosh_hashanah", "'at the "
                      "going-OUT of the year' (23:16): asif read "
                      "as HARVEST — grain reaped at the festival "
                      "is known to have reached a THIRD of its "
                      "growth before Rosh Hashanah, and the verse "
                      "calls that moment the year's exit — the "
                      "seam fixed at Tishrei with a growth "
                      "threshold beneath it; R. Zeira's answer to "
                      "the precision challenge: 'ALL the Sages' "
                      "measures are thus' — the data channel "
                      "self-labeled at the calendar's seam "
                      "(13a:2-4; the 23:16 row named for exo_23)",
                      machine_claim="EX34-08", **IM)]
        return None

    # ------------------------------------------- month mechanics
    MM = _EX("Rosh Hashanah 20a:14-16 (add vs sanctify) + "
             "20b:9-12 (the day boundary) + 25a:3-6 (the "
             "authority story)",
             "Exod.12.2 + 12.18 + 24.9 (exo_12_passover_and_exodus "
             "EX12-32 — F-080; exo_24_covenant_ascent EX24-07 — "
             "F-019's seat, ANTICIPATED)")

    def rule_mechanics(case):
        q = case.get("query")
        if q == "month_add_vs_sanctify":
            return [V("stretch_never_fabricate", "'THIS month is "
                      "for you — LIKE THIS see and sanctify' "
                      "(12:2): the month is sanctified by SIGHT; "
                      "Rava's split — the court may ADD a day at "
                      "need but never SANCTIFY at need (20a:14-15); "
                      "enacted at the witnesses: press them to "
                      "DELAY a timely sighting, never to affirm an "
                      "unseen moon (R. Yehoshua ben Levi, 20a:16) — "
                      "the court stretches, never fabricates",
                      machine_claim="EX12-32 (EX12-22's commission "
                      "— ANTICIPATED surface)", **MM)]
        if q == "day_boundary_source":
            return [V("evening_to_evening", "night-and-day belong "
                      "to the month — from 'from evening to "
                      "evening' (Lev 23:32) (20b:9)",
                      authority="R. Yochanan",
                      machine_claim="EX12-32", **MM),
                    V("twentyfirst_at_evening", "from THIS book's "
                      "ink: 'until the twenty-first day of the "
                      "month AT EVENING' (12:18) — the day follows "
                      "the night at the matza-window's own clause "
                      "(20b:10); Abaye — the arms differ only in "
                      "exegesis; Rava — half-night between them "
                      "(20b:11-12)", authority="Reish Lakish",
                      **MM)]
        if q == "calendar_authority":
            return [V("every_court_as_moses", "the UNNAMED SEVENTY "
                      "(24:9): why are the elders' names not "
                      "given? — that every three who stand as a "
                      "court over Israel stand AS THE COURT OF "
                      "MOSES (R. Dosa, 25a:5); with R. Akiva's "
                      "you-shall-proclaim reading — in their time "
                      "or not, there are no appointed times but "
                      "those the court declares (25a:4) — and the "
                      "law enacted: R. Yehoshua's staff and money "
                      "carried on his own reckoned Yom Kippur "
                      "(25a:6)", machine_claim="EX24-07 (ANTICIPATED — F-019 seated the unnamed-seventy law in the Mishpatim round; the sugya arrived answered)", **MM)]
        return None

    # ------------------------------------------------ year seams
    YS = _EX("Rosh Hashanah 7a:17-18 (the shekels) + 9a:2-5 (the "
             "harvest rest) + Taanit 29a:2-4 (the Ninth of Av)",
             "Exod.12.2 + 34.21 + 40.17 (EX12-32 + EX34-08 + "
             "EX40-07)")

    def rule_seams(case):
        q = case.get("query")
        if q == "shekels_year_head":
            return [V("nisan_by_months_analogy", "the shekels' new "
                      "year: the month's offering comes from the "
                      "NEW terumah ('the burnt-offering of each "
                      "month... for the months of the YEAR') — and "
                      "year-year is learned from 'it is FIRST for "
                      "you for the months of the year' (12:2), NOT "
                      "from Tishrei's verse: derive a "
                      "year-with-months from a year-with-months — "
                      "the analogy-SELECTION rule on the record "
                      "(7a:17-18)", machine_claim="EX12-32", **YS)]
        if q == "harvest_rest_assignment":
            return [V("sabbatical_edges", "'in plowing and in "
                      "harvest you shall rest' (34:21): the "
                      "seventh year's own are already banned — so "
                      "the EVE-year's plowing entering it and the "
                      "seventh's harvest exiting it: sanctity "
                      "extended at both edges (9a:3)",
                      authority="R. Akiva",
                      machine_claim="EX34-08", **YS),
                    V("omer_excluded_shabbat", "as plowing is "
                      "optional so the harvest meant is optional — "
                      "the OMER harvest, a mitzva, excluded (and "
                      "overrides): the verse assigned to the "
                      "Sabbath (9a:4)", authority="R. Yishmael",
                      **YS)]
        if q == "ninth_av_computation":
            return [V("computed_from_erection_date", "the decree's "
                      "date COMPUTED from 40:17: erected on the "
                      "first of the first month of year two; the "
                      "cloud lifted the twentieth of the second "
                      "month; three days' journey, the craving "
                      "month, Miriam's seven days — twenty-nine of "
                      "Sivan; forty days of spying land the return "
                      "on the NINTH OF AV — the weeping night "
                      "computed to the day from this book's "
                      "closing chapter (Taanit 29a:2-4)",
                      machine_claim="EX40-07", **YS)]
        return None

    return {
        "nisan_for_kings": {"fn": rule_kings},
        "intercalation_machine": {"fn": rule_intercalation},
        "month_mechanics": {"fn": rule_mechanics},
        "year_seams": {"fn": rule_seams},
    }
