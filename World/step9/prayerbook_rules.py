# prayerbook_rules.py — round 30, THE PRAYER BOOK OF THE PATRIARCHS
# (the first block of the GENESIS campaign, 2026-09-04; owner: "Do 3
# then 2"). The three instituted prayers with the offerings arm, the
# fixed place, the six-hours constant, the day boundary's two liturgy
# jobs, the silent line, the visited-Sarah dispute, and three
# standing seats consumed as credits. Read-source:
# logic/oral_triage/genesis_block_prayerbook_2026-09-04.md.


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    PP = _EX("Berakhot 26b:4-10, 27a:9-11",
             "Gen 19:27 + 24:63 + 28:11 + 18:1 (gen_35, G35-26 / "
             "F-113)")
    PR = _EX("Berakhot 2a:8-10, 6b:7-9, 26a:16-18",
             "Gen 19:27 + 1:5 (gen_35 G35-26 / F-113; gen_01 G01-07 "
             "/ F-116)")
    SL = _EX("Pesachim 56a:6-8",
             "Gen 49:1 (gen_72, G72-34 / F-114)")
    RV = _EX("Rosh Hashanah 32b:4-6",
             "Gen 21:1 (gen_37, G37-30 / F-115)")
    PL = _EX("Berakhot 13a:8; Pesachim 117b:11; Chullin 49a:18 "
             "(standing seats)",
             "Gen 17:5 + 12:2-3 (gen_33 G33-20; gen_27 G27-18, "
             "G27-22)")

    def rule_patriarch_prayers(case):
        q = case.get("query")
        if q == "three_prayers_source":
            return [V("patriarchs_instituted",
                       "תפלות אבות תקנום ('the PATRIARCHS instituted "
                       "the prayers') — with a baraita in support: the "
                       "three founder rows below — Berakhot 26b:4-5",
                       authority="R. Yosei son of R. Chanina",
                       machine_claim="G35-26", **PP),
                    V("against_daily_offerings",
                      "תפלות כנגד תמידין תקנום ('the prayers were "
                      "instituted AGAINST THE DAILY OFFERINGS') — with "
                      "a baraita in support: each prayer's time limit "
                      "is its offering's clock — Berakhot 26b:4, "
                      "26b:8-10; the sugya keeps BOTH baraitot",
                      authority="R. Yehoshua ben Levi", **PP)]
        if q == "morning_prayer_founder":
            return [V("abraham_standing",
                      "אברהם תקן תפלת שחרית ('Abraham instituted the "
                      "morning prayer') — וישכם אברהם בבקר אל המקום "
                      "אשר עמד שם ('Abraham rose early to the place "
                      "where he had STOOD,' Gen 19:27), and אין עמידה "
                      "אלא תפלה ('standing is nothing but prayer' — "
                      "'Pinchas STOOD and prayed,' Ps 106:30): the "
                      "verbal analogy on the standing-verb — Berakhot "
                      "26b:5",
                      authority="the baraita",
                      machine_claim="G35-26", **PP)]
        if q == "afternoon_prayer_founder":
            return [V("isaac_meditation",
                      "יצחק תקן תפלת מנחה ('Isaac instituted the "
                      "afternoon prayer') — ויצא יצחק לשוח בשדה לפנות "
                      "ערב ('Isaac went out to MEDITATE in the field "
                      "toward evening,' Gen 24:63), and אין שיחה אלא "
                      "תפלה ('meditation is nothing but prayer' — 'he "
                      "pours out his siach before the LORD,' Ps "
                      "102:1) — Berakhot 26b:6",
                      authority="the baraita", **PP)]
        if q == "evening_prayer_founder":
            return [V("jacob_encounter",
                      "יעקב תקן תפלת ערבית ('Jacob instituted the "
                      "evening prayer') — ויפגע במקום וילן שם ('he "
                      "ENCOUNTERED the place and lodged,' Gen 28:11), "
                      "and אין פגיעה אלא תפלה ('encounter is nothing "
                      "but prayer' — 'do not ENCOUNTER Me,' Jer "
                      "7:16) — Berakhot 26b:7",
                      authority="the baraita", **PP)]
        if q == "prayer_time_limits":
            return [V("until_midday",
                       "the morning prayer until MIDDAY — שהרי תמיד "
                       "של שחר קרב והולך עד חצות ('for the morning "
                       "daily offering is brought until midday'): the "
                       "offering's clock is the prayer's — Berakhot "
                       "26b:8",
                       authority="the sages",
                       machine_claim="G35-26", **PP),
                    V("until_four_hours",
                      "R. Yehuda: until FOUR hours — for the morning "
                      "daily offering is brought until four hours — "
                      "Berakhot 26b:8 (the afternoon and evening rows "
                      "follow at 26b:9-10: until evening or the "
                      "afternoon's plag; the evening prayer has no "
                      "fixed limit, for the limbs and fats burn all "
                      "night)",
                      authority="R. Yehuda", **PP)]
        if q == "heat_of_day_hours":
            return [V("six_hours",
                      "כחם היום הרי שש שעות אמור ('as the HEAT OF THE "
                      "DAY — six hours is stated,' Gen 18:1's own "
                      "token) against וחם השמש ונמס ('the sun grew hot "
                      "and it melted,' the manna's token) = four "
                      "hours: the two heat-phrases assigned their "
                      "hours, our verse carrying the six — Berakhot "
                      "27a:9-11",
                      authority="the baraita, both arms keeping the "
                                "four-hours reading",
                      machine_claim="G35-26", **PP)]
        return None

    def rule_prayer_practice(case):
        q = case.get("query")
        if q == "fixed_prayer_place":
            return [V("abraham_precedent",
                      "whence that Abraham FIXED A PLACE? — אל המקום "
                      "אשר עמד שם ('to the place where he had STOOD,' "
                      "Gen 19:27): he returned to the same standing- "
                      "place; whoever fixes a place for prayer is "
                      "called of Abraham's disciples — Berakhot "
                      "6b:7-8",
                      authority="the gemara",
                      machine_claim="G35-26", **PR)]
        if q == "missed_prayer_makeup":
            return [V("next_prayer_twice",
                      "erred and missed the afternoon — prays the "
                      "evening TWICE (R. Yochanan); the dilemma's own "
                      "hinge was our day-boundary: missed-evening "
                      "makes morning-twice משום דחד יומא הוא ('because "
                      "it is ONE DAY') — ויהי ערב ויהי בקר יום אחד "
                      "('and it was evening and it was morning, one "
                      "day,' Gen 1:5) — and prayer is MERCY, not a "
                      "lapsed offering — Berakhot 26a:17-18",
                      authority="R. Yochanan",
                      machine_claim="G01-07", **PR)]
        if q == "shema_evening_first":
            return [V("creation_order",
                      "why does the evening Shema come first in the "
                      "Mishnah? — יליף מברייתו של עולם ('learned from "
                      "the CREATION OF THE WORLD'): ויהי ערב ויהי בקר "
                      "יום אחד ('and it was evening and it was "
                      "morning, one day,' Gen 1:5) — night precedes "
                      "day in the liturgy because it precedes day in "
                      "the world's boot sequence — Berakhot 2a:9",
                      authority="the gemara's second answer",
                      machine_claim="G01-07", **PR)]
        return None

    def rule_silent_line(case):
        if case.get("query") == "blessed_name_silent":
            return [V("said_in_a_whisper",
                      "at Jacob's deathbed — ויקרא יעקב אל בניו ('and "
                      "Jacob called to his sons,' Gen 49:1) — he "
                      "sought to reveal the end and the Presence "
                      "left; the sons answered SHEMA ('as your heart "
                      "holds only One, so do ours'), and Jacob "
                      "answered ברוך שם כבוד מלכותו לעולם ועד "
                      "('Blessed is the Name of His glorious kingdom "
                      "forever'). The sages: Moses did not say it; "
                      "Jacob did — התקינו שיהו אומרים אותו בחשאי "
                      "('they instituted saying it SILENTLY'), the "
                      "princess-and-gravy parable beside — Pesachim "
                      "56a:7-8",
                      authority="R. Shimon ben Lakish with the "
                                "sages' enactment",
                      machine_claim="G72-34", **SL)]
        return None

    def rule_remembrance_verses(case):
        if case.get("query") == "visited_sarah_status":
            return [V("counts_as_remembrance",
                       "פקדונות הרי הן כזכרונות ('VISITINGS are like "
                       "remembrances') — וה׳ פקד את שרה ('and the LORD "
                       "visited Sarah,' Gen 21:1) may serve as a "
                       "remembrance-verse; and though Sarah's is an "
                       "individual's — כיון דאתו רבים מינה כרבים דמיא "
                       "('since the MANY came from her, it is as the "
                       "many's') — Rosh Hashanah 32b:5-6",
                       authority="R. Yosei",
                       machine_claim="G37-30", **RV),
                    V("not_a_remembrance",
                      "R. Yehuda: visitings are NOT like remembrances "
                      "— the verse does not serve the liturgy's "
                      "remembrance slot — Rosh Hashanah 32b:5",
                      authority="R. Yehuda", **RV)]
        return None

    def rule_patriarch_liturgy(case):
        q = case.get("query")
        if q == "abram_name_ban":
            return [V("positive_command_breached",
                       "כל הקורא לאברהם אברם עובר בעשה ('whoever calls "
                       "Abraham ABRAM transgresses a POSITIVE "
                       "command') — 'your name SHALL BE Abraham' (Gen "
                       "17:5) — Berakhot 13a:8; STANDING SEAT: G33-20 "
                       "has held the row with both arms and the "
                       "Sarai/Jacob contrasts since the reading",
                       authority="Bar Kappara",
                       machine_claim="G33-20 (standing)", **PL),
                    V("negative_command_breached",
                      "R. Eliezer: a NEGATIVE command — 'your name "
                      "shall NO MORE be called Abram' — the second "
                      "arm, held at the same seat — Berakhot 13a:8",
                      authority="R. Eliezer",
                      machine_claim="G33-20 (standing)", **PL)]
        if q == "amidah_patriarch_opening":
            return [V("clause_mapped_blessing",
                      "the Amidah's opening blessing is Gen 12:2's "
                      "clause map — 'I will make you a great nation' "
                      "= אלהי אברהם ('God of Abraham'), 'I will bless "
                      "you' = God of Isaac, 'I will make your name "
                      "great' = God of Jacob; 'and BE a blessing' — "
                      "with YOU the blessing seals — Pesachim "
                      "117b:11; STANDING SEAT: G27-22 (Reish "
                      "Lakish's map, held since the reading)",
                      authority="R. Shimon ben Lakish",
                      machine_claim="G27-22 (standing)", **PL)]
        if q == "priests_return_blessing":
            return [V("blessers_blessed",
                      "ואברכה מברכיך ('and I will bless THOSE WHO "
                      "BLESS YOU,' Gen 12:3) — R. Akiva's source that "
                      "the blessing priests are themselves blessed — "
                      "Chullin 49a:18; STANDING SEAT: G27-18 held the "
                      "warrant with its second Babylonian seat before "
                      "this block opened",
                      authority="R. Akiva",
                      machine_claim="G27-18 (standing)", **PL)]
        return None

    return {
        "patriarch_prayers": {"fn": rule_patriarch_prayers,
                              "tractate": "Berakhot"},
        "prayer_practice": {"fn": rule_prayer_practice,
                            "tractate": "Berakhot"},
        "silent_line": {"fn": rule_silent_line,
                        "tractate": "Pesachim"},
        "remembrance_verses": {"fn": rule_remembrance_verses,
                               "tractate": "Rosh Hashanah"},
        "patriarch_liturgy": {"fn": rule_patriarch_liturgy,
                              "tractate": "Berakhot"},
    }
