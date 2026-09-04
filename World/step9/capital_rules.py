#!/usr/bin/env python3
"""capital_rules.py — round 25: CAPITAL MODES AND IDOLATRY
SERVICE, the fourteenth Exodus Talmud-first exam block
(2026-09-04). Five modules — the witch, bestiality's passive, the
service paradigm, the blasphemy verb and the ruler's gate, the
satellites. engine.py merges build(V) at its tail. Read-source:
logic/oral_triage/exodus_block_capital_2026-09-04.md."""


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    # ------------------------------------------------- the witch
    WI = _EX("Sanhedrin 67a:19-21 + 60a:1; Yevamot 4a:4-6 = "
             "Berakhot 21b:9-11",
             "Exod.22.17 (exo_22_property_social, EX22-17 — F-092)")

    def rule_witch(case):
        q = case.get("query")
        if q == "witch_gender_scope":
            return [V("men_included_frequency_noun", "מכשפה — "
                      "'whether man or woman; why the feminine? "
                      "because MOST women are found in sorcery' — "
                      "the noun's gender is a frequency datum, not "
                      "a scope limit (67a:19)",
                      machine_claim="EX22-17", **WI)]
        if q == "witch_death_mode":
            return [V("sword_by_soul_analogy", "here 'you shall "
                      "not let a witch LIVE' — there 'you shall "
                      "not let any soul LIVE' (Deut 20:16): as "
                      "there by the SWORD, so here (67a:20)",
                      authority="R. Yosei HaGelili",
                      machine_claim="EX22-17", **WI),
                    V("stoning_by_sinai_boundary", "here lo "
                      "techayeh — there 'whether beast or man it "
                      "shall not LIVE' (Exod 19:13, THE SINAI "
                      "BOUNDARY VERSE): as there by STONING, so "
                      "here (67a:21) — the mode derived from the "
                      "clause whose machine EX19-10/EX19-16 seat; "
                      "ben Azzai and R. Yehuda reach stoning by "
                      "rival routes (4a:5-6)",
                      authority="R. Akiva", **WI)]
        if q == "juxtaposition_validity":
            return [V("adjacency_teaches", "the witch was PLACED "
                      "beside the beast-lier to teach: as he is "
                      "stoned, so she (Yevamot 4a:5 = Berakhot "
                      "21b:10) — with Rav Yosef's meta-rule: even "
                      "one who rejects adjacency generally "
                      "expounds it in DEUTERONOMY (4a:4)",
                      authority="ben Azzai",
                      machine_claim="EX22-17", **WI),
                    V("class_exemplar_route", "'because they "
                      "placed the matter beside it, shall we take "
                      "this one out to STONING?!' — instead: ov "
                      "and yidoni were inside the sorcerers' "
                      "class and singled out to compare — same "
                      "verdict, adjacency refused (4a:6 = 21b:11)",
                      authority="R. Yehuda", **WI)]
        return None

    # ------------------------------------------ bestiality's file
    BE = _EX("Sanhedrin 54b:5-7",
             "Exod.22.18 (exo_22_property_social, EX22-17 — "
             "F-092; the animal's own trial credited at Sanhedrin "
             "15a:14, the courts block)")

    def rule_bestiality(case):
        q = case.get("query")
        if q == "bestiality_passive":
            return [V("liable_by_reassignment", "כל שכב עם בהמה "
                      "מות יומת ('ALL who lie with a beast shall "
                      "surely die'): the active lier's punishment "
                      "is heard elsewhere — 'if it is not needed "
                      "for the lier, APPLY IT to the lain-with' "
                      "(אם אינו ענין — the reassignment middah, "
                      "54b:6); mode stoning by the kill-verb "
                      "analogy (54b:5), the warning at Leviticus "
                      "18:23 (54b:7)",
                      machine_claim="EX22-17", **BE)]
        return None

    # --------------------------------------- the service paradigm
    SV = _EX("Sanhedrin 60b:7-13 + 61a:14-16 + 61b:19-21 + "
             "63a:1-3 + 63a:13-17; Avodah Zarah 51a:13-14",
             "Exod.22.19 + 34.14 (exo_22_property_social EX22-17 "
             "+ exo_34_second_tablets EX34-11 — F-092/F-094; the "
             "zevichah paradigm held at EX22-09 since F-017)")

    def rule_service(case):
        q = case.get("query")
        if q == "idol_slaughter_scope":
            return [V("idol_service_not_outside_slaughter", "had "
                      "it said 'one who sacrifices shall be "
                      "destroyed' alone, I would say it speaks of "
                      "slaughtering sacred offerings OUTSIDE — "
                      "לאלהים ('TO THE GODS') teaches: "
                      "idol-service slaughter (60b:8)",
                      machine_claim="EX22-17", **SV)]
        if q == "idol_service_extension":
            return [V("all_inside_services_emptied", "incense and "
                      "libation from where? בלתי לה' לבדו ('save "
                      "to the LORD alone') — it EMPTIED all the "
                      "services to the Unique Name (60b:9); the "
                      "hugger and kisser excluded — 'zoveach' "
                      "bounds the capital act to inside-style "
                      "service and the bow (60b:13) — EX22-09's "
                      "zevichah row held this paradigm",
                      machine_claim="EX22-17", **SV)]
        if q == "blemished_idol_offering":
            return [V("exempt_inside_style_only", "slaughtering a "
                      "BLEMISHED animal to idols is exempt: 'the "
                      "Torah forbade only INSIDE-STYLE' (כעין "
                      "פנים) — what the Temple would not receive "
                      "the clause does not punish (Avodah Zarah "
                      "51a:13); Rava probes the blemish parameter "
                      "at the Noahide-altar edge (51a:14)",
                      authority="R. Yochanan (cited by R. Abahu)",
                      machine_claim="EX22-17", **SV)]
        if q == "punished_bow_warning":
            return [V("warning_at_34_14", "the bow's punishment "
                      "by the Deuteronomy juxtaposition — 'the "
                      "warning from where? כי לא תשתחוה לאל אחר "
                      "(you shall not bow to another god, 34:14)' "
                      "(60b:11-12): the second tablets' clause is "
                      "the punished bow's azhara",
                      machine_claim="EX34-11", **SV)]
        if q == "bowing_verse_census":
            return [V("three_offices_assigned", "Abaye: THREE "
                      "bowing verses in the idolatry file — one "
                      "for the idol worshiped by bowing, one for "
                      "the idol not so worshiped, one TO DIVIDE "
                      "(bowing carved as its own liability) "
                      "(63a:2-3); 34:14's own office is the "
                      "azhara (60b:12)",
                      authority="Abaye",
                      machine_claim="EX34-11", **SV)]
        if q == "one_lapse_unification":
            return [V("one_liability_one_service", "R. Ami: "
                      "sacrificed, incensed, and poured in ONE "
                      "LAPSE — one liability; Abaye's reason: לא "
                      "תעבדם ('you shall not serve them,' 20:5) "
                      "MADE THEM ALL ONE SERVICE (63a:1)",
                      authority="R. Ami (reason per Abaye)",
                      machine_claim="EX34-11", **SV)]
        if q == "love_fear_worship":
            return [V("liable_haman_proof", "'to THEM you shall "
                      "not bow' — but you may bow to a man; even "
                      "one worshiped like Haman? ולא תעבדם — and "
                      "Haman WAS worshiped from FEAR: love-or-fear "
                      "worship liable (61b:20)",
                      authority="Abaye",
                      machine_claim="EX34-11", **SV),
                    V("exempt_fear_distinguished", "like-Haman-"
                      "but-not-like-Haman: Haman was himself an "
                      "idol, but worshiped from fear — love-or-"
                      "fear worship exempt (61b:21)",
                      authority="Rava", **SV)]
        if q == "self_deification_speech":
            return [V("speech_liable", "where they WORSHIPED him "
                      "all agree liable — לא תעשה לך פסל read to "
                      "self-deification (61a:15); the dispute is "
                      "mere speech ('come worship me') — speech "
                      "is a thing",
                      authority="R. Meir",
                      machine_claim="EX22-17", **SV),
                    V("speech_exempt", "mere speech is not a "
                      "thing (61a:15) — narrowed by Rav Yosef's "
                      "retraction: even R. Yehuda convicts on the "
                      "enticed's own 'I will worship' (61a:16)",
                      authority="R. Yehuda", **SV)]
        if q == "accepting_as_god":
            return [V("equated_by_calf_hekesh", "the calf verse "
                      "chains its three verbs — 'they BOWED, they "
                      "SACRIFICED, they SAID: these are your "
                      "gods' (32:8): the SAYING equated by hekesh "
                      "to the bowing and the sacrifice — "
                      "accepting an idol as god IS worship "
                      "(63a:14)",
                      machine_claim="EX32-08", **SV)]
        if q == "joining_names":
            return [V("uprooted_lord_alone", "whoever JOINS "
                      "Heaven's name with another thing is "
                      "uprooted from the world: בלתי לה' לבדו "
                      "('save to the LORD alone,' 22:19); the "
                      "calf's plural he'elukha read as craving "
                      "MANY gods — with R. Yochanan's row: but "
                      "for that vav, annihilation (63a:15-17)",
                      authority="R. Shimon ben Yochai",
                      machine_claim="EX22-17", **SV)]
        return None

    # -------------------------------- the curse and the ruler gate
    CU = _EX("Sanhedrin 56a:5-7 + 66a:11-13 + 66a:22-24 + "
             "85a:13-15; Yevamot 22b:6-8",
             "Exod.22.27 (exo_22_property_social, EX22-18 — "
             "F-093; the curse counts held at EX22-09 since "
             "F-017)")

    def rule_curse(case):
        q = case.get("query")
        if q == "blasphemy_verb":
            return [V("cursing_from_balaam", "whence that nokev "
                      "(Lev 24:16) means CURSING? מה אקב לא קבה "
                      "אל ('how shall I CURSE whom God has not "
                      "cursed' — Balaam's own verb, Num 23:8); "
                      "and its WARNING from here: אלהים לא תקלל "
                      "(22:27) (56a:6); the piercing alternative "
                      "parsed and set aside (56a:7)",
                      authority="Shmuel",
                      machine_claim="EX22-18", **CU)]
        if q == "blasphemy_elohim_referent":
            return [V("profane_judges", "elohim here is PROFANE — "
                      "the judges (66a:24); the parent-curser's "
                      "warning path needs it (66a:23)",
                      authority="R. Yishmael",
                      machine_claim="EX22-18", **CU),
                    V("sacred_name", "elohim here is SACRED — the "
                      "Name-blesser's warning (66a:24, with R. "
                      "Eliezer ben Yaakov's row)",
                      authority="R. Akiva", **CU)]
        if q == "parent_curser_warning":
            return [V("binyan_av_judge_prince", "the punishment "
                      "is heard (21:17) — the warning built: a "
                      "judge-father under 'you shall not curse "
                      "elohim,' a prince-father under 'a ruler in "
                      "your people'; neither — בנין אב from the "
                      "two: their common 'IN YOUR PEOPLE' reaches "
                      "every parent (66a:12-13)",
                      machine_claim="EX22-18", **CU)]
        if q == "ruler_curse_gate":
            return [V("deeds_of_your_people_repentance", "ונשיא "
                      "בעמך לא תאור — only בעושה מעשה עמך ('one "
                      "who DOES THE DEEDS of your people,' "
                      "85a:14), striking carried over by hekesh "
                      "(85a:15); the edge: the barred-union (mamzer) "
                      "son liable "
                      "for his father WHEN HE REPENTED — the gate "
                      "runs on repentance status, not pedigree "
                      "(Yevamot 22b:7-8)",
                      machine_claim="EX22-18", **CU)]
        return None

    # -------------------------------------------- the satellites
    ST = _EX("Sanhedrin 56b:9-11 + 58b:2-4 + 58b:16-20",
             "Exod.2.12-13 + 6.20 + 32.8 (exo_02_drawn_from_the_"
             "water EX02-15, exo_06_i_am_the_lord EX06-15, "
             "exo_32_golden_calf EX32-08 — F-095/F-096/F-097)")

    def rule_satellites(case):
        q = case.get("query")
        if q == "calf_noahide_source":
            return [V("making_or_worship_fork", "the Noahide "
                      "idolatry command sourced two ways — 'they "
                      "turned quickly from the way I COMMANDED "
                      "them: they MADE a calf' (32:8) or Hosea's "
                      "walked-after-tzav — and the fork: a "
                      "gentile who MADE an idol without "
                      "worshiping is liable from the making on "
                      "one arm, only on worship on the other; "
                      "the arms recorded UNASSIGNED (Rav Chisda "
                      "and Rav Yitzchak bar Avdimi, one each — "
                      "chad amar) (56b:10-11)",
                      machine_claim="EX32-08", **ST)]
        if q == "amram_aunt_scope":
            return [V("fathers_side_resolution", "'and Amram took "
                      "Jochebed HIS AUNT' (6:20) objected against "
                      "the pre-Sinai incest scope — resolved: his "
                      "FATHER'S-side aunt, outside the ban "
                      "(58b:3-4) — and the frozen unit's own "
                      "translation layer already renders 'his "
                      "father's sister' at the 6:20 step",
                      machine_claim="EX06-15", **ST)]
        if q == "gentile_strikes_israelite":
            return [V("liable_death_no_man", "a gentile who "
                      "strikes an Israelite is liable to death: "
                      "'he turned this way and that and saw there "
                      "was NO MAN, and struck the Egyptian' "
                      "(2:12) (58b:17); the Presence-slap escort "
                      "noted (58b:18)",
                      authority="R. Chanina",
                      machine_claim="EX02-15", **ST)]
        if q == "raised_hand":
            return [V("called_wicked_imperfect_verb", "one who "
                      "RAISES his hand though he did not strike "
                      "is called WICKED: למה תכה ('why WOULD you "
                      "strike,' 2:13) — not 'why did you strike': "
                      "the verse's own imperfect verb carries the "
                      "law (58b:19); Zeiri's sinner row beside it "
                      "(58b:20)",
                      authority="Reish Lakish",
                      machine_claim="EX02-15", **ST)]
        return None

    return {
        "witch_machine": {"fn": rule_witch},
        "bestiality_file": {"fn": rule_bestiality},
        "idol_service_machine": {"fn": rule_service},
        "curse_ruler_file": {"fn": rule_curse},
        "capital_satellites": {"fn": rule_satellites},
    }
