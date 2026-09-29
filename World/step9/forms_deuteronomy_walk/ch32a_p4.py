# THE ROWS built from the spec's lines: (name, op, subject, en, he with its gloss, ink, corpus, exam)
CELLN = {k: v for k, v in S.CELLS.items()}
SUBJ_EN = {'israel_people': 'Israel', 'yehoshua': 'Joshua (the entity yehoshua)', 'moses': 'Moses'}
# the he's seat is the verse PHRASE found it in — read from the phrase table's own call above (the verse typed beside the tokens), never a second typing
HV = {}
for l in open(__file__, encoding='utf-8').read().split('\n'):
    for m in re.finditer(r"H\['([a-z_]+)'\] = PHRASE\(D, (32), (\d+), ", l): HV[m.group(1)] = (m.group(2), m.group(3))
assert len(HV) == 42 and set(HV) == set(OWN42), (len(HV), set(OWN42) - set(HV))
NEW = []
for kind, first, rng, claim, cell, form, fields, effs, reuses in S.LINES:
    c_, lo_, hi_ = RNG(rng)
    for name, op, sub in effs:
        en, gloss, ink, ask = E[name]
        assert ask in fields, (name, ask, fields)
        assert int(HV[name][0]) == c_ and lo_ <= int(HV[name][1]) <= hi_, (name, HV[name], rng)   # the phrase's verse inside its line's range
        assert ('on ' + SUBJ_EN[sub].split(' (')[0]) in en, (name, sub, en[:120])   # the subject named in the value
        NEW.append((name, op, sub, en, "%s (%s — Deut %s:%s)" % (H[name], gloss, HV[name][0], HV[name][1]), ink, CORPUS, EX % (cell, CELLN[cell], ask, kind)))
assert len(NEW) == 42 and [n for n, *_ in NEW] == list(OWN42), (len(NEW), [n for n, *_ in NEW][:3])
assert all(H[n] in he for n, op, sub, en, he, *_ in NEW), 'every he from the phrase table'
added = 0
for name, op, sub, en, he, ink, corpus, exam in NEW:
    if name in fx: continue
    text = text.rstrip('\n') + '\n' + f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    ledger_op: {op}   # {W20}: chapter 32's compile, LEAN — {name} on {sub}, the name and the value from the spine's rows, Onkelos, the outside rows and the twenty-six Mishnah and Tosefta rows\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    exam: {q(exam)}\n"
    added += 1
# ---- THE THREE REUSED ROWS AMENDED with their further seats (13b's, 14b's, 18b's and 19b's precedent — a reused effect is a further entry on the same ledger; the row names its new seat, its value untouched) ----
SEATS = {'heaven_and_earth_witness': [('fifth_seat', "%s — the STATUS REUSED at Deut 32:1 by law_song_charge_nebo on israel_people (the line song_witnesses_called_declared: 'give ear, O heavens, and I will speak; and let the earth hear the words of my mouth' — the imperative plural ONCE in the Bible; THE CHAIN OF WITNESSES' FIFTH SEAT — 4:26, 30:19, 31:28, 32:1 on obey_horeb's DATA the_witnesses_chain; the court law read into the witnesses by the Sifrei 306:9, 306:12 and 323:5; Isaiah 1:2's twin taught at 306:11-12); 4:26 the first seat, 8:19's testimony the second, 30:19 the third, 31:28 the fourth" % W20)],
         'face_hidden_and_forsaken_foretold': [('second_seat', "%s — the HEAVEN entry REUSED at Deut 32:20 by law_song_charge_nebo on israel_people (the line song_face_hidden_foolish_nation_declared: 'and He said: I will hide My face from them, I will see what their end shall be' — THE HIDDEN FACE THE THIRD TIME: Onkelos 'I will remove My Shekhinah' at 31:17, 31:18 and 32:20, the Sifrei 320:3 speaking Onkelos's words; the cohortative ONCE in the Bible); 31:17-18 the first seat (covenant_return_charge's line apostasy_and_hidden_face_foretold)" % W20)],
         'length_of_days_on_the_land_promised': [('second_seat', "%s — the HEAVEN entry REUSED at Deut 32:47 by law_song_charge_nebo on israel_people (the line set_your_heart_no_empty_matter_declared: 'and through this thing you shall prolong your days on the land which you cross the Jordan to possess' — 11:9's five in order; the reward's two arms, the fruit here and the days there); 30:20 the first seat (covenant_return_charge's line life_and_death_choice_declared)" % W20)]}
assert sorted(SEATS) == sorted(S.REUSE_BEFORE) and sum(len(v) for v in SEATS.values()) == 3 == len(S.REUSES)
for name, seats in SEATS.items():
    for k, v in seats:
        assert re.search(r'Deut 32:\d+', v) and k.split('_')[0] in ('second', 'third', 'fourth', 'fifth', 'sixth', 'seventh')
    assert S.REUSE_BEFORE[name] + len(seats) == S.REUSE_AFTER[name]
amended = 0
for name, seats in SEATS.items():
    i = text.index(f'\n  {name}:\n'); j = i + 1
    while True:
        j = text.find('\n  ', j + 1)
        if j < 0 or (j + 3 < len(text) and text[j + 3] not in ' \n' and text[j + 2] == ' '): break
    row = text[i:j] if j > 0 else text[i:]
    if W20 in row: continue
    ins = ''.join(f'    {k}: {q(v)}\n' for k, v in seats)
    text = text[:i] + row.rstrip('\n') + '\n' + ins + (text[j + 1:] if j > 0 else '')
    amended += len(seats)
if not CHECK:
    open(path, 'w', encoding='utf-8').write(text)
fx = yaml.safe_load(open(path, encoding='utf-8'))['effects']
assert CHECK or (all(n in fx for n, *_ in NEW) and fx['doctrine_as_rain_and_dew_likened']['ledger_op'] == 'status' and fx['jealousy_by_no_people_foolish_nation']['ledger_op'] == 'heaven' and fx['hoshea_speaks_the_song_beside_moses']['ledger_op'] == 'status' and fx['see_the_land_from_afar_not_go_there']['ledger_op'] == 'heaven' and fx['as_aaron_died_in_hor_and_was_gathered']['ledger_op'] == 'status')
assert CHECK or (fx['heaven_and_earth_witness'].get('fifth_seat') and fx['face_hidden_and_forsaken_foretold'].get('second_seat') and fx['length_of_days_on_the_land_promised'].get('second_seat')), 'the reused rows amended'
C = S.counts()
assert sum(1 for n, op, *_ in NEW if op == 'block') == 0 == C['ops'].get('block', 0) and sum(1 for n, op, *_ in NEW if op == 'status') == 32 == C['ops']['status'] and sum(1 for n, op, *_ in NEW if op == 'heaven') == 10 == C['ops']['heaven'], (sum(1 for n, op, *_ in NEW if op == 'status'), sum(1 for n, op, *_ in NEW if op == 'heaven'))
SUBC = {}
for n, op, sub, *_ in NEW: SUBC[sub] = SUBC.get(sub, 0) + 1
assert SUBC == {'israel_people': 36, 'yehoshua': 1, 'moses': 5} == C['subjects_new'], (SUBC, C['subjects_new'])
print('effects: %d %s (registry %d) — 32 status / 0 block / 10 heaven on %s; the reused rows amended with %d seats (%s); the he found in the verses: %s' % (added, 'to add' if CHECK else 'added', len(fx), SUBC, amended, 'to amend' if CHECK else 'amended', ' | '.join('%s=%s' % (k, v) for k, v in H.items())))
print('TYPES A OK' + (' (check)' if CHECK else ''))
