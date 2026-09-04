#!/usr/bin/env python3
"""persons_rules.py — round 14: THE ORDINANCES' PERSONS, the third
Exodus Talmud-first exam block (2026-09-04). Ten modules on Exodus
21:1-22:2, the derivation layer over the compiled chapter-21 machine
(the law-era 35 claims + the compiler seats). engine.py merges
build(V) at its tail. Read-source record:
logic/oral_triage/exodus_block_persons_2026-09-04.md."""


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    # -------------------------------------------------- forewarning
    FW = _EX("Sanhedrin 41a:1-3 (the school of Chizkiya; the school "
             "of R. Yishmael's gatherer parallel)",
             "Exod.21.14 (exo_21_the_ordinances, EX21-23 — seated "
             "F-051)")

    def rule_forewarning(case):
        if case.get("query") != "forewarning_source":
            return None
        return [V("intent_implies_warning", "'if a man come "
                  "INTENTIONALLY upon his neighbor' (21:14) — how do "
                  "the witnesses know he acted intentionally? THEY "
                  "FOREWARNED HIM and he persisted (the school of "
                  "Chizkiya); the school of R. Yishmael reads the "
                  "gatherer's present tense the same way, and 41a:1 "
                  "carries the requirement to lashes",
                  machine_claim="EX21-23", **FW)]

    # -------------------------------------------------- slave clock
    SC = _EX("Niddah 47b:21 + 48a:2 (whole years from 'AND in the "
             "seventh') + Kiddushin 17a:1-4 (the sick slave) + "
             "18a:8-9 (sold for his theft)",
             "Exod.21.2 + 22.2 (exo_21_the_ordinances, EX21-25 — "
             "seated F-054; the compiled term clock behind it)")

    def rule_slave_clock(case):
        q = case.get("query")
        if q == "slave_year_semantics":
            return [V("whole_years_to_his_date", "'six years he shall "
                      "work AND IN THE SEVENTH' — the vav pulls his "
                      "service into the seventh calendar year until "
                      "his own sale-date: time-to-time whole years, "
                      "never the calendar's edge (Niddah 48a:2)",
                      machine_claim="EX21-25", **SC)]
        if q == "sick_slave_exit":
            return [V("exits_at_seventh", "'and in the seventh he "
                      "shall go out' — in any case: sickness owes no "
                      "make-up time (up to three years; four is as "
                      "six; and light tasks count as service — "
                      "Kiddushin 17a:1-4)", machine_claim="EX21-25",
                      **SC)]
        if q == "slave_resale":
            return [V("theft_yes_fine_no", "'sold for his THEFT' "
                      "(22:2) — for the principal, never the double "
                      "or conspiring-testimony; and once per theft "
                      "(twice only for two thefts — Rava, Kiddushin "
                      "18a:9)", machine_claim="EX21-25", **SC)]
        return None

    # -------------------------------------------------- designation
    DS = _EX("Kiddushin 19a:3-9 (Reish Lakish's dilemma; R. Yannai; "
             "Abaye son of R. Abbahu's ye'adah/ya'adah read)",
             "Exod.21.8-9 (exo_21_the_ordinances, EX21-25)")

    def rule_designation(case):
        q = case.get("query")
        if q == "designation_consent":
            return [V("consent_required", "יְעָדָהּ ('designate her') "
                      "read יְדָעָהּ-wise as HE MUST INFORM HER — "
                      "consent in the word's own letters (Abaye son "
                      "of R. Abbahu; the M-16 revocalization read)",
                      machine_claim="EX21-25", **DS)]
        if q == "designation_minor_son":
            return [V("adult_only", "R. Yannai: designation applies "
                      "only to an adult man BECAUSE only with "
                      "consent — the minor-son dilemma lands on the "
                      "consent rule (Kiddushin 19a:7)",
                      machine_claim="EX21-25", **DS)]
        return None

    # -------------------------------------------- maidservant family
    MF = _EX("Sotah 23b:9 (if a MAN sells) + Bekhorot 50b:7 (without "
             "money) + Yevamot 22b:5 + 70a:5 (the matrilineal reach) "
             "+ Temurah 25b:3-4 (the freed fetus)",
             "Exod.21.4 + 21.7 + 21.11 (exo_21_the_ordinances, "
             "EX21-25; the standing L4-02 matrilineal seat credited)")

    def rule_maidservant(case):
        q = case.get("query")
        if q == "daughter_sale_power":
            return [V("father_only", "'if a MAN sells his daughter' "
                      "(21:7) — the father sells, the mother cannot "
                      "(Sotah 23b:9)", machine_claim="EX21-25", **MF)]
        if q == "maidservant_exit_money":
            return [V("dinar_minimum", "Beit Shammai: a dinar — the "
                      "betrothal-money floor derived from 'out for "
                      "nothing, WITHOUT MONEY' (21:11: no money for "
                      "THIS master, money for another)",
                      authority="Beit Shammai",
                      machine_claim="EX21-25", **MF),
                    V("perutah_minimum", "Beit Hillel: a perutah",
                      authority="Beit Hillel",
                      machine_claim="EX21-25", **MF)]
        if q == "slave_lineage_reach":
            return [V("mother_only", "'the wife and her children "
                      "shall be her master's' (21:4) — the slave "
                      "disqualifies by his BED, never his SEED "
                      "(Yevamot 70a:5); no levirate brotherhood "
                      "(22b:5); Rava reads the same clause freeing "
                      "the fetus with the freed mother (Temurah "
                      "25b:4) — the standing L4-02 seat's reach "
                      "measured", machine_claim="L4-02 + EX21-25",
                      **MF)]
        return None

    # ---------------------------------------------- day-or-two
    DT = _EX("Bava Batra 50a:7-50b:3 (the four-way baraita)",
             "Exod.21.21 (exo_21_the_ordinances, EX21-25)")

    def rule_day_or_two(case):
        if case.get("query") != "day_or_two_holder":
            return None
        return [V("first_master", "R. Meir: use-ownership IS "
                  "ownership — the seller within his thirty days",
                  authority="R. Meir", machine_claim="EX21-25", **DT),
                V("second_master", "R. Yehuda: 'he is his MONEY' — "
                  "the buyer", authority="R. Yehuda",
                  machine_claim="EX21-25", **DT),
                V("both_included", "R. Yosei: the use-vs-thing "
                  "question is UNCERTAIN, and capital doubt is "
                  "lenient — both exempt from execution",
                  authority="R. Yosei", machine_claim="EX21-25",
                  **DT),
                V("neither_included", "R. Elazar: 'his money' — "
                  "wholly his: neither qualifies, both executed",
                  authority="R. Elazar", machine_claim="EX21-25",
                  **DT)]

    # ------------------------------------------------ the burglar
    BG = _EX("Sanhedrin 72a:15-72b:12 (the two baraitot resolved at "
             "the father; Shabbat; the pursuer status; the location "
             "extension)",
             "Exod.22.1-2 (exo_22_property_social, EX22-01 the "
             "tunneler seat; EX22-15 — seated F-052)")

    def rule_burglar(case):
        q = case.get("query")
        if q == "burglar_hostility":
            return [V("doubt_kills_except_father", "'if the sun is "
                      "risen' is a METAPHOR — clear as the sun: the "
                      "two baraitot resolve at kinship (72b:1): a "
                      "FATHER breaking into his son's house is "
                      "presumed merciful — kill only on certainty; "
                      "anyone else — doubt kills; the metaphor itself was "
                      "ANTICIPATED — EX22-01 holds R. Yishmael's "
                      "peace-clarity read with Onkelos's eye-of-witnesses",
                      machine_claim="EX22-01 + EX22-15", **BG)]
        if q == "burglar_shabbat":
            return [V("applies_and_rescue_stands", "both clauses run "
                      "on Shabbat — and Rav Sheshet: if the wall "
                      "fell ON him on Shabbat, CLEAR THE PILE: the "
                      "kill-license is a state that lapses, not a "
                      "status — the rescue duty survives (72b:3-5)",
                      machine_claim="EX22-15", **BG)]
        if q == "burglar_killer_scope":
            return [V("anyone_any_death", "'and is smitten' — by ANY "
                      "person (the burglar is a PURSUER, anyone "
                      "saves the householder); 'and dies' — by any "
                      "death (needed because murderer + blood-"
                      "redeemer are two-verses-as-one and teach no "
                      "principle — the meta-rule named, 72b:8-10)",
                      machine_claim="EX22-15", **BG)]
        if q == "burglar_location_scope":
            return [V("beyond_the_breach", "'found' — roof, "
                      "courtyard, enclosure too; 'breaking in' is "
                      "the common case — or: HIS BREAKING IN IS HIS "
                      "FOREWARNING, elsewhere a warning is owed "
                      "(both baraitot carried, 72b:11-12)",
                      machine_claim="EX22-15", **BG)]
        return None

    # ------------------------------------------- the striving men
    SM = _EX("Sanhedrin 74a:2-4 (R. Yonatan ben Shaul) + 79a:10-11 "
             "(the transfer dispute; Rebbi's money reading) + Bava "
             "Kamma 43a:4 (Rav Pappa) + Arakhin 7a:11-13",
             "Exod.21.22-23 (exo_21_the_ordinances, EX21-24 — "
             "seated F-053)")

    def rule_striving(case):
        q = case.get("query")
        if q == "pursuer_limb_rule":
            return [V("killer_executed", "one who could save the "
                      "pursued by a LIMB and killed instead is a "
                      "murderer (R. Yonatan ben Shaul) — proven from "
                      "our verse: the striving men strive TO KILL, "
                      "yet the fetus-payment stands exactly where "
                      "the limb sufficed (74a:3-4)",
                      machine_claim="EX21-24", **SM)]
        if q == "transferred_intent_liability":
            return [V("liable", "the Rabbis: meant this one, killed "
                      "that one — liable; 'if there is a tragedy, "
                      "life for life'", authority="the Rabbis",
                      machine_claim="EX21-24", **SM),
                    V("monetary_only", "R. Shimon exempts — and "
                      "Rebbi reads 'life for life' as MONETARY "
                      "restitution by the giving-term (79a:11)",
                      authority="R. Shimon with Rebbi's reading",
                      machine_claim="EX21-24", **SM)]
        if q == "offspring_payment_recipient":
            return [V("the_father", "Rav Pappa: בַּעַל read as the "
                      "one who FATHERED — the payment his, even "
                      "unmarried, even divorced (Bava Kamma 43a:4)",
                      machine_claim="EX21-24", **SM)]
        if q == "condemned_pregnant_delay":
            return [V("not_delayed", "the court does not wait — "
                      "though our verse makes the fetus the "
                      "husband's money, 'both of them' adds the "
                      "fetus to her sentence (Arakhin 7a:12-13); "
                      "the travailing-chair exception stands",
                      machine_claim="EX21-24", **SM)]
        return None

    # ---------------------------------------------- striker penalties
    SP = _EX("Sanhedrin 84b:5 (strikes-and-dies) + 52b:13 (the "
             "avenged sword) + 78a:18-19 (R. Nechemya) + 85b:10 "
             "(the dead father) + Makkot 8b:14 + Bava Kamma "
             "90b:14-15",
             "Exod.21.12-20 (exo_21_the_ordinances, EX21-23)")

    def rule_striker(case):
        q = case.get("query")
        if q == "parent_striker_element":
            return [V("wound_without_death", "wherever 'strikes' is "
                      "written WITHOUT 'and he dies,' death is not "
                      "meant (21:12's own pairing) — the "
                      "parent-striker (21:15) is liable for a mere "
                      "wound, by strangulation (84b:5)",
                      machine_claim="EX21-23", **SP)]
        if q == "slave_killer_mode":
            return [V("the_sword", "'he shall be AVENGED' (21:20) — "
                      "vengeance decoded by Leviticus 26:25's "
                      "avenging SWORD; the murderer's decapitation "
                      "rides it, edge not point (52b:13-14)",
                      machine_claim="EX21-23", **SP)]
        if q == "unwitting_parent_wound":
            return [V("no_exile", "Rava: exile belongs to the "
                      "unintentional MURDERER alone — the unwitting "
                      "parent-wounder is excluded though his "
                      "intentional act would execute (Makkot 8b:14)",
                      machine_claim="EX21-23", **SP)]
        if q == "weapon_assessment":
            return [V("submitted_to_assembly", "Shimon HaTimni: "
                      "stone-or-fist (21:18) defines the class "
                      "SUBMITTED to the assembly and the witnesses "
                      "— the item must be assessable",
                      authority="Shimon HaTimni",
                      machine_claim="EX21-23", **SP),
                    V("witnesses_suffice", "R. Akiva: the court "
                      "never saw the blow either — witnesses "
                      "testify to the item as to the striking",
                      authority="R. Akiva", machine_claim="EX21-23",
                      **SP)]
        if q == "eased_then_died":
            return [V("liable", "assessed to die, eased, then died "
                      "— liable (the first opinion)",
                      authority="the first opinion",
                      machine_claim="EX21-23", **SP),
                    V("exempt_basis_found", "R. Nechemya exempts — "
                      "'if he rises and walks outside' (21:19) is "
                      "his verse: there is a basis for the matter",
                      authority="R. Nechemya",
                      machine_claim="EX21-23", **SP)]
        if q == "dead_parent_curse":
            return [V("liable_after_death", "R. Yoshiya derives it "
                      "from 21:17's own clause; R. Yonatan spends "
                      "that clause on the daughter and the "
                      "in-between cases — both assignments recorded "
                      "(85b:9-11)", machine_claim="EX21-23", **SP)]
        return None

    # ------------------------------------------- goring-ox riders
    GO = _EX("Bava Kamma 44b:16 (the seven tokens) + 43a:9-11 (the "
             "stoning linkage) + 11a:4 (the carcass) + 71a:8-9 (the "
             "agency bend) + Sanhedrin 78a:14-15 + 79b:13 + Gittin "
             "42b:7-8",
             "Exod.21.28-37 (exo_21_the_ordinances, EX21-24; the "
             "law-era L28/L29/L37 claims credited beneath)")

    def rule_goring_riders(case):
        q = case.get("query")
        if q == "ox_token_census":
            return [V("six_inclusions", "SEVEN 'ox' tokens in "
                      "21:28-32 — six inclusions: the woman's, the "
                      "orphans', the steward's, the desert ox, the "
                      "consecrated, the dead convert's (an "
                      "ink-census row)", authority="the first "
                      "opinion", machine_claim="EX21-24", **GO),
                    V("three_ownerless_exempt", "R. Yehuda carves "
                      "the ownerless three out — even consecrated "
                      "AFTER the goring (Rav Huna's extension)",
                      authority="R. Yehuda", machine_claim="EX21-24",
                      **GO)]
        if q == "tereifa_ox_trial":
            return [V("ox_liable_owner_exempt", "Rava: wherever we "
                      "cannot read 'its owner shall also die' we do "
                      "not read 'the ox shall be stoned' — the "
                      "flawed OWNER exempts his ox; the flawed ox "
                      "itself still stands trial",
                      authority="Rava", machine_claim="EX21-24",
                      **GO),
                    V("both_exempt", "Rav Ashi extends the "
                      "juxtaposition to the ox itself",
                      authority="Rav Ashi", machine_claim="EX21-24",
                      **GO)]
        if q == "intermingled_ox_verdict":
            return [V("all_exempt", "the Rabbis: as the owner's "
                      "verdict needs his presence, the ox's needs "
                      "its own — unidentifiable, all exempt",
                      authority="the Rabbis", machine_claim="EX21-24",
                      **GO),
                    V("vaulted_chamber", "R. Yehuda: gather them to "
                      "the vaulted chamber", authority="R. Yehuda",
                      machine_claim="EX21-24", **GO)]
        if q == "unintentional_kill_payments":
            return [V("both_ride_the_stoning", "the thirty (Reish "
                      "Lakish) and the ransom (Rabba) both RIDE the "
                      "stoning — no stoning, no payment; Abaye's "
                      "admission objection recorded beside it "
                      "(43a:9-11)", machine_claim="EX21-24", **GO)]
        if q == "half_freed_thirty":
            return [V("half_to_master", "the half-slave "
                      "half-freeman killed by an ox: HALF a penalty "
                      "to the master, half a ransom to his heirs "
                      "(Gittin 42b:8; the manumission-lacking "
                      "master's status the dilemma)",
                      machine_claim="EX21-24", **GO)]
        if q == "pit_carcass_duty":
            return [V("owner_of_pit_raises", "'he shall restore "
                      "money... and the carcass' — the carcass "
                      "rides the restore-verb: the pit-owner raises "
                      "it to its owner (Bava Kamma 11a:4)",
                      machine_claim="EX21-24", **GO)]
        if q == "theft_agency":
            return [V("liable_through_agent", "'slaughter it OR "
                      "sell it' — as selling runs through another, "
                      "so slaughtering: the ONE bend in "
                      "no-agent-in-sin (Rava; the schools' 'or' and "
                      "tachat routes beside it, 71a:8-9)",
                      machine_claim="EX21-24", **GO)]
        return None

    # ---------------------------------------------- abduction
    AB = _EX("Sanhedrin 85b:21-86a:17 (the scope closure; the "
             "teiku; the context middah)",
             "Exod.21.16 + 20.13 (exo_21_the_ordinances, EX21-26 — "
             "seated F-055; also block 5's docket)")

    def rule_abduction(case):
        q = case.get("query")
        if q == "abduction_gender_scope":
            return [V("all_combinations", "Deut 24:7's male abductor "
                      "× our 21:16's unspecified — and 'that "
                      "abductor shall die' closes the grid: man or "
                      "woman abducting man or woman (85b:22-23)",
                      machine_claim="EX21-26", **AB)]
        if q == "abduction_exploitation_edge":
            return [V("teiku", "reclining on the sleeping man; "
                      "standing the pregnant woman against the wind "
                      "— is that exploitation? THE DILEMMA STANDS "
                      "UNRESOLVED (85b:21): the machine returns the "
                      "tradition's own recorded open state",
                      machine_claim="EX21-26", **AB)]
        if q == "decalogue_theft_object":
            return [V("persons_by_context", "'you shall not steal' "
                      "(20:13) speaks of PERSONS — a matter derived "
                      "from its context (capital neighbors), the "
                      "middah NAMED; the mirror baraita runs Lev "
                      "19:11 to property by ITS context (86a:16-17)",
                      machine_claim="EX21-26", **AB)]
        if q == "abduction_of_slave":
            return [V("exempt", "'from the children of Israel' — "
                      "the slave and the half-slave excluded (the "
                      "Rabbis, 86a:14)", machine_claim="EX21-26",
                      **AB)]
        return None

    return {
        "forewarning_derivation": {"fn": rule_forewarning},
        "slave_clock_law": {"fn": rule_slave_clock},
        "designation_law": {"fn": rule_designation},
        "maidservant_family": {"fn": rule_maidservant},
        "day_or_two_authority": {"fn": rule_day_or_two},
        "burglar_law": {"fn": rule_burglar},
        "striving_men_machine": {"fn": rule_striving},
        "striker_penalties": {"fn": rule_striker},
        "goring_ox_riders": {"fn": rule_goring_riders},
        "abduction_machine": {"fn": rule_abduction},
    }
