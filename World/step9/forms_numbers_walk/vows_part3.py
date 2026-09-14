

# ===== F1: THE MAN (Num 30:2-3) =============================================================================
def the_man(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'frame':
        ink('30:2', '"and Moses SPOKE to the heads of the tribes of the children of Israel, saying: THIS IS THE THING which the LORD commanded" — no divine frame: the formula at %d Bible seats, its two Numbers seats %s the book\'s two law chapters without "the LORD spoke to Moses" (computed)' % (len(THIS_IS), THIS_IS[-2:]))
        move('Sifrei 153:2', 'Moses prophesied with "thus said the LORD" as the prophets and ADDED "this is the thing" — the relay\'s own mark')
        move('Bava Batra 120b:1', 'the vows\' law in ALL generations by the verbal analogy "this" / "this" with Lev 17:2 — against 36:6\'s "this generation": the relayed statute is not case-bound (the installed_by decision\'s witness)')
        return out('a law relayed in Moses\' voice — this is the thing which the LORD commanded, for all generations', ['commanded'])
    if ask == 'this_is_the_thing':
        ink('30:2', '"this is the thing" — the limiter: the husband\'s verb in the chapter is ANNUL (six tokens), "permit" never (computed at the reading)')
        move('Sifrei 153:2; Nedarim 77b:9-78a:1', 'two a-fortiori refused by the words — the sage DISSOLVES and does not annul, the husband ANNULS and does not dissolve')
        move('Nedarim 77b:8 (R. Yochanan)', 'a sage who said "annulled" or a husband who said "dissolved" HAS SAID NOTHING — each office its own verb')
        return out('two offices, two verbs — the husband annuls, the sage dissolves; the words crossed say nothing', ['accepted'])
    if ask == 'heads_of_the_tribes':
        ink('30:2', '"to the heads of the tribes" — %d Bible seats (Solomon\'s assembly the other two), "TO the heads" one (computed)' % len(HEADS))
        move('Sifrei 153:1 (R. Yonatan)', 'the frame freed by Exod 34:31-32 (the princes return first) — the FREED phrase teaches: the release of vows by experts alone')
        move('Nedarim 78b:3 (Rav Chisda / R. Yochanan); 78a:3; 78b:2 (ben Azzai)', 'a single expert from "the heads of the tribes"; three laymen by the verbal analogy with Lev 17:2, or by ben Azzai\'s "the vows\' portion needs no expert"')
        dat('the row sage_release = %s' % data['sage_release']['value'])
        return out('the sage\'s release — one expert or three laymen: the shelf\'s office on the freed phrase', ['accepted'])
    if ask == 'sage_release_flies':
        move('Mishnah Chagigah 1:8 (10a:4)', 'the dissolution of vows FLIES IN THE AIR — nothing to support it')
        move('Chagigah 10a:9, 10a:13 (Shmuel; Rava)', 'Shmuel\'s source has no refutation: "he shall not profane HIS word" — he cannot, others may; "one spicy pepper is better than a basket of squash"')
        return out('flies in the air — the one unrefuted ground the chapter\'s own clause 30:3', ['accepted'])
    if ask == 'sage_release_form':
        move('Nedarim 77b:2 (Rav Nachman); 77a:7 (Abaye)', 'dissolved standing, alone, at night, on the Sabbath, by relatives, even when one could have asked before — no court act')
        move('Nedarim 77b:3', 'Rabban Gamliel sat — an opening by REGRET needed; Rav Nachman: not needed')
        dat('the row sage_release = %s' % data['sage_release']['value'])
        return out('no session, no court — standing, alone, at night; the regret arm recorded', ['accepted'])
    if ask == 'sage_release_presence':
        move('Nedarim 65a:1 (Rav Nachman; Tosefta 2:12); 65a:4', 'a vow off a person is dissolved only IN HIS PRESENCE — "in MIDIAN ... go, return" (Exod 4:19); Zedekiah\'s oath and the Sanhedrin\'s error')
        return out('dissolved in the presence of the one vowed against', ['accepted'])
    if ask == 'sage_release_timing':
        move('Nedarim 90a:3; 90b:4', 'the sage dissolves only a vow IN EFFECT — "his word" must be his in force (R. Natan and the Rabbis agree; the second version refuted)')
        return out('only a vow in effect is dissolved', ['accepted'])
    if ask == 'openings':
        move('Mishnah Nedarim 9:1-10', 'the openings: the parents\' honor (disputed), the new situation (disputed), the Torah\'s prohibitions, the marriage contract, the Sabbaths and festivals, his own honor')
        return out('an opening on "had I known" — the answer sheet\'s method, never the ink\'s', ['accepted'])
    if ask == 'mistaken_vow':
        move('Mishnah Nedarim 9:10 (66a:12); 65a:6 (R. Yochanan)', '"ugly so-and-so" who is beautiful — permitted: a vow MISTAKEN FROM THE OUTSET never took effect; the dog already dead')
        return out('a mistaken vow — no vow', ['exempt'])
    if ask == 'age':
        age, sex, knows = case['age'], case['sex'], case.get('knows_to_whom', True)
        floor, top = (11, 12) if sex == 'girl' else (12, 13)
        ink('30:3', '"a MAN, when he vows" — the minor excluded (Sifrei 153:3); "and a woman ... in her youth" (30:4)')
        move('CALLED cold_run_naso.nazirite(vow_form) -> %s [IMPORT, live]' % NAZ_SUB[0], 'the age by the identity with 6:2 "when a man or woman shall clearly utter a vow" — Niddah 46a:2 (thirteen and a day without clear utterance)')
        move('Mishnah Niddah 5:6 (45b:2-4)', 'the girl eleven and a day EXAMINED, twelve and a day valid; the boy twelve / thirteen; before — no vow even saying "we know"; after — a vow even saying "we do not know"')
        dat('the row vow_ages = %s' % data['vow_ages']['value'])
        if age < floor:
            return out('a minor — no vow, no consecration (even saying "we know")', ['exempt'])
        if age < top:
            return out('the examined year — bound if she knows in Whose name' if knows else 'the examined year — she does not know in Whose name: no vow', ['vow_bound'] if knows else ['exempt'])
        return out('of age — the vow stands without examination', ['vow_bound'])
    if ask == 'vow_vs_oath':
        ink('30:3', '"vows a vow to the LORD, or swears an oath to bind a bond on his soul" — vows and oaths ADJACENT (Nedarim 2b:2); the oath by the seven-stem, starred by the parser at %s' % STARRED)
        move('Nedarim 13b:4; Shevuot 25a:11-12', 'THE TWO STRINGENCIES — vows take effect on a MITZVA, oaths not (no oath to neglect a mitzva — "HIS word he shall not profane", 16b:3); oaths take effect on the INTANGIBLE, vows only on substance')
        move('Sifrei 153:3', 'a vow is as by the king\'s life, an oath as by the King himself (2 Kings 2:2 the form)')
        return out('the vow binds the OBJECT (even a mitzva\'s), the oath binds the PERSON (even to nothing tangible)', ['accepted'])
    if ask == 'vow_support':
        base = case['base']
        ink('30:3', '"vows a VOW" — the doubled noun (Shevuot 20b:3); "to the LORD" (Nedarim 13a:3-4)')
        move('Nedarim 14a:5, 13a:2; Mishnah Nedarim 2:1 (13b:7)', 'a vow takes effect by association with a thing forbidden BY A VOW (an offering, a konam); by a Torah-forbidden thing (carrion, the pig, Aaron\'s terumah) it does not — the firstborn disputed')
        dat('the row vow_support_base = %s' % data['vow_support_base']['value'])
        return out('leans on a vowed thing — bound' if base == 'vowed' else 'leans on a Torah-forbidden thing — no vow', ['vow_bound'] if base == 'vowed' else ['exempt'])
    if ask == 'substitutes':
        move('Mishnah Nedarim 1:2 (10a:11); 10b:11', 'konam, konach, konas bind as "an offering"; nazik as "a nazirite"; shevuta as "an oath"; "by mohi" nothing, "by the oath Mohi said" binds')
        dat('the row substitutes_source = %s' % data['substitutes_source']['value'])
        return out('the substitutes bind — the nations\' words or the Sages\' devised ones', ['vow_bound'])
    if ask == 'not_non_sacred':
        move('Mishnah Nedarim 1:3 (10b:12); 11b:1, 11b:6', '"what I eat of yours shall be NOT non-sacred" — forbidden; "as non-sacred" — permitted; R. Meir infers no positive from a negative')
        return out('the negation of the common binds — "not non-sacred" is an offering', ['vow_bound'])
    if ask == 'on_a_limb':
        move('Mishnah Nedarim 1:4 (13b:3); Rav Yehuda 13b:5', '"konam my MOUTH speaking with you, my HAND working, my FOOT walking" — a vow on a limb, a thing of substance — forbidden; "what I speak" would be intangible')
        return out('a vow on the limb binds; on the act it would not', ['vow_bound'])
    if ask == 'bind_the_permitted':
        ink('30:3', '"to BIND a bond on his soul" — bind the permitted, not permit the forbidden (Sifrei 153:4)')
        move('Shevuot 27a:1-5; Nedarim 16b:3', 'an oath to eat carrion or to neglect a mitzva takes no effect — "sworn from Sinai"; the oath to harm himself binds (27a:6)')
        return out('no oath to permit the forbidden — the oath void', ['exempt'])
    if ask == 'not_profane':
        ink('30:3', '"he shall not PROFANE his word" — one Bible seat in this sense (computed)')
        move('Sifrei 153:4; Nedarim 81b:5, 90a:3', 'HE shall not profane it — the sage releases others, not himself; Rabban Gamliel: annul even a vow that does not take effect')
        move('Nedarim 15a:8, 81b:9', 'the custom of a place treated as forbidden — "he shall not profane his word" by rabbinic law (a quasi-vow)')
        return out('the vower bound to his word; the sage not for himself; the custom a quasi-vow', ['commanded'])
    if ask == 'two_transgressions':
        ink('30:3', '"he shall not profane his word; according to all that proceeds out of his mouth he shall do" — the two clauses')
        move('Sifrei 153:4; Nedarim 3a:7', 'TWO transgressions on the unpaid vow — "he shall not profane" and "you shall not delay" (Deut 23:22), on the nazirite\'s vow too')
        move('CALLED cold_run_musafim.the_calendar(vow_deadline) -> %s; DATA vow_deadline = %s (%d settings) [IMPORT, live]' % (MU_DEADLINE[0], MU_ROW['value'], len(MU_ROW['settings'])), 'the delay ban\'s clock in festivals — the musafim runner\'s row READ, never re-declared (the 9b debt (iv) paid); Deuteronomy 23 not compiled — OWED')
        return out('profane and delay — two transgressions; the delay counted in festivals by call', ['commanded'])
    if ask == 'delay_clocks':
        move('Rosh Hashanah 4a:13-14, 4b:2 (the five counts); 6a:16 (Rava); 6a:14 (Rava)', 'three festivals (the first tanna) / in order (R. Shimon) / one (R. Meir) / two (R. Eliezer b. Yaakov) / by Sukkot (R. Elazar b. R. Shimon); the POSITIVE mitzva at the first festival; CHARITY at once — the poor are everywhere')
        move('Rosh Hashanah 5b:11', 'the count RESTARTS at a replacement animal\'s consecration')
        return out('two dues — the positive at the first festival, the prohibition at the third; charity now', ['commanded'])
    if ask == 'sin_in_you':
        move('Rosh Hashanah 5b:5; 6a:3', '"and it would be sin IN YOU" — not in your offering (the late offering not disqualified), not in your wife (the delay\'s sin his alone)')
        return out('the delay\'s sin on the vower alone — the offering and the wife unmoved', ['accepted'])
    if ask == 'vow_vs_gift':
        move('Rosh Hashanah 6a:12; 6a:8', 'a VOW-offering ("upon me") — died or stolen, he pays again; a GIFT ("this one") — not liable; the bare vow and the designated animal both transgress by delay')
        return out('the vow\'s debit persists past its object; the gift\'s dies with it', ['vow_bound'])
    if ask == 'lips_or_heart':
        ink('30:3, 30:13', '"according to all that proceeds out of his MOUTH", "all that proceeds from her LIPS" — the ink names the mouth and the lips')
        move('Shevuot 26b:9 (Shmuel); 26b:15-16', 'the oath needs the lips — "clearly with his lips" (Lev 5:4); the Tabernacle\'s willing heart (Exod 35:22) stands apart')
        move('Sifrei 153:4; Chagigah 10a:8, 10a:11', '"on his soul" — the inward acceptance counts (the Sifrei); R. Yitzchak\'s "willing heart" for the vow')
        dat('the row oath_by_the_heart = %s' % data['oath_by_the_heart']['value'])
        return out('the lips required — the heart\'s vow the Sifrei\'s arm, recorded', ['accepted'])
    if ask == 'vower_a_sinner':
        move('Nedarim 77b:4 (Rav Dimi; Rav Zevid on Deut 23:23); 10a:9 (R. Elazar HaKappar)', 'whoever vows, even fulfilling it, is called a sinner; whoever fasts needlessly is a sinner')
        dat('the row vower_a_sinner = %s' % data['vower_a_sinner']['value'])
        return out('the vower called a sinner — the vow\'s standing on the shelf', ['accepted'])
    if ask == 'on_his_soul':
        ink('30:3', '"to bind a bond ON HIS SOUL" — the chapter\'s one masculine soul-token against ten "her soul" (computed)')
        move('Nazir 61a:8 (Rava)', 'one whose soul is in his own possession — the SLAVE excluded from vows (the nazirite\'s verse includes him there)')
        return out('the slave\'s soul not his — no vow', ['exempt'])
    if ask == 'konam_measure':
        move('Shevuot 22a:9 (Rav Pappa); 22a:2; 22a:6 (R. Akiva)', 'konamot forbid ANY AMOUNT — the item itself "like an offering"; no misuse of consecrated property applies to a konam (R. Akiva)')
        dat('the row konam_measure = %s' % data['konam_measure']['value'])
        return out('any amount — the vow forbids the object, not the act', ['vow_bound'])
    if ask == 'intimations':
        move('Nedarim 3b:4', 'the intimations ("handles" — a partial formula) from "lindor neder" or from "according to all that proceeds out of his mouth" — two sources')
        return out('the partial formula binds — two sources for one rule', ['vow_bound'])
    if ask == 'all_that_proceeds':
        ink('30:3', '"according to all that proceeds out of his mouth he shall do" — one seat, its echoes 32:24 (the next portion) and Judg 11:36')
        move('Rosh Hashanah 6a:5 (the baraita on Deut 23:24)', '"that which has gone out of your lips": a POSITIVE mitzva; "you shall keep": a PROHIBITION; "and do": the COURT\'S warrant to compel')
        return out('the vow\'s fulfilment — a positive duty, a prohibition, and the court\'s compulsion on one clause', ['commanded'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE DAUGHTER (Num 30:4-6) ==========================================================================
def the_daughter(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'in_her_youth':
        stage = case['stage']
        ink('30:4', '"and a woman, when she vows a vow to the LORD, and binds a bond IN HER FATHER\'S HOUSE IN HER YOUTH" — "in her youth" %s (computed)' % IN_HER_YOUTH)
        move('Sifrei 153:4', '"in her youth" — past minority, short of maturity: twelve years and a day; the mature daughter outside the father\'s power')
        move('Mishnah Nedarim 10:2, 11:10 (89b:2)', 'the father never annuls in her maturity; the Rabbis\' three whose vows stand — the mature, the orphan, the orphan in her father\'s lifetime')
        dat('the row vow_ages = %s' % data['vow_ages']['value'])
        if stage == 'minor':
            return out('a minor — no vow', ['exempt'])
        return out('in her youth — under her father' if stage == 'youth' else 'mature — her vow stands, no annuller', ['vow_bound'])
    if ask == 'fathers_domain':
        ink('30:4', '"in her father\'s house" — his DOMAIN')
        move('Sifrei 153:4; Nedarim 70a-70b', 'widowed or divorced from BETROTHAL she is still his; "in her youth in her father\'s house" — all her youth in his house: the widow of marriage excluded')
        return out('the father\'s domain — the betrothal\'s widow in, the marriage\'s out', ['accepted'])
    if ask == 'hearing_by_report':
        ink('30:5-6', '"and her father HEARS her vow" — "on the day of HIS HEARING" (30:6): the hearing by report counts (Sifrei 153:5)')
        move('Nedarim 72b:10', 'even R. Yoshiyah\'s steward never heard — hearing by report is no obstacle')
        return out('told by others — the hearing day opens', ['vow_confirmed'])
    if ask == 'the_deaf':
        ink('30:5', '"and her father hears" — the deaf excluded (Sifrei 153:5, 153:8)')
        move('Nedarim 73a:4 (Rava\'s baraita)', '"and her husband hears it" excludes the wife of a deaf man — the deaf cannot annul')
        dat('the row hearing_required = %s' % data['hearing_required']['value'])
        return out('the deaf hear nothing — no hearing day, no annulment', ['exempt'])
    if ask == 'intends_her':
        ink('30:5', '"and her father is silent TO HER" — the intended daughter (Sifrei 153:5: "I thought it was my wife\'s" — he may still annul)')
        move('Mishnah Nedarim 11:5 (86b:4-5); 87a:3-4', 'the wife\'s vow thought the daughter\'s, figs thought grapes — he must annul AGAIN; a specified wrong report voids the act')
        return out('the annulment void — the intended vow only; he annuls again', ['accepted'])
    if ask == 'confirmed_for_one_hour':
        ink('30:5', '"then all her vows SHALL STAND" — the stand-root twelve tokens in the chapter')
        move('Sifrei 153:5; Nedarim 79a:1', 'CONFIRMED FOR ONE HOUR, NEVER ANNULLED — silence confirms, silence does not annul; confirmed, he cannot annul')
        move('Nedarim 70a:4', 'the hour itself left open on the shelf ("and I" read as confirmed forever) — the day stands')
        return out('confirmed once, never annulled', ['vow_confirmed'])
    if ask == 'restraint_is_annulment':
        ink('30:6, 30:9', '"and if her father RESTRAIN her" — defined by the pair at 30:9 "he restrains her and ANNULS her vow" (the two verbs adjacent here alone, computed at index %s)' % RESTRAIN_ANNUL)
        move('Sifrei 153:6, 153:9; Nedarim 71b-72a', 'restraint is annulment; silence on the hearing day is as the vow\'s day')
        return out('restraint = annulment — the word defined by its pair', ['vow_annulled'])
    if ask == 'fathers_hearing_day':
        ink('30:6', '"on the day of his hearing" — the father\'s clock')
        move('Sifrei 153:6', 'the induction from the husband refused, the a-fortiori refused, and 30:17\'s LIKENING decides — "you are compelled to liken the father to the husband" (the hekkesh: the likening by juxtaposition)')
        return out('the father\'s day by the footer\'s likening', ['vow_annulled'])
    if ask == 'forgiveness':
        ink('30:6', '"and the LORD will forgive her, because her father restrained her" — the clause\'s %d seats all in this chapter (computed)' % len(FORGIVE))
        move('Sifrei 153:6; Kiddushin 81b:5; Nazir 23a:3', 'the woman who broke a vow her father annulled without her knowing — she needs forgiveness for the INTENT (the swine and the lamb); no lashes (Nedarim 83a:1)')
        return out('annulled unknown to her — forgiven for the intent, no lashes', ['vow_annulled'])
    if ask == 'caretaker':
        ink('30:6', '"BECAUSE HER FATHER RESTRAINED HER" — his act, not her assurance, not a caretaker\'s (Sifrei 153:6)')
        move('Bava Metzia 96a:20; Nazir 12b:3; Nedarim 72b:8-9', 'R. Yoshiyah: the husband alone (the doubled "her husband"); R. Yonatan: a man\'s agent is as himself')
        dat('the row annul_by_messenger = %s' % data['annul_by_messenger']['value'])
        return out('the act his own — the messenger a recorded dispute', ['accepted'])
    if ask == 'annulment_without_hearing':
        move('Nedarim 72b:3-73a:1', 'may he annul without hearing? every proof answered "when I hear it" — UNRESOLVED; the machine keeps the ink\'s trigger')
        dat('the row hearing_required = %s' % data['hearing_required']['value'])
        return out('unresolved on the shelf — the hearing the machine\'s trigger', ['accepted'])
    if ask == 'fathers_scope':
        move('Sifrei 155:1', '"I reasoned and reversed; the reversal fell and I merited the first reasoning" — and it too fails: 30:17 likens the father to the husband')
        dat('the row fathers_scope = %s' % data['fathers_scope']['value'])
        return out('the father as the husband by the likening — the reversed induction named', ['accepted'])
    if ask == 'fathers_rights':
        move('Ketubot 46b:6, 47a:6; Kiddushin 3b:7', '"in her youth, in her father\'s house" (30:17) — her gains and her betrothal money are her father\'s: the vows\' clause generalized (a taught transfer)')
        return out('the footer\'s clause carried to her gains — labeled', ['accepted'])
    if ask == 'heart_annuls':
        move('Nedarim 79a:1; 77b:7 (the houses)', 'annulled in his heart — NOT annulled; confirmed in his heart — confirmed; Beit Hillel: the heart suffices')
        dat('the row annulment_in_the_heart = %s' % data['annulment_in_the_heart']['value'])
        return out('the annulment an act — the heart\'s arm recorded', ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE BETROTHED (Num 30:7-9) =========================================================================
def the_betrothed(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'joint_authority':
        by = set(case.get('by', []))
        ink('30:7-9', '"and if she be to a husband and her vows are upon her ... but if her husband disallow her on the day he hears" — the betrothed (R. Yoshiyah, Sifrei 153:7)')
        move('Mishnah Nedarim 10:1 (66b:10-67a:1); Rabba 67a:5; R. Yishmael\'s school 68a:1 from 30:17', 'her father AND her husband annul TOGETHER; one alone — not annulled; one confirming — needless to say')
        dat('the row betrothed_authority = %s' % data['betrothed_authority']['value'])
        return out('annulled — both together' if by == {'father', 'husband'} else 'not annulled — one alone', ['vow_annulled'] if by == {'father', 'husband'} else ['vow_bound'])
    if ask == 'be_she_shall_be':
        ink('30:7', '"and if she BE, SHE SHALL BE to a husband" — the doubled verb (its two Bible seats %s)' % BE_BE)
        move('Nedarim 67b:2; 70a:8 (Rabba); 70b:1', '"be" = betrothal; two beings = TWO BETROTHALS — the betrothed dies and the authority reverts to the father')
        return out('the doubled verb read as law — betrothal, and the second betrothal after the first\'s death', ['accepted'])
    if ask == 'fathers_death':
        move('Mishnah Nedarim 10:2; 70a:7 from 30:17', 'THE FATHER DIES — the authority does not pass to the betrothed: "in her youth, in her father\'s house" even after his death')
        return out('the father dead — the betrothed alone annuls nothing; the vow stands', ['vow_bound'])
    if ask == 'betrotheds_death':
        heard = case.get('husband', 'unheard')
        move('Mishnah Nedarim 10:2; 70a:8; the baraita 68a:5-68b:1', 'THE BETROTHED DIES — reversion to the father when he had not heard, or heard and was silent, or annulled and died THE SAME DAY; if he confirmed, or died silent THE NEXT DAY — the father cannot')
        if heard in ('unheard', 'silent_same_day', 'annulled_same_day'):
            return out('reverted to the father — he annuls alone', ['vow_annulled'])
        return out('confirmed before his death — the father cannot', ['vow_confirmed'])
    if ask == 'vows_carried':
        ink('30:7', '"and her vows are UPON HER" — the vows brought from the father\'s house (Sifrei 153:7); "upon her" superfluous (Nedarim 71a:3)')
        move('Nedarim 71a:2 (Shmuel); Mishnah Nedarim 10:3', 'the LAST betrothed annuls even vows disclosed to the first; betrothed a hundred times the same day — her father and her last husband annul')
        return out('the vows carried to the last betrothed — annulled with the father', ['vow_annulled'])
    if ask == 'share_or_weaken':
        move('Nedarim 69a:1-2, 71b:1', 'Beit Shammai: each severs HALF; Beit Hillel: the annulment WEAKENS the whole — the father annuls the whole again; the halakha (the ruling) as Beit Hillel')
        dat('the row share_or_weaken = %s' % data['share_or_weaken']['value'])
        return out('the joint annulment weakens, never severs', ['accepted'])
    if ask == 'fathers_confirmation':
        move('Nedarim 67b:4', 'the father\'s CONFIRMATION blocks — the betrothed can no longer annul')
        return out('one confirming — confirmed', ['vow_confirmed'])
    if ask == 'dissolved_confirmation':
        move('Nedarim 67a:4', 'one annulled, the other confirmed and had his confirmation dissolved by a sage — they must annul TOGETHER anew')
        return out('the dissolved confirmation does not revive the other\'s annulment', ['accepted'])
    if ask == 'utterance_is_oath':
        ink('30:7', '"or the UTTERANCE of her lips with which she bound her soul" — the noun\'s two seats %s (computed)' % UTTERANCE)
        move('CALLED cold_run_vayikra5.graded_offering(utterance_oath) -> %s / %s [IMPORT, live]' % (OATH_OPTION[0], OATH_NO_OPTION[0]), 'the utterance IS an oath — Lev 5:4 "to utter with the lips" (Sifrei 153:7; Shevuot 20a:4-9): the option template the oath\'s own')
        return out('the utterance of her lips = an oath — Leviticus 5:4 by call', ['accepted'])
    if ask == 'annul_in_advance':
        ink('30:9', '"and he annul her vow WHICH IS UPON HER" — the vows upon her, not those she will make (Sifrei 153:10)')
        move('Mishnah Nedarim 10:7 (75a:5); 75a:6', 'R. Eliezer: annulled in advance; the Rabbis: "confirm IT ... annul IT" — what came to confirmation came to annulment')
        dat('the row annul_in_advance = %s' % data['annul_in_advance']['value'])
        return out('"all vows you will vow are annulled" — nothing (the Rabbis)', ['vow_bound'])
    if ask == 'confirmation_and_annulment_reach':
        ink('30:14', '"her husband shall confirm IT, or her husband shall annul IT" — the two verbs with the one suffix %s (computed)' % (CONFIRM_ANNUL_IT,))
        move('Sifrei 153:10; Nedarim 75a:6, 76b:1', 'the parallel reach — what can come to confirmation can come to annulment, what cannot, cannot')
        return out('the two verbs one reach', ['accepted'])
    if ask == 'divorce_as':
        move('Nedarim 71b:2-72a:8', 'divorce after the hearing — as silence or as confirmation? every proof turned; UNRESOLVED')
        dat('the row divorce_as = %s' % data['divorce_as']['value'])
        return out('unresolved — the machine writes nothing at a divorce', ['accepted'])
    if ask == 'sustained_betrothed':
        move('Mishnah Nedarim 10:5 (73b:1); 73b:5 (Rav Pinchas in Rava\'s name)', 'the adult who waited twelve months — R. Eliezer: the husband annuls alone ("every woman vows on her husband\'s consent"); the Rabbis: not until she enters')
        dat('the row betrothed_authority = %s' % data['betrothed_authority']['value'])
        return out('the sustained betrothed — R. Eliezer\'s arm recorded; the Rabbis rule', ['accepted'])
    if ask == 'levirate_widow':
        move('Mishnah Nedarim 10:6 (74a:1-4); 74a:5-75a:3', 'R. Eliezer annuls; R. Yehoshua one brother; R. Akiva never — the bond not substantial, no stoning for her')
        dat('the row yavam_annuls = %s' % data['yavam_annuls']['value'])
        return out('the levirate widow — R. Akiva: no annulment', ['accepted'])
    if ask == 'two_wives':
        ink('30:9', '"he restrains HER" — the singular')
        move('Nedarim 73a:5-7 (R. Yehuda)', 'as "and he shall make HER drink" (5:27) is one woman, so "disallows HER" — not two wives at once (NS.sotah\'s two_at_once by reference)')
        return out('one wife at a time', ['accepted'])
    if ask == 'same_day_hundred':
        move('Mishnah Nedarim 10:3 (71a:1)', 'betrothed, vowed, divorced and betrothed again the same day, even to a hundred — her father and her LAST husband annul')
        return out('the last husband and the father annul', ['vow_annulled'])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE WIDOW AND THE DIVORCEE (Num 30:10) =============================================================
def the_widow(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'from_marriage':
        ink('30:10', '"but the vow of a widow or of a divorced woman ... shall stand against her" — "a widow or a divorced woman" %s (computed)' % WIDOW_DIVORCEE)
        move('Sifrei 154:1; Ketubot 49a:2 (R. Yishmael\'s school)', 'from MARRIAGE, not from betrothal — as the mature daughter has wholly left the father\'s domain, so these: out of the father\'s and the husband\'s — who could annul?')
        return out('no annuller — the vow stands', ['vow_bound'])
    if ask == 'orphan_in_fathers_lifetime':
        move('Sifrei 154:1 (R. Akiva); Mishnah Nedarim 11:10; 89b:2 (Rav)', '"an orphan in her father\'s lifetime" — R. Yehuda\'s nine, the Rabbis\' THREE: the mature, the orphan, the orphan in her father\'s lifetime')
        return out('the orphan in her father\'s lifetime — her vows stand', ['vow_bound'])
    if ask == 'remarried':
        when = case['when']
        ink('30:11', '"and if in her husband\'s house she vowed" — in any event, even a forbidden marriage (Sifrei 154:1: the high priest\'s widow, the common priest\'s divorcee)')
        move('Mishnah Nedarim 11:9 (88b:7); 89a:1', 'the widow\'s "nazirite after thirty days" — married within, the new husband CANNOT annul; a vow made under him — he annuls')
        return out('vowed in widowhood — the new husband annuls nothing' if when == 'before' else 'vowed in his house — the husband annuls', ['vow_bound'] if when == 'before' else ['vow_annulled'])
    if ask == 'vow_timing':
        move('Nedarim 89a:2-5 (R. Yishmael / R. Akiva; Rav Chisda, Abaye)', 'the vow hung on MARRIAGE follows its taking effect (R. Yishmael), hung on DAYS its utterance; R. Akiva: the binding at widowhood')
        dat('the row widows_vow_timing = %s' % data['widows_vow_timing']['value'])
        return out('the authority at the vow\'s making — the marriage-hook the disputed arm', ['vow_bound'])
    if ask == 'once_out_one_hour':
        move('Mishnah Nedarim 11:9; Yevamot 87a:7', 'ONCE SHE LEFT TO HER OWN AUTHORITY ONE HOUR — vowed, divorced and taken back the same day: he cannot annul; handed to the husband\'s messengers and widowed on the way — out')
        return out('out one hour — the earlier vows beyond him', ['vow_bound'])
    if ask == 'priests_daughter_pair':
        ink('30:10, 30:4', '"a widow or a divorced woman" and "in her youth" — the priest\'s daughter\'s words at Lev 22:13 (the three Torah seats of the pair; computed)')
        move('CALLED cold_run_priesthood.holy_food(return) -> %s; (eating_table, after=fathers_house) -> %s [IMPORT, live]' % (PR_RETURN['v']['widow_and_divorcee'], PR_TABLE['v']), 'the priest\'s daughter returns to her father\'s bread; Yevamot 87a:6 — not to her father\'s POWER over vows (Rava, from 30:10)')
        return out('the pair of words shared — the return is for terumah, not for vows', ['accepted'])
    if ask == 'levirate':
        move('Mishnah Nedarim 10:6', 'the widow awaiting the brother-in-law — R. Akiva: he annuls nothing')
        dat('the row yavam_annuls = %s' % data['yavam_annuls']['value'])
        return out('awaiting the brother-in-law — her vow stands', ['vow_bound'])
    return out('no verdict in span', [FX.NONE])
