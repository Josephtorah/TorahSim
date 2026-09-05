# tazria_rules.py — round 43, THE TAZRIA-METZORA EXAM (2026-09-05).
# Bare Mishnah rows citing Lev 12-15, graded after the derivation.
# Read-source: logic/oral_triage/tazria_exam_mishnah_2026-09-05.md.


def build(V):
    def _EX(mishnah, anchor, **extra):
        d = dict(talmud_source=mishnah, exodus_anchor=anchor)
        d.update(extra)
        return d

    YO = _EX("Mishnah Keritot 1:6; 2:3; 6:9; Eduyot 4:10; 5:1; "
             "Niddah 3:2; 5:1; Makkot 3:2; Nedarim 4:3",
             "Lev 12:2-8 (lev_12, LV12-03/05/06 — the childbirth "
             "machine)")
    MI = _EX("Mishnah Shabbat 19:3; 19:5; Megillah 2:4; Nedarim 3:11",
             "Lev 12:3 (lev_12, LV12-04 — the override at its source)")
    NG = _EX("Mishnah Negaim 2:3; 10:2; Shevuot 1:1; Eduyot 5:6; "
             "Moed Katan 1:5; Nazir 8:2; 9:4; Megillah 1:7",
             "Lev 13 (lev_13 units, L13-05/06 + LV13A/C claims)")
    MR = _EX("Mishnah Negaim 14:2; 14:10; Menachot 3:6; 5:6; 5:7; "
             "9:3; Zevachim 5:5; Arakhin 4:2; Keritot 2:3; Sotah "
             "1:5; Moed Katan 3:1; Nazir 6:6; 7:3; Avodah Zarah "
             "5:9; Megillah 2:5",
             "Lev 14:2-32 (lev_14_metzora_cleanse, LV14A claims)")
    HO = _EX("Mishnah Negaim 12:5; 12:6; 12:7",
             "Lev 14:33-45 (lev_14_house_nega, LV14B claims)")
    ZA = _EX("Mishnah Niddah 5:1; 8:3; Eduyot 1:11; 5:1; 6:2; "
             "Beitzah 2:10; Chagigah 2:7; Horayot 1:3; Shabbat 9:1; "
             "9:3; Megillah 2:4",
             "Lev 15 (lev_15 units, LV15A/B claims)")

    def rule_yoledet_file(case):
        q = case.get("query")
        if q == "eve_of_eighty_one":
            return [V("shammai_exempt",
                      "the eve-of-81 miscarriage: Beth Shammai exempt "
                      "from the offering (the night unfit to bring)",
                      authority="Beth Shammai — Mishnah Keritot 1:6",
                      machine_claim="LV12-06", **YO),
                    V("hillel_liable",
                      "Beth Hillel liable — 'or for a daughter' "
                      "includes her; the Shabbat-day-81 proof; the "
                      "same exchange the Sifra carries at the seat",
                      authority="Beth Hillel — Mishnah Keritot 1:6",
                      machine_claim="LV12-06", **YO)]
        if q == "eve81_in_leniency_list":
            return [V("listed_shammai_leniency",
                      "the same case standing in Eduyot's list of "
                      "Beth Shammai's leniencies and Beth Hillel's "
                      "stringencies — the dispute's registry row",
                      authority="Mishnah Eduyot 4:10",
                      machine_claim="LV12-06", **YO)]
        if q == "one_offering_many_births":
            return [V("one_per_term",
                      "many births or marks within one term — ONE "
                      "offering ('a leper who was marked with many "
                      "marks'); the Sifra's zot-torat-hayoledet row "
                      "with the gold-dinar market story at the seat",
                      authority="Mishnah Keritot 2:3",
                      machine_claim="LV12-05", **YO)]
        if q == "dove_or_turtledove_rank":
            return [V("both_equal",
                      "'a young pigeon OR a turtledove' (Lev 12:6) — "
                      "the written order swaps across verses to teach "
                      "THE TWO ARE EQUAL — the Mishnah cites the "
                      "childbirth verse itself",
                      authority="Mishnah Keritot 6:9",
                      machine_claim="LV12-06", **YO)]
        if q == "miscarried_forms_grid":
            return [V("human_form_decides",
                      "the miscarried-forms grid: scale/hair/dust — "
                      "the water test; fish and swarm forms — with "
                      "blood impure; beast and bird forms — R. Meir "
                      "sits for both; the sages' rule: WHATEVER LACKS "
                      "HUMAN FORM IS NO CHILD — the Sifra's zachar "
                      "predicate at its Mishnah seat",
                      authority="the sages — Mishnah Niddah 3:2",
                      machine_claim="LV12-03", **YO)]
        if q == "caesarean_status":
            return [V("not_a_birth",
                      "the caesarean: no impure days, no pure days, "
                      "no offering — the Sifra's seeding-place "
                      "exclusion ruling",
                      authority="the sages — Mishnah Niddah 5:1",
                      machine_claim="LV12-03", **YO),
                    V("r_shimon_as_born",
                      "R. Shimon: it is as born — the dissent the "
                      "Sifra records at the same clause",
                      authority="R. Shimon — Mishnah Niddah 5:1",
                      machine_claim="LV12-03", **YO)]
        if q == "impure_ate_holy_lash":
            return [V("in_the_lash_list",
                      "the impure who ate holy food stands in the "
                      "flogging list — the touch-ban's lash layer "
                      "riding the childbirth clause 'no holy thing "
                      "shall she touch' (Lev 12:4)",
                      authority="Mishnah Makkot 3:2",
                      machine_claim="LV12-03", **YO)]
        if q == "benefactor_brings_kinim":
            return [V("birds_not_his_benefit",
                      "one forbidden by vow to benefit another may "
                      "still offer FOR him the bird-pairs of zavim, "
                      "zavot, and BIRTHING MOTHERS — the offering is "
                      "not the offerer's benefit",
                      authority="Mishnah Nedarim 4:3",
                      machine_claim="LV12-06", **YO)]
        if q == "leper_purity_blood":
            return [V("shammai_pure",
                      "the leprous woman's purity-blood: Beth "
                      "Shammai purify",
                      authority="Beth Shammai — Mishnah Eduyot 5:1",
                      machine_claim="LV12-05", **YO),
                    V("hillel_like_her_spittle",
                      "Beth Hillel: like her spittle and her urine — "
                      "the severe-liquids family",
                      authority="Beth Hillel — Mishnah Eduyot 5:1",
                      machine_claim="LV15A-02", **YO)]
        return []

    def rule_milah_shabbat_file(case):
        q = case.get("query")
        if q == "doubtful_androgynous_shabbat":
            return [V("no_override_r_yehuda_permits",
                      "the doubtful and the androgynous do NOT "
                      "override Shabbat (R. Yehuda permits the "
                      "androgynous) — the Sifra's certain-not-"
                      "doubtful row at its Mishnah seat",
                      authority="Mishnah Shabbat 19:3 with R. Yehuda",
                      machine_claim="LV12-04", **MI),
                    ]
        if q == "milah_day_table":
            return [V("eight_to_twelve_only",
                      "circumcised at eight, nine, ten, eleven, "
                      "twelve — never fewer nor more: twilight-born "
                      "ninth; eve-of-Shabbat twilight tenth; festival "
                      "after Shabbat eleventh; the two new-year days "
                      "twelfth; a sick child waits till he heals",
                      authority="Mishnah Shabbat 19:5",
                      machine_claim="LV12-04", **MI)]
        if q == "milah_daylight_gate":
            return [V("sunrise_proper_dawn_valid",
                      "no circumcising, immersing, sprinkling — and "
                      "the day-watcher does not immerse — until "
                      "SUNRISE; done from dawn, valid: the by-day "
                      "family's hour gate",
                      authority="Mishnah Megillah 2:4",
                      machine_claim="LV12-04", **MI)]
        if q == "foreskin_name_scope":
            return [V("named_for_the_nations",
                      "'foreskinned' in vows means the nations — "
                      "'for all the nations are foreskinned' (Jer "
                      "9:25): the vow lexicon on the milah clause",
                      authority="Mishnah Nedarim 3:11",
                      machine_claim="LV12-04", **MI)]
        return []

    def rule_negaim_exam_file(case):
        q = case.get("query")
        if q == "marks_two_that_are_four":
            return [V("national_two_by_two",
                      "'the appearances of marks: two that are four' "
                      "— standing in the national two-by-two list "
                      "with oaths, impurity-knowings, and Shabbat "
                      "carryings: the shade table as a charter row",
                      authority="Mishnah Shevuot 1:1",
                      machine_claim="L13-06", **NG)]
        if q == "dim_priest_dark_house":
            return [V("neither_examines",
                      "the priest blind in one eye or dim of sight "
                      "shall not examine ('to all the appearance of "
                      "the priest's EYES'); and THE DARK HOUSE — no "
                      "windows are opened to see its mark: both "
                      "halves of the calibration carve in one row",
                      authority="Mishnah Negaim 2:3",
                      machine_claim="L13-06", **NG)]
        if q == "yellow_hair_turned_dispute":
            return [V("r_yehuda_even_unturned",
                      "R. Yehuda: wherever 'turned' is needed the "
                      "verse says turned — the scall says 'WAS' — "
                      "yellow defiles even unturned",
                      authority="R. Yehuda — Mishnah Negaim 10:2",
                      machine_claim="LV13C-02", **NG),
                    V("r_shimon_turned_only",
                      "R. Shimon: turned only — the white-hair "
                      "a-fortiori (a hair no other hair rescues "
                      "defiles only turned...)",
                      authority="R. Shimon — Mishnah Negaim 10:2",
                      machine_claim="LV13C-02", **NG)]
        if q == "akavya_four_things":
            return [V("returning_hair_defiled_refused_office",
                      "Akavya's four things — the RETURNING HAIR "
                      "(shear pekidah) he defiled and the sages "
                      "purify — and his refusal: 'better be called a "
                      "fool all my days than be wicked one hour "
                      "before the Place'; the dispute the Sifra "
                      "carries at the raw-flesh seat",
                      authority="Mishnah Eduyot 5:6",
                      machine_claim="LV13A-02", **NG)]
        if q == "festival_mark_exam":
            return [V("r_meir_lenient_only",
                      "R. Meir: examine marks on the festival TO BE "
                      "LENIENT, never to be stringent",
                      authority="R. Meir — Mishnah Moed Katan 1:5",
                      machine_claim="LV13A-03", **NG),
                    V("sages_neither",
                      "the sages: neither lenient nor stringent — "
                      "the grace-days family's festival face",
                      authority="the sages — Mishnah Moed Katan 1:5",
                      machine_claim="LV13A-03", **NG)]
        if q == "doubtful_mark_nazirite":
            return [V("certain_overrides_doubt_not",
                      "the mark's shave overrides the nazirite's "
                      "razor-ban when CERTAIN, not when doubtful — "
                      "with the 60/120-day computation riding it: "
                      "the Sifra's gauge-rule rider at its Mishnah "
                      "seat",
                      authority="Mishnah Nazir 8:2",
                      machine_claim="LV13C-03", **NG)]
        if q == "seven_ways_zav_exam":
            return [V("before_threshold_only",
                      "'in seven ways they examine the zav before he "
                      "is bound to the flow: food, drink, burden, "
                      "jumping, illness, sight, thought' — after it, "
                      "no examination: his coerced, doubtful, and "
                      "semen impure, 'the matter has legs' — the "
                      "seat's row VERBATIM; and mark-doubt at the "
                      "start pure, once bound impure",
                      authority="Mishnah Nazir 9:4",
                      machine_claim="LV15A-01", **NG)]
        if q == "quarantine_decision_deltas":
            return [V("only_loosing_rending_and_birds",
                      "the deltas table: two-vs-three sightings — "
                      "only the offering; quarantined-vs-decided "
                      "leper — only loosing and rending; pure-from-"
                      "quarantine vs pure-from-decision — only the "
                      "shave and the birds: three machine diffs in "
                      "one row",
                      authority="Mishnah Megillah 1:7",
                      machine_claim="LV13C-06", **NG)]
        return []

    def rule_metzora_rite_file(case):
        q = case.get("query")
        if q == "bird_release_geography":
            return [V("city_out_field_ward",
                      "he faces neither sea nor city nor desert — "
                      "'outside the city, over the open field': the "
                      "Sifra's geography row as procedure; and the "
                      "shaved leper's razor over ALL his flesh",
                      authority="Mishnah Negaim 14:2",
                      machine_claim="LV14A-03", **MR)]
        if q == "oil_on_blood_place":
            return [V("place_causes_not_blood",
                      "poured into the fellow's palm (his own "
                      "valid); seven dips toward the House; the oil "
                      "'on the PLACE of the asham's blood'; the "
                      "head-oil dispute (R. Akiva withholds, R. "
                      "Yochanan b. Nuri leftover-of-mitzvah); the "
                      "log-deficit fork — the whole seat standing "
                      "in one Mishnah row",
                      authority="Mishnah Negaim 14:10",
                      machine_claim="LV14A-06", **MR)]
        if q == "leper_four_species_withhold":
            return [V("mutually_withholding",
                      "'the four in the leper withhold one another' "
                      "— cedar, hyssop, scarlet, birds: the kit is "
                      "atomic",
                      authority="Mishnah Menachot 3:6",
                      machine_claim="LV14A-02", **MR)]
        if q == "log_and_asham_waved":
            return [V("waved_not_presented_again",
                      "the leper's log of oil and his asham head "
                      "the waved-not-presented list — the standing "
                      "tenufah family with the two-hands choreography",
                      authority="Mishnah Menachot 5:6",
                      machine_claim="LV14A-06", **MR)]
        if q == "asham_metzora_waving_grid":
            return [V("laid_and_waved_alive",
                      "R. Shimon's three-kinds grid: the leper's "
                      "asham takes laying AND live waving, and no "
                      "slaughtered waving — unique among offerings",
                      authority="R. Shimon — Mishnah Menachot 5:7",
                      machine_claim="LV14A-06", **MR)]
        if q == "quarter_log_water_leper":
            return [V("the_visibility_quarter",
                      "'what did the QUARTER-LOG serve? a quarter of "
                      "water for the LEPER' — the visibility ratio "
                      "the Sifra measures ('water in which the "
                      "bird's blood stays recognizable') quantified "
                      "in the measures table",
                      authority="Mishnah Menachot 9:3",
                      machine_claim="LV14A-03", **MR)]
        if q == "log_per_minchah_dispute":
            return [V("sages_log_per_tenth",
                      "the sages: sixty tenths take sixty logs",
                      authority="the sages — Mishnah Menachot 9:3",
                      machine_claim="LV14A-07", **MR),
                    V("reby_one_log_even_sixty",
                      "R. Eliezer b. Yaakov: even sixty tenths — "
                      "one log, 'for a minchah AND A LOG of oil' "
                      "(Lev 14:21): the Sifra's arm citing the "
                      "poverty verse itself",
                      authority="R. Eliezer b. Yaakov — Mishnah "
                                "Menachot 9:3",
                      machine_claim="LV14A-07", **MR)]
        if q == "asham_metzora_regime":
            return [V("north_slaughter_two_that_are_four",
                      "the leper's asham in the ashamot list: "
                      "north-slaughter, service-vessel reception in "
                      "the north, two gifts that are four, eaten "
                      "inside the hangings by priestly males till "
                      "midnight — the chatat-regime the Sifra "
                      "derives, in the answer-sheet's grid",
                      authority="Mishnah Zevachim 5:5",
                      machine_claim="LV14A-06", **MR)]
        if q == "leper_offering_by_vower":
            return [V("his_status_not_the_vowers",
                      "'this leper's offering is on me' — a poor "
                      "vower for a POOR leper brings the poor "
                      "offering, for a RICH leper the rich (Rabbi's "
                      "arachin cross-argument beside): the Sifra's "
                      "hu-velo-nodrav at its Mishnah seat",
                      authority="Mishnah Arakhin 4:2",
                      machine_claim="LV14A-07", **MR)]
        if q == "birds_then_remarked":
            return [V("needs_his_chatat",
                      "brought his birds and was marked again — the "
                      "birds do not count for him until he brings "
                      "his CHATAT",
                      authority="Mishnah Keritot 2:3",
                      machine_claim="LV14A-07", **MR),
                    V("r_yehuda_his_asham",
                      "R. Yehuda: until he brings his ASHAM — the "
                      "sampling-point dispute in the answer sheet",
                      authority="R. Yehuda — Mishnah Keritot 2:3",
                      machine_claim="LV14A-07", **MR)]
        if q == "nicanor_station_shared":
            return [V("sotah_yoledet_metzora_stand_there",
                      "the East Gate upon Nicanor's door — 'there "
                      "they water the accused wives, PURIFY THE "
                      "BIRTHING MOTHERS, AND PURIFY THE LEPERS': the "
                      "station the Sifra fixes (backs east, faces "
                      "west), shared by the three protocols",
                      authority="Mishnah Sotah 1:5",
                      machine_claim="LV14A-06", **MR)]
        if q == "festival_shave_list":
            return [V("rising_leper_shaves",
                      "the festival shave-list: the sea-traveler, "
                      "the freed captive, the released prisoner, the "
                      "absolved excommunicate, the nazirite — AND "
                      "THE LEPER RISING FROM IMPURITY TO PURITY: the "
                      "protocol's shave overrides the festival ban",
                      authority="Mishnah Moed Katan 3:1",
                      machine_claim="LV14A-05", **MR)]
        if q == "leper_days_nazir_count":
            return [V("counting_days_count_for_him",
                      "'in truth they said: the days of the zav and "
                      "the zavah and the leper's QUARANTINE days "
                      "COUNT for him' — the nazirite's clock keeps "
                      "running through them (completion days void)",
                      authority="Mishnah Nazir 7:3",
                      machine_claim="LV14A-01", **MR)]
        if q == "shave_sunset_offerings":
            return [V("purity_hangs_on_his_shave",
                      "R. Akiva to R. Tarfon: the nazirite's purity "
                      "hangs on his DAYS, the leper's on his SHAVE — "
                      "and he brings no offering unless the sun set "
                      "on his immersion: the Sifra's exchange "
                      "standing whole in the Mishnah",
                      authority="Mishnah Nazir 6:6",
                      machine_claim="LV14A-05", **MR)]
        if q == "leper_birds_any_amount":
            return [V("forbidden_in_any_amount",
                      "the leper's birds stand in the forbidden-and-"
                      "forbidding-in-any-amount list (with the "
                      "scapegoat and the broken-necked heifer) — the "
                      "slaughtered bird's ban has no measure",
                      authority="Mishnah Avodah Zarah 5:9",
                      machine_claim="LV14A-03", **MR)]
        if q == "whole_day_leper_purification":
            return [V("all_day_valid",
                      "'the whole day is valid... for the "
                      "purification of the leper' — the by-day "
                      "family's whole-day rule in the valid-hours "
                      "list",
                      authority="Mishnah Megillah 2:5",
                      machine_claim="LV14A-01", **MR)]
        return []

    def rule_house_file(case):
        q = case.get("query")
        if q == "kenega_humility_row":
            return [V("even_the_expert_says_like",
                      "'even a sage who KNOWS it is certainly a mark "
                      "shall not decree and say A MARK appeared to "
                      "me, but SOMETHING LIKE A MARK appeared to me' "
                      "— the Sifra's humility protocol VERBATIM "
                      "(Onkelos keeps the very particle); with the "
                      "evacuation and R. Meir's earthenware sermon "
                      "in the same row",
                      authority="Mishnah Negaim 12:5",
                      machine_claim="LV14B-02", **HO)]
        if q == "lintel_quarantine_station":
            return [V("stands_at_the_door_and_shuts",
                      "not from inside his own house, not from "
                      "inside the marked house — he stands AT THE "
                      "DOOR of the marked house and quarantines; "
                      "the stone-replacement rules beside (no "
                      "side-to-side, no lime, two for two)",
                      authority="Mishnah Negaim 12:6",
                      machine_claim="LV14B-05", **HO)]
        if q == "house_spread_grades":
            return [V("adjacent_any_distant_bean_return_two",
                      "'the adjacent spread — any amount; the "
                      "distant — a bean; and the RETURNING in "
                      "houses — two beans': the three grades "
                      "VERBATIM as the Sifra states them; the "
                      "demolition row beside",
                      authority="Mishnah Negaim 12:7",
                      machine_claim="LV14B-06", **HO)]
        return []

    def rule_zavim_file(case):
        q = case.get("query")
        if q == "inner_house_asymmetry":
            return [V("she_inside_he_outside",
                      "all women defile IN THE INNER HOUSE ('blood "
                      "shall be her flow IN HER FLESH') — but the "
                      "zav and the semen-emitter defile only once "
                      "their impurity goes OUTSIDE: the Sifra's "
                      "inside-as-outside asymmetry, both halves in "
                      "one row citing the verse",
                      authority="Mishnah Niddah 5:1",
                      machine_claim="LV15B-01", **ZA)]
        if q == "blood_not_stain":
            return [V("dam_not_ketem_lenient",
                      "R. Akiva purified the stain-seer ('perhaps a "
                      "wound?') and answered the staring students: "
                      "'the sages said the matter NOT to be "
                      "stringent but to be LENIENT — BLOOD shall be "
                      "her flow, blood and not a stain' — the "
                      "leniency derived from 15:19's own noun",
                      authority="R. Akiva — Mishnah Niddah 8:3",
                      machine_claim="LV15B-01", **ZA)]
        if q == "bridal_chair_midras":
            return [V("shammai_defile",
                      "the bridal chair stripped of its coverings — "
                      "Beth Shammai defile (midras stands)",
                      authority="Beth Shammai — Mishnah Eduyot 1:11",
                      machine_claim="LV15A-03", **ZA),
                    V("hillel_purify",
                      "Beth Hillel purify — the designated-seat "
                      "classifier's dispute row",
                      authority="Beth Hillel — Mishnah Eduyot 1:11",
                      machine_claim="LV15A-03", **ZA)]
        if q == "living_greater_than_dead":
            return [V("bed_below_madaf_above",
                      "the testimony's own meta-rule: 'GREATER is "
                      "the impurity of the living than of the dead "
                      "— the living makes a bed BENEATH him (to "
                      "defile persons and garments) and a madaf "
                      "ABOVE him (to defile food and drink), which "
                      "the dead does not' — the under/over lattice "
                      "as testimony",
                      authority="Mishnah Eduyot 6:2",
                      machine_claim="LV15A-06", **ZA)]
        if q == "childs_wagon_midras":
            return [V("midras_impure_pressing",
                      "the child's wagon — midras-impure (it takes "
                      "the pressure), movable on Shabbat, dragged "
                      "only over vessels; 'because it PRESSES' (R. "
                      "Yehuda) — the pressure-column family at a "
                      "vessel row",
                      authority="Mishnah Beitzah 2:10",
                      machine_claim="LV15A-04", **ZA)]
        if q == "garments_midras_ladder":
            return [V("each_grade_midras_to_the_next",
                      "the purity ladder: an am-haaretz's garments "
                      "are midras to the abstainers, theirs to "
                      "terumah-eaters, theirs to the holy, theirs "
                      "to the purification water — with Yosef b. "
                      "Yoezer and Yochanan b. Gudgeda as the "
                      "recorded exemplars: the midras grade run as "
                      "a social gradient",
                      authority="Mishnah Chagigah 2:7",
                      machine_claim="LV15A-04", **ZA)]
        if q == "court_partial_uprooting":
            return [V("day_watcher_case_liable",
                      "the court that uproots a WHOLE body ('no "
                      "niddah in the Torah') is exempt; partial "
                      "uprooting — 'there IS niddah, but the "
                      "day-watcher's partner is exempt' — LIABLE: "
                      "the watcher's law is the recorded example of "
                      "a PART of the niddah code ('davar — a word, "
                      "not the whole body')",
                      authority="Mishnah Horayot 1:3",
                      machine_claim="LV15B-05", **ZA)]
        if q == "idol_carried_like_niddah":
            return [V("carry_defiles_by_the_verse",
                      "R. Akiva: an idol defiles by CARRY like the "
                      "niddah — 'you shall cast them away like a "
                      "menstruous thing' (Isa 30:22): her carry-"
                      "defilement exported as the comparison's "
                      "measure",
                      authority="R. Akiva — Mishnah Shabbat 9:1",
                      machine_claim="LV15B-02", **ZA)]
        if q == "third_day_discharge_sinai":
            return [V("ready_for_three_days",
                      "'whence that the third-day discharger is "
                      "impure? — BE READY FOR THREE DAYS (Exod "
                      "19:15)': the Sinai-preparation anchor of the "
                      "dispute the Sifra carries (R. Elazar b. "
                      "Azariah / R. Yishmael / R. Akiva); the "
                      "scarlet tongue rider beside",
                      authority="Mishnah Shabbat 9:3",
                      machine_claim="LV15A-08", **ZA)]
        if q == "day_watcher_immersion_hour":
            return [V("after_sunrise_dawn_valid",
                      "'the day-against-day watcher shall not "
                      "immerse until the sun rises' — done from "
                      "dawn, valid: her watch-day's hour gate in "
                      "the by-day list",
                      authority="Mishnah Megillah 2:4",
                      machine_claim="LV15B-05", **ZA)]
        return []

    return {
        "yoledet_file": {"fn": rule_yoledet_file, "tractate": "Keritot"},
        "milah_shabbat_file": {"fn": rule_milah_shabbat_file,
                               "tractate": "Shabbat"},
        "negaim_exam_file": {"fn": rule_negaim_exam_file,
                             "tractate": "Negaim"},
        "metzora_rite_file": {"fn": rule_metzora_rite_file,
                              "tractate": "Negaim"},
        "house_file": {"fn": rule_house_file, "tractate": "Negaim"},
        "zavim_file": {"fn": rule_zavim_file, "tractate": "Niddah"},
    }
