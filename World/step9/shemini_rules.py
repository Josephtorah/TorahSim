# shemini_rules.py — round 42, THE SHEMINI EXAM (2026-09-05).
# Bare Mishnah rows citing Lev 9-11, graded after the derivation.
# Read-source: logic/oral_triage/shemini_exam_mishnah_2026-09-05.md.


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    BP = _EX("Mishnah Sotah 7:6; Tamid 7:2; Menachot 5:6",
             "Lev 9:22 (lev_09, LV09-08 — the transposed blessing)")
    ON = _EX("Mishnah Horayot 3:5; Pesachim 8:8",
             "Lev 10:19 (lev_10, LV10-10 — the goat inquiry's onen "
             "machine; Pesachim 8:8 is the seat's own cited proof)")
    WF = _EX("Mishnah Nazir 6:1; Sanhedrin 7:2",
             "Lev 10:9 + 10:6 (lev_10, LV10-07 wine / LV10-05 the "
             "burning export)")
    SP = _EX("Mishnah Niddah 6:9; Bikkurim 2:11; Berakhot 6:3; "
             "Shabbat 14:1; Makkot 3:2; Shabbat 6:10",
             "Lev 11:3-29 (lev_11_animals, LV11A-02/07/09; "
             "lev_11_carcass, LV11B-03)")
    PU = _EX("Mishnah Chullin 9:5; Sotah 5:2; Eduyot 6:3; 7:8; "
             "Eruvin 10:15; Pesachim 1:6",
             "Lev 11:24-39 (lev_11_carcass, LV11B-01/05/06/12)")
    HK = _EX("Mishnah Makhshirin 1:3; Eduyot 4:6",
             "Lev 11:38 (lev_11_carcass, LV11B-08 — the hekhsher "
             "machine)")

    def rule_blessing_palms(case):
        q = case.get("query")
        if q == "blessing_regime_table":
            return [V("temple_one_name_as_written",
                      "the regime table: in the PROVINCE three "
                      "blessings, in the TEMPLE one; the Name AS "
                      "WRITTEN inside, by epithet outside; hands to "
                      "the shoulders outside, above the heads inside "
                      "— except the high priest, not above the "
                      "frontplate (R. Yehuda: even he raises) — on "
                      "וישא אהרן את ידיו ('and Aaron LIFTED his "
                      "hands,' Lev 9:22) — Mishnah Sotah 7:6",
                      authority="the Mishnah with R. Yehuda's arm",
                      machine_claim="LV09-08", **BP)]
        if q == "temple_service_blessing":
            return [V("one_blessing_on_the_steps",
                      "the daily service runs it: the priests on the "
                      "porch steps, five vessels in hand, bless the "
                      "people ONE blessing — the Temple regime "
                      "inside the tamid's own narrative — Mishnah "
                      "Tamid 7:2",
                      authority="the Mishnah",
                      machine_claim="LV09-08", **BP)]
        if q == "wave_required_list":
            return [V("waved_not_presented",
                      "the list requiring WAVING without "
                      "presentation (the leper's log and asham, the "
                      "firstfruits per R. Eliezer b. Yaakov, the "
                      "individual's peace-offering portions, the two "
                      "loaves and lambs) with the two-hands-beneath "
                      "choreography — the lifted-lifting family the "
                      "Onkelos policy tracks — Mishnah Menachot 5:6",
                      authority="the Mishnah",
                      machine_claim="LV09-08 (the lifting family)", **BP)]
        return None

    def rule_onen_file(case):
        q = case.get("query")
        if q == "onen_priest_split":
            return [V("hp_offers_not_eats",
                      "the HIGH PRIEST offers as an acute mourner "
                      "and does NOT eat; the commoner neither "
                      "offers nor eats — the Lev 10:19 machine run "
                      "generationally — Mishnah Horayot 3:5",
                      authority="the Mishnah",
                      machine_claim="LV10-10", **ON)]
        if q == "onen_pesach_evening":
            return [V("immerses_eats_pesach_at_evening",
                      "the acute mourner IMMERSES AND EATS HIS "
                      "PESACH AT EVENING — but not other holies: "
                      "the very proof Rabbi cited for the scribal "
                      "night ban, standing in the seat since the "
                      "derivation — Mishnah Pesachim 8:8",
                      authority="the Mishnah (Rabbi's cited proof)",
                      machine_claim="LV10-10", **ON)]
        return None

    def rule_wine_and_fire(case):
        q = case.get("query")
        if q == "nazir_wine_measure":
            return [V("quarter_log_attested_again",
                      "the nazirite's first-Mishnah measure: liable "
                      "עד שישתה רביעית יין ('until he drinks a "
                      "QUARTER-LOG of wine') — the same rebiit the "
                      "priests' wine ban carries: the data value "
                      "attested at a second machine — Mishnah "
                      "Nazir 6:1",
                      authority="the first Mishnah (R. Akiva's "
                                "joining arm beside)",
                      machine_claim="LV10-07", **WF)]
        if q == "burning_execution_mode":
            return [V("soul_burned_body_intact",
                      "execution by burning: the lit wick into the "
                      "mouth, burning the entrails — THE SOUL "
                      "BURNED AND THE BODY INTACT: the Miluim "
                      "burning analogy running as court procedure "
                      "(R. Yehuda's dissent kept) — Mishnah "
                      "Sanhedrin 7:2",
                      authority="the Mishnah with R. Yehuda's arm",
                      machine_claim="LV10-05", **WF)]
        return None

    def rule_species_file(case):
        q = case.get("query")
        if q == "sign_correlations":
            return [V("scale_implies_fin",
                      "whatever has a SCALE has a FIN (fin-havers "
                      "without scales exist); whatever has HORNS "
                      "has HOOVES — the correlation engineering "
                      "behind the one-sign shortcut — Mishnah "
                      "Niddah 6:9",
                      authority="the Mishnah",
                      machine_claim="LV11A-07", **SP)]
        if q == "koy_class":
            return [V("slaughter_and_impurity_like_both",
                      "THE KOY: split from both classes where they "
                      "split, equal to BOTH where they share — "
                      "requires slaughter like either, contaminates "
                      "as carcass and as limb-from-the-living like "
                      "either — the hybrid running the "
                      "class-inclusion machine — Mishnah Bikkurim "
                      "2:11",
                      authority="the Mishnah",
                      machine_claim="LV11A-02", **SP)]
        if q == "locust_blessing":
            return [V("shehakol_with_curse_arm",
                      "the pure locust BLESSED shehakol; R. "
                      "Yehuda's arm — no blessing on a curse-kind "
                      "(the dispute kept) — Mishnah Berakhot 6:3",
                      authority="the Mishnah with R. Yehuda's arm",
                      machine_claim="LV11A-09", **SP)]
        if q == "eight_have_hides":
            return [V("wounder_liable_on_eight",
                      "the EIGHT swarmers said in the Torah — the "
                      "trapper and the WOUNDER liable on Shabbat (a "
                      "bruise needs a hide to pool under); other "
                      "swarmers, the wounder exempt — the skins "
                      "dispute's practical shadow — Mishnah "
                      "Shabbat 14:1",
                      authority="the Mishnah",
                      machine_claim="LV11B-03", **SP)]
        if q == "dietary_lash_layer":
            return [V("lashes_for_the_bans",
                      "the flogging list carries the eaters of "
                      "carcasses, terefot, detestables and swarmers "
                      "— the dietary bans' lash layer enumerated — "
                      "Mishnah Makkot 3:2",
                      authority="the Mishnah",
                      machine_claim="LV11A-05 (the ban layer)", **SP)]
        if q == "chargol_egg_cure":
            return [V("cure_dispute_recorded",
                      "the CHARGOL'S EGG carried as a cure — R. "
                      "Meir permits going out with it; the sages "
                      "forbid even on a weekday as the ways of the "
                      "Amorite — the named locust species in folk "
                      "practice, the dispute recorded — Mishnah "
                      "Shabbat 6:10",
                      authority="R. Meir against the sages",
                      machine_claim="LV11A-09", **SP)]
        return None

    def rule_purity_file(case):
        q = case.get("query")
        if q == "thigh_bone_grid":
            return [V("sealed_pure_pierced_impure",
                      "the grid: the dead's and the consecrated's "
                      "thigh-bone — impure sealed or pierced; the "
                      "carcass's and the swarmer's — SEALED PURE, "
                      "pierced any-amount impure; and the gate "
                      "rule: what comes to the class of TOUCH comes "
                      "to the class of CARRY — Mishnah Chullin 9:5",
                      authority="the Mishnah",
                      machine_claim="LV11B-12", **PU)]
        if q == "third_loaf_yitma":
            return [V("second_renders_third",
                      "THE SEAT ANSWERS: R. Akiva reads יטמא "
                      "('SHALL RENDER impure') — the second loaf "
                      "contaminates the THIRD; R. Yehoshua's "
                      "dust-from-your-eyes over R. Yochanan b. "
                      "Zakkai — the same teaching, same "
                      "exclamation, seated at LV11B-06 from the "
                      "Sifra before this row was opened — Mishnah "
                      "Sotah 5:2",
                      authority="R. Akiva",
                      machine_claim="LV11B-06", **PU)]
        if q == "separated_piece_disputes":
            return [V("three_cornered_dispute",
                      "an olive of FLESH parting from the living "
                      "limb — R. Eliezer contaminates (the limb "
                      "like a whole corpse), R. Yehoshua and R. "
                      "Nechunya purify; a barley-corn of BONE — R. "
                      "Nechunya contaminates, the others purify: "
                      "each arm's reasoning recorded over the "
                      "flesh-parting-is-pure row — Mishnah "
                      "Eduyot 6:3",
                      authority="the three-cornered dispute",
                      machine_claim="LV11B-01", **PU)]
        if q == "cauldron_rim_testimony":
            return [V("olive_cookers_impure_dyers_pure",
                      "Menachem b. Signai's TESTIMONY: the "
                      "olive-cookers' cauldron rim-addition impure, "
                      "the dyers' pure — 'they used to say the "
                      "reverse': the work-test at a named testimony "
                      "— Mishnah Eduyot 7:8",
                      authority="Menachem b. Signai's testimony",
                      machine_claim="LV11B-05", **PU)]
        if q == "temple_swarmer_removal":
            return [V("belt_or_tongs_dispute",
                      "a swarmer found in the TEMPLE: removed with "
                      "the belt (not delaying the impurity — R. "
                      "Yochanan b. Beroka) or wooden tongs (not "
                      "multiplying it — R. Yehuda); from where — "
                      "the sanctuary and porch (ben Nanas) or "
                      "wherever karet applies (R. Akiva) — Mishnah "
                      "Eruvin 10:15",
                      authority="the recorded dispute pairs",
                      machine_claim="LV11B-03", **PU)]
        if q == "adding_impurity_practice":
            return [V("never_refrained_from_adding",
                      "R. Chanina the deputy's practice row: the "
                      "priests never refrained from burning "
                      "offspring-impure flesh WITH father-impure "
                      "flesh — adding impurity to impurity "
                      "lawfully; R. Akiva's oil-lamp addition — "
                      "Mishnah Pesachim 1:6",
                      authority="R. Chanina the deputy of the "
                                "priests; R. Akiva's addition",
                      machine_claim="LV11B-06 (the grades layer)", **PU)]
        return None

    def rule_hekhsher_file(case):
        q = case.get("query")
        if q == "intent_gate_mishnah":
            return [V("until_intends_and_gives",
                      "the intent gate at its Mishnah seat: the "
                      "tree-shaker's fall splits the houses on "
                      "the when-it-is-given clause; R. Yehoshua in Abba Yosei's name: "
                      "'WONDER TO YOURSELF if any liquid "
                      "contaminates in the Torah until one INTENDS "
                      "and gives' — וכי יתן מים על זרע ('when water "
                      "IS PUT on seed,' Lev 11:38) — Mishnah "
                      "Makhshirin 1:3",
                      authority="R. Yehoshua in Abba Yosei's name",
                      machine_claim="LV11B-08", **HK)]
        if q == "olive_jar_piercing":
            return [V("hillel_pierce_with_concession",
                      "the pickled-olives jar: Bet Shammai — no "
                      "piercing needed; Bet Hillel — PIERCE it (the "
                      "brine unwanted); both conceding a "
                      "pierced-and-resealed jar is pure — the "
                      "intent machine at a houses dispute — "
                      "Mishnah Eduyot 4:6",
                      authority="the houses with the concession",
                      machine_claim="LV11B-08", **HK)]
        return None

    return {
        "blessing_palms": {"fn": rule_blessing_palms,
                           "tractate": "Sotah"},
        "onen_file": {"fn": rule_onen_file, "tractate": "Horayot"},
        "wine_and_fire": {"fn": rule_wine_and_fire,
                          "tractate": "Nazir"},
        "species_file": {"fn": rule_species_file,
                         "tractate": "Niddah"},
        "purity_file": {"fn": rule_purity_file,
                        "tractate": "Chullin"},
        "hekhsher_file": {"fn": rule_hekhsher_file,
                          "tractate": "Makhshirin"},
    }
