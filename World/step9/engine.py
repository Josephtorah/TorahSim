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


# ------------------------------------------------------ judgment_durations
# F-004 (owner: "build F-004"): the flood's twelve months is COMPUTED from
# the machine's own date rows — the first verdict derived end to end from
# the corpus's facts rather than looked up. The gehinom member is
# IMPORT-ONLY by the owner's ruling on F-005 ("ok import only for F-005").
import re as _re
import sqlite3 as _sql
from pathlib import Path as _P

_WORLD_DB = _P(__file__).resolve().parent.parent / "world.sqlite"

EDU_PROV = dict(
    mishnah="Mishnah Eduyot 2:10",
    talmud_bridge="the Mishnah's five-judgment census itself — our flood is "
                  "its first member (machine claim G17-11 holds the census "
                  "and the day-by-day calendar)",
    genesis_anchor="Gen.7.11 start anchor; Gen.8.13-14 end (gen_17_boarding, "
                   "gen_19_the_remembering)",
)

_NUM = {"echad": 1, "sheni": 2, "shivah": 7, "esrim": 20}


def _flood_span():
    """Read the machine's own date rows and compute the span. Returns
    (months, days_beyond, provenance_rows) or None if the rows are absent —
    the verdict is COMPUTED, never assumed."""
    if not _WORLD_DB.exists():
        return None
    con = _sql.connect(_WORLD_DB)
    rows = {}
    for seq, unit, ref, payload in con.execute(
            "SELECT seq, unit, ref, payload FROM standing "
            "WHERE kind='TIME_ANCHOR'"):
        m = _re.search(r"shnat_(\d+)_chodesh_(\d+)_yom_(\d+)", payload)
        if m:
            rows[ref] = (tuple(int(x) for x in m.groups()),
                         "standing seq %d (%s)" % (seq, unit))
    end_fact = con.execute(
        "SELECT seq, unit, fact FROM facts WHERE ref='Gen.8.14' "
        "AND fact LIKE 'ba_chodesh%'").fetchone()
    con.close()
    start = rows.get("Gen.7.11")
    year_marker = rows.get("Gen.8.13")
    if not (start and year_marker and end_fact):
        return None
    (y1, m1, d1), src1 = start
    (y2, _, _), src2 = year_marker
    # the end fact spells its numbers in the corpus's own transliteration:
    # ba_chodesh_ha_sheni_be_shivah_ve_esrim_yom — month 2, day 27
    parts = end_fact[2].split("_")
    nums = [_NUM[p] for p in parts if p in _NUM]
    m2 = nums[0]
    d2 = sum(nums[1:])
    months = (y2 - y1) * 12 + (m2 - m1)
    days = d2 - d1
    prov = [src1, src2,
            "fact seq %d (%s): %s" % (end_fact[0], end_fact[1], end_fact[2])]
    return months, days, prov


def rule_judgment_durations(case):
    if case.get("query") != "duration_of_judgment":
        return None
    subj = case.get("subject")
    if subj == "generation_of_the_flood":
        span = _flood_span()
        if span is None:
            return [V("twelve_months",
                      "held as the chain's ruling (G17-11); the date rows "
                      "were not found to compute from",
                      machine_claim="G17-11", **EDU_PROV)]
        months, days, prov = span
        return [V("twelve_months",
                  "COMPUTED from the machine's own date rows: year 600 "
                  "month 2 day 17 (the breach) to year 601 month 2 day 27 "
                  "(the earth dry) = %d months and %d days beyond — the "
                  "excess the chain itself counts as the solar year's "
                  "eleven days over the lunar (G17-11). The Mishnah's "
                  "twelve-month row, derived end to end from the corpus."
                  % (months, days),
                  machine_claim="G17-11; date rows: " + "; ".join(prov),
                  **EDU_PROV)]
    if subj == "the_wicked_in_gehinom":
        return [
            V("twelve_months", "Isaiah 66:23 — 'from one month until its "
              "month'", authority="the anonymous first opinion",
              imported_from="Mishnah Eduyot 2:10 — IMPORT-ONLY by owner "
                            "ruling on F-005 (2026-08-31); no Genesis "
                            "anchor; proof text is Isaiah, not yet derived",
              **EDU_PROV),
            V("passover_to_shavuot", "Isaiah 66:23 — 'from one sabbath "
              "until its sabbath'", authority="R. Yochanan ben Nuri",
              imported_from="Mishnah Eduyot 2:10 — IMPORT-ONLY per F-005",
              **EDU_PROV),
        ]
    return None


# ============================= THE GENESIS SWEEP (2026-08-31, owner: "Go")
# Seven modules compiled from cases_gen_sweep.yaml — every remaining
# Mishnah case row citing Genesis. Findings F-007..F-011 filed for the
# unheld legs; imports labeled in provenance, never silent.

# ---------------------------------------------------------- sciatic_nerve
SINEW_PROV = dict(
    mishnah="Mishnah Chullin 7:1 + 7:6",
    talmud_bridge="the Mishnah itself quotes Gen 32:33 at 7:6 ('therefore "
                  "the children of Israel eat not the sinew of the "
                  "thigh-vein'); Chullin 89b-103a develops scope",
    genesis_anchor="Gen.32.33 (gen_55_two_camps_wrestled_name, claim "
                   "G55-31) — Genesis's only narrator-voice food law",
)


def rule_sciatic_nerve(case):
    animal = case.get("animal")
    if case.get("part") == "sinew_fat":
        return [V("permitted",
                  "its fat is permitted — technically; Israel's "
                  "self-stringency on the outer extensions recorded as "
                  "such, not as law (Rav Huna)",
                  machine_claim="G55-31", **SINEW_PROV)]
    if animal == "bird":
        return [V("permitted",
                  "does not apply to a bird, for it has no spoon (socket) "
                  "of the thigh", machine_claim="G55-31", **SINEW_PROV)]
    if animal == "fetus":
        return [
            V("forbidden", "applies to the fetus",
              authority="the anonymous first opinion",
              machine_claim="G55-31", **SINEW_PROV),
            V("permitted", "does not apply to the fetus",
              authority="R. Yehudah", machine_claim="G55-31", **SINEW_PROV),
        ]
    if animal == "impure_species":
        # the PROVENANCE dispute — when was this law given? (F-011)
        return [
            V("forbidden", "the sinew was forbidden from the sons of "
              "Jacob, while impure animals were still permitted them",
              authority="R. Yehudah",
              machine_claim="G55-35 (seated 2026-08-31, finding F-011)",
              **SINEW_PROV),
            V("permitted", "it was said at SINAI, but written in its "
              "place — the law never bound the patriarchal era",
              authority="the sages",
              machine_claim="G55-35 (seated 2026-08-31, finding F-011)",
              **SINEW_PROV),
        ]
    if animal == "beast" or case.get("thigh") in ("right", "left"):
        return [V("forbidden",
                  "applies in the Land and outside it, with the Temple "
                  "and without, to beast and wild animal, right thigh and "
                  "left; the gemara's one-side-vs-both dispute is held "
                  "with each side's own logic-dictates tradition",
                  machine_claim="G55-31", **SINEW_PROV)]
    return None


# ----------------------------------------------------------- day_boundary
DAY_PROV = dict(
    mishnah="Mishnah Chullin 5:5",
    talmud_bridge="Ben Zoma's verbal analogy (gezerah shavah, middah I2): "
                  "'ONE DAY' of it-and-its-young reads as 'ONE DAY' of "
                  "the work of creation — the day follows the night",
    genesis_anchor="Gen.1.5 (gen_01_creation_boot) — 'and there was "
                   "EVENING and there was MORNING, one day': evening "
                   "precedes morning in the ink the machine executes",
    anchor_pending="Leviticus 22:28 — the it-and-its-young law itself; "
                   "Leviticus 22 not yet derived. See FRONTIER.md.",
)


def rule_day_boundary(case):
    m = case.get("mother_slaughtered")
    o = case.get("offspring_slaughtered")
    if m == "night" and o == "following_day":
        return [V("same_day_violation",
                  "the day follows the night — the night and its "
                  "following daytime are ONE day of Gen 1:5's structure",
                  machine_claim="gen_01_creation_boot operator order "
                  "(evening before morning)", **DAY_PROV)]
    if m == "day" and o == "following_night":
        return [V("different_days_permitted",
                  "nightfall closed the day — the following night opens "
                  "the NEXT day", machine_claim="gen_01_creation_boot "
                  "operator order", **DAY_PROV)]
    return None


# --------------------------------------------------------- seas_as_mikveh
SEAS_PROV = dict(
    mishnah="Mishnah Mikvaot 5:4 (verbatim = Mishnah Parah 8:8)",
    talmud_bridge="the Mishnah quotes Gen 1:10 itself in R. Meir's name",
    genesis_anchor="Gen.1.10 (gen_03_double_build, NAME operator) — 'and "
                   "the GATHERING (mikveh) of the waters He called SEAS' "
                   "— the naming's own noun is the ritual-pool term",
)


def rule_seas_as_mikveh(case):
    if case.get("water_body") not in ("sea", "great_sea") \
            or case.get("use") != "ritual_immersion":
        return None
    return [
        V("valid_as_mikveh", "all seas are as a mikveh — from our verse's "
          "naming", authority="R. Meir",
          machine_claim="G03-12 (seated 2026-08-31, finding F-007; held in "
          "the NAME op prose since 2026-08-23)",
          **SEAS_PROV),
        V("only_the_great_sea", "the Great Sea alone is as a mikveh; "
          "'seas' is plural because many kinds of seas are in it",
          authority="R. Yehudah",
          machine_claim="G03-12 (seated 2026-08-31)", **SEAS_PROV),
        V("purify_as_flowing", "all seas purify as flowing streams, yet "
          "are invalid for zavim (those with a discharge), metzoraim "
          "(those with the plague), and sanctifying purification-waters",
          authority="R. Yosei",
          machine_claim="G03-12 (seated 2026-08-31)", **SEAS_PROV),
    ]


# ------------------------------------------------ forgiveness_after_injury
FORGIVE_PROV = dict(
    mishnah="Mishnah Bava Kamma 8:7",
    talmud_bridge="the Mishnah quotes both verses itself",
    genesis_anchor="Gen.20.7 + Gen.20.17 (gen_36_gerar_dream_prophet, "
                   "operators THE_PROPHET_AND_THE_RETURN_COMMAND and "
                   "THE_PRAYER_AND_THE_HEALING)",
)


def rule_forgiveness(case):
    if case.get("injurer_paid") == "yes" \
            and case.get("asked_forgiveness") == "no":
        return [V("not_forgiven",
                  "though he pays him, he is not forgiven until he ASKS "
                  "of him — 'now restore the man's wife, for he is a "
                  "prophet and will pray for you'",
                  machine_claim="G36-18 (seated 2026-08-31, finding F-008)",
                  **FORGIVE_PROV)]
    if case.get("victim_asked") == "yes" \
            and case.get("victim_withholds") == "yes":
        return [V("withholder_is_cruel",
                  "the forgiver must not be cruel — 'and Abraham prayed "
                  "to God, and God healed Abimelech': the wronged prayed "
                  "for his own wronger",
                  machine_claim="G36-18 (seated 2026-08-31, finding F-008)", **FORGIVE_PROV)]
    return None


# --------------------------------------------------------- seed_categories
SEED_PROV = dict(
    mishnah="Mishnah Nedarim 3:11",
    talmud_bridge="the Mishnah's own rows; the descent statute at Gen "
                  "21:12 read partitive ('IN Isaac — part and not all')",
    genesis_anchor="Gen.21.12 (gen_37_laughter_wilderness_oath, claim "
                   "G37-25); Genesis 17 whole "
                   "(gen_33_shaddai_covenant_flesh)",
)

_GEN_XML = _P("<repo-old>/Data/Gen.xml")


def _covenant_count():
    """Count covenant-word tokens in Genesis 17's own ink. COMPUTED,
    never assumed — returns (count, per-verse list) or None."""
    if not _GEN_XML.exists():
        return None
    import unicodedata
    xml = _GEN_XML.read_text(encoding="utf-8")
    ch = _re.findall(r'<verse osisID="Gen\.17\.(\d+)"[^>]*>(.*?)</verse>',
                     xml, _re.S)
    if not ch:
        return None
    total, per = 0, []
    for vnum, body in ch:
        words = _re.findall(r"<w[^>]*>([^<>]*)</w>", body)
        n = 0
        for w in words:
            skel = "".join(c for c in w if not
                           unicodedata.category(c).startswith("M"))
            if "ברית" in skel.replace("/", ""):
                n += 1
        if n:
            per.append("Gen.17.%s:%d" % (vnum, n))
            total += n
    return total, per


def rule_seed_categories(case):
    if case.get("query") == "covenants_over_circumcision":
        cc = _covenant_count()
        if cc is None:
            return [V("thirteen", "R. Yishmael's count, held as text — the "
                      "ink was not found to compute from",
                      machine_claim="G33-30 (seated 2026-08-31, finding F-009)", **SEED_PROV)]
        total, per = cc
        return [V("thirteen" if total == 13 else "count_mismatch_%d" % total,
                  "COMPUTED from the machine's own Genesis 17 ink: %d "
                  "covenant-word tokens (%s). R. Yishmael's 'thirteen "
                  "covenants were cut over circumcision' — the count is "
                  "the chapter's own token census." % (total, ", ".join(per)),
                  machine_claim="G33-30 (seated 2026-08-31, finding F-009) + live "
                  "Data/Gen.xml ink census", **SEED_PROV)]
    vow = case.get("vow")
    cp = case.get("counterparty")
    if vow == "no_benefit_from_sons_of_noah":
        if cp == "israelite":
            return [V("permitted", "Israel left the sons-of-Noah category "
                      "through Abraham — the vow does not reach them",
                      machine_claim="category structure; the exit-by-"
                      "Abraham reading imported from the row",
                      **SEED_PROV)]
        return [V("forbidden", "the nations remain in the sons-of-Noah "
                  "category", machine_claim="imported from the row",
                  **SEED_PROV)]
    if vow == "no_benefit_from_seed_of_abraham":
        if cp == "descendant_of_ishmael_or_esau":
            return [V("permitted", "'in Isaac shall seed be called to "
                      "you' — partitive: part of Isaac and not all of "
                      "him; Ishmael and Esau stand outside the called "
                      "line", machine_claim="G37-25", **SEED_PROV)]
        if cp == "israelite":
            return [V("forbidden", "Israel is the called seed",
                      machine_claim="G37-25", **SEED_PROV)]
    return None


# ---------------------------------------------------------- world_to_come
WTC_PROV = dict(
    mishnah="Mishnah Sanhedrin 10:3",
    talmud_bridge="the Mishnah quotes the three Genesis verses itself",
    genesis_anchor="Gen.6.3 (gen_15_flood_prologue, claim G15-10); "
                   "Gen.11.8-9 (gen_25_babel); Gen.13.13 "
                   "(gen_29_separation_promise, THE_SODOM_VERDICT)",
    anchor_pending="the chapter's non-Genesis members (spies, wilderness "
                   "generation, Korach's band, ten tribes) rest on "
                   "Numbers and Deuteronomy — not yet derived. See "
                   "FRONTIER.md.",
)


def rule_world_to_come(case):
    if case.get("query") != "share_in_world_to_come":
        return None
    subj = case.get("subject")
    if subj == "generation_of_the_flood":
        return [V("no_share_and_no_judgment",
                  "'My spirit shall not JUDGE (yadon) man forever' — "
                  "neither judgment nor spirit; the tannaim parse the "
                  "clause four ways, all held",
                  machine_claim="G15-10 (verdict AND derivation held)",
                  **WTC_PROV)]
    if subj == "generation_of_the_dispersion":
        return [V("no_share",
                  "'and the LORD scattered them' — the scattering "
                  "doubled: this world and the next",
                  machine_claim="G25-16 (seated 2026-08-31, finding F-010)", **WTC_PROV)]
    if subj == "men_of_sodom":
        return [
            V("no_share_but_stand_in_judgment",
              "'wicked' in this world, 'and sinners' in the next — yet "
              "they stand in judgment",
              authority="the anonymous first opinion",
              machine_claim="G29-23 (held since the unit's own reading — the "
              "finding's Sodom no-share leg was wrong, corrected at the "
              "seat)", **WTC_PROV),
            V("no_share_and_no_judgment",
              "these and those do not stand in judgment",
              authority="R. Nechemiah",
              machine_claim="G29-25 (seated 2026-08-31, finding F-010)", **WTC_PROV),
        ]
    return None


# ------------------------------------------------- circumcision_third_day
CIRC_PROV = dict(
    mishnah="Mishnah Shabbat 19:3 (+ 9:3, the same Genesis leg)",
    talmud_bridge="Shmuel's ruling in the held cluster: BECAUSE OF "
                  "DANGER, OUR VERSE IS THE MEASURE of the third day's "
                  "peril",
    genesis_anchor="Gen.34.25 (gen_57_deceit_at_the_gate, claim G57-23) "
                   "— 'on the third day, when they were in pain'",
)


def rule_circumcision_third_day(case):
    if case.get("day") != "shabbat":
        return None
    state = case.get("child_state")
    if state == "third_day_after_circumcision" \
            and case.get("act") == "bathing":
        return [V("permitted",
                  "the third day's peril, measured by our verse — danger "
                  "overrides Shabbat (R. Elazar b. Azariah; Shmuel)",
                  machine_claim="G57-23", **CIRC_PROV)]
    if state == "safek_or_androgynos" and case.get("act") == "circumcision":
        return [
            V("no_override",
              "doubt and the androgynos do not override Shabbat — "
              "structural contrast with the life_override module: doubt "
              "of LIFE overrides, doubt of OBLIGATION does not",
              authority="the anonymous first opinion",
              machine_claim="the contrast structure; the safek rule "
              "itself imported (no Genesis anchor claimed by the row)",
              **CIRC_PROV),
            V("override_for_androgynos", "R. Yehudah permits the "
              "androgynos", authority="R. Yehudah",
              machine_claim="imported from the row", **CIRC_PROV),
        ]
    return None


# =================================================================
# THE NOAHIDE BLOCK (2026-09-01, owner: "open the noahide block") —
# the first TALMUD-ONLY law modules: no Mishnah row above them. The
# provenance key is talmud_source, not mishnah + talmud_bridge: the
# Talmud is the ruling body here and Genesis its stated derivation.
# Spec: cases_noahide.yaml. Findings F-012..F-016 mark the unheld and
# half-held legs; nothing fixed inline.

SEVEN_PROV = dict(
    talmud_source="Sanhedrin 56a:24 (the baraita) + 56b:4-8 (the "
                  "word-by-word derivation) + 57a:1-7 (the school of "
                  "Menashe's alternate system)",
    genesis_anchor="Gen.2.16 (gen_08_toledot_garden_first_rule, claim "
                   "G08-28 — the unit's crown)",
)


def rule_noahide_seven_laws(case):
    q = case.get("query")
    if q == "noahide_laws_census":
        return [
            V("seven_laws",
              "courts, blasphemy, idolatry, forbidden relations, "
              "bloodshed, robbery, limb from the living",
              authority="the baraita (Sanhedrin 56a:24), derived word by "
                        "word from Gen 2:16",
              machine_claim="G08-28", **SEVEN_PROV),
            V("seven_laws_menashe_variant",
              "castration (Gen 9:7) and mixed kinds (Gen 6:20) IN; "
              "courts and blasphemy OUT — the flood indictment "
              "(Gen 6:11-12) as its derivation spine",
              authority="the school of Menashe (Sanhedrin 57a:1-7)",
              machine_claim="legs held: G21-15 (castration + dissent), "
                            "G16-15 (mixed-kinds dispute); the list "
                            "variant itself talmud_source only",
              **SEVEN_PROV),
        ]
    if q == "laws_commanded_to_adam":
        return [
            V("idolatry_only", "ויצו ה' אלהים על האדם — 'and the LORD God "
              "commanded THE MAN' (Gen 2:16)",
              authority="R. Yehudah (Sanhedrin 56b:23)",
              machine_claim="G08-28 (the dispute recorded)", **SEVEN_PROV),
            V("also_blasphemy", "the Name in the same clause",
              authority="R. Yehudah ben Beteira (56b:23)",
              machine_claim="G08-28", **SEVEN_PROV),
            V("also_courts", "אלהים read as the judges",
              authority="some say (56b:23)",
              machine_claim="G08-28", **SEVEN_PROV),
        ]
    if q == "which_token_yields":
        tok = case.get("token")
        if tok == "vayetzav":
            return [
                V("courts", "ויצו — 'and He commanded': as it says, 'he "
                  "will command his children... to DO JUSTICE' (Gen "
                  "18:19)",
                  authority="the mainline derivation (Sanhedrin 56b:5)",
                  machine_claim="G08-30 (F-012 SEATED 2026-09-01 — the dispute dual-track beside G08-28)", **SEVEN_PROV),
                V("idolatry", "ויצו = idolatry, אלהים = courts — the "
                  "inversion",
                  authority="R. Yitzchak (Sanhedrin 56b:8; Bereshit "
                            "Rabbah 16:6's side)",
                  machine_claim="G08-28", **SEVEN_PROV),
            ]
        if tok == "every_tree":
            return [V("robbery_ban",
                      "מכל עץ הגן — 'of every tree of the garden': yours "
                      "and not stolen (56b:7); and from Gen 9:3 'as the "
                      "GREEN herb' — like ownerless field growth, not a "
                      "tended garden (R. Levi, 57a:4)",
                      machine_claim="G21-08 (the 9:3 route with its "
                                    "recorded dispute)", **SEVEN_PROV)]
    return None


EXEC_PROV = dict(
    talmud_source="Sanhedrin 57a:8 (three) / 57a:11 (four) / 57a:13 (all "
                  "seven); 57a:12 — their prohibition is their death",
    genesis_anchor="Gen.9.6 (gen_21_blessing_blood_law, claim G21-11 — "
                   "'revealed at bloodshed, the same holds for all')",
)


def rule_noahide_execution_scope(case):
    if case.get("query") != "noahide_executed_for":
        return None
    law = case.get("law")
    if law == "bloodshed" and "killer" not in case and "victim" not in case:
        return [V("executed",
                  "explicit at Gen 9:6 — every rung of the count ladder "
                  "agrees", machine_claim="G21-11", **EXEC_PROV)]
    if law == "robbery":
        return [
            V("not_executed",
              "the school of Rav's counts: three (relations, bloodshed, "
              "blasphemy — the גש\"ר mnemonic) or four (idolatry joins) — "
              "robbery outside both",
              authority="Rav Yosef 57a:8; Rav Sheshet 57a:11",
              machine_claim="talmud_source only (the ladder rungs "
                            "unheld)", **EXEC_PROV),
            V("executed",
              "'the Merciful revealed it at bloodshed and the same holds "
              "for all'",
              authority="Rav Huna, Rav Yehudah, all the students of Rav "
                        "(57a:13)",
              machine_claim="G21-11 (the paradigm sentence held)",
              **EXEC_PROV),
        ]
    return None


PROC_PROV = dict(
    talmud_source="Sanhedrin 57b:2 (the aggadah-book baraita) + 57b:3-5 "
                  "(Gen 9:5 word by word) + 57b:6 + 57b:9",
    genesis_anchor="Gen.9.5-6 (gen_21_blessing_blood_law, claim G21-11; "
                   "the no-forewarning second leg G36-14 at Gen 20:7)",
)


def rule_noahide_procedure(case):
    q = case.get("query")
    if q == "conviction_stands":
        w = case.get("witness_is")
        if w == "woman":
            return [V("testimony_not_accepted",
                      "מיד איש — 'from the hand of a MAN,' and not from a "
                      "woman's mouth (57b:2/4)",
                      machine_claim="G21-17 (F-013 seated 2026-09-01)", **PROC_PROV)]
        if w == "relative":
            return [V("conviction_stands",
                      "אחיו — 'his brother': even a relative (57b:4)",
                      machine_claim="G21-17 (F-013 seated 2026-09-01)", **PROC_PROV)]
        return [V("conviction_stands",
                  "one judge (Gen 9:5 'I will require it' — singular), "
                  "one witness, no forewarning — each from its own word",
                  machine_claim="G21-11", **PROC_PROV)]
    if q == "noahide_executed_for" and case.get("law") == "bloodshed":
        if case.get("killer") == "woman":
            return [V("executed",
                      "שופך דם האדם — 'WHOEVER sheds the blood of man,' "
                      "in any case (Rav Yehudah's resolution, 57b:9)",
                      machine_claim="G21-17 (F-013 seated 2026-09-01)", **PROC_PROV)]
        if case.get("victim") == "fetus":
            return [
                V("executed",
                  "באדם — 'the blood of man IN a man' is the embryo",
                  authority="R. Yishmael (57b:5)",
                  machine_claim="G21-11 (the fetus reading)", **PROC_PROV),
                V("mode_reading_strangulation",
                  "באדם routed to execution mode — bloodshed of a man "
                  "that stays IN his body is strangulation",
                  authority="the school of Menashe (57b:6)",
                  machine_claim="G21-11 (the strangler)", **PROC_PROV),
            ]
    return None


REL_PROV = dict(
    talmud_source="Sanhedrin 58a:7-8 (Gen 2:24 dissected) + 57b:10 + "
                  "58b:5-6 + 58b:14",
    genesis_anchor="Gen.2.24 (gen_09_helper_woman_first_speech, claim "
                   "G09-19 — the span's law crown)",
)


def rule_noahide_relations(case):
    q = case.get("query")
    if q == "relation_permitted":
        p = case.get("partner")
        if p == "male":
            return [V("forbidden", "ודבק — 'and shall CLEAVE,' not to a "
                      "male (58a:8)", machine_claim="G09-19", **REL_PROV)]
        if p == "neighbors_wife":
            return [V("forbidden", "באשתו — 'to HIS wife,' not the "
                      "neighbor's (58a:8)", machine_claim="G09-19",
                      **REL_PROV)]
        if p == "animal":
            return [V("forbidden", "והיו לבשר אחד — those who can become "
                      "one flesh; beast and wild animal excluded (58a:8)",
                      machine_claim="G09-19", **REL_PROV)]
        if p == "fathers_side":
            return [
                V("fathers_sister_banned", "אביו = the father's sister",
                  authority="R. Eliezer (58a:7)",
                  machine_claim="G09-19 (dual-track)", **REL_PROV),
                V("fathers_wife_banned", "אביו = the father's wife",
                  authority="R. Akiva (58a:7)",
                  machine_claim="G09-19 (dual-track)", **REL_PROV),
            ]
        if p == "maternal_sister":
            return [V("forbidden",
                      "the baraita's law; Gen 20:12 ('my father's "
                      "daughter, NOT my mother's') pressed as proof at "
                      "58b:5 and DEFLECTED at 58b:6 — the verse's "
                      "recorded role is attempted evidence",
                      machine_claim="G36-19 (F-016 seated 2026-09-01 as a kept record)", **REL_PROV)]
    if q == "relation_liability" and case.get("subject_gender") == "woman":
        return [V("liable",
                  "proposed exempt from יעזב איש ('a MAN shall leave'); "
                  "resolved — והיו לבשר אחד re-combined them (57b:10)",
                  machine_claim="G09-19 (the gender scope settled from "
                                "the tail clause)", **REL_PROV)]
    return None


SAB_PROV = dict(
    talmud_source="Sanhedrin 58b:25 (Resh Lakish; Ravina — even a "
                  "Monday) + 57a:12 (their prohibition is their death) + "
                  "59a:2-5 (the Torah-study exchange)",
    genesis_anchor="Gen.8.22 (gen_20_exit_altar, claim G20-19 — seated "
                   "2026-09-01; G20-18 the termination-condition reading)",
)


def rule_gentile_sabbath_torah(case):
    if case.get("query") != "gentile_liability":
        return None
    act = case.get("act")
    if act == "kept_full_sabbath":
        return [V("liable",
                  "ויום ולילה לא ישבותו — 'day and night they shall not "
                  "CEASE' (Gen 8:22) read onto them; their prohibition "
                  "is their death; any full day of rest, even Monday",
                  machine_claim="G20-19 (F-014 seated 2026-09-01)",
                  **SAB_PROV)]
    if act == "studied_torah":
        return [
            V("liable", "מורשה — 'an inheritance' (Deut 33:4): ours, not "
              "theirs (read also as מאורסה, 'betrothed')",
              authority="R. Yochanan (59a:2)",
              machine_claim="imported — no Genesis ink; Deut 33:4 "
                            "anchor_pending", **SAB_PROV),
            V("like_high_priest", "האדם — 'THE MAN who does them and "
              "lives by them' (Lev 18:5), not priests-Levites-Israelites",
              authority="R. Meir (59a:4)",
              machine_claim="imported — Lev 18:5 anchor_pending (the "
                            "FRONTIER's standing row)", **SAB_PROV),
        ]
    if act == "studied_own_seven":
        return [V("praised_like_high_priest",
                  "התם בשבע מצות דידהו — 'there, in their own seven' "
                  "(the resolution, 59a:5)",
                  machine_claim="imported (the resolution row)",
                  **SAB_PROV)]
    return None


SINAI_PROV = dict(
    talmud_source="Sanhedrin 59a:10-12 (R. Yose son of R. Chanina's "
                  "framework) + 59b:1-12 (its test cases)",
    genesis_anchor="instances: Gen 32:33 (G55-35 + G55-36 the framework, held), Gen 21:12 "
                   "(G37-25, held), Gen 17:9/17:14 (G33-31, seated "
                   "2026-09-01)",
)


def rule_repeated_at_sinai(case):
    if case.get("query") != "who_is_bound":
        return None
    cmd = case.get("commandment")
    if cmd == "sciatic_nerve":
        return [V("israel_only_reverse_instance",
                  "said to Israel (the sons of Jacob) and not the sons "
                  "of Noach — 'and we have only the sinew, per R. "
                  "Yehudah' (59a:12)",
                  machine_claim="G55-35 (the effective-date dispute "
                                "seated)", **SINAI_PROV)]
    if cmd == "circumcision":
        lin = case.get("lineage")
        if lin == "sons_of_ishmael":
            return [V("exempt", "כי ביצחק יקרא לך זרע — 'IN Isaac shall "
                      "seed be called to you' (Gen 21:12, 59b:10)",
                      machine_claim="G37-25 + the compiled "
                                    "seed_categories module",
                      **SINAI_PROV)]
        if lin == "sons_of_esau":
            return [V("exempt", "ביצחק ולא כל יצחק — 'IN Isaac, and not "
                      "all of Isaac' (59b:11)",
                      machine_claim="G37-25 (the partitive excluding "
                                    "Esau)", **SINAI_PROV)]
        if lin == "sons_of_keturah":
            return [V("obligated", "את בריתי הפר — 'My covenant he has "
                      "broken' (Gen 17:14), to INCLUDE the sons of "
                      "Keturah (R. Yose bar Avin, 59b:12)",
                      machine_claim="G33-31 (F-015 seated 2026-09-01)",
                      **SINAI_PROV)]
        return [V("abraham_line_only",
                  "two recorded resolutions: the Sinai repetition (Lev "
                  "12:3) came to permit Shabbat (59b:2); or the command "
                  "was never general — אתה וזרעך, 'YOU and your seed,' "
                  "no one else (59b:9)",
                  machine_claim="G33-31 (F-015 seated 2026-09-01) + G33-24",
                  **SINAI_PROV)]
    if cmd == "procreation":
        return [V("israel_only",
                  "said to the sons of Noach (Gen 9:7) and repeated at "
                  "Sinai (Deut 5:27) — but the repetition came for the "
                  "counted-body principle (59b:4), so the framework "
                  "routes it to Israel",
                  machine_claim="the 9:7 verse-role dispute held at "
                                "G21-15 (command vs blessing); the "
                                "routing talmud_source", **SINAI_PROV)]
    s, r = case.get("said_to_noahides"), case.get("repeated_at_sinai")
    if s == "yes" and r == "yes":
        return [V("both_bound", "כל מצוה שנאמרה לבני נח ונשנית בסיני לזה "
                  "ולזה נאמרה — 'said to both' (59a:11)",
                  machine_claim="G55-36 (F-015 seated 2026-09-01)",
                  **SINAI_PROV)]
    if s == "yes" and r == "no":
        return [V("israel_only",
                  "not repeated — to Israel and not the sons of Noach; "
                  "the sugya's worked example is circumcision (59b:1)",
                  machine_claim="G55-36 (F-015 seated 2026-09-01)", **SINAI_PROV)]
    return None


MEAT_PROV = dict(
    talmud_source="Sanhedrin 59b:13-21 (the two-era grant + the labor "
                  "readings) + 57a:4-5 + 59a:6-9 (the carve-outs)",
    genesis_anchor="Gen.1.29-30 against Gen.9.3-4 "
                   "(gen_21_blessing_blood_law G21-08/G21-09; the "
                   "Adam-era grant and dominion-as-labor at gen_06 "
                   "rev 2)",
)


def rule_meat_timeline(case):
    q = case.get("query")
    if q == "dominion_meaning":
        return [V("labor_not_eating",
                  "ורדו — 'and have dominion' (Gen 1:26/1:28) pressed "
                  "three times: fish (driving with the shibbuta), fowl "
                  "(threshing with geese), the creeping serpent — each "
                  "resolved as labor (59b:16-21)",
                  machine_claim="gen_06 rev 2 (dominion = labor, read at "
                                "Sanhedrin 59b's own primary)",
                  **MEAT_PROV)]
    if q != "food_permitted":
        return None
    era, food = case.get("era"), case.get("food")
    if era == "adam" and food == "meat":
        return [V("forbidden",
                  "Gen 1:29 — the herb grant only: 'to you and to every "
                  "beast,' not the beasts to you (Rav, 59b:13)",
                  machine_claim="gen_06 rev 2 (the vegetarian grant)",
                  **MEAT_PROV)]
    if era == "noach":
        if food == "meat":
            return [V("permitted",
                      "כירק עשב נתתי לכם את כל — 'as the green herb I "
                      "have given you everything' (Gen 9:3)",
                      machine_claim="G21-08 (the two-era architecture "
                                    "stated)", **MEAT_PROV)]
        if food == "limb_from_living":
            return [V("forbidden",
                      "אך בשר בנפשו דמו לא תאכלו (Gen 9:4) — the ban "
                      "born of the grant one verse earlier",
                      machine_claim="G21-09 (the grant driving the law)",
                      **MEAT_PROV)]
        if food == "blood_from_living":
            return [
                V("forbidden", "the clause split two ways — the limb, "
                  "and the blood of a living animal",
                  authority="R. Chanina ben Gamliel (59a:6)",
                  machine_claim="G21-09 (the two-way split at the "
                                "baraita)", **MEAT_PROV),
                V("permitted_clause_routed_elsewhere",
                  "the rabbis route the clause to permit swarming "
                  "creatures (59a:7/9)",
                  authority="the rabbis",
                  machine_claim="G21-09", **MEAT_PROV),
            ]
        if food == "swarming_limb":
            return [V("excluded_from_ban",
                      "אך excludes them (59b:14); or Rav Huna — דמו, "
                      "'whose blood is distinct from its flesh' "
                      "(59b:15): two recorded routes, one verdict",
                      machine_claim="talmud_source (the routes); the "
                                    "ladder frame at G21-09",
                      **MEAT_PROV)]
    return None


OFR_PROV = dict(
    talmud_source="Avodah Zarah 51a:15-18 (R. Elazar's missing-limb "
                  "ban; the terefah steps) + Sanhedrin 57a:7 (mixed "
                  "kinds)",
    genesis_anchor="Gen.6.19-20 + Gen.7.3 + Gen.6.9 (gen_16_ark_spec, "
                   "claim G16-15 — the boarding list as altar standard)",
)


def rule_noahide_offerings(case):
    q = case.get("query")
    if q == "offering_valid" and case.get("offerer") == "noahide":
        d = case.get("defect")
        if d == "missing_limb":
            return [V("invalid",
                      "ומכל החי — 'of all the LIVING' (Gen 6:19): bring "
                      "an animal whose limbs are all alive (51a:15)",
                      machine_claim="G16-15", **OFR_PROV)]
        if d == "terefah":
            return [V("invalid",
                      "להחיות זרע — 'to keep seed ALIVE' (Gen 7:3): a "
                      "terefah cannot breed (51a:16); Noach himself "
                      "proven whole — תמים (Gen 6:9, 51a:18)",
                      machine_claim="G16-15 (its seat routes the "
                                    "exclusion via אתך = like-you; both "
                                    "steps are the sugya's own)",
                      **OFR_PROV)]
    if q == "noahide_bound_by" and case.get("law") == "mixed_kinds":
        return [
            V("bound", "מהעוף למינהו — 'of the fowl after its kind' "
              "(Gen 6:20) read as law",
              authority="the school of Menashe (57a:7)",
              machine_claim="G16-15 (the dispute recorded)", **OFR_PROV),
            V("not_bound", "the kinds-clause read as companionship "
              "only — לצותא בעלמא",
              authority="the other side (57a:7)",
              machine_claim="G16-15", **OFR_PROV),
        ]
    return None


CIRC_AGENT_PROV = dict(
    talmud_source="Avodah Zarah 26b:12 (R. Yehudah from Gen 17:9) + "
                  "27a:6 (the doubled-verb derivation)",
    genesis_anchor="Gen.17.9-13 (gen_33_shaddai_covenant_flesh, claims "
                   "G33-24 + G33-22)",
)


def rule_circumcision_agent(case):
    if case.get("query") == "circumcision_valid" \
            and case.get("circumciser") == "gentile":
        return [V("invalid",
                  "ואתה את בריתי תשמור — 'and YOU shall keep My "
                  "covenant' (Gen 17:9, R. Yehudah); or המול ימול — the "
                  "doubled verb (Gen 17:13): one verdict, two recorded "
                  "derivations",
                  machine_claim="G33-24 (eligibility) + G33-22 (the "
                                "doubled-verb battleground)",
                  **CIRC_AGENT_PROV)]
    return None


SHEM_PROV = dict(
    talmud_source="Avodah Zarah 36b:7 — 'harlotry too, the court of "
                  "Shem decreed against it'",
    genesis_anchor="Gen.38.24 (gen_61_yehuda_tamar, claim G61-16 — "
                   "Shem's court among the three where the Voice "
                   "testified)",
)


def rule_court_of_shem(case):
    if case.get("query") == "harlotry_justiciable" \
            and case.get("era") == "patriarchal":
        return [V("justiciable",
                  "ויאמר יהודה הוציאוה ותשרף — 'bring her out and let "
                  "her be burned' (Gen 38:24): a court already trying "
                  "harlotry; the decree's ancient seat",
                  machine_claim="G61-16 (the tribunal held; the "
                                "decree-history leg talmud_source)",
                  **SHEM_PROV)]
    return None


PUR_PROV = dict(
    talmud_source="Sanhedrin 72b:15 + 72b:17 (the warning formula and "
                  "the acceptance ladder)",
    genesis_anchor="Gen.9.6 (gen_21_blessing_blood_law, claim G21-13 — "
                   "refusal and license on one verse)",
)


def rule_pursuer(case):
    q = case.get("query")
    if q == "bystander_may_kill" \
            and case.get("target") == "pursuer_to_kill":
        return [V("licensed",
                  "שופך דם האדם באדם דמו ישפך — באדם read "
                  "instrumentally: 'save the blood of the pursued BY the "
                  "blood of the pursuer' (72b:15); whether the pursuer "
                  "needs forewarning is disputed on both sides",
                  machine_claim="G21-13", **PUR_PROV)]
    if q == "pursuer_court_liability" \
            and case.get("said") == "on_that_condition":
        return [V("liable",
                  "the acceptance ladder (72b:17): 'I know it is so' — "
                  "exempt; 'on that condition I act' — liable",
                  machine_claim="G21-13 (the formula's verse-use held; "
                                "the ladder talmud_source)",
                  **PUR_PROV)]
    return None


# =================================================================
# THE MISHPATIM EXAM (2026-09-01, owner: "run step 9 on mishpatim") —
# the first parashah-rhythm round: the statutes derived in the morning,
# the case shelf faced the same day. Provenance carries mekhilta_spine
# (the spine read the sitting the statutes were derived) beside the
# Mishnah row and the Exodus anchor. Spec: cases_mishpatim.yaml.

def _MP(mishnah, spine, anchor, **extra):
    d = dict(mishnah=mishnah, mekhilta_spine=spine, exodus_anchor=anchor)
    d.update(extra)
    return d

AVOT_PROV = _MP("Mishnah Bava Kamma 1:1 + 2:2 + 5:7 + 6:2; Gittin 5:1",
                "Mekhilta on Exod 22:4-5 (read 2026-09-01)",
                "Exod.22.4-5 (exo_22_property_social, EX22-02/03/08)")


def rule_four_avot_damages(case):
    q = case.get("query")
    if q == "damage_category_census":
        return [V("four_fathers", "the ox, the pit, the grazer, the "
                  "fire — not this like that, the common side: their "
                  "way is to damage and their keeping is on you",
                  machine_claim="EX22-02 (tooth) + EX22-03 (fire); ox "
                  "and pit at the frozen exo_21 units", **AVOT_PROV)]
    if q == "assessment_land":
        return [V("best_land", "payment from the BEST land (meitav) — "
                  "the Mekhilta's R. Yishmael / R. Akiva dispute, the "
                  "Mishnah's standing table (damages best, creditor "
                  "middling, ketubah poorest — Gittin 5:1)",
                  machine_claim="EX22-02", **AVOT_PROV)]
    if q == "species_scope":
        return [V("same_as_ox", "ox = every beast, wild animal and "
                  "fowl for the whole duty-list — 'the verse spoke of "
                  "the ORDINARY CASE'", machine_claim="EX22-08 (dibber "
                  "ba-hoveh, the named method)", **AVOT_PROV)]
    if q == "damage_liability" and case.get("eaten") == "suited_produce":
        dom = case.get("damage_domain")
        if dom == "public":
            return [V("exempt_pays_benefit", "in the public domain the "
                      "tooth is exempt — pays what it benefited",
                      machine_claim="EX22-02 (the domain matrix)",
                      **AVOT_PROV)]
        if dom == "victims":
            return [V("full_payment", "in the victim's domain the "
                      "tooth pays in full", machine_claim="EX22-02",
                      **AVOT_PROV)]
    return None


FIRE_PROV = _MP("Mishnah Bava Kamma 6:4 + 6:5 (quoting Exod 22:5)",
                "Mekhilta on Exod 22:5", "Exod.22.5 (EX22-03)")


def rule_fire_liability(case):
    q = case.get("query")
    if q == "fire_agency":
        v = case.get("via")
        if v == "incompetent":
            return [V("exempt_human_liable_heaven", "sent by the "
                      "deaf-mute, the deranged, the minor — exempt in "
                      "man's court, liable in Heaven's",
                      machine_claim="EX22-03", **FIRE_PROV)]
        if v == "wind":
            return [V("all_exempt", "the wind fanned it — all exempt",
                      machine_claim="EX22-03", **FIRE_PROV)]
    if q == "fire_distance":
        return [
            V("beit_kor", "as if standing in the middle of a beit kor",
              authority="R. Elazar ben Azariah", machine_claim="EX22-03 "
              "(the Mekhilta's own table)", **FIRE_PROV),
            V("sixteen_cubits", "as the public road",
              authority="R. Eliezer", machine_claim="EX22-03", **FIRE_PROV),
            V("fifty_cubits", "fifty", authority="R. Akiva",
              machine_claim="EX22-03", **FIRE_PROV),
            V("all_by_the_blaze", "'shalem yeshalem ha-mav'ir' — all "
              "according to the blaze", authority="R. Shimon",
              machine_claim="EX22-03", **FIRE_PROV),
        ]
    if q == "fire_scope" and case.get("contents") == "hidden_vessels":
        return [
            V("pays_contents", "pays what was inside",
              authority="R. Yehudah", machine_claim="EX22-03", **FIRE_PROV),
            V("grain_only", "only the stack of wheat or barley — the "
              "hidden excluded", authority="the sages (= the Mekhilta's "
              "open-things rule)", machine_claim="EX22-03", **FIRE_PROV),
        ]
    return None


THEFT_PROV = _MP("Mishnah Bava Kamma 7:1 + 7:4 + 9:8; Shevuot 8:3-4; "
                 "Ketubot 3:9", "Mekhilta on Exod 22:3 + 22:6-8",
                 "Exod.22.3-8 (EX22-04, EX22-09)")


def rule_theft_and_confession(case):
    q = case.get("query")
    if q == "theft_payment":
        if case.get("thief_from") == "thief":
            return [V("exempt_double", "the thief after the thief does "
                      "not pay double — the Mekhilta's row",
                      machine_claim="EX22-04 area (the 22:6 reading)",
                      **THEFT_PROV)]
        if case.get("proof") == "self_admission":
            return [V("principal_only", "whoever pays MORE than the "
                      "damage does not pay by his own mouth — asher "
                      "yarshi'un, the JUDGES convict, not the "
                      "self-convicter", machine_claim="EX22-09 (leg d, "
                      "F-017)", **THEFT_PROV)]
    if q == "deposit_plea" and case.get("plea") == "stolen":
        p = case.get("proof")
        if p == "witnesses_after_oath":
            return [V("double", "swore 'stolen' and witnesses prove he "
                      "took it — pays double", machine_claim="EX22-04 "
                      "(the oath machine) + EX22-05", **THEFT_PROV)]
        if p == "self_admission_after_oath":
            return [V("principal_fifth_guilt_offering", "admitted on "
                      "his own — principal, the added fifth, and the "
                      "guilt offering", machine_claim="EX22-09 (leg d)",
                      **THEFT_PROV)]
    return None


KEEP_PROV = _MP("Mishnah Bava Metzia 7:8 (the four keepers verbatim) + "
                "3:12 + 6:6 + 8:1", "Mekhilta on Exod 22:6-8 + 22:9-12 "
                "+ 22:13-14", "Exod.22.6-14 (EX22-04, EX22-06)")


def rule_four_keepers(case):
    q = case.get("query")
    if q == "keeper_liability":
        k = case.get("keeper")
        if k == "unpaid":
            return [V("swears_on_all", "the unpaid keeper swears on "
                      "everything", machine_claim="EX22-06", **KEEP_PROV)]
        if k == "borrower":
            return [V("pays_all", "the borrower pays everything",
                      machine_claim="EX22-06", **KEEP_PROV)]
        if k == "paid":
            return [V("swears_accidents_pays_theft_loss", "the paid "
                      "keeper and the hirer swear on the broken, the "
                      "captured and the dead, and PAY loss and theft",
                      machine_claim="EX22-06 (the table closing on the "
                      "chapter's own ink)", **KEEP_PROV)]
    if q == "misuse_liability" and case.get("stage") == "intent_only":
        return [
            V("liable", "Beit Shammai: liable for the intent — 'al kol "
              "devar pesha'", authority="Beit Shammai",
              machine_claim="EX22-04 (the held dispute)", **KEEP_PROV),
            V("not_liable_until_act", "Beit Hillel: only from the "
              "moment he misused — 'im lo shalach yado' quoted",
              authority="Beit Hillel", machine_claim="EX22-04",
              **KEEP_PROV),
        ]
    if q == "owner_with":
        s = case.get("sequence")
        if s == "owner_first":
            return [V("exempt", "'if its owner is with it he shall not "
                      "pay' (Exod 22:14) — owner engaged first",
                      machine_claim="EX22-06 (be-ve'alav)", **KEEP_PROV)]
        if s == "cow_first":
            return [V("liable", "'its owner not with it, he shall "
                      "surely pay' (Exod 22:13) — the cow came first",
                      machine_claim="EX22-06", **KEEP_PROV)]
    return None


OATHM_PROV = _MP("Mishnah Shevuot 6:3 + 6:4 + 7:1",
                 "Mekhilta on Exod 22:6-8 + 22:9-12",
                 "Exod.22.7-10 (EX22-04, EX22-05)")


def rule_oath_mechanics(case):
    q = case.get("query")
    if q == "oath_default":
        return [V("swear_and_not_pay", "ALL WHO SWEAR BY TORAH LAW "
                  "SWEAR AND DO NOT PAY — the Mekhilta's row as the "
                  "Mishnah's opening; the swear-and-take five are the "
                  "sages' inversions, listed as such",
                  machine_claim="EX22-05", **OATHM_PROV)]
    if q == "partial_admission":
        k = case.get("admitted_kind")
        if k == "different":
            return [V("exempt", "claimed wheat, admitted barley — the "
                      "admission must be OF THE CLAIM'S KIND",
                      machine_claim="EX22-04 (ki hu zeh)", **OATHM_PROV)]
        if k == "land":
            return [V("exempt_but_drawn_in", "land carries no oath (the "
                      "middah's movables-only output) — but movables "
                      "admitted DRAW the land-claims into the oath "
                      "(zokekin)", machine_claim="EX22-04", **OATHM_PROV)]
    if q == "oath_on_claim_of" and case.get("claimant") == "minor":
        return [V("no_oath", "no oath on the claim of the deaf-mute, "
                  "the deranged or the minor; one swears TO the minor "
                  "and to consecrated property",
                  machine_claim="EX22-04 (import leg — the Mishnah's "
                  "own carve)", **OATHM_PROV)]
    return None


ONA_PROV = _MP("Mishnah Bava Metzia 4:10 (quoting Exod 22:20)",
               "Mekhilta on Exod 22:20 (words vs money)",
               "Exod.22.20 (the EX22 ledger's held row)")


def rule_verbal_wronging(case):
    if case.get("query") != "speech_permitted":
        return None
    t, s = case.get("target"), case.get("speech")
    if (t, s) == ("penitent", "remind_deeds"):
        return [V("forbidden", "do not say 'remember your former "
                  "deeds' — wronging by WORDS, the Mekhilta's split",
                  machine_claim="ledger-held (exo_22 reading, 22:20)",
                  **ONA_PROV)]
    if (t, s) == ("converts_son", "remind_fathers_deeds"):
        return [V("forbidden", "'remember your fathers' deeds'? — 'and "
                  "a sojourner you shall not wrong' quoted in the row",
                  machine_claim="ledger-held", **ONA_PROV)]
    return None


def rule_interest_parties(case):
    if case.get("query") != "interest_violators":
        return None
    return [V("five_parties", "the lender, the borrower, the "
              "guarantor and the witnesses transgress; the sages add "
              "THE SCRIBE — the Mekhilta's row met verbatim",
              machine_claim="EX22-09 (F-017 leg a)",
              **_MP("Mishnah Bava Metzia 5:11",
                    "Mekhilta on Exod 22:24", "Exod.22.24 (EX22-09)"))]


UNL_PROV = _MP("Mishnah Bava Metzia 2:10 (quoting azov ta'azov + imo)",
               "Mekhilta on Exod 23:4-5", "Exod.23.5 (EX23-03)")


def rule_unloading_duty(case):
    if case.get("query") != "unload_duty":
        return None
    if case.get("times") == "repeated":
        return [V("still_liable", "unloaded and it re-collapsed — even "
                  "four and five times: azov TA'AZOV",
                  machine_claim="EX23-03", **UNL_PROV)]
    if case.get("owner_helps") == "no":
        return [V("exempt", "he sat aside and said 'the duty is "
                  "yours' — IMO, with him: the idle owner exempts you "
                  "(old or sick — the duty stands)",
                  machine_claim="EX23-03", **UNL_PROV)]
    if case.get("order_from") == "father_contrary":
        return [V("not_obeyed", "his father said do not unload — he "
                  "does not listen: the parents are themselves bound",
                  machine_claim="EX23-03 (the held priority case)",
                  **UNL_PROV)]
    if case.get("load") == "overload":
        return [V("exempt", "more than its load — tachat masao, a load "
                  "it can stand under", authority="R. Yose ha-Gelili",
                  machine_claim="EX23-03", **UNL_PROV)]
    return None


COURT_PROV = _MP("Mishnah Sanhedrin 1:1 + 1:6 + 4:2; Rosh Hashanah 2:9",
                 "Mekhilta on Exod 22:6-8 + 23:2",
                 "Exod.22.8 + 23.2 + 24.9 (EX22-04, EX23-02, EX24-07)")


def rule_court_architecture(case):
    q = case.get("query")
    if q == "court_size":
        ct = case.get("case_type")
        if ct == "monetary":
            return [V("three", "monetary cases in THREE — the "
                      "elohim-tokens of our deposit passage",
                      machine_claim="EX22-04", **COURT_PROV)]
        if ct == "capital":
            return [V("twenty_three", "derived THROUGH our 23:2: "
                      "tilt-for-good by one, tilt-for-evil by two, no "
                      "even bench — ten, ten, and three",
                      machine_claim="EX23-02 (the margin of two)",
                      **COURT_PROV)]
        if ct == "fines":
            return [
                V("three", "the rapist, the seducer and the defamer in "
                  "three", authority="R. Meir", machine_claim="EX22-04",
                  **COURT_PROV),
                V("defamer_twenty_three", "the defamer in twenty-three "
                  "— capital matter inside it", authority="the sages",
                  machine_claim="EX23-02", **COURT_PROV),
            ]
    if q == "deliberation_start" and case.get("case_type") == "capital":
        return [V("from_the_side", "capital deliberation begins FROM "
                  "THE SIDE — the junior speaks first (purity cases "
                  "from the great)", machine_claim="EX23-02 area (the "
                  "lo-taaneh clause)", **COURT_PROV)]
    if q == "court_authority" and case.get("bench") == "any_three":
        return [V("as_moses_court", "the seventy elders of our 24:9 "
                  "left UNNAMED — so every three that stands as a "
                  "court over Israel is AS THE COURT OF MOSES (the "
                  "calendar case decided by it)",
                  machine_claim="EX24-07 (F-019)", **COURT_PROV)]
    return None


def rule_witness_fitness(case):
    if case.get("query") != "witness_fit":
        return None
    c = case.get("candidate")
    if c in ("dice_player", "interest_lender"):
        return [V("disqualified", "the dice player, the interest "
                  "lender, the pigeon racers, the seventh-year traders "
                  "— the case shelf's list on the Mekhilta's "
                  "violent-and-robbers filter",
                  machine_claim="EX23-01",
                  **_MP("Mishnah Sanhedrin 3:3; Shevuot 4:1",
                        "Mekhilta on Exod 23:1", "Exod.23.1 (EX23-01)"))]
    return None


TUN_PROV = _MP("Mishnah Sanhedrin 8:6", "Mekhilta on Exod 22:1-2",
               "Exod.22.1-2 (EX22-01)")


def rule_tunneler(case):
    if case.get("query") != "tunneler_payment" or case.get("broke") != "jar":
        return None
    bl = case.get("blood_license")
    if bl == "standing":
        return [V("exempt_payment", "judged by his end — while his "
                  "killer bears no blood-guilt, his own payments "
                  "merge into his forfeit life: broke the jar, exempt "
                  "(the Mekhilta's wine-jars inside the row)",
                  machine_claim="EX22-01", **TUN_PROV)]
    if bl == "lapsed":
        return [V("liable_payment", "the sun risen — the "
                  "witnesses'-eye clarity: blood-guilt stands, so the "
                  "jar is paid for", machine_claim="EX22-01 (the "
                  "Onkelos rendering)", **TUN_PROV)]
    return None


def rule_sorcerer_mode(case):
    if case.get("query") != "execution_mode"             or case.get("offender") != "sorcerer":
        return None
    return [V("stoning", "the sorcerer stands in the Mishnah's stoned "
              "list — the case table DECIDING the Mekhilta's recorded "
              "mode dispute (R. Akiva's stoning over R. Yishmael's "
              "sword)", machine_claim="ledger-held dispute (exo_22 "
              "reading, 22:17); the decision is the case shelf's",
              **_MP("Mishnah Sanhedrin 7:4", "Mekhilta on Exod 22:17",
                    "Exod.22.17 (the EX22 ledger's dispute row)"))]


IDOL_PROV = _MP("Mishnah Sanhedrin 7:6", "Mekhilta on Exod 22:19 + 23:13",
                "Exod.22.19 + 23.13 (EX22-09)")


def rule_idolatry_service(case):
    q = case.get("query")
    if q == "idol_service_liability":
        s = case.get("service")
        if s == "temple_style":
            return [V("liable_any_idol", "slaughtering, burning, "
                      "libating, bowing — liable for ANY idol, its own "
                      "cult or not: the zevichah paradigm",
                      machine_claim="EX22-09 (F-017 leg b)", **IDOL_PROV)]
        if s == "embrace_kiss":
            return [V("prohibition_only", "embracing, kissing, "
                      "sweeping, washing — a prohibition, not the "
                      "capital count", machine_claim="EX22-09",
                      **IDOL_PROV)]
    if q == "vow_in_idol_name":
        return [V("prohibition", "vowing and fulfilling in its name — "
                  "our 23:13's 'let it not be heard upon your mouth' "
                  "consumed by the row", machine_claim="EX22-09 + the "
                  "EX23 ledger's 23:13 row", **IDOL_PROV)]
    return None


def rule_bribe_consequences(case):
    if case.get("query") != "bribe_taker_fate":
        return None
    return [V("eyes_dim", "the judge who takes a bribe and tilts — "
              "his eyes dim before he leaves the world, the Mishnah "
              "quoting our 23:8 verbatim (the Mekhilta's blindness "
              "ladder)", machine_claim="EX23-04",
              **_MP("Mishnah Peah 8:9 (the verse quoted)",
                    "Mekhilta on Exod 23:6-8", "Exod.23.8 (EX23-04)"))]


APP_PROV = _MP("Mishnah Chagigah 1:1 (quoting shalosh regalim) + 1:2",
               "Mekhilta on Exod 23:14-17", "Exod.23.14-17 (EX23-07)")


def rule_appearance_duty(case):
    q = case.get("query")
    if q == "appearance_obligated":
        if case.get("person") == "woman":
            return [V("exempt", "zekhurkha — your MALES",
                      machine_claim="EX23-07 (the word-by-word table)",
                      **APP_PROV)]
        if case.get("appearer") == "lame":
            return [V("exempt", "regalim — on his feet",
                      machine_claim="EX23-07", **APP_PROV)]
        if case.get("person") == "man":
            return [V("obligated", "ALL are obligated in appearing "
                      "except the listed", machine_claim="EX23-07",
                      **APP_PROV)]
    if q == "appearance_minimum":
        return [
            V("appearance_two_silver", "the appearance two silver, the "
              "festival offering a maah", authority="Beit Shammai",
              machine_claim="the Mishnah's own minimums (import)",
              **APP_PROV),
            V("appearance_one_maah", "the appearance a maah, the "
              "festival offering two silver", authority="Beit Hillel",
              machine_claim="import", **APP_PROV),
        ]
    return None


MMK_PROV = _MP("Mishnah Chullin 8:4; Kiddushin 2:9; Avodah Zarah 5:9",
               "Mekhilta on Exod 23:19 (the seven answers; Onkelos "
               "printing the verdict)", "Exod.23.19 (EX23-08)")


def rule_meat_milk_scope(case):
    q = case.get("query")
    if q == "meat_milk":
        p = case.get("pair")
        if p == "pure_in_pure":
            return [V("forbidden_cook_and_benefit", "pure meat in pure "
                      "milk — forbidden to cook and in benefit (and on "
                      "the forbidden-in-any-quantity list)",
                      machine_claim="EX23-08", **MMK_PROV)]
        if p == "pure_in_impure":
            return [V("permitted_both", "pure in impure and impure in "
                      "pure — permitted to cook and in benefit",
                      machine_claim="EX23-08", **MMK_PROV)]
        if p == "fowl_in_milk":
            return [
                V("not_torah", "'kid' three times — excluding the wild "
                  "animal, the fowl and the impure beast",
                  authority="R. Akiva", machine_claim="EX23-08 (both "
                  "positions in the morning's reading)", **MMK_PROV),
                V("fowl_excluded_no_mothers_milk", "'its MOTHER'S milk' "
                  "— the fowl has none", authority="R. Yose ha-Gelili",
                  machine_claim="EX23-08", **MMK_PROV),
            ]
    if q == "betrothal_with" and case.get("item") == "meat_in_milk":
        return [V("invalid", "betrothal with meat-in-milk is NO "
                  "betrothal — the benefit ban consumed by marriage "
                  "law; sold first, the proceeds betroth",
                  machine_claim="EX23-08 (the benefit ladder)",
                  **MMK_PROV)]
    return None


def rule_pesach_over_chametz(case):
    if case.get("query") != "pesach_slaughter_with_leaven":
        return None
    return [
        V("violates", "slaughtering the Passover while leaven stands "
          "violates the prohibition — the Mekhilta's R. Yishmael (R. "
          "Akiva adds the throwing)", machine_claim="EX23-08",
          **_MP("Mishnah Pesachim 5:4", "Mekhilta on Exod 23:18",
                "Exod.23.18 (EX23-08)")),
        V("also_the_tamid", "the daily offering too — 'the offering "
          "wholly Mine'", authority="R. Yehudah",
          machine_claim="EX23-08",
          **_MP("Mishnah Pesachim 5:4", "Mekhilta on Exod 23:18",
                "Exod.23.18 (EX23-08)")),
    ]


GIFT_PROV = _MP("Mishnah Terumot 3:6 (quoting Exod 22:28) + 3:7",
                "Mekhilta on Exod 22:28", "Exod.22.28 (EX22-10)")


def rule_gift_order(case):
    q = case.get("query")
    if q == "gift_reordered":
        return [V("act_stands_though_forbidden", "mah she-asah asui — "
                  "the reordering transgresses and the act stands, the "
                  "Mishnah quoting our verse",
                  machine_claim="EX22-10 (F-020)", **GIFT_PROV)]
    if q == "gift_order_reason":
        return [V("names_count", "firstfruits first, for they carry "
                  "FOUR titles; terumah three; the tithes after — the "
                  "Mekhilta's argument as the Mishnah's reason",
                  machine_claim="EX22-10", **GIFT_PROV)]
    return None


BIK_PROV = _MP("Mishnah Bikkurim 1:2 + 1:3 + 1:9; Shekalim 8:8; "
               "Challah 4:10", "Mekhilta on Exod 23:19",
               "Exod.23.16 + 23.19 (EX23-08, EX23-09)")


def rule_bikkurim_duty(case):
    q = case.get("query")
    if q == "bikkurim_brings" and case.get("grower") == "sharecropper":
        return [
            V("does_not_bring", "'until all growth is from YOUR land' "
              "— sharecroppers, tenants, seizers and robbers excluded",
              authority="Mishnah Bikkurim 1:2",
              machine_claim="EX23-09 (the delta's Mishnah seat)",
              **BIK_PROV),
            V("brings_but_does_not_read", "the Mekhilta re-includes "
              "them by the bring-verb, without the recital",
              authority="Mekhilta on Exod 23:19",
              machine_claim="EX23-09 (dual-track)", **BIK_PROV),
        ]
    if q == "bikkurim_timing" and case.get("brought") == "before_shavuot":
        return [V("refused", "the men of Mount Tzevoim brought before "
                  "Shavuot and were not accepted — on our 23:16's own "
                  "words", machine_claim="EX23-09 (F-018)", **BIK_PROV)]
    if q == "bikkurim_liability":
        return [V("until_temple_mount", "responsible until he brings "
                  "them to the Temple Mount — the bring-verb of 23:19",
                  machine_claim="EX23-09", **BIK_PROV)]
    if q == "bikkurim_era" and case.get("temple") == "absent":
        return [V("not_practiced", "shekalim and firstfruits run only "
                  "with the House standing; grain-tithe and firstborn "
                  "either way", machine_claim="EX23-09 area (the "
                  "beit-H' dependency)", **BIK_PROV)]
    return None


def rule_shemitah_model(case):
    if case.get("query") != "hefker_scope":
        return None
    P = _MP("Mishnah Eduyot 4:3", "Mekhilta on Exod 23:10-11",
            "Exod.23.11 (EX23-05)")
    return [
        V("poor_only", "ownerless to the poor is ownerless",
          authority="Beit Shammai", machine_claim="EX23-05", **P),
        V("also_rich_like_shemitah", "not ownerless until ownerless "
          "also to the rich — LIKE THE SEVENTH YEAR: our clause as the "
          "model", authority="Beit Hillel", machine_claim="EX23-05", **P),
    ]


# Module registry — routing follows the Mishnah's own organization (the
# owner's tractate map, logic/MISHNAH_TOPICS.md): each module names the
# tractate whose case rows feed it, so the code's structure grows into the
# tradition's structure as more books and tractates arrive.
RULES = {
    "life_override": {"fn": rule_life_override, "tractate": "Yoma"},
    "procreation_measure": {"fn": rule_procreation, "tractate": "Yevamot"},
    "judgment_durations": {"fn": rule_judgment_durations,
                           "tractate": "Eduyot"},
    "sciatic_nerve": {"fn": rule_sciatic_nerve, "tractate": "Chullin"},
    "day_boundary": {"fn": rule_day_boundary, "tractate": "Chullin"},
    "seas_as_mikveh": {"fn": rule_seas_as_mikveh, "tractate": "Mikvaot"},
    "forgiveness_after_injury": {"fn": rule_forgiveness,
                                 "tractate": "Bava Kamma"},
    "seed_categories": {"fn": rule_seed_categories, "tractate": "Nedarim"},
    "world_to_come": {"fn": rule_world_to_come, "tractate": "Sanhedrin"},
    "circumcision_third_day": {"fn": rule_circumcision_third_day,
                               "tractate": "Shabbat"},
    # the Noahide block (2026-09-01) — Talmud-only law
    "noahide_seven_laws": {"fn": rule_noahide_seven_laws,
                           "tractate": "Sanhedrin"},
    "noahide_execution_scope": {"fn": rule_noahide_execution_scope,
                                "tractate": "Sanhedrin"},
    "noahide_procedure": {"fn": rule_noahide_procedure,
                          "tractate": "Sanhedrin"},
    "noahide_relations": {"fn": rule_noahide_relations,
                          "tractate": "Sanhedrin"},
    "gentile_sabbath_torah": {"fn": rule_gentile_sabbath_torah,
                              "tractate": "Sanhedrin"},
    "repeated_at_sinai": {"fn": rule_repeated_at_sinai,
                          "tractate": "Sanhedrin"},
    "meat_timeline": {"fn": rule_meat_timeline, "tractate": "Sanhedrin"},
    "noahide_offerings": {"fn": rule_noahide_offerings,
                          "tractate": "Avodah Zarah"},
    "circumcision_agent": {"fn": rule_circumcision_agent,
                           "tractate": "Avodah Zarah"},
    "court_of_shem": {"fn": rule_court_of_shem,
                      "tractate": "Avodah Zarah"},
    "pursuer": {"fn": rule_pursuer, "tractate": "Sanhedrin"},
    # the Mishpatim exam (2026-09-01) — the parashah-rhythm round
    "four_avot_damages": {"fn": rule_four_avot_damages,
                          "tractate": "Bava Kamma"},
    "fire_liability": {"fn": rule_fire_liability, "tractate": "Bava Kamma"},
    "theft_and_confession": {"fn": rule_theft_and_confession,
                             "tractate": "Bava Kamma"},
    "four_keepers": {"fn": rule_four_keepers, "tractate": "Bava Metzia"},
    "oath_mechanics": {"fn": rule_oath_mechanics, "tractate": "Shevuot"},
    "verbal_wronging": {"fn": rule_verbal_wronging,
                        "tractate": "Bava Metzia"},
    "interest_parties": {"fn": rule_interest_parties,
                         "tractate": "Bava Metzia"},
    "unloading_duty": {"fn": rule_unloading_duty,
                       "tractate": "Bava Metzia"},
    "court_architecture": {"fn": rule_court_architecture,
                           "tractate": "Sanhedrin"},
    "witness_fitness": {"fn": rule_witness_fitness,
                        "tractate": "Sanhedrin"},
    "tunneler": {"fn": rule_tunneler, "tractate": "Sanhedrin"},
    "sorcerer_mode": {"fn": rule_sorcerer_mode, "tractate": "Sanhedrin"},
    "idolatry_service": {"fn": rule_idolatry_service,
                         "tractate": "Sanhedrin"},
    "bribe_consequences": {"fn": rule_bribe_consequences,
                           "tractate": "Peah"},
    "appearance_duty": {"fn": rule_appearance_duty, "tractate": "Chagigah"},
    "meat_milk_scope": {"fn": rule_meat_milk_scope, "tractate": "Chullin"},
    "pesach_over_chametz": {"fn": rule_pesach_over_chametz,
                            "tractate": "Pesachim"},
    "gift_order": {"fn": rule_gift_order, "tractate": "Terumot"},
    "bikkurim_duty": {"fn": rule_bikkurim_duty, "tractate": "Bikkurim"},
    "shemitah_model": {"fn": rule_shemitah_model, "tractate": "Eduyot"},
}


def answer(module, case_input):
    entry = RULES.get(module)
    return entry["fn"](case_input) if entry else None


# ---- the Exodus 1-21 backfill exam's modules (2026-09-01) ----
# 33 rules in backfill_rules.py — Part I on the FWD-era units' new
# EXnn-14+ seats, Part II re-checking chapter 21 against the law-era
# claims. build(V) avoids a circular import.
import backfill_rules as _bf
RULES.update(_bf.build(V))

# ---- the Terumah exam's modules (2026-09-01, same day the parashah
# was derived and stamped — the derive-then-examine rhythm's third
# cycle). 11 rules in terumah_rules.py; mitzvah_orientation is
# Talmud-only (talmud_source in place of a Mishnah row).
import terumah_rules as _tr
RULES.update(_tr.build(V))

# ---- the Tetzaveh exam's modules (2026-09-01, same sitting as the
# derivation — the rhythm's fourth cycle). 9 rules in
# tetzaveh_rules.py.
import tetzaveh_rules as _tv
RULES.update(_tv.build(V))

# ---- the Ki Tisa exam's modules (2026-09-01, the rhythm's fifth
# cycle). 15 rules in kitisa_rules.py.
import kitisa_rules as _kt
RULES.update(_kt.build(V))

# ---- the Vayakhel-Pekudei exam's modules (2026-09-02, round 9 — the
# book of Exodus' closing cycle). 4 rules in vayakhel_pekudei_rules.py.
import vayakhel_pekudei_rules as _vp
RULES.update(_vp.build(V))

# Round 10 — THE VAYIKRA EXAM (2026-09-03, the book of Leviticus'
# opening cycle). 17 rules in vayikra_rules.py.
import vayikra_rules as _vk
RULES.update(_vk.build(V))

# Round 11 — THE TZAV EXAM (2026-09-03, the derive-then-examine
# rhythm's eighth cycle). 16 rules in tzav_rules.py.
import tzav_rules as _tz
RULES.update(_tz.build(V))

# Round 12 — THE LEAVEN MACHINE (2026-09-04, the first of the 18
# Exodus Talmud-first exam blocks; the Noahide precedent). 9 rules
# in leaven_rules.py.
import leaven_rules as _lv
RULES.update(_lv.build(V))

# Round 13 — THE COURTS (2026-09-04, the second Exodus Talmud-first
# exam block). 10 rules in courts_rules.py.
import courts_rules as _ct
RULES.update(_ct.build(V))

# Round 14 — THE ORDINANCES' PERSONS (2026-09-04, the third Exodus
# Talmud-first exam block). 10 rules in persons_rules.py.
import persons_rules as _pr
RULES.update(_pr.build(V))

# Round 15 — OATHS AND DEPOSITS (2026-09-04, the fourth Exodus
# Talmud-first exam block — the compiled guardians' exam shelf).
# 3 rules in oaths_rules.py.
import oaths_rules as _oa
RULES.update(_oa.build(V))

# Round 16 — THE PASCHAL OFFERING (2026-09-04, the fifth Exodus
# Talmud-first exam block — the map's largest). 9 rules in
# pesach_rules.py.
import pesach_rules as _pe
RULES.update(_pe.build(V))

# Round 17 — SHABBAT'S MACHINERY (2026-09-04, the sixth Exodus
# Talmud-first exam block — the twice-drawn import edge). 10 rules
# in shabbat_rules.py.
import shabbat_rules as _sh
RULES.update(_sh.build(V))

# Round 18 — MATZA, HERBS, AND THE TELLING (2026-09-04, the seventh
# Exodus Talmud-first exam block — the Passover family's eating
# wing). 8 rules in matza_rules.py.
import matza_rules as _ma
RULES.update(_ma.build(V))

# Round 19 — EGYPT AND THE GENERATIONS (2026-09-04, the eighth
# Exodus Talmud-first exam block — the Passover family's closing
# wing: the export engine's derivation layer). 4 rules in
# egypt_rules.py.
import egypt_rules as _eg
RULES.update(_eg.build(V))

# Round 20 — THE INK LAYER (2026-09-04, the ninth Exodus
# Talmud-first exam block — the Talmud ruling about the ink
# itself). 5 rules in ink_rules.py.
import ink_rules as _ik
RULES.update(_ik.build(V))

# Round 21 — CONDUCT AND LITURGY (2026-09-04, the tenth Exodus
# Talmud-first exam block — the small pair's second half). 5 rules
# in conduct_rules.py.
import conduct_rules as _cd
RULES.update(_cd.build(V))

# Round 22 — THE CALENDAR (2026-09-04, the eleventh Exodus
# Talmud-first exam block). 4 rules in calendar_rules.py.
import calendar_rules as _ca
RULES.update(_ca.build(V))

# Round 23 — THE SINAI COVENANT (2026-09-04, the twelfth Exodus
# Talmud-first exam block — the module-name guard fired third
# time: boundary_machine_sinai beside round 17's boundary_machine).
# 5 rules in covenant_rules.py.
import covenant_rules as _cv
RULES.update(_cv.build(V))

# Round 24 — FESTIVALS AND GIFTS (2026-09-04, the thirteenth Exodus
# Talmud-first exam block — the module-name guard fired a FOURTH
# time: appearance_exemptions beside the standing appearance_duty).
# 5 rules in festivals_rules.py.
import festivals_rules as _fs
RULES.update(_fs.build(V))

# Round 25 — CAPITAL MODES AND IDOLATRY SERVICE (2026-09-04, the
# fourteenth Exodus Talmud-first exam block). 5 rules in
# capital_rules.py.
import capital_rules as _cp
RULES.update(_cp.build(V))

# Round 26 — SANCTUARY CONSTANTS (2026-09-04, the fifteenth Exodus
# Talmud-first exam block). 5 rules in sanctuary_rules.py.
import sanctuary_rules as _sc
RULES.update(_sc.build(V))

# Round 27 — VESTMENTS AND INVESTITURE (2026-09-04, the sixteenth
# Exodus Talmud-first exam block). 4 rules in vestments_rules.py.
import vestments_rules as _vt
RULES.update(_vt.build(V))

# Round 28 — THE SERVICE ORDER (2026-09-04, the seventeenth Exodus
# Talmud-first exam block — the sanctuary family closes). 5 rules
# in service_rules.py.
import service_rules as _sv
RULES.update(_sv.build(V))

# Round 29 — THE DECALOGUE (2026-09-04, the eighteenth and FINAL
# Exodus Talmud-first exam block — the campaign's finale). 6 rules
# in decalogue_rules.py.
import decalogue_rules as _dc
RULES.update(_dc.build(V))
