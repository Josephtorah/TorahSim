#!/usr/bin/env python3
"""service_rules.py — round 28: THE SERVICE ORDER, the seventeenth
Exodus Talmud-first exam block (2026-09-04). Five modules — the
lamp, the morning order, the laver, the corners, the oil and
incense. engine.py merges build(V) at its tail. Read-source:
logic/oral_triage/exodus_block_service_2026-09-04.md."""


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    # ------------------------------------------------- the lamp
    LP = _EX("Shabbat 21a:8-10; Yoma 45b:6-8; Pesachim 59a:1-4; "
             "Zevachim 11b:29-31",
             "Exod.27.20-21 (exo_27_altar_court, EX27-10 — F-106)")

    def rule_lamp(case):
        q = case.get("query")
        if q == "self_ascending_flame":
            return [V("temple_wick_oil_bar", "wicks and oils the "
                      "sages barred for Shabbat may not be lit IN "
                      "THE TEMPLE — להעלות נר תמיד ('to cause a "
                      "lamp to ASCEND continually'): the flame "
                      "must ascend BY ITSELF, not by another "
                      "thing (Rami bar Chama, Shabbat 21a:9; the "
                      "worn-trousers objection answered at the "
                      "water-drawing, 21a:10)",
                      authority="Rami bar Chama",
                      machine_claim="EX27-10", **LP)]
        if q == "perpetual_fire_source":
            return [V("outer_altar_head", "אש תמיד — 'the "
                      "PERPETUAL fire I told you of shall be only "
                      "on the head of the OUTER altar' (Yoma "
                      "45b:7); the menorah's fire fetched FROM it "
                      "by the fire-fire analogy through the pan "
                      "(45b:8): the lamp lit from the altar",
                      machine_claim="EX27-10", **LP)]
        if q == "lamp_oil_quota":
            return [V("measure_for_the_night", "מערב ועד בקר — "
                      "GIVE IT ITS MEASURE, that it burn from "
                      "evening to morning (Pesachim 59a:3 = "
                      "Zevachim 11b:30): the clause read as the "
                      "oil's quota",
                      machine_claim="EX27-10", **LP)]
        if q == "lamps_last":
            return [V("only_overnight_service", "אתו ('IT') — no "
                      "service is valid from evening to morning "
                      "but THIS alone (59a:4): the lamps close "
                      "the day's order, the oto-token the "
                      "order's seal",
                      machine_claim="EX27-10", **LP)]
        return None

    # ----------------------------------------- the morning order
    MO = _EX("Yoma 14b:8-9 + 62b:10-13; Pesachim 59a:2 + 59a:8-10",
             "Exod.29.38-39 + 30.7-8 (exo_29_investiture EX29-15 "
             "+ exo_30_incense_shekel EX30-11 — F-107/F-108; the "
             "schedule held at EX30-01, the heartbeat at EX29-08)")

    def rule_order(case):
        q = case.get("query")
        if q == "incense_first":
            return [V("doubled_morning_precedes", "nothing "
                      "precedes the morning daily offering EXCEPT "
                      "the incense — of it is written בבקר בבקר "
                      "('in the morning, in the morning,' 30:7): "
                      "the DOUBLED morning precedes the single "
                      "(Pesachim 59a:9); the day's closing "
                      "bracket listed — incense, lamps, pesach, "
                      "the bather (59a:10)",
                      machine_claim="EX30-11", **MO)]
        if q == "tend_burn_order":
            return [V("tend_then_burn", "בבקר בבקר בהיטיבו את "
                      "הנרות והדר יקטירנה — when he TENDS the "
                      "lamps, and then he shall burn: the verse's "
                      "own sequence (Yoma 14b:9); the arrangement "
                      "interrupts the lamps with the INCENSE "
                      "(14b:8)",
                      authority="Abba Shaul",
                      machine_claim="EX30-11", **MO),
                    V("burn_then_tend", "burn and then tend — the "
                      "clause read otherwise; the arrangement "
                      "interrupts with the daily offering's BLOOD "
                      "(14b:8-9)",
                      authority="the Rabbis", **MO)]
        if q == "daily_lambs_equality":
            return [V("equal_for_mitzvah_valid_unequal", "כבשים — "
                      "the plural's minimum, TWO; Numbers 28:3's "
                      "'two' teaches BOTH EQUAL; unequal still "
                      "valid by the doubled כבש כבש: equal for "
                      "the MITZVAH, valid otherwise (Yoma 62b:11) "
                      "— the grade split on the daily heartbeat",
                      machine_claim="EX29-15", **MO)]
        if q == "lambs_sun_position":
            return [V("opposite_the_day", "שנים ליום — two "
                      "AGAINST THE DAY: the morning lamb at the "
                      "northwest corner, the afternoon at the "
                      "northeast — the slaughter positioned by "
                      "the light; the day's-duty alternative "
                      "excluded, the token freed (62b:12-13)",
                      machine_claim="EX29-15", **MO)]
        return None

    # ------------------------------------------------ the laver
    LV = _EX("Yoma 32b:9-11; Sanhedrin 83b:15-17",
             "Exod.30.20 (exo_30_incense_shekel, EX30-11 — "
             "F-108; the wash-as-sanctify layer held at EX30-05)")

    def rule_laver(case):
        q = case.get("query")
        if q == "dress_wash_order":
            return [V("dress_then_wash", "all agree at the SECOND "
                      "sanctification he dresses and then washes "
                      "— או בגשתם אל המזבח ('or when they "
                      "APPROACH'): one lacking only approach "
                      "washes — excluded he who lacks dressing "
                      "AND approach (Rav Acha bar Yaakov, Yoma "
                      "32b:10)",
                      authority="Rav Acha bar Yaakov",
                      machine_claim="EX30-11", **LV)]
        if q == "unwashed_death":
            return [V("death_by_the_lavers_clause", "unwashed "
                      "hands and feet serving — death: 'they "
                      "shall WASH with water, THAT THEY DIE NOT' "
                      "(30:20, Sanhedrin 83b:16): the laver's own "
                      "death clause as the service bar",
                      machine_claim="EX30-11", **LV)]
        return None

    # ------------------------------------------- the corners
    AC = _EX("Yoma 58a:1-2; Shevuot 8b:8-10",
             "Exod.30.10 (exo_30_incense_shekel, EX30-11 — "
             "F-108; the annual protocol held at EX30-03)")

    def rule_corners(case):
        q = case.get("query")
        if q == "corner_bloods":
            return [V("separate_presentations", "this by itself "
                      "and this by itself — 'of the bull's blood "
                      "AND of the goat's blood' stands written; "
                      "why 'once'? — once and not twice from "
                      "each (Yoma 58a:1-2)",
                      authority="R. Yonatan",
                      machine_claim="EX30-11", **AC),
                    V("mixed_presentation", "has it not already "
                      "said אחת ('ONCE')? — one presentation, the "
                      "bloods mixed (58a:1)",
                      authority="R. Yoshiyah", **AC)]
        if q == "once_tokens":
            return [V("two_exclusions_one_year", "the inner goat "
                      "for the outer's charge? אחת — ONE "
                      "atonement, not two; the outer for the "
                      "inner's? אחת בשנה — not twice in the year "
                      "(Shevuot 8b:9-10): the clause's two tokens "
                      "performing two exclusions in the "
                      "atonement algebra",
                      machine_claim="EX30-11", **AC)]
        return None

    # --------------------------------- the money, oil, incense
    OI = _EX("Bekhorot 50a:2-4; Horayot 11b:9-11; Keritot 3a:2-4 "
             "+ 5a:25-27 + 6b:6-8 + 7a:5-7",
             "Exod.30.13 + 30.31-34 (exo_30_incense_shekel, "
             "EX30-11 — F-108; the anti-duplication clauses held "
             "at EX30-06, the denominations at EX30-09/10)")

    def rule_oil(case):
        q = case.get("query")
        if q == "sela_conversion":
            return [V("computed_through_the_translation", "Rava: "
                      "Torah selas are three-and-a-third denars — "
                      "עשרים גרה השקל ('twenty gera the shekel,' "
                      "30:13), ומתרגמינן ('AND WE TRANSLATE') "
                      "twenty MA'IN, and six ma'a to the denar "
                      "(Bekhorot 50a:3): the Talmud computing "
                      "THROUGH Onkelos' unit conversion — the "
                      "corpus' conversion layer confirmed at the "
                      "source; the inflation objection "
                      "reconciled (50a:4)",
                      authority="Rava",
                      machine_claim="EX30-11", **OI)]
        if q == "anointing_inheritance":
            return [V("priests_son_yes_kings_son_no", "even a "
                      "High Priest son of a High Priest REQUIRES "
                      "anointing; kings are not anointed "
                      "son-after-father (Solomon, Joash, Jehoahaz "
                      "— each only against a dispute); and THAT "
                      "oil remains — זה ('THIS') in letter-values "
                      "TWELVE: the twelve logs endure (Horayot "
                      "11b:10-11): the succession gate with the "
                      "letter arithmetic carrying the perpetuity",
                      machine_claim="EX30-11", **OI)]
        if q == "two_bans_one_karet":
            return [V("sin_offering_divides", "wherever TWO "
                      "prohibitions share ONE karet, the "
                      "sin-offering DIVIDES between them — the "
                      "compounder and the anointer: not-poured + "
                      "not-made (30:32) under one excision clause "
                      "(30:33) (R. Elazar per R. Hoshaya, Keritot "
                      "3a:3): the division rule at the oil verses",
                      authority="R. Elazar per R. Hoshaya",
                      machine_claim="EX30-11", **OI)]
        if q == "hp_own_flesh":
            return [V("liable_status_never_discharges", "the High "
                      "Priest who took oil from HIS OWN HEAD to "
                      "his stomach — liable: על בשר אדם לא ייסך, "
                      "even the anointed flesh (Keritot 7a:6); "
                      "against terumah oil (profaned once "
                      "misused) — the anointing oil NEVER loses "
                      "status: 'the crown of his God's oil is "
                      "upon him' (7a:7)",
                      machine_claim="EX30-11", **OI)]
        if q == "eleven_spices":
            return [V("stated_at_sinai_counted_from_tokens", "R. "
                      "Yochanan: ELEVEN spices were STATED TO "
                      "MOSES AT SINAI — the list partly "
                      "unwritten; Rav Huna counts it from the "
                      "verse's own tokens (spices two, three "
                      "named, spices doubled to ten, frankincense "
                      "eleven — Keritot 6b:7): the data channel "
                      "self-labeled at our verse; the rival "
                      "general-detail-general read beside it — "
                      "what rises in smoke and smells (6b:8): the "
                      "method-fork family's third seat",
                      authority="R. Yochanan (count per Rav Huna)",
                      machine_claim="EX30-11", **OI)]
        if q == "weighing_protocol":
            return [V("tippings_known_to_heaven", "weighed exact "
                      "(בד בבד — 'part for part') or with "
                      "surplus? proven from the cinnamon's TWO "
                      "weighings: the surplus exists and 'the "
                      "Holy One knows the TIPPINGS' (Rav Yehuda, "
                      "Keritot 5a:26-27): the weighing-protocol "
                      "parameter recorded with its proof",
                      authority="Rav Yehuda",
                      machine_claim="EX30-11", **OI)]
        return None

    return {
        "lamp_service": {"fn": rule_lamp},
        "morning_order": {"fn": rule_order},
        "laver_machine": {"fn": rule_laver},
        "atonement_corners": {"fn": rule_corners},
        "oil_and_incense": {"fn": rule_oil},
    }
