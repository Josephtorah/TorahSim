# decalogue_rules.py — round 29, THE DECALOGUE (the eighteenth and
# FINAL Exodus Talmud-first exam block, 2026-09-04; owner: "Go").
# The image ban's scope run (Rosh Hashanah 24a-b with the Avodah
# Zarah 43b parallel), the duress gate, the vain-name clause's oath
# machinery, the visited iniquity, the utterances' riders, and the
# altar paragraph. Read-source:
# logic/oral_triage/exodus_block_decalogue_2026-09-04.md.


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    IMG = _EX("Rosh Hashanah 24a:18-24b:13 with the Avodah Zarah "
              "43b:4-15 parallel",
              "Exod 20:4 + 20:23 (exo_20, EX20-20 / F-109)")
    DUR = _EX("Avodah Zarah 54a:3-5",
              "Exod 20:5 (exo_20, EX20-20 / F-109)")
    OATH = _EX("Shevuot 20b:5-10, 21a:5-7, 29a:12-14",
               "Exod 20:7 (exo_20, EX20-21 / F-110)")
    INIQ = _EX("Berakhot 7a:26-28",
               "Exod 20:5 (exo_20, EX20-22 / F-111)")
    RIDE = _EX("Sanhedrin 99a:21; Bava Metzia 5b:18-20; Beitzah "
               "15b:3-5; Bava Kamma 74b:7-9; Sanhedrin 86a:15-17 "
               "(standing, the persons block)",
               "Exod 20:2 + 20:8 + 20:15-17 (exo_20, EX20-22 / F-111)")
    ALT = _EX("Zevachim 54a:7-9, 58a:4-6, 59a:10-12, 61b:3-5",
              "Exod 20:24-25 (exo_20, EX20-23 / F-112)")

    def rule_image_making(case):
        q = case.get("query")
        if q == "temple_furniture_replica":
            return [V("forbidden_replicable_attendant",
                      "לא תעשון אתי — לא תעשון כדמות שמשיי ('you shall "
                      "not make WITH ME' = 'you shall not make the "
                      "likeness of My attendants'); the Torah barred "
                      "attendants that CAN be replicated: no house after "
                      "the Sanctuary's form, no porch after the entrance "
                      "hall, no courtyard after the Temple court, "
                      "שלחן כנגד שלחן מנורה כנגד מנורה ('a table matching "
                      "the Table, a candelabrum matching the "
                      "Candelabrum') — Rosh Hashanah 24a:19-20",
                      authority="Abaye", machine_claim="EX20-20", **IMG)]
        if q == "candelabrum_lamp_count":
            return [V("permitted_off_count",
                      "one MAY make a lamp of five, six, or eight — but "
                      "of SEVEN one may not make even in other metals; "
                      "R. Yosei bar Yehuda adds even of wood, as the "
                      "Hasmonean kings did — and they answered him: the "
                      "spits were of IRON coated in tin; they grew rich "
                      "— silver; richer — gold (the poverty progression "
                      "witnesses the seven-lamp form's reach) — Rosh "
                      "Hashanah 24b:1-2",
                      authority="the baraita with R. Yosei bar Yehuda's "
                                "wood arm answered",
                      machine_claim="EX20-20", **IMG)]
        if q == "human_face_alone":
            return [V("forbidden_by_revocalization",
                      "all faces are permitted except the HUMAN face — "
                      "Rav Huna son of Rav Idi from Abaye's lecture: "
                      "לא תעשון אתי — לא תעשון אותי ('you shall not make "
                      "WITH ME' read 'you shall not make ME') — the "
                      "revocalization move on the same consonants (the "
                      "M-16 family) — Rosh Hashanah 24b:4",
                      authority="Rav Huna son of Rav Idi citing Abaye",
                      machine_claim="EX20-20", **IMG)]
        if q == "four_faces_together":
            return [V("forbidden",
                      "for non-replicable attendants the Torah barred "
                      "only דמות ארבעה פנים בהדי הדדי ('the likeness of "
                      "the four faces together') — the chariot's "
                      "four-faced creature — Rosh Hashanah 24b:3",
                      authority="Abaye", machine_claim="EX20-20", **IMG)]
        if q == "celestial_making":
            return [V("forbidden_upper_dwelling",
                      "mere MAKING of sun, moon, stars and constellations "
                      "is barred — the baraita reads them as attendants "
                      "שבמדור העליון ('of the upper dwelling'), with the "
                      "ofanim, seraphim, holy chayot and ministering "
                      "angels — Rosh Hashanah 24b:5, 24b:8; Avodah "
                      "Zarah 43b:5, 43b:9",
                      authority="Abaye", machine_claim="EX20-20", **IMG)]
        if q == "image_serving_scope":
            return [V("liable_down_to_the_worm",
                      "the SERVING ban runs the verse's own four domains: "
                      "אשר בשמים ('that is in heaven') includes sun, "
                      "moon, stars, constellations; ממעל ('above') the "
                      "ministering angels; אשר בארץ ('that is in the "
                      "earth') mountains, hills, seas, rivers; מתחת "
                      "('under') לרבות שלשול קטן ('to include even the "
                      "tiny worm') — Rosh Hashanah 24b:6-7; Avodah "
                      "Zarah 43b:6-8 (the four-domain parse)",
                      authority="the baraita, resolved to the serving ban",
                      machine_claim="EX20-20", **IMG)]
        if q == "moon_diagram_warrant":
            return [V("permitted_learn_to_rule",
                      "Rabban Gamliel's moon diagrams stand: OTHERS made "
                      "them for him and as Nasi the many were always "
                      "with him (no suspicion attaches to the many — "
                      "the Nehardea statue where Rav, Shmuel and Levi "
                      "prayed); or they were in SECTIONS; or he made "
                      "them לְהִתְלַמֵּד — לא תלמד לעשות אבל אתה למד להבין "
                      "ולהורות ('you shall not learn to DO — but you may "
                      "learn to understand and to rule,' Deut 18:9) — "
                      "Rosh Hashanah 24b:9-13",
                      authority="the sugya's three resolutions",
                      machine_claim="EX20-20", **IMG)]
        if q == "seal_ring_states":
            return [V("protruding_wear_bar_seal_ok",
                      "טבעת חותמו בולט אסור להניחה ומותר לחתום בה חותמו "
                      "שוקע מותר להניחה ואסור לחתום בה ('a ring whose "
                      "seal protrudes — forbidden to wear it, permitted "
                      "to seal with it; its seal sunken — permitted to "
                      "wear, forbidden to seal') — the suspicion runs on "
                      "the raised image either way — Rosh Hashanah "
                      "24b:10; Avodah Zarah 43b:12",
                      authority="the baraita", machine_claim="EX20-20",
                      **IMG)]
        return None

    def rule_duress_gate(case):
        if case.get("query") == "forced_worship_setting":
            return [V("private_exempt_public_dies",
                      "Rava: all were in the class of לא תעבדם ('you "
                      "shall not serve them'); when Scripture specified "
                      "וחי בהם ('and LIVE by them,' Lev 18:5) — not die "
                      "by them — duress LEFT the class; then Scripture "
                      "wrote back 'you shall not profane My holy Name' "
                      "— even under duress. How? הא בצנעא והא בפרהסיא "
                      "('this in private, that in public') — Avodah "
                      "Zarah 54a:4-5",
                      authority="Rava", machine_claim="EX20-20", **DUR)]
        return None

    def rule_vain_name_clause(case):
        q = case.get("query")
        if q == "oath_clause_assignment":
            return [V("past_false_vain_future_broken_false",
                      "Rav Dimi citing R. Yochanan: 'I ate / I did not "
                      "eat' [the PAST falsehood] is שוא ('vain'), its "
                      "warning from this clause — לא תשא את שם ה׳ אלהיך "
                      "לשוא ('you shall not take the name of the LORD "
                      "your God in vain'); 'I will eat / I will not eat' "
                      "broken is שקר ('false'), its warning from Lev "
                      "19:12 'do not swear by My name falsely' — "
                      "Shevuot 20b:6",
                      authority="Rav Dimi citing R. Yochanan",
                      machine_claim="EX20-21", **OATH)]
        if q == "vain_false_utterance":
            return [V("spoken_as_one",
                      "שוא ושקר בדיבור אחד נאמרו ('vain and false were "
                      "spoken in ONE UTTERANCE') — like זכור ושמור "
                      "('remember and keep'), what the mouth cannot "
                      "speak and the ear cannot hear — the single-"
                      "utterance pair EX20-18's own prose has carried "
                      "since derivation ('remember-and-keep in one "
                      "saying') — Shevuot 20b:9",
                      authority="the baraita",
                      machine_claim="EX20-21", **OATH)]
        if q == "speech_lash_exception":
            return [V("flogged_without_act",
                      "every negative command WITH an act is flogged, "
                      "without an act not flogged — חוץ מנשבע ומימר "
                      "ומקלל את חבירו בשם ('except the swearer, the "
                      "exchanger, and one who curses his fellow by the "
                      "Name'): the three speech-crimes flogged with no "
                      "act — Shevuot 21a:5",
                      authority="R. Yehuda in the name of R. Yosei "
                                "HaGelili",
                      machine_claim="EX20-21", **OATH)]
        if q == "guiltless_clause_split":
            return [V("heaven_holds_court_clears",
                      "כי לא ינקה ('for He will not hold guiltless') — "
                      "the court ABOVE does not clear him, but the court "
                      "BELOW flogs him and clears him; Rav Pappa's "
                      "challenge answered from the clause's own subject: "
                      "since it is written לא ינקה ה׳ ('the LORD will "
                      "not clear'), it is HE who does not clear — the "
                      "lower court flogs and clears — Shevuot 21a:6-7",
                      authority="R. Yochanan citing R. Shimon ben "
                                "Yochai, sharpened by Abaye",
                      machine_claim="EX20-21", **OATH)]
        if q == "oath_god_word_ambiguity":
            return [V("court_understanding_required",
                      "Moses swore Israel 'not on YOUR understanding "
                      "but on the Omnipresent's and mine' — because "
                      "saying 'keep what אלוה says' is ambiguous: idols "
                      "are also CALLED elo'ah, as this chapter's own "
                      "clause writes אלהי כסף ואלהי זהב ('gods of silver "
                      "and gods of gold,' Exod 20:23) — Shevuot "
                      "29a:12-13 (the oaths block's court-understanding "
                      "machinery, its Exod 20 hook now seated)",
                      authority="the sugya",
                      machine_claim="EX20-21", **OATH)]
        return None

    def rule_visiting_iniquity(case):
        if case.get("query") == "iniquity_transfer":
            return [V("visited_only_when_grasping",
                      "פקד עון אבות על בנים ('visits the iniquity of "
                      "fathers on sons,' this clause) against ובנים לא "
                      "יומתו על אבות ('sons shall not die for fathers,' "
                      "Deut 24:16) — resolved: הא כשאוחזין מעשה אבותיהם "
                      "בידיהם ('this when they grasp their fathers' "
                      "deeds in their hands'), that when they do not — "
                      "Berakhot 7a:26-27",
                      authority="the gemara's reconciliation",
                      machine_claim="EX20-22", **INIQ)]
        return None

    def rule_utterance_riders(case):
        q = case.get("query")
        if q == "anokhi_denier":
            return [V("despiser_of_the_word",
                      "the school of R. Yishmael: כי דבר ה׳ בזה ('he "
                      "despised the word of the LORD,' Num 15:31) — "
                      "זה המבזה דבור שנאמר לו למשה מסיני ('this is one "
                      "who despises the utterance said to Moses at "
                      "Sinai'): אנכי ה׳ אלהיך ('I am the LORD your God') "
                      "and לא יהיה לך ('you shall have no other') — the "
                      "idolater classified as the denier of THIS "
                      "utterance — Sanhedrin 99a:21",
                      authority="the school of R. Yishmael",
                      machine_claim="EX20-22", **RIDE)]
        if q == "covet_folk_scope":
            return [V("seizure_without_payment",
                      "Rav Acha of Difti to Ravina: 'but he violates "
                      "לא תחמוד (you shall not covet)!' — answered: "
                      "לא תחמוד לאינשי בלא דמי משמע להו ('to people, the "
                      "covet ban means taking WITHOUT payment') — the "
                      "one who pays does not see himself in the ban: "
                      "the commandment's recorded folk-parameter — "
                      "Bava Metzia 5b:19-20",
                      authority="the sugya's answer",
                      machine_claim="EX20-22", **RIDE)]
        if q == "festival_eve_provision":
            return [V("remember_verb_hook",
                      "Shmuel: the joining of cooked foods (eruv "
                      "tavshilin) hangs on זכור את יום השבת לקדשו "
                      "('remember the Sabbath day') — זכרהו מאחר שבא "
                      "להשכיחו ('remember it in the face of another day "
                      "that comes to make it forgotten'): the festival "
                      "before Shabbat; Rava's alternative — that he "
                      "select a fine portion for each — Beitzah 15b:4-5",
                      authority="Shmuel, with Rava's alternative reason",
                      machine_claim="EX20-22", **RIDE)]
        if q == "contradicted_capital_witnesses":
            return [V("flogged_not_executed",
                       "R. Elazar: עדים שהוכחשו בנפש לוקין ('witnesses "
                       "contradicted in a capital case are FLOGGED') "
                       "under לא תענה ('you shall not testify falsely') "
                       "— and had they been executable it would be a "
                       "prohibition given over to warning of court "
                       "execution, which carries no lashes (Bava Kamma "
                       "74b:8-9); EX20-14's plotting file holds the "
                       "lash arithmetic",
                       authority="R. Elazar",
                       machine_claim="EX20-22", **RIDE),
                    V("executed",
                      "the other arm: contradicted and later proven "
                      "plotting — נהרגין ('they are executed'); the "
                      "sugya assigns the arms between R. Yochanan and "
                      "R. Elazar by inference — Bava Kamma 74b:7",
                      authority="the arm assigned to R. Yochanan",
                      machine_claim="EX20-22", **RIDE)]
        if q == "theft_utterance_scope":
            return [V("persons_by_context",
                      "לא תגנב ('you shall not steal,' Exod 20:15) is "
                      "THEFT OF PERSONS — דבר הלמד מענינו ('a matter "
                      "derived from its context'): its neighbors kill "
                      "and adultery are capital; Lev 19:11's theft is "
                      "PROPERTY by ITS context — the middah named on "
                      "the commandment itself — Sanhedrin 86a:15-17 "
                      "(standing verdict, the persons block's read; "
                      "also this block's docket)",
                      authority="the baraita, the context middah named",
                      machine_claim="EX20-22", **RIDE)]
        return None

    def rule_altar_upon_it(case):
        q = case.get("query")
        if q == "altar_build_method":
            return [V("poured_frames_no_iron",
                      "Levi's baraita: they bring a frame 32 by 32, one "
                      "cubit high — polished round stones, large and "
                      "small — ומביא סיד וקוניא וזפת וממחה ושופך ('and he "
                      "brings lime, quicklime and pitch, melts and "
                      "pours'): the FOUNDATION; then 30 by 30 five "
                      "high, then 28 by 28 three high — the arrangement "
                      "place: whole stones bound by pour, no iron ever "
                      "swung (the sword-profanes clause EX20-12 holds) "
                      "— Zevachim 54a:8-9",
                      authority="Levi's baraita",
                      machine_claim="EX20-23", **ALT)]
        if q == "altar_top_slaughter":
            return [V("whole_top_either",
                       "R. Yochanan: both expound ONE verse — וזבחת "
                       "עליו את עולתיך ואת שלמיך ('and you shall "
                       "sacrifice UPON IT your burnt-offerings and "
                       "your peace-offerings'): R. Yosei — ALL of the "
                       "top fit for either offering — Zevachim 58a:5-6",
                       authority="R. Yosei",
                       machine_claim="EX20-23", **ALT),
                    V("half_burnt_half_peace",
                      "R. Yosei son of R. Yehuda: HALF for the "
                      "burnt-offering, half for the peace-offering — "
                      "the top split north and south — Zevachim 58a:6",
                      authority="R. Yosei son of R. Yehuda",
                      machine_claim="EX20-23", **ALT)]
        if q == "damaged_altar_offerings":
            return [V("slaughtered_there_invalid",
                       "Rav: מזבח שנפגם כל הקדשים שנשחטו שם פסולין ('an "
                       "altar that was damaged — all offerings "
                       "slaughtered there are invalid') — the verse he "
                       "had lost and R. Shimon b. Rabbi restored: "
                       "וזבחת עליו — 'upon it' when WHOLE, not when "
                       "lacking; living animals are not rejected — "
                       "Zevachim 59a:10-11",
                       authority="Rav",
                       machine_claim="EX20-23", **ALT),
                    V("both_invalid",
                      "R. Yochanan: both invalid — living animals ARE "
                      "rejected while the altar stands damaged — "
                      "Zevachim 59a:12",
                      authority="R. Yochanan",
                      machine_claim="EX20-23", **ALT)]
        if q == "altar_material_history":
            return [V("three_stones_tokens_three_houses",
                      "Rav Huna citing Rav: Shiloh's altar was of "
                      "STONES — R. Eliezer ben Yaakov's baraita: "
                      "אבנים אבנים אבנים שלש פעמים ('stones, stones, "
                      "stones — three times,' Exod 20:25 with Deut "
                      "27's pair) — one for Shiloh, one for Nov and "
                      "Gibeon, one for the Eternal House: the token "
                      "census assigning the altar's material through "
                      "history — Zevachim 61b:4",
                      authority="Rav Huna citing Rav",
                      machine_claim="EX20-23", **ALT)]
        return None

    return {
        "image_making": {"fn": rule_image_making,
                         "tractate": "Rosh Hashanah"},
        "duress_gate": {"fn": rule_duress_gate,
                        "tractate": "Avodah Zarah"},
        "vain_name_clause": {"fn": rule_vain_name_clause,
                             "tractate": "Shevuot"},
        "visiting_iniquity": {"fn": rule_visiting_iniquity,
                              "tractate": "Berakhot"},
        "utterance_riders": {"fn": rule_utterance_riders,
                             "tractate": "Sanhedrin"},
        "altar_upon_it": {"fn": rule_altar_upon_it,
                          "tractate": "Zevachim"},
    }
