

# ===== F4: PEOR — THE SIN, THE HANGING, THE JUDGES, THE ZEALOT (Num 25:1-9) ================================
def peor(case, data):
    q = case['ask']; P.clear()
    if q == 'spec_run':
        ink('25:1-2', "'the people began to whore after the daughters of Moab; and they called the people to the sacrifices of their gods, and the people ate and bowed to their gods' — Exod 34:15-16 clause by clause; the feminine 'their gods' at %s alone" % [k for k in THEIR_GODS_FEM if k[0] != '1Kgs']); move('Exod 34:15-16 by the erection engine (CALL)', "covenant('eat_sacrifice') = %s; ('daughters_two_seats') names %s" % (ER_EAT, ER_DAUGHTERS[0])); move('M-22 the run teaches the spec', 'the Numbers exemplar (MOVE_CATALOG.md)')
        return out("Exod 34:15-16's spec RUN at 25:1-2 — whored after their daughters, ate of their sacrifices, bowed to their gods; the feminine 'their gods' at the two seats alone (the erection engine CALLED)", ['whored_after', 'bowed_to_their_gods'])
    if q == 'shittim_name':
        dat('the row shittim_name = %s' % data['shittim_name']['value']); move('Bekhorot 5b:5; Sanhedrin 106a:12', "the place's name (R. Eliezer) / nonsense (R. Yehoshua)"); ink('25:1', "'Shittim' — the tabernacle's acacia timber, the last camp (33:49)")
        return out("Shittim the place's name (R. Eliezer) / an allusion to nonsense, harlotry and idolatry (R. Yehoshua) — DISPUTE (Bekhorot 5b)", ['encamped_at'])
    if q == 'called_the_people':
        dat('the row called_the_people = %s' % data['called_the_people']['value']); move('Bekhorot 5b:6; Sanhedrin 106a:13', 'naked women met them (R. Eliezer) / emissions (R. Yehoshua)')
        return out("'and they called the people' (25:2) — naked women met them (R. Eliezer) / they all had emissions (R. Yehoshua): DISPUTE (Bekhorot 5b)", [FX.NONE])
    if q == 'dwelt_is_pain':
        ink('25:1', "'and Israel dwelt in Shittim'"); move('Sanhedrin 106a:15', "every 'and he dwelt' is pain — the four seats computed: %s" % [k for k in DWELT if k in {('Num', 25, 1), ('Gen', 37, 1), ('Gen', 47, 27), ('1Kgs', 5, 5)}])
        return out("'and Israel dwelt' — every 'and he dwelt' announces pain: Shittim, Jacob (Gen 37:1), Goshen (47:27), Judah and Israel (1 Kgs 5:5) — Sanhedrin 106a:15, the four seats computed", [FX.NONE])
    if q == 'peor_service':
        dat('the row peor_service = %s' % data['peor_service']['value']); move('Mishnah Sanhedrin 7:6; Sanhedrin 106a:11; Jerusalem Talmud Sanhedrin 10:2:15; Sifrei Bamidbar 131:2', "'you do not bow, you only strip for it' — the Sages: baring is its worship")
        return out("baring oneself to Peor is its worship — liable as an idolater (Mishnah Sanhedrin 7:6): the Sifrei's rule at the reading, the answer sheet here", ['stoned'])
    if q == 'wine_decree_date':
        dat('the row wine_decree_date = %s' % data['wine_decree_date']['value']); move('Sanhedrin 106a:10; Jerusalem Talmud 10:2:15; Sifrei 131:2', "'neither Ammonite wine nor gentile wine had been prohibited yet' — Avodah Zarah 36b's decree later")
        return out("the decree on gentile wine is later than Peor — 'not yet forbidden' at Shittim (Sanhedrin 106a:10; the Sifrei; the Jerusalem Talmud): a law's installation dated by the shelf", [FX.NONE])
    if q == 'yoked_like_the_lid':
        ink('25:3, 25:5, 19:15', "'yoked' (nitzmad) — its noun 19:15's cord-bound lid (tzamid patil)"); move('Sanhedrin 64a:11', "like a tightly bound cover on a vessel — against 'cleave to the LORD' like two dates")
        return out("yoked to Baal-peor like a cord-bound lid on a vessel (Sanhedrin 64a:11 — 19:15's word, the reading's crown); Israel to the LORD like two dates lightly touching", ['yoked_to_baal_peor'])
    if q == 'hang_before_the_sun':
        ink('25:4', "'take all the heads of the people and hang them to the LORD before the sun' — Saul's sons' verb (2 Sam 21:6)"); move('Sanhedrin 34b:21, 35a:2; Jerusalem Talmud 10:2:17', 'judged by day; the heads as judges hang the sinners; Onkelos: judge and kill'); move('Deut 21:22-23 by the wood-gatherer\'s court (CALL)', 'the hanging after the stoning: %s' % MK_HANGING)
        return out("'hang them before the sun' — the heads installed as judges, the sinners judged by day and hanged (Sanhedrin 34b-35a; the Jerusalem Talmud); the wood-gatherer's court: the idolater hanged after stoning", ['commanded'])
    if q == 'judges_count':
        move('Exod 18:21 by the exodus engine (CALL)', 'the judges of Israel %d' % EX_JUDGES); dat('the row each_his_two = %d — %d executed (the Jerusalem Talmud 10:2:17)' % (data['each_his_two']['value'], EX_JUDGES * data['each_his_two']['value']))
        return out("the judges of Israel 78,600 (Exod 18:21's tiers by the exodus engine) — each executing two = 157,200 (the Jerusalem Talmud Sanhedrin 10:2:17; the Sifrei 131:2)", ['commanded'])
    if q == 'zealot_rule':
        arm = case.get('arm', 'in_the_act')
        dat('the row zealot_rule = %s; the arms: %s' % (data['zealot_rule']['value'], sorted(data['zealot_rule']['settings'])))
        move('Mishnah Sanhedrin 9:6', "one who cohabits with an Aramean woman — zealots strike him"); move('Sanhedrin 82a:10', 'during the act only; the pursued may kill the zealot; not taught'); ink('25:6-8', 'the bringing-near and the spear — the act and its end')
        if arm == 'in_the_act':
            return out("zealots strike him — Zimri in the act (Mishnah Sanhedrin 9:6; Sanhedrin 82a); the cohabits entry OPEN from 25:6 to the spear", ['cohabits_with_an_aramean', 'slain'])
        if arm == 'separated':
            return out("separated — the zealot who then strikes is a murderer, executed (Sanhedrin 82a:10)", ['exempt'])
        if arm == 'self_defense':
            return out("Zimri turning and killing Phinehas — not executed: the zealot is a pursuer (Sanhedrin 82a:10)", ['exempt'])
        if arm == 'asks_the_court':
            return out("one who asks the court is not instructed — the law is not taught (Sanhedrin 82a:12; Moses forgot it)", ['exempt'])
        return out('no arm named', [FX.NONE])
    if q == 'halakha_forgotten':
        ink('25:6', "'before the eyes of Moses... and they were weeping at the door of the tent'"); move('Sanhedrin 82a:12', "'is she forbidden? who permitted Jethro's daughter?' — the law eluded Moses; the Sanhedrin wept; Phinehas saw")
        return out("the law forgotten by Moses at 25:6 — the Sanhedrin wept, the zealot remembered (Sanhedrin 82a:12): the rule not taught, installed by the deed", ['wept'])
    if q == 'no_weapon_in_the_hall':
        ink('25:7', "'he rose from the midst of the congregation and took a spear' — the spear the Torah's one (%s)" % SPEAR); move('Sanhedrin 82a:15', 'one does not enter the study hall armed; the blade hidden')
        return out("the spear taken only after rising from the assembly (25:7) — one does not enter the study hall armed (Sanhedrin 82a:15); the Torah's one spear", [FX.NONE])
    if q == 'cast_before_god':
        ink('25:8-9', "'and the plague was stayed' — Aaron's clause; 'the dead in the plague' — Korach's formula; the count %s" % COUNT); move('Sanhedrin 44a:14, 82b:3', "Phinehas cast them before God: 'for these shall twenty-four thousand fall?' — Ps 106:30 'executed judgment'")
        return out("cast before God — 'shall twenty-four thousand fall for these?' (Sanhedrin 82b:3; Ps 106:30): the plague stayed at the spear, the count 24,000 by the parser", ['plague_struck', 'slain'])
    if q == 'for_its_sake':
        move('Horayot 10b:15; Nazir 23b:4', "Tamar for a mitzvah — kings and prophets; Zimri for a transgression — twenty-four thousand fell")
        return out("Zimri's licentiousness not for its own sake — twenty-four thousand fell (Nazir 23b; Horayot 10b); Tamar's for a mitzvah bore kings", [FX.NONE])
    if q == 'plague_count':
        ink('25:9, 17:14', "'the dead in the plague were' — 24,000 here, 14,700 at Korach (the parser's %s, %s)" % (COUNT, KORACH_COUNT)); move('cold_run_korach (CALL)', KR_COUNT); move('cold_run_bamidbar (CALL)', 'the total %s; Simeon %s -> %s (1:23, 26:14)' % (BM_TOTAL.split()[0], SIMEON[0], SIMEON[1]))
        return out("the plague's dead 24,000 (25:9) — Korach's formula and 14,700 (17:14); Simeon 59,300 -> 22,200 the checkpoint at the second census; the total 603,550 (bamidbar CALLED)", ['plague_struck'])
    if q == 'aaron_and_phinehas':
        ink('25:8, 25:13, 17:12-13', "'and the plague was stayed' at %s; 'and he atoned for' at %s — the father's censer and the son's spear one clause and one verb" % (sorted(STAYED), sorted(ATONED_FOR))); move('cold_run_korach (CALL)', KR_INCENSE); move('Sifrei Bamidbar 131:3', 'turner-away of wrath, son of a turner-away')
        return out("Aaron's incense clause and verb at Phinehas's spear — 'the plague was stayed' (17:13, 25:8) and 'he atoned for' (17:12, 25:13): the Sifrei's father-son title measured on the ink; korach's incense cell CALLED", ['plague_struck'])
    if q == 'idolatry_principle':
        move('cold_run_shelach (CALL)', SH_IDOL); ink('25:2-3', "the community ate, bowed and yoked itself — 15:22-31's class")
        return out("the Peor congregation under 15:22-31's principle — the shelach engine's idolatry_principle row CALLED", ['yoked_to_baal_peor'])
    if q == 'anger_third':
        ink('25:3', "'and the anger of the LORD burned against Israel' — the third anger; 32:13-14 Moses retells it"); move('Zevachim 102a', 'the mark: the plague')
        return out("the third anger (25:3) — its mark the plague, stayed by the spear (25:8)", ['mark_of_anger', 'plague_struck'])
    if q == 'aramean_woman':
        dat('the row aramean_woman = %s' % data['aramean_woman']['value']); move('Kiddushin 3:12 by the family engine (CALL)', "the child follows the gentile mother")
        return out("the Midianite woman's child would follow her (Kiddushin 3:12 by the family engine) — the case the zealots strike in (Mishnah Sanhedrin 9:6)", ['cohabits_with_an_aramean'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: PHINEHAS AND MIDIAN (Num 25:10-19) ================================================================
def phinehas_and_midian(case, data):
    q = case['ask']; P.clear()
    if q == 'priesthood_by_the_deed':
        ink('25:13', "'a covenant of everlasting priesthood' — written after the deed; Phinehas born Exod 6:25, silent until 25:7"); move('Zevachim 101b:10', 'Phinehas did not become a priest until he killed Zimri'); move('cold_run_priesthood (CALL)', 'the addressees row: %s — the grandson the named exception' % PR_ADDRESSEES)
        return out("Phinehas not a priest until he killed Zimri — 'a covenant of everlasting priesthood' written only after (Zevachim 101b); the priesthood engine's addressees bind the sons of Aaron, this grandson the exception", ['invested_office'])
    if q == 'covenant_of_peace':
        ink('25:12', "'behold, I give him My covenant of peace' — one seat; Malachi's covenant with Levi (2:5)"); move('Sanhedrin 82b:6', 'greet Phinehas first with peace; the atonement forever')
        return out("the covenant of peace (25:12) — HEAVEN's entry in force forever; God to Moses: greet him first with peace (Sanhedrin 82b:6)", ['covenant_of_peace'])
    if q == 'seed_after_him':
        ink('25:13', "'for him and for his seed after him'"); move('Ketubot 13b:16; Yevamot 100b:8', "a priest whose seed is attributed to him — the shetuki (father unknown) silenced from the service")
        return out("'his seed after him' — the priest's descendants must be attributed to him: the shetuki serves not, marries yes (Ketubot 13b; Yevamot 100b)", [FX.NONE])
    if q == 'unfit_seed_service':
        move('Kiddushin 66b:10', "'his seed after him' includes unfit seed — the divorcee's son's service valid after the fact")
        return out("the disqualified priest's service valid after the fact — 'his seed after him' includes unfit seed (Kiddushin 66b:10)", ['accepted'])
    if q == 'blemished_service':
        ink('25:12', "'My covenant of peace [shalom]' — read whole [shalem]"); dat('the row vav_of_shalom = %s' % data['vav_of_shalom']['value']); move('Kiddushin 66b:13', "the blemished priest's service retroactively invalid; Rav Nachman: the vav severed by tradition")
        return out("the blemished priest's service invalid — 'peace' read 'whole' (Kiddushin 66b:13); the severed vav a letter's shape the DB's bytes cannot carry", ['disqualified'])
    if q == 'lineage_answer':
        ink('25:7, 25:11', "'Phinehas son of Eleazar son of Aaron the priest' — the three-generation title twice"); move('Sanhedrin 82b:5; Sifrei Bamidbar 131:3', "the tribes' taunt 'son of Puti'; the verse answers with the lineage — three generations as three deeds")
        return out("the lineage answers the taunt — 'son of Eleazar son of Aaron the priest' (25:11): priest son of priest, zealot son of zealot, turner-away son of turner-away (the Sifrei 131:3; Sanhedrin 82b:5)", [FX.NONE])
    if q == 'covenant_salt_priesthood':
        move('Menachot 20a:1', "'covenant' at the salt (18:19) and at the priesthood (25:13) — salting indispensable as the priesthood (R. Shimon)"); move('cold_run_korach (CALL)', "the covenant of salt korach's row")
        return out("'covenant' at 18:19 and 25:13 — the salt as indispensable as the priesthood (Menachot 20a; korach's covenant_of_salt row)", [FX.NONE])
    if q == 'twenty_four_gifts':
        move('cold_run_korach (CALL)', 'the twenty-four: %d in the sanctuary, %d at the borders' % (len(KR_24['sanctuary']), len(KR_24['borders']))); move('Sifrei Bamidbar 131:5; Bava Kamma 110b', "the priesthood's twenty-four gifts")
        return out("the twenty-four priestly gifts (the Sifrei 131:5; Bava Kamma 110b) — korach's row CALLED: the priesthood Phinehas's covenant confers", [FX.NONE])
    if q == 'high_priest_count':
        dat('the row high_priest_count = %s against %s' % (data['high_priest_count']['value'], 'more_than_three_hundred'))
        return out("twelve high priests in the first Temple and eighty in the second (the Sifrei 131:4) against Yoma 9a's more than three hundred — the shelf disagreeing with itself, recorded: DISPUTE", [FX.NONE])
    if q == 'atone_tense':
        ink('25:13', "'and he atoned for' — the morphology tags the narrative past; Onkelos a past"); dat('the row atone_tense = %s' % data['atone_tense']['value']); move('Sifrei Bamidbar 131:5; Sanhedrin 82b:6', "'not to atone but and he will atone — he stands and atones until the revival of the dead'")
        return out("'and he atoned' read future by the Sifrei against the morphology's past — the atonement forever (Sanhedrin 82b:6): DISPUTE on the tense of one word", ['atoned_forgiven'])
    if q == 'midian_not_moab':
        ink('25:17', "'harass the Midianites and strike them' — Moab not named"); move('Bava Kamma 38a:16', "Moses' a fortiori from Midian to Moab — Deut 2:9 had to forbid it")
        return out("Midian harassed, Moab spared — Moses' own a fortiori needed Deut 2:9's bar (Bava Kamma 38a); the debit on Israel toward Midian OPEN to 31:7", ['commanded'])
    if q == 'balaam_death':
        dat('the row balaam_death = %s' % data['balaam_death']['value']); ink('31:8', "'Balaam son of Beor they slew with the sword' — the ass's sword-clause (22:29) closed there"); move('Sanhedrin 106a:16-17, 106b:1; Jerusalem Talmud 10:2:18', 'to collect his wages for the 24,000; all four modes (Rav); on their slain four ways')
        return out("Balaam killed by the sword at Midian (31:8) — come for his wages for the twenty-four thousand (Sanhedrin 106a:16); all four court modes in him (Rav, 106b:1)", [FX.NONE])
    if q == 'everlasting_priesthood':
        ink('25:13, Exod 40:15', "'everlasting priesthood' at two seats — the sons' clause narrowed to one son's line"); move('Exod 40:15 by the erection engine (CALL)', "command('everlasting_priesthood') = %s" % ER_PRIESTHOOD)
        return out("'everlasting priesthood' at Exod 40:15 (all Aaron's sons — the erection engine's clause) and 25:13 (Phinehas's line): the clause narrowed", ['invested_office'])
    if q == 'cozbi_and_zur':
        ink('25:15, 25:18, 31:8', "'Cozbi daughter of Zur, head of the peoples' — Zur one of the five kings (Josh 13:21); 'their sister'"); dat('the row cozbi_and_zur = %s' % data['cozbi_and_zur']['value'])
        return out("Cozbi daughter of Zur — Zur one of Midian's five kings killed beside Balaam (31:8): the father dies in the war his daughter's death opens", [FX.NONE])
    if q == 'harass_root':
        ink('25:17-18, 10:9', "'harass... for they harass you' — the trumpets' enemy-word (10:9), Esther's title for Haman the Agagite (3:10); 'their wiles' Joseph's brothers' verb (Gen 37:18)"); ink('24:7', "'higher than Agag' — Haman's ancestor")
        return out("the harass-root (25:17-18) — the trumpets' enemy (10:9) and Haman the Agagite's title in Esther; 24:7's Agag and this command meet in one root", ['commanded'])
    if q == 'rule_installed':
        move('Mishnah Sanhedrin 9:6; Sanhedrin 82a:12', "the halakha (the law) not taught — installed by the deed (25:7-8), ratified by the output (25:10-13)"); ink('25:10-13', "the covenant and the priesthood — the deed's reward, the ink's own output")
        return out("the zealots' rule installed by the deed and ratified by the covenant's speech — rule_installed on the tent (law_balak:zealot), no halt and no docket: THE TENT's form at a second seat", ['rule_installed'])
    if q == 'atoned_forever':
        ink('25:13', "'and he atoned for the children of Israel' — Aaron's verb at 17:12"); move('Sanhedrin 82b:6', 'worthy of atoning forever')
        return out("'and he atoned for the children of Israel' (25:13) — Aaron's incense verb (17:12); the atonement forever (Sanhedrin 82b:6)", ['atoned_forgiven'])
    return out('no verdict in span', [FX.NONE])
