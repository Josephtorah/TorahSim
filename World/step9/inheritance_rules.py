# inheritance_rules.py — round 34, INHERITANCE, DEEDS, AND SURETY
# (Genesis exam block 5 of 12, 2026-09-04). Read-source:
# logic/oral_triage/genesis_block_inheritance_2026-09-04.md.


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    LD = _EX("Bava Batra 56a:8-9, 69b:1; Bekhorot 50a:7-9",
             "Gen 23:16-17 + 15:18 (gen_39 G39-35 / F-128; gen_31 "
             "G31-21 / F-129)")
    IC = _EX("Bava Batra 110b:8-10, 113a:3-5, 123a:9-11, 143b:5-7",
             "Gen 42:13 + 48:5 + 46:23 (gen_65 G65-34 / F-132; "
             "gen_71 G71-29 / F-130; gen_69 G69-30 / F-135)")
    SR = _EX("Bava Batra 173b:8-11",
             "Gen 43:9 + 42:37 (gen_66 G66-35 / F-131; gen_65 "
             "G65-34 / F-132)")
    ED = _EX("Sanhedrin 91a:7-9, 91a:15-17",
             "Gen 9:25 + 25:5-6 (gen_23 G23-16 / F-133; gen_42 "
             "G42-29 / F-134)")
    KF = _EX("Horayot 5b:14-16, 6b:1-3",
             "Gen 48:4-6 (gen_71, G71-29 / F-130)")

    def rule_land_and_deeds(case):
        q = case.get("query")
        if q == "covenant_land_exclusion":
            return [V("three_nations_outside_tithe",
                      "whatever the Holy One showed Moses is "
                      "tithe-bound — לאפוקי קיני קניזי וקדמוני ('to "
                      "EXCLUDE the Kenite, the Kenizzite, and the "
                      "Kadmonite,' Gen 15:19's own list): the "
                      "covenant's land list as boundary law, with "
                      "the three tannaitic identifications recorded "
                      "(R. Meir, R. Yehuda, R. Shimon) — Bava Batra "
                      "56a:8-9",
                      authority="Rav Yehuda citing Shmuel, with the "
                                "three identification arms",
                      machine_claim="G31-21", **LD)]
        if q == "deed_boundary_source":
            return [V("border_clause_from_machpelah",
                      "ויקם שדה עפרון ('and the field of Ephron "
                      "AROSE') with בכל גבלו סביב ('in all its "
                      "border round about,' Gen 23:17): one who "
                      "needs a boundary — excluded those that need "
                      "none; Rav Mesharshiya: מכאן למצרים מן התורה "
                      "('from here — boundaries from the Torah'): "
                      "the deed's border clause drafted from our "
                      "purchase — Bava Batra 69b:1",
                      authority="Rav Yehuda citing Rav, with Rav "
                                "Mesharshiya",
                      machine_claim="G39-35", **LD)]
        if q == "walking_acquisition":
            return [V("walking_acquires_r_eliezer",
                      "R. Eliezer: WALKING a parcel acquires it — "
                      "קום התהלך בארץ ('arise, WALK the land in its "
                      "length and breadth, for to you I give it,' "
                      "Gen 13:17) — Bava Batra 100a:7; STANDING "
                      "SEAT: G29-18 has held the mode with its "
                      "dispute since the reading",
                      authority="R. Eliezer",
                      machine_claim="G29-18 (standing)", **LD)]
        if q == "ephron_currency_exception":
            return [V("centenaria_despite_plain",
                      "R. Chanina's three-corpus table: every plain "
                      "'silver' in the TORAH is a sela, in the "
                      "PROPHETS litrin, in the WRITINGS kintarin "
                      "(centenaria) — חוץ מן כספו של עפרון ('EXCEPT "
                      "the silver of EPHRON'): though written "
                      "plain, centenaria — עבר לסחר ('current with "
                      "the merchant,' Gen 23:16), for there are "
                      "places that call a centenarium a shekel — "
                      "Bekhorot 50a:8",
                      authority="R. Chanina",
                      machine_claim="G39-35", **LD)]
        return None

    def rule_inheritance_canon(case):
        q = case.get("query")
        if q == "paternal_brotherhood":
            return [V("father_not_mother",
                      "paternal brothers inherit: Rabbah — אתיא "
                      "אחוה אחוה מבני יעקב ('brotherhood-brotherhood "
                      "derived from the SONS OF JACOB,' Gen 42:13): "
                      "as there from the father and not the mother, "
                      "so here — with the family-of-the-father "
                      "completion at 110b:10 — Bava Batra 110b:9-10",
                      authority="Rabbah",
                      machine_claim="G65-34", **IC)]
        if q == "cleave_word_inheritance":
            return [V("doubled_cleave_token",
                      "the husband-inheritance derivation: Rav "
                      "Nachman bar Yitzchak — ידבקו תרוייהו ידבקו "
                      "כתיב בהו ('THEY SHALL CLEAVE — in both "
                      "verses the cleave-verb is written'): the "
                      "doubled token of the cleave-family whose "
                      "Torah root is Gen 2:24's ve-davak, with "
                      "Rava's and Rav Ashi's routes recorded "
                      "beside — Bava Batra 113a:3-5",
                      authority="Rav Nachman bar Yitzchak, with "
                                "Rava and Rav Ashi's routes",
                      machine_claim="G65-34", **IC)]
        if q == "tribal_double_portion":
            return [V("like_reuben_and_simeon",
                      "Joseph's double portion: Rav Pappa — perhaps "
                      "a mere palm tree? Abaye: עליך אמר קרא אפרים "
                      "ומנשה כראובן ושמעון יהיו לי ('against you the "
                      "verse says: EPHRAIM AND MANASSEH shall be to "
                      "me LIKE REUBEN AND SIMEON,' Gen 48:5) — two "
                      "full tribal shares — Bava Batra 123a:9-10",
                      authority="Abaye",
                      machine_claim="G71-29", **IC)]
        if q == "bnei_canon":
            return [V("one_child_written_plural",
                      "do people call one son 'sons'? Abaye: ובני דן "
                      "חשים ('and the SONS of Dan — CHUSHIM,' Gen "
                      "46:23, one child written plural); Rava's "
                      "recorded deflection (perhaps 'like "
                      "reed-thickets,' the school of Chizkiya) with "
                      "the two replacement seats — 'sons of Pallu: "
                      "Eliav' (Num 26:8), 'sons of Ethan: Azariah' "
                      "(1 Chr 2:8): a three-verse ink-canon, our "
                      "token the opener — Bava Batra 143b:5-7",
                      authority="Abaye, Rava, and Rav Yosef",
                      machine_claim="G69-30", **IC)]
        return None

    def rule_surety_root(case):
        q = case.get("query")
        if q == "guarantor_source":
            return [V("judah_pledge_root",
                      "Rav Huna: whence that a guarantor becomes "
                      "OBLIGATED? — אנכי אערבנו מידי תבקשנו ('I will "
                      "be SURETY for him — from MY HAND you shall "
                      "require him,' Gen 43:9): Judah's pledge as "
                      "surety law's root — Bava Batra 173b:9",
                      authority="Rav Huna",
                      machine_claim="G66-35", **SR)]
        if q == "unconditional_guarantor":
            return [V("reuben_pledge_type",
                      "Rav Chisda's objection types the pledges: "
                      "that is KABBLANUT ('unconditional "
                      "assumption') — תנה אתו על ידי ואני אשיבנו "
                      "('GIVE HIM INTO MY HAND and I will return "
                      "him,' Gen 42:37, Reuben's form): the "
                      "guarantor taxonomy drawn between the two "
                      "brothers' own clauses (the final proof "
                      "moving to Proverbs 20:16) — Bava Batra "
                      "173b:10-11",
                      authority="Rav Chisda's classification",
                      machine_claim="G65-34", **SR)]
        return None

    def rule_estate_doctrines(case):
        q = case.get("query")
        if q == "slave_property_doctrine":
            return [V("master_owns_acquisitions",
                      "Geviha ben Pesisa before Alexander, against "
                      "the claim from Africa: 'I bring proof only "
                      "from the Torah' — ארור כנען עבד עבדים יהיה "
                      "לאחיו ('cursed be Canaan; a SLAVE of slaves "
                      "shall he be,' Gen 9:25): עבד שקנה נכסים עבד "
                      "למי ונכסים למי ('a slave who acquired "
                      "property — the slave to whom, and the "
                      "property to whom?') — what a slave acquires "
                      "his master owns; the claimants fled leaving "
                      "sown fields — Sanhedrin 91a:7-9",
                      authority="Geviha ben Pesisa, the recorded "
                                "adjudication",
                      machine_claim="G23-16", **ED)]
        if q == "lifetime_gift_deeds":
            return [V("deeds_settle_inheritance",
                      "against the concubines' sons' claim: ויתן "
                      "אברהם את כל אשר לו ליצחק ('Abraham GAVE all "
                      "he had to Isaac') and נתן אברהם מתנת ('to "
                      "the concubines' sons Abraham gave GIFTS,' "
                      "Gen 25:5-6) — a father "
                      "who deeded in his lifetime and sent them "
                      "from one another: none has a claim on the "
                      "other; R. Yirmiya bar Abba's rider on what "
                      "the 'gifts' were — Sanhedrin 91a:15-16",
                      authority="Geviha ben Pesisa, the recorded "
                                "adjudication",
                      machine_claim="G42-29", **ED)]
        return None

    def rule_kahal_file(case):
        q = case.get("query")
        if q == "kahal_definition":
            return [V("single_tribe_is_kahal",
                      "Rav Acha bar Yaakov: הנני מפרך והרביתך ונתתיך "
                      "לקהל עמים ('behold, I will make you fruitful "
                      "and make you a KAHAL of peoples,' Gen 48:4) "
                      "— said when BENJAMIN alone was yet to be "
                      "born: 'another kahal is being born to you' — "
                      "a single tribe is called a congregation — "
                      "Horayot 5b:15 (Rav Sheva's challenge at "
                      "5b:16 recorded)",
                      authority="Rav Acha bar Yaakov",
                      machine_claim="G71-29", **KF)]
        if q == "levi_kahal_exclusion":
            return [V("holding_defines_kahal",
                      "the tribe of LEVI is not called kahal — from "
                      "the same verse: כל שיש לו אחוזה איקרי קהל "
                      "('whoever HAS A HOLDING is called kahal; no "
                      "holding, no kahal'); then only eleven! — "
                      "Abaye: 'Ephraim and Manasseh like Reuben "
                      "and Simeon' (48:5); Rava: 'on the name of "
                      "their brothers they shall be called in "
                      "their inheritance' (48:6) — equated for "
                      "INHERITANCE, not for another matter: the "
                      "very token round 33 seated for the levirate "
                      "name, now bounding the kahal count — "
                      "Horayot 6b:1-3",
                      authority="Rav Acha son of R. Yaakov, with "
                                "Abaye and Rava",
                      machine_claim="G71-29", **KF)]
        return None

    return {
        "land_and_deeds": {"fn": rule_land_and_deeds,
                           "tractate": "Bava Batra"},
        "inheritance_canon": {"fn": rule_inheritance_canon,
                              "tractate": "Bava Batra"},
        "surety_root": {"fn": rule_surety_root,
                        "tractate": "Bava Batra"},
        "estate_doctrines": {"fn": rule_estate_doctrines,
                             "tractate": "Sanhedrin"},
        "kahal_file": {"fn": rule_kahal_file,
                       "tractate": "Horayot"},
    }
