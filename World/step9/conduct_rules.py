#!/usr/bin/env python3
"""conduct_rules.py — round 21: CONDUCT AND LITURGY, the tenth
Exodus Talmud-first exam block (2026-09-04). Five modules — the
liturgy and conduct rules grounded in Exodus's ink. engine.py
merges build(V) at its tail.
Read-source: logic/oral_triage/exodus_block_conduct_2026-09-04.md."""


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    # ------------------------------------------ recitation modes
    RM = _EX("Sotah 27b:11-12 (the Song's modes) + 33a:14 (the "
             "Levites' tongue) + Berakhot 45a:8-9 (the translator)",
             "Exod.19.19 + 15.1 (exo_19_sinai_and_the_covenant, "
             "EX19-15 — F-076: Sinai's dialogue as the liturgy's "
             "voice standard)")

    def rule_recitation(case):
        q = case.get("query")
        if q == "song_recitation":
            return [V("responsive_like_hallel", "'and they said, "
                      "SAYING' (15:1) — the spare word: Israel "
                      "ANSWERED after Moses phrase by phrase, as "
                      "one reads hallel (27b:11)",
                      authority="R. Akiva",
                      machine_claim="EX19-15", **RM),
                    V("together_like_shema", "as one reads the "
                      "SHEMA — together after the opener, not as "
                      "hallel (27b:12)", authority="R. Nechemya",
                      **RM)]
        if q == "levites_language":
            return [V("holy_tongue_by_voice_link", "the Levites' "
                      "answering in the HOLY TONGUE: voice-voice "
                      "from Moses — 'Moses speaks and God ANSWERS "
                      "HIM BY VOICE' (19:19): as Sinai's dialogue "
                      "ran in the holy tongue, so the Levites' "
                      "(33a:14)", machine_claim="EX19-15", **RM)]
        if q == "targum_voice":
            return [V("not_above_reader", "the translator may not "
                      "out-voice the reader — 'answers him BY "
                      "VOICE' = BY MOSES' VOICE: the Answerer "
                      "matched the reader's volume; and if the "
                      "translator cannot rise, the READER lowers — "
                      "the matching is the law (45a:8-9). The "
                      "machine's own reading instrument (the "
                      "Targum) regulated from Sinai's dialogue — "
                      "beside Mishnah Megillah 4:10's calf-account "
                      "rule seated in the Ki Tisa round",
                      machine_claim="EX19-15", **RM)]
        return None

    # ------------------------------------- the liturgy of the Name
    LN = _EX("Sotah 38a:9-13 (the blessing's Name and site) + "
             "Berakhot 6a:13 (the Presence at study) + 54a:9 (the "
             "greeting)",
             "Exod.20.21 (exo_20_the_ten_utterances, EX20-19 — "
             "F-077: one clause, two recorded jobs)")

    def rule_name_liturgy(case):
        q = case.get("query")
        if q == "name_blessing_site":
            return [V("chosen_house_by_inverted_verse", "the "
                      "priestly blessing carries the EXPLICIT Name "
                      "in the chosen house alone — the naming-link "
                      "route (38a:10), and R. Yoshiya's route on "
                      "our clause: 'in every place where I cause My "
                      "Name to be mentioned' (20:21) — 'can every "
                      "place enter your mind?! the verse is "
                      "INVERTED: wherever I come to you and bless "
                      "you, THERE I mention My Name — the chosen "
                      "house' (38a:11): a recorded READ-ORDER "
                      "operation; converts, women, freedmen "
                      "included, face to face (38a:12-13)",
                      machine_claim="EX20-19", **LN)]
        if q == "presence_at_study":
            return [V("presence_with_even_one", "the SAME clause's "
                      "second job (6a:13): even ONE who sits with "
                      "Torah — the Presence with him: 'wherever I "
                      "cause My Name to be mentioned, I will come "
                      "to you and bless you' — the site law and "
                      "the study law standing together on one "
                      "clause", machine_claim="EX20-19", **LN)]
        if q == "greeting_with_name":
            return [V("instituted_time_to_act", "greeting a fellow "
                      "WITH THE NAME — instituted, Boaz the "
                      "exemplar, under 'a time to act for the "
                      "LORD' (54a:9): the Name-boundary's "
                      "conduct-side rider",
                      machine_claim="EX20-19", **LN)]
        return None

    # ---------------------------------------------- the kiddush file
    KF = _EX("Pesachim 106a:5-7 (over wine; entry and day) + "
             "117b:8 (the exodus mention) + Berakhot 20b:7-14 (the "
             "women's duties)",
             "Exod.20.8 (exo_20_the_ten_utterances, EX20-18 — "
             "F-077's kiddush half; 16:8 the Grace challenge)")

    def rule_kiddush(case):
        q = case.get("query")
        if q == "kiddush_wine":
            return [V("over_wine_entry_and_day", "'REMEMBER the "
                      "Sabbath day to sanctify it' (20:8) — "
                      "remember it OVER WINE (106a:5); the essence "
                      "at the DAY'S ENTRY (night), and the day's "
                      "cup from 'remember THE DAY' (106a:6-7)",
                      machine_claim="EX20-18", **KF)]
        if q == "kiddush_exodus_mention":
            return [V("required_by_remember_link", "the EXODUS must "
                      "be mentioned in the day's kiddush — "
                      "remember-remember: 'that you may remember "
                      "the day of your going out' beside 'remember "
                      "the Sabbath day' (117b:8, Rav Acha bar "
                      "Yaakov): the exodus wired into the Sabbath "
                      "cup by the shared verb",
                      machine_claim="EX20-18", **KF)]
        if q == "women_kiddush":
            return [V("torah_grade_by_keep_remember", "women owe "
                      "KIDDUSH by TORAH LAW (Rav Adda bar Ahava, "
                      "20b:8) — Rava's clincher: 'REMEMBER and "
                      "KEEP' — whoever is in the KEEPING is in the "
                      "REMEMBERING; women, obligated in the "
                      "Sabbath's bans, are obligated in its "
                      "sanctification (20b:10): the utterance-pair "
                      "run as one law",
                      machine_claim="EX20-18", **KF)]
        if q == "women_grace":
            return [V("obligated_grading_open", "women owe the "
                      "GRACE — the 'evening meat, morning bread' "
                      "challenge (16:8) refused as a time-bound "
                      "classifier (20b:7); but the GRADE — Torah "
                      "or rabbinic — is raised for discharging "
                      "others and the proof deflected (a "
                      "rabbinic-measure meal): a recorded OPEN "
                      "grading, carried honestly (20b:11-14)",
                      machine_claim="EX20-18", **KF)]
        return None

    # ------------------------------------- the blessing derivations
    BD = _EX("Berakhot 48b:5-12 (Grace, before-blessing, the "
             "Torah-blessing) + 54a:10-12 (the miracle stations) + "
             "54b:7-9 (the seeing list) + 60a:29 (the healing "
             "license)",
             "Exod.23.25 + 24.12 + 18.10 + 17.12 + 21.19 (the "
             "blessing-genre's Exodus anchors; EX21-07 holds the "
             "license — ANTICIPATED)")

    def rule_blessings(case):
        q = case.get("query")
        if q == "blessing_before_food":
            return [V("three_routes_recorded", "the blessing BEFORE "
                      "eating, three recorded routes: the "
                      "a-fortiori (sated blesses — hungry all the "
                      "more, 48b:5); R. Yitzchak — 'and He shall "
                      "BLESS your bread' (23:25) re-voweled to the "
                      "imperative, and it is 'bread' only BEFORE "
                      "eaten (48b:7, the M-16 family); R. Natan — "
                      "Samuel's feast (48b:8)",
                      machine_claim="EX23-11 (the serve-and-bless "
                      "clause's seat)", **BD)]
        if q == "torah_blessing_source":
            return [V("giving_pair_and_afortiori", "the "
                      "Torah-blessing: R. Yishmael's a-fortiori "
                      "(the hour's life — the world's life all the "
                      "more); R. Chiyya b. Nachmani — the "
                      "GIVING-pair: 'the good land which He GAVE "
                      "you' beside 'I will GIVE you the tablets "
                      "and the Torah' (24:12) (48b:10)",
                      machine_claim="EX24 (the tablets clause; row "
                      "named in the ledger)", **BD)]
        if q == "miracle_blessing_source":
            return [V("yitro_charter", "the miracle-places blessing "
                      "from YITRO — 'Blessed be the LORD who saved "
                      "you' (18:10, 54a:10): the genre's charter "
                      "is Exodus's own convert; the individual's "
                      "station beside (Rava's ruling, 54a:11-12)",
                      machine_claim="EX18 (the blessing verse; row "
                      "named in the ledger)", **BD)]
        if q == "moses_stone_station":
            return [V("blessing_station", "THE STONE MOSES SAT ON "
                      "(17:12) stands in the must-bless-on-seeing "
                      "list (54b:7) — the ink's own furniture as a "
                      "liturgy station; Lot's wife beside it with "
                      "the true-Judge blessing (54b:8-9)",
                      machine_claim="EX17 (the heavy-hands verse; "
                      "row named in the ledger)", **BD)]
        if q == "heal_license":
            return [V("granted_by_doubled_verb", "'and heal he "
                      "shall HEAL' (21:19) — the school of R. "
                      "Yishmael: FROM HERE, PERMISSION IS GRANTED "
                      "TO THE PHYSICIAN (60a:29), against the "
                      "bloodletting prayer's hesitation (60a:28) — "
                      "ANTICIPATED VERBATIM: EX21-07 holds the "
                      "license with the 15:26 Divine-Healer wire "
                      "since the ordinances derivation",
                      machine_claim="EX21-07 (ANTICIPATED)", **BD)]
        return None

    # ------------------------------------------------ conduct rules
    CR = _EX("Berakhot 62b:23-25 (the mount's list) + 64a:9-10 (the "
             "farewell) + Sanhedrin 5b:8-9 (the ruling license) + "
             "Shabbat 10b:4-5 (the announced gift) + Taanit 27b:9 / "
             "Beitzah 16a:10-12 (the added soul)",
             "Exod.31.13 + 31.17 + 3.5 + 4.18 + 33.7 "
             "(exo_31_craftsmen_shabbat, EX31-07 — F-078)")

    def rule_conduct(case):
        q = case.get("query")
        if q == "temple_mount_conduct":
            return [V("shoe_staff_shortcut_banned", "the mount's "
                      "conduct list: no staff, no shoe, no "
                      "money-belt, no dust, no shortcut — the shoe "
                      "from 'remove your shoes from your feet' "
                      "(3:5), spitting by the a-fortiori (62b:23; "
                      "R. Yosei b. Yehuda's sack route beside)",
                      machine_claim="EX03 (the bush charge; row "
                      "named in the ledger)", **CR)]
        if q == "farewell_formula":
            return [V("to_peace_living_in_peace_dead", "to the "
                      "living 'go TO peace' — Yitro to Moses "
                      "(4:18), who went and prospered; 'go IN "
                      "peace' is the dead's farewell (David to "
                      "Absalom the counter-exemplar) (64a:9-10)",
                      machine_claim="EX04 (the farewell verse; row "
                      "named in the ledger)", **CR)]
        if q == "ruling_jurisdiction":
            return [V("master_leave_camp_measure", "a student may "
                      "not rule without his master's PERMISSION "
                      "(5b:8, the decree), nor in his master's "
                      "jurisdiction unless THREE PARASANGS distant "
                      "— CORRESPONDING TO THE CAMP OF ISRAEL "
                      "(5b:9): the wilderness camp (33:7's "
                      "tent-outside-the-camp geometry) as the "
                      "law's unit of distance",
                      machine_claim="EX33 (the tent clause; row "
                      "named in the ledger)", **CR)]
        if q == "announced_gift":
            return [V("announce_unless_self_revealing", "THE GIVER "
                      "MUST INFORM — 'to KNOW that I the LORD "
                      "sanctify you' (31:13): 'a good gift is in "
                      "My treasury, Shabbat its name — go and "
                      "INFORM them' (10b:4); the shining-face "
                      "counter resolved: a gift bound to become "
                      "known needs no announcing — Shabbat's "
                      "REWARD is the unannounced part (10b:5; "
                      "Beitzah 16a:11's twin fork)",
                      machine_claim="EX31-07", **CR)]
        if q == "added_soul":
            return [V("given_taken_vai_read", "AN ADDED SOUL given "
                      "on Sabbath eve, taken at its close — שבת "
                      "וינפש (31:17) read 'he rested — VAI, the "
                      "soul is lost' (Taanit 27b:9; Beitzah "
                      "16a:12): the Sunday fast barred; and the "
                      "sign given IN PRIVATE ('between Me and the "
                      "children of Israel,' Beitzah 16a:10) — the "
                      "announced-gift fork's twin",
                      machine_claim="EX31-07", **CR)]
        return None

    return {
        "recitation_modes": {"fn": rule_recitation},
        "liturgy_of_the_name": {"fn": rule_name_liturgy},
        "kiddush_file": {"fn": rule_kiddush},
        "blessing_derivations": {"fn": rule_blessings},
        "conduct_rules": {"fn": rule_conduct},
    }
