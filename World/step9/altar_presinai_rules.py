# altar_presinai_rules.py — round 38, THE ALTAR BEFORE SINAI
# (Genesis exam block 9 of 12, 2026-09-04). Read-source:
# logic/oral_triage/genesis_block_altar_2026-09-04.md.


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    TG = _EX("Zevachim 53b:7-9",
             "Gen 49:27 (gen_72, G72-36 / F-162)")
    AM = _EX("Zevachim 88b:5-7",
             "Gen 37:31 (gen_60, G60-23 / F-163)")
    OP = _EX("Zevachim 97b:8-10",
             "Gen 22:10 + 22:13 (gen_38, G38-42 / F-164)")
    NA = _EX("Zevachim 108b:14-16, 115b:17-18, 116a:10-15",
             "Gen 8:20 + 7:16 + 4:4 (gen_20 G20-20 / F-165; gen_17 "
             "G17-19 / F-166; gen_12 G12-23 / F-167)")
    PT = _EX("Nedarim 32b:5-8",
             "Gen 14:18 (gen_30, G30-33 / F-168)")

    def rule_temple_geography_gen(case):
        if case.get("query") == "strip_of_benjamin":
            return [V("altar_in_the_torn_ones_portion",
                      "why did the southeast corner have no "
                      "foundation? R. Elazar: because it was not in "
                      "the portion of THE TORN ONE — בנימין זאב יטרף "
                      "('Benjamin, a WOLF that tears,' Gen 49:27): "
                      "the altar eats a cubit in Judah's portion, "
                      "and רצועה היתה יוצאה ('a STRIP went out') of "
                      "Judah's into Benjamin's — righteous Benjamin "
                      "grieving daily to take it: Temple geometry "
                      "assigned by the testament's own animal "
                      "emblem — Zevachim 53b:7-9",
                      authority="R. Elazar with R. Levi bar Chama",
                      machine_claim="G72-36", **TG)]
        return None

    def rule_atonement_map(case):
        if case.get("query") == "tunic_atonement":
            return [V("bloodshed_by_the_dipped_tunic",
                      "the priestly garments atone as the offerings "
                      "do — and the TUNIC atones for BLOODSHED: "
                      "וישחטו שעיר עזים ויטבלו את הכתנת בדם ('they "
                      "slaughtered a goat kid and dipped THE TUNIC "
                      "IN THE BLOOD,' Gen 37:31): Joseph's tunic "
                      "as the atonement map's bloodshed entry, the "
                      "whole garment-by-garment table beside — "
                      "Zevachim 88b:5-7",
                      authority="R. Einini bar Sasson",
                      machine_claim="G60-23", **AM)]
        return None

    def rule_olah_protocol(case):
        if case.get("query") == "offering_vessel_source":
            return [V("knife_proves_vessel_duty",
                      "every offering requires a VESSEL — and the "
                      "burnt-offering's own proof: וישלח אברהם את "
                      "ידו ויקח את המאכלת ('Abraham stretched out "
                      "his hand and took THE KNIFE,' Gen 22:10) — "
                      "and that was a burnt-offering, as written "
                      "ויעלהו לעלה תחת בנו ('he offered it up as a "
                      "BURNT-OFFERING instead of his son,' 22:13): "
                      "the binding supplying the olah's vessel "
                      "requirement — Zevachim 97b:8-9",
                      authority="the sugya",
                      machine_claim="G38-42", **OP)]
        return None

    def rule_noah_altar(case):
        q = case.get("query")
        if q == "outside_slaughter_source":
            return [V("liability_at_the_offering_up",
                      "R. Yosei's reason that outside-slaughter "
                      "liability rides the OFFERING-UP: דכתיב ויבן "
                      "נח מזבח לה׳ ('as it is written: Noah BUILT "
                      "AN ALTAR to the LORD,' Gen 8:20) — the altar "
                      "is the criterion; R. Shimon's Manoach-rock "
                      "counter recorded — Zevachim 108b:15-16",
                      authority="Rav Huna stating R. Yosei's "
                                "reason",
                      machine_claim="G20-20", **NA)]
        if q == "private_altar_species":
            return [V("all_clean_species_fit",
                      "all clean species are fit on a private "
                      "altar: ויקח מכל הבהמה הטהרה ומכל העוף הטהר "
                      "('and he took of EVERY clean beast and "
                      "EVERY clean fowl,' Gen 8:20) — beast as "
                      "stated, the wild animal included in beast — "
                      "Zevachim 115b:18",
                      authority="Rav Huna",
                      machine_claim="G20-20", **NA)]
        if q == "self_presenting_animals":
            return [V("came_of_themselves",
                      "how did Noah know the clean? Rav Chisda: "
                      "passed before the ark — those it accepted; "
                      "R. Abahu: והבאים זכר ונקבה ('and those that "
                      "CAME, male and female,' Gen 7:16) — הבאין "
                      "מאיליהן ('they came OF THEMSELVES'): the "
                      "roster verb as the selection protocol — "
                      "Zevachim 116a:10-11",
                      authority="R. Abahu with Rav Chisda's arm",
                      machine_claim="G17-19", **NA)]
        if q == "noahide_peace_offerings":
            return [V("peace_offered_by_fats",
                       "did the sons of Noah offer PEACE-offerings? "
                       "The yes arm: והבל הביא גם הוא מבכרות צאנו "
                       "ומחלבהן ('Abel brought, he too, of the "
                       "firstborn of his flock and of their FATS,' "
                       "Gen 4:4) — what has its FAT offered but not "
                       "all of it? peace-offerings — Zevachim "
                       "116a:14",
                       authority="the arm holding they offered",
                       machine_claim="G12-23", **NA),
                    V("burnt_only",
                      "the no arm: burnt-offerings only — 'awake, "
                      "north wind, and come, south' read as the "
                      "peace-offering's LATER arrival (Song of "
                      "Songs 4:16) — Zevachim 116a:13, 116a:15",
                      authority="the arm holding they did not",
                      **NA)]
        return None

    def rule_priesthood_transfer(case):
        q = case.get("query")
        if q == "priesthood_transfer":
            return [V("from_shem_to_abraham",
                      "R. Zecharya in R. Yishmael's name: the Holy "
                      "One sought to bring the priesthood from "
                      "SHEM — והוא כהן לאל עליון ('and he was "
                      "PRIEST to God Most High,' Gen 14:18) — but "
                      "when he blessed Abraham BEFORE his Maker "
                      "('does one bless the servant before his "
                      "Owner?'), it was taken from him and given "
                      "to Abraham, Psalm 110's oath riding על "
                      "דברתי מלכי צדק ('on the WORD of "
                      "Malchizedek') — Nedarim 32b:6-7",
                      authority="R. Zecharya in R. Yishmael's "
                                "name",
                      machine_claim="G30-33", **PT)]
        if q == "priest_seed_excluded":
            return [V("he_and_not_his_seed",
                      "והיינו דכתיב והוא כהן לאל עליון — הוא כהן "
                      "ואין זרעו כהן ('and this is why it is "
                      "written: HE was priest to God Most High — "
                      "HE a priest, and his SEED not priests'): "
                      "the pronoun's restriction sealing the "
                      "transfer — Nedarim 32b:8",
                      authority="the sugya's closing derivation",
                      machine_claim="G30-33", **PT)]
        return None

    return {
        "temple_geography_gen": {"fn": rule_temple_geography_gen,
                                 "tractate": "Zevachim"},
        "atonement_map": {"fn": rule_atonement_map,
                          "tractate": "Zevachim"},
        "olah_protocol": {"fn": rule_olah_protocol,
                          "tractate": "Zevachim"},
        "noah_altar": {"fn": rule_noah_altar,
                       "tractate": "Zevachim"},
        "priesthood_transfer": {"fn": rule_priesthood_transfer,
                                "tractate": "Nedarim"},
    }
