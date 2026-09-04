#!/usr/bin/env python3
"""courts_rules.py — round 13: THE COURTS, the second Exodus
Talmud-first exam block (2026-09-04). Ten modules on the appointment
narrative (Exodus 18:13-26), the deposit-court verses (22:7-8), and
the justice cluster (23:1-8), compiled from the Sanhedrin
composition/procedure sugyot per the Noahide precedent. The
already-compiled composition tables (court_architecture, court_tiers,
witness_fitness, stoned_ox_process) stand untouched; these modules
carry the DERIVATION layer and the unheld rows. engine.py merges
build(V) at its tail. Read-source record:
logic/oral_triage/exodus_block_courts_2026-09-04.md."""


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    # ------------------------------------- the three-judges derivation
    TJ = _EX("Sanhedrin 3b:2 (R. Yoshiya) + 3b:3 (R. Yonatan) + 3b:17 "
             "(R. Yehuda HaNasi) + 3b:4-5 (the elohim-not-shofet "
             "exchange)",
             "Exod.22.7-8 (exo_22_property_social, EX22-04 — the seat "
             "ANTICIPATED the sugya: R. Yoshiya, R. Yonatan who does "
             "not expound beginnings, and Rebbi from the plural verb "
             "all stand in the frozen claim since 2026-09-02)")

    def rule_three_judges(case):
        q = case.get("query")
        if q == "three_judges_source":
            return [V("three_elohim_count", "R. Yoshiya: the deposit "
                      "passage writes ha-elohim THREE times (22:7, "
                      "22:8 twice) — three judges; his defense: had "
                      "the plain sense been all, the verse would say "
                      "'the judge' — the god-word was chosen to count",
                      authority="R. Yoshiya", machine_claim="EX22-04",
                      **TJ),
                    V("two_plus_odd", "R. Yonatan: the FIRST mention "
                      "serves the plain sense and is not counted (the "
                      "verse speaks the world's common language) — two "
                      "mentions, and no even court: three",
                      authority="R. Yonatan", machine_claim="EX22-04",
                      **TJ),
                    V("five_by_analogy", "R. Yehuda HaNasi: yarshi'un "
                      "('shall condemn') is PLURAL — two; the-court/"
                      "the-court carries two more from the verse above "
                      "— four; no even court: FIVE (the M-12 "
                      "grammatical-number hook at the bench itself; R. "
                      "Abbahu's ridicule of the verdict-of-three "
                      "reading recorded beside it)",
                      authority="R. Yehuda HaNasi",
                      machine_claim="EX22-04", **TJ)]
        if q == "first_mention_counted":
            return [V("counted", "R. Yoshiya counts it — the god-word "
                      "over the judge-word is the signal",
                      authority="R. Yoshiya", machine_claim="EX22-04",
                      **TJ),
                    V("not_counted", "R. Yonatan: a first mention is "
                      "stated for the matter itself; tallies open at "
                      "the second (the meta-rule; block 15's docket "
                      "holds its general form)",
                      authority="R. Yonatan", machine_claim="EX22-04",
                      **TJ)]
        return None

    # ------------------------------------------------- the odd court
    OC = _EX("Sanhedrin 3b:6 (R. Eliezer son of R. Yosei HaGelili) + "
             "3b:7-13 (R. Yoshiya's scope and the majority "
             "a-fortiori)",
             "Exod.23.2 (exo_23_justice_calendar, EX23-10 — the "
             "conduct file, seated F-050; EX23-02 the margin of two)")

    def rule_odd_court(case):
        q = case.get("query")
        if q == "even_court_valid":
            return [V("never_even", "'to incline after a multitude' — "
                      "make yourself a court that CAN incline: an odd "
                      "bench (R. Eliezer son of R. Yosei HaGelili); "
                      "every composition above rides it (+1 at three, "
                      "five, twenty-three, seventy-one)",
                      machine_claim="EX23-10", **OC)]
        if q == "odd_court_scope":
            return [V("all_courts", "the standing rule: no even bench "
                      "anywhere — R. Yehuda concedes it below the "
                      "Great Sanhedrin (the laying-on five)",
                      authority="the Rabbis", machine_claim="EX23-10",
                      **OC),
                    V("capital_only", "R. Yoshiya: the incline-verse "
                      "speaks of capital law only; monetary benches "
                      "may stand even", authority="R. Yoshiya",
                      machine_claim="EX23-10", **OC)]
        if q == "monetary_majority":
            return [V("majority_suffices", "even R. Yoshiya follows "
                      "the majority in money — a fortiori from "
                      "capital: if the strict follows the many, the "
                      "lenient surely does (Sanhedrin 3b:13; the "
                      "two-against-one mishnah stands)",
                      machine_claim="EX23-10", **OC)]
        return None

    # -------------------------------------- the twenty-three arithmetic
    CA = _EX("Mishnah Sanhedrin 1:6 via Sanhedrin 2a:14-16 (the "
             "congregation count and the margin) + 10a:11 (the "
             "wicked-wicked analogy) + 2a:10 + 15b:7 (the beasts) + "
             "15b:6 (the Sinai ox)",
             "Exod.23.2 (exo_23_justice_calendar, EX23-02 the margin "
             "of two; EX23-10)",
             mishnah="Mishnah Sanhedrin 1:4 + 1:6")

    def rule_capital_arithmetic(case):
        q = case.get("query")
        if q == "twenty_three_derivation":
            return [V("congregation_plus_margin", "a congregation "
                      "judges and a congregation saves (Numbers "
                      "35:24-25) — ten and ten, the congregation "
                      "fixed at ten by the spies; and our 23:2 adds "
                      "the margin: convict by two, so twenty-two — "
                      "and no even court: TWENTY-THREE",
                      machine_claim="EX23-02", **CA)]
        if q == "convict_margin":
            return [V("two_to_convict_one_to_acquit", "'you shall not "
                      "follow a multitude to convict' against 'to "
                      "incline after a multitude': your inclining for "
                      "good is by ONE, your inclining for evil by TWO "
                      "(Sanhedrin 2a:16 — every step on the verse)",
                      machine_claim="EX23-02", **CA)]
        if q == "lashes_court":
            return [V("three", "the first tanna: lashes in three",
                      authority="the Sages", machine_claim="EX23-10",
                      **CA),
                    V("twenty_three", "R. Yishmael, by the "
                      "wicked-wicked verbal analogy — 'if the wicked "
                      "man deserves to be beaten' beside 'a wicked "
                      "man guilty of death': the lash trial dressed "
                      "as a capital trial (Sanhedrin 10a:11)",
                      authority="R. Yishmael", machine_claim="EX23-10",
                      **CA)]
        if q == "beast_that_killed":
            return [V("twenty_three", "R. Akiva: the wolf, lion, "
                      "bear, leopard, cheetah, snake that killed are "
                      "judged like the ox — with the Reish Lakish / "
                      "R. Yochanan split on whether killing first is "
                      "even needed (ownability)",
                      authority="R. Akiva", machine_claim="EX23-10",
                      **CA),
                    V("kill_first_merits", "R. Eliezer: no court — "
                      "whoever kills them first merits",
                      authority="R. Eliezer", machine_claim="EX23-10",
                      **CA)]
        if q == "ox_at_sinai":
            return [V("twenty_three", "Rami bar Yechezkel: 'whether "
                      "animal or man it shall not live' (19:13) — the "
                      "animal judged like the man; a standing rule "
                      "drawn from a time-bound law, the dilemma named "
                      "and answered (Sanhedrin 15b:6)",
                      machine_claim="EX23-10", **CA)]
        return None

    # --------------------------------------------- the great court
    GC = _EX("Sanhedrin 16a:1 (Rav Adda bar Ahava) + 16a:2 (Ulla) + "
             "16b:9 (as Moses appointed) + 17a:2-3 (the with-you "
             "exchange)",
             "Exod.18.22+25 (exo_18_jethro_and_the_judges, EX18-15 — "
             "the appointment constitution, seated F-051; EX18-14 "
             "the tiers)")

    def rule_great_court(case):
        q = case.get("query")
        if q == "great_matter_meaning":
            return [V("matters_of_a_great_one", "Rav Adda bar Ahava: "
                      "'every GREAT matter' = the matters of a GREAT "
                      "ONE — the tribe's Nasi tried by seventy-one",
                      authority="Rav Adda bar Ahava",
                      machine_claim="EX18-15", **GC),
                    V("border_disputes", "Ulla in R. Elazar's name: "
                      "two tribes' inheritance dispute — as the first "
                      "division ran by the seventy-one elders",
                      authority="Ulla citing R. Elazar",
                      machine_claim="EX18-15", **GC)]
        if q == "lesser_courts_appointer":
            return [V("the_seventy_one", "as Moses — who stands in "
                      "the great court's place — appointed the courts "
                      "for all the people (18:25-26), lesser benches "
                      "are appointed by the seventy-one",
                      machine_claim="EX18-15", **GC)]
        if q == "judge_qualification":
            return [V("similar_to_you", "'and they shall bear WITH "
                      "YOU' (18:22, the Rabbis; R. Yehuda from "
                      "Numbers 11:17): with you — LIKE you, fit "
                      "lineage and free of blemish; the seated "
                      "marriageable-bench rule's own derivation",
                      machine_claim="EX18-15", **GC)]
        return None

    # ---------------------------------------------- the town threshold
    TT = _EX("Mishnah Sanhedrin 1:6 via Sanhedrin 17b:10-11 + 18a:2-3",
             "Exod.18.21 (exo_18_jethro_and_the_judges, EX18-15)",
             mishnah="Mishnah Sanhedrin 1:6")

    def rule_town_threshold(case):
        q = case.get("query")
        if q == "town_court_minimum":
            return [V("one_hundred_twenty", "the first tanna: a town "
                      "of a hundred and twenty (the breakdown's frame "
                      "at 17b:10 — the bench, its officers, the ten "
                      "amenities)", authority="the first tanna",
                      machine_claim="EX18-15", **TT),
                    V("two_hundred_thirty", "R. Nechemya: two hundred "
                      "thirty — twenty-three ministers of TENS, each "
                      "judge standing over his verse-given ten "
                      "(18:21; Rabbi's 277/278 variants reconciled by "
                      "the 70/71 dispute at 18a:2)",
                      authority="R. Nechemya", machine_claim="EX18-15",
                      **TT)]
        if q == "officer_census":
            # The verse's own tiers divide the wilderness count:
            total = 600000
            census = sum(total // n for n in (1000, 100, 50, 10))
            assert census == 78600
            return [V("seventy_eight_thousand_six_hundred", "COMPUTED "
                      "from 18:21's own denominations over the "
                      "six-hundred-thousand: 600 ministers of "
                      "thousands + 6,000 of hundreds + 12,000 of "
                      "fifties + 60,000 of tens = 78,600 judges "
                      "(Sanhedrin 18a:3 — the machine reruns the "
                      "division and lands on the recorded sum)",
                      machine_claim="EX18-15", **TT)]
        return None

    # ------------------------------------------------ king and court
    KC = _EX("Sanhedrin 18b:9 (al riv → al rav) + 19a:15-17 (Rav "
             "Yosef; the Yannai episode) + 20b:11-12 (the entrance "
             "duties)",
             "Exod.23.2 + 21.29 + 17.16 (exo_23_justice_calendar, "
             "EX23-10)",
             mishnah="Mishnah Sanhedrin 2:2")

    def rule_king_court(case):
        q = case.get("query")
        if q == "king_on_bench":
            return [V("never_seated", "'do not answer in a cause "
                      "[riv]' read 'do not answer over a master "
                      "[rav]': a bench no one dares contradict is no "
                      "bench — the king sits on no Sanhedrin (and no "
                      "intercalation court: the soldiers' sustenance; "
                      "the high priest off it too — the cold)",
                      machine_claim="EX23-10", **KC)]
        if q == "king_judged":
            return [V("israel_kings_not_judged", "Rav Yosef: the "
                      "kings of ISRAEL — for the Yannai episode: the "
                      "summons rode our 21:29 ('he should be "
                      "testified against WITH HIS OWNER' — the owner "
                      "stands with his ox), Yannai refused, and the "
                      "bench fell silent — the decree's recorded "
                      "cause", authority="Rav Yosef on the kings of "
                      "Israel", machine_claim="Mishnah Sanhedrin 2:2 + talmud_source (the 21:29 summons hook lives in exo_21's span)", **KC),
                    V("davidic_judged", "the house of David judges "
                      "and is judged — 'execute justice in the "
                      "morning'; adorn yourself first, then adorn "
                      "others", authority="Rav Yosef on the house of "
                      "David", machine_claim="Mishnah Sanhedrin 2:2 + talmud_source", **KC)]
        if q == "entrance_mitzvot_order":
            return [V("king_first", "R. Yosei's three entrance duties "
                      "— king, Amalek, the chosen house — ordered by "
                      "17:16: 'the hand upon the throne [kes] of the "
                      "LORD... war with Amalek' — the throne is the "
                      "king (1 Chronicles 29:23), so the king "
                      "precedes the war, and the house comes last",
                      machine_claim="talmud_source only (the Exod 17:16 anchor lives in exo_17's span)", **KC)]
        return None

    # --------------------------------------- witness disqualification
    WD = _EX("Sanhedrin 9b:8 + 25a:8-9 (his own relative) + 10a:10 "
             "(the actless ban) + 27b:15-17 (the fathers verse)",
             "Exod.23.1 + 20.13 + 34.7 (exo_23_justice_calendar, "
             "EX23-01 the wicked-witness filter; EX23-10)")

    def rule_witness_disq(case):
        q = case.get("query")
        if q == "self_incrimination":
            return [V("testimony_splits", "Rava: A PERSON IS HIS OWN "
                      "RELATIVE — he cannot render himself wicked, so "
                      "the self-condemning half of his testimony is "
                      "void and the half against the other stands "
                      "(the sodomy witness at 9b:8; the interest "
                      "borrower at 25a:9 — two seats, one principle)",
                      machine_claim="EX23-10", **WD)]
        if q == "false_witness_lash_source":
            return [V("own_derivation_needed", "20:13's testify-ban "
                      "involves NO ACT — and an actless prohibition "
                      "is not flogged (the meta-rule this corpus "
                      "already carries at Pesachim 84a:14's "
                      "bone-breaking seat) — so the conspiring "
                      "witness's lashes ride their own "
                      "justify/condemn derivation (Sanhedrin 10a:10)",
                      machine_claim="EX23-10", **WD)]
        if q == "children_for_fathers":
            return [V("only_holding_the_deeds", "34:7's visiting-"
                      "iniquity against 'each dies for his own sin' — "
                      "resolved: the fathers' iniquity reaches "
                      "children WHO HOLD THE ANCESTORS' DEEDS IN "
                      "THEIR HANDS; and the testimony layer reads "
                      "fathers-for-children at the witness stand "
                      "(27b:15)", machine_claim="EX23-10", **WD)]
        return None

    # --------------------------------- procedure times and returns
    PT = _EX("Sanhedrin 33b:5-6 (the innocent/righteous assignment) + "
             "34b:8-9 (Rava's day/night reconciliation) + 35b:4-7 "
             "(murder against service and Shabbat) + 36b:2-3 (the "
             "ox's protections)",
             "Exod.23.6-7 + 21.14 + 18.22 (exo_23_justice_calendar, "
             "EX23-10)",
             mishnah="Mishnah Sanhedrin 4:1")

    def rule_procedure(case):
        q = case.get("query")
        if q == "return_for_acquittal":
            return [V("brought_back", "'the INNOCENT you shall not "
                      "slay' — one walking out condemned returns for "
                      "a reason to acquit: he may yet be innocent",
                      machine_claim="EX23-04 (the acquittal asymmetry, seated 2026-09-01 — the seat anticipated the sugya)", **PT)]
        if q == "return_for_liability":
            return [V("not_brought_back", "'the RIGHTEOUS you shall "
                      "not slay' — one walking out acquitted was "
                      "found righteous in his trial: he never "
                      "returns for liability", machine_claim="EX23-04",
                      **PT)]
        if q == "monetary_trial_times":
            st = case.get("stage")
            if st == "trial_open":
                return [V("day_only", "Rava reconciles 'they shall "
                          "judge at ALL times' (18:22) with 'on the "
                          "DAY' (Deut 21:16): the trial OPENS by day",
                          machine_claim="EX18-15", **PT)]
            if st == "verdict":
                return [V("night_allowed", "the verdict may conclude "
                          "at night — that is the 'at all times' of "
                          "our verse (monetary law)",
                          machine_claim="EX18-15", **PT)]
        if q == "ox_stoning_class":
            return [V("only_the_twenty_three", "R. Abbahu: of the ten "
                      "capital protections the stoned ox keeps ONE — "
                      "the bench of twenty-three; 'you shall not "
                      "incline the judgment of your POOR' — your "
                      "poor, not the ox (36b:2-3)",
                      machine_claim="EX23-10", **PT)]
        if q == "murder_overrides":
            return [V("service_not_shabbat", "'from My altar you "
                      "shall take him' (21:14) — the murder trial "
                      "pulls even the serving priest from the altar; "
                      "but not Shabbat: the school of R. Yishmael "
                      "reads 'no fire in your habitations' (35:3) as "
                      "execution-burning banned on Shabbat — with the "
                      "R. Yosei / R. Natan kindling fork beneath it, "
                      "the same fork Rava's three learnings hit at "
                      "Pesachim 5b:1 (block 9's import edge, recorded "
                      "from two directions)", machine_claim="EX23-10",
                      **PT)]
        return None

    # ------------------------------------------ standing and distance
    SD = _EX("Shevuot 30b:2-3 (the posture rows) + 30b:13-14 (the "
             "distancing cluster) + Sanhedrin 7b:15 (lo tissa / lo "
             "tassi)",
             "Exod.18.13 + 23.1 + 23.7 (exo_18_jethro_and_the_judges, "
             "EX18-15; exo_23_justice_calendar, EX23-10)")

    def rule_standing(case):
        q = case.get("query")
        if q == "court_posture":
            return [V("judges_sit_litigants_stand", "'Moses SAT to "
                      "judge the people, and the people STOOD' "
                      "(18:13) — at the verdict the judges sit and "
                      "the litigants stand; witnesses always stand "
                      "(Deut 19:17's two-men-shall-stand)",
                      machine_claim="EX18-15", **SD)]
        if q == "judge_advocacy":
            return [V("distancing_cluster", "'distance yourself from "
                      "a false matter' (23:7) three times over: the "
                      "judge no advocate for his own rulings; no "
                      "ignoramus student debating before him; no "
                      "joining a known robber in judgment or "
                      "testimony", machine_claim="EX23-10", **SD)]
        if q == "litigant_ex_parte":
            return [V("forbidden_both_sides", "lo tissa ('you shall "
                      "not BEAR a false report') read also lo tassi "
                      "('you shall not DELIVER') — the judge may not "
                      "hear one litigant alone, and the litigant may "
                      "not explain himself alone: one verse, both "
                      "addressees (Rav Kahana, Sanhedrin 7b:15)",
                      machine_claim="EX23-01 (the three warnings, seated 2026-08-12 — the seat anticipated the sugya)", **SD)]
        return None

    # ------------------------------------------------ bench integrity
    BI = _EX("Sanhedrin 7b:9 (Rav Ashi) + 7b:12 (Bar Kappara; R. "
             "Eliezer's arm)",
             "Exod.20.20 + 20.23-21.1 (exo_23_justice_calendar, "
             "EX23-10)")

    def rule_bench_integrity(case):
        q = case.get("query")
        if q == "judge_for_payment":
            return [V("gods_of_silver", "'you shall not make with Me "
                      "gods of SILVER and gods of GOLD' (20:20) — Rav "
                      "Ashi: the judge who comes for silver and the "
                      "judge who comes for gold: an appointed-for-pay "
                      "bench is an idol", machine_claim="talmud_source only (the Exod 20:20 anchor lives in exo_20's span)",
                      **BI)]
        if q == "temperance_source":
            return [V("steps_then_ordinances", "'neither shall you go "
                      "up by STEPS onto My altar' — and juxtaposed: "
                      "'now these are the ORDINANCES' (20:23-21:1) — "
                      "Bar Kappara: be temperate in judgment; R. "
                      "Eliezer's arm: the judge steps over no heads",
                      machine_claim="talmud_source only (the Exod 20:23-21:1 anchor lives in exo_20's span)", **BI)]
        return None

    return {
        "three_judges_derivation": {"fn": rule_three_judges},
        "odd_court_law": {"fn": rule_odd_court},
        "capital_court_arithmetic": {"fn": rule_capital_arithmetic},
        "great_court_docket": {"fn": rule_great_court},
        "town_court_threshold": {"fn": rule_town_threshold},
        "king_and_court": {"fn": rule_king_court},
        "witness_disqualification_law": {"fn": rule_witness_disq},
        "procedure_times_and_returns": {"fn": rule_procedure},
        "standing_and_distance": {"fn": rule_standing},
        "bench_integrity": {"fn": rule_bench_integrity},
    }
