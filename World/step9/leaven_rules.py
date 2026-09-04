#!/usr/bin/env python3
"""leaven_rules.py — round 12: THE LEAVEN MACHINE, the first of the 18
Exodus Talmud-first exam blocks (2026-09-04). Nine modules on the
leaven verses (Exodus 12:15-20, 13:3-7, 34:25), compiled from the
Pesachim deadline/benefit/after-Passover sugyot per the Noahide
precedent: provenance carries talmud_source (with mishnah beside it
where a Mishnah row stands above the sugya). engine.py merges
build(V) at its tail. Read-source record:
logic/oral_triage/exodus_block_leaven_2026-09-04.md."""


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    # ------------------------------------------------- the deadline
    DL = _EX("Pesachim 4b:9 (Abaye's two verses) + 5a:5 (the word "
             "'akh/yet' divides the day) + 5a:6 (rishon = previous, "
             "Job 15:7) + 5a:16 (Rava: Ex 34:25, no slaughter over "
             "leaven) + 5a:18-20 (the baraita: R. Yishmael, R. Akiva, "
             "R. Yosei)",
             "Exod.12.15+18 (exo_12_passover_and_exodus, EX12-03 the "
             "two lean firsts on the leaven clock; EX12-23 the "
             "derivation cluster, seated F-046)",
             mishnah="Mishnah Pesachim 1:4 (the hour fences)")

    def rule_deadline(case):
        q = case.get("query")
        if q == "removal_day":
            return [V("fourteenth_from_midday",
                      "harishon of Ex 12:15 is the FOURTEENTH — rishon "
                      "means previous (Job 15:7's parallelism), and the "
                      "word akh ('yet') divides the day: removal binds "
                      "from midday. Rava lands the same threshold from "
                      "Ex 34:25 (no leaven at the slaughter hour), R. "
                      "Akiva from the kindling labor (burning cannot "
                      "run on the Festival itself) — four recorded "
                      "derivations, one clock. The ink already carries "
                      "the sign: the Torah's two LEAN rishon skeletons "
                      "both sit on this chapter's leaven clock, and the "
                      "Kitzur reads the dropped vav as the six kept "
                      "hours (EX12-03)", machine_claim="EX12-23", **DL)]
        if q == "removal_night_scope":
            m = case.get("moment")
            if m == "night_of_fifteenth":
                return [V("bound", "the juxtaposition chain: removal "
                          "rides the eating ban (both in Ex 12:19), the "
                          "eating ban rides matza (Ex 12:20 + 12:18), "
                          "and matza's clock opens IN THE EVENING — the "
                          "nights are inside without a second verse "
                          "(Pesachim 5a:1-3)", machine_claim="EX12-23",
                          **DL)]
            if m == "night_of_fourteenth":
                return [V("not_yet_bound", "'on the DAY' is written — "
                          "the removal duty opens on the fourteenth by "
                          "day, not the evening before (Pesachim 5a:4); "
                          "the lamplight SEARCH that evening is the "
                          "Mishnah's own fence (Pesachim 1:1, EX12-19)",
                          machine_claim="EX12-23", **DL)]
        if q == "eating_hour_fence":
            return [V("eat_through_five", "R. Meir: eat through hour "
                      "five, burn at six — the rabbinic fence sits ON "
                      "the Torah's midday threshold",
                      authority="R. Meir", machine_claim="EX12-23",
                      **DL),
                    V("eat_through_four", "R. Yehuda: eat through four, "
                      "abeyance in five, burn at six",
                      authority="R. Yehuda", machine_claim="EX12-23",
                      **DL)]
        return None

    # -------------------------------------------- seen versus found
    SF = _EX("Pesachim 5b:2-6 (the two-phrase baraita) + 6a:6-8 (the "
             "gentile's dough baraita, Rav Pappa / Rav Ashi)",
             "Exod.12.19 (exo_12_passover_and_exodus, EX12-24 the "
             "division of labor, seated F-047; EX12-19 the ownership "
             "scope on lekha)")

    def rule_seen_found(case):
        q = case.get("query")
        if q == "seen_vs_found":
            o = case.get("owner")
            if o == "gentile":
                return [V("may_be_seen", "'no leaven shall be SEEN with "
                          "you' — YOURS you may not see; you may see "
                          "another's and the consecrated (Pesachim "
                          "5b:3)", machine_claim="EX12-24", **SF)]
            if o == "israelite":
                return [V("neither_seen_nor_found", "your own leaven: "
                          "the seen-ban walks the borders, the "
                          "found-ban empties the houses — concealment "
                          "and deposits included (Pesachim 5b:3-6)",
                          machine_claim="EX12-24", **SF)]
        if q == "deposit_duty":
            a = case.get("act")
            if a == "accepted_responsibility":
                return [V("must_remove", "a gentile's leaven deposited "
                          "with a Jew who accepted responsibility is "
                          "FOUND in his house — he removes it (Pesachim "
                          "6a:6, the responsibility parameter)",
                          machine_claim="EX12-24", **SF)]
            if a == "designated_room":
                return [V("exempt", "a room designated for the gentile "
                          "is the gentile's own space — 'in YOUR "
                          "houses, and that house is not his' (Rav "
                          "Ashi, Pesachim 6a:8; Rav Pappa hangs the "
                          "cite on the deposit clause instead — both "
                          "resolutions recorded, one bottom line)",
                          machine_claim="EX12-24", **SF)]
        if q == "leaven_zone_scope":
            return [V("all_possessions", "houses extended to pits, "
                      "ditches, and caves by 'in all your borders,' and "
                      "the baraita carries each place's law to the "
                      "other — one merged scope (Pesachim 5b:5-6)",
                      machine_claim="EX12-24", **SF)]
        return None

    # ------------------------------------------------- the benefit ban
    BF = _EX("Pesachim 21b:5 (Chizkiya: the PASSIVE VOICE of Ex 13:3) "
             "+ 21b:6 (R. Abbahu: every eat-ban) + 21b:11 (R. Yehuda's "
             "route: Ex 22:30, cast it to the DOGS) + 24a:4 (R. "
             "Yonatan: the spare clause of Ex 29:34) + 23a:12 (R. "
             "Yosei HaGelili's recorded dissent)",
             "Exod.13.3 (exo_13_consecration_and_pillars, EX13-16 the "
             "benefit-ban file, seated F-048)")

    def rule_benefit(case):
        q = case.get("query")
        if q == "leaven_benefit_scope":
            return [V("benefit_forbidden", "the standing rule: 'lo "
                      "ye'akhel' in the passive — no permitted "
                      "consumption at all, benefit converts to food "
                      "money (Chizkiya; R. Abbahu reaches it for every "
                      "eat-ban)", authority="Chizkiya and the Rabbis",
                      machine_claim="EX13-16", **BF),
                    V("benefit_permitted", "R. Yosei HaGelili: 'be "
                      "astounded with yourself' — benefit from leaven "
                      "permitted all seven days; his hook is 13:7's "
                      "'with YOU — yours' (Pesachim 23a:12); dissent "
                      "carried forever",
                      authority="R. Yosei HaGelili",
                      machine_claim="EX13-16", **BF)]
        if q == "benefit_derivation_route":
            return [V("route_passive_voice", "Chizkiya: the passive "
                      "form itself widens the ban — the M-15 voice "
                      "read", authority="Chizkiya",
                      machine_claim="EX13-16", **BF),
                    V("route_universal_eat_ban", "R. Abbahu: every "
                      "it-shall-not-be-eaten bans benefit unless the "
                      "verse releases it (the carcass's give-or-sell, "
                      "on R. Meir's reading)", authority="R. Abbahu",
                      machine_claim="EX13-16", **BF),
                    V("route_dogs_verse", "on R. Yehuda's as-written "
                      "carcass, the route is Ex 22:30 — 'sacred men... "
                      "cast it to the dogs': to the dog yes, any other "
                      "ban no", authority="R. Yehuda's line",
                      machine_claim="EX13-16", **BF),
                    V("route_consecration_leftover", "R. Yonatan: Ex "
                      "29:34's 'it shall not be eaten' is SPARE (the "
                      "burn clause already bans eating) — reassigned "
                      "to all Torah bans, and past eating to benefit; "
                      "the burn MODE stays home (Pesachim 24a:4-5)",
                      authority="R. Yonatan",
                      machine_claim="EX13-16", **BF)]
        if q == "charred_before_time":
            return [V("benefit_permitted_after", "Rava: charred before "
                      "its hour, it is no longer bread — benefit stands "
                      "even after (Pesachim 21b:2)",
                      machine_claim="EX13-16", **BF)]
        if q == "betrothal_with" and case.get("item") == "leaven":
            return [V("betrothal_invalid", "from hour six the leaven is "
                      "benefit-dead and worth no perutah — betrothal "
                      "with it takes no hold, even wheat of the "
                      "mountains (Pesachim 21b:3, the rabbinic hours "
                      "already carry it)", machine_claim="EX13-16",
                      **BF)]
        if q == "burning_benefit":
            return [V("forbidden_while_burning", "even on R. Yehuda's "
                      "burn rule, no warming by the fire of the mitzvah "
                      "— benefit banned during the burning itself "
                      "(Pesachim 21b:4)", machine_claim="EX13-16", **BF)]
        return None

    # -------------------------------------------------- removal mode
    RM = _EX("Pesachim 27b:8-10 (R. Yehuda's a-fortiori, the Rabbis' "
             "validity gate, the what-do-we-find refounding) + 28a:8-9 "
             "(crumble to wind and sea)",
             "Exod.12.15 (exo_12_passover_and_exodus, EX12-23)",
             mishnah="Mishnah Pesachim 2:1")

    def rule_removal_mode(case):
        q = case.get("query")
        if q == "removal_mode":
            return [V("burning_only", "R. Yehuda: as the leftover "
                      "offering burns, leaven — carrying the stricter "
                      "seen/found bans — burns a fortiori; refounded "
                      "on the what-do-we-find form after the gate "
                      "fired", authority="R. Yehuda",
                      machine_claim="EX12-23", **RM),
                    V("any_means", "the Rabbis: 'you shall REMOVE' — "
                      "in any manner; crumble it to the wind, throw it "
                      "to the sea (Pesachim 28a:8; grinding follows "
                      "dissolution, wheat yes, bread no)",
                      authority="the Rabbis", machine_claim="EX12-23",
                      **RM)]
        if q == "inference_validity":
            return [V("invalid_derivation", "the Rabbis' gate: a "
                      "derivation whose start is stringent and whose "
                      "outcome is lenient is NO derivation — with no "
                      "wood he would sit idle, and the Torah said "
                      "remove in any manner (Pesachim 27b:9); an "
                      "inference-validity meta-rule, catalogued",
                      machine_claim="EX12-23", **RM)]
        return None

    # --------------------------------------------- after Passover
    AP = _EX("Pesachim 28a:10-29a:7 (the three-authority frame; Rava "
             "reads the mishnah as R. Shimon plus a Sages' penalty; "
             "R. Acha bar Yaakov as R. Yehuda by Torah law; the "
             "lashes split at 29a:7)",
             "Exod.13.7 (exo_13_consecration_and_pillars, EX13-16)",
             mishnah="Mishnah Pesachim 2:2")

    def rule_after_passover(case):
        q = case.get("query")
        if q == "elapsed_leaven_law_layer":
            return [V("rabbinic_fine", "Rava: the mishnah is R. Shimon "
                      "— by Torah law elapsed leaven is permitted, and "
                      "the Jew who kept it through seen/found is FINED "
                      "by the Sages", authority="Rava",
                      machine_claim="EX13-16", **AP),
                    V("torah_ban", "R. Acha bar Yaakov: the mishnah is "
                      "R. Yehuda — the after-window is one of his "
                      "three verses, a Torah ban",
                      authority="R. Acha bar Yaakov",
                      machine_claim="EX13-16", **AP)]
        if q == "elapsed_gentile_lashes":
            return [V("flogged", "Rava: within R. Yehuda's framework "
                      "the eater of a gentile's elapsed leaven is "
                      "flogged", authority="Rava",
                      machine_claim="EX13-16", **AP),
                    V("not_flogged", "R. Acha bar Yaakov: he is not",
                      authority="R. Acha bar Yaakov",
                      machine_claim="EX13-16", **AP)]
        if q == "ban_window_census":
            return [V("three_windows", "R. Yehuda: three verses, three "
                      "windows — Ex 13:3 before its time, Ex 12:20 "
                      "after its time, Deut 16:3 during (the "
                      "Deuteronomy import edge)",
                      authority="R. Yehuda", machine_claim="EX13-16",
                      **AP),
                    V("during_only", "R. Shimon: the ban runs when "
                      "matza-duty runs; 12:20 goes to "
                      "leavened-through-another-substance, 13:3 to "
                      "Egypt's one day", authority="R. Shimon",
                      machine_claim="EX13-16", **AP)]
        if q == "egypt_passover_leaven_days":
            return [V("one_day", "R. Yosei HaGelili: 'leavened bread "
                      "shall not be eaten' stands juxtaposed to 'THIS "
                      "DAY you go forth' (Ex 13:3-4) — Egypt's own "
                      "Passover banned leaven one day (R. Yehuda "
                      "either concedes the juxtaposition or reads "
                      "seven — both arms recorded, Pesachim 28b:8)",
                      authority="R. Yosei HaGelili",
                      machine_claim="EX13-16", **AP)]
        return None

    # ------------------------------------------------------ mixtures
    MX = _EX("Pesachim 43a:18-19 (the kutach baraita: karet for the "
             "full-fledged from Ex 12:15, plain prohibition for the "
             "admixture from Ex 12:20; whose baraita — R. Eliezer's "
             "line on mixtures, R. Meir's on the hardened) + 28b:5+7 "
             "(machmetzet by both routes)",
             "Exod.12.20+15 (exo_12_passover_and_exodus, EX12-02 the "
             "lean eat-word, EX12-24)")

    def rule_mixtures(case):
        q = case.get("query")
        if q == "leaven_mixture_liability":
            return [V("prohibition_no_karet", "'ANYTHING leavened' (Ex "
                      "12:20) pulls Babylonian kutach, Median beer, "
                      "Edomite vinegar, Egyptian zitom into the ban — "
                      "and 12:15's karet clause holds at full-fledged "
                      "leavened bread only", machine_claim="EX12-24",
                      **MX)]
        if q == "leaven_full_liability":
            return [V("karet", "'whoever eats leavened bread, that soul "
                      "shall be cut off' (Ex 12:15) — the karet seat, "
                      "its eat-word written LEAN forever (EX12-02)",
                      machine_claim="EX12-24", **MX)]
        if q == "leavened_by_other_substance":
            return [V("bound", "dough leavened by another substance is "
                      "leaven — R. Shimon from 12:20's own verse, R. "
                      "Yehuda from the bare general term (Pesachim "
                      "28b:5+7, both routes recorded)",
                      machine_claim="EX12-24", **MX)]
        return None

    # ----------------------------------------- the two-words measure
    TW = _EX("Yoma 79b:5-6 (Rav Zevid; Beit Shammai's two-words "
             "argument: had one measure served, one word would have "
             "served — leaven the strong riser at the olive, bread "
             "the weak at the date; and the date is LESS than the "
             "egg)",
             "Exod.12.19+13.7 (exo_12_passover_and_exodus, EX12-19 "
             "carrying the seated Beitzah 1:1 dispute)",
             mishnah="Mishnah Beitzah 1:1")

    def rule_two_words(case):
        q = case.get("query")
        if q == "leaven_two_words_reason":
            return [V("measures_differ", "Beit Shammai: the verse "
                      "writes BOTH 'leaven' and 'leavened bread' — two "
                      "words, two measures (olive for leaven, large "
                      "date for bread); Beit Hillel holds the olive "
                      "for both — the seated dispute's derivation "
                      "layer", authority="Beit Shammai per Rav Zevid",
                      machine_claim="EX12-19", **TW)]
        if q == "date_vs_egg_volume":
            return [V("date_less_than_egg", "Rav Zevid: the large date "
                      "they spoke of is LESS than an egg-bulk — the "
                      "affliction measure's volume fixed against the "
                      "leaven rows (a transmitted quantity, the data "
                      "channel)", machine_claim="EX12-19", **TW)]
        return None

    # ---------------------------------------- matza's standing duty
    MS = _EX("Pesachim 28b:10-12 (R. Yehuda: the juxtaposition binds "
             "matza nowadays; R. Shimon: Ex 12:18's own evening span; "
             "the impure and far-traveled no worse than the "
             "uncircumcised) + Kiddushin 37b:12 (in all your "
             "DWELLINGS) + Rosh Hashanah 20b:10 (Reish Lakish)",
             "Exod.12.18+20 (exo_12_passover_and_exodus, EX12-04 the "
             "lean matzot ink)")

    def rule_matza_standing(case):
        q = case.get("query")
        if q == "matza_after_temple":
            return [V("obligatory", "matza binds with no Temple and no "
                      "lamb — three recorded routes: R. Yehuda rides "
                      "the leaven juxtaposition, R. Shimon rides Ex "
                      "12:18's own 'in the evening you shall eat "
                      "matzot,' and the dwellings-word carries it to "
                      "every seat (Kiddushin 37b:12)",
                      machine_claim="EX12-04", **MS)]
        if q == "matza_impure_far_traveled":
            return [V("obligated", "the impure and the far-traveled "
                      "eat matza and bitter herbs — R. Yehuda spends "
                      "Ex 12:18 on them; R. Shimon needs no verse: no "
                      "worse than the uncircumcised, whose 'of IT' "
                      "blocks the lamb alone (Ex 12:48)",
                      machine_claim="EX12-04", **MS)]
        if q == "day_boundary_source":
            return [V("evening_begins_day", "Reish Lakish: 'on the "
                      "fourteenth at evening... until the twenty-first "
                      "at evening' (Ex 12:18) — the day begins at "
                      "evening; R. Yochanan's rival seat is Lev 23:32, "
                      "and Abaye records no practical difference",
                      machine_claim="EX12-04", **MS)]
        return None

    # ------------------------------------------------ search law
    SL = _EX("Pesachim 10b:13-16 (R. Yehuda's three times against the "
             "Rabbis; Rav Chisda and Rabba bar Rav Huna: three "
             "searches for three verses; Rav Yosef: three "
             "OPPORTUNITIES) + 6b:2-3 (the study window)",
             "Exod.12.15+19 (exo_12_passover_and_exodus, EX12-19 the "
             "lamplight search row)",
             mishnah="Mishnah Pesachim 1:1")

    def rule_search_law(case):
        q = case.get("query")
        if q == "search_count":
            return [V("three_searches", "R. Yehuda as Rav Chisda and "
                      "Rabba bar Rav Huna read him: three searches "
                      "answering the three removal verses (13:7, "
                      "12:19, 12:15); Rav Yosef re-reads the three as "
                      "opportunities with a closing gate",
                      authority="R. Yehuda", machine_claim="EX12-19",
                      **SL),
                    V("search_when_missed", "the Rabbis: one search, "
                      "and whoever missed it searches at the next "
                      "station — eve, morning, Festival, even after "
                      "(the elapsed leaven still owed removal)",
                      authority="the Rabbis", machine_claim="EX12-19",
                      **SL)]
        if q == "study_window":
            return [V("thirty_days", "the Sages: Moses stands on the "
                      "New Moon of Nisan (Ex 12:2) warning for the "
                      "fourteenth (12:3) — thirty days of asking and "
                      "expounding", authority="the Sages",
                      machine_claim="EX12-19", **SL),
                    V("two_weeks", "Rabban Shimon ben Gamliel: two "
                      "weeks — Moses simply finished all the Passover "
                      "matters in one speech; no window derives",
                      authority="Rabban Shimon ben Gamliel",
                      machine_claim="EX12-19", **SL)]
        return None

    return {
        "leaven_deadline": {"fn": rule_deadline},
        "leaven_seen_found": {"fn": rule_seen_found},
        "leaven_benefit": {"fn": rule_benefit},
        "leaven_removal_mode": {"fn": rule_removal_mode},
        "leaven_after_passover": {"fn": rule_after_passover},
        "leaven_mixtures": {"fn": rule_mixtures},
        "leaven_measures_derivation": {"fn": rule_two_words},
        "matza_standing_duty": {"fn": rule_matza_standing},
        "leaven_search_law": {"fn": rule_search_law},
    }
