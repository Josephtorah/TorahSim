#!/usr/bin/env python3
"""terumah_rules.py — the Terumah exam's rule modules (2026-09-01,
owner: "commit and push. then run step 9 on terumah").

Eleven modules on Exod 25-27 anchors, compiled the same day the
parashah was derived and stamped (the derive-then-examine rhythm's
third cycle). Provenance mishnah + exodus_anchor (the fresh Terumah
seats); mitzvah_orientation carries talmud_source in place of a
Mishnah row (the Noahide shape — the Talmud is the ruling body).

engine.py calls build(V) at its tail and merges the returned registry —
no circular import; V is engine's verdict constructor."""


def build(V):
    def _TR(mishnah, anchor, **extra):
        d = dict(mishnah=mishnah, exodus_anchor=anchor)
        d.update(extra)
        return d

    # ------------------------------------------------ temple_funds
    FUNDS = _TR("Mishnah Shekalim 4:6",
                "Exod.25.2+8 (exo_25, EX25-08 + EX25-02)")

    def rule_temple_funds(case):
        q = case.get("query")
        if q == "craftsmen_payment" and \
                case.get("funds_source") == "consecrated_property":
            return [V("give_as_wages", "items fit for communal offerings "
                      "go to the craftsmen in their wages",
                      authority="R. Akiva", machine_claim="EX25-08",
                      **FUNDS),
                    V("desacralize_then_pay", "einah hi ha-middah — "
                      "separate the wages, desacralize onto the "
                      "craftsmen's money, buy back from the new fund",
                      authority="Ben Azzai", **FUNDS)]
        if q == "surplus_offering":
            return [V("gold_leaf_holy_of_holies", "the surplus became "
                      "gold leaf for the Holy of Holies — the rider on "
                      "EX25-08 (Midrash Tanchuma, Terumah 1, the "
                      "yelamdenu opening)", machine_claim="EX25-08",
                      **FUNDS)]
        return None

    # ------------------------------------------------ sanctuary_extension
    EXT = _TR("Mishnah Shevuot 2:2; Mishnah Sanhedrin 1:5 (credit)",
              "Exod.25.9 (exo_25, EX25-03 — ve-khen taasu, the "
              "constitutional clause)")
    EXT_ELEMENTS = {"king", "prophet", "urim_tummim", "sanhedrin_71",
                    "two_thanksgivings", "song"}

    def rule_sanctuary_extension(case):
        q = case.get("query")
        if q == "extension_validity":
            have = set(case.get("extension_elements") or [])
            if have == EXT_ELEMENTS:
                return [V("valid", "the full constitution re-enacted — "
                          "king, prophet, Urim and Tummim, the "
                          "seventy-one, two thanksgivings, song",
                          machine_claim="EX25-03", **EXT)]
            return [V("invalid", "kol she-lo naaseh be-khol ellu — "
                      "missing: %s; no sanctity conferred"
                      % ", ".join(sorted(EXT_ELEMENTS - have)),
                      machine_claim="EX25-03", **EXT)]
        if q == "entrant_liability" and \
                case.get("addition_status") == "unconsecrated":
            return [V("exempt", "one who enters an addition not made "
                      "with all these is not liable", **EXT)]
        if q == "extension_bench":
            return [V("seventy_one", "ein mosifin al ha-ir ve-al "
                      "ha-azarot ella be-vet din shel shivim ve-echad "
                      "(Mishnah Sanhedrin 1:5, the backfill's docket)",
                      machine_claim="EX25-03", **EXT)]
        return None

    # ------------------------------------------------ showbread_form
    FORM = _TR("Mishnah Menachot 11:5 + 11:4",
               "Exod.25.23+30 (exo_25, EX25-11 + EX25-06)")
    # The verse's own dimensions: two cubits length, one cubit width.
    TABLE_CUBITS = (2, 1)
    NUM_EN = {5: "five", 6: "six", 10: "ten", 12: "twelve"}

    def rule_showbread_form(case):
        q = case.get("query")
        if q == "table_dimensions":
            k = case.get("cubit_handbreadths")
            if k in (5, 6):
                length = TABLE_CUBITS[0] * k
                width = TABLE_CUBITS[1] * k
                verdict = "%s_by_%s" % (NUM_EN[length], NUM_EN[width])
                who = "R. Yehudah" if k == 5 else "R. Meir"
                return [V(verdict, "COMPUTED: the verse's two-cubits-"
                          "by-one at %d handbreadths to the cubit = "
                          "%dx%d" % (k, length, width), authority=who,
                          machine_claim="EX25-11", **FORM)]
        if q == "bread_form":
            return [V("must_have_faces", "lechem PANIM — she-yehe lo "
                      "panim (Ben Zoma on 25:30's own name)",
                      authority="Ben Zoma", machine_claim="EX25-11",
                      **FORM)]
        if q == "bread_dimensions":
            item = case.get("item")
            if item == "showbread":
                return [V("ten_by_five_horns_seven", "the mnemonic's "
                          "second half: 10-5-7", machine_claim="EX25-11",
                          **FORM)]
            if item == "two_loaves":
                return [V("seven_by_four_horns_four", "the mnemonic's "
                          "first half: 7-4-4", machine_claim="EX25-11",
                          **FORM)]
        if q == "frankincense_placement":
            return [V("beside_the_rows", "the bowls stood in the gap — "
                      "al can mean ADJACENT (ve-alav mateh Menashe, "
                      "Numbers 2:20)", authority="Abba Shaul",
                      machine_claim="EX25-11", **FORM),
                    V("on_the_rows", "ve-natata al ha-maarekhet — the "
                      "plain 'upon'", authority="the sages' challenge",
                      **FORM)]
        return None

    # ------------------------------------------------ showbread_tamid
    TAMID = _TR("Mishnah Menachot 11:7 + 11:6",
                "Exod.25.30 (exo_25, EX25-12 + EX25-06 — lefanai "
                "TAMID quoted as the row's own proof)")

    def rule_showbread_tamid(case):
        q = case.get("query")
        if q == "tamid_satisfied":
            ex = case.get("exchange")
            if ex == "simultaneous":
                return [V("satisfied", "this one's handbreadth beside "
                          "that one's — the table never bare",
                          machine_claim="EX25-12", **TAMID)]
            if ex == "same_day_gap":
                return [V("not_satisfied", "she-ne'emar lefanai TAMID — "
                          "strict simultaneity",
                          authority="the first tanna",
                          machine_claim="EX25-12", **TAMID),
                        V("satisfied", "even these withdraw and these "
                          "place later — that too is TAMID (no vacant "
                          "night)", authority="R. Yose",
                          machine_claim="EX25-12", **TAMID)]
            if ex == "overnight_vacant":
                return [V("not_satisfied", "a vacant night fails the "
                          "token on every recorded view",
                          machine_claim="EX25-12", **TAMID)]
        if q == "table_order":
            return [V("marble_in_gold_out", "maalin ba-kodesh ve-lo "
                      "moridin — marble for the incoming bread, gold "
                      "for the outgoing", machine_claim="EX25-12",
                      **TAMID)]
        if q == "rod_work_on_sabbath":
            return [V("deferred", "lo siddur kanim ve-lo netilatan "
                      "docheh et ha-shabbat (Mishnah Menachot 11:6)",
                      **TAMID)]
        return None

    # ------------------------------------------------ menorah_integrity
    MENORAH = _TR("Mishnah Menachot 3:7",
                  "Exod.25.31-36 (exo_25, EX25-07 — one drawn piece, "
                  "six from the sides and the shaft = seven)")

    def rule_menorah_integrity(case):
        if case.get("query") == "menorah_validity":
            b, l = case.get("branches"), case.get("lamps")
            if b == 7 and l == 7:
                return [V("valid", "seven branches, seven lamps — the "
                          "verse's own count", machine_claim="EX25-07",
                          **MENORAH)]
            return [V("invalid", "shivah kenei menorah meakkevin zeh "
                      "et zeh — the count is blocking: %d branches, "
                      "%d lamps" % (b, l), machine_claim="EX25-07",
                      **MENORAH)]
        return None

    # ------------------------------------------------ sanctuary_partition
    PART = _TR("Mishnah Yoma 5:1",
               "Exod.26.33 (exo_26, EX26-04 — the row quotes the "
               "verse as R. Yose's proof)")

    def rule_sanctuary_partition(case):
        q = case.get("query")
        if q == "partition_count":
            t = case.get("temple")
            if t == "tabernacle":
                return [V("one", "ve-hivdilah ha-parokhet lakhem — the "
                          "verse's single separating veil",
                          machine_claim="EX26-04", **PART)]
            if t == "second_temple":
                return [V("two", "the two curtains with a cubit "
                          "between them", authority="the rabbis",
                          machine_claim="EX26-04", **PART),
                        V("one", "lo hayetah sham ella parokhet achat "
                          "bilvad — she-ne'emar our 26:33",
                          authority="R. Yose", machine_claim="EX26-04",
                          **PART)]
        if q == "curtain_openings":
            return [V("outer_south_inner_north", "the outer pinned "
                      "from the south, the inner from the north — the "
                      "walk between them", **PART)]
        return None

    # ------------------------------------------------ mitzvah_orientation
    ORIENT = _TR(None,
                 "Exod.26.15 (exo_26, EX26-06 + EX26-02 — atzei "
                 "shittim OMDIM, the standing-word)",
                 talmud_source="Babylonian Talmud Sukkah 45b — "
                               "she-omdim derekh gedilatan (Mishnah "
                               "Sukkah 3:14 the case neighborhood)")
    ORIENT = {k: v for k, v in ORIENT.items() if v is not None}

    def rule_mitzvah_orientation(case):
        if case.get("query") == "mitzvah_object_orientation":
            h = case.get("held")
            if h == "as_grown":
                return [V("valid", "taken the way they grow — upright "
                          "as they stood", machine_claim="EX26-06",
                          **ORIENT)]
            if h == "inverted":
                return [V("invalid", "acacia wood STANDING — the "
                          "orientation law from the boards' own token",
                          machine_claim="EX26-06", **ORIENT)]
        return None

    # ------------------------------------------------ sheretz_removal
    SHERETZ = _TR("Mishnah Eruvin 10:15; Mishnah Tamid 5:5 (the "
                  "psakhter's services)",
                  "Exod.27.3 (exo_27, EX27-06 + EX27-04 — sirotav "
                  "le-dashno, the ash-vessel list)")

    def rule_sheretz_removal(case):
        q = case.get("query")
        if q == "sheretz_removal_method":
            return [V("belt", "she-lo lash-hot et ha-tumah — impurity "
                      "must not linger",
                      authority="R. Yochanan ben Beroka",
                      machine_claim="EX27-06", **SHERETZ),
                    V("wooden_tongs", "she-lo le-rabbot et ha-tumah — "
                      "impurity must not spread", authority="R. Yehudah",
                      machine_claim="EX27-06", **SHERETZ)]
        if q == "sheretz_removal_zones":
            return [V("hall_vestibule_altar", "the hall, the vestibule, "
                      "and between vestibule and altar",
                      authority="R. Shimon ben Nannas",
                      machine_claim="EX27-06", **SHERETZ),
                    V("karet_zones", "wherever deliberate entry is "
                      "cut-off and inadvertent a sin-offering",
                      authority="R. Akiva", machine_claim="EX27-06",
                      **SHERETZ)]
        if q == "sheretz_found_elsewhere":
            return [V("covered_with_psakhter", "kofin alav psakhter — "
                      "the great bronze ash-vessel's second service "
                      "(Mishnah Tamid 5:5)", machine_claim="EX27-06",
                      **SHERETZ)]
        return None

    # ------------------------------------------------ karpef_carrying
    KARPEF = _TR("Mishnah Eruvin 2:5",
                 "Exod.27.18 (exo_27, EX27-02 — the court as the "
                 "standard area: bet satayim = this courtyard)")
    COURT_AREA = 100 * 50  # the verse's own hundred-by-fifty

    def rule_karpef_carrying(case):
        q = case.get("query")
        if q == "karpef_limit":
            side = COURT_AREA ** 0.5
            return [V("seventy_and_remainder_squared", "COMPUTED: the "
                      "square on the courtyard's area — root of %d is "
                      "%.2f, seventy cubits and a remainder"
                      % (COURT_AREA, side), machine_claim="EX27-02",
                      **KARPEF)]
        if q == "karpef_carrying":
            if case.get("amenity") == "none":
                return [V("forbidden", "a watch-hut, a dwelling, or "
                          "nearness to town is required",
                          authority="R. Yehudah ben Baba",
                          machine_claim="EX27-02", **KARPEF),
                        V("permitted", "the measure alone suffices — "
                          "seventy and a remainder squared",
                          authority="R. Akiva", machine_claim="EX27-02",
                          **KARPEF)]
            if case.get("length_to_width") == "double":
                return [V("forbidden", "length one cubit over width "
                          "already forbids", authority="R. Eliezer",
                          **KARPEF),
                        V("permitted", "even length double its width — "
                          "the courtyard's own hundred-by-fifty "
                          "proportion", authority="R. Yose",
                          machine_claim="EX27-02", **KARPEF)]
        return None

    # ------------------------------------------------ curtain_boundary
    CURTAIN = _TR("Mishnah Makkot 3:3 (credit — read in the backfill)",
                  "Exod.27.9 (exo_27, EX27-01 — the hangings as the "
                  "statute's own line)")

    def rule_curtain_boundary(case):
        if case.get("query") == "eating_liability" and \
                case.get("offering") == "most_holy":
            where = case.get("eaten")
            if where == "outside_curtains":
                return [V("lashes_forty", "kodshei kodashim chutz "
                          "la-kelaim — in the forty-lashes list",
                          machine_claim="EX27-01", **CURTAIN)]
            if where == "within_curtains":
                return [V("permitted", "eaten within the boundary the "
                          "hangings draw", machine_claim="EX27-01",
                          **CURTAIN)]
        return None

    # ------------------------------------------------ oil_grades
    OIL = _TR("Mishnah Menachot 8:5 + 8:4",
              "Exod.27.20 (exo_27, EX27-03 — zakh katit la-maor, the "
              "grade scoped to the lamp)")

    def rule_oil_grades(case):
        q = case.get("query")
        if q == "oil_acceptable":
            dest = case.get("destination")
            pressing = case.get("pressing")
            if dest == "menorah":
                if pressing == 1:
                    return [V("acceptable", "the crushed first pressing "
                              "of each olive feeds the lamp (Mishnah "
                              "Menachot 8:4)", machine_claim="EX27-03",
                              **OIL)]
                return [V("not_acceptable", "zakh katit la-maor — only "
                          "the crushed first pressing for the light",
                          machine_claim="EX27-03", **OIL)]
            if dest == "meal_offering":
                return [V("acceptable", "ve-lo zakh katit la-menachot — "
                          "the stricter grade is NOT demanded there",
                          machine_claim="EX27-03", **OIL)]
        if q == "meal_offering_requires_crushed":
            return [V("no", "the a-fortiori (menorah not-for-eating "
                      "demands it, meal-offerings eaten all the more "
                      "so) is REFUTED by the verse: crushed FOR THE "
                      "LIGHT and not crushed for the meal-offerings — "
                      "middah I1 blocked by limiting ink",
                      machine_claim="EX27-03", **OIL)]
        if q == "oil_grade_order":
            # COMPUTED: rank = olive + pressing over the 3x3 table;
            # the Mishnah's stated equal pairs are the anti-diagonals.
            ranks = {}
            for olive in (1, 2, 3):
                for pressing in (1, 2, 3):
                    ranks.setdefault(olive + pressing, []).append(
                        (olive, pressing))
            equal_tiers = [tier for tier in ranks.values()
                           if len(tier) > 1]
            return [V("sum_diagonal", "COMPUTED: rank by olive+pressing "
                      "— %d tiers, the equal pairs %s exactly as the "
                      "Mishnah states them"
                      % (len(ranks), equal_tiers),
                      machine_claim="EX27-03", **OIL)]
        return None

    return {
        "temple_funds": {"fn": rule_temple_funds, "tractate": "Shekalim"},
        "sanctuary_extension": {"fn": rule_sanctuary_extension,
                                "tractate": "Shevuot"},
        "showbread_form": {"fn": rule_showbread_form,
                           "tractate": "Menachot"},
        "showbread_tamid": {"fn": rule_showbread_tamid,
                            "tractate": "Menachot"},
        "menorah_integrity": {"fn": rule_menorah_integrity,
                              "tractate": "Menachot"},
        "sanctuary_partition": {"fn": rule_sanctuary_partition,
                                "tractate": "Yoma"},
        "mitzvah_orientation": {"fn": rule_mitzvah_orientation,
                                "tractate": "Sukkah"},
        "sheretz_removal": {"fn": rule_sheretz_removal,
                            "tractate": "Eruvin"},
        "karpef_carrying": {"fn": rule_karpef_carrying,
                            "tractate": "Eruvin"},
        "curtain_boundary": {"fn": rule_curtain_boundary,
                             "tractate": "Makkot"},
        "oil_grades": {"fn": rule_oil_grades, "tractate": "Menachot"},
    }
