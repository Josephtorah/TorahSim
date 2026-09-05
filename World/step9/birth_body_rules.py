# birth_body_rules.py — round 39, BIRTH AND THE BODY (Genesis exam
# block 10 of 12, 2026-09-04). Read-source:
# logic/oral_triage/genesis_block_birth_2026-09-04.md.


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    PF = _EX("Niddah 8b:16-18, 28a:8-10",
             "Gen 38:24 + 38:28 (gen_61, G61-20 / F-169)")
    BP = _EX("Bekhorot 46b:1-3; Sotah 45b:16-18",
             "Gen 7:22 (gen_18_the_rise, G18-11 / F-170)")
    LL = _EX("Niddah 31a:23-25",
             "Gen 46:15 (gen_69, G69-31 / F-171)")
    PO = _EX("Niddah 70b:6-8",
             "Gen 19:26 (gen_35, G35-28 / F-172)")
    DC = _EX("Bava Kamma 49a:4-6",
             "Gen 22:5 (gen_38, G38-43 / F-173)")
    BC = _EX("Niddah 22b:13; 25a:9; Bava Kamma 91b:8; Taanit "
             "22b:11 (standing)",
             "Gen 2:7 + 3:21 + 9:5 (G08-25, G11-24, G21-10, "
             "G08-19 standing)")

    def rule_pregnancy_file(case):
        q = case.get("query")
        if q == "pregnancy_recognition":
            return [V("three_months_by_tamar",
                      "when is the fetus recognized? Sumchos in R. "
                      "Meir's name: THREE MONTHS — and though there "
                      "is no proof, there is a REMEMBRANCE: ויהי "
                      "כמשלש חדשים ('and it came to pass, about "
                      "THREE MONTHS later,' Gen 38:24 — Tamar's "
                      "showing); the zekher-grade weighed at 8b:18 "
                      "(a strong support, since term varies) — "
                      "Niddah 8b:17-18",
                      authority="Sumchos in R. Meir's name",
                      machine_claim="G61-20", **PF)]
        if q == "returned_hand":
            return [V("mother_birth_impure",
                      "Rav Huna: the fetus put out its hand and "
                      "drew it back — the mother is BIRTH-IMPURE: "
                      "ויהי בלדתה ויתן יד ('and it came to pass IN "
                      "HER BIRTHING, that he put out a hand,' Gen "
                      "38:28 — Zerach's scarlet thread): the "
                      "emergence clause read as birth's onset; Rav "
                      "Nachman's calibration (concern yes, "
                      "pure-days only at majority exit) — Niddah "
                      "28a:9-10",
                      authority="Rav Huna with Rav Nachman's "
                                "calibration",
                      machine_claim="G61-20", **PF)]
        return None

    def rule_body_predicates(case):
        q = case.get("query")
        if q == "nose_firstborn_law":
            return [V("head_counts_by_nostril_breath",
                      "Shmuel: the head does not exempt in "
                      "nonviable births — כל אשר נשמת רוח חיים "
                      "באפיו ('all in whose NOSTRILS was the breath "
                      "of the spirit of life,' Gen 7:22): where the "
                      "breath is in the nostrils, the emerging head "
                      "COUNTS; where not, it does not — the "
                      "firstborn law's nose-predicate, the scan's "
                      "third recorded call site — Bekhorot 46b:1-2",
                      authority="Shmuel",
                      machine_claim="G18-11", **BP)]
        if q == "nose_corpse_law":
            return [V("life_measured_at_the_nose",
                      "even Abba Shaul (formed from the navel) "
                      "concedes: for the matter of LIFE all agree — "
                      "באפיה הוא ('it is in the NOSTRILS'), as "
                      "written 'all in whose nostrils was the "
                      "breath of life' (Gen 7:22): the corpse "
                      "measured FROM THE NOSE for the nearest-city "
                      "rite — the same token's second law — Sotah "
                      "45b:16-17",
                      authority="the sugya reconciling Abba Shaul",
                      machine_claim="G18-11", **BP)]
        return None

    def rule_lineage_ledger(case):
        if case.get("query") == "sex_determination_ledger":
            return [V("males_hung_on_females",
                      "the early formulation had no proof until R. "
                      "TZADOK came and explained it from the "
                      "ledger's own ink: אלה בני לאה ('these are "
                      "the SONS of Leah') and ואת דינה בתו ('and "
                      "DINAH his DAUGHTER,' Gen 46:15) — תלה "
                      "הזכרים בנקבות ונקבות בזכרים ('he hung the "
                      "males on the females and the females on the "
                      "males'): the descent roster's own gender "
                      "attributions as the rule's proof — Niddah "
                      "31a:23-24",
                      authority="R. Tzadok",
                      machine_claim="G69-31", **LL)]
        return None

    def rule_purity_objects(case):
        if case.get("query") == "salt_pillar_purity":
            return [V("pillar_does_not_defile",
                      "does Lot's wife defile? — מת מטמא ואין נציב "
                      "מלח מטמא ('a CORPSE defiles, and a pillar of "
                      "SALT does not defile,' on Gen 19:26): the "
                      "object-class question posed and answered on "
                      "our verse's own artifact, beside the "
                      "revived-son twin — Niddah 70b:7-8",
                      authority="the recorded answer to the three "
                                "questions",
                      machine_claim="G35-28", **PO)]
        return None

    def rule_damages_class(case):
        if case.get("query") == "fetus_damages_class":
            return [V("paid_as_animal_loss",
                      "Rav Pappa: an ox that gored a slave-woman "
                      "and her children came out — the owner PAYS "
                      "fetus damages, for it is as a pregnant "
                      "she-donkey damaged: שבו לכם פה עם החמור "
                      "('sit here WITH THE DONKEY,' Gen 22:5) — עם "
                      "הדומה לחמור ('a people LIKE the donkey'): "
                      "the tradition's own recorded doctrine, its "
                      "harshness on the page — Bava Kamma 49a:5",
                      authority="Rav Pappa",
                      machine_claim="G38-43", **DC)]
        return None

    def rule_body_credits(case):
        q = case.get("query")
        if q == "miscarriage_form_rule":
            return [V("forming_forming_analogy",
                      "the miscarriage-form question rides the "
                      "forming verb written of the human (Gen 2:7) "
                      "AND the beasts (2:19) — the yatzar-yatzar "
                      "verbal analogy; STANDING SEAT: G08-25 has "
                      "held the birth-impurity derivation since "
                      "the reading — Niddah 22b:13",
                      authority="the sugya",
                      machine_claim="G08-25 (standing)", **BC)]
        if q == "formed_skin_rule":
            return [V("skin_only_for_the_formed",
                      "skin is made only for the FORMED — עור "
                      "('garments of SKIN He made them,' Gen "
                      "3:21); STANDING SEAT: G11-24's garments "
                      "operator holds the row — Niddah 25a:9",
                      authority="the sugya",
                      machine_claim="G11-24 (standing)", **BC)]
        if q == "self_injury_ban":
            return [V("forbidden_courts_split",
                      "SELF-INJURY forbidden: 'from the hand of "
                      "YOUR SOULS I will require your blood' (Gen "
                      "9:5); STANDING SEAT: G21-10 holds the ban "
                      "with the two-courts split — Bava Kamma "
                      "91b:8",
                      authority="R. Elazar",
                      machine_claim="G21-10 (standing)", **BC)]
        if q == "self_affliction_limit":
            return [V("keep_the_soul_alive",
                      "the self-affliction limit: ויהי האדם לנפש "
                      "חיה ('and the man became a LIVING SOUL,' "
                      "Gen 2:7) — keep alive the soul I gave you; "
                      "STANDING: G08-19's nefesh-chayah census "
                      "holds the phrase's whole career — Taanit "
                      "22b:11",
                      authority="the gemara",
                      machine_claim="G08-19 (standing)", **BC)]
        return None

    return {
        "pregnancy_file": {"fn": rule_pregnancy_file,
                           "tractate": "Niddah"},
        "body_predicates": {"fn": rule_body_predicates,
                            "tractate": "Bekhorot"},
        "lineage_ledger": {"fn": rule_lineage_ledger,
                           "tractate": "Niddah"},
        "purity_objects": {"fn": rule_purity_objects,
                           "tractate": "Niddah"},
        "damages_class": {"fn": rule_damages_class,
                          "tractate": "Bava Kamma"},
        "body_credits": {"fn": rule_body_credits,
                         "tractate": "Niddah"},
    }
