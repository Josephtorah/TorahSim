#!/usr/bin/env python3
"""engine.py — the first compiled rules (Step 9 pilot, model layer).

Two modules compiled from the exam spec; one deliberately left uncompiled so
the report can show the difference. A RULE is a function: case-input ->
LIST of verdicts (a dispute is two labeled verdicts, never an error), each
carrying its provenance: the Mishnah row, the Talmud bridge, the Genesis
anchor, and the machine claims that hold it.

Design decisions the exam forced (see REPORT.md):
- uncertainty is first-class input (Yoma's triple doubt);
- verdicts are lists, authorities labeled (Yevamot's two disputes);
- provenance is part of the return type, not a comment;
- a rule may carry MORE than the exam asked (the ten-years riders the
  machine held at Gen 16:3), and says so.
"""


def V(verdict, basis, authority=None, **prov):
    out = {"verdict": verdict, "basis": basis, "provenance": prov}
    if authority:
        out["authority"] = authority
    return out


# ---------------------------------------------------------- life_override
LIFE_PROV = dict(
    mishnah="Mishnah Yoma 8:7",
    talmud_bridge="Yoma 85a:11 — life is tested at the nose, from Gen 7:22 "
                  "('all in whose nostrils was the breath of the spirit of "
                  "life')",
    genesis_anchor="Gen.7.22 (gen_18_the_rise, claim G18-05)",
    anchor_pending="Leviticus 18:5 'and live by them' — the override's "
                   "surviving derivation for DOUBT cases (Yoma 85b:6); "
                   "Leviticus 18 not yet derived. Also owed: Exodus 31:16 "
                   "(the certain-danger derivation, Yoma 85b:3); Exodus 31 "
                   "not yet derived. See FRONTIER.md.",
)


def rule_life_override(case):
    if case.get("event") != "rockslide_burial" or case.get("day") != "shabbat":
        return None
    found = case.get("found")
    if found == "dead_mid_clearing":
        # THE MISHNAH'S OWN ADDITION: no machine claim held this leg (Class
        # C before compilation) — the verdict is imported from the case
        # shelf, and the provenance says exactly that.
        return [V("stop_clearing",
                  "Shabbat is not desecrated for the dignity of the dead",
                  machine_claim="G18-10 (seated 2026-08-31, finding F-001)",
                  **LIFE_PROV)]
    if found == "alive_mid_clearing":
        return [V("continue_clearing",
                  "life confirmed — the override stands until extrication; "
                  "digging from below one continues to the nose, from above "
                  "the nose suffices", machine_claim="G18-05", **LIFE_PROV)]
    if case.get("uncertain"):
        return [V("clear_the_debris",
                  "doubt of life overrides Shabbat; stacked uncertainties "
                  "(presence, life, identity) do not weaken the override",
                  machine_claim="G18-05", **LIFE_PROV)]
    return None


# ----------------------------------------------------- procreation_measure
PRO_PROV = dict(
    mishnah="Mishnah Yevamot 6:6",
    talmud_bridge="the Mishnah itself cites Gen 5:2 (Hillel) and Gen 1:28 "
                  "(R. Yochanan ben Beroka) — the bridge is inside the row",
    genesis_anchor="Gen.5.2 (gen_14, claim G14-15); Gen.16.3 (gen_32, claim "
                   "G32-16); Gen.1.28 ketiv (gen_06, claim G06-03)",
)


def rule_procreation(case):
    if case.get("person") == "woman":
        # the machine holds ONE side in ink (the lean ve-khivshuha ketiv,
        # 'and subdue HER' -> the man is commanded); the dissent is imported.
        return [
            V("not_commanded",
              "the written skeleton of Gen 1:28 reads 'and subdue HER' in "
              "the singular — the man, not the woman, is commanded",
              authority="the anonymous first opinion",
              machine_claim="G06-03 (ink-derived, Yevamot 65b)", **PRO_PROV),
            V("commanded",
              "'And God blessed THEM... be fruitful and multiply' — Gen "
              "1:28 addresses both",
              authority="R. Yochanan ben Beroka",
              machine_claim="G06-12 (claim-visible 2026-08-31, finding F-003; held in the BLESS operator prose since 2026-08-23)", **PRO_PROV),
        ]
    if case.get("person") != "man":
        return None
    kids = case.get("children")
    if kids is not None:
        males = kids.count("male")
        females = kids.count("female")
        shammai = "duty_discharged" if males >= 2 else "duty_stands"
        hillel = ("duty_discharged" if (males >= 1 and females >= 1)
                  else "duty_stands")
        if shammai == hillel:
            return [V(shammai, "both houses agree on this composition",
                      machine_claim="G14-15", **PRO_PROV)]
        return [
            V(shammai, "two males discharge the duty",
              authority="Beit Shammai", machine_claim="G14-15", **PRO_PROV),
            V(hillel, "a male AND a female — 'male and female He created "
              "them' (Gen 5:2)", authority="Beit Hillel",
              machine_claim="G14-15", **PRO_PROV),
        ]
    if case.get("married_years") is not None:
        # the ten-years rule — held at Gen 16:3, with the tradition's own
        # epistemic grade and riders the exam spec did not know.
        yrs = case["married_years"]
        since = case.get("miscarriage_at_year")
        if since is not None:
            effective = yrs - since
            v = ("count_restarts_from_miscarriage" if effective < 10
                 else "must_act")
            return [V(v, "the ten-year count restarts from the miscarriage",
                      machine_claim="G32-22 (seated 2026-08-31, finding F-002)",
                      **PRO_PROV)]
        if yrs >= 10 and case.get("births", 0) == 0:
            return [V("must_act",
                      "ten childless years — divorce and remarry, or take a "
                      "second wife. RIDERS THE MACHINE ALREADY HELD (G32-16, "
                      "Gen 16:3): years outside the Land do not count; "
                      "sickness and imprisonment are excluded. GRADE: the "
                      "tradition marks this derivation 'no proof, but a "
                      "hint' (Tosefta Yevamot 8:4)",
                      machine_claim="G32-16", **PRO_PROV)]
        return [V("duty_stands", "under ten years — the count still runs",
                  machine_claim="G32-16", **PRO_PROV)]
    return None


# judgment_durations: DELIBERATELY NOT COMPILED — the report shows the
# contrast between an examined module and a compiled one.

# Module registry — routing follows the Mishnah's own organization (the
# owner's tractate map, logic/MISHNAH_TOPICS.md): each module names the
# tractate whose case rows feed it, so the code's structure grows into the
# tradition's structure as more books and tractates arrive.
RULES = {
    "life_override": {"fn": rule_life_override, "tractate": "Yoma"},
    "procreation_measure": {"fn": rule_procreation, "tractate": "Yevamot"},
}


def answer(module, case_input):
    entry = RULES.get(module)
    return entry["fn"](case_input) if entry else None
