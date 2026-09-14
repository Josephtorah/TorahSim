

# ===== F4: THE SUSPECTED WIFE (Num 5:11-31) =================================================================
def sotah(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'conditions':
        ink('5:13', '"a man lay with her... hidden from her husband\'s eyes, and she was secreted and defiled, and there is no witness against her, and she was not seized" — six clauses (the reading\'s NS05B-02)')
        return out('six: lain with, hidden, secreted, defiled, no witness, not seized', ['forbidden_to_her_husband'])
    if ask == 'witnesses':
        what = case['what']
        ink('5:13', '"and there is no witness [ed] against her [bah]" — the singular: not two witnesses, one (Sotah 2a:12)')
        if what == 'defilement':
            return out('one witness suffices (5:13)', ['forbidden_to_her_husband'])
        s = data['sotah_witness_counts']['value']; dat('the row sotah_witness_counts = %s: %s' % (s, data['sotah_witness_counts']['settings'][s]))
        if what == 'warning':
            return out('two (R. Yehoshua; the mishnah)', ['forbidden_to_her_husband'])
        if what == 'seclusion':
            return out('two (R. Yehoshua) — R. Eliezer one' if s == 'two_two_one' else 'one or himself (R. Eliezer)', ['forbidden_to_her_husband'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'secluded':
        s = data['secreting_minimum']['value']; dat('the row secreting_minimum = %s: %s' % (s, data['secreting_minimum']['settings'][s]))
        ink('5:13', '"and she was defiled SECRETLY" — the measure of seclusion = the time for defilement (Sotah 2b:21, 4a:9)')
        return out('the time for the first stage of intercourse — the returning of a palm (R. Eliezer)', ['forbidden_to_her_husband'])
    if ask == 'status':
        who = case['who']
        if who in ('betrothed', 'awaiting_levir'):
            ink('5:29', '"when a wife, UNDER HER HUSBAND, goes aside"'); move('Mishnah Sotah 4:1; Kiddushin 27b:7; Sotah 24a:11-12', 'the betrothed and the widow awaiting the levir neither drink nor collect — not yet under her husband (R. Yoshiya: the widow drinks — recorded)')
            return out('neither drinks nor collects (5:29 under her husband)', ['exempt', 'ketubah_forfeited'])
        if who == 'forbidden_marriage':
            move('Mishnah Sotah 4:1', 'a widow to a High Priest, a divorcee to a priest, a mamzeret to an Israelite — the rite applies to permitted marriages')
            return out('neither drinks nor collects (a forbidden marriage)', ['exempt', 'ketubah_forfeited'])
        if who == 'ailonit':
            ink('5:28', '"she shall be cleared and sown with seed" — whose way is to bear'); move('Sotah 25b-26a; Mishnah 4:3', 'the sexually undeveloped woman neither drinks nor collects (R. Elazar: drinks — recorded)')
            return out('neither (the Rabbis; R. Elazar: drinks)', ['exempt', 'ketubah_forfeited'])
        if who == 'convert':
            ink('5:12', '"and SAY TO THEM" — the amplification'); move('Sotah 26a:11; Mishnah Eduyot 5:6', 'the proselyte woman drinks (the Sages; Akavya: not — Karkemit)')
            return out('drinks (the Sages; Akavya recorded)', ['tested_by_the_waters'])
        if who == 'priests_wife':
            move('Mishnah Sotah 4:4; Sotah 26a:12; Yevamot 56b', 'the priest\'s wife drinks; cleared she is permitted (raped she would be forbidden — "she")')
            return out('drinks; cleared she is permitted', ['tested_by_the_waters'])
        if who == 'eunuchs_wife':
            move('Mishnah Sotah 4:4; Sotah 26a:15', 'the eunuch\'s wife drinks — "besides your husband" does not exclude him')
            return out('drinks', ['tested_by_the_waters'])
        if who == 'pregnant_or_nursing':
            move('Mishnah Sotah 4:3', 'R. Meir: neither; the Rabbis: he separates and remarries — drinks')
            return out('the Rabbis: drinks; R. Meir: neither', ['tested_by_the_waters'])
        if who == 'married':
            return out('drinks or forfeits her contract (Mishnah 4:3)', ['tested_by_the_waters'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'husband_clean':
        ink('5:31', '"and the man shall be clear from iniquity, and that woman shall bear her iniquity"')
        move('Kiddushin 27b:9; Shevuot 5a:10; Sotah 28a:1, 47b; Yevamot 58a:12; Sifrei 21:3', 'when the man is clear the water tests his wife; not clear — it does not (the reading\'s NS05B-11)')
        return out('tested' if case.get('clean', True) else 'the waters do not test — the man not clear of iniquity (5:31)', ['tested_by_the_waters'] if case.get('clean', True) else ['exempt'])
    if ask == 'husband_first':
        ink('5:20', '"some man has lain with you BESIDES your husband"'); move('Sotah 24b:2; Yevamot 58a:14 (R. Acha bar Chanina)', 'only when the husband\'s cohabitation preceded the paramour\'s')
        return out('only when the husband\'s cohabitation preceded (5:20)', ['tested_by_the_waters'])
    if ask == 'husband_dead':
        s = data['husband_died_ketubah']['value']; dat('the row husband_died_ketubah = %s: %s' % (s, data['husband_died_ketubah']['settings'][s]))
        return out('Beit Hillel: no drink, no ketubah' if s == 'no_drink_no_ketubah' else 'Beit Shammai: collect, no drink', ['exempt', 'ketubah_forfeited'] if s == 'no_drink_no_ketubah' else ['exempt'])
    if ask == 'warned_about':
        who = case['who']
        if who in ('relative', 'gentile', 'shachuf'):
            move('Mishnah Sotah 4:4; Sotah 26b:1-6 (Shmuel; Rav Hamnuna)', 'a warning about a forbidden relative, a gentile, a shachuf — valid (the two "defiled"s do not exclude)')
            return out('valid', ['forbidden_to_her_husband'])
        if who in ('minor', 'beast'):
            ink('5:13', '"and a MAN lay with her"'); move('Mishnah Sotah 4:4; Sotah 26b:2', 'not a minor, not one who is not a man')
            return out('no warning', ['exempt'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'warning_scope':
        ink('5:12', '"and say to them"'); move('Sotah 24a:10', 'the betrothed and the widow awaiting the levir are included in the WARNING (forbidden by it), not the drinking')
        return out('the betrothed and the shomeret yavam can be warned, not tested', ['forbidden_to_her_husband'])
    if ask == 'court_warns':
        ink('5:12', '"the wife of ANY man"'); move('Mishnah Sotah 4:5; Sotah 27a:7-9', 'the court warns the deaf-mute\'s, the imbecile\'s, the prisoner\'s wife — to disqualify the ketubah (the Sages); R. Yosei: to drink when he returns')
        return out('to disqualify the ketubah (the Sages); R. Yosei: to drink too', ['ketubah_forfeited'])
    if ask == 'witnesses_overseas':
        move('Sotah 6a:10 (Rav Sheshet)', '"no witness against her" — witnesses overseas exist: the water does not test her')
        return out('not tested — witnesses exist overseas', ['exempt'])
    if ask == 'witnesses_conspiring':
        move('Keritot 24a:9 (R. Elazar)', 'the witnesses to her seclusion found conspiring — her meal-offering non-sacred')
        return out('her minchah non-sacred', ['exempt'])
    if ask == 'rumor':
        move('Mishnah Sotah 6:1', 'warned and secluded on a bird\'s word — R. Eliezer: divorces her with the ketubah; R. Yehoshua: not until the spinners by moonlight')
        return out('R. Eliezer: divorce with the ketubah; R. Yehoshua: not until the spinners', ['forbidden_to_her_husband'])
    if ask == 'witness_of_defilement':
        who = case['who']
        move('Mishnah Sotah 6:2', 'one witness of defilement — she does not drink; a slave or maidservant believed to bar the ketubah; her mother-in-law and the four believed only to bar the drinking')
        return out('believed — bars the ketubah' if who in ('slave', 'maidservant', 'any') else 'believed only to bar the drinking', ['ketubah_forfeited'] if who in ('slave', 'maidservant', 'any') else ['exempt'])
    if ask == 'contradicting':
        f, a = case['for'], case['against']
        move('Mishnah Sotah 6:4', 'one against one, one against two — she drinks; two against one — does not drink, divorced')
        return out('does not drink, divorced' if (f == 2 and a == 1) else 'drinks', ['exempt'] if (f == 2 and a == 1) else ['tested_by_the_waters'])
    if ask == 'escort':
        ink('5:15', '"the MAN shall bring his wife to the priest"'); move('Sotah 7a:10; Mishnah 1:3', 'by Torah law he alone; the Sages: two scholars accompany (R. Yehuda: trusted)')
        return out('two scholars (rabbinic; R. Yehuda: trusted)', ['tested_by_the_waters'])
    if ask == 'court':
        ink('5:30', '"all this LAW"'); move('Sotah 7b:3 (torah/torah with Deut 17:11); Mishnah 1:4', 'the Great Sanhedrin of seventy-one')
        return out('the Sanhedrin of seventy-one (torah/torah)', ['tested_by_the_waters'])
    if ask == 'admonition':
        move('Mishnah Sotah 1:4', 'threatened as capital witnesses: wine, levity, immaturity, bad neighbors; act for the great Name, that it not be erased')
        return out('wine, levity, immaturity, bad neighbors; act for the great Name', ['tested_by_the_waters'])
    if ask == 'confesses':
        move('Mishnah Sotah 1:5', '"I am defiled" — she writes a receipt for her contract and is divorced')
        return out('a receipt for the ketubah; divorced', ['ketubah_forfeited', 'forbidden_to_her_husband'])
    if ask == 'place':
        ink('5:18', '"the priest shall stand the woman BEFORE THE LORD"'); move('Sotah 8a:2; Mishnah 1:5', 'the Eastern Gate — Nicanor\'s, opposite the Sanctuary')
        return out('the Nicanor gate — before the LORD', ['tested_by_the_waters'])
    if ask == 'uncovering':
        ink('5:18', '"and uncover the woman\'s head"'); move('Sotah 8a:10; Mishnah 1:5-6', 'the head, the body, the hair unbraided; black garments; the adornments removed; the Egyptian rope; watchers except her slaves (R. Yehuda: unless attractive)')
        return out('the head, the body, the hair unbraided; black garments; the Egyptian rope; the adornments removed', ['tested_by_the_waters'])
    if ask == 'minchah_form':
        ink('5:15', '"a tenth of an ephah of BARLEY meal; he shall pour no oil on it nor put frankincense on it"'); move('Mishnah Sotah 2:1; Menachot 59a:5; Mishnah Menachot 5:3', 'barley, unsifted; in a basket then a service vessel; neither oil nor frankincense')
        move('CALLED cold_run_minchah.adjuncts(sinner) -> %s [IMPORT, live]' % ADJ_SINNER, 'the sinner\'s meal-offering (Lev 5:11) the parallel — neither (the Sifrei 8:1\'s reading)')
        return out('barley, unsifted; no oil, no frankincense — as the sinner\'s: ' + ADJ_SINNER, ['accepted'])
    if ask == 'ephah':
        move('Onkelos 5:15 (the reading\'s crown)', '"a tenth of THREE SE\'AH" — the conversion layer on a dry measure')
        return out('a tenth of an ephah = a tenth of three se\'ah (Onkelos)', ['accepted'])
    if ask == 'fistful':
        f = MN.fistful('overflowing_or_fingertips')['v']                                                          # THE CALL
        ink('5:26', '"the priest shall take a fistful of the meal-offering, its memorial, and burn it on the altar"')
        move('CALLED cold_run_minchah.fistful(overflowing_or_fingertips) -> %s [IMPORT, live]' % f, 'the scoop\'s measure the meal-offering engine\'s: level, three fingers over the palm')
        return out('the scoop level — the meal-offering engine: overflowing or fingertips ' + f, ['accepted'])
    if ask == 'waving':
        ink('5:25', '"the priest shall take the meal-offering from the woman\'s HAND and wave it"'); move('Kiddushin 36b:4-5; Sotah 19a:9-10; Mishnah 3:1', 'hand/hand with Lev 7:30 — by her hand and the priest\'s together')
        return out('by her hand and the priest\'s together (hand/hand with Lev 7:30)', ['accepted'])
    if ask == 'bringing_near':
        ink('5:25', '"and draw it near to the altar"'); move('Menachot 60b:6, 61a:8; Mishnah Menachot 5:6', 'the sotah\'s minchah requires both bringing near and waving')
        return out('required (5:25 draw it near)', ['accepted'])
    if ask == 'minchah_not_for_its_name':
        ink('5:15', '"a reminder of iniquity" / Lev 10:17 "to bear the iniquity"'); move('Menachot 4a:8-16', 'like a sin-offering: not for its name disqualified; the surplus to communal gifts')
        return out('disqualified; the surplus to communal gifts', ['disqualified'])
    if ask == 'water_and_dust':
        ink('5:17', '"holy water in an earthen vessel; and of the dust on the floor of the tabernacle... into the water"')
        s = data['dust_order']['value']; dat('the row dust_order = %s' % s)
        move('Mishnah Sotah 2:2; Sotah 15b; Menachot 88b:3; Temurah 12b:6', 'half a log from the laver (R. Yehuda a quarter); the cubit-square tablet, the ring, the dust visible; water first')
        return out('half a log from the laver (R. Yehuda a quarter); the dust from the Sanctuary floor, visible on the water; water first (R. Shimon: either)', ['accepted'])
    if ask == 'vessel':
        move('Sotah 15b:4 (R. Yishmael: vessel/vessel with the leper\'s); 15b:9 (Rabba)', 'a NEW earthenware vessel')
        return out('a new earthenware vessel (R. Yishmael)', ['accepted'])
    if ask == 'bitter_added':
        ink('5:23', '"into the water of BITTERNESS" — bitter before the erasure'); move('Sotah 20a:4 (Shmuel\'s father)', 'a bitter substance is put in')
        return out('a bitter substance in the water', ['accepted'])
    if ask == 'scroll_text':
        move('Mishnah Sotah 2:3; Sotah 17a; Berakhot 15b:24', 'the Rabbis: 5:19 through 5:22\'s curses, without 5:21\'s frame and the amens; R. Yosei the whole; R. Yehuda the curses alone')
        return out('from 5:19 through 5:22\'s curses, without the frame and the amens (the Rabbis); R. Yosei whole; R. Yehuda curses alone', ['accepted'])
    if ask == 'scroll_material':
        ink('5:23', '"the priest shall write these curses IN A SCROLL and blot them out into the water"'); move('Mishnah Sotah 2:4; Sotah 17b:1-2; Eruvin 13a:10', 'parchment; ink that can be blotted out — no iron sulfate')
        return out('a scroll (parchment); erasable ink; no iron sulfate', ['accepted'])
    if ask == 'scroll_time':
        move('Sotah 17b:3 (Rava; torah/torah)', 'written at night — unfit'); return out('by day', ['accepted'])
    if ask == 'scroll_order':
        move('Sotah 17b:4', '"THESE curses" — as written in the Torah'); return out('the Torah\'s order', ['accepted'])
    if ask == 'scroll_before_oath':
        ink('5:21, 5:23', 'the oath, then the writing'); move('Sotah 17b:5', 'written before the oath — unfit'); return out('unfit', ['disqualified'])
    if ask == 'scroll_erasure':
        move('Sotah 18a:2', '"all this law" — written whole, erased at once'); return out('written whole, erased at once', ['accepted'])
    if ask == 'for_her_name':
        ink('5:30', '"and the priest shall PERFORM with her all this law"'); move('Eruvin 13b:2; Sotah 20b:6', 'the erasure for her name; the writing need not be')
        return out('the erasure for her name; the writing not', ['accepted'])
    if ask == 'language':
        ink('5:21', '"and the priest shall SAY to the woman"'); move('Sotah 32b:2; Mishnah 7:1', 'in any language')
        return out('any language', ['accepted'])
    if ask == 'oath_order':
        ink('5:19-20', 'the innocent clause first, then "but if you have gone aside"'); move('Sanhedrin 32b:18 (Rebbi; Abaye and Rava)', 'the priest states the innocent scenario first')
        return out('the innocent clause first', ['accepted'])
    if ask == 'oaths_count':
        ink('5:19, 5:21', '"the priest shall cause her to swear" — twice'); move('Sotah 18a:8 (R. Zeira, Rav)', 'one before the erasure, one after')
        return out('two: before and after the erasure', ['accepted'])
    if ask == 'amen_amen':
        ink('5:22', '"and the woman shall say: amen, amen" — the bare double at Num 5:22 and Neh 8:6 alone (the reading)'); move('Mishnah Sotah 2:5; Kiddushin 27b:6', 'on the curse and the oath; this man and another; betrothed, married, awaiting the levir, married to the levir')
        return out('on the curse and the oath; this man and another; betrothed, married, awaiting the levir, married to the levir', ['accepted'])
    if ask == 'amen_is_oath':
        move('Shevuot 29b:9 (Shmuel)', 'one who answers amen is as one who swore'); return out('amen = her oath (Shmuel)', ['accepted'])
    if ask == 'oath_form':
        ink('5:21', '"the oath of the curse" — Lev 5:1\'s "curse" by the identity (Sifrei 14:1)'); move('Shevuot 35b:23-36a:10', 'an oath is a curse, administered in the Name; amen the oath')
        return out('a curse, in the Name', ['accepted'])
    if ask == 'oath_scope':
        move('Mishnah Sotah 2:6', 'not before betrothal nor after divorce — only acts that would forbid her'); return out('only acts that would forbid her', ['accepted'])
    if ask == 'several_warnings':
        ink('5:29', '"this is the law of JEALOUSIES" — plural'); move('Keritot 9b:10', 'one meal-offering for several warnings'); return out('one meal-offering (jealousies)', ['accepted'])
    if ask == 'order':
        s = data['sotah_order']['value']; dat('the row sotah_order = %s: %s' % (s, data['sotah_order']['settings'][s]))
        return out('drink then offer (the Rabbis); R. Shimon offer then drink; either valid after the fact', ['tested_by_the_waters'])
    if ask == 'preconditions':
        ink('5:26', '"AFTERWARD he shall make the woman drink"'); move('Sotah 19b:2 (R. Shimon)', 'three preclude: the fistful offered, the scroll erased, the oath accepted')
        return out('R. Shimon: the fistful offered, the scroll erased, the oath accepted', ['tested_by_the_waters'])
    if ask == 'refuses':
        when = case['when']
        move('Mishnah Sotah 3:3; Sotah 19b:1 (R. Akiva)', 'before the erasure: the scroll sequestered, the minchah burned; after: forced; confessed after: the water poured out')
        if when == 'before_erasure':
            return out('the scroll sequestered, the minchah burned; not forced', ['exempt'])
        if when == 'after_erasure':
            return out('forced to drink', ['tested_by_the_waters'])
        if when == 'confesses_after_erasure':
            return out('the water poured out, the minchah scattered', ['ketubah_forfeited'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'time':
        move('Mishnah Megillah 2:5; Megillah 20b:9, 20b:17; Sotah 17b:3', 'by day, the whole day'); return out('by day, the whole day', ['tested_by_the_waters'])
    if ask == 'two_at_once':
        ink('5:16, 5:27', '"bring HER near"; "make HER drink" — her alone'); move('Sotah 8a:4; Nedarim 73a:7 (R. Yehuda)', 'not two together'); return out('not together', ['tested_by_the_waters'])
    if ask == 'outcome':
        if case.get('guilty'):
            if case.get('merit'):
                s = data['merit_suspends']['value']; dat('the row merit_suspends = %s: %s' % (s, data['merit_suspends']['settings'][s]))
                return out('suspended (three, nine, twelve months — the Sifrei; one to three years — the mishnah; R. Shimon none)', ['tested_by_the_waters'])
            ink('5:27', '"her belly shall swell and her thigh fall, and the woman shall be a curse"'); move('Mishnah Sotah 3:4, 1:7; Sotah 9b, 28a:14', 'her face greens, her eyes bulge — the thigh first (measure for measure); the paramour too')
            return out('her face greens, her belly swells, her thigh falls — she dies; the paramour too', ['tested_by_the_waters', 'put_to_death'])
        ink('5:28', '"and if the woman was not defiled but is clean, she shall be cleared and sown with seed"'); move('Sotah 26a:7-8 (R. Akiva / R. Yishmael)', 'the barren conceives; or pain to ease, females to males')
        return out('cleared and sown with seed (the barren conceives — R. Akiva; R. Yishmael: ease)', ['tested_by_the_waters', 'accepted'])
    if ask == 'paramour_tested':
        ink('5:24, 5:27', '"the water shall enter her" twice'); move('Mishnah Sotah 5:1; Sotah 27b:3, 28a:9-10', 'the water tests him as her')
        return out('tested too (5:24, 5:27)', ['tested_by_the_waters'])
    if ask == 'defiled_consequences':
        ink('5:14, 5:27, 5:29', '"defiled" thrice; 5:29\'s "AND is defiled" the vav'); move('Sotah 28a:19, 29a:2 (R. Akiva); Mishnah 5:1', 'forbidden to her husband, to her paramour, to the priesthood, from terumah')
        return out('forbidden to her husband, her paramour, the priesthood and terumah (R. Akiva)', ['forbidden_to_her_husband'])
    if ask == 'doubt_forbids':
        ink('5:14', '"and she was defiled... or she was not defiled" — the doubtful case'); move('Sotah 28a:21; Mishnah 1:2', 'forbidden to her husband until clarified')
        return out('forbidden to her husband until clarified', ['forbidden_to_her_husband'])
    if ask == 'levirate':
        move('Yevamot 11a:10; Mishnah Sotah 1:2', '"defiled" with Lev 18:24\'s — as a forbidden relative: she and her rival exempt from levirate and chalitzah')
        return out('exempt from levirate and chalitzah (Yevamot 11a)', ['exempt'])
    if ask == 'minchah_disposition':
        c = case['case']
        move('Mishnah Sotah 3:6-7', 'impure before the vessel — redeemed; after — burned; the confessed, the witnessed, the refusing, the husband\'s refusal or cohabitation — burned; every priest\'s wife\'s burned; a priest\'s daughter married to an Israelite — eaten')
        if c == 'priests_daughter_to_israelite':
            return out('eaten', ['accepted'])
        return out('burned (once in a service vessel; redeemed if before)', ['disqualified'])
    if ask == 'disabled':
        ink('5:13, 5:18, 5:22', '"hidden from the EYES"; "STAND the woman... in her HANDS"; "the woman shall SAY"'); move('Sotah 27a:10-27b:1 (Rav Sheshet, Rav Ashi, Mar bar Rav Ashi)', 'blind, lame, handless, mute — neither side')
        return out('neither side drinks or gives to drink', ['exempt'])
    if ask == 'intercourse':
        ink('5:13', '"and SHE was not seized" — raped, permitted; "she" adds cases')
        if case.get('who') == 'priests_wife':
            move('Yevamot 56b:7', 'the priest\'s wife forbidden even when seized'); return out('forbidden (the priest\'s wife)', ['forbidden_to_her_husband'])
        move('Ketubot 51b:13 (Rava); 74a:13; Yevamot 100b', 'raped permitted; begun under duress ended willingly permitted; the mistaken betrothal permitted')
        return out('permitted to her husband', ['accepted'])
    if ask == 'drinks_twice':
        ink('5:29', '"this is the law of jealousy"'); move('Sotah 18b:15', 'she drinks and drinks again for a second warning'); return out('drinks again for a second warning', ['tested_by_the_waters'])
    if ask == 'abolished':
        s = data['waters_abolished']['value']; dat('the row waters_abolished = %s: %s' % (s, data['waters_abolished']['settings'][s]))
        return out('the rite runs (the ink); abolished by Rabban Yochanan ben Zakkai — Hosea 4:14 (the tradition\'s setting)', ['tested_by_the_waters'])
    if ask == 'warning_permitted':
        ink('5:14', '"and he warned his wife"'); move('Sotah 3a:17 (R. Eliezer b. Yaakov); 3a:10', 'permitted against "you shall not hate"; optional (R. Yishmael) or obligatory (R. Akiva)')
        return out('permitted (R. Eliezer b. Yaakov); optional or obligatory disputed', ['forbidden_to_her_husband'])
    if ask == 'spelling':
        ink('5:19', '"hinnaki" written WITHOUT the yod — measured on the DB: %s' % HINNAKI_DEFECTIVE); ink('5:12', '"tisteh" with the sin-dot — measured: %s' % TISTEH_SIN)
        move('Kiddushin 62a:2 (R. Tanchum); Sotah 3a:4 (Reish Lakish)', 'read also chinnaki (you shall choke); read tishteh (folly) — M-16\'s shape on the sotah\'s own verses')
        return out('hinnaki without the yod read also as chinnaki; tisteh read as folly — the ink measured', ['forbidden_to_her_husband'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE NAZIRITE (Num 6:1-21) =========================================================================
def nazirite(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'vow_form':
        form = case['form']
        ink('6:2', '"when a man or woman shall clearly utter a vow, the vow of a nazirite [nazir], to separate [lehazir]"')
        if form in ('substitute', 'intimation'):
            move('Nedarim 3a:5; Mishnah Nedarim 1:1, Nazir 1:1', 'nazir lehazir — substitutes and intimations bind'); return out('binds (nazir lehazir)', ['nazirite_vow_bound'])
        if form == 'partial':
            s = data['nazir_vow_scope']['value']; dat('the row nazir_vow_scope = %s' % s); move('Mishnah Nazir 1:2; Nazir 3b:11, 4a:3', 'one prohibition named — a full nazirite (R. Shimon: all required)')
            return out('a full nazirite', ['nazirite_vow_bound'])
        if form == 'birds':
            move('Mishnah Nazir 1:1; Nazir 2a:3, 3b:2', 'R. Meir: a nazirite (the impure nazirite\'s birds); the Sages: not'); return out('the Sages: not (R. Meir: a nazirite)', ['exempt'])
        if form == 'from_the_cup':
            move('Mishnah Nazir 2:3', 'a cup poured — a full nazirite; the intoxicated woman\'s a konam on the cup'); return out('a nazirite; the drunk woman\'s a konam', ['nazirite_vow_bound'])
        if form == 'conditioned_on_wine':
            move('Mishnah Nazir 2:4', 'on condition to drink and become impure — a full nazirite'); return out('a full nazirite', ['nazirite_vow_bound'])
        if form == 'mistaken_no_wine':
            move('Mishnah Nazir 2:4', 'did not know wine is forbidden — bound (R. Shimon: free)'); return out('bound (R. Shimon free)', ['nazirite_vow_bound'])
        if form == 'mistaken_sages_permit':
            move('Mishnah Nazir 2:4', 'thought the Sages would permit — free (R. Shimon: bound)'); return out('free (R. Shimon bound)', ['exempt'])
        if form == 'figs':
            move('Mishnah Nazir 2:1; Nazir 9a:2', 'Beit Shammai: a nazirite; Beit Hillel: not'); return out('Beit Hillel: not (Shammai: a nazirite)', ['exempt'])
        if form == 'samson':
            move('Mishnah Nazir 1:2', 'a Samson-nazirite never shaves and brings no impurity offering'); return out('a Samson-nazirite: never shaves, no impurity offering', ['nazirite_vow_bound'])
        if form == 'permanent':
            move('Mishnah Nazir 1:2', 'the permanent nazirite lightens with a razor and brings three'); return out('lightens with a razor every thirty, brings three', ['nazirite_vow_bound'])
        if form == 'ambiguous_intimation':
            move('Nedarim 5b:5', 'Abaye valid, Rava not'); return out('Rava: not', ['exempt'])
        if form == 'uncertain':
            move('Mishnah Nazir 5:5; Nazir 34a:1', 'Shammai all; Hillel whose statement failed; R. Tarfon none (explicitness)'); return out('Hillel: whose statement failed; R. Tarfon none', ['nazirite_vow_bound'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'who_vows':
        who, age = case['who'], case.get('age')
        ink('6:2', '"speak to the children of Israel... a man or woman"')
        if who == 'gentile':
            move('Nazir 61a:7-12; Mishnah 9:1; Menachot 73b', '"the children of Israel" — not the gentiles'); return out('no naziriteship', ['exempt'])
        if who == 'woman':
            move('Mishnah Nazir 9:1', 'women yes (the husband nullifies, cannot force)'); return out('yes', ['nazirite_vow_bound'])
        if who == 'slave':
            move('Nazir 61a:7; Mishnah 9:1', '"a man or woman" includes slaves (the master forces)'); return out('yes (the master forces)', ['nazirite_vow_bound'])
        if who == 'boy':
            move('Niddah 46a:2; Mishnah Niddah 5:6', 'thirteen and a day — valid; the twelfth year examined')
            return out('valid (thirteen and a day)' if age >= 13 else ('examined (the twelfth year)' if age == 12 else 'invalid'), ['nazirite_vow_bound'] if age >= 13 else ['exempt'])
        if who == 'girl':
            move('Mishnah Niddah 5:6', 'twelve and a day — valid; the eleventh year examined')
            return out('valid (twelve and a day)' if age >= 12 else ('examined (the eleventh year)' if age == 11 else 'invalid'), ['nazirite_vow_bound'] if age >= 12 else ['exempt'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'term':
        form = case['form']; d = data['nazir_default_days']['value']
        dat('the row nazir_default_days = %d: %s' % (d, data['nazir_default_days']['settings'][d]))
        if form in ('unspecified', 'long', 'short', 'till_the_end_of_the_world'):
            move('Mishnah Nazir 1:3', 'unspecified, long, short, till the end of the world — thirty'); return out('%d days' % d, ['nazirite_vow_bound'])
        if form == 'and_a_day':
            move('Mishnah Nazir 1:3', '"and a day", "and an hour", "one and a half" — two terms'); return out('%d days (two terms)' % (2 * d), ['nazirite_vow_bound'])
        if form == 'thirty_and_an_hour':
            move('Mishnah Nazir 1:3', 'no naziriteship for hours — thirty-one'); return out('31 days', ['nazirite_vow_bound'])
        if form == 'like_the_hairs':
            move('Mishnah Nazir 1:4', 'forever, shaving every thirty (Rebbi: one long term)'); return out('forever, shaving every thirty (Rebbi: one term)', ['nazirite_vow_bound'])
        if form == 'capacity':
            move('Mishnah Nazir 1:5', 'asked his intent: one long term — thirty; unspecified — mustard seeds, a life'); return out('a life (mustard seeds) or thirty by his intent', ['nazirite_vow_bound'])
        if form == 'distance':
            move('Mishnah Nazir 1:6', 'the days of the walk; under thirty — thirty'); return out('%d days' % max(d, case.get('days', 0)), ['nazirite_vow_bound'])
        if form == 'solar_year':
            move('Mishnah Nazir 1:7', '365 consecutive terms'); return out('365 terms', ['nazirite_vow_bound'])
        if form == 'hundred_days':
            return out('100 days', ['nazirite_vow_bound'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'shaving_day':
        form = case['form']
        move('Mishnah Nazir 3:1-2', 'unspecified — the thirty-first (the thirtieth fulfilled); "thirty days" — the thirty-first only; two terms — 31 and 61 (30 and 60; 59 fulfilled)')
        if form == 'unspecified':
            return out('the thirty-first (the thirtieth fulfilled)', ['nazirite_term_fulfilled'])
        if form == 'stated_thirty':
            return out('the thirty-first only', ['nazirite_term_fulfilled'])
        if form == 'two_terms':
            return out('31 and 61 (30 and 60; 59 fulfilled)', ['nazirite_term_fulfilled'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'ate':
        product, amount = case['product'], case.get('amount', 'olive')
        ink('6:3-4', '"from wine and strong drink he shall separate; vinegar... anything soaked... fresh or dried... anything made of the vine, from kernels to skin"')
        if product == 'leaves':
            s = data['nazir_leaves']['value']; dat('the row nazir_leaves = %s: %s' % (s, data['nazir_leaves']['settings'][s]))
            return out('permitted (the Rabbis; R. Elazar forbids)', ['exempt'])
        if product == 'wine' and amount == 'less_than_a_quarter_log':
            move('Mishnah Nazir 6:1; Nazir 38b:1', 'a quarter-log for drinking (R. Akiva: an olive\'s bulk with bread)'); return out('exempt (R. Akiva: an olive\'s bulk with bread)', ['exempt'])
        if product == 'mixture':
            move('Nazir 35b:12, 38a:2; Pesachim 43b (R. Yochanan; R. Elazar)', '"soaked" — permitted combines with forbidden for the nazirite alone'); return out('combines — liable (soaked)', ['lashes'])
        if product == 'seed':
            s = data['general_prohibition_lashes']['value']; dat('the row general_prohibition_lashes = %s' % s)
            return out('lashes (Rava one set; Abaye two)', ['lashes'])
        if product == 'two_seeds_one_skin':
            move('Mishnah Nazir 6:2 (R. Elazar b. Azarya)', 'liable only for two chartzannim and a zag — 6:4\'s plural and singular'); return out('R. Elazar b. Azarya\'s measure — liable', ['lashes'])
        move('Mishnah Nazir 6:1-2; Nazir 38b:2; 34b:11', 'wine, grapes, kernels, skins, vinegar each by itself — an olive\'s bulk; each kind called by two names liable for each')
        return out('lashes', ['lashes'])
    if ask == 'mitzvah_wine':
        move('Nazir 4a:3, 44a:9; Sifrei 23:1', '"wine AND strong drink" — obligatory wine like optional'); return out('forbidden like optional', ['lashes'])
    if ask == 'benefit_from_wine':
        ink('6:4', '"all the days of HIS naziriteship"'); move('Pesachim 23a:5 (Mar Zutra)', 'the nazirite may own and benefit from wine'); return out('permitted (his naziriteship)', ['exempt'])
    if ask == 'shaving_means':
        means = case['means']
        ink('6:5', '"a razor shall not come upon his head... he shall be holy, let the locks grow"')
        if means in ('razor', 'scissors'):
            move('Mishnah Nazir 6:3', 'scissors or a razor — liable'); return out('liable', ['lashes'])
        if means == 'plucked_any':
            move('Nazir 39b:5-6 (R. Yoshiya / R. Yonatan); Mishnah 6:3', 'plucked any amount — liable (R. Yoshiya; R. Yonatan exempt)'); return out('R. Yoshiya liable (R. Yonatan exempt)', ['lashes'])
        if means == 'shampoo':
            move('Mishnah Nazir 6:3', 'may shampoo and separate by hand; not comb (R. Yishmael: not with earth)'); return out('permitted; combing not', ['exempt'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'shaved_by_another':
        ink('6:5', '"a razor shall not COME upon his head" — passive'); move('Nazir 44a:17', 'he and another — both liable'); return out('both liable', ['lashes'])
    if ask == 'shaving_amount':
        ink('6:9', '"on the seventh day he shall shave IT"'); move('Nazir 42a:3', 'not fulfilled until all is removed'); return out('all the hair', ['accepted'])
    if ask == 'final_shaving_tool':
        move('Nazir 40a:2-10 (Rebbi); Mishnah 6:3\'s rider', 'the final shaving by razor; the Levites\' razor 8:7 (Beha\'alotcha\'s)'); return out('a razor', ['accepted'])
    if ask == 'impurity_kinds':
        source, mode = case['source'], case.get('mode', 'contact')
        ink('6:6-7, 6:9', '"he shall not come upon a dead body... when they die"; "if any man DIE suddenly beside him"')
        if source in ('corpse', 'olive_of_corpse', 'ladle_of_dust', 'spine', 'skull', 'limb', 'half_kav_bones', 'half_log_blood'):
            move('Mishnah Nazir 7:2', 'shaves — by contact, carrying and tent'); return out('shaves', ['count_voided'])
        if source == 'barley_grain_bone':
            move('Mishnah Nazir 7:2', 'by contact and carrying, not by tent'); return out('shaves' if mode != 'tent' else 'not — the barley-grain bone does not defile by tent', ['count_voided'] if mode != 'tent' else ['exempt'])
        if source == 'quarter_log_blood':
            move('Mishnah Nazir 7:3-4', 'R. Akiva\'s a-fortiori refused: a halakhah to Moses from Sinai'); return out('not (a halakhah to Moses from Sinai — R. Akiva\'s a-fortiori refused)', ['exempt'])
        if source in ('boughs', 'beit_haperas', 'land_of_nations', 'grave_cover', 'tent_only', 'quarter_kav_bones', 'vessels_touching'):
            move('Mishnah Nazir 7:3', 'sprinkled but no negation and no offering'); return out('not — sprinkled, no negation', ['exempt'])
        if source in ('leprosy', 'ziva'):
            move('Nazir 48a:1 (Rebbi); Mishnah 7:3', '"when they die" — not their leprosy or ziva; the leper\'s and zav\'s days count'); return out('not corpse impurity — no negation; the days count', ['exempt'])
        if source == 'creeping':
            move('Pesachim 80b:15', 'only corpse impurity interrupts'); return out('not — only the corpse', ['exempt'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'impurity_for':
        who = case['who']
        ink('6:7', '"for his father, or his mother, for his brother, or his sister he shall not become impure when they die"')
        if who == 'relative':
            move('Zevachim 100a:6; Sanhedrin 35a:13', 'not — even on the way to the Passover or the circumcision'); return out('not — even on the way to the Passover', ['exempt'])
        if who == 'met_mitzvah':
            move('Nazir 44a:8, 48a-48b; Yevamot 7a:3; Megillah 3b:8; Berakhot 19b:15; Mishnah 7:1', 'becomes impure — even on the way to the Passover'); return out('becomes impure — even on the way to the Passover', ['count_voided'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'met_mitzvah_with_high_priest':
        move('Mishnah Nazir 7:1', 'R. Eliezer: the priest (no offering); the Rabbis: the nazirite (his holiness not permanent)'); return out('the nazirite becomes impure (the Rabbis); R. Eliezer the priest', ['count_voided'])
    if ask == 'impurity_lashes':
        move('Nazir 42b:1 (Rabba, Rav Huna)', 'contact, carrying, tent — one ban; entering an enclosure — another; impure again — one set'); return out('a set per distinct ban (the corpse and the enclosure); repeated impurity one set', ['lashes'])
    if ask == 'lashes_count':
        n = case.get('warnings', 0)
        move('Mishnah Makkot 3:7-8; Mishnah Nazir 6:4', 'all day — one set; per warning followed by the act — each'); return out('%d set(s) — one, or one per warning' % max(1, n), ['lashes'])
    if ask == 'what_negates':
        act = case['act']
        ink('6:12', '"the former days shall fall, for his separation was defiled"')
        if act == 'impurity':
            day, term = case.get('day', 15), case.get('term', 30)
            if day <= 2:
                move('Nazir 19b:2-5 (Abaye; Rava)', '"the first days" plural — no negation until two days'); return out('nothing — no first days (two)', ['exempt'])
            if term == 30 and day == 30:
                move('Mishnah Nazir 3:3', 'impure on the thirtieth — negates all (R. Eliezer seven)'); return out('all (R. Eliezer seven)', ['count_voided'])
            if term == 100 and day == 100:
                move('Mishnah Nazir 3:4', 'the hundredth — all (R. Eliezer thirty)'); return out('all (R. Eliezer thirty)', ['count_voided'])
            if term == 100 and day == 101:
                move('Mishnah Nazir 3:4', 'the 101st before the offerings — thirty (R. Eliezer seven)'); return out('thirty (R. Eliezer seven)', ['count_voided'])
            move('Mishnah Nazir 6:5, 7:2; Nazir 44a:13', 'impurity negates all — recount after purification and offerings'); return out('all — recount after purification and offerings', ['count_voided'])
        if act == 'shaving':
            move('Mishnah Nazir 6:3, 6:5; Nazir 44a:13', 'shaving negates thirty'); return out('thirty', ['count_voided'])
        if act == 'wine':
            move('Nazir 44a:11', 'wine negates nothing'); return out('nothing', ['lashes'])
        if act == 'unknown_impurity':
            ink('6:9', '"BESIDE him" — known'); move('Nazir 63a:4; Pesachim 81b:4; Mishnah 9:2', 'the grave of the depths does not negate'); return out('nothing (the depths)', ['exempt'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'vowed_in_cemetery':
        move('Mishnah Nazir 3:5; Nazir 18a:2', 'the days there do not count; no shaving, no birds; left and re-entered — counts and brings (R. Eliezer: not the same day)'); return out('the days do not count; no shaving, no birds; re-entered: counts and brings', ['exempt'])
    if ask == 'defiled':
        ink('6:9-12', '"he shall shave his head on the day of his cleansing, on the seventh day; on the eighth day two turtledoves or two young pigeons... a lamb of its first year for a guilt-offering; the former days shall fall"')
        s = data['nazir_recount_day']['value']; dat('the row nazir_recount_day = %s' % s)
        move('Mishnah Nazir 6:6; Keritot 2b:5; Mishnah Keritot 2:2; Nazir 18a-18b', 'sprinkled the third and seventh, shaves the seventh, brings the eighth; intentional as unwitting; the recount from the eighth (Rebbi)')
        return out('sprinkled the third and seventh, shaves the seventh, brings the eighth (a lamb asham, two birds); intentional as unwitting; the recount from the eighth', ['count_voided'])
    if ask == 'birds':
        move('Mishnah Kinnim 1:1, 2:5; Sifrei 29:2', 'one sin-offering, one burnt-offering; a turtledove not paired with a pigeon'); return out('one chatat, one olah; not mixed', ['accepted'])
    if ask == 'completion':
        ink('6:13-18', '"he shall bring himself to the door... one he-lamb for a burnt-offering, one ewe-lamb for a sin-offering, one ram for peace-offerings, and a basket of unleavened bread... and the nazirite shall shave his consecrated head at the door of the tent of meeting"')
        move('Mishnah Nazir 6:7-8; Nazir 45a', 'three animals; shaves after the peace-offering (R. Yehuda; R. Elazar the sin); any one suffices; unspecified animals sorted by fitness')
        d = OF.dispatch('todah_and_nazir_ram')                                                                    # THE CALL
        move('CALLED cold_run_offerings.dispatch(todah_and_nazir_ram) -> %s [IMPORT, live]' % sorted(d), 'the ram\'s procedure the offering engine\'s')
        return out('three animals — the sin, the burnt, the peace; shaves after the peace-offering (R. Yehuda; R. Elazar the sin); any one suffices', ['nazirite_term_fulfilled'])
    if ask == 'where_shaves':
        ink('6:18', '"at the door of the tent of meeting... on the fire under the sacrifice of the peace-offering"'); move('Nazir 45a:13 (R. Yitzchak); Sifrei 34:1; Yoma 16a:2; 45a:14 (Abba Chanan)', 'where the peace-offering is cooked — the Chamber of the Nazirites; Abba Chanan: while the entrance is open')
        return out('where the peace-offering is cooked — the Chamber of the Nazirites (Abba Chanan: while the entrance is open)', ['nazirite_term_fulfilled'])
    if ask == 'hair_under_pot':
        where, which = case.get('where', 'temple'), case.get('which', 'purity')
        move('Mishnah Nazir 6:8; Menachot 91b:1; Temurah 34a:4', 'the purity shaving in the Temple: under the peace-offering\'s pot (the sin or guilt fulfill); the province: not thrown; the impurity shaving: not thrown, the hair buried')
        if which == 'impurity':
            return out('not thrown; the hair buried (the pure\'s burned)', ['count_voided'])
        if where == 'province':
            return out('not thrown', ['nazirite_term_fulfilled'])
        return out('under the peace-offering\'s pot (the others fulfill)', ['nazirite_term_fulfilled'])
    if ask == 'hair':
        ink('6:5', '"he shall be HOLY, let the locks grow" — the hair holy'); move('Kiddushin 57b:6; Avodah Zarah 74a:3; Temurah 28a:11; Mishnah AZ 5:9', 'forbidden for benefit in any amount; burned')
        return out('holy — forbidden for benefit in any amount; burned', ['disqualified'])
    if ask == 'loaves':
        ink('6:15', '"a basket of unleavened bread, loaves mingled with oil and wafers spread with oil, and their meal-offering and their libations"'); move('Mishnah Menachot 7:2, 3:6; Menachot 46b, 78a, 91a-b', 'loaves and wafers, ten kav; both indispensable; sanctified by the ram\'s slaughter; libations for the burnt- and peace-offerings')
        return out('loaves and wafers (no poached), ten kav; both indispensable; sanctified by the ram\'s slaughter; with libations for the burnt- and peace-offerings', ['accepted'])
    if ask == 'foreleg':
        v, e, _ = TZ.dues_machine({'ask': 'breast_thigh'}, TZ.PARAMS)                                                # THE CALL
        ink('6:19-20', '"the cooked foreleg of the ram, one loaf, one wafer on the palms of the nazirite... waved... holy to the priest beside the breast of waving and the thigh of lifting"')
        move('CALLED cold_run_tzav.dues_machine(breast_thigh) -> %s [IMPORT, live]' % v, 'I11 stated on 6:20 (Sifrei 37:1): the breast and thigh kept out of the shoulder-law; the nazirite woman waves too (Kiddushin 36b:7)')
        return out('the cooked foreleg, a loaf and a wafer on his palms, waved (the woman too); beside the ' + v, ['due_to_priest'])
    if ask == 'foreleg_bounds':
        move('Mishnah Chullin 10:4', 'from the lower knee joint to the thigh bone\'s protrusion'); return out('the lower knee joint to the thigh bone\'s protrusion (Mishnah Chullin 10:4)', ['due_to_priest'])
    if ask == 'ram_eaten_by':
        move('Zevachim 55a:6', 'the foreleg the priest\'s; the rest the owner\'s'); return out('the owner; the foreleg the priest\'s', ['accepted'])
    if ask == 'asham':
        d = OF.dispatch('communal_shelamim_and_asham')                                                            # THE CALL
        move('CALLED cold_run_offerings.dispatch(communal_shelamim_and_asham) -> %s [IMPORT, live]' % sorted(d), 'Mishnah Zevachim 5:5: the nazirite\'s guilt-offering — north, two-that-are-four, male priests, a day and a night; eaten by the priests (Menachot 73a)')
        return out('north; two placements that are four; male priests within the curtains, a day and a night (Mishnah Zevachim 5:5)', ['due_to_priest'])
    if ask == 'permitted_after':
        s = data['nazir_permitted_after']['value']; dat('the row nazir_permitted_after = %s' % s); ink('6:20', '"and AFTER THAT the nazirite may drink wine"')
        return out('after one offering (the Rabbis; R. Shimon); R. Eliezer after all', ['nazirite_term_fulfilled'])
    if ask == 'after_term_before_offerings':
        ink('6:6', '"ALL the days"'); move('Nazir 14b:9-15a:1 (the baraita)', 'flogged for impurity, shaving and wine alike'); return out('lashes for impurity, shaving and wine alike (the baraita)', ['lashes'])
    if ask == 'waving_indispensable':
        move('Nazir 46b:1 (Tosefta 1:5) / Menachot 19a:12 (Rav)', 'with or without palms — not indispensable; Rav: yes'); return out('not (the Tosefta: with or without palms); Rav: yes', ['accepted'])
    if ask == 'vow_on_vow':
        move('Nedarim 18a:3; Nazir 5a:19', 'nazir lehazzir — naziriteship on a prior naziriteship'); return out('takes effect (two terms)', ['nazirite_vow_bound'])
    if ask == 'chained_vows':
        move('Mishnah Nazir 4:1', '"and I", "and I" — all; the first dissolved, all; the last, he alone'); return out('all dissolved' if case.get('which_dissolved') == 'first' else 'the last alone', ['exempt'])
    if ask == 'spouse_and_i':
        move('Mishnah Nazir 4:1-2', 'his vow then hers — he nullifies hers; hers then his — he cannot (his own would fall)'); return out('he nullifies hers, his stands' if case.get('who_first') == 'husband' else 'he cannot nullify (his own would fall)', ['nazirite_vow_bound'])
    if ask == 'husband_annuls_after':
        stage = case['stage']
        move('Mishnah Nazir 4:5', 'after the blood of one offering — cannot (R. Akiva: after any slaughter); at the impurity shaving — can (a downcast wife); R. Meir even at purity')
        return out('cannot (R. Akiva: after any slaughter)' if stage == 'blood_sprinkled_purity' else 'can — a downcast wife', ['nazirite_vow_bound'] if stage == 'blood_sprinkled_purity' else ['exempt'])
    if ask == 'nullified_unknown':
        move('Mishnah Nazir 4:3', 'no lashes (R. Yehuda: lashes of rebellion)'); return out('no lashes (R. Yehuda: lashes of rebellion)', ['exempt'])
    if ask in ('nullified_after_separation', 'died_with_funds'):
        whose, allocated = case.get('whose', 'hers'), case.get('allocated')
        move('Mishnah Nazir 4:4; Mishnah Meilah 3:2; Meilah 11a:7', 'his animal grazes; hers: the sin dies, the burnt offered, the peace eaten a day without loaves; unallocated funds — gifts; allocated — the sin\'s to the Dead Sea, the burnt\'s an olah (misuse), the peace\'s a shelamim a day without loaves')
        if whose == 'his':
            return out('grazes', ['exempt'])
        if allocated is None:
            return out('the sin-offering dies, the burnt offered, the peace eaten a day without loaves', ['accepted'])
        return out('the sin\'s to the Dead Sea, the burnt\'s an olah (misuse), the peace\'s a shelamim a day without loaves' if allocated else 'communal gifts', ['accepted'])
    if ask == 'father_vows_son':
        move('Mishnah Nazir 4:6; Mishnah Sotah 3:8', 'a father may (not a mother); the son\'s or relatives\' objection cancels'); return out('a father may (not a mother); the son\'s or relatives\' objection cancels', ['nazirite_vow_bound'])
    if ask == 'shaves_on_fathers_funds':
        move('Mishnah Nazir 4:7', 'only a son who was a nazirite in his father\'s lifetime (R. Yosei: vowed after — gifts)'); return out('may (vowed in his father\'s lifetime)' if case.get('when_vowed') == 'in_lifetime' else 'communal gifts (R. Yosei)', ['accepted'])
    if ask == 'designated_by_others':
        ink('6:21', '"beside that for which his means suffice"'); move('Temurah 10a:5', 'designation by others effective'); return out('effective (6:21 his means)', ['accepted'])
    if ask == 'dissolved_by_sage':
        move('Mishnah Nazir 5:3', 'released — the animal grazes; not — counts from the vow'); return out('the animal grazes' if case.get('released') else 'counts from the vow', ['exempt'] if case.get('released') else ['nazirite_vow_bound'])
    if ask == 'vow_in_error':
        move('Mishnah Nazir 5:4', 'vowed then stolen — a nazirite; stolen then vowed — not (Nachum the Mede\'s error)'); return out('a nazirite (the event after the vow)' if case.get('event_before') is False else 'not — an error from the outset (Nachum the Mede)', ['nazirite_vow_bound'] if case.get('event_before') is False else ['exempt'])
    if ask == 'conditioned_on_birth':
        form, born = case['form'], case['born']
        move('Mishnah Nazir 2:7-8', '"a son" — a daughter or tumtum not; "a child" — any; a miscarriage not (R. Shimon\'s condition)')
        if born == 'miscarriage':
            return out('not (R. Shimon\'s condition)', ['exempt'])
        return out('a nazirite' if (form == 'child' or born == 'son') else 'not', ['nazirite_vow_bound'] if (form == 'child' or born == 'son') else ['exempt'])
    if ask == 'two_terms_order':
        move('Mishnah Nazir 2:9-10', 'his own first then the son\'s; reversed — the son\'s interrupts; a hundred days: born within seventy — nothing lost, after — the seventy negated'); return out('born within seventy days — nothing lost; after — the seventy negated' if case.get('born_on_day', 0) > 70 else 'born within seventy days — nothing lost', ['nazirite_vow_bound'])
    if ask == 'doubtful_vow':
        c = case.get('case', 'turned_back')
        move('Mishnah Nazir 5:6-7; Mishnah Tahorot 4:7, 4:12', 'the man turned back — none (lenient; R. Shimon\'s condition); the koy — all bound')
        return out('all bound (the koy)' if c == 'koy' else 'none (lenient; R. Shimon\'s condition)', ['nazirite_vow_bound'] if c == 'koy' else ['exempt'])
    if ask == 'two_doubtful':
        move('Mishnah Nazir 8:1', 'ben Zoma\'s procedure (the Rabbis agreed)'); return out('ben Zoma\'s procedure (the Rabbis)', ['accepted'])
    if ask == 'doubtful_leper':
        move('Mishnah Nazir 8:2; Nazir 60a:6', 'sixty days to sacred food, a hundred and twenty to wine and the dead'); return out('sixty days to sacred food, a hundred and twenty to wine and the dead', ['nazirite_vow_bound'])
    if ask == 'leper_nazirite_shaves':
        z = MZ.shave('nazirite')['v']                                                                              # THE CALL
        move('CALLED cold_run_metzora.shave(nazirite) -> %s [IMPORT, live]' % z, 'Lev 14:9 "his head" — the leper\'s positive command overrides 6:5\'s razor (Nazir 41a, 58a; Yevamot 5a)')
        return out('shaves with a razor — the leper\'s command overrides (metzora: %s)' % z, ['accepted'])
    if ask == 'oath_on_seed':
        move('Shevuot 22b:8 (Rav Ashi)', 'any amount or an olive\'s bulk — an open dilemma'); return out('an open dilemma (Rav Ashi)', [FX.NONE])
    if ask == 'sinner':
        ink('6:11', '"and atone for him for sinning by the soul"'); move('Bava Kamma 91b; Nazir 19a; Taanit 11a; Nedarim 10a', 'HaKappar: a sinner; R. Elazar: holy'); return out('a sinner (HaKappar) / holy (R. Elazar) — a dispute', ['accepted'])
    if ask == 'exemptions':
        move('Mishnah Nazir 6:5', 'the vine none; impurity and shaving: the met mitzvah, the leper\'s shaving'); return out('the vine none; impurity and shaving: the met mitzvah, the leper\'s shaving', ['accepted'])
    if ask == 'impure_after_first_blood':
        move('Mishnah Nazir 6:11', 'R. Eliezer negates all; the Rabbis: brings the rest (Miriam of Tarmod)'); return out('brings the rest and is pure (the Rabbis); R. Eliezer negates all', ['accepted'])
    if ask == 'shaved_on_invalid':
        move('Mishnah Nazir 6:10', 'the offering invalid — the shaving invalid; R. Shimon: that one alone fails; all three with one valid — the shaving valid'); return out('the shaving invalid (R. Shimon: that one alone fails); one of three valid — valid', ['disqualified'])
    if ask == 'vowed_abroad':
        move('Mishnah Nazir 3:6', 'Shammai thirty more; Hillel all again (Queen Helene)'); return out('Hillel: all again (Shammai: thirty)', ['nazirite_vow_bound'])
    return out('no verdict in span', [FX.NONE])
