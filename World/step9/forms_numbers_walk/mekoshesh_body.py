

# ===== F1: THE CAPITAL PROCEDURE — from the guard to the grave (Num 15:34-36; Lev 24:14, 24:23; Deut 17:7, 21:22-23) ======
def capital_procedure(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'custody':
        ink('Num 15:34', '"and they placed him in the guard, for it had not been declared what should be done to him" — the halt')
        if case.get('liable') is True:
            move('Sifrei Bamidbar 114:1', 'all who are liable to death (the shelf\'s bracketed emendation of its "karet") are CONFINED '
                 'pending judgment — the custody rule generalized from the case; Sanhedrin 78b:4: known from the outset to be '
                 'liable, the mode unknown')
            return out('confined until it be declared', ['in_custody'])
        move('Sanhedrin 78b:5-6', 'the liability itself unknown — Rabbi Nechemya derives the confinement from the blasphemer (Lev '
             '24:12); the sages: the blasphemer\'s was a provisional edict, not derived (the striker whose victim lingers, Mishnah '
             'Sanhedrin 9:1)')
        return out('confined until it be declared — Rabbi Nechemya (from the blasphemer); the sages: not derived, a provisional edict', ['in_custody'])
    if ask == 'warning':
        ink('Num 15:33', '"and they brought him near, those who found him gathering wood" — 15:32\'s "gathering" REPEATED (the '
                         'participle\'s whole Torah career, computed)')
        if not case.get('warned'):
            move('Mishnah Sanhedrin 5:1', '"did you warn him?" — the court\'s question to the witnesses; no warning, no death (Sifrei '
                 '113:1: the repetition teaches they WARNED him and he continued)')
            return out('not put to death — no forewarning', ['exempt'])
        if not case.get('labor_named'):
            move('Sifrei Bamidbar 113:1', 'R. Yitzchak: the warning itself follows a-fortiori from idolatry (the gravest, not liable '
                 'without it), so the repetition is FREED to teach that the warning SPECIFIES THE LABOR — for all the primary '
                 'labors of the Torah')
            return out('not put to death — the labor unspecified in the warning', ['exempt'])
        row = data['warning_names_the_death']['value']
        if not case.get('death_named'):
            if row == 'required':
                dat('warning_names_the_death = required — Rabbi Yehuda (Sanhedrin 80b:5, 8b:5): the defendant is not executed '
                    'unless the witnesses told him by which death he would die; the wood-gatherer a provisional edict')
                return out('not put to death — the death unnamed in the warning (Rabbi Yehuda)', ['exempt'])
            dat('warning_names_the_death = %s — the first tanna (Sanhedrin 80b:5): forewarning derived from the wood-gatherer, '
                'executed though Moses himself did not know the mode; the mode need not be named' % row)
            return out('put to death — the warning named the labor; the mode need not be named (the first tanna)', ['warned_specifying_the_labor', 'put_to_death'])
        move('Sanhedrin 80b:5', 'the warning named the labor and the death — liable on both settings of the row')
        return out('put to death — the warning named the labor and the death', ['warned_specifying_the_labor', 'put_to_death'])
    if ask == 'venue':
        ink('Num 15:35', '"stone him with stones, all the congregation, OUTSIDE THE CAMP" — the sentence')
        ink('Num 15:36', '"and all the congregation brought him outside the camp" — the execution')
        ink('Lev 24:14', '"bring out the curser outside the camp" — the blasphemer\'s (Mishnah Sanhedrin 6:1 quotes it; graded at '
                         'the blasphemer\'s runner, credited); computed: "outside the camp" at all four seats')
        move('Sifrei Bamidbar 114:1', '"and they brought him outside" — all liable to death are executed OUTSIDE THE COURT; the '
             'Mishnah: a little beyond it, the cloth-waver and the horseman, the return on a reason to acquit')
        return out('outside the court, a little beyond it', [FX.NONE])
    if ask == 'confession':
        ink('Joshua 7:19-25', '"my son, give glory to the LORD... and confess"; "I have sinned"; "the LORD shall trouble you THIS '
                              'DAY" — Achan\'s run [the Prophets demonstrate by RUN]')
        move('Mishnah Sanhedrin 6:2', 'ten cubits from the place: "confess" — the way of all who are executed; the confessor has a '
             'portion in the world to come; this day troubled, not the next')
        if case.get('can_confess', True):
            return out('a portion in the world to come — troubled this day, not the next (Achan)', ['confessed'])
        move('Mishnah Sanhedrin 6:2', 'one who cannot confess says "let my death be an atonement for all my sins"; Rabbi Yehuda\'s '
             'conspired-against adds "except this sin" — the sages: then everyone would')
        return out('let my death be an atonement for all my sins', ['confessed'])
    if ask == 'stripping':
        ink('Num 15:36', '"and they stoned HIM" — the pronoun the Talmud reads as him without his clothing (Sanhedrin 45a:3, on the '
                         'blasphemer\'s 24:23; graded at the blasphemer\'s runner as the recorded dispute, credited)')
        move('Mishnah Sanhedrin 6:3', 'four cubits from the place: stripped; a man covered in front — the sages: a man stoned naked, '
             'a woman not; Rabbi Yehuda: a woman covered front and back')
        if case.get('sex', 'man') == 'woman':
            return out('not stripped (the sages); covered front and back (Rabbi Yehuda)', [FX.NONE])
        return out('stripped, covered in front', [FX.NONE])
    if ask == 'stoning':
        ink('Num 15:35', '"stone him with stones, all the congregation" — in its PRESENCE (Sifrei 114:1), not by every hand')
        ink('Num 15:36', '"and they stoned him with stones, and he died"')
        ink('Deut 17:7', '"the hand of the witnesses shall be first upon him to put him to death, and afterward the hand of all the '
                         'people" [OWED FORWARD to Deuteronomy]')
        dat('stoning_house_height = %s — %s' % (data['stoning_house_height']['value'], data['stoning_house_height']['settings'][data['stoning_house_height']['value']]))
        move('Sifrei Bamidbar 114:1 = Mishnah Sanhedrin 6:4', 'the first witness pushes him at the loins; face up, turned back if on '
             'his chest; dead — enough; else the second witness sets THE STONE on his heart; dead — enough; else ALL ISRAEL stone '
             'him WITH STONES')
        d = case['died_at']
        if d == 'the_push':
            return out('dead by the first witness\'s push — enough', ['stoned'])
        if d == 'the_stone':
            return out('dead by the second witness\'s stone on the heart — enough', ['stoned'])
        return out('stoned by all the people with stones — the witnesses\' hand first', ['stoned'])
    if ask == 'stones_and_a_stone':
        ink('Num 15:35-36', '"with STONES" twice (בָּאֲבָנִים, "with stones")')
        ink('Lev 24:23', '"with A STONE" (אָבֶן, "a stone") — the singular; computed: no plural there')
        move('Sifrei Bamidbar 114:1', 'two verses reconciled — the stone the second witness sets, the stones of all Israel: "stone '
             'him with stones" fulfilled and "they stoned him with a stone" fulfilled (I13\'s shape; Deut 17:7 the third verse)')
        return out('both verses fulfilled: the second witness\'s stone, all Israel\'s stones', [FX.NONE])
    if ask == 'hanging':
        ink('Deut 21:22-23', '"if there be in a man a sin of a death sentence, and he be put to death, and you hang him on a tree... you '
                             'shall not leave his body overnight on the tree" [OWED FORWARD to Deuteronomy]')
        ink('Num 15:36', '"as the LORD commanded Moses" — the run line; the Sifrei reads the hanging into it (114:1: "hang him, and '
                         'they hanged him" — Rabbi Eliezer)')
        row = data['hanging_after_stoning']['value']
        t, sex = case.get('transgression'), case.get('sex', 'man')
        if row == 'all_the_stoned':
            dat('hanging_after_stoning = all_the_stoned — Rabbi Eliezer (Mishnah Sanhedrin 6:4): all who are stoned are hanged; a '
                'woman facing the tree')
            return out('hanged facing the tree (Rabbi Eliezer)' if sex == 'woman' else 'hanged after death (Rabbi Eliezer: all the stoned)', ['hanged'])
        dat('hanging_after_stoning = %s — the sages (Mishnah Sanhedrin 6:4): only the blasphemer and the idolater; a man hanged, a '
            'woman not; hanged and loosed at once' % row)
        if t in ('blasphemy', 'idolatry'):
            if sex == 'woman':
                return out('not hanged (a woman — the sages)', [FX.NONE])
            return out('hanged after death, loosed at once', ['hanged'])
        return out('not hanged (the sages: the blasphemer and the idolater alone)', [FX.NONE])
    if ask == 'burial':
        ink('Deut 21:23', '"you shall surely bury him that day" [OWED FORWARD to Deuteronomy]')
        move('Mishnah Sanhedrin 6:5', 'the same-day burial a command and leaving overnight a prohibition, except for the dead\'s '
             'honor; NOT in his ancestral plot — TWO GRAVEYARDS of the court: one for the decapitated and strangled, one for the '
             'stoned and burned')
        dat('the two graveyards — the court\'s own arrangement, no verse: a datum')
        if case.get('after'):
            move('Mishnah Sanhedrin 6:6', 'the flesh decomposed, the bones gathered to the ancestral plot; the relatives greet the '
                 'judges and witnesses; NO MOURNING RITES (the unmourned death atones), grief in the heart')
            return out('the bones gathered to the ancestral plot; no mourning, grief in the heart', [FX.NONE])
        return out('buried the same day in the court\'s graveyard for the stoned and the burned', ['buried'])
    if ask == 'mode':
        move('Mishnah Sanhedrin 7:1', 'four deaths handed to the court — stoning, burning, killing, strangling in descending '
             'severity; Rabbi Shimon: burning, stoning, strangling, killing; "this is the mitzvah of the stoned" closes chapter 6')
        return out('stoning — the severest of the four (the sages; Rabbi Shimon: burning)', [FX.NONE])
    raise ValueError(ask)


# ===== F2: THE GATHERER — the case as one pipeline (Num 15:32-36), the Sabbath engine CALLED ============================
def the_gatherer(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'labor':
        ink('Num 15:32', '"gathering wood" (מְקֹשֵׁשׁ עֵצִים, "gathering sticks") — no labor of the thirty-nine named')
        row = data['gatherers_labor']['value']
        dat('gatherers_labor = %s — %s' % (row, data['gatherers_labor']['settings'][row]))
        move('Shabbat 96b:18', 'every arm is capital — "with regard to that labor there is no uncertainty": the hidden scroll\'s one '
             'non-capital labor is not the gatherer\'s on any arm (Mishnah Sanhedrin 7:8\'s criterion: deliberate karet, '
             'unwitting a sin offering)')
        verdict = {'detaching': 'detaching (the baraita; the Sifrei\'s own word) — capital',
                   'carrying': 'carrying four cubits in the public domain (Rav Yehuda in Shmuel\'s name) — capital',
                   'gathering': 'gathering sticks into a pile (Rav Acha son of Rabbi Yaakov; Onkelos) — capital'}[row]
        return out(verdict, [FX.NONE])
    if ask == 'identity':
        ink('Num 15:32', '"a MAN" — unnamed in the ink')
        move('Sifrei Bamidbar 113:1 = Shabbat 96b:19-20', 'ZELOPHEHAD — R. Akiva, the verbal analogy "wilderness" here and at 27:3; '
             'R. Yehuda b. Beteira: "the Torah concealed him and you reveal him; you libel that righteous man" — one of the BOLD '
             'ONES (14:44); the two arms recorded, UNASSIGNED (the entity registry\'s note; sitting 4 reads 27:3 against it)')
        return out('unassigned: Zelophehad (R. Akiva, the verbal analogy on "wilderness") against one of the bold ones (R. Yehuda b. Beteira)', [FX.NONE])
    if ask == 'liability':
        ink('Exod 31:14', '"its profaners shall surely be put to death... that soul shall be cut off" — the standing liability '
                          '(Sanhedrin 78b:7: Moses knew from this verse that the gatherer was liable to death)')
        c = IS.sabbath('two_sanctions')
        move('CALLED IS.sabbath(two_sanctions) -> %s' % c['fx'], c['why'][:200])
        if case.get('witnessed', True):
            return out('put to death — its profaners shall surely die (with witnesses)', ['put_to_death'])
        return out('cut off — karet (without witnesses)', ['karet_cut_off'])
    if ask == 'mode':
        ink('Num 15:35', '"die shall die the man; stone him with stones" — the generations\' rule is THE MODE (Sifrei 114:1: "die '
                         'shall die" for the generations, "stone him" for the hour)')
        c = IS.sabbath('death_run')
        move('CALLED IS.sabbath(death_run) -> %s' % c['fx'], c['why'][:220])
        return out('stoning — the mode supplied at the run (the Sabbath engine\'s cell death_run, its import given its home)', ['stoned'])
    if ask == 'uncertainty':
        ink('Num 15:34', '"for it had not been declared what should be done to him" — yet Exod 31:14 already sentences the profaner')
        move('Sanhedrin 78b:7 = Sifrei Bamidbar 114:1', 'Moses knew he was liable to death; he did not know by WHICH death — the '
             'gatherer\'s uncertainty is the MODE, the blasphemer\'s whether he was liable at all')
        return out('the mode, not the liability', ['in_custody'])
    if ask == 'the_case':
        lab, _, _ = the_gatherer({'ask': 'labor'}, data)
        warn, e1, _ = capital_procedure({'ask': 'warning', 'warned': True, 'labor_named': True, 'death_named': False}, data)
        liab, e2, _ = the_gatherer({'ask': 'liability', 'witnessed': True}, data)
        cust, e3, _ = capital_procedure({'ask': 'custody', 'liable': True}, data)
        mode, e4, _ = the_gatherer({'ask': 'mode'}, data)
        ston, e5, _ = capital_procedure({'ask': 'stoning', 'died_at': 'all_israel'}, data)
        hang, e6, _ = capital_procedure({'ask': 'hanging', 'transgression': 'sabbath'}, data)
        del P[:]
        ink('Num 15:32-36', 'found gathering (15:32); warned by the finders, the labor named (15:33); in the guard, the mode undeclared '
                            '(15:34); the sentence — stoning, all the congregation, outside the camp (15:35); stoned with stones and '
                            'he died, as commanded (15:36)')
        move('the pipeline', ' | '.join([lab, warn, liab, cust, mode, ston, hang]))
        return out('found gathering, warned of the labor, confined until declared, stoned with stones outside the camp, and he died; not hanged (the sages)',
                   ['warned_specifying_the_labor', 'put_to_death', 'in_custody', 'stoned'])
    raise ValueError(ask)


# ===== THE DAEMON — the wrap (motion 6): a thin daemon over the compiled cells ==========================================
def law_mekoshesh(event, world):
    """Num 15:32-36 (cold_run_mekoshesh.py F1-F2). CASE-BORN, the third: installed by the tent's output (sentence_declared at
    15:35). The liability and the mode are law_sabbath's writes on the same act; this daemon writes the procedure's own."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'gathered_wood_on_the_sabbath':
        # THE ACT (15:32-33): the finders' warning read off the repetition — a status on the person; law_sabbath writes the rest
        if event.get('warned', True) and event.get('labor_named', True):
            return [E_('warned_specifying_the_labor', event['profaner'], value=event.get('labor'), law='F1 [INK 15:33 "those who found him gathering wood" — the repetition; Sifrei Bamidbar 113:1: they warned him, of the kind of his labor]')]
        return []
    if k == 'forewarned_before_the_act':
        p = event['person']
        v, e, _ = capital_procedure({'ask': 'warning', 'warned': event.get('warned'), 'labor_named': event.get('labor_named'), 'death_named': event.get('death_named')}, DATA)
        if 'put_to_death' in e:
            return [E_('warned_specifying_the_labor', p, value=event.get('transgression'), law='F1 [%s]' % v),
                    E_('put_to_death', p, value='forewarned', law='F1 [INK 15:33; Mishnah Sanhedrin 5:1; the row warning_names_the_death — %s]' % v)]
        return [E_('exempt', p, value='the_warning_wanting', law='F1 [%s]' % v)]
    if k == 'stoning_carried_out':
        p = event['person']; out_ = []
        if event.get('confessed'):
            v, e, _ = capital_procedure({'ask': 'confession'}, DATA)
            out_.append(E_('confessed', p, value='before_the_stoning', law='F1 [Mishnah Sanhedrin 6:2; Joshua 7:19-25 — %s]' % v))
        v, e, _ = capital_procedure({'ask': 'stoning', 'died_at': event['died_at']}, DATA)
        out_.append(E_('stoned', p, value=event['died_at'], law='F1 [INK 15:35-36; Deut 17:7; Sifrei 114:1 = Mishnah Sanhedrin 6:4 — %s]' % v))
        v, e, _ = capital_procedure({'ask': 'hanging', 'transgression': event.get('transgression'), 'sex': event.get('sex', 'man')}, DATA)
        if e == ['hanged']:
            out_.append(E_('hanged', p, value='after_death', law='F1 [Deut 21:22; Mishnah Sanhedrin 6:4 — %s]' % v))
        v, e, _ = capital_procedure({'ask': 'burial'}, DATA)
        out_.append(E_('buried', p, value='the_courts_graveyard', law='F1 [Deut 21:23; Mishnah Sanhedrin 6:5 — %s]' % v))
        return out_
    if k == 'stoned_as_commanded':
        # THE EXECUTION, second seat (15:36): the tent daemon closes the body entries; this daemon writes the hanging under the
        # row's Rabbi Eliezer arm alone — the running setting (the sages) leaves the Sabbath profaner unhanged: the negative branch's silence
        v, e, _ = capital_procedure({'ask': 'hanging', 'transgression': event.get('transgression', 'sabbath'), 'sex': event.get('sex', 'man')}, DATA)
        if e == ['hanged']:
            return [E_('hanged', event.get('person', event['subject']), value='after_death', law='F1 [Deut 21:22; Sifrei Bamidbar 114:1 (Rabbi Eliezer\'s arm) — %s]' % v)]
        return []
    return []


def scene():
    """THE SCENE — the recorded rows replayed on the world engine (the exam bench: law_mekoshesh alone)."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 15:32-36: Mishnah Sanhedrin 5:1, 6:1-6, 7:1-8 on the engine — the warning and the protocol (clock unit: days)')
        w.laws = [law_mekoshesh]
        w.advance(1)
        for p, wd, ln, dn in (('the-unwarned', False, False, False), ('the-warned-unnamed', True, False, False), ('the-warned-named', True, True, False), ('the-fully-warned', True, True, True)):
            w.submit({'kind': 'forewarned_before_the_act', 'subject': p, 'person': p, 'transgression': 'sabbath', 'warned': wd, 'labor_named': ln, 'death_named': dn, 'case_source': 'Mishnah Sanhedrin 5:1; Sifrei Bamidbar 113:1; Sanhedrin 80b:5 — the warning rows'})
        for p, t, d, c, s in (('the-pushed', 'sabbath', 'the_push', True, 'man'), ('the-stoned', 'sabbath', 'the_stone', False, 'man'), ('the-all-israel', 'sabbath', 'all_israel', False, 'man'),
                              ('the-blasphemer-row', 'blasphemy', 'the_stone', True, 'man'), ('the-woman-blasphemer', 'blasphemy', 'the_stone', False, 'woman')):
            w.submit({'kind': 'stoning_carried_out', 'subject': p, 'person': p, 'transgression': t, 'died_at': d, 'confessed': c, 'sex': s, 'case_source': 'Mishnah Sanhedrin 6:2-6 — the protocol rows; Deut 17:7'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    hanged_total = sum(1 for l in w.log if l[0] == 'WRITE' and 'hanged' in str(l))
    return (n('the-unwarned', 'exempt'), n('the-warned-unnamed', 'exempt'), n('the-warned-named', 'put_to_death'), n('the-warned-named', 'warned_specifying_the_labor'),
            n('the-fully-warned', 'put_to_death'), n('the-pushed', 'confessed'), n('the-pushed', 'stoned'), n('the-pushed', 'buried'), n('the-stoned', 'stoned'),
            n('the-all-israel', 'stoned'), n('the-blasphemer-row', 'hanged'), n('the-woman-blasphemer', 'hanged'), hanged_total), w
SCENE, _W = scene()


def narrative():
    """THE TENT sitting 3 (2026-09-09; THE_TENT.md section 3): the chapter's own case AS HISTORY — Num 15:32-36's four lines in the
    text's order on a world with the library's tent daemon registered first, the Exodus engine's law_sabbath second (the liability
    and the mode), this runner's daemon third; recorded by the sequential run's recorder and stitched onto the tape. Not a graded
    cell: the tuple below is a tripwire typed from THE_TENT.md's design; the sequence world's RUN tuple grades the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 15:32-36: the wood-gatherer on the tape — the act, the halt, the sentence, the execution (clock unit: days)')
        w.laws = [WE.law_tent, IS.law_sabbath, law_mekoshesh]
        w.advance(1)
        g = 'the-wood-gatherer'
        w.submit({'kind': 'gathered_wood_on_the_sabbath', 'subject': g, 'profaner': g, 'witnessed': True, 'labor': DATA['gatherers_labor']['value'], 'warned': True, 'labor_named': True, 'case_source': 'Num 15:32-33 — and they found a man gathering wood on the Sabbath day; and they brought him near, those who found him gathering wood, to Moses and to Aaron and to all the congregation'})
        w.submit({'kind': 'placed_in_custody', 'subject': g, 'person': g, 'case_of': 'Num 15:32', 'uncertainty': 'the_mode', 'case_source': 'Num 15:34 — and they placed him in the guard, for it had not been declared what should be done to him (Sanhedrin 78b:7: the mode; Onkelos: bound him in the guardhouse)'})
        w.submit({'kind': 'sentence_declared', 'subject': g, 'person': g, 'sentence': 'stoning', 'outside_the_camp': True, 'hands_laid': False, 'installs': 'law_sabbath:death_run', 'case_source': 'Num 15:35 — and the LORD said to Moses: die shall die the man; stone him with stones, all the congregation, outside the camp (Sifrei 114:1: for the generations / for the hour)'})
        w.submit({'kind': 'stoned_as_commanded', 'subject': g, 'person': g, 'transgression': 'sabbath', 'case_source': 'Num 15:36 — and all the congregation brought him outside the camp and stoned him with stones, and he died, as the LORD commanded Moses'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    is_open = lambda eid, eff: [e.get('open') for e in w.entity(eid).ledger if e['effect'] == eff]
    owed = [e for e in w.entity('the-court').ledger if e['effect'] == 'declaration_owed']
    rule = [e for e in w.entity('the-tabernacle').ledger if e['effect'] == 'rule_installed']
    g = 'the-wood-gatherer'
    return (n(g, 'labor_barred'), n(g, 'put_to_death'), n(g, 'stoned'), is_open(g, 'stoned'), n(g, 'warned_specifying_the_labor'), n(g, 'in_custody'), is_open(g, 'in_custody'),
            len(owed), owed[0].get('open') if owed else None, (owed[0].get('covered_by') or None) if owed else None,
            len(rule), rule[0].get('value') if rule else None, n(g, 'hanged')), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (1, 1, 1, [False], 1, 1, [False], 1, False, ['law_mekoshesh', 'law_sabbath'], 1, 'law_sabbath:death_run', 0)   # THE_TENT.md section 3: law_sabbath decides at the act (the liability and the mode), the warning on the person; the guard and the docket, covered by both daemons; the sentence installs the cell, no second stoned; the execution closes both body entries; no hanging on the sages' arm
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE TENT: the wood-gatherer narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the Mishnah's rows (num_15_mekoshesh_exam_2026-09-09.md) and the Talmud's per gap.
# =====================================================================
D_YEHUDA = dict(DATA, warning_names_the_death=dict(DATA['warning_names_the_death'], value='required'))
D_ELIEZER = dict(DATA, hanging_after_stoning=dict(DATA['hanging_after_stoning'], value='all_the_stoned'))
D_CARRY = dict(DATA, gatherers_labor=dict(DATA['gatherers_labor'], value='carrying'))
D_GATHER = dict(DATA, gatherers_labor=dict(DATA['gatherers_labor'], value='gathering'))
CASES = [
    # F1 — the custody
    ('Sifrei Bamidbar 114:1 / Sanhedrin 78b:4 — liable to death, the mode unknown: confined',
     lambda: capital_procedure({'ask': 'custody', 'liable': True}, DATA), 'confined until it be declared'),
    ('Sanhedrin 78b:5-6 — the liability itself unknown (the blasphemer\'s shape; the striker)',
     lambda: capital_procedure({'ask': 'custody', 'liable': None}, DATA), 'confined until it be declared — Rabbi Nechemya (from the blasphemer); the sages: not derived, a provisional edict'),
    # F1 — the warning
    ('Mishnah Sanhedrin 5:1 — "did you warn him?": no warning',
     lambda: capital_procedure({'ask': 'warning', 'warned': False}, DATA), 'not put to death — no forewarning'),
    ('Sifrei Bamidbar 113:1 — warned, the labor unspecified',
     lambda: capital_procedure({'ask': 'warning', 'warned': True, 'labor_named': False}, DATA), 'not put to death — the labor unspecified in the warning'),
    ('Sanhedrin 80b:5 — the first tanna: the labor named, the death unnamed (the running setting)',
     lambda: capital_procedure({'ask': 'warning', 'warned': True, 'labor_named': True, 'death_named': False}, DATA), 'put to death — the warning named the labor; the mode need not be named (the first tanna)'),
    ('Sanhedrin 80b:5, 8b:5 — Rabbi Yehuda: the death unnamed (the row\'s other setting)',
     lambda: capital_procedure({'ask': 'warning', 'warned': True, 'labor_named': True, 'death_named': False}, D_YEHUDA), 'not put to death — the death unnamed in the warning (Rabbi Yehuda)'),
    ('Sanhedrin 80b:5 — the labor and the death both named',
     lambda: capital_procedure({'ask': 'warning', 'warned': True, 'labor_named': True, 'death_named': True}, DATA), 'put to death — the warning named the labor and the death'),
    # F1 — the protocol
    ('Mishnah Sanhedrin 6:1 (credited) — the venue',
     lambda: capital_procedure({'ask': 'venue'}, DATA), 'outside the court, a little beyond it'),
    ('Mishnah Sanhedrin 6:2 — the confession (Achan)',
     lambda: capital_procedure({'ask': 'confession'}, DATA), 'a portion in the world to come — troubled this day, not the next (Achan)'),
    ('Mishnah Sanhedrin 6:2 — one who cannot confess',
     lambda: capital_procedure({'ask': 'confession', 'can_confess': False}, DATA), 'let my death be an atonement for all my sins'),
    ('Mishnah Sanhedrin 6:3 (credited) — stripping: a man',
     lambda: capital_procedure({'ask': 'stripping', 'sex': 'man'}, DATA), 'stripped, covered in front'),
    ('Mishnah Sanhedrin 6:3 — stripping: a woman (the sages; Rabbi Yehuda recorded)',
     lambda: capital_procedure({'ask': 'stripping', 'sex': 'woman'}, DATA), 'not stripped (the sages); covered front and back (Rabbi Yehuda)'),
    ('Mishnah Sanhedrin 6:4 — dead by the push',
     lambda: capital_procedure({'ask': 'stoning', 'died_at': 'the_push'}, DATA), 'dead by the first witness\'s push — enough'),
    ('Mishnah Sanhedrin 6:4 — dead by the stone on the heart',
     lambda: capital_procedure({'ask': 'stoning', 'died_at': 'the_stone'}, DATA), 'dead by the second witness\'s stone on the heart — enough'),
    ('Mishnah Sanhedrin 6:4 / Deut 17:7 — all the people',
     lambda: capital_procedure({'ask': 'stoning', 'died_at': 'all_israel'}, DATA), 'stoned by all the people with stones — the witnesses\' hand first'),
    ('Sifrei Bamidbar 114:1 — "with stones" and "with a stone" reconciled',
     lambda: capital_procedure({'ask': 'stones_and_a_stone'}, DATA), 'both verses fulfilled: the second witness\'s stone, all Israel\'s stones'),
    ('Mishnah Sanhedrin 6:4 — the hanging: the Sabbath profaner (the sages, the running setting)',
     lambda: capital_procedure({'ask': 'hanging', 'transgression': 'sabbath'}, DATA), 'not hanged (the sages: the blasphemer and the idolater alone)'),
    ('Mishnah Sanhedrin 6:4 — the hanging: the blasphemer',
     lambda: capital_procedure({'ask': 'hanging', 'transgression': 'blasphemy'}, DATA), 'hanged after death, loosed at once'),
    ('Mishnah Sanhedrin 6:4 — the hanging: a woman blasphemer (the sages)',
     lambda: capital_procedure({'ask': 'hanging', 'transgression': 'blasphemy', 'sex': 'woman'}, DATA), 'not hanged (a woman — the sages)'),
    ('Mishnah Sanhedrin 6:4 / Sifrei 114:1 — Rabbi Eliezer: all the stoned (the row\'s other setting)',
     lambda: capital_procedure({'ask': 'hanging', 'transgression': 'sabbath'}, D_ELIEZER), 'hanged after death (Rabbi Eliezer: all the stoned)'),
    ('Mishnah Sanhedrin 6:5 — the burial',
     lambda: capital_procedure({'ask': 'burial'}, DATA), 'buried the same day in the court\'s graveyard for the stoned and the burned'),
    ('Mishnah Sanhedrin 6:6 — after: the bones, no mourning',
     lambda: capital_procedure({'ask': 'burial', 'after': True}, DATA), 'the bones gathered to the ancestral plot; no mourning, grief in the heart'),
    ('Mishnah Sanhedrin 7:1 (credited) — the mode among the four',
     lambda: capital_procedure({'ask': 'mode'}, DATA), 'stoning — the severest of the four (the sages; Rabbi Shimon: burning)'),
    # F2 — the gatherer
    ('Shabbat 96b:15 — the labor: detaching (the running setting; the Sifrei\'s word)',
     lambda: the_gatherer({'ask': 'labor'}, DATA), 'detaching (the baraita; the Sifrei\'s own word) — capital'),
    ('Shabbat 96b:15 — carrying four cubits (Rav Yehuda in Shmuel\'s name)',
     lambda: the_gatherer({'ask': 'labor'}, D_CARRY), 'carrying four cubits in the public domain (Rav Yehuda in Shmuel\'s name) — capital'),
    ('Shabbat 96b:15 — gathering into a pile (Rav Acha; Onkelos)',
     lambda: the_gatherer({'ask': 'labor'}, D_GATHER), 'gathering sticks into a pile (Rav Acha son of Rabbi Yaakov; Onkelos) — capital'),
    ('Sifrei Bamidbar 113:1 / Shabbat 96b:19-20 — who he was',
     lambda: the_gatherer({'ask': 'identity'}, DATA), 'unassigned: Zelophehad (R. Akiva, the verbal analogy on "wilderness") against one of the bold ones (R. Yehuda b. Beteira)'),
    ('Exod 31:14 (the Sabbath engine called) — the liability with witnesses',
     lambda: the_gatherer({'ask': 'liability', 'witnessed': True}, DATA), 'put to death — its profaners shall surely die (with witnesses)'),
    ('Onkelos Exod 31:14 (called) — without witnesses',
     lambda: the_gatherer({'ask': 'liability', 'witnessed': False}, DATA), 'cut off — karet (without witnesses)'),
    ('Num 15:35 (the Sabbath engine\'s death_run called) — the mode',
     lambda: the_gatherer({'ask': 'mode'}, DATA), 'stoning — the mode supplied at the run (the Sabbath engine\'s cell death_run, its import given its home)'),
    ('Sanhedrin 78b:7 — the halt\'s uncertainty',
     lambda: the_gatherer({'ask': 'uncertainty'}, DATA), 'the mode, not the liability'),
    ('Num 15:32-36 — the chapter\'s own case as one pipeline',
     lambda: the_gatherer({'ask': 'the_case'}, DATA), 'found gathering, warned of the labor, confined until declared, stoned with stones outside the camp, and he died; not hanged (the sages)'),
    # THE WRAP: the scene on the world engine
    ('THE SCENE on the world engine — the wrap: four warning rows (two exempt, two put to death — the warned-named row carrying the warning status), five protocol rows (the pushed confessed, stoned and buried; the stoned and all-Israel rows; the blasphemer hanged; the woman not) — the tuple typed from the design',
     lambda: (SCENE, [FX.NONE], [('INK', 'Num 15:33-36 — the recorded rows replayed: Mishnah Sanhedrin 5:1, 6:2-6; Sanhedrin 80b:5')]),
     (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1)),
    ('THE NARRATIVE on the world engine — the tape\'s four lines with the tent daemon first and the Sabbath engine second (the tripwire typed from THE_TENT.md section 3)',
     lambda: (NARRATIVE, [FX.NONE], [('INK', 'Num 15:32-36 — the act, the halt, the sentence, the execution')]),
     (1, 1, 1, [False], 1, 1, [False], 1, False, ['law_mekoshesh', 'law_sabbath'], 1, 'law_sabbath:death_run', 0)),
]

if __name__ == '__main__':
    ok = 0
    frac = {'INK': 0, 'MOVE': 0, 'DATA': 0}
    used_effects = []
    print()
    for label, fn, want in CASES:
        got, effects, prov = fn()
        hit = got == want
        ok += hit
        kinds = [k for k, _ in prov]
        cls = 'INK' if all(k == 'INK' for k in kinds) else ('MOVE' if 'MOVE' in kinds else 'DATA')
        frac[cls] += 1
        print('%s  [%s]  %s' % ('PASS' if hit else 'MISS', cls, label))
        if not hit:
            print('      expected: %s' % (want,))
            print('      got     : %s' % (got,))
        used_effects += effects
        for line in FX.render(effects):
            print('        ->%s' % line)
    print()
    print('WATCH COVERAGE (the wrap):')
    _W.print_coverage()
    print('MATRIX: %d/%d cells match the answer sheet' % (ok, len(CASES)))
    tot = len(CASES)
    print('FRACTIONS: pure ink %d/%d (%.0f%%) · named moves %d/%d (%.0f%%) · data %d/%d (%.0f%%)' %
          (frac['INK'], tot, 100.0 * frac['INK'] / tot, frac['MOVE'], tot, 100.0 * frac['MOVE'] / tot, frac['DATA'], tot, 100.0 * frac['DATA'] / tot))
    ops = FX.summarize(used_effects)
    print('LEDGER OPS this span writes:', ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
    print('THE PARAMETER ROWS: gatherers_labor = %s; warning_names_the_death = %s; hanging_after_stoning = %s; stoning_house_height = %s (the other settings recorded in DATA)' %
          tuple(DATA[r]['value'] for r in ('gatherers_labor', 'warning_names_the_death', 'hanging_after_stoning', 'stoning_house_height')))
    print('THE FORK PRINTED: under hanging_after_stoning = all_the_stoned (Rabbi Eliezer) the tape\'s execution at Num 15:36 would write hanged on the gatherer; the running setting (the sages) writes nothing — the Sifrei\'s own arm recorded, not run.')
    print('THE RULE INSIDE A LAW: the sentence at 15:35 installs law_sabbath:death_run — a CELL of the Exodus engine, not a daemon; its in-force gate is the second pass\'s (D2).')
    if ok == len(CASES):
        print('\nTHE WOOD-GATHERER COMPILES — the second Numbers span, the third case-born law: the mode already held by the Exodus engine given its home; the procedure from the guard to the grave compiled.')
