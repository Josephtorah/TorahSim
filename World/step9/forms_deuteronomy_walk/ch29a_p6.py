# THE ROWS built from the spec's lines: (name, op, subject, en, he with its gloss, ink, corpus, exam)
CELLN = {k: v for k, v in S.CELLS.items()}
SUBJ_EN = {'israel_people': 'Israel', 'yehoshua': 'Joshua (the entity yehoshua)', 'moses': 'Moses', 'the_levites': 'the Levites'}
# the he's seat is the verse PHRASE found it in — read from the phrase table's own call above (the verse typed beside the tokens), never a second typing
HV = {}
for l in open(__file__, encoding='utf-8').read().split('\n'):
    for m in re.finditer(r"H\['([a-z_]+)'\] = PHRASE\(D, (29|30|31), (\d+), ", l): HV[m.group(1)] = (m.group(2), m.group(3))
assert len(HV) == 59 and set(HV) == set(OWN59), (len(HV), set(OWN59) - set(HV))
NEW = []
for kind, first, rng, claim, cell, form, fields, effs, reuses in S.LINES:
    c_, lo_, hi_ = RNG(rng)
    for name, op, sub in effs:
        en, gloss, ink, ask = E[name]
        assert ask in fields, (name, ask, fields)
        assert int(HV[name][0]) == c_ and lo_ <= int(HV[name][1]) <= hi_, (name, HV[name], rng)   # the phrase's verse inside its line's range
        assert ('on ' + SUBJ_EN[sub].split(' (')[0]) in en, (name, sub, en[:120])   # the subject named in the value
        NEW.append((name, op, sub, en, "%s (%s — Deut %s:%s)" % (H[name], gloss, HV[name][0], HV[name][1]), ink, CORPUS, EX % (cell, CELLN[cell], ask, kind)))
assert len(NEW) == 59 and [n for n, *_ in NEW] == list(OWN59), (len(NEW), [n for n, *_ in NEW][:3])
assert all(H[n] in he for n, op, sub, en, he, *_ in NEW), 'every he from the phrase table'
added = 0
for name, op, sub, en, he, ink, corpus, exam in NEW:
    if name in fx: continue
    text = text.rstrip('\n') + '\n' + f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    ledger_op: {op}   # {W19}: chapters 29-31's compile, LEAN — {name} on {sub}, the name and the value from the spine's rows, Onkelos, the outside rows and the seven Mishnah and Tosefta rows\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    exam: {q(exam)}\n"
    added += 1
# ---- THE SEVEN REUSED ROWS AMENDED with their nine further seats (13b's, 14b's and 18b's precedent — a reused effect is a further entry on the same ledger; the row names its new seat, its value untouched) ----
SEATS = {'entered_the_covenant': [('fourth_seat', "%s — the STATUS REUSED at Deut 29:11 by law_covenant_return_charge on israel_people (the line covenant_oath_entered_declared: 'that you may enter into the covenant of the LORD your God and into His oath' — the second covenant, at Moab; 28:69 'besides the covenant at Horeb'; the Sifrei 104:8's three covenants); Exodus 24's three entries the first seats (the blood thrown)" % W19)],
         'became_the_lords_people_this_day': [('second_seat', "%s — the STATUS REUSED at Deut 29:12 by law_covenant_return_charge on israel_people (the line covenant_oath_entered_declared: 'that He may establish you this day for a people to Himself and He will be your God, as He spoke to you and as He swore to your fathers' — the establishing; the AS_WHEN pointer a run citation of the oath lines); 27:9's the first seat" % W19)],
         'heaven_and_earth_witness': [('third_seat', "%s — the STATUS REUSED at Deut 30:19 by law_covenant_return_charge on israel_people (the line life_and_death_choice_declared: 'I call heaven and earth to witness against you this day: life and death I have set before you' — its first seven words identical with 4:26; THE CHAIN OF WITNESSES 4:26, 30:19, 31:28, 32:1 — obey_horeb's DATA the_witnesses_chain); 4:26 the first seat, 8:19's 'I testify' the second" % W19),
                                      ('fourth_seat', "%s — the STATUS REUSED at Deut 31:28 by law_covenant_return_charge on israel_people (the line assembly_and_song_spoken_declared: 'assemble to me all the elders of your tribes and your officers, that I may speak these words in their ears and call heaven and earth to witness against them' — the chain's fourth seat; 32:1 'give ear, O heavens' the fifth, sitting 20's)" % W19)],
         'blessing_and_curse_set': [('second_seat', "%s — the STATUS REUSED at Deut 30:19 by law_covenant_return_charge on israel_people (the line life_and_death_choice_declared: 'life and death I have set before you, the blessing and the curse' — the pair named a second time with the terms life and death; 'the blessing and the curse' 30:1, 30:19 and Joshua 8:34); 11:26's the first seat" % W19)],
         'cleaving_commanded': [('third_seat', "%s — the STATUS REUSED at Deut 30:20 by law_covenant_return_charge on israel_people (the line life_and_death_choice_declared: 'to love the LORD your God, to hearken to His voice and to cleave to Him, for He is your life and the length of your days'); 10:20 the first seat, 13:5 the second" % W19)],
         'fear_not_promised': [('fifth_seat', "%s — the HEAVEN entry REUSED at Deut 31:6 by law_covenant_return_charge ON ISRAEL_PEOPLE — the first entry on Israel's ledger (the line crossing_charge_declared: 'be strong and of good courage, fear not nor be dismayed at them, for the LORD your God, He it is who goes with you; He will not fail you nor forsake you' — the plural imperative; 20:3-4's war speech by CALL); Isaac's, Jacob's, Moses' (Numbers 21:33-34) and Joshua's (3:21-22) the four before it" % W19),
                               ('sixth_seat', "%s — the HEAVEN entry REUSED at Deut 31:8 by law_covenant_return_charge ON YEHOSHUA — the second on his ledger (the line joshua_charged_before_israel: 'and the LORD, He it is who goes before you; He will be with you; He will not fail you nor forsake you; fear not nor be dismayed' — Moses' public charge; 3:21-22's the first; Joshua 1:5-6, 1:9 the run, a pointer ahead owed)" % W19)],
         'glory_appeared': [('seventh_seat', "%s — the HEAVEN entry REUSED at Deut 31:15 by law_covenant_return_charge ON THE_TENT_OF_MEETING — the sixth on the tent's ledger, the seventh on the world (the line tent_summons_cloud_appeared: 'and the LORD appeared in the tent in a pillar of cloud, and the pillar of cloud stood over the door of the tent' — Exodus 33:9-10 and Numbers 12:5 the kin four in order; the cloud's last standing in the Torah's narrative — the three gifts by three merits, Tosefta Sotah 11:4); Exodus 40:34, Numbers 14:10, 16:18-19, 17:6-7, 20:6 on the tent and Leviticus 9:23 on Israel the six before it" % W19)]}
assert sorted(SEATS) == sorted(S.REUSE_BEFORE) and sum(len(v) for v in SEATS.values()) == 9 == len(S.REUSES)
for name, seats in SEATS.items():
    for k, v in seats:
        assert re.search(r'Deut 3[01]:\d+|Deut 29:\d+', v) and k.split('_')[0] in ('second', 'third', 'fourth', 'fifth', 'sixth', 'seventh')
    assert S.REUSE_BEFORE[name] + len(seats) == S.REUSE_AFTER[name]
amended = 0
for name, seats in SEATS.items():
    i = text.index(f'\n  {name}:\n'); j = i + 1
    while True:
        j = text.find('\n  ', j + 1)
        if j < 0 or (j + 3 < len(text) and text[j + 3] not in ' \n' and text[j + 2] == ' '): break
    row = text[i:j] if j > 0 else text[i:]
    if W19 in row: continue
    ins = ''.join(f'    {k}: {q(v)}\n' for k, v in seats)
    text = text[:i] + row.rstrip('\n') + '\n' + ins + (text[j + 1:] if j > 0 else '')
    amended += len(seats)
if not CHECK:
    open(path, 'w', encoding='utf-8').write(text)
fx = yaml.safe_load(open(path, encoding='utf-8'))['effects']
assert CHECK or (all(n in fx for n, *_ in NEW) and fx['heart_turning_to_other_gods_barred']['ledger_op'] == 'block' and fx['hidden_idolater_unpardoned']['ledger_op'] == 'heaven' and fx['covenant_words_keeping_commanded']['ledger_op'] == 'status' and fx['lord_with_joshua_promised']['ledger_op'] == 'heaven' and fx['book_of_the_law_beside_the_ark_commanded']['ledger_op'] == 'status')
assert CHECK or (fx['entered_the_covenant'].get('fourth_seat') and fx['became_the_lords_people_this_day'].get('second_seat') and fx['heaven_and_earth_witness'].get('third_seat') and fx['heaven_and_earth_witness'].get('fourth_seat') and fx['blessing_and_curse_set'].get('second_seat') and fx['cleaving_commanded'].get('third_seat') and fx['fear_not_promised'].get('fifth_seat') and fx['fear_not_promised'].get('sixth_seat') and fx['glory_appeared'].get('seventh_seat')), 'the reused rows amended'
C = S.counts()
assert sum(1 for n, op, *_ in NEW if op == 'block') == 2 == C['ops']['block'] and sum(1 for n, op, *_ in NEW if op == 'status') == 31 == C['ops']['status'] and sum(1 for n, op, *_ in NEW if op == 'heaven') == 26 == C['ops']['heaven'], (sum(1 for n, op, *_ in NEW if op == 'block'), sum(1 for n, op, *_ in NEW if op == 'status'), sum(1 for n, op, *_ in NEW if op == 'heaven'))
SUBC = {}
for n, op, sub, *_ in NEW: SUBC[sub] = SUBC.get(sub, 0) + 1
assert SUBC == {'israel_people': 53, 'yehoshua': 3, 'moses': 2, 'the_levites': 1} == C['subjects_new'], (SUBC, C['subjects_new'])
print('effects: %d %s (registry %d) — 31 status / 2 block / 26 heaven on %s; the reused rows amended with %d seats (%s); the he found in the verses: %s' % (added, 'to add' if CHECK else 'added', len(fx), SUBC, amended, 'to amend' if CHECK else 'amended', ' | '.join('%s=%s' % (k, v) for k, v in H.items())))
print('TYPES A OK' + (' (check)' if CHECK else ''))
