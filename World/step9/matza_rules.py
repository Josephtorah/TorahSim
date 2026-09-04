#!/usr/bin/env python3
"""matza_rules.py — round 18: MATZA, HERBS, AND THE TELLING, the
seventh Exodus Talmud-first exam block (2026-09-04). Eight modules
over Exodus 12:8, 12:17-20, 13:3-16 — the Passover family's
eating-side wing plus the consecration chapter's tefillin file.
engine.py merges build(V) at its tail.
Read-source record: logic/oral_triage/exodus_block_matza_2026-09-04.md."""


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    # ---------------------------------------- the tefillin's housing
    TH = _EX("Menachot 34b:1-5 (the totafot count; the head's one-"
             "hide housing; the arm's one sign) + 37a:2-4 (the "
             "weak-arm heh) + 29b:1-2 (the severed letters) + "
             "44a:16 (the eight positives)",
             "Exod.13.9 + 13:16 (exo_13_consecration_and_pillars, "
             "EX13-15 the received form + EX13-04 the heh's census "
             "— ANTICIPATED; F-067 seats the derivation file)")

    def rule_housing(case):
        q = case.get("query")
        if q == "totafot_compartments":
            return [V("four_from_ketiv", "R. Yishmael counts the "
                      "spellings: לטטפת ('totafot') defective here "
                      "(13:16), defective at Deut 6:8, FULL at Deut "
                      "11:18 — four mentions, four compartments (the "
                      "scribal datum EX13-15 holds, at its "
                      "derivation)", authority="R. Yishmael",
                      machine_claim="EX13-15", **TH),
                    V("four_from_loanword", "tot = two in Katfei, "
                      "pat = two in Afriki — the word itself says "
                      "four (R. Akiva)", authority="R. Akiva",
                      machine_claim="EX13-15", **TH)]
        if q == "tefillin_head_hides":
            return [V("four_in_one_hide", "four passages on four "
                      "hides in four compartments OF ONE HIDE — "
                      "לזכרון ('for a memorial,' 13:9) singular: one "
                      "memorial, not two or three; one-hide-slit "
                      "fulfills (Rebbi requires the spaces; the "
                      "Rabbis not; furrows visible or unfit)",
                      machine_claim="EX13-17", **TH)]
        if q == "tefillin_arm_hides":
            return [V("one_hide_one_sign", "the arm written on ONE "
                      "hide — לאות ('for a sign') singular: one sign "
                      "outside, one inside (four-hide writing "
                      "fulfills; R. Yehuda requires attachment, R. "
                      "Yosei not)", machine_claim="EX13-17", **TH)]
        if q == "tefillin_arm_side":
            return [V("left_from_keha", "ידכה written WITH THE HEH — "
                      "read yad KEHA, the WEAK arm = the left (Rav "
                      "Ashi; the chet-alternative refused at the "
                      "spelling); the tannaic fork spends the same "
                      "heh on the stump inclusion — EX13-04's ink "
                      "note become law",
                      authority="Rav Ashi (the ketiv route)",
                      machine_claim="EX13-04 (EX13-17 seats)", **TH),
                    V("left_from_bind_write", "R. Natan: writing is "
                      "with the right, binding with the right — so "
                      "donning on the left (the route that needs no "
                      "spelling)", authority="R. Natan",
                      machine_claim="EX13-17", **TH)]
        if q == "tefillin_positives_census":
            return [V("eight", "arm and head in each of the FOUR "
                      "passages (13:9, 13:16, Deut 6:8, Deut 11:18) "
                      "— eight positive commands violated by the "
                      "bare-headed arm (Rav Sheshet, 44a:16); "
                      "one-of-two: don what you have (Rav Chisda's "
                      "retraction)", machine_claim="EX13-17", **TH)]
        if q == "severed_letter_test":
            return [V("child_reads", "the severed vav of ויהרג ('and "
                      "He slew,' 13:15): bring a child neither wise "
                      "nor foolish — reads 'slew,' fit; reads 'will "
                      "be slain,' unfit (R. Zeira); the severed heh "
                      "of העם (13:3) fit if a small-letter's measure "
                      "remains (R. Abba) — the average reader as the "
                      "ink-validity oracle",
                      machine_claim="EX13-17", **TH)]
        return None

    # ------------------------------- the material, place, time, engine
    TR = _EX("Shabbat 108a:11-12 (the material table + the "
             "Boethusian) + Makkot 11a:8-9 (the Torah juxtaposed; "
             "sinews) + Arakhin 19b:5-7 (the registers) + Eruvin "
             "96a:10-11 (the time forks) + Kiddushin 35a:4-6 (the "
             "women's engine)",
             "Exod.13.9 (exo_13_consecration_and_pillars, EX13-17 "
             "seats — F-067; EX13-08's le-moadah beside the time "
             "sugya)")

    def rule_regime(case):
        q = case.get("query")
        if q == "tefillin_material":
            return [V("permitted_to_your_mouth", "written only on "
                      "the hide of species PERMITTED TO YOUR MOUTH — "
                      "למען תהיה תורת יהוה בפיך ('that the LORD's "
                      "Torah be in your mouth,' 13:9); kosher "
                      "carcasses and mortally-stricken INCLUDED "
                      "(died by the King's own hand — the parable); "
                      "wrapped with their hair, sewn with their "
                      "sinews — the sewing a halachah to Moses from "
                      "Sinai (the data channel self-labeled); the "
                      "whole-Torah juxtaposition carries the rule to "
                      "scroll sheets (Makkot 11a:8, Rav's linen "
                      "testimony overruled)",
                      machine_claim="EX13-17", **TR)]
        if q == "tefillin_placement_height":
            return [V("biceps", "ידכה at the tefillin = the BICEPS "
                      "(the school of Menashe, kibborit); the "
                      "hand-word's three registers: Torah = the "
                      "upper arm, vows follow speech (the elbow), "
                      "the Temple washing = the wrist (received) — "
                      "one word, declared scopes",
                      machine_claim="EX13-17", **TR)]
        if q == "tefillin_time_shabbat":
            return [V("excluded_days_are_signs", "R. Akiva: לאות "
                      "('for a sign') — worn when a sign is NEEDED; "
                      "Shabbat and festivals are THEMSELVES signs, "
                      "excluded", authority="R. Akiva",
                      machine_claim="EX13-17", **TR),
                    V("shabbat_fit_time", "R. Natan's line: the "
                      "night is fit (keep or remove at will), hence "
                      "Shabbat fit too (Yonatan HaKitoni bars the "
                      "night — both edges dual-tracked)",
                      authority="R. Natan", machine_claim="EX13-17",
                      **TR)]
        if q == "women_timebound_engine":
            return [V("exempt_by_juxtaposition", "the Pafunya route "
                      "(Rav Acha bar Yaakov): the whole Torah "
                      "juxtaposed to tefillin — time-bound and women "
                      "exempt, so women exempt from EVERY positive "
                      "time-bound command and obligated in the rest; "
                      "matza is the counter-exemplar women DO owe "
                      "(the two-verses-as-one frame); on R. Meir's "
                      "not-time-bound tefillin the engine fails — "
                      "the dependency recorded",
                      machine_claim="EX13-17", **TR)]
        if q == "tefillin_coming_term":
            return [V("reward_reading", "the coming term at 13:11 — "
                      "the school of R. Yishmael: perform this "
                      "command, and by its merit ENTER the land",
                      machine_claim="EX13-17", **TR)]
        return None

    # ---------------------------------------- the matza obligation
    MO = _EX("Pesachim 120a:6-13 (Rava's grade split; the "
             "singled-seventh; the first night saved) + 28b:10-12 "
             "(the post-Temple routes; the impure and the "
             "traveler) + Kiddushin 37b:12 (the dwellings scope)",
             "Exod.12.15 + 12:18 + 12:20 (exo_12_passover_and_exodus, "
             "EX12-04 the lean ketiv of the anchor verse; EX12-29 "
             "seats — F-069)",
             mishnah="Mishnah Pesachim 10:5 (the trio's mishnah)")

    def rule_obligation(case):
        q = case.get("query")
        if q == "matza_first_night":
            return [V("torah_grade_matza_rabbinic_herbs", "Rava: "
                      "matza nowadays TORAH-GRADE from בערב תאכלו "
                      "מצת ('in the evening you shall eat matzot,' "
                      "12:18) — an anchor independent of the lamb; "
                      "herbs rabbinic (Num 9:11 lamb-dependent)",
                      authority="Rava", machine_claim="EX12-29",
                      **MO),
                    V("both_rabbinic", "Rav Acha bar Yaakov: both "
                      "rabbinic nowadays — 12:18 re-spent on the "
                      "impure and the distant traveler",
                      authority="Rav Acha bar Yaakov",
                      machine_claim="EX12-29", **MO)]
        if q == "matza_seven_days":
            return [V("six_optional_first_night_owed", "the seventh "
                      "singled out of 'seven days you shall eat' "
                      "(12:15) by Deut 16:8's SIX — teaching about "
                      "the whole generalization: optional all seven "
                      "— except the FIRST NIGHT, saved by Num 9:11's "
                      "'with matzot and herbs they shall eat it' "
                      "(the middah and its carve-back, 120a:11-13)",
                      machine_claim="EX12-29", **MO)]
        if q == "matza_post_temple":
            return [V("both_routes_recorded", "R. Yehuda: the "
                      "leaven-matza juxtaposition (leaven banned "
                      "now, matza owed now); R. Shimon: 12:18's "
                      "date-anchored evening command — two recorded "
                      "routes, one standing obligation",
                      machine_claim="EX12-29", **MO)]
        if q == "matza_impure_traveler":
            return [V("owed_matza_and_herbs", "the lamb-barred "
                      "still owe the night's bread: R. Yehuda from "
                      "12:18; R. Shimon from בו ('OF IT,' 12:48) — "
                      "the lamb alone the uncircumcised does not "
                      "eat, matza and herbs he eats",
                      machine_claim="EX12-29", **MO)]
        if q == "matza_dwellings_scope":
            return [V("everywhere_and_always", "בכל מושבתיכם ('in "
                      "all your dwellings,' 12:20): matza and herbs "
                      "owed with or without a Paschal offering, "
                      "everywhere (Kiddushin 37b:12) — the "
                      "dwellings term carrying the post-Temple "
                      "scope", machine_claim="EX12-29", **MO)]
        return None

    # ------------------------------------------- the guarded grain
    MM = _EX("Pesachim 38b:1-3 (the two exclusion routes) + "
             "40a:14-15 (the guard stage) + 36a:17-19 (first "
             "fruits)",
             "Exod.12.17 + 12:15 + 12:20 (exo_12_passover_and_exodus, "
             "EX12-29 seats — F-069)")

    def rule_material(case):
        q = case.get("query")
        if q == "matza_guarded":
            return [V("guarded_for_its_sake", "ושמרתם את המצות "
                      "('you shall GUARD the matzot,' 12:17): "
                      "guarded FOR THE SAKE of matza — the "
                      "nazirite's wafers and thanks-loaves excluded "
                      "(Rabba); Rav Yosef reaches the same exclusion "
                      "from 12:15's eatable-all-seven (the offering "
                      "loaves live a day) — two routes, both "
                      "baraita-backed", machine_claim="EX12-29",
                      **MM)]
        if q == "matza_guard_stage":
            return [V("from_the_grain", "Rava's reversal: soaking "
                      "the grain is A MITZVA — if not for soaking, "
                      "what needs guarding? guarding at the "
                      "kneading is no guarding; Rav Huna's "
                      "gentile-dough rule keeps the obligation's "
                      "bite on the guarded olive-bulk at the end",
                      machine_claim="EX12-29", **MM)]
        if q == "matza_first_fruits":
            return [V("excluded_by_habitations", "'in ALL your "
                      "habitations' (12:20) — first-fruits wheat "
                      "eatable only in Jerusalem, excluded (R. "
                      "Yosei HaGelili)",
                      authority="R. Yosei HaGelili",
                      machine_claim="EX12-29", **MM),
                    V("excluded_by_herbs_analogy", "R. Akiva: the "
                      "matza-herbs juxtaposition — herbs are no "
                      "first-fruits species, so matza need not be",
                      authority="R. Akiva", machine_claim="EX12-29",
                      **MM)]
        return None

    # ------------------------------------------------- the herbs
    HT = _EX("Pesachim 39a:12-14 (the plural, the bounds, the one "
             "bed)",
             "Exod.12.8 (exo_12_passover_and_exodus, EX12-09 the "
             "two-eatings verse; EX12-29 seats — F-069)")

    def rule_herbs(case):
        q = case.get("query")
        if q == "herbs_species":
            return [V("many_species_matza_bounded", "מררים ('bitter "
                      "herbS,' 12:8) — the plural licenses MANY "
                      "species (Abaye against one-bitterest and "
                      "two-only); bounded by the matza analogy: "
                      "tithe-purchasable, human food, many types "
                      "(the M-12 grammatical-number hook at its own "
                      "daf)", machine_claim="EX12-29", **HT)]
        if q == "herbs_planting":
            return [V("one_bed_one_class", "the listed species "
                      "plant in ONE BED — no diverse-kinds among "
                      "them (Rav): the species table is a botanical "
                      "class", machine_claim="EX12-29", **HT)]
        return None

    # ------------------------------------------------ the telling
    TT = _EX("Pesachim 116b:2-9 (the trio's mishnah; for-ME; the "
             "pointing; the lifting)",
             "Exod.13.8 (exo_13_consecration_and_pillars, EX13-18 "
             "seats — F-068; the trio anticipated at EX12-20)",
             mishnah="Mishnah Pesachim 10:5")

    def rule_telling(case):
        q = case.get("query")
        if q == "telling_self_view":
            return [V("every_generation_for_me", "בעבור זה עשה יהוה "
                      "לי ('because of this the LORD did for ME,' "
                      "13:8): every generation views itself as "
                      "having left — 'for me,' not 'for my "
                      "fathers'; Rava adds: say 'and He took US "
                      "out'", machine_claim="EX13-18 (EX12-20 "
                      "anticipated the trio)", **TT)]
        if q == "telling_pointing":
            return [V("blind_exempt_this_points", "זה ('THIS') "
                      "matched to 'THIS son of ours' at the "
                      "rebellious son — the blind cannot point, the "
                      "blind exempt from the telling (Rav Acha bar "
                      "Yaakov); the counter (blind Rav Yosef and "
                      "Rav Sheshet recited themselves) resolved by "
                      "the rabbinic-nowadays grade — the pointing "
                      "and the era-grade interlock",
                      machine_claim="EX13-18", **TT)]
        if q == "telling_lifting":
            return [V("lift_matza_herbs_never_meat", "lift the "
                      "matza and the herbs at their naming; NEVER "
                      "the meat — it would look like sacrificial "
                      "meat outside the Temple (Rava, 116b:7)",
                      machine_claim="EX13-18", **TT)]
        return None

    # ------------------------------------------ the night's clock
    NW = _EX("Pesachim 120b:4-6 (the midnight analogy) + 109b:4-6 "
             "(the watchings night) + 108a:3-5 (ben Beteira's "
             "window)",
             "Exod.12.8 + 12:42 + 12:6 (exo_12_passover_and_exodus, "
             "EX12-15 the watchings pair — ANTICIPATED; EX12-21 "
             "holds the midnight-vs-haste table; EX12-29 seats)")

    def rule_night(case):
        q = case.get("query")
        if q == "eating_deadline_analogy":
            return [V("midnight_by_night_night", "R. Elazar ben "
                      "Azarya: בלילה הזה ('on THAT night,' 12:8) "
                      "matched to the striking's 'that night' "
                      "(12:12), clocked at midnight (11:4) — eating "
                      "ends at MIDNIGHT; the mishnah's "
                      "hands-defiling-after-midnight rides it; R. "
                      "Akiva's until-haste stands beside in the "
                      "two-era table (EX12-21, credited)",
                      machine_claim="EX12-21", **NW)]
        if q == "watchings_night":
            return [V("pairs_concern_suspended", "ליל שמרים ('a "
                      "night of WATCHINGS,' 12:42): the guarded "
                      "night — the four cups pass the pairs "
                      "objection (Rav Nachman); Rava's "
                      "blessing-cup-for-good and Ravina's "
                      "each-cup-its-own-freedom beside it — three "
                      "recorded routes",
                      machine_claim="EX12-15 (EX12-29 seats)", **NW)]
        if q == "slaughter_whole_day":
            return [V("whole_day_valid", "ben Beteira: בין הערבים "
                      "('between the evenings,' 12:6) = between "
                      "yesterday's evening and today's — the whole "
                      "fourteenth fit; a morning slaughter "
                      "for-its-name VALID on his view (extends the "
                      "round-16 window module, credit noted)",
                      authority="ben Beteira",
                      machine_claim="EX12-29", **NW)]
        return None

    # ------------------------------------------- the frame lexicon
    FL = _EX("Pesachim 42a:4-5 (the lemor readings) + 113b:3-5 "
             "(the permitted hatred)",
             "Exod.12.1 (exo_12_passover_and_exodus, EX12-29 "
             "seats; the 23:5 anchor lives in exo_23's span — "
             "noted, unseated)")

    def rule_frame(case):
        q = case.get("query")
        if q == "lemor_frame":
            return [V("say_a_prohibition", "לאמר ('saying,' 12:1) — "
                      "the school of Rav: lav emor, 'say a "
                      "PROHIBITION': commands under the "
                      "saying-frame read as prohibitions (R. "
                      "Yehuda's lo-emor beside it)",
                      machine_claim="EX12-29", **FL)]
        if q == "permitted_hatred":
            return [V("lone_witness_may_hate", "שנאך ('he who HATES "
                      "you,' 23:5) fixed on a JEW — the lone "
                      "witness to a sin may hate (the Lev 19:17 "
                      "tension resolved at the witnessed-sin case); "
                      "foreign span: serves exo_23, "
                      "talmud_source-only, unseated",
                      machine_claim="talmud_source only (the Exod "
                      "23:5 anchor lives in exo_23's span)", **FL)]
        return None

    return {
        "tefillin_housing": {"fn": rule_housing},
        "tefillin_regime": {"fn": rule_regime},
        "matza_obligation": {"fn": rule_obligation},
        "matza_material": {"fn": rule_material},
        "herbs_table": {"fn": rule_herbs},
        "the_telling": {"fn": rule_telling},
        "night_and_window": {"fn": rule_night},
        "frame_lexicon": {"fn": rule_frame},
    }
