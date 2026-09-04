#!/usr/bin/env python3
"""ink_rules.py — round 20: THE INK LAYER, the ninth Exodus
Talmud-first exam block (2026-09-04). Five modules — the rows where
the Talmud rules about the ink itself: vocalization authority, the
script witness, letter arithmetic, the undecided parses, the Name's
ink laws, the inference licenses. engine.py merges build(V) at its
tail. Read-source: logic/oral_triage/exodus_block_ink_2026-09-04.md."""


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    # ------------------------------------ vocalization authority
    VA = _EX("Sanhedrin 4a:12-4b:16 (the read-form/written-skeleton "
             "sugya, its exemplars and its scope law)",
             "Exod.23.19 (exo_23_justice_calendar, EX23-12 — F-073; "
             "the front-end question the project measured, named in "
             "the tradition's own words)")

    def rule_vocalization(case):
        q = case.get("query")
        if q == "mikra_masoret_scope":
            return [V("dispute_only_where_forms_differ", "the sugya's "
                      "final law (4b:14): the read-form/written-"
                      "skeleton dispute lives ONLY where the written "
                      "letters differ from the read form; where the "
                      "two are identical — the milk/fat pair, same "
                      "letters, only vowels apart — ALL follow the "
                      "READ form. The tradition's own boundary on "
                      "vowel authority, matching the front-end "
                      "measurement (vowels decide nothing alone "
                      "against the consonants)",
                      machine_claim="EX23-12", **VA)]
        if q == "chalev_exemplar":
            return [V("way_of_cooking_seal", "everyone reads 'in its "
                      "mother's MILK' (4a:15) — and the sugya's close "
                      "moves the law off the vowels entirely: Rav "
                      "Acha son of Rav Ika — the Torah forbade the "
                      "WAY OF COOKING (לא תבשל, 4b:16): the kid-law "
                      "stands on the verb, not the vowel",
                      machine_claim="EX23-12 (the seated meat-in-milk "
                      "cluster — ANTICIPATED)", **VA)]
        if q == "sukka_walls_count":
            return [V("four_by_masoret", "the Rabbis count the "
                      "SPELLINGS — defective, defective, full = four "
                      "wall-units, the received law trimming the "
                      "third to a handbreadth (4a:12)",
                      authority="the Rabbis",
                      machine_claim="EX23-12", **VA),
                    V("six_by_mikra", "R. Shimon counts the READ "
                      "forms — six, the received law trimming the "
                      "fourth (4a:13)", authority="R. Shimon", **VA)]
        if q == "yireh_counter_exemplar":
            return [V("equal_forms_disputed_recorded", "the sugya's "
                      "own counter-exemplar (4b:15): shall-SEE / "
                      "shall-BE-SEEN (23:17) are letter-identical "
                      "yet expounded both ways — Yochanan ben "
                      "Dahavai's two-whole-eyes law — the M-16 "
                      "revocalization family's charter case; the "
                      "festival law itself is block 17's",
                      machine_claim="EX23-12", **VA)]
        return None

    # --------------------------------------- the script witness
    SW = _EX("Sanhedrin 21b:22-22a:6 (the three positions on the "
             "script) + 29a:33-36 (whoever adds subtracts)",
             "Exod.27.10 (exo_27_altar_court, EX27-08 — F-074; the "
             "arithmetic pair anchors Exod.25.10 + 26.7, rows named "
             "in the ledger)")

    def rule_script(case):
        q = case.get("query")
        if q == "script_history":
            return [V("changed_in_ezra_days", "first given in the "
                      "Ivri script and holy tongue; re-given in "
                      "Ezra's days in Ashurit; Israel chose Ashurit "
                      "+ the holy tongue (21b:22; R. Yosei: the "
                      "script was changed through Ezra, 21b:24-25)",
                      authority="Mar Zutra/Mar Ukva + R. Yosei",
                      machine_claim="EX27-08", **SW),
                    V("given_lost_restored", "given IN THIS SCRIPT "
                      "at first, turned to Roetz when they sinned, "
                      "restored when they repented (22a:3)",
                      authority="Rebbi", **SW),
                    V("never_changed", "the script never changed at "
                      "all — the vavs of the pillars (22a:5)",
                      authority="R. Elazar HaModai (via R. Shimon "
                      "b. Elazar)", **SW)]
        if q == "vav_pillars_witness":
            return [V("letter_names_itself", "ווי העמודים ('the "
                      "HOOKS of the pillars,' 27:10): the hook is "
                      "NAMED by the letter vav — so the letter "
                      "looked like a hook then as now; as the "
                      "pillars did not change, the vavs did not "
                      "change — the ink carrying its own "
                      "paleographic witness (22a:5, with Esther's "
                      "'like their script' beside)",
                      machine_claim="EX27-08", **SW)]
        if q == "adds_subtracts":
            return [V("added_letter_lowers_count", "whoever ADDS "
                      "subtracts (29a:34, from Eve's added "
                      "touch-ban): Rav Mesharshiya — the alef of "
                      "אמתים ('two cubits,' 25:10) turns two "
                      "hundred into two; Rav Ashi — the ayin of "
                      "עשתי עשרה ('eleven curtains,' 26:7) turns "
                      "twelve into eleven: a letter added, a "
                      "number lowered, twice in the dwelling's own "
                      "measures", machine_claim="EX27-08 (rows for "
                      "exo_25/exo_26 named in the ledger)", **SW)]
        return None

    # --------------------------------------- the undecided parses
    UP = _EX("Yoma 52a:10-52b:7 (Isi ben Yehuda's census + Rav "
             "Chisda's rider)",
             "Exod.25.34 + 17.9 + 24.5 (the three Exodus members; "
             "the census is the tradition's own record of "
             "undecidable syntax — RESEARCH_LOG 2026-09-03 already "
             "carries it as the cantillation verdict's witness)")

    def rule_undecided(case):
        q = case.get("query")
        if q == "undecided_census":
            return [V("five_verses_no_decision", "Isi ben Yehuda: "
                      "FIVE verses in the Torah have no decision "
                      "(52a:10): se'et, meshukkadim, machar, arur, "
                      "ve-kam (52b:1-5) — the tradition's own census "
                      "of syntactic undecidability, and none of the "
                      "five is case law (the standing research-log "
                      "witness)", **UP)]
        if q == "meshukkadim_parse":
            return [V("attachment_undecided", "מְשֻׁקָּדִים "
                      "('almond-worked,' 25:34): whether the "
                      "almond-work modifies the cups before it or "
                      "the menorah-clause after — no decision "
                      "(52b:2)", **UP)]
        if q == "machar_parse":
            return [V("attachment_undecided", "מָחָר ('tomorrow,' "
                      "17:9): 'go out, fight with Amalek — "
                      "tomorrow' or 'fight; tomorrow I stand on the "
                      "hill' — no decision (52b:3)", **UP)]
        if q == "young_men_parse":
            return [V("undecided_for_rav_chisda", "the young men's "
                      "offerings (24:5): did they bring bulls for "
                      "BOTH classes or only as the peace-offerings "
                      "— undecided for Rav Chisda, decided for Isi "
                      "(52b:7): even the census's edge carries a "
                      "recorded second opinion", **UP)]
        return None

    # ------------------------------------------ the Name's ink laws
    NI = _EX("Shevuot 35a:27-35b:7 (the erasure lists) + Pesachim "
             "50a:18-21 (the concealment ketiv) + 117a:1-3 (the "
             "compounds)",
             "Exod.3.15 (exo_03_bush_and_name, EX03-14 — F-075; the "
             "Tzevaot row anchors Exod.7.4, the compounds "
             "Exod.17.16 — rows named in the ledger)")

    def rule_name_ink(case):
        q = case.get("query")
        if q == "tzevaot_erasure":
            return [V("wholly_erasable_israels_title", "R. Yosei: "
                      "Tzevaot is the title of ISRAEL — 'I shall "
                      "bring out MY HOSTS, My people' (7:4) — so "
                      "wholly erasable (35b:5)",
                      authority="R. Yosei",
                      machine_claim="EX03-14", **NI),
                    V("inerasable_name", "the list's law: Tzevaot "
                      "stands among the inerasable Names "
                      "(35a:27) — and Shmuel rules: the law is NOT "
                      "per R. Yosei (35b:5)",
                      authority="the Rabbis (Shmuel's ruling)",
                      **NI)]
        if q == "name_suffix_letters":
            return [V("prefix_erasable_suffix_sanctified", "letters "
                      "BEFORE the Name erasable (the lamed, bet, "
                      "vav prefixes); letters AFTER it — the Sages "
                      "erase, ACHERIM rule they stand, for the Name "
                      "has sanctified them — and Rav Huna rules per "
                      "Acherim (35b:6-7): sanctity flows forward "
                      "through the word, not back",
                      machine_claim="EX03-14", **NI)]
        if q == "le_alem_concealment":
            return [V("ketiv_commands_concealment", "לעלם written "
                      "defective (3:15): read 'to CONCEAL' — the "
                      "elder's one word stopping Rava's public "
                      "exposition (50a:20); R. Avina's pairing: 'My "
                      "NAME' — concealed; 'My MEMORIAL' — spoken: "
                      "written yod-he, read alef-dalet, this world; "
                      "read as written in the world to come "
                      "(50a:19-21) — the defective spelling IS the "
                      "law", machine_claim="EX03-14", **NI)]
        if q == "name_compounds":
            return [V("three_positions_teiku_rider", "which "
                      "compounds carry the Name (117a:1): R. "
                      "Yochanan — halleluya, kes-Ya, Yedidya; Rav — "
                      "kes-Ya and Merchavya; Rabbah — Merchavya "
                      "alone; merchav-Ya for Rav Chisda — TEIKU, "
                      "the question stands (117a:2, the campaign's "
                      "second recorded TEIKU verdict-state); "
                      "Yedidya split — yedid profane, Ya holy "
                      "(117a:3)", machine_claim="EX03-14 (kes-Ya "
                      "anchors 17:16, row named)", **NI)]
        return None

    # ------------------------------------- the inference licenses
    IL = _EX("Shabbat 97a:1 (the analogy license) + Sanhedrin 3b:3 "
             "(the first-mention rule, the courts block's read)",
             "Exod.4.1 + 22.8 (the meta-rules the compiler runs "
             "under; EX23-12 carries the file)")

    def rule_inference(case):
        q = case.get("query")
        if q == "verbal_analogy_license":
            return [V("received_only", "R. Yehuda ben Beteira had "
                      "the letters but not the tradition — had he "
                      "received the verbal analogy he would have "
                      "used it: ONE DOES NOT REASON A VERBAL "
                      "ANALOGY FROM HIS OWN MIND (97a:1) — the "
                      "license rule for middah II (the triage's own "
                      "headline find, now examined)",
                      machine_claim="EX23-12", **IL)]
        if q == "first_mention_rule":
            return [V("plain_sense_not_counted", "R. Yonatan: a "
                      "FIRST mention serves the plain sense and "
                      "does not join the count (3b:3) — the "
                      "counting-derivation's own overhead rule, "
                      "read fresh at the courts block and doubling "
                      "here as the ink-layer's meta-rule",
                      machine_claim="EX23-12 (the courts block's "
                      "three-judges file — ANTICIPATED)", **IL)]
        return None

    return {
        "vocalization_authority": {"fn": rule_vocalization},
        "script_witness": {"fn": rule_script},
        "undecided_parses": {"fn": rule_undecided},
        "name_ink_laws": {"fn": rule_name_ink},
        "inference_license": {"fn": rule_inference},
    }
