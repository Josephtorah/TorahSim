#!/usr/bin/env python3
"""vestments_rules.py — round 27: VESTMENTS AND INVESTITURE, the
sixteenth Exodus Talmud-first exam block (2026-09-04). Four
modules — the frontplate's state machine, the vestments' form,
the investiture machine, the consecration foods. engine.py merges
build(V) at its tail. Read-source:
logic/oral_triage/exodus_block_vestments_2026-09-04.md."""


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    # -------------------------------- the frontplate's machine
    FP = _EX("Yoma 7b:3-5; Pesachim 77a:11-13; Shabbat 12a:4; "
             "Yevamot 60b:13",
             "Exod.28.38 (exo_28_priest_garments, EX28-13 — "
             "F-103; the acceptance function held at EX28-06 and "
             "its scope at EX28-11 since derivation)")

    def rule_frontplate(case):
        q = case.get("query")
        if q == "plate_state_machine":
            return [V("forehead_contact_required", "על מצח ונשא "
                      "('on the forehead... and he shall BEAR') — "
                      "contact required; broken, all agree OFF "
                      "(Abaye's frame, Yoma 7b:4)",
                      authority="R. Yehuda",
                      machine_claim="EX28-13", **FP),
                    V("always_accepts", "תמיד לרצון — 'always on "
                      "his forehead'? impossible (the privy, "
                      "sleep) — rather ALWAYS ACCEPTING: the "
                      "always-word moved from the wearing to the "
                      "function (7b:5); the proof — the Yom "
                      "Kippur High Priest in linen accepts with "
                      "the plate off (Pesachim 77a:13)",
                      authority="R. Shimon", **FP)]
        if q == "public_impurity_scope":
            return [V("permitted_outright_lone_arm", "no tanna "
                      "holds impurity PERMITTED for the public "
                      "except R. Yehuda (Pesachim 77a:12) — the "
                      "lone arm named",
                      authority="R. Yehuda",
                      machine_claim="EX28-13", **FP),
                    V("pushed_aside_needs_plate", "all others: "
                      "public impurity is PUSHED ASIDE and needs "
                      "the plate to accept (77a:11) — EX28-11's "
                      "scoped acceptance held this shape",
                      authority="the Sages (the standing premise)",
                      **FP)]
        if q == "plate_ordeal_use":
            return [V("acceptance_not_calamity", "pass the women "
                      "before the plate? — לרצון להם ('for "
                      "acceptance FOR THEM'): for acceptance, NOT "
                      "for calamity; Rav Ashi's gate — for THEM: "
                      "Israel acceptance-only, the nations even "
                      "calamity (Yevamot 60b:13): the "
                      "instrument's polarity scoped by its own "
                      "dative",
                      authority="Rav Kahana b. Rav Natan; Rav Ashi",
                      machine_claim="EX28-13", **FP)]
        if q == "attention_afortiori":
            return [V("constant_touching_from_tamid", "one must "
                      "touch his tefillin every hour — from the "
                      "PLATE: one Name only, yet 'on his forehead "
                      "ALWAYS — that he not divert his attention'; "
                      "tefillin with many Names, all the more "
                      "(the school of R. Yishmael, Shabbat 12a:4) "
                      "— the plate's tamid exported to the "
                      "tefillin's handling law",
                      machine_claim="EX28-13", **FP)]
        return None

    # ------------------------------------ the vestments' form
    VF = _EX("Sotah 36a:11-13; Yoma 72b:2-3 + 44b:15-16; Arakhin "
             "3b:12-14; Zevachim 19a:24-26 + 119b:18",
             "Exod.28.10 + 28.32-43 (exo_28_priest_garments, "
             "EX28-14 — F-104; the announced entry held at "
             "EX28-05, the stones at EX28-12)")

    def rule_form(case):
        q = case.get("query")
        if q == "shoulder_stones":
            return [V("six_six_birth_order_fifty", "two stones, "
                      "twelve names — six on each ('six of their "
                      "names on the one stone,' 28:10); the "
                      "SECOND by their birth, the first not "
                      "(Judah advanced); FIFTY letters, "
                      "twenty-five per stone (Sotah 36a:12-13)",
                      machine_claim="EX28-14", **VF)]
        if q == "garment_craft":
            return [V("woven_sleeves_excepted", "priestly "
                      "garments WOVEN, not needle-work — מעשה ארג "
                      "(28:32); Abaye: the needle serves only the "
                      "SLEEVES, woven apart and attached (Yoma "
                      "72b:3)",
                      machine_claim="EX28-14", **VF)]
        if q == "tefillin_slot":
            return [V("hair_between_plate_turban", "the hand "
                      "tefillin on his FLESH; the head — 'set the "
                      "TURBAN on his head' (29:6)? his HAIR "
                      "showed between plate and turban — where "
                      "the tefillin sit (Arakhin 3b:13-14 = "
                      "Zevachim 19a:25-26): the vestment set "
                      "leaves the tefillin their slot",
                      machine_claim="EX28-14", **VF)]
        if q == "pan_sounding_ring":
            return [V("sound_heard_fulfilled", "every other day "
                      "the pan had no rattle-ring; TODAY it had "
                      "one (ben HaSegan, Yoma 44b:16) — read "
                      "against ונשמע קולו ('its sound shall be "
                      "heard,' 28:35): the entry announced even "
                      "where the robe is absent",
                      authority="ben HaSegan",
                      machine_claim="EX28-14", **VF)]
        if q == "private_altar_priest":
            return [V("great_altar_only", "the GREAT altar "
                      "requires a priest in the service garments "
                      "— לשרת בקדש ('to serve in the holy place,' "
                      "28:43); the private altar needs neither "
                      "(Zevachim 119b:18): the garments' "
                      "jurisdiction bounded to the public house",
                      machine_claim="EX28-14", **VF)]
        return None

    # --------------------------------- the investiture machine
    IV = _EX("Sanhedrin 83b:12-14; Yoma 5a:9-11 + 5b:3-5; "
             "Zevachim 13a:11-13 + 24b:2-4 + 12b:14",
             "Exod.29.1-30 (exo_29_investiture, EX29-14 — F-105; "
             "the this-the-thing clause held at EX29-01, the "
             "garment transfer at EX29-05)")

    def rule_investiture(case):
        q = case.get("query")
        if q == "unvested_priest":
            return [V("stranger_death_by_heaven", "וחגרת אתם אבנט "
                      "('you shall gird them with the sash,' "
                      "29:9): while their vestments are ON them, "
                      "their priesthood is on them; off — off, "
                      "and they are STRANGERS: a stranger who "
                      "served dies by Heaven (Sanhedrin "
                      "83b:13-14): the office literally worn — "
                      "EX28-07's wear-or-die held the shape",
                      authority="R. Abahu per R. Yochanan",
                      machine_claim="EX29-14", **IV)]
        if q == "investiture_week":
            return [V("either_clock_qualifies", "'SEVEN DAYS "
                      "shall the son wear them' (29:30) — robed "
                      "seven and anointed seven; robed seven "
                      "anointed one, or the reverse? 'who shall "
                      "be ANOINTED and who shall be INVESTED' "
                      "(Leviticus 16:32) — either way (Yoma "
                      "5a:10): the succession's two clocks "
                      "decoupled",
                      machine_claim="EX29-14", **IV)]
        if q == "trousers_gap":
            return [V("imported_this_the_thing", "the TROUSERS "
                      "are not written in the portion — וזה הדבר "
                      "('and THIS is the THING,' 29:1) imports "
                      "the trousers and the tenth-ephah (R. Yosei "
                      "b. Chanina, Yoma 5b:4-5): the ink's own "
                      "gap and the clause that supplies it — "
                      "riding EX29-01's this-the-thing crown",
                      authority="R. Yosei b. Chanina",
                      machine_claim="EX29-14", **IV)]
        if q == "blood_collection":
            return [V("fit_vested_priest", "collection = 'and "
                      "they shall present' — by the sons of Aaron "
                      "THE PRIESTS: a fit priest in service "
                      "vessels (Zevachim 13a:11); R. Akiva's "
                      "route — bene-Aharon here, 'the ANOINTED "
                      "priests' there (Numbers 3:3): as there fit "
                      "and vested, so here (13a:12)",
                      authority="R. Akiva",
                      machine_claim="EX29-14", **IV)]
        if q == "finger_placement":
            return [V("placing_bound_parse_direction", "'...and "
                      "PLACE on the horns with your FINGER' "
                      "(29:12) — the finger binds the PLACING, "
                      "the collection stays free, because מקרא "
                      "נדרש לפניו ('a verse is expounded on what "
                      "PRECEDES it, not before-the-before, and "
                      "not after') — a parsing-direction "
                      "meta-rule stated as law on the verse's own "
                      "syntax (Zevachim 24b:2-3); R. Yochanan's "
                      "laterality default beside it: finger or "
                      "priesthood — only the RIGHT (24b:4)",
                      authority="R. Elazar b. R. Shimon",
                      machine_claim="EX29-14", **IV)]
        if q == "doubled_it":
            return [V("one_freed_for_derivation", "תרי הוא כתיבי "
                      "('TWO its are written') at the burnt "
                      "offering (29:18's family) — one needed, "
                      "one FREED for the derivation (Zevachim "
                      "12b:14): the freed-token operator's "
                      "smallest exemplar, the export family "
                      "again",
                      machine_claim="EX29-14", **IV)]
        return None

    # --------------------------------- the consecration foods
    CF = _EX("Pesachim 59b:3-5; Yoma 68b:18-20; Sukkah 49b:1; "
             "Zevachim 28b:4-6 + 44b:5-7",
             "Exod.29.33-34 (exo_29_investiture, EX29-14 — "
             "F-105; the sacred meal's fences held at EX29-06)")

    def rule_foods(case):
        q = case.get("query")
        if q == "priests_eat_atonement":
            return [V("owners_atoned_by_the_meal", "ואכלו אתם אשר "
                      "כפר בהם ('they shall EAT those by which "
                      "atonement was made,' 29:33) — THE PRIESTS "
                      "EAT AND THE OWNERS ARE ATONED: the meal a "
                      "stage of the owners' atonement (Pesachim "
                      "59b:4, in the fats-then-flesh sequence "
                      "59b:3) — EX29-06's eaten-by-those-it-"
                      "atoned clause held it",
                      machine_claim="EX29-14", **CF)]
        if q == "vestment_personal_use":
            return [V("sleep_never_eat_as_service", "'they did "
                      "not SLEEP in sacred garments' — but eat "
                      "they did? eating differs: SERVICE-NEED, "
                      "per the atonement-eaters clause; walking "
                      "pressed as well (Yoma 68b:19-20): the "
                      "personal-use boundary drawn through "
                      "29:33's own function",
                      machine_claim="EX29-14", **CF)]
        if q == "disposal_sanctity":
            return [V("pouring_so_burning", "as its pouring is IN "
                      "SANCTITY, so its burning is IN SANCTITY — "
                      "Ravina's kodesh-kodesh from 'pour a "
                      "libation in the HOLY' with 29:34's "
                      "burn-the-leftover-for-it-is-HOLY (Sukkah "
                      "49b:1): disposal inherits the rite's grade",
                      authority="Ravina",
                      machine_claim="EX29-14", **CF)]
        if q == "leftover_excision":
            return [V("kodesh_kodesh_notar", "the leftover's "
                      "excision anchored by kodesh-kodesh — 'the "
                      "HOLY of the LORD he profaned, cut off' "
                      "with 29:34's because-it-is-sacred: as "
                      "there NOTAR, so here (R. Yochanan by Zavdi "
                      "bar Levi's teaching, Zevachim 28b:5); "
                      "out-of-place excluded from karet (28b:6)",
                      authority="R. Yochanan",
                      machine_claim="EX29-14", **CF)]
        if q == "meal_offering_inclusion":
            return [V("omer_jealousy_included", "'EVERY meal "
                      "offering of theirs' includes the OMER and "
                      "the JEALOUSY offering — lest 29:33's "
                      "atonement-eaters clause exclude them (the "
                      "omer permits, the jealousy clarifies, "
                      "neither atones) — included anyway "
                      "(Zevachim 44b:6): the atonement-word "
                      "bounded from excluding",
                      machine_claim="EX29-14", **CF)]
        return None

    return {
        "frontplate_machine": {"fn": rule_frontplate},
        "vestment_form": {"fn": rule_form},
        "investiture_machine": {"fn": rule_investiture},
        "consecration_foods": {"fn": rule_foods},
    }
