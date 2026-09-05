# courts_gen_rules.py — round 35, THE COURTS' GENESIS LAYER
# (Genesis exam block 6 of 12, 2026-09-04). Read-source:
# logic/oral_triage/genesis_block_courts_2026-09-04.md.


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    JA = _EX("Sanhedrin 5a:5-7",
             "Gen 49:10 (gen_72, G72-35 / F-136)")
    DC = _EX("Makkot 9a:9-11; Ketubot 30a:5-7; Sanhedrin 46b:20-22",
             "Gen 20:6 + 42:38 + 23:2 (gen_36 G36-21 / F-138; "
             "gen_65 G65-35 / F-140; gen_39 G39-36 / F-137)")
    SB = _EX("Makkot 11b:1-2; Moed Katan 18a:3-5",
             "Gen 43:9 + 22:5 (gen_66 G66-36 / F-139; gen_38 "
             "G38-40 / F-141)")
    AP = _EX("Avodah Zarah 53b:12-13",
             "Gen 11:1-9 (gen_25, G25-17 / F-142)")
    FC = _EX("Sanhedrin 29a:33-34; 37b:12; Kiddushin 61b:9 "
             "(standing)",
             "Gen 3:3 + 4:7 + 4:14-16 (gen_10 prose; gen_12 "
             "G12-15, G12-19)")

    def rule_judicial_authority(case):
        if case.get("query") == "scepter_license":
            return [V("exilarch_judging_license",
                      "לא יסור שבט מיהודה ('the SCEPTER shall not "
                      "depart from Judah,' Gen 49:10) — אלו ראשי "
                      "גליות שבבבל ('these are the EXILARCHS in "
                      "Babylon who rule Israel with the staff'); "
                      "'the lawgiver from between his feet' — the "
                      "descendants of Hillel who teach Torah "
                      "publicly: the verse read as the license "
                      "GEOGRAPHY of judicial authority (staff here, "
                      "lawgiver there; authority from here serves "
                      "there), with Rabbah bar Chana's "
                      "license-in-hand case beside — Sanhedrin "
                      "5a:5-7",
                      authority="the baraita",
                      machine_claim="G72-35", **JA)]
        return None

    def rule_death_court_files(case):
        q = case.get("query")
        if q == "heaven_jurisdiction_token":
            return [V("heavens_hand_by_to_me",
                      "'you shall DIE for the woman you took' (Gen "
                      "20:3) — by man's hand? No: by HEAVEN'S — "
                      "דיקא נמי דכתיב מחטוא לי ('precisely so, for "
                      "it is written: from sinning AGAINST ME,' "
                      "20:6): the dative token assigns the "
                      "jurisdiction; the Joseph counter ('I would "
                      "sin against God' — yet man's court) resolved "
                      "by judgment-given-over-to-man — Makkot "
                      "9a:9-11",
                      authority="Rav Chisda against Rava's "
                                "challenge",
                      machine_claim="G36-21", **DC)]
        if q == "ason_analogy":
            return [V("heaven_ason_exempts_too",
                      "R. Nechunya ben HaKanah's rule by the ason "
                      "pair: נאמר אסון בידי אדם ('calamity is said "
                      "by the hand of MAN,' Exod 21:23) ונאמר אסון "
                      "בידי שמים ('and calamity is said by the "
                      "hand of HEAVEN' — 'lest a calamity befall "
                      "him,' Gen 42:38): as man's-hand ason exempts "
                      "from payment, so Heaven's — the verbal "
                      "analogy between the two ason tokens, with "
                      "Rav Adda's lions-and-thieves challenge "
                      "answered (Jacob warned about everything) — "
                      "Ketubot 30a:5-7",
                      authority="Abaye stating R. Nechunya ben "
                                "HaKanah's reason",
                      machine_claim="G65-35", **DC)]
        if q == "eulogy_subject_question":
            return [V("first_proof_deflected",
                      "is the eulogy the honor of the LIVING or of "
                      "the DEAD? The sugya's FIRST proof is our "
                      "verse: ויבא אברהם לספד לשרה ולבכתה ('Abraham "
                      "came to EULOGIZE Sarah and to weep for her,' "
                      "Gen 23:2) — if for the living's honor, would "
                      "they delay Sarah for Abraham's honor? — "
                      "deflected: Sarah herself is pleased that "
                      "Abraham is honored through her; the question "
                      "runs on — our verse opens the file and its "
                      "deflection is kept — Sanhedrin 46b:20-22",
                      authority="the sugya, the proof and its "
                                "deflection both recorded",
                      machine_claim="G39-36", **DC)]
        return None

    def rule_speech_binding(case):
        q = case.get("query")
        if q == "conditional_ban_release":
            return [V("binds_absent_release",
                      "Rav Yehuda citing Rav: נידוי על תנאי צריך "
                      "הפרה ('a ban on CONDITION requires RELEASE') "
                      "— from JUDAH: 'if I do not bring him to you, "
                      "I will have sinned all my days' (Gen 43:9) — "
                      "and though he BROUGHT him, Judah's bones "
                      "rolled in their coffin all forty wilderness "
                      "years until Moses prayed: the conditional "
                      "self-ban bound even after the condition was "
                      "met — Makkot 11b:1-2",
                      authority="Rav Yehuda citing Rav, with R. "
                                "Shmuel bar Nachmani's narrative "
                                "proof",
                      machine_claim="G66-36", **SB)]
        if q == "lips_covenant":
            return [V("speech_shapes_outcome",
                      "R. Yochanan: whence that ברית כרותה לשפתים "
                      "('a covenant is CUT TO THE LIPS')? — 'sit "
                      "here with the donkey, and I and the lad "
                      "will go... and worship AND RETURN to you' "
                      "(Gen 22:5) — ואיסתייעא מלתא דהדור תרוייהו "
                      "('and it came to pass: BOTH returned'): the "
                      "spoken plural shaped the outcome on the "
                      "mountain of the binding — Moed Katan "
                      "18a:3-4",
                      authority="R. Yochanan",
                      machine_claim="G38-40", **SB)]
        return None

    def rule_annulment_precedent(case):
        if case.get("query") == "idol_annulment_precedent":
            return [V("peacetime_abandonment_annuls",
                      "the Mishnah: an idol its worshipers "
                      "abandoned in PEACETIME is permitted, in "
                      "wartime forbidden; Rav: בית נמרוד ('the "
                      "HOUSE OF NIMROD' — the dispersion's tower, "
                      "Gen 11:1-9) is as peacetime-abandoned and "
                      "PERMITTED — though the Merciful scattered "
                      "them like wartime, אי בעיא למיהדר הדור ('had "
                      "they wished to return, they could have "
                      "returned'): not returning IS the annulment — "
                      "Avodah Zarah 53b:12-13",
                      authority="R. Yirmiya bar Abba citing Rav",
                      machine_claim="G25-17", **AP)]
        return None

    def rule_form_credits(case):
        q = case.get("query")
        if q == "adds_subtracts_rule":
            return [V("eden_seat_of_the_rule",
                      "כל המוסיף גורע ('whoever ADDS, SUBTRACTS') — "
                      "Chizkiya's seat: Eve's added 'nor touch it' "
                      "(Gen 3:3) against the command as given — the "
                      "hermeneutic law's Eden exemplar; STANDING: "
                      "gen_10's own prose has carried the rule "
                      "since derivation, and the ink block (round "
                      "20) read the sugya in full with its two "
                      "letter-arithmetic companions — Sanhedrin "
                      "29a:33-34",
                      authority="Chizkiya",
                      machine_claim="gen_10 prose (standing)", **FC)]
        if q == "exile_half_atonement":
            return [V("half_remitted_by_ink_delta",
                      "EXILE ATONES HALF: the sentence was נע ונד "
                      "('wandering AND roaming,' Gen 4:12,14) — the "
                      "settlement notice records only וישב בארץ נוד "
                      "('and he dwelt in the land of NOD,' 4:16): "
                      "one term served, one remitted — the ink "
                      "delta IS the derivation; STANDING SEAT: "
                      "G12-19 has held the half-decree reading "
                      "since the reading — Sanhedrin 37b:12",
                      authority="the sugya",
                      machine_claim="G12-19 (standing)", **FC)]
        if q == "doubled_condition_form":
            return [V("r_meir_doubled_condition",
                      "R. Meir's law of legal FORM — a condition "
                      "must be DOUBLED (tenai kaful, stated with "
                      "both arms): אם תיטיב ('IF you do well') and "
                      "ואם לא תיטיב ('AND IF you do not,' Gen 4:7): the "
                      "first doubled condition in the canon as the "
                      "form's exemplar; STANDING SEAT: G12-15 holds "
                      "the clause as therapeutic program AND law of "
                      "form — Kiddushin 61b:9",
                      authority="R. Meir",
                      machine_claim="G12-15 (standing)", **FC)]
        return None

    return {
        "judicial_authority": {"fn": rule_judicial_authority,
                               "tractate": "Sanhedrin"},
        "death_court_files": {"fn": rule_death_court_files,
                              "tractate": "Makkot"},
        "speech_binding": {"fn": rule_speech_binding,
                           "tractate": "Makkot"},
        "annulment_precedent": {"fn": rule_annulment_precedent,
                                "tractate": "Avodah Zarah"},
        "form_credits": {"fn": rule_form_credits,
                         "tractate": "Sanhedrin"},
    }
