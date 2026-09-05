# levirate_rules.py — round 33, LEVIRATE, SEED, AND UNIONS (Genesis
# exam block 4 of 12, 2026-09-04). Read-source:
# logic/oral_triage/genesis_block_levirate_2026-09-04.md.


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    LN = _EX("Yevamot 24a:5-7",
             "Gen 48:6 (gen_71, G71-28 / F-124)")
    EO = _EX("Yevamot 34b:2-5",
             "Gen 38:9-10 (gen_61, G61-18 / F-125)")
    PN = _EX("Yevamot 63b:15-18",
             "Gen 9:6-7 (gen_21, G21-18 / F-126)")
    SD = _EX("Yevamot 42a:6; Yevamot 100b:9 (standing)",
             "Gen 17:7 (gen_33, G33-27 standing)")
    IE = _EX("Yevamot 88a:12-14",
             "Gen 42:8 (gen_65, G65-33 / F-127)")

    def rule_levirate_name(case):
        if case.get("query") == "levirate_name_meaning":
            return [V("inheritance_by_name_analogy",
                      "'he shall arise on the NAME of his brother' "
                      "(Deut 25:6) — you say for INHERITANCE, or "
                      "only for the literal name (call him Yosef, "
                      "call him Yochanan)? נאמר כאן יקום על שם אחיו "
                      "ונאמר להלן על שם אחיהם יקראו בנחלתם ('name is "
                      "said here, and there: on the name of their "
                      "brothers they shall be called IN THEIR "
                      "INHERITANCE,' Gen 48:6) — as the name there "
                      "is inheritance, so here: the levirate "
                      "'name' is the estate, resolved on our "
                      "verse's own token — Yevamot 24a:5-6 (the "
                      "frame beside: the eldest performs; the "
                      "aylonit excluded by 'that she bears'; the "
                      "eunuch by 'his name is erased')",
                      authority="the baraita's verbal analogy",
                      machine_claim="G71-28", **LN)]
        return None

    def rule_er_onan_file(case):
        q = case.get("query")
        if q == "onan_act_source":
            return [V("destroyed_on_ground",
                      "Onan's act is WRITTEN: והיה אם בא אל אשת אחיו "
                      "ושחת ארצה ('when he came to his brother's "
                      "wife he DESTROYED on the ground,' Gen 38:9) — "
                      "the like-and-not-like frame: the nursing "
                      "baraita's practice is 'as the act of Er and "
                      "Onan' in outcome, not in manner — Yevamot "
                      "34b:2-3",
                      authority="the gemara",
                      machine_claim="G61-18", **EO)]
        if q == "er_act_source":
            return [V("same_death_inference",
                      "Er whence? Rav Nachman bar Yitzchak: וימת גם "
                      "אתו ('and He killed him TOO,' Gen 38:10) — אף "
                      "הוא באותו מיתה מת ('he too died the SAME "
                      "death'): the matched deaths prove the "
                      "matched act; the motives split — Onan, that "
                      "the seed not be his; Er, that she not "
                      "conceive and her beauty dim — Yevamot 34b:4",
                      authority="Rav Nachman bar Yitzchak",
                      machine_claim="G61-18", **EO)]
        return None

    def rule_procreation_neglect(case):
        if case.get("query") == "procreation_neglect_grade":
            return [V("sheds_blood",
                       "R. Eliezer: whoever does not engage in "
                       "procreation is AS ONE WHO SHEDS BLOOD — "
                       "שפך דם האדם ('who sheds man's blood,' Gen "
                       "9:6) with ואתם פרו ורבו ('and YOU, be "
                       "fruitful and multiply,' 9:7) written "
                       "immediately after: the juxtaposition IS "
                       "the derivation — Yevamot 63b:16",
                       authority="R. Eliezer",
                       machine_claim="G21-18", **PN),
                    V("diminishes_image",
                      "R. Yaakov: as one who DIMINISHES THE IMAGE — "
                      "כי בצלם אלהים עשה את האדם ('for in the image "
                      "of God He made man,' 9:6) with 'and you, be "
                      "fruitful' after it — Yevamot 63b:17",
                      authority="R. Yaakov",
                      machine_claim="G21-18", **PN),
                    V("both_grades",
                      "Ben Azzai: as one who sheds blood AND "
                      "diminishes the image — both juxtapositions "
                      "read together; with his own recorded "
                      "exception standing beside ('what shall I "
                      "do — my soul desires Torah; the world can "
                      "persist through others,' 63b:18) — Yevamot "
                      "63b:17-18",
                      authority="Ben Azzai",
                      machine_claim="G21-18", **PN)]
        return None

    def rule_seed_distinction(case):
        q = case.get("query")
        if q == "remarriage_wait":
            return [V("three_month_distinction",
                      "the wait between husbands: לזרעך אחריך ('to "
                      "your seed AFTER YOU,' Gen 17:7) — the first "
                      "husband's seed must be DISTINGUISHABLE from "
                      "the second's: Shmuel's three months — "
                      "Yevamot 42a:6; STANDING SEAT: G33-27 has "
                      "held the three family laws of the clause "
                      "since the reading",
                      authority="Shmuel",
                      machine_claim="G33-27 (standing)", **SD)]
        if q == "union_ban":
            return [V("gentile_slave_excluded",
                      "להיות לך לאלהים ולזרעך אחריך ('to be God to "
                      "you and to your seed after you,' Gen 17:7) — "
                      "the clause grounding the ban on unions with "
                      "one whose seed is not 'after you': the "
                      "gentile and the slave — Yevamot 100b:9; "
                      "STANDING SEAT: G33-27",
                      authority="the sugya",
                      machine_claim="G33-27 (standing)", **SD)]
        return None

    def rule_identity_evidence(case):
        if case.get("query") == "beard_recognition":
            return [V("beard_signature_rule",
                      "the missing-husband case: two witnesses say "
                      "'we were with him from his leaving until "
                      "now — it is YOU who do not recognize him' — "
                      "דכתיב ויכר יוסף את אחיו והם לא הכרהו ('as it "
                      "is written: Joseph RECOGNIZED his brothers, "
                      "and they did not recognize him,' Gen 42:8); "
                      "Rav Chisda: he left without the beard's "
                      "signature and returned with it — "
                      "recognizability itself is EVIDENCE with a "
                      "recorded aging parameter — Yevamot 88a:12-13",
                      authority="Rav Chisda",
                      machine_claim="G65-33", **IE)]
        return None

    return {
        "levirate_name": {"fn": rule_levirate_name,
                          "tractate": "Yevamot"},
        "er_onan_file": {"fn": rule_er_onan_file,
                         "tractate": "Yevamot"},
        "procreation_neglect": {"fn": rule_procreation_neglect,
                                "tractate": "Yevamot"},
        "seed_distinction": {"fn": rule_seed_distinction,
                             "tractate": "Yevamot"},
        "identity_evidence": {"fn": rule_identity_evidence,
                              "tractate": "Yevamot"},
    }
