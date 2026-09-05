# table_knife_rules.py — round 37, THE TABLE AND THE KNIFE (Genesis
# exam block 8 of 12, 2026-09-04). Read-source:
# logic/oral_triage/genesis_block_table_knife_2026-09-04.md.


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    SF = _EX("Chullin 16a:4-6, 85a:11-13, 90b:3-5",
             "Gen 22:10 + 43:16 + 32:33 (gen_38 G38-41 / F-151; "
             "gen_66 G66-37 / F-153; gen_55 G55-37 / F-155)")
    DF = _EX("Chullin 113a:19-20, 113b:1-3, 139b:18-20; Bava Kamma "
             "55a:11-13, 65b:17-19",
             "Gen 38:20 + 7:14 + 31:38 + 1:21 (gen_61 G61-19 / "
             "F-158; gen_17 G17-18 / F-159; gen_54 G54-43 / F-160; "
             "gen_05 G05-08 / F-161)")
    SG = _EX("Chullin 95b:7-9, 95b:13-15",
             "Gen 24:14 + 42:36 (gen_40 G40-36 / F-156; gen_65 "
             "G65-36 / F-157)")
    RO = _EX("Chullin 89a:3-5, 60b:11-13",
             "Gen 14:24 + 21:23 (gen_30 G30-32 / F-154; gen_37 "
             "G37-31 / F-152)")

    def rule_slaughter_file(case):
        q = case.get("query")
        if q == "detached_blade":
            return [V("valid_with_detached",
                      "whence that slaughter is valid with a "
                      "DETACHED blade? — ויקח את המאכלת לשחט ('and "
                      "he took THE KNIFE to slay,' Gen 22:10): "
                      "Rebbi's derivation at the binding's own "
                      "instrument, with Rav's recorded quip and the "
                      "answer — the verse also teaches Abraham's "
                      "ZEAL — Chullin 16a:5",
                      authority="Rebbi, with the zeal rider",
                      machine_claim="G38-41", **SF)]
        if q == "fitting_slaughter":
            return [V("r_shimon_fit_slaughter_source",
                      "R. Shimon's requirement of FITTING slaughter: "
                      "גמר מטבח טבח והכן ('derived from SLAUGHTER A "
                      "SLAUGHTERING AND PREPARE,' Gen 43:16 — "
                      "Joseph's kitchen order): as there a slaughter "
                      "fit for eating, so everywhere; R. Meir's "
                      "counter-canon (slaughter is derived from "
                      "slaughter, not from slaughtering) recorded "
                      "beside — Chullin 85a:12-13",
                      authority="R. Mani bar Pattish stating R. "
                                "Shimon's reason",
                      machine_claim="G66-37", **SF)]
        if q == "sinew_subject_scope":
            return [V("israel_not_the_altar",
                      "the sinew of a burnt-offering: Rav Huna — "
                      "removed; Rav Chisda's retort: מי כתיב על כן "
                      "לא יאכל המזבח ('is it written: the ALTAR "
                      "shall not eat it?') — על כן לא יאכלו בני "
                      "ישראל כתיב ('the CHILDREN OF ISRAEL shall "
                      "not eat' is what is written,' Gen 32:33): "
                      "the ban's SUBJECT is Israel, not the fire — "
                      "with Rav Huna's from-Israel's-permitted "
                      "counter-principle — Chullin 90b:4-5",
                      authority="Rav Chisda against Rav Huna, both "
                                "recorded",
                      machine_claim="G55-37", **SF)]
        return None

    def rule_definition_file(case):
        q = case.get("query")
        if q == "kid_definition":
            return [V("plain_kid_includes_cow_ewe",
                      "the meat-milk KID defined: R. Elazar — וישלח "
                      "יהודה את גדי העזים ('Judah sent the KID OF "
                      "THE GOATS,' Gen 38:20): where Scripture "
                      "means goats it SAYS goats — plain gedi "
                      "includes cow and ewe; the second leg at "
                      "27:16's skins-of-the-kids-of-goats, the "
                      "two-verses-as-one discipline worked through "
                      "— Chullin 113a:20-113b:3",
                      authority="R. Elazar",
                      machine_claim="G61-19", **DF)]
        if q == "bird_wing_tokens":
            return [V("ark_tokens_in_bird_law",
                      "the bird-law dialectic probes כל צפור כל כנף "
                      "('every BIRD, every WING,' Gen 7:14 — the "
                      "ark's own roster): is tzippor the pure bird "
                      "and kanaf the winged class? — the ark's "
                      "taxonomy tokens serving as the sugya's test "
                      "verse — Chullin 139b:18-20",
                      authority="the sugya's dialectic",
                      machine_claim="G17-18", **DF)]
        if q == "day_old_ram":
            return [V("day_old_called_ram",
                      "Rava: a day-old ox is an 'ox' — and a "
                      "day-old RAM is a 'ram': ואילי צאנך לא אכלתי "
                      "('the RAMS of your flock I have not eaten,' "
                      "Gen 31:38) — rams he did not eat, lambs he "
                      "ate?! Rather: a day-old ram is called RAM — "
                      "the age-definition from Jacob's protest — "
                      "Bava Kamma 65b:17-18",
                      authority="Rava",
                      machine_claim="G54-43", **DF)]
        if q == "sea_kilayim":
            return [V("lashes_by_land_analogy",
                      "R. Yirmiya citing Reish Lakish: breeding two "
                      "SEA species — LASHES: אתיא למינהו למינהו "
                      "מיבשה ('derived by ITS-KIND from ITS-KIND, "
                      "from the dry land' — Gen 1:21's sea kinds "
                      "read through 1:25's land kinds): creation "
                      "ink as forbidden-mixture law, with Rachava's "
                      "goat-and-shibbuta driving query beside — "
                      "Bava Kamma 55a:12-13",
                      authority="Rav Adda bar Ahava in Ulla's name",
                      machine_claim="G05-08", **DF)]
        return None

    def rule_sign_file(case):
        q = case.get("query")
        if q == "divination_paradigm":
            return [V("eliezer_test_defines_ban",
                      "Rav: כל נחש שאינו כאליעזר עבד אברהם ('any "
                      "DIVINATION not like Eliezer Abraham's "
                      "servant's — and Jonathan son of Saul's — is "
                      "no divination'): the maiden-test of Gen "
                      "24:14 as the nichush ban's PARADIGM CASE — "
                      "the definition by exemplar, with the sages' "
                      "own sign-practices recorded beside (the "
                      "ferry, the book, the child) — Chullin "
                      "95b:8-9",
                      authority="Rav",
                      machine_claim="G40-36", **SG)]
        if q == "three_time_chazakah":
            return [V("established_three_times",
                      "a house, a child, a wife are a SIGN, not "
                      "divination — R. Elazar: והוא דאיתחזק תלתא "
                      "זימני ('and that is when ESTABLISHED THREE "
                      "TIMES') — דכתיב יוסף איננו ושמעון איננו ואת "
                      "בנימין תקחו ('as it is written: Joseph is "
                      "gone, Simeon is gone, and Benjamin you "
                      "would take,' Gen 42:36): the presumption's "
                      "THREE-COUNT drawn from Jacob's own sentence "
                      "— Chullin 95b:13-14",
                      authority="R. Elazar",
                      machine_claim="G65-36", **SG)]
        return None

    def rule_robbery_and_oath(case):
        q = case.get("query")
        if q == "consumed_robbery":
            return [V("unrestorable_even_by_righteous",
                      "R. Abba: קשה גזל הנאכל ('CONSUMED robbery is "
                      "hard') — even the perfectly righteous cannot "
                      "restore it: בלעדי רק אשר אכלו הנערים ('save "
                      "only what the lads have EATEN,' Gen 14:24) — "
                      "Abram returns everything except what was "
                      "eaten: the restitution boundary at "
                      "consumption — Chullin 89a:4",
                      authority="R. Abba",
                      machine_claim="G30-32", **RO)]
        if q == "standing_oath_bar":
            return [V("conquest_routed_around_oath",
                      "Reish Lakish's 'verses fit to burn that are "
                      "the BODY of Torah': the Avvim notice matters "
                      "because Abimelech's oath — אם תשקר לי ולניני "
                      "ולנכדי ('if you deal falsely with me, my "
                      "offspring, my posterity,' Gen 21:23) — BARRED "
                      "Israel from Philistine land: the Caphtorim "
                      "took it from the Avvim first, and Israel "
                      "from the Caphtorim — the canon records the "
                      "workaround that keeps a patriarch's oath — "
                      "Chullin 60b:11-12",
                      authority="Reish Lakish's canon with the "
                                "recorded route",
                      machine_claim="G37-31", **RO)]
        return None

    return {
        "slaughter_file": {"fn": rule_slaughter_file,
                           "tractate": "Chullin"},
        "definition_file": {"fn": rule_definition_file,
                            "tractate": "Chullin"},
        "sign_file": {"fn": rule_sign_file,
                      "tractate": "Chullin"},
        "robbery_and_oath": {"fn": rule_robbery_and_oath,
                             "tractate": "Chullin"},
    }
