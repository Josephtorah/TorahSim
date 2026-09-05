# name_ink_rules.py — round 36, THE NAME AND THE INK (Genesis exam
# block 7 of 12, 2026-09-04). Read-source:
# logic/oral_triage/genesis_block_name_ink_2026-09-04.md.


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    NS = _EX("Shevuot 35b:8-12",
             "Gen 18:3 + 19:18 (gen_34 G34-25 / F-143; gen_35 "
             "G35-27 / F-144)")
    OF = _EX("Shevuot 36a:12-15, 38b:19-23",
             "Gen 9:11-15 + 24:2-3 (gen_22 G22-12 / F-145; gen_40 "
             "G40-35 / F-146)")
    IC = _EX("Chullin 65a:1-2; Nedarim 37b:7-9; Sanhedrin "
             "108b:13-15; Pesachim 7b:13-15; standing seats",
             "Gen 14:4 + 18:5 + 6:18/8:16 + 44:12 + 7:8 + 17:5 "
             "(gen_30 G30-31 / F-148; gen_34 G34-25; gen_16 G16-20 "
             "/ F-149; gen_67 G67-33 / F-147; G17-10, G33-19 "
             "standing)")
    SG = _EX("Bekhorot 55a:21-22",
             "Gen 2:11-14 (gen_08, G08-31 / F-150)")

    def rule_name_sanctity(case):
        q = case.get("query")
        if q == "abraham_names_exception":
            return [V("profane_addressed_to_guests",
                       "all the Names said of Abraham are HOLY — "
                       "חוץ מזה שהוא חול ('except this one, which "
                       "is PROFANE'): ויאמר אדני אם נא מצאתי חן "
                       "('and he said: my lord, if I have found "
                       "favor,' Gen 18:3) — addressed to the "
                       "guests: erasure law drawn token by token "
                       "on our own ink — Shevuot 35b:9",
                       authority="the first tanna",
                       machine_claim="G34-25", **NS),
                    V("holy_even_this",
                      "Chanina the nephew of R. Yehoshua and R. "
                      "Elazar ben Azariah in R. Elazar HaModai's "
                      "name: EVEN THIS is holy — Abraham asked the "
                      "Presence to wait while he served the "
                      "guests: the arm from which 'hospitality is "
                      "greater than receiving the Presence' is "
                      "ruled — Shevuot 35b:10",
                      authority="the pair in R. Elazar HaModai's "
                                "name", **NS)]
        if q == "lot_names_exception":
            return [V("holy_kill_and_revive",
                      "all the Names in the LOT passage are "
                      "profane — except this one, which is HOLY: "
                      "אל נא אדני ('please, no, my Lord,' Gen "
                      "19:18) — מי שיש בידו להמית ולהחיות ('He who "
                      "has power to KILL AND REVIVE — that is the "
                      "Holy One'): the capability test deciding "
                      "the token's sanctity — Shevuot 35b:11",
                      authority="the baraita",
                      machine_claim="G35-27", **NS)]
        return None

    def rule_oath_formula(case):
        q = case.get("query")
        if q == "no_is_oath":
            return [V("doubled_no_doubled_yes",
                      "R. Elazar: לאו שבועה הן שבועה ('NO is an "
                      "oath, and YES is an oath') — no-as-oath "
                      "from ולא יהיה עוד המים למבול ('the waters "
                      "shall NO more become a flood,' Gen 9:15) "
                      "with Isaiah's 'I have SWORN'; and Rava's "
                      "cap: only DOUBLED — as the covenant itself "
                      "doubles the negation (9:11 and 9:15): "
                      "no-no twice, yes-yes twice — Shevuot "
                      "36a:13-14",
                      authority="R. Elazar with Rava's doubling "
                                "condition",
                      machine_claim="G22-12", **OF)]
        if q == "oath_by_the_name":
            return [V("torah_formula_with_object_grasp",
                      "how is the oath administered? Rav Yehuda "
                      "citing Rav: בשבועה האמורה בתורה ('with the "
                      "oath STATED IN THE TORAH') — ואשביעך בה׳ "
                      "אלהי השמים ('and I will make you swear by "
                      "the LORD, God of heaven,' Gen 24:3, "
                      "Abraham's adjuration); and the practical "
                      "point survives even for the sages: צריך "
                      "לאתפושי חפצא בידיה ('he must GRASP AN "
                      "OBJECT in his hand') — the thigh-grasp of "
                      "24:2 as the oath's object protocol, with "
                      "Rava's judge-who-erred rider — Shevuot "
                      "38b:20-23",
                      authority="Rav Yehuda citing Rav, with "
                                "Ravina and Rav Ashi's exchange",
                      machine_claim="G40-35", **OF)]
        return None

    def rule_ink_canon_gen(case):
        q = case.get("query")
        if q == "kedorlaomer_layout":
            return [V("two_words_never_two_lines",
                      "a name the scribe splits — two names? Then "
                      "את כדר לעמר ('Kedorlaomer,' Gen 14:4), which "
                      "the scribe splits in two! Answer: בשתי תיבות "
                      "פסיק להו ('in two WORDS he may split it') "
                      "בשני שיטין לא פסיק להו ('in two LINES he "
                      "may not') — the layout law on our token — "
                      "Chullin 65a:1-2",
                      authority="the sugya",
                      machine_claim="G30-31", **IC)]
        if q == "scribes_adornment":
            return [V("five_adornments_two_ours",
                      "עיטור סופרים ('the scribes' ADORNMENT') — "
                      "the five recorded readings, TWO on our "
                      "verses: אחר תעבורו ('AFTERWARD you shall "
                      "pass on,' Gen 18:5) and the after-she-goes "
                      "clause of Gen 24:55, with Num 12:14 and two "
                      "Psalms seats: the scribes' recorded reading "
                      "layer, catalogued beside mikra sofrim and "
                      "the read-not-written list — Nedarim 37b:7-9",
                      authority="the baraita's catalog",
                      machine_claim="G34-25", **IC)]
        if q == "operand_order_law":
            return [V("separated_entry_rejoined_exit",
                      "law from OPERAND ORDER: the entry — 'you "
                      "and your sons, and your wife and your "
                      "sons' wives' (Gen 6:18, the couples "
                      "SEPARATED); the exit — 'you AND YOUR WIFE, "
                      "your sons AND THEIR WIVES' (8:16, "
                      "REJOINED); R. Yochanan: from here — "
                      "relations were forbidden in the ark; the "
                      "three who transgressed recorded beside — "
                      "Sanhedrin 108b:14-15",
                      authority="R. Yochanan",
                      machine_claim="G16-20", **IC)]
        if q == "found_found_chain":
            return [V("four_link_analogy_chain",
                      "Rav Chisda's chain for the leaven search: "
                      "למדנו מציאה ממציאה ('we learned FINDING from "
                      "FINDING') — 'leaven shall not be FOUND' "
                      "beside ויחפש ('he SEARCHED') and וימצא "
                      "('and it was FOUND,' Gen 44:12, the goblet); "
                      "finding from searching, searching from "
                      "candles, candles from candle: the four-link "
                      "verbal-analogy chain with our verse the "
                      "first link — Pesachim 7b:13-15",
                      authority="Rav Chisda",
                      machine_claim="G67-33", **IC)]
        if q == "clean_language_canon":
            return [V("eight_letters_curved",
                      "עקם הכתוב שמנה אותיות ('the verse BENT EIGHT "
                      "LETTERS') rather than utter an ugly word — "
                      "'which is not pure' for 'the impure' (Gen "
                      "7:8) — Pesachim 3a:10; STANDING SEATS: "
                      "G17-02/G17-10 hold the canon with the "
                      "eight-letter count machine-verified",
                      authority="the school of R. Yishmael",
                      machine_claim="G17-10 (standing)", **IC)]
        if q == "notarikon_license":
            return [V("av_hamon_proof_seat",
                      "whence NOTARIKON (words as acronyms) from "
                      "the Torah? — אב המון ('father of a "
                      "MULTITUDE,' Gen 17:5) unpacked letter by "
                      "letter — Shabbat 105a:2; STANDING SEAT: "
                      "G33-19 holds the proof-seat since the "
                      "reading",
                      authority="the school of R. Yishmael",
                      machine_claim="G33-19 (standing)", **IC)]
        return None

    def rule_scope_geography(case):
        if case.get("query") == "rivers_below_euphrates":
            return [V("euphrates_above_all",
                      "vow-scope geography: one who vows off "
                      "'water that comes from the Euphrates' — Rav "
                      "Yehuda citing Rav: כל הנהרות למטה משלש "
                      "נהרות ושלש נהרות למטה מפרת ('ALL the rivers "
                      "are below the three rivers, and the three "
                      "below the EUPHRATES'): Eden's four-river "
                      "cosmography (Gen 2:11-14, 'the fourth "
                      "river is Perat') running as "
                      "vow-interpretation law — Bekhorot 55a:21-22",
                      authority="Rav Yehuda citing Rav",
                      machine_claim="G08-31", **SG)]
        return None

    return {
        "name_sanctity": {"fn": rule_name_sanctity,
                          "tractate": "Shevuot"},
        "oath_formula": {"fn": rule_oath_formula,
                         "tractate": "Shevuot"},
        "ink_canon_gen": {"fn": rule_ink_canon_gen,
                          "tractate": "Chullin"},
        "scope_geography": {"fn": rule_scope_geography,
                            "tractate": "Bekhorot"},
    }
