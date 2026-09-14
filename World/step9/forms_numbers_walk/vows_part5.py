

# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
REQUIRED = {'man': set(), 'mature': set(), 'widow': set(), 'daughter': {'father'}, 'betrothed': {'father', 'husband'}, 'married': {'husband'}}   # the authority table (F2-F5): who annuls whom
def law_vows(event, world):
    """Num 30:1-17 (cold_run_vows.py F1-F7). installed_by boot — THE FORM FOR A LAW IN MOSES' VOICE (the class named in the registry):
    the ONE tape line writes the statutes commanded; THE STATE MACHINE on three case kinds — vow_uttered -> the DEBIT vow_bound toward
    HEAVEN; vow_heard -> the TIMER vow_confirmed due the hearing day + 1 (the calendar row's setting) or at once on the confirming words;
    vow_restrained on the day by the RIGHT authority -> the timer cancelled, the debit closed, HEAVEN forgives (vow_annulled); after the
    fire -> the vow stands and the annulling husband bears her iniquity; the wrong authority, the partial annulment (R. Yishmael's arm),
    the steward (R. Yoshiyah's arm) and the unheard vow write NOTHING — the vow stands."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'vows_law_spoken':
        return [E_('commanded', 'israel', value='the statutes of vows — Num 30:2-17', law='F7 [INK 30:2 "this is the thing which the LORD commanded" ... 30:17 "these are the statutes which the LORD commanded Moses, between a man and his wife, between a father and his daughter" — Moses\' one speech to the heads of the tribes (%s), no divine frame; no timer, no close]' % event.get('to'))]
    if k == 'vow_uttered':
        vower, vow = event['vower'], event['vow']
        if event.get('age') is not None:
            v, e, _ = the_man({'ask': 'age', 'age': event['age'], 'sex': event.get('sex', 'girl'), 'knows_to_whom': event.get('knows_to_whom', True)}, DATA)
            if e == ['exempt']:
                return [E_('exempt', vower, value=v, law='F1 [%s]' % v)]
        if event.get('void'):
            return [E_('exempt', vower, value='a vow against an owed duty — void (Mishnah Nedarim 11:4)', law='F6 [INK 30:14 the vows he annuls — the owed work is not hers to forbid]')]
        return [E_('vow_bound', vower, cp='HEAVEN', value=vow, law='F1 [INK 30:3 "he shall not profane his word; according to all that proceeds out of his mouth he shall do" — the %s\'s %s (%s): the debit toward Heaven]' % (event.get('status', 'man'), event.get('vow_kind', 'vow'), event.get('content_class', 'other')))]
    if k == 'vow_heard':
        vower, vow = event['vower'], event['vow']
        if event.get('deaf'):
            return [E_('exempt', vower, value='the deaf cannot annul — the vow stands unheard', law='F2 [INK 30:5 "and her father hears" — the deaf excluded (Sifrei 153:5; Nedarim 73a:4)]')]
        if not event.get('intends_her', True):
            return []                                                          # "I thought it was my wife's" — no hearing of THIS vow: no clock (Sifrei 153:5; Mishnah Nedarim 11:5)
        if event.get('confirm_words'):
            return [E_('vow_confirmed', vower, value=vow, law='F5 [Nedarim 77b:5 "you did well" — confirmed by his words at once]')]
        return [E_('vow_confirmed', vower, value=vow, due=hearing_due(world), law='F6 [INK 30:5, 30:8 "and is silent to her, then all her vows shall stand" — THE TIMER: the hearing day + 1 (the calendar row vow_annulment_window = %s); the report counts (30:6 "on the day of his hearing")]' % WINDOW)]
    if k == 'vow_restrained':
        vower, vow, by = event['vower'], event['vow'], set(event.get('by', []))
        note = '%s — restrained by %s' % (src.split(' — ')[0], '+'.join(sorted(by)))
        ledger = world.entity(vower).ledger
        confirmed = any(e['effect'] == 'vow_confirmed' and e.get('value') == vow for e in ledger)
        pending = any(eff['effect'] == 'vow_confirmed' and eff.get('value') == vow and world._registry.get(eff['subject'], eff['subject']) == world._registry.get(vower, vower) for _, eff in world.timers)
        if confirmed:
            if 'husband' in by:
                return [E_('iniquity_borne', event.get('husband', vower + '-husband'), cp='HEAVEN', value=vow, law='F6 [INK 30:16 "and if he annul them after his hearing, then he shall bear her iniquity" — after the confirmation: the vow stands, the iniquity his (Sifrei 156:2)]')]
            return []                                                          # the father after the day: the ink names the husband alone — the vow stands, nothing written
        if not pending:
            return []                                                          # never heard: no clock to close — annulment without hearing UNRESOLVED (Nedarim 73a:1), the vow stands
        required = REQUIRED[event.get('status', 'man')]
        if not required or by != required:
            return []                                                          # the wrong authority (the father over the married; one of the two over the betrothed; any over the widow): the vow stands
        if event.get('status') == 'married' and event.get('content_class', 'other') not in ('affliction', 'between'):
            return []                                                          # THE FILTER (30:14 + 30:17): neither affliction nor between them — the vow stands
        if event.get('partial'):
            return []                                                          # R. Yishmael's arm (the Mishnah's): annulled for a part is not annulled until the whole
        if event.get('via_messenger'):
            return []                                                          # R. Yoshiyah's arm: the steward annuls nothing (the DATA row annul_by_messenger)
        world.cancel_timers(vower, 'vow_confirmed', note)
        world.close(vower, 'vow_bound', note, value=vow)
        return [E_('vow_annulled', vower, cp='HEAVEN', value=vow, law='F2 [INK 30:6 "and if her father restrain her on the day of his hearing ... and the LORD will forgive her" — the timer cancelled, the debit closed, Heaven forgives (30:9 restraint = annulment)]')]
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form) ----
    if k == 'mans_vow_case':
        v, e, _ = the_man(dict(event, ask=event['ask']), DATA); L = 'F1 [%s]' % v; s_ = event['person']
        W = {'vow_bound': E_('vow_bound', s_, cp='HEAVEN', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'commanded': E_('commanded', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'daughters_vow_case':
        v, e, _ = the_daughter(dict(event, ask=event['ask']), DATA); L = 'F2 [%s]' % v; s_ = event['person']
        W = {'vow_bound': E_('vow_bound', s_, cp='HEAVEN', value=v, law=L), 'vow_confirmed': E_('vow_confirmed', s_, value=v, law=L), 'vow_annulled': E_('vow_annulled', s_, cp='HEAVEN', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'betrothed_vow_case':
        v, e, _ = the_betrothed(dict(event, ask=event['ask']), DATA); L = 'F3 [%s]' % v; s_ = event['person']
        W = {'vow_bound': E_('vow_bound', s_, cp='HEAVEN', value=v, law=L), 'vow_confirmed': E_('vow_confirmed', s_, value=v, law=L), 'vow_annulled': E_('vow_annulled', s_, cp='HEAVEN', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'widows_vow_case':
        v, e, _ = the_widow(dict(event, ask=event['ask']), DATA); L = 'F4 [%s]' % v; s_ = event['person']
        W = {'vow_bound': E_('vow_bound', s_, cp='HEAVEN', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'wifes_vow_case':
        v, e, _ = the_wife(dict(event, ask=event['ask']), DATA); L = 'F5 [%s]' % v; s_ = event['person']
        W = {'vow_bound': E_('vow_bound', s_, cp='HEAVEN', value=v, law=L), 'vow_confirmed': E_('vow_confirmed', s_, value=v, law=L), 'vow_annulled': E_('vow_annulled', s_, cp='HEAVEN', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'affliction_oath_case':
        v, e, _ = the_affliction_oath(dict(event, ask=event['ask']), DATA); L = 'F6 [%s]' % v; s_ = event['person']
        W = {'vow_bound': E_('vow_bound', s_, cp='HEAVEN', value=v, law=L), 'vow_confirmed': E_('vow_confirmed', s_, value=v, law=L), 'vow_annulled': E_('vow_annulled', s_, cp='HEAVEN', value=v, law=L), 'iniquity_borne': E_('iniquity_borne', s_, cp='HEAVEN', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'statutes_case':
        v, e, _ = the_statutes(dict(event, ask=event['ask']), DATA); L = 'F7 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'commanded': E_('commanded', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINE = 'Num 30:2-17 — and Moses spoke to the heads of the tribes of the children of Israel, saying: this is the thing which the LORD commanded: a man, when he vows a vow to the LORD, or swears an oath to bind a bond on his soul, he shall not profane his word ... these are the statutes which the LORD commanded Moses, between a man and his wife, between a father and his daughter, in her youth in her father\'s house'
CLOSE = 'none — the statutes commanded; the vows themselves are the bench\'s (no vow is uttered on the tape in this chapter)'


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): THE STATE MACHINE's persons through vow_uttered /
    vow_heard / vow_restrained with the clock advanced one day to fire the pending confirmations, then the seven case kinds on the exam's persons."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 30:1-17: Mishnah Nedarim 9-11, Niddah 5:6, Shabbat 24:5 on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_vows]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # ---- THE STATE MACHINE (LITERAL submits — the daemon gate parses no loop) ----
        w.submit({'kind': 'vow_uttered', 'subject': 'the-man', 'vower': 'the-man', 'vow': 'the-man:olah-upon-me', 'status': 'man', 'vow_kind': 'vow', 'case_source': 'Num 30:3 — a man vows a burnt offering upon himself (Rosh Hashanah 6a:12)'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-minor', 'vower': 'the-minor', 'vow': 'the-minor:konam', 'status': 'daughter', 'age': 10, 'sex': 'girl', 'case_source': 'Mishnah Niddah 5:6 — a girl of ten vows: no vow'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-examined-girl', 'vower': 'the-examined-girl', 'vow': 'the-examined-girl:konam', 'status': 'daughter', 'age': 11, 'sex': 'girl', 'knows_to_whom': True, 'case_source': 'Mishnah Niddah 5:6 — a girl of eleven and a day who knows in Whose name: bound'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-examined-boy', 'vower': 'the-examined-boy', 'vow': 'the-examined-boy:konam', 'status': 'man', 'age': 12, 'sex': 'boy', 'knows_to_whom': False, 'case_source': 'Mishnah Niddah 5:6 — a boy of twelve and a day who does not know: no vow'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-daughter', 'vower': 'the-daughter', 'vow': 'the-daughter:konam-figs', 'status': 'daughter', 'content_class': 'other', 'case_source': 'Num 30:4 — a daughter in her youth in her father\'s house vows'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-father', 'vower': 'the-daughter', 'vow': 'the-daughter:konam-figs', 'by': ['father'], 'silent': True, 'case_source': 'Num 30:5 — her father hears and is silent: the hearing day opens'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-father', 'vower': 'the-daughter', 'vow': 'the-daughter:konam-figs', 'by': ['father'], 'status': 'daughter', 'content_class': 'other', 'case_source': 'Num 30:6 — her father restrains her on the day of his hearing: annulled, the LORD forgives her'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-daughter-silent', 'vower': 'the-daughter-silent', 'vow': 'the-daughter-silent:konam', 'status': 'daughter', 'content_class': 'other', 'case_source': 'Num 30:4 — a second daughter vows'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-father-silent', 'vower': 'the-daughter-silent', 'vow': 'the-daughter-silent:konam', 'by': ['father'], 'silent': True, 'case_source': 'Num 30:5 — her father hears and stays silent past the day'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-betrothed', 'vower': 'the-betrothed', 'vow': 'the-betrothed:konam', 'status': 'betrothed', 'content_class': 'other', 'case_source': 'Num 30:7 — a betrothed maiden vows (Mishnah Nedarim 10:1)'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-betrothed-father', 'vower': 'the-betrothed', 'vow': 'the-betrothed:konam', 'by': ['father', 'husband'], 'silent': True, 'case_source': 'Num 30:8 — her father and her husband hear'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-betrothed-father', 'vower': 'the-betrothed', 'vow': 'the-betrothed:konam', 'by': ['father'], 'status': 'betrothed', 'content_class': 'other', 'case_source': 'Mishnah Nedarim 10:1 — the father annulled and not the husband: not annulled'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-betrothed-father', 'vower': 'the-betrothed', 'vow': 'the-betrothed:konam', 'by': ['father', 'husband'], 'status': 'betrothed', 'content_class': 'other', 'case_source': 'Mishnah Nedarim 10:1 — her father and her husband annul together: annulled'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-widow', 'vower': 'the-widow', 'vow': 'the-widow:nazirite-after-thirty', 'status': 'widow', 'content_class': 'affliction', 'case_source': 'Num 30:10 — a widow vows (Mishnah Nedarim 11:9)'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-new-husband', 'vower': 'the-widow', 'vow': 'the-widow:nazirite-after-thirty', 'by': ['husband'], 'status': 'widow', 'content_class': 'affliction', 'case_source': 'Mishnah Nedarim 11:9 — married within the thirty days, the new husband cannot annul'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-wife-affliction', 'vower': 'the-wife-affliction', 'vow': 'the-wife-affliction:konam-produce-of-the-world', 'status': 'married', 'content_class': 'affliction', 'case_source': 'Num 30:11, 30:14 — a married woman vows off the produce of the world (Mishnah Nedarim 11:2)'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-husband-affliction', 'vower': 'the-wife-affliction', 'vow': 'the-wife-affliction:konam-produce-of-the-world', 'by': ['husband'], 'silent': True, 'case_source': 'Num 30:12 — her husband hears'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-husband-affliction', 'vower': 'the-wife-affliction', 'vow': 'the-wife-affliction:konam-produce-of-the-world', 'by': ['husband'], 'status': 'married', 'content_class': 'affliction', 'case_source': 'Num 30:13 — her husband annuls on the day: annulled, the LORD forgives her'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-wife-other', 'vower': 'the-wife-other', 'vow': 'the-wife-other:konam-my-fathers-work', 'status': 'married', 'content_class': 'other', 'case_source': 'Mishnah Nedarim 11:4 — "I will not make anything for my father" — neither affliction nor between them'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-husband-other', 'vower': 'the-wife-other', 'vow': 'the-wife-other:konam-my-fathers-work', 'by': ['husband'], 'silent': True, 'case_source': 'Num 30:12 — her husband hears'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-husband-other', 'vower': 'the-wife-other', 'vow': 'the-wife-other:konam-my-fathers-work', 'by': ['husband'], 'status': 'married', 'content_class': 'other', 'case_source': 'Mishnah Nedarim 11:4 — he cannot annul: the filter of 30:14 and 30:17'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-wife-after', 'vower': 'the-wife-after', 'vow': 'the-wife-after:konam-bathing', 'status': 'married', 'content_class': 'affliction', 'case_source': 'Num 30:14 — an affliction oath (Mishnah Nedarim 11:1)'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-husband-after', 'vower': 'the-wife-after', 'vow': 'the-wife-after:konam-bathing', 'by': ['husband'], 'silent': True, 'case_source': 'Num 30:15 — her husband is silent from day to day'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-deaf-wife', 'vower': 'the-deaf-wife', 'vow': 'the-deaf-wife:konam', 'status': 'married', 'content_class': 'affliction', 'case_source': 'Nedarim 73a:4 — the wife of a deaf man vows'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-deaf-husband', 'vower': 'the-deaf-wife', 'vow': 'the-deaf-wife:konam', 'by': ['husband'], 'deaf': True, 'case_source': 'Nedarim 73a:4 — "and her husband hears it" excludes the deaf: no hearing'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-wife-well-done', 'vower': 'the-wife-well-done', 'vow': 'the-wife-well-done:konam', 'status': 'married', 'content_class': 'affliction', 'case_source': 'Nedarim 77b:5 — she vows'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-husband-well-done', 'vower': 'the-wife-well-done', 'vow': 'the-wife-well-done:konam', 'by': ['husband'], 'confirm_words': True, 'case_source': 'Nedarim 77b:5 — "you did well": confirmed by his words'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-husband-well-done', 'vower': 'the-wife-well-done', 'vow': 'the-wife-well-done:konam', 'by': ['husband'], 'husband': 'the-husband-well-done', 'status': 'married', 'content_class': 'affliction', 'case_source': 'Num 30:16 — he annuls after confirming: he bears her iniquity'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-wife-mistaken', 'vower': 'the-wife-mistaken', 'vow': 'the-wife-mistaken:konam', 'status': 'married', 'content_class': 'affliction', 'case_source': 'Mishnah Nedarim 11:5 — the wife vows'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-husband-mistaken', 'vower': 'the-wife-mistaken', 'vow': 'the-wife-mistaken:konam', 'by': ['husband'], 'silent': True, 'intends_her': False, 'case_source': 'Mishnah Nedarim 11:5 — he thought it was his daughter\'s: no hearing of this vow'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-wife-partial', 'vower': 'the-wife-partial', 'vow': 'the-wife-partial:konam-figs-and-grapes', 'status': 'married', 'content_class': 'affliction', 'case_source': 'Mishnah Nedarim 11:6 — "figs and grapes are konam to me"'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-husband-partial', 'vower': 'the-wife-partial', 'vow': 'the-wife-partial:konam-figs-and-grapes', 'by': ['husband'], 'silent': True, 'case_source': 'Num 30:12 — her husband hears'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-husband-partial', 'vower': 'the-wife-partial', 'vow': 'the-wife-partial:konam-figs-and-grapes', 'by': ['husband'], 'status': 'married', 'content_class': 'affliction', 'partial': True, 'case_source': 'Mishnah Nedarim 11:6 — annulled for the figs alone: not annulled till the grapes (R. Yishmael)'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-wife-steward', 'vower': 'the-wife-steward', 'vow': 'the-wife-steward:konam', 'status': 'married', 'content_class': 'affliction', 'case_source': 'Nedarim 72b:8 — the wife vows while the husband is away'})
        w.submit({'kind': 'vow_heard', 'subject': 'the-steward', 'vower': 'the-wife-steward', 'vow': 'the-wife-steward:konam', 'by': ['husband'], 'silent': True, 'report': True, 'case_source': 'Nedarim 72b:10 — the report reaches the household'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-steward', 'vower': 'the-wife-steward', 'vow': 'the-wife-steward:konam', 'by': ['husband'], 'status': 'married', 'content_class': 'affliction', 'via_messenger': True, 'case_source': 'Nedarim 72b:8 — the steward annuls in his stead: nothing (R. Yoshiyah)'})
        w.submit({'kind': 'vow_uttered', 'subject': 'the-void-vow', 'vower': 'the-void-vow', 'vow': 'the-void-vow:konam-your-bed', 'status': 'married', 'content_class': 'between', 'void': True, 'case_source': 'Nedarim 81b:4 — "I will not make your bed": void, she owes it'})
        w.advance(w.clock.day + 1)                                             # THE HEARING DAY ENDS: the pending confirmations fire at the evening boundary
        w.submit({'kind': 'vow_restrained', 'subject': 'the-father-silent', 'vower': 'the-daughter-silent', 'vow': 'the-daughter-silent:konam', 'by': ['father'], 'status': 'daughter', 'content_class': 'other', 'case_source': 'Sifrei 153:5 — confirmed for one hour, never annulled: the father after the day annuls nothing'})
        w.submit({'kind': 'vow_restrained', 'subject': 'the-husband-after', 'vower': 'the-wife-after', 'vow': 'the-wife-after:konam-bathing', 'by': ['husband'], 'husband': 'the-husband-after', 'status': 'married', 'content_class': 'affliction', 'case_source': 'Num 30:16 — he annuls them after his hearing: he shall bear her iniquity'})
        # ---- the exam's persons through the seven case kinds ----
        w.submit({'kind': 'mans_vow_case', 'subject': 'the-frame', 'person': 'the-frame', 'ask': 'frame', 'case_source': 'Num 30:2 — the exam\'s row frame'})
        w.submit({'kind': 'mans_vow_case', 'subject': 'the-two-offices', 'person': 'the-two-offices', 'ask': 'this_is_the_thing', 'case_source': 'Nedarim 77b:8 — the exam\'s row this_is_the_thing'})
        w.submit({'kind': 'mans_vow_case', 'subject': 'the-expert', 'person': 'the-expert', 'ask': 'heads_of_the_tribes', 'case_source': 'Nedarim 78b:3 — the exam\'s row heads_of_the_tribes'})
        w.submit({'kind': 'mans_vow_case', 'subject': 'the-vower-of-carrion', 'person': 'the-vower-of-carrion', 'ask': 'vow_support', 'base': 'torah_forbidden', 'case_source': 'Mishnah Nedarim 2:1 — the exam\'s row vow_support (a Torah-forbidden base)'})
        w.submit({'kind': 'mans_vow_case', 'subject': 'the-delayer', 'person': 'the-delayer', 'ask': 'two_transgressions', 'case_source': 'Nedarim 3a:7 — the exam\'s row two_transgressions'})
        w.submit({'kind': 'mans_vow_case', 'subject': 'the-slave', 'person': 'the-slave', 'ask': 'on_his_soul', 'case_source': 'Nazir 61a:8 — the exam\'s row on_his_soul'})
        w.submit({'kind': 'daughters_vow_case', 'subject': 'the-mature-daughter', 'person': 'the-mature-daughter', 'ask': 'in_her_youth', 'stage': 'mature', 'case_source': 'Mishnah Nedarim 11:10 — the exam\'s row in_her_youth (mature)'})
        w.submit({'kind': 'daughters_vow_case', 'subject': 'the-deaf-father', 'person': 'the-deaf-father', 'ask': 'the_deaf', 'case_source': 'Nedarim 73a:4 — the exam\'s row the_deaf'})
        w.submit({'kind': 'daughters_vow_case', 'subject': 'the-forgiven-daughter', 'person': 'the-forgiven-daughter', 'ask': 'forgiveness', 'case_source': 'Kiddushin 81b:5 — the exam\'s row forgiveness'})
        w.submit({'kind': 'daughters_vow_case', 'subject': 'the-confirmed-hour', 'person': 'the-confirmed-hour', 'ask': 'confirmed_for_one_hour', 'case_source': 'Sifrei 153:5 — the exam\'s row confirmed_for_one_hour'})
        w.submit({'kind': 'betrothed_vow_case', 'subject': 'the-joint-annullers', 'person': 'the-joint-annullers', 'ask': 'joint_authority', 'by': ['father', 'husband'], 'case_source': 'Mishnah Nedarim 10:1 — the exam\'s row joint_authority'})
        w.submit({'kind': 'betrothed_vow_case', 'subject': 'the-orphaned-betrothed', 'person': 'the-orphaned-betrothed', 'ask': 'fathers_death', 'case_source': 'Mishnah Nedarim 10:2 — the exam\'s row fathers_death'})
        w.submit({'kind': 'betrothed_vow_case', 'subject': 'the-advance-annuller', 'person': 'the-advance-annuller', 'ask': 'annul_in_advance', 'case_source': 'Mishnah Nedarim 10:7 — the exam\'s row annul_in_advance'})
        w.submit({'kind': 'betrothed_vow_case', 'subject': 'the-utterer', 'person': 'the-utterer', 'ask': 'utterance_is_oath', 'case_source': 'Shevuot 20a:4 — the exam\'s row utterance_is_oath'})
        w.submit({'kind': 'widows_vow_case', 'subject': 'the-widow-of-marriage', 'person': 'the-widow-of-marriage', 'ask': 'from_marriage', 'case_source': 'Sifrei 154:1 — the exam\'s row from_marriage'})
        w.submit({'kind': 'widows_vow_case', 'subject': 'the-priests-daughter', 'person': 'the-priests-daughter', 'ask': 'priests_daughter_pair', 'case_source': 'Yevamot 87a:6 — the exam\'s row priests_daughter_pair'})
        w.submit({'kind': 'wifes_vow_case', 'subject': 'the-earlier-vow', 'person': 'the-earlier-vow', 'ask': 'in_husbands_house', 'when': 'before', 'case_source': 'Nedarim 67b:1 — the exam\'s row in_husbands_house (before)'})
        w.submit({'kind': 'wifes_vow_case', 'subject': 'the-two-silences', 'person': 'the-two-silences', 'ask': 'two_silences', 'case_source': 'Nedarim 79a:5 — the exam\'s row two_silences'})
        w.submit({'kind': 'wifes_vow_case', 'subject': 'the-nazirite-wife', 'person': 'the-nazirite-wife', 'ask': 'her_and_i', 'who_first': 'husband', 'case_source': 'Mishnah Nazir 4:1 — the exam\'s row her_and_i'})
        w.submit({'kind': 'affliction_oath_case', 'subject': 'the-storekeeper-vow', 'person': 'the-storekeeper-vow', 'ask': 'affliction_scope', 'what': 'storekeeper', 'case_source': 'Mishnah Nedarim 11:2 — the exam\'s row affliction_scope (this storekeeper)'})
        w.submit({'kind': 'affliction_oath_case', 'subject': 'the-deadline', 'person': 'the-deadline', 'ask': 'the_deadline', 'case_source': 'Nedarim 76b:4-8 — the exam\'s row the_deadline'})
        w.submit({'kind': 'affliction_oath_case', 'subject': 'the-late-annuller', 'person': 'the-late-annuller', 'ask': 'after_his_hearing', 'case_source': 'Nedarim 79a:4 — the exam\'s row after_his_hearing'})
        w.submit({'kind': 'affliction_oath_case', 'subject': 'the-sabbath-annuller', 'person': 'the-sabbath-annuller', 'ask': 'annul_on_sabbath', 'case_source': 'Mishnah Shabbat 24:5 — the exam\'s row annul_on_sabbath'})
        w.submit({'kind': 'affliction_oath_case', 'subject': 'the-bed-vow', 'person': 'the-bed-vow', 'ask': 'void_vow_owed_duty', 'case_source': 'Nedarim 81b:4 — the exam\'s row void_vow_owed_duty'})
        w.submit({'kind': 'statutes_case', 'subject': 'the-likening', 'person': 'the-likening', 'ask': 'likening_both_ways', 'case_source': 'Sifrei 156:3 — the exam\'s row likening_both_ways'})
        w.submit({'kind': 'statutes_case', 'subject': 'the-receipt', 'person': 'the-receipt', 'ask': 'the_receipt', 'case_source': 'Num 30:1 — the exam\'s row the_receipt'})
        w.submit({'kind': 'statutes_case', 'subject': 'the-generations', 'person': 'the-generations', 'ask': 'all_generations', 'case_source': 'Bava Batra 120b:1 — the exam\'s row all_generations'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    closed = lambda eid: len([e for e in w.entity(eid).ledger if e['effect'] == 'vow_bound' and not e.get('open')])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    return ((n('the-man', 'vow_bound'), n('the-minor', 'exempt'), n('the-examined-girl', 'vow_bound'), n('the-examined-boy', 'exempt'),
             n('the-daughter', 'vow_annulled'), closed('the-daughter'), n('the-daughter-silent', 'vow_confirmed'), n('the-daughter-silent', 'vow_annulled'), closed('the-daughter-silent'),
             n('the-betrothed', 'vow_annulled'), closed('the-betrothed'), n('the-widow', 'vow_annulled'), closed('the-widow'),
             n('the-wife-affliction', 'vow_annulled'), closed('the-wife-affliction'), n('the-wife-other', 'vow_annulled'), n('the-wife-other', 'vow_confirmed'),
             n('the-wife-after', 'vow_confirmed'), n('the-wife-after', 'vow_annulled'), n('the-husband-after', 'iniquity_borne'),
             n('the-deaf-wife', 'exempt'), n('the-deaf-wife', 'vow_confirmed'), n('the-wife-well-done', 'vow_confirmed'), n('the-husband-well-done', 'iniquity_borne'),
             n('the-wife-mistaken', 'vow_confirmed'), n('the-wife-partial', 'vow_confirmed'), n('the-wife-partial', 'vow_annulled'), n('the-wife-steward', 'vow_confirmed'), n('the-wife-steward', 'vow_annulled'),
             n('the-void-vow', 'exempt'), n('the-void-vow', 'vow_bound')),
            (tset, tfire, tcan, len(w.timers)),
            (n('the-frame', 'commanded'), n('the-two-offices', 'accepted'), n('the-expert', 'accepted'), n('the-vower-of-carrion', 'exempt'), n('the-delayer', 'commanded'), n('the-slave', 'exempt'),
             n('the-mature-daughter', 'vow_bound'), n('the-deaf-father', 'exempt'), n('the-forgiven-daughter', 'vow_annulled'), n('the-confirmed-hour', 'vow_confirmed'),
             n('the-joint-annullers', 'vow_annulled'), n('the-orphaned-betrothed', 'vow_bound'), n('the-advance-annuller', 'vow_bound'), n('the-utterer', 'accepted'),
             n('the-widow-of-marriage', 'vow_bound'), n('the-priests-daughter', 'accepted'), n('the-earlier-vow', 'vow_bound'), n('the-two-silences', 'vow_confirmed'), n('the-nazirite-wife', 'vow_annulled'),
             n('the-storekeeper-vow', 'vow_bound'), n('the-deadline', 'vow_confirmed'), n('the-late-annuller', 'iniquity_borne'), n('the-sabbath-annuller', 'vow_annulled'), n('the-bed-vow', 'exempt'),
             n('the-likening', 'accepted'), n('the-receipt', 'accepted'), n('the-generations', 'commanded')),
            len(w.entities)), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run, NUMBERS_WALK.md "Sitting 10b" — the state machine's arithmetic): the man bound, the minor and the unknowing boy exempt,
# the examined girl bound; the daughter annulled with her debit CLOSED; the silent daughter confirmed by the fire, never annulled, the debit open; the betrothed annulled by
# the pair (the father alone wrote nothing) with the debit closed; the widow untouched; the affliction wife annulled and closed; the other-class wife not annulled and confirmed
# by the fire; the wife-after confirmed by the fire, not annulled, her husband bears the iniquity; the deaf-wife exempt, no confirmation; the well-done wife confirmed at once,
# her husband bears; the mistaken hearing no confirmation; the partial and the steward's wives confirmed by the fire, not annulled; the void vow exempt, no debit.
# TIMERS: set 8 (the daughter, the silent daughter, the betrothed, the affliction wife, the other-class wife, the wife-after, the partial, the steward), fired 5 (the silent
# daughter, the other-class, the wife-after, the partial, the steward), cancelled 3 (the daughter, the betrothed, the affliction wife), pending 0. ENTITIES: the machine's
# 19 persons written on + the exam's 27 = 46.
SCENE_PREDICTED = ((1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0), (8, 5, 3, 0),
                   (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 46)


def narrative():
    """THE NUMBERS WALK 10b (2026-09-12): the portion's own act AS HISTORY — the ONE line of 30:2-17 at the counter's day (40, 6, 1), page-order
    after the calendar's line (28:1-29:39), on a world with this runner's daemon: ONE write (the statutes commanded on israel), no timer, no
    marker, no entity but israel. Recorded by the sequential run's recorder and stitched onto the tape. Not a graded cell: the tuple below is
    a tripwire typed from the design; the sequence world's RUN tuple and CV1-CV9 grade the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 30:2-17: the vows\' law on the tape — Moses\' one speech to the heads of the tribes (the exodus epoch)', epoch='exodus')
        w.laws = [law_vows]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the one line typed out
        w.submit({'kind': 'vows_law_spoken', 'subject': 'moses', 'to': 'the-heads-of-the-tribes', 'heads': ['30:3 a man', '30:4 a daughter in her youth', '30:6 restrained', '30:7 the betrothed', '30:9 the husband on the day', '30:10 the widow', '30:11 the married', '30:13 annulled', '30:15 silent from day to day', '30:16 after his hearing'], 'close': CLOSE, 'case_source': LINE})
    writes = [e for e in w.entity('israel').ledger if e['effect'] == 'commanded']
    return (len(writes), len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:]), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (1, 0, 1, (6, 1))   # NUMBERS_WALK.md "Sitting 10b": one write (commanded on israel), no timer, one entity, the date (6, 1) of the fortieth year
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: the vows\' narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
