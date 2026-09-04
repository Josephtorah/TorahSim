#!/usr/bin/env python3
"""oaths_rules.py — round 15: OATHS AND DEPOSITS, the fourth Exodus
Talmud-first exam block (2026-09-04). Three modules on Exodus
22:6-10 — the oath machinery's derivation layer over the compiled
guardians function. engine.py merges build(V) at its tail.
Read-source record: logic/oral_triage/exodus_block_oaths_2026-09-04.md."""


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    # ------------------------------------------- the oath of the Lord
    OL = _EX("Shevuot 39b:5-7 (Rabbi Shimon ben Tarfon; the "
             "court's-understanding rider with the reed of Rava's "
             "court) + 47a:10-12 (R. Ami's not-the-heirs baraita)",
             "Exod.22.10 (exo_22_property_social, EX22-16 — seated "
             "F-056)")

    def rule_oath_lord(case):
        q = case.get("query")
        if q == "false_oath_reach":
            return [V("both_parties", "'the oath of the LORD shall "
                      "be BETWEEN THEM BOTH' — the false oath's "
                      "punishment reaches the swearer AND the one "
                      "who imposed it (Rabbi Shimon ben Tarfon; the "
                      "bystanders' 'depart from the tents of these "
                      "wicked men' said of both) — ANTICIPATED: EX22-05 has "
                      "held R. Natan's falls-on-both since the law era",
                      machine_claim="EX22-05", **OL)]
        if q == "heirs_oath":
            return [V("not_between_heirs", "'between them both' — "
                      "and NOT between their heirs (R. Ami's "
                      "baraita): the heir's oath over what he "
                      "cannot know drops where his father's would "
                      "have stood (47a:11-12) — ANTICIPATED: EX22-05 holds "
                      "the heirs exclusion at the Mekhilta layer",
                      machine_claim="EX22-05", **OL)]
        if q == "oath_understanding":
            return [V("courts_understanding", "the oath is "
                      "administered on THE COURT'S understanding, "
                      "never the swearer's private one — the reed "
                      "of Rava's court (the coins hidden in the "
                      "cane) is the recorded exploit it blocks "
                      "(39b:7)", machine_claim="EX22-16", **OL)]
        return None

    # --------------------------------------------- the oath's subject
    OS = _EX("Shevuot 43a:1-3 (the generalization-detail-"
             "generalization on 22:6 and 22:9 with the four "
             "exclusions) + 42b:16-17 (the same middah at the "
             "double payment) + 42a:12 (if a MAN delivers) + 42b:15 "
             "(the defined-amount mishnah)",
             "Exod.22.6-9 (exo_22_property_social, EX22-04 — the "
             "standing seat already names the middah on 'every "
             "matter of trespass'; EX22-16)",
             mishnah="Mishnah Shevuot 6:1-3")

    def rule_oath_subject(case):
        q = case.get("query")
        if q == "oath_subject_scope":
            return [V("movable_intrinsic", "'silver or vessels to "
                      "safeguard' (22:6) run as generalization-"
                      "detail-generalization: the keeper's oath "
                      "covers movables with intrinsic value — LAND "
                      "out (not movable), CANAANITE SLAVES out "
                      "(compared to land), DOCUMENTS out (no "
                      "intrinsic value), CONSECRATED out ('his "
                      "NEIGHBOR'); the paid keeper's own verse "
                      "(22:9) runs the same middah (43a:1-3)",
                      machine_claim="EX22-16", **OS)]
        if q == "double_payment_scope":
            return [V("movable_intrinsic", "'every matter of "
                      "trespass... ox, donkey, sheep, clothing... "
                      "any lost thing' (22:8) — the same "
                      "generalization-detail-generalization: double "
                      "payment for movables with intrinsic value "
                      "(42b:16-17; the standing EX22-04 seat "
                      "already names this middah on the verse — "
                      "anticipated)", machine_claim="EX22-04",
                      **OS)]
        if q == "minor_claim_oath":
            return [V("no_oath", "'if a MAN delivers' — a minor's "
                      "delivery is nothing: no court oath on his "
                      "claim (42a:12; but one swears TO a minor "
                      "for consecrated property — the rider "
                      "recorded)", machine_claim="EX22-16", **OS)]
        if q == "undefined_claim_oath":
            return [V("exempt_until_defined", "oaths ride claims "
                      "defined by size, weight, or number — "
                      "full-house-of-produce exempts; "
                      "up-to-the-ledge against up-to-the-window "
                      "obligates (the mishnah at 42b:15)",
                      machine_claim="EX22-16", **OS)]
        return None

    # ------------------------------------------------ oath suspects
    SU = _EX("Shevuot 47b:4 (Shimon ben Tarfon's revocalization)",
             "Exod.22.10 (exo_22_property_social, EX22-16; the "
             "Exod 20:13 anchor lives in exo_20's span — noted, "
             "unseated)")

    def rule_oath_suspects(case):
        if case.get("query") != "oath_suspect_accessory":
            return None
        return [V("accessory_read_in", "lo tinaf ('you shall not "
                  "commit adultery') READ lo tanif ('you shall not "
                  "CAUSE adultery') — the accessory read into the "
                  "commandment by revocalization (the M-16 move; "
                  "the oath-suspect sugya's own seat)",
                  machine_claim="talmud_source only (the Exod 20:13 "
                  "anchor lives in exo_20's span)", **SU)]

    return {
        "oath_of_the_lord": {"fn": rule_oath_lord},
        "oath_subject_matter": {"fn": rule_oath_subject},
        "oath_suspects": {"fn": rule_oath_suspects},
    }
