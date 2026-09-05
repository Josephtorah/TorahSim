# circumcision_rules.py — round 31, THE CIRCUMCISION MACHINE
# (Genesis exam block 2 of 12, 2026-09-04). Six of thirteen docket
# rows were already seated at gen_33 before the block opened; the
# fresh seven complete the machine. Read-source:
# logic/oral_triage/genesis_block_circumcision_2026-09-04.md.


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    OV = _EX("Shabbat 132a:6-10 (standing G33-21), 132a:9, 132b:9-11",
             "Gen 17:7-14 (gen_33, G33-32 / F-117)")
    PC = _EX("Shabbat 108a:10, 133b:12-14, 137a:2-4",
             "Gen 17:10-14 (gen_33, G33-32 / F-117)")
    PT = _EX("Kiddushin 29a:11-13; Shabbat 132a:15, 132a:20 "
             "(standing G33-24, G33-25)",
             "Gen 17:10-14 + 21:4 (gen_33; the mother-exempt token "
             "at gen_37's 21:4)")
    RP = _EX("Yevamot 72a:6-8",
             "Gen 17:13-14 (gen_33, G33-32 / F-117)")

    def rule_milah_overrides(case):
        q = case.get("query")
        if q == "shabbat_override_analogies":
            return [V("generations_analogy_survives",
                      "the three candidate analogies from the "
                      "chapter's own tokens — the SIGN of 17:11, the "
                      "COVENANT of 17:11, the GENERATIONS of 17:7 — "
                      "raised in turn against the Sabbath's matching "
                      "tokens; the first two weighed and set aside, "
                      "the third carries the override — Shabbat "
                      "132a:6-10; STANDING SEAT: G33-21 has held the "
                      "weighing WITH the discarded candidates named "
                      "since the reading",
                      authority="the sugya's recorded selection",
                      machine_claim="G33-21 (standing)", **OV)]
        if q == "adult_covenant_challenge":
            return [V("refuted_by_karet_distinction",
                      "גדול דכתיב ביה ברית לידחי שבת ('an ADULT, of "
                      "whom covenant is written — let him override "
                      "Shabbat!'): the challenge extending the "
                      "covenant-token to the adult's late "
                      "circumcision; refused — the adult stands "
                      "under excision (karet) and is not "
                      "timely-circumcision's like — Shabbat 132a:9 "
                      "with 132b:11's distinction",
                      authority="the sugya",
                      machine_claim="G33-32", **OV)]
        if q == "leprosy_override":
            return [V("flesh_despite_bright_spot",
                      "circumcision overrides LEPROSY: the positive "
                      "command comes and overrides the negative "
                      "(cutting the bright spot); ימול בשר ערלתו "
                      "('the FLESH of his foreskin shall be "
                      "circumcised,' 17:14's token) — בשר ואף על פי "
                      "שיש שם בהרת ('flesh — even though a bright "
                      "spot is there') — Shabbat 132b:9",
                      authority="the baraita",
                      machine_claim="G33-32", **OV)]
        if q == "in_between_derivation":
            return [V("common_side_of_both",
                      "the adult has 'flesh' written (17:14), the "
                      "minor has 'flesh' written — the IN-BETWEEN "
                      "whence? Abaye: אתיא מביניא ('derived from "
                      "between them') — not from the adult alone "
                      "(karet-bound), not from the minor alone "
                      "(timely), but the common side: circumcised, "
                      "and overriding leprosy — Shabbat 132b:10-11",
                      authority="Abaye",
                      machine_claim="G33-32", **OV)]
        return None

    def rule_milah_procedure(case):
        q = case.get("query")
        if q == "circumcision_site":
            return [V("fruit_making_place",
                      "WHERE is it done? נאמר כאן ערלתו ונאמר להלן "
                      "ערלתו ('his foreskin here, its foreskin "
                      "there' — the tree's foreskin, Lev 19:23): as "
                      "there a thing that MAKES FRUIT, so here — R. "
                      "Yoshiya; R. Natan needs no analogy: וערל זכר "
                      "('the uncircumcised MALE,' 17:14) — the place "
                      "where male is told from female: two recorded "
                      "routes, one site — Shabbat 108a:10",
                      authority="R. Yoshiya and R. Natan, both "
                                "routes recorded",
                      machine_claim="G33-32", **PC)]
        if q == "circumciser_fitness":
            return [V("male_token_scope",
                      "all are fit to circumcise except the deaf, "
                      "the insane, and the minor; R. Yehuda "
                      "validates a minor and invalidates a woman — "
                      "and why does circumcision differ? דכתיב המול "
                      "לכם כל זכר ('every MALE among you shall be "
                      "circumcised,' 17:10's own token) — Shabbat "
                      "137a:2-3",
                      authority="R. Yehuda's arm with the token "
                                "named",
                      machine_claim="G33-32", **PC)]
        if q == "dusk_wound_circumciser":
            return [V("wound_karet_liable",
                      "Rav Ashi's case: the craftsman at Shabbat "
                      "DUSK — they told him 'you have no time,' he "
                      "said 'I have,' cut, did not finish, ואישתכח "
                      "דחבורה הוא דעבד ('and it turns out a WOUND is "
                      "what he made') — no mitzvah to shelter the "
                      "act: liable to excision — Shabbat 133b:12-13",
                      authority="Rav Ashi",
                      machine_claim="G33-32", **PC)]
        if q == "suction_requirement":
            return [V("danger_removed",
                      "Rav Pappa: האי אומנא דלא מייץ סכנה הוא "
                      "ומעברינן ליה ('a craftsman who does not "
                      "SUCTION — he is a danger, and we remove "
                      "him'): the procedure's safety clause — "
                      "Shabbat 133b:14",
                      authority="Rav Pappa",
                      machine_claim="G33-32", **PC)]
        return None

    def rule_milah_parties(case):
        q = case.get("query")
        if q == "circumcision_cascade":
            return [V("three_tier_father_court_self",
                      "father first; failing him THE COURT, from "
                      "17:10's 'circumcise for yourselves every "
                      "male'; failing the court the man HIMSELF, "
                      "from 17:14 with its excision penalty — "
                      "Kiddushin 29a:11; STANDING SEAT: G33-24 has "
                      "held the cascade with the eligibility rule "
                      "since the reading",
                      authority="the baraita",
                      machine_claim="G33-24 (standing)", **PT)]
        if q == "mother_exempt":
            return [V("him_not_her",
                      "whence that SHE is not obligated? — כאשר צוה "
                      "אתו אלהים ('as God commanded HIM,' Gen 21:4): "
                      "אותו ולא אותה ('him — and not her'); and "
                      "for the generations, the school of R. "
                      "Yishmael's rider: wherever tzav ('command') "
                      "is said it is urging, immediate and for the "
                      "generations — Kiddushin 29a:12-13",
                      authority="the gemara with the school of R. "
                                "Yishmael",
                      machine_claim="G33-32", **PT)]
        if q == "eighth_day_clause":
            return [V("day_not_night_eighth_not_seventh",
                      "בן שמנת ימים ('at eight DAYS old,' 17:12) "
                      "does double duty: by day and not by night "
                      "(R. Yochanan), and the eighth and not the "
                      "seventh — Shabbat 132a:15, 132a:20; STANDING "
                      "SEAT: G33-25 has held both jobs plus the "
                      "shard-dismissal since the reading",
                      authority="R. Yochanan with the baraita",
                      machine_claim="G33-25 (standing)", **PT)]
        return None

    def rule_milah_repeat(case):
        if case.get("query") == "drawn_foreskin":
            return [V("recircumcised_even_hundred_times",
                      "the DRAWN foreskin (mashukh) must be "
                      "re-circumcised: R. Yehuda's danger arm "
                      "answered by the recorded precedent — many "
                      "circumcised in Ben Koziva's days and bore "
                      "sons and daughters — המול ימול ('circumcised "
                      "he SHALL BE circumcised,' 17:13) אפילו מאה "
                      "פעמים ('even a hundred times'), and את בריתי "
                      "הפר ('he broke MY COVENANT,' 17:14) לרבות את "
                      "המשוך ('to include the drawn one'); the "
                      "doubled verb serves the impeding shreds — "
                      "Yevamot 72a:6-8",
                      authority="the baraita answering R. Yehuda",
                      machine_claim="G33-32", **RP)]
        return None

    return {
        "milah_overrides": {"fn": rule_milah_overrides,
                            "tractate": "Shabbat"},
        "milah_procedure": {"fn": rule_milah_procedure,
                            "tractate": "Shabbat"},
        "milah_parties": {"fn": rule_milah_parties,
                          "tractate": "Kiddushin"},
        "milah_repeat": {"fn": rule_milah_repeat,
                         "tractate": "Yevamot"},
    }
