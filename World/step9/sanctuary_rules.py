#!/usr/bin/env python3
"""sanctuary_rules.py — round 26: SANCTUARY CONSTANTS, the
fifteenth Exodus Talmud-first exam block (2026-09-04). Five
modules — the ark file, the structure, the candelabrum's method
fork, the altar constants, the treasury and measures. engine.py
merges build(V) at its tail. Read-source:
logic/oral_triage/exodus_block_sanctuary_2026-09-04.md."""


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    # ---------------------------------------------- the ark file
    AR = _EX("Yoma 3b:2-4 + 72a:8-10 + 72b:6-8 + 52b:13-15",
             "Exod.25.8-15 (exo_25_ark_table_menorah, EX25-13 — "
             "F-098)")

    def rule_ark(case):
        q = case.get("query")
        if q == "taking_funding":
            return [V("private_lekha", "קח לך ('take YOURSELF') = "
                      "from your own; ויקחו אליך = from the "
                      "public (3b:2); the installation's "
                      "take-lekha proven from-your-own by the "
                      "goat/calf redundancy (3b:4)",
                      authority="R. Yoshiyah",
                      machine_claim="EX25-13", **AR),
                    V("public_endearment", "both from the public "
                      "— lekha is ENDEARMENT: 'as if from yours: "
                      "I want yours more than theirs' (3b:2)",
                      authority="R. Yonatan", **AR)]
        if q == "ark_verbs_harmonized":
            return [V("will_indexed_dispatch", "'you shall make "
                      "YOURSELF an ark' (Deut 10:1) against 'THEY "
                      "shall make an ark' (25:10) — here when "
                      "Israel does the Presence's will, here when "
                      "not (Abba Chanan per R. Elazar, 3b:3); the "
                      "second dispatch beside it: the scholar's "
                      "townspeople do his work (72b:8)",
                      authority="Abba Chanan per R. Elazar",
                      machine_claim="EX25-13", **AR)]
        if q == "crown_consonants":
            return [V("crown_or_estranged", "written זר "
                      "('stranger'), read זֵר ('crown'): merited "
                      "— it becomes his CROWN; not merited — it "
                      "becomes ESTRANGED from him (72b:7); the "
                      "three crowns beside it — altar Aaron's, "
                      "table David's, the ark's STILL LYING for "
                      "whoever will take it (72b:6)",
                      authority="R. Yochanan",
                      machine_claim="EX25-13", **AR)]
        if q == "staves_prohibitions":
            return [V("lashes_loose_not_slipping", "detaching the "
                      "breastplate (לא יזח, 28:28) and removing "
                      "the staves (לא יסרו, 25:15) — lashes both "
                      "(R. Elazar, 72a:9), Rav Acha bar Yaakov's "
                      "design-spec probe answered by the bare "
                      "negative both times; the contradiction "
                      "resolved as a mechanical spec — they "
                      "LOOSEN but do not SLIP OUT (R. Yosei b. R. "
                      "Chanina, 72a:10)",
                      machine_claim="EX25-13", **AR)]
        if q == "manna_jar_location":
            return [V("hidden_with_ark_three_chains", "R. Elazar: "
                      "שמה שמה ('there-there'), דורות דורות "
                      "('generations-generations'), משמרת משמרת "
                      "('keeping-keeping') — three verbal-analogy "
                      "chains from the jar's own verse (16:33-34) "
                      "to the ark's terms: the jar hidden WITH "
                      "the ark at Josiah's hiding (52b:13-15)",
                      authority="R. Elazar",
                      machine_claim="EX25-13", **AR)]
        return None

    # ------------------------------------------- the structure
    ST = _EX("Shabbat 98b:1-6; Yoma 51b:5-6 + 72b:18-19; Bava "
             "Batra 99a:6-7; Avodah Zarah 24a:2",
             "Exod.26 + 25.20 (exo_26_curtains_boards, EX26-07 — "
             "F-100)")

    def rule_structure(case):
        q = case.get("query")
        if q == "beam_taper":
            return [V("taper_to_fingerbreadth", "the beams a "
                      "cubit thick below, tapering to a "
                      "FINGERBREADTH — יהיו תמים על ראשו read "
                      "with תמו נכרתו ('ended, cut off') (98b:2); "
                      "the corner geometry shaped like mountains "
                      "(98b:4)",
                      authority="R. Yehuda",
                      machine_claim="EX26-07", **ST),
                    V("cubit_throughout", "a cubit throughout — "
                      "יחדו ('together/equal') (98b:2); tamim "
                      "re-read as whole-not-sawn (98b:3)",
                      authority="R. Nechemiah", **ST)]
        if q == "middle_bar":
            return [V("standing_miracle", "'the middle bar within "
                      "the beams from end to end' (26:28) — "
                      "taught: BY MIRACLE it stood — the bar "
                      "threading the three walls recorded as the "
                      "architecture's honest impossibility "
                      "(98b:5)",
                      machine_claim="EX26-07", **ST)]
        if q == "partition_count":
            return [V("two_curtains_second_temple", "the second "
                      "Temple lacked the first's cubit wall and "
                      "its status was doubtful (inside or "
                      "outside?) — they made TWO curtains a cubit "
                      "apart (51b:6)",
                      authority="the Rabbis",
                      machine_claim="EX26-07", **ST),
                    V("one_curtain_ink", "והבדילה הפרכת ('the "
                      "curtain shall DIVIDE,' 26:33) — only ONE "
                      "(51b:5); the Rabbis answer: that verse is "
                      "the Tabernacle's",
                      authority="R. Yosei", **ST)]
        if q == "cherub_faces":
            return [V("angled_student_teacher", "toward-each-"
                      "other against toward-the-House resolved "
                      "will-indexed (99a:6); and for the House "
                      "arm, 25:20's each-to-his-brother — ANGLED: "
                      "אונקלוס הגר ('Onkelos the convert') — "
                      "child-faced work, angled, 'like a STUDENT "
                      "TAKING LEAVE OF HIS TEACHER' (99a:7): the "
                      "corpus' own translator cited by name on "
                      "this unit's ink",
                      authority="Onkelos the convert (the baraita)",
                      machine_claim="EX26-07", **ST)]
        if q == "onyx_boundary":
            return [V("list_break_remixed", "אבני שהם without the "
                      "joining vav — THE MATTER BREAKS (the "
                      "contribution list's boundary); 'stones of "
                      "setting' re-mixed it (Avodah Zarah 24a:2): "
                      "the donation list's syntax ruled at the "
                      "letter grain",
                      machine_claim="EX26-07", **ST)]
        if q == "craft_words":
            return [V("needle_one_face_weave_two", "מעשה רקם "
                      "('embroiderer's work') against מעשה חשב "
                      "('designer's work') — R. Elazar: they "
                      "embroider where they design (72b:18); R. "
                      "Nechemiah's split: rokem = NEEDLE work, "
                      "one face; choshev = WEAVING, two faces "
                      "(72b:19)",
                      machine_claim="EX26-07", **ST)]
        return None

    # ---------------------------------- the candelabrum's fork
    CM = _EX("Sukkah 50b:5-7",
             "Exod.25.31 (exo_25_ark_table_menorah, EX25-14 — "
             "F-099)")

    def rule_candelabrum(case):
        q = case.get("query")
        if q == "candelabrum_method_fork":
            return [V("metal_by_general_detail", "ועשית מנורת "
                      "(general), זהב טהור (detail), מקשה תעשה "
                      "המנורה (general) — like the detail: OF "
                      "METAL, all metals valid (50b:6)",
                      authority="Rebbi (general-and-detail)",
                      machine_claim="EX25-14", **CM),
                    V("all_but_earthenware", "amplified, limited, "
                      "amplified — amplified ALL, excluded only "
                      "EARTHENWARE (50b:7): the SAME verse "
                      "through the rival engine, a different "
                      "valid-materials table — middah governance "
                      "measured on the unit's own ink (the fork "
                      "named at 50b:5)",
                      authority="R. Yosei b. R. Yehuda "
                      "(amplify-and-limit)", **CM)]
        return None

    # ------------------------------------- the altar constants
    AL = _EX("Zevachim 53a:8-10 + 62a:7-9; Sanhedrin 34b:1-2",
             "Exod.27.1-5 (exo_27_altar_court, EX27-09 — F-101)")

    def rule_altar(case):
        q = case.get("query")
        if q == "red_line":
            return [V("torah_gave_partition", "the crimson thread "
                      "girds the altar at its MIDDLE dividing "
                      "upper bloods from lower — והיתה הרשת עד "
                      "חצי המזבח ('the net shall reach to the "
                      "HALF of the altar,' 27:5): THE TORAH GAVE "
                      "THE PARTITION (Rav Acha bar Rav Katina, "
                      "53a:9)",
                      authority="Rav Acha bar Rav Katina",
                      machine_claim="EX27-09", **AL)]
        if q == "altar_indispensables":
            return [V("corner_ramp_base_square", "CORNER, RAMP, "
                      "BASE, and SQUARE indispensable; the "
                      "measures not — המזבח ('THE altar'): "
                      "wherever the definite article stands, it "
                      "binds (Rav Huna, 62a:8); the karkov's "
                      "referent recorded both ways — Rebbi's "
                      "kiyor, R. Yosei b. R. Yehuda's ledge "
                      "(62a:9)",
                      authority="Rav Huna",
                      machine_claim="EX27-09", **AL)]
        if q == "altar_touch_scope":
            return [V("suited_only_two_sources", "'whatever "
                      "touches the altar becomes holy' (29:37) "
                      "bounded by the NEXT verse — as LAMBS "
                      "(29:38) are suited, so all: only the "
                      "suited is sanctified by touch; R. Akiva "
                      "binds it from olah (29:25) — two sources, "
                      "one bound, their exclusion-delta recorded "
                      "(Sanhedrin 34b:1-2)",
                      machine_claim="EX27-09", **AL)]
        return None

    # -------------------------------- the treasury and measures
    TR = _EX("Bekhorot 5a:17-19; Temurah 31b:6-8; Tamid 31b:9-11",
             "Exod.38.29 + 25.8 + 25.23 (exo_38_court_inventory "
             "EX38-08 + exo_25 EX25-14 — F-102/F-099)")

    def rule_treasury(case):
        q = case.get("query")
        if q == "sanctuary_maneh":
            return [V("double_computed_from_surplus", "'the brass "
                      "of the offering: seventy talents and 2,400 "
                      "shekels' (38:29) — ninety-six maneh stand "
                      "there COUNTED IN SMALL CHANGE rather than "
                      "rounded to a talent: the sanctuary maneh "
                      "was DOUBLE — the metrological constant "
                      "computed from the inventory's own refusal "
                      "to round, argued at both edges (Bekhorot "
                      "5a:17-19)",
                      machine_claim="EX38-08", **TR)]
        if q == "craftsmen_payment":
            return [V("maintenance_not_altar", "craftsmen are "
                      "paid from MAINTENANCE consecrations, not "
                      "altar consecrations — ועשו לי ('they shall "
                      "make ME,' 25:8) read 'from what is MINE' "
                      "(R. Abahu, Temurah 31b:7): the treasury "
                      "split at the sanctuary verse",
                      authority="R. Abahu",
                      machine_claim="EX25-14", **TR)]
        if q == "table_promotion":
            return [V("promote_never_demote", "the shewbread's "
                      "path — silver table entering, gold "
                      "exiting, the golden table always inside: "
                      "מעלין בקודש ולא מורידין ('promote in "
                      "sanctity, never demote,' Tamid 31b:9-10); "
                      "the exception's physics recorded — marble "
                      "at the entry because metal SCALDS "
                      "(31b:11)",
                      machine_claim="EX25-14", **TR)]
        return None

    return {
        "ark_and_making": {"fn": rule_ark},
        "structure_machine": {"fn": rule_structure},
        "candelabrum_method": {"fn": rule_candelabrum},
        "altar_constants": {"fn": rule_altar},
        "treasury_and_measures": {"fn": rule_treasury},
    }
