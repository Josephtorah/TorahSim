#!/usr/bin/env python3
"""shabbat_rules.py — round 17: SHABBAT'S MACHINERY, the sixth Exodus
Talmud-first exam block (2026-09-04). Ten modules over Exodus 16,
20:9-10, 31:12-17, 35:1-3, 36:6 — the twice-drawn import edge run at
last. engine.py merges build(V) at its tail.
Read-source record: logic/oral_triage/exodus_block_shabbat_2026-09-04.md."""


def build(V):
    def _EX(talmud, anchor, **extra):
        d = dict(talmud_source=talmud, exodus_anchor=anchor)
        d.update(extra)
        return d

    # -------------------------------------------- the forgetting machine
    FM = _EX("Shabbat 69b:6-70a:1 (Rava's desert protocol; the "
             "verse-pair of Rav Nachman/Rabba bar Avuh with Rav "
             "Nachman bar Yitzchak's reversal; Rav Nachman's "
             "unwittingness-count answer)",
             "Exod.31.14-16 (exo_31_craftsmen_shabbat, EX31-05 the "
             "Great Principle grid — ANTICIPATED; F-061 seats the "
             "derivation file)",
             mishnah="Mishnah Shabbat 7:1")

    def rule_forgetting(case):
        q = case.get("query")
        if q == "forgot_essence_offering":
            return [V("one_for_all", "forgot the very principle of "
                      "Shabbat — ONE offering for everything: the "
                      "singular 'the Shabbat' of Exod 31:16 read as "
                      "one observance for many Shabbatot (Rav Nachman "
                      "citing Rabba bar Avuh; Rav Nachman bar "
                      "Yitzchak reverses which verse carries which "
                      "arm — the grid stands either way)",
                      machine_claim="EX31-05", **FM)]
        if q == "forgot_days_offering":
            return [V("one_per_shabbat", "knew the principle, forgot "
                      "the day — one offering PER SHABBAT: the plural "
                      "'My Shabbatot' (Lev 26:2) supplies the "
                      "per-Shabbat arm; unwitting about ONE matter "
                      "(Rav Nachman's count at 70a:1)",
                      machine_claim="EX31-05", **FM)]
        if q == "forgot_labors_offering":
            return [V("one_per_labor", "knew the day, forgot the "
                      "labors — one offering PER LABOR CATEGORY: "
                      "unwitting about MANY matters; the offering "
                      "follows the unwittingness count (Rav Nachman, "
                      "70a:1)", machine_claim="EX31-05", **FM)]
        if q == "desert_lost_count":
            return [V("count_six_keep_seventh", "lost the day in the "
                      "desert: count six days and keep a seventh — "
                      "working the survival minimum EVERY day, the "
                      "kept day distinguished by kiddush "
                      "('sanctification') and havdala ('separation') "
                      "alone (Rava, 69b:6)", **FM)]
        if q == "desert_partial_count":
            return [V("work_departure_day", "he who recalls the count "
                      "of days since departure works freely on that "
                      "weekday each week — he did not leave on "
                      "Shabbat; the convoy-on-Friday rider blocks a "
                      "second day (Rava, 69b:7)", **FM)]
        return None

    # -------------------------------------------- the division of labors
    DL = _EX("Shabbat 70a:2-6 (Shmuel's doubled death-verb; R. "
             "Natan's kindling ladder with the plowing-harvest rung "
             "of 34:21; R. Yosei's from-one-of-them at Lev 4:2)",
             "Exod.31.14 + 35:1-3 (exo_31_craftsmen_shabbat EX31-06 "
             "seated F-061; exo_35_shabbat_donate EX35-06 seated "
             "F-062)",
             mishnah="Mishnah Shabbat 7:1-2")

    def rule_division(case):
        q = case.get("query")
        if q == "division_source":
            return [V("each_labor_its_own", "every labor its own "
                      "liability — three recorded routes: Shmuel "
                      "reads מות יומת ('he shall surely die,' 31:14) "
                      "as many deaths amplified, displaced to the "
                      "unwitting as money-death; R. Natan climbs "
                      "kindling (35:3) over the plowing-harvest rung "
                      "(34:21); R. Yosei derives from מאחת מהנה "
                      "('from one, of them,' Lev 4:2) — "
                      "one-that-is-many", machine_claim="EX31-06",
                      **DL)]
        if q == "kindling_singled_out":
            return [V("mere_prohibition", "kindling singled out AS A "
                      "PROHIBITION — no stoning, no karet (R. Yosei; "
                      "Shmuel rules with him)",
                      authority="R. Yosei", machine_claim="EX35-06",
                      **DL),
                    V("divides_labors", "kindling singled out TO "
                      "DIVIDE — each labor its own liability (R. "
                      "Natan); the fork recorded in FOUR courtrooms: "
                      "Shabbat 70a:5, Sanhedrin 62a:7-8, Sanhedrin "
                      "35b:7, Yevamot 6b:4-5",
                      authority="R. Natan", machine_claim="EX35-06",
                      **DL)]
        if q == "labor_count_39":
            return [V("thirty_nine", "אלה הדברים ('these are the "
                      "things,' 35:1): devarim two, the definite "
                      "article three, aleh thirty-six by letters — "
                      "THIRTY-NINE labors stated to Moses at Sinai "
                      "(70a:3; Rebbi's own count at 97b:2 — the "
                      "answer sheet's author holds the arithmetic)",
                      machine_claim="EX35-06", **DL)]
        return None

    # ------------------------------------------------- the labor census
    LC = _EX("Shabbat 74b:5-7 (Rava's barrel, Abaye's receptacle; "
             "the spinning-on-the-goats objection from 35:26; Resh "
             "Lakish's feather)",
             "Exod.35.26 (exo_35_36_work_start — the build's own "
             "wool-work; labors keyed to the build per EX31-03's "
             "join)")

    def rule_census(case):
        q = case.get("query")
        if q == "composite_liability":
            return [V("seven_to_thirteen", "one artifact, counted "
                      "liabilities: earthen barrel SEVEN, oven EIGHT "
                      "(+smooth), reed receptacle ELEVEN, sewn mouth "
                      "THIRTEEN (+sew +tie) — the division of labors "
                      "run as arithmetic (Rava, Abaye, 74b:5)", **LC)]
        if q == "spin_on_animal":
            return [V("three_liabilities", "shear, comb, spin — three "
                      "offerings for spinning on the animal's back "
                      "(R. Yochanan)", authority="R. Yochanan", **LC),
                    V("exempt_atypical", "not the typical manner of "
                      "any of the three (Rav Kahana); the "
                      "wise-hearted women who spun ON the goats "
                      "(35:26) answered: extraordinary wisdom is "
                      "different", authority="Rav Kahana", **LC)]
        if q == "feather_three":
            return [V("shear_cut_smooth", "pluck the wing = shearing; "
                      "snip the tip = cutting; pull the threads = "
                      "smoothing (Resh Lakish on the Tosefta, 74b:7)",
                      **LC)]
        return None

    # -------------------------------------------------- carrying out
    CO = _EX("Shabbat 96b:1-3 (R. Yochanan's camp proclamation; the "
             "passing-passing analogy to the Jubilee) + 92a:5-7 "
             "(the Kehat rows) + 117b:8 (the skill carve) + Rosh "
             "Hashanah 34a:17 (the voice export)",
             "Exod.36.6 (exo_35_36_work_start, EX36-05 — "
             "ANTICIPATED: the seat hung the carrying labor on the "
             "stop order; F-064 seats the derivation)",
             mishnah="Mishnah Shabbat 10:3 (the carrying manners)")

    def rule_carrying(case):
        q = case.get("query")
        if q == "carrying_out_source":
            return [V("camp_proclamation", "ויעבירו קול במחנה ('and "
                      "they passed a proclamation through the camp,' "
                      "36:6): Moses sat in the Levites' camp — the "
                      "public domain — and said: do not carry out "
                      "from the private domain to it (R. Yochanan, "
                      "96b:1)", machine_claim="EX36-05", **CO)]
        if q == "proclamation_day":
            return [V("shabbat_by_analogy", "the proclamation rang on "
                      "Shabbat: העברה-העברה ('passing-passing') from "
                      "the Jubilee shofar (Lev 25:9) — a banned-labor "
                      "day both (96b:2-3); the completed-intake "
                      "alternative (36:7) answered by the analogy",
                      machine_claim="EX36-05", **CO)]
        if q == "shofar_voice":
            return [V("with_a_sound", "the same analogy run the other "
                      "way: the shofar's 'passing' learns from Moses' "
                      "proclamation to be WITH A VOICE (Rosh Hashanah "
                      "34a:17) — our verse the fixed end of both "
                      "directions", machine_claim="EX36-05", **CO)]
        if q == "carry_above_ten":
            return [V("liable", "carrying above ten handbreadths "
                      "liable — as the sons of Kehat carried: the "
                      "ten-cubit boards, Moses spreading the tent, "
                      "the pole-load riding one-third above (R. "
                      "Elazar, 92a:6-7)", **CO)]
        if q == "carry_manner":
            return [V("typical_liable_backhanded_exempt", "right "
                      "hand, left hand, lap, shoulder — liable, as "
                      "the sons of Kehat; backhanded, foot, mouth, "
                      "elbow, ear, hair, hem, shoe — exempt: not the "
                      "manner of carriers (the mishnah, 92a:5)", **CO)]
        if q == "skill_not_labor":
            return [V("excluded_from_labor", "כל מלאכה ('any labor,' "
                      "20:10) excludes shofar-blowing and bread-"
                      "removal — SKILL, not labor (the school of R. "
                      "Yishmael, 117b:8); altered anyway where "
                      "possible", **CO)]
        return None

    # --------------------------------------------- the boundary machine
    BM = _EX("Eruvin 48a:13-15 (his place = the body's four) + "
             "51a:7-9 (the verse split four/two-thousand; Rav "
             "Chisda's place-place chain through Exod 21:13 to the "
             "Levite cities; the thousand-rung refused) + 17b:12-13 "
             "(Rav Ashi's ink parse)",
             "Exod.16.29 (exo_16_manna_and_sabbath, EX16-10 crown + "
             "EX16-14 prototype — ANTICIPATED; F-063 seats the "
             "recorded routes; the 21:13 rung joins "
             "exo_21_the_ordinances' asylum clause)")

    def rule_boundary(case):
        q = case.get("query")
        if q == "four_cubits_source":
            return [V("four_expansive", "שבו איש תחתיו ('remain every "
                      "man in his place'): the body's three cubits "
                      "plus one to spread hands and feet — expansive "
                      "four (R. Meir)", authority="R. Meir",
                      machine_claim="EX16-10", **BM),
                    V("four_exact", "three plus one to move an object "
                      "from feet to head — exactly four (R. Yehuda)",
                      authority="R. Yehuda", machine_claim="EX16-10",
                      **BM)]
        if q == "two_thousand_source":
            return [V("place_place_chain", "the verse split against "
                      "itself: 'his place' = four cubits, 'let no "
                      "man go out' = two thousand — Rav Chisda's "
                      "chain: place-place to the asylum verse (21:13), "
                      "fleeing-fleeing, border-border, "
                      "outside-outside, landing on the Levite "
                      "cities' measured two thousand (Num 35:5); the "
                      "thousand-cubit rung refused — outside learns "
                      "from outside, not outward (51a:8-9)",
                      machine_claim="EX16-14", **BM)]
        if q == "boundary_verb_parse":
            return [V("go_out_written", "אל יצא ('let no man GO OUT') "
                      "is written — not 'carry out': the plain verse "
                      "is the boundary alone, no court death rides "
                      "it (Rav Ashi, 17b:13); the flogging question "
                      "of 17b:12 turns on the same letters",
                      machine_claim="EX16-10", **BM)]
        return None

    # ---------------------------------------------- life overrides
    LO = _EX("Yoma 85a:12-85b:6 (the road tournament: R. Yishmael's "
             "tunneler, R. Akiva's altar, R. Elazar b. Azarya's "
             "limb; R. Yosei b. R. Yehuda's BUT, R. Yonatan ben "
             "Yosef's sacred-to-you, R. Shimon b. Menasya's "
             "one-for-many; Shmuel's live-by-them with Rava's "
             "refutation sweep) + Sanhedrin 35b:5-8 (the "
             "execution direction)",
             "Exod.31.13-16 + 21:14 + 22:1 (exo_31 EX31-06 seats "
             "the tournament, F-061; EX22-01 seeded the tunneler "
             "route, EX22-15 the rubble rescue — ANTICIPATED)")

    def rule_life(case):
        q = case.get("query")
        if q == "life_override_source":
            return [V("live_by_them", "וחי בהם ('and live by them,' "
                      "Lev 18:5) — and not die by them: Shmuel's "
                      "route alone survives Rava's refutation sweep "
                      "(every other proof covers CERTAIN danger "
                      "only; doubt needs Shmuel) — 'one spicy pepper "
                      "better than a whole basket of squash'; the "
                      "refuted-but-recorded routes: the tunneler "
                      "a-fortiori (R. Yishmael, 22:1), from-My-altar "
                      "(R. Akiva, 21:14), the one-limb a-fortiori "
                      "(R. Elazar b. Azarya), אך ('BUT,' 31:13 — R. "
                      "Yosei b. R. Yehuda), sacred-TO-YOU (31:14 — "
                      "R. Yonatan ben Yosef), desecrate-one-keep-"
                      "many (31:16 — R. Shimon b. Menasya)",
                      machine_claim="EX31-06 (EX22-01 seeded)",
                      **LO)]
        if q == "rubble_check":
            return [V("to_the_nose", "clearing from above, stop at "
                      "the NOSE — 'all in whose nostrils was the "
                      "breath of life' (Gen 7:22); from below, "
                      "reach the nose (Rav Pappa, 85a:12) — the "
                      "wall-rescue EX22-15 holds runs this protocol",
                      machine_claim="EX22-15", **LO)]
        if q == "murderer_at_altar":
            return [V("taken_not_from_atop_except_life", "מעם מזבחי "
                      "('from My altar,' 21:14): the murderer-priest "
                      "taken to die — but not from ATOP it "
                      "mid-service; and to PRESERVE life, even from "
                      "atop (Rabba bar bar Chana citing R. Yochanan, "
                      "85a:15-85b:1): testimony stops the service",
                      **LO)]
        if q == "execution_on_shabbat":
            return [V("does_not_override", "murder overrides the "
                      "service (21:14) and the service overrides "
                      "Shabbat — yet execution does NOT override "
                      "Shabbat: the school of R. Yishmael's "
                      "kindling-at-the-habitations read (35:3), "
                      "Rava's answer at Sanhedrin 35b:6 — the "
                      "courts' burning named in the ban "
                      "(ANTICIPATED: EX35-01 cited Mishnah Sanhedrin "
                      "4:1's non-burning court)",
                      machine_claim="EX35-06 (EX35-01 anticipated)",
                      **LO)]
        return None

    # ------------------------------------- the meals and the preparation
    MP = _EX("Shabbat 117b:7-11 (rescue direction; the skill carve; "
             "rise-early; two loaves; the three todays) + Beitzah "
             "2b:9-11 (Rabba's preparation doctrine) + Pesachim "
             "47b:10 (set-aside's source and warning)",
             "Exod.16.5 + 16:22-25 (exo_16_manna_and_sabbath, "
             "EX16-16 seats the statute file — F-063)",
             mishnah="Mishnah Shabbat 16:2-3 (the rescue rows)")

    def rule_meals(case):
        q = case.get("query")
        if q == "meal_count":
            return [V("three", "three meals from the three todays of "
                      "16:25, the evening meal counted in (the "
                      "Rabbis)", authority="the Rabbis",
                      machine_claim="EX16-16", **MP),
                    V("four", "four — the three todays all daytime, "
                      "the evening besides (R. Chidka)",
                      authority="R. Chidka", machine_claim="EX16-16",
                      **MP)]
        if q == "fire_rescue_cap":
            return [V("three_meals_by_hour", "rescue three meals' "
                      "worth — evening fire three, morning two, "
                      "afternoon one: the cap tracks the meals still "
                      "owed (117b:8, 117b:11); forgotten bread out "
                      "by knife, not paddle", machine_claim="EX16-16",
                      **MP)]
        if q == "rescue_direction":
            return [V("toward_greater_sanctity_only", "Yom Kippur "
                      "rescues FOR Shabbat; Shabbat never for Yom "
                      "Kippur, a festival, or the next Shabbat; fine "
                      "bread rescued bars coarse after it (117b:7)",
                      **MP)]
        if q == "two_loaves":
            return [V("hold_two_break_one", "לחם משנה ('double "
                      "bread,' 16:22): break bread over TWO loaves — "
                      "Rav Kahana held two and broke one, "
                      "'collected' double; R. Zeira's whole-meal "
                      "slice not gluttony on Shabbat (117b:9-10)",
                      machine_claim="EX16-16", **MP)]
        if q == "prepare_early":
            return [V("rise_early_sixth", "rise early on the sixth "
                      "day for Shabbat's expenses — והכינו ('and "
                      "they shall prepare,' 16:5), the manna "
                      "gathered at morning (Rav Chisda, 117b:9)",
                      machine_claim="EX16-16", **MP)]
        if q == "preparation_doctrine":
            return [V("weekday_prepares", "the WEEKDAY prepares for "
                      "Shabbat and festival; a festival never for "
                      "Shabbat nor Shabbat for a festival — and "
                      "heaven's own preparation counts (the egg "
                      "finished yesterday; Rabba on 16:5, Beitzah "
                      "2b:10); the plain-day eggs barred by decree "
                      "both directions (2b:11)",
                      machine_claim="EX16-16", **MP)]
        if q == "muktzeh_source":
            return [V("prepare_plus_labor_warning", "set-aside "
                      "Torah-grade: the definition from והכינו "
                      "('prepare,' 16:5), the WARNING from 'you "
                      "shall not perform any labor' (20:10) — "
                      "Pesachim 47b:10's pair", machine_claim="EX16-16",
                      **MP)]
        return None

    # ------------------------------------------------ the rest roster
    RR = _EX("Bava Kamma 54b:13-14 (the two-Decalogue comparison; "
             "the refused shrink) + Shabbat 153b:7-8 (the laden "
             "animal) + 120b:11 (doing vs causing) + 18a:5-7 "
             "(vessel rest) + Bava Metzia 32a:15-16 (the parent's "
             "command)",
             "Exod.20.10-12 + 23:13 (exo_20_the_ten_utterances, "
             "EX20-16(d) the purse row — ANTICIPATED; F-065 seats "
             "the roster's runs; the 23:13 vessel-rest anchor "
             "seats F-066 → EX23-11)")

    def rule_roster(case):
        q = case.get("query")
        if q == "animal_rest_scope":
            return [V("all_animals", "'your cattle' (20:10) beside "
                      "'your ox and your donkey' (Deut 5:14): the "
                      "named pair teaches that EVERYWHERE it stands, "
                      "wild beasts and birds stand with it — the "
                      "whole animal kingdom rests (R. Yosei in R. "
                      "Yishmael's name, 54b:13); the "
                      "generalization-detail shrink refused (54b:14)",
                      machine_claim="EX20-17", **RR)]
        if q == "laden_animal":
            return [V("place_while_walking", "the purse on the donkey "
                      "= driving a laden beast against 20:10's own "
                      "roster — resolved: place it ON THE WALKING "
                      "animal (no lifting-and-placing), remove when "
                      "it stands (Rav Adda bar Ahava, 153b:8) — the "
                      "EX16-14 carrying grammar running the animal "
                      "case (ANTICIPATED: EX20-16(d) holds the "
                      "gentile-then-donkey mishnah)",
                      machine_claim="EX20-17 (EX20-16 anticipated)",
                      **RR)]
        if q == "cause_not_do":
            return [V("causing_permitted", "לא תעשה כל מלאכה ('you "
                      "shall not PERFORM any labor,' 20:10): "
                      "performance barred, indirect causation "
                      "permitted (120b:11) — with the agitated-owner "
                      "rider and the Name-erasure asymmetry left "
                      "standing (120b:12)", machine_claim="EX20-17",
                      **RR)]
        if q == "parent_vs_shabbat":
            return [V("do_not_listen", "honor of parents EQUATED to "
                      "the Omnipresent's honor (20:12 beside Prov "
                      "3:9) — hence the keeping verse must say it: "
                      "the parent's command to desecrate is not "
                      "obeyed (Bava Metzia 32a:15-16)",
                      machine_claim="EX20-15 (the equal-weight seat)",
                      **RR)]
        if q == "vessel_rest":
            return [V("noise_contempt", "the mill barred for its "
                      "NOISE — contempt for the day (Rabba)",
                      authority="Rabba", machine_claim="EX23-11",
                      **RR),
                    V("vessel_rest_torah", "the resting of VESSELS, "
                      "Torah-grade even for Beit Hillel — the "
                      "Mekhilta's hook on 'in all that I said to "
                      "you, take heed' (23:13); saved licenses: a "
                      "vessel that performs no action rests while "
                      "its work happens (Rav Yosef, 18a:6-7)",
                      authority="Rav Yosef", machine_claim="EX23-11",
                      **RR)]
        return None

    # ------------------------------------- the overlap and the product
    OP = _EX("Shabbat 114b:6-7 (the trimming dispute on shabbaton) "
             "+ Yoma 81a:20-21 (the affliction analogies) + Bava "
             "Kamma 71a:17-21 (the product legs) + Sanhedrin 78b:7 "
             "(the gatherer's mode)",
             "Exod.16.23 + 31:14-15 (exo_16 EX16-16 the shabbaton "
             "shell; exo_31 EX31-06 the product legs and the "
             "gatherer — F-061/F-063)")

    def rule_overlap(case):
        q = case.get("query")
        if q == "yk_shabbat_trimming":
            return [V("prohibited", "Yom Kippur on Shabbat: trimming "
                      "vegetables prohibited — שבתון ('a solemn "
                      "rest,' 16:23) commands a rabbinic shell "
                      "beyond the labor ban (Rav Huna with the "
                      "baraita, 114b:6)", authority="Rav Huna",
                      machine_claim="EX16-16", **OP),
                    V("permitted", "permitted — shabbaton re-read as "
                      "the positive resting command (labor then "
                      "breaks positive and negative both); the "
                      "shell's existence is the dispute (R. "
                      "Yochanan, 114b:7)", authority="R. Yochanan",
                      machine_claim="EX16-16", **OP)]
        if q == "yk_affliction_warning":
            return [V("warning_by_analogy", "the affliction's warning "
                      "requirement learned by analogy — the school "
                      "of R. Yishmael from affliction-affliction "
                      "(the rape verse); Rav Acha bar Yaakov from "
                      "שבת שבתון ('a Shabbat of solemn rest,' 31:15) "
                      "— the weekly Shabbat lends Yom Kippur its "
                      "warning doctrine (Yoma 81a:21); one of the "
                      "five labor-verses stands free for it (81a:20)",
                      machine_claim="EX31-06", **OP)]
        if q == "shabbat_product":
            return [V("others_after_shabbat_deliberate_never",
                      "R. Yochanan HaSandlar's grid: unwitting "
                      "cooking — eaten after Shabbat by OTHERS, not "
                      "him; deliberate — never by anyone (71a:17)",
                      **OP)]
        if q == "product_benefit":
            return [V("benefit_permitted", "קדש היא לכם ('it is holy "
                      "TO YOU,' 31:14): like consecrated food for "
                      "EATING — but 'to you' keeps it yours for "
                      "BENEFIT (71a:18-19)", machine_claim="EX31-06",
                      **OP)]
        if q == "product_unwitting":
            return [V("deliberate_only", "מחלליה ('its desecrators') "
                      "beside death — the analogy spoke of the "
                      "deliberate, death-liable worker only "
                      "(71a:20)", machine_claim="EX31-06", **OP)]
        if q == "product_law_grade":
            return [V("torah_grade", "the product ban Torah-grade "
                      "(one of Rav Acha and Ravina)",
                      authority="Rav Acha / Ravina (unassigned)",
                      **OP),
                    V("rabbinic_grade", "rabbinic (the other) — the "
                      "assignment itself unrecorded: 'one said... "
                      "and one said' (71a:21)",
                      authority="Rav Acha / Ravina (unassigned)",
                      **OP)]
        if q == "gatherer_doubt":
            return [V("mode_only", "Moses KNEW the gatherer dies — "
                      "מחלליה מות יומת ('its desecrators shall "
                      "surely die,' 31:14); only the MODE waited "
                      "('it had not been declared WHAT,' Num 15:34) "
                      "— against the blasphemer's full doubt "
                      "(Sanhedrin 78b:7)", machine_claim="EX31-06",
                      **OP)]
        return None

    # ------------------------------------------- the eve's vigilance
    EV = _EX("Shabbat 20a:3-6 (the dusk licenses; the Hearth "
             "Chamber's two routes; the bonfire measures) + 23b:5 "
             "(the pillars' overlap) + 18a:5 (the self-running "
             "licenses) + 117b:7 + the word-order pair 16:23/35:2 "
             "+ 132a:6-8 (sign against sign)",
             "Exod.12.5 + 13:16-22 + 16:23 + 35:2-3 (exo_16 "
             "EX16-09 the two fences — ANTICIPATED; exo_35 EX35-06; "
             "the 12:5 and 13:22 anchors noted at their own units, "
             "unseated — ledger rows carry them)")

    def rule_eve(case):
        q = case.get("query")
        if q == "paschal_dusk":
            return [V("group_vigilant", "the paschal lamb lowered at "
                      "dusk: the registered group is VIGILANT — the "
                      "whole-roast lamb would invite coal-stoking; "
                      "vigilance is the license's parameter (20a:4; "
                      "the pesach block's registration machine "
                      "supplies the group)", **EV)]
        if q == "hearth_chamber":
            return [V("habitations_exclusion", "במשבתיכם ('in YOUR "
                      "habitations,' 35:3) — the Temple excluded "
                      "from the kindling ban (Rav Huna)",
                      authority="Rav Huna", machine_claim="EX35-06",
                      **EV),
                    V("limbs_and_fats", "the verse permits the limbs "
                      "and fats on the altar; the Chamber rests on "
                      "priestly vigilance instead (Rav Chisda)",
                      authority="Rav Chisda", machine_claim="EX35-06",
                      **EV)]
        if q == "lamp_timing":
            return [V("neither_early_nor_late", "the lamp meets the "
                      "dark without gap or show — taught from the "
                      "pillars' OVERLAP (13:22): the day's fences "
                      "overlap (23b:5, Rav Yosef's wife and the "
                      "elder's rule)", **EV)]
        if q == "tosefet_fences":
            return [V("add_at_entry_and_exit", "the word-order pair — "
                      "שבתון שבת־קדש ('solemn rest, holy Shabbat,' "
                      "16:23) against the reversed order of 35:2 — "
                      "rest added from the weekday at ENTRY and "
                      "EXIT both (ANTICIPATED: EX16-09 holds the "
                      "two fences); the rescue-direction rows run "
                      "on the same sanctity ladder (117b:7)",
                      machine_claim="EX16-09", **EV)]
        if q == "nightfall_license":
            return [V("self_running_permitted", "the canal waters "
                      "the garden all Shabbat, incense under the "
                      "clothes, the salve on the eye — work that "
                      "runs by itself may start before dark "
                      "(18a:5); only the acting vessel is barred "
                      "(18a:7)", **EV)]
        if q == "bonfire_measure":
            return [V("most_each_branch", "most of EACH branch lit "
                      "before dark (Rav)", authority="Rav", **EV),
                    V("no_bring_thinner", "lit enough that none say "
                      "'bring thinner branches' (Shmuel; Rav "
                      "Chiyya's flame-ascends-by-itself standard in "
                      "support)", authority="Shmuel", **EV)]
        if q == "circumcision_override_route":
            return [V("covenant_covenant", "sign-against-sign fails — "
                      "phylacteries carry the sign-word too (13:16); "
                      "the override rides ברית ('covenant'): Gen "
                      "17:11 matched to 31:16, the word phylacteries "
                      "lack (132a:6-8) — the selection lexical, both "
                      "candidate words in the sign chapter",
                      machine_claim="EX31-06", **EV)]
        return None

    return {
        "forgetting_machine": {"fn": rule_forgetting},
        "division_of_labors": {"fn": rule_division},
        "labor_census": {"fn": rule_census},
        "carrying_out": {"fn": rule_carrying},
        "boundary_machine": {"fn": rule_boundary},
        "life_override_derivation": {"fn": rule_life},
        "meals_and_preparation": {"fn": rule_meals},
        "rest_roster": {"fn": rule_roster},
        "overlap_and_product": {"fn": rule_overlap},
        "eve_vigilance": {"fn": rule_eve},
    }
