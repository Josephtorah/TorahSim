#!/usr/bin/env python3
"""covenant_rules.py — round 23: THE SINAI COVENANT, the twelfth
Exodus Talmud-first exam block (2026-09-04). Five modules — the
covenant's own machinery. engine.py merges build(V) at its tail.
Read-source: logic/oral_triage/exodus_block_covenant_2026-09-04.md."""


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    # -------------------------------------- the sequestering machine
    SQ = _EX("Yoma 3b:12-4b:11 (the six-days building principle and "
             "the cloud sugya)",
             "Exod.24.16-18 (exo_24_covenant_ascent, EX24-08 — "
             "F-083)")

    def rule_sequester(case):
        q = case.get("query")
        if q == "sequester_source":
            return [V("six_days_building_principle", "'the cloud "
                      "covered him SIX DAYS, and He called to Moses "
                      "on the SEVENTH' (24:16) — a BUILDING "
                      "PRINCIPLE: whoever enters the camp of the "
                      "Presence requires six days' sequestering — "
                      "the High Priest's week derived from Moses' "
                      "six (the mishnah's seventh day is R. Yehuda "
                      "ben Beteira's precaution) (3b:14-15); the "
                      "supporting baraita: ascended, covered, "
                      "SANCTIFIED in the cloud — to receive the "
                      "Torah in sanctity (4a:10)",
                      machine_claim="EX24-08", **SQ)]
        if q == "cloud_entry_contradiction":
            return [V("grasped_and_brought", "'Moses could NOT "
                      "enter the tent for the cloud dwelt on it' "
                      "(40:35) against 'Moses CAME INTO the cloud' "
                      "(24:18) — the Holy One GRASPED Moses and "
                      "brought him in (4b:9)",
                      authority="R. Zerika / R. Elazar",
                      machine_claim="EX24-08", **SQ),
                    V("path_as_the_sea", "WITHIN-WITHIN from the "
                      "sea: 'the children of Israel came WITHIN the "
                      "sea... the waters a wall' — a PATH through "
                      "the cloud as through the sea (4b:10)",
                      authority="the school of R. Yishmael", **SQ)]
        if q == "cloud_purpose":
            return [V("three_readings_recorded", "the covering's "
                      "purpose, three recorded readings: honor to "
                      "Moses (with Moses-called-all-standing, 4b:7); "
                      "R. Natan — to PURGE the food and drink in "
                      "him, setting him as the ministering angels; "
                      "R. Matya ben Charash — to cast AWE, that the "
                      "Torah be given in dread ('where there is "
                      "joy, there be trembling') (4b:1-2)",
                      machine_claim="EX24-08", **SQ)]
        if q == "call_before_speech":
            return [V("manners_and_confidentiality", "call before "
                      "speech: say nothing to your fellow without "
                      "first calling him — and a word said stays "
                      "under do-not-say until 'go tell' (4b:11): "
                      "two conduct rules from the theophany's own "
                      "call frame", machine_claim="EX24-08", **SQ)]
        return None

    # ------------------------------------- the giving-date machine
    GD = _EX("Shabbat 86b:5-87b:7 (the date dispute, the three "
             "things, the crowns) + Yoma 4b:3-6 (the mapping)",
             "Exod.19.1 + 19.10-15 (exo_19_sinai_and_the_covenant, "
             "EX19-16 — F-084)")

    def rule_giving(case):
        q = case.get("query")
        if q == "giving_date":
            return [V("sixth_of_sivan", "the ten utterances given "
                      "on the SIXTH of Sivan (86b:5) — with the "
                      "day-by-day reconstruction (87a:1)",
                      authority="the Rabbis",
                      machine_claim="EX19-16", **GD),
                    V("seventh_of_sivan", "on the SEVENTH — Moses "
                      "having added a day of his own reasoning "
                      "(86b:5, 87a:2-3); the Yoma mapping: R. Yosei "
                      "HaGelili and R. Akiva divide the sequestering "
                      "against the forty days on the same split, R. "
                      "Akiva's count closing on the seventeenth of "
                      "Tammuz for the breaking (Yoma 4b:3-6)",
                      authority="R. Yosei", **GD)]
        if q == "giving_date_agreements":
            return [V("new_moon_and_shabbat_agreed", "Rava's two "
                      "agreed pegs: ALL agree they arrived at the "
                      "NEW MOON ('THIS day they came' linked to "
                      "'THIS month is for you' — the this-word "
                      "analogy) and ALL agree the Torah was given "
                      "ON SHABBAT ('REMEMBER the Sabbath day' "
                      "linked to 'REMEMBER this day,' 13:3 — the "
                      "zakhor-zakhor link, the remember-remember "
                      "family the kiddush file rides); the dispute "
                      "lives only in the month-fixing weekday "
                      "(86b:5)", machine_claim="EX19-16 (EX20-18's "
                      "remember-link — the same analogy family)",
                      **GD)]
        if q == "moses_three_reasonings":
            return [V("day_separation_tablets_assented", "THREE "
                      "things Moses did of his own reasoning, each "
                      "with recorded divine assent (87a:2-5): the "
                      "ADDED DAY ('today and tomorrow' — today LIKE "
                      "tomorrow, with its night; assent: the "
                      "Presence waited to Shabbat morning); the "
                      "SEPARATION (his own a-fortiori from the "
                      "people's one-hour audience; assent: 'return "
                      "to your tents... but you stand here with "
                      "Me'); the BREAKING (a-fortiori from the "
                      "pesach's apostate clause, 12:43 — one law of "
                      "the six hundred thirteen bars the apostate, "
                      "the whole Torah and Israel apostates all the "
                      "more; assent: 'which you BROKE' — strength "
                      "to you that you broke) — human inference "
                      "entering the record with its ratifications",
                      machine_claim="EX19-16 (the 12:43 apostasy "
                      "reading — round 19's freed-token seat, "
                      "ANTICIPATED)", **GD)]
        if q == "ten_crowns":
            return [V("erection_day_ten_firsts", "the erection day "
                      "(40:17) took TEN CROWNS — first of the "
                      "creation order, the princes, the priesthood, "
                      "the service, the fire's descent, the eating "
                      "of holy things, the Presence's dwelling, the "
                      "blessing of Israel, the ban on altars, the "
                      "months (87b:6) — landing on the erection "
                      "date's one-round-old seat",
                      machine_claim="EX40-07 (ANTICIPATED — seated "
                      "round 22)", **GD)]
        return None

    # ----------------------------------------- the boundary machine
    BM = _EX("Sanhedrin 45a:14-16 (the double verb) + 15b:6 (the "
             "beast's court) + Beitzah 5a:6-5b:6 (the release rule)",
             "Exod.19.12-13 + 34.3 (exo_19_sinai_and_the_covenant, "
             "EX19-16 — F-084)")

    def rule_boundary(case):
        q = case.get("query")
        if q == "stoning_procedure":
            return [V("push_then_stone_generations", "'he shall "
                      "surely be STONED or surely be THROWN DOWN' "
                      "(19:13): pushing from the throw-verb, stoning "
                      "from the stone-verb, both together; died "
                      "from the push alone — discharged; and the "
                      "clause extends FOR THE GENERATIONS — the "
                      "execution procedure's source is the "
                      "boundary's own double verb (45a:14-15)",
                      machine_claim="EX19-16", **BM)]
        if q == "sinai_beast_court":
            return [V("twenty_three", "'whether BEAST or MAN, it "
                      "shall not live' (19:13) — as a man by "
                      "twenty-three, so a beast by twenty-three "
                      "(Rami bar Yechezkel, 15b:6): the boundary's "
                      "animal tried by a full court",
                      machine_claim="EX19-16", **BM)]
        if q == "bound_release_rule":
            return [V("counted_release_required", "a matter enacted "
                      "by council needs another council to release "
                      "it (Rav Yosef, 5a:6): the separation needed "
                      "the explicit 'return to your tents' (5b:3), "
                      "and the mount — its graze-ban bound to the "
                      "Presence (34:3) — should have auto-released "
                      "when the Presence left; 'when the ram's horn "
                      "sounds THEY may ascend' (19:13) teaches even "
                      "a lapsed reason needs its formal release: "
                      "the mount's sanctity ended by PROCLAMATION, "
                      "not by default (5b:4-5); the rabbinic tier's "
                      "vineyard case beside (5b:6)",
                      machine_claim="EX19-16", **BM)]
        return None

    # ---------------------------------------- the covenant liturgy
    CL = _EX("Rosh Hashanah 17b:5-7 (the wrapped Leader; the "
             "covenant) + Yoma 36b:5-6 + 37a:1-2 (the confession)",
             "Exod.34.6-10 + 34.7 + 32.30-31 (exo_34_second_tablets, "
             "EX34-09 — F-085)")

    def rule_liturgy(case):
        q = case.get("query")
        if q == "attributes_covenant":
            return [V("never_return_empty", "'and the LORD passed "
                      "before his face and called': were it not "
                      "written it could not be said — the Holy One "
                      "WRAPPED HIMSELF as a prayer leader and "
                      "showed Moses the ORDER: whenever Israel sin, "
                      "let them perform this order and I forgive "
                      "(17b:5); the doubled Name — before the sin "
                      "and after the repentance (17b:6); and Rav "
                      "Yehuda: A COVENANT IS CUT to the thirteen "
                      "attributes that they never return empty — "
                      "'behold, I cut a covenant' (34:10) (17b:7)",
                      machine_claim="EX34-09", **CL)]
        if q == "confession_order":
            return [V("wronged_rebelled_sinned", "the order as the "
                      "attributes verse speaks it — 'bearing "
                      "iniquity and transgression and sin' (34:7), "
                      "as Moses said it (36b:5)",
                      authority="R. Meir",
                      machine_claim="EX34-09", **CL),
                    V("sinned_wronged_rebelled", "iniquities are "
                      "the deliberate, transgressions the "
                      "rebellions, sins the inadvertent — having "
                      "confessed the deliberate, shall he return "
                      "to the inadvertent? the order runs from the "
                      "lightest (36b:6)", authority="the Sages",
                      **CL)]
        if q == "confession_opener":
            return [V("ana_from_horeb_kashya_kept", "the confession "
                      "opens with PLEASE — atonement-atonement from "
                      "HOREB (Moses' 'perhaps I shall atone,' "
                      "32:30, with the ana of 32:31); the "
                      "by-the-NAME leg from the broken-neck heifer "
                      "(37a:1) — and Abaye's asymmetry stands "
                      "recorded as KASHYA (the heifer should learn "
                      "the ana and its priests say none): a "
                      "standing difficulty carried honestly "
                      "(37a:2)", machine_claim="EX34-09", **CL)]
        return None

    # ------------------------------------------ the Sinai charters
    SC = _EX("Berakhot 5a:3 (the canon channel) + Yevamot 46b:1-3 "
             "(conversion's immersion)",
             "Exod.24.12 + 19.10 (exo_24_covenant_ascent, EX24-08 — "
             "F-083)")

    def rule_charters(case):
        q = case.get("query")
        if q == "canon_channel":
            return [V("five_terms_whole_canon", "'I will give you "
                      "the TABLETS, and the TORAH, and the "
                      "COMMANDMENT, which I have WRITTEN, to TEACH "
                      "THEM' (24:12) — tablets = the ten "
                      "utterances; Torah = Scripture; the "
                      "commandment = MISHNAH; which-I-have-written "
                      "= the Prophets and Writings; to-teach-them = "
                      "TALMUD — all given to Moses from Sinai: the "
                      "whole library enumerated from one verse, the "
                      "two-channel charter's second seat beside "
                      "34:27's (Berakhot 5a:3)",
                      machine_claim="EX24-08 (the 34:27 charter — "
                      "the Ki Tisa round's seat, its second witness "
                      "here)", **SC)]
        if q == "conversion_immersion":
            return [V("afortiori_from_washing", "'SANCTIFY them "
                      "today and tomorrow, and let them WASH their "
                      "garments' (19:10): where no garment-washing "
                      "is required immersion is required — where "
                      "washing is required, immersion all the more: "
                      "the fathers entered the covenant by "
                      "immersion, and the convert enters as they "
                      "did (46b:2); the mere-cleanliness challenge "
                      "kept on the record (46b:3)",
                      machine_claim="EX24-08 (EX19-16 the anchor "
                      "row)", **SC)]
        return None

    return {
        "sequestering_machine": {"fn": rule_sequester},
        "giving_date_machine": {"fn": rule_giving},
        "boundary_machine_sinai": {"fn": rule_boundary},
        "covenant_liturgy": {"fn": rule_liturgy},
        "sinai_charters": {"fn": rule_charters},
    }
