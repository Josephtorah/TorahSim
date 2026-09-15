import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK 5b — the two gates' first fails READ and paid: (1) the daemon gate parses literal `if k == '...'` branches only and a kind
# name of letters and underscores — the `if k in (...)` branches split, the digit kind renamed (fire_consumed_the_250 -> fire_consumed_the_two_
# hundred_fifty) in the runner, the registry and the daemon block; the case kinds' declared sets brought to the cells' written sets; (2) the
# dependency gate's six undispositioned token edges dispositioned — chatat, minchah, moadim, vayikra5, yovel CALL by live calls at import
# (18:9's sin, meal and guilt offerings; 18:13's first fruits; 18:16's valuation), family VIA zelophehad; the three AS_WHEN pointers INTERNAL;
# the registration edge — the import and the DAEMON_ORDER row in cold_run_sequence.py.
import re
S = '<scratch>'
R = (_ROOT + '/World/step9')
def rep(path, a, b, n=1):
    s = open(path, encoding='utf-8').read()
    assert s.count(a) == n, (path, a[:70], s.count(a))
    open(path, 'w', encoding='utf-8').write(s.replace(a, b))
# ---- the runner parts ----
for part in ('korach_part1.py', 'korach_part4.py', 'korach_part5.py'):
    p = f'{S}/{part}'; s = open(p, encoding='utf-8').read()
    s = s.replace('fire_consumed_the_250', 'fire_consumed_the_two_hundred_fifty')
    open(p, 'w', encoding='utf-8').write(s)
rep(f'{S}/korach_part1.py', "import cold_run_offerings as OF                  # THE EDGE: korach -> offerings CALL, reference (18:18's peace offering row)\n",
    "import cold_run_offerings as OF                  # THE EDGE: korach -> offerings CALL, reference (18:18's peace offering row)\n"
    "import cold_run_chatat as CH                     # THE EDGE: korach -> chatat CALL, reference (18:9's 'every sin offering of theirs' — the most-holy list; 16:26's 'their sins' the homograph)\n"
    "import cold_run_minchah as MN                    # THE EDGE: korach -> minchah CALL, reference (18:9's 'every meal offering of theirs'; 16:15's 'their offering' Cain's word, the homograph)\n"
    "import cold_run_moadim as MO                     # THE EDGE: korach -> moadim CALL, reference (18:13's first fruits — the two loaves' precedence, Menachot 84b)\n"
    "import cold_run_vayikra5 as V5                   # THE EDGE: korach -> vayikra5 CALL, reference (18:9's 'every guilt offering of theirs')\n"
    "import cold_run_yovel as YV                      # THE EDGE: korach -> yovel CALL, reference (18:16's 'by your valuation' — Lev 27:25's shekel at its second seat; the tithe VIA temurah)\n")
rep(f'{S}/korach_part1.py', "OF_SHELAMIM = OF.dispatch('shelamim'); assert isinstance(OF_SHELAMIM, dict) and 'place' in OF_SHELAMIM, type(OF_SHELAMIM)\n",
    "OF_SHELAMIM = OF.dispatch('shelamim'); assert isinstance(OF_SHELAMIM, dict) and 'place' in OF_SHELAMIM, type(OF_SHELAMIM)\n"
    "CH_SIN = CH.domain({'intent': 'unwitting'})['v']                                 # 18:9's sin offering — the chatat engine's own object (the unwitting arm)\n"
    "MN_SINNER = MN.adjuncts('sinner')                                                 # 18:9's meal offering — the sinner's (no oil, no frankincense): the priests eat its remainder (Menachot 73a)\n"
    "MO_LOAVES = MO.two_loaves(); MO_LOAVES = MO_LOAVES['v'] if isinstance(MO_LOAVES, dict) else MO_LOAVES   # 18:13's first fruits — the two loaves precede (Menachot 84b:6)\n"
    "V5_ASHAM = V5.pointers('asham_procedure', V5.DATA); V5_ASHAM = V5_ASHAM['v'] if isinstance(V5_ASHAM, dict) else V5_ASHAM   # 18:9's guilt offering — the Lev 5 engine's own\n"
    "YV_SHEKEL = YV.field_valuation(49)['shekel']['v']; assert YV_SHEKEL == 20, YV_SHEKEL   # 18:16 'by your valuation... twenty gerah' — Lev 27:25's definition at its second seat\n")
rep(f'{S}/korach_part3.py', "move('Menachot 58a:14', 'the leper\\'s log included')\n        return out(\"every offering, every meal offering, every sin offering, every guilt offering (18:9)",
    "move('Menachot 58a:14', 'the leper\\'s log included'); move('CALLED cold_run_chatat.domain(unwitting) -> %r; cold_run_minchah.adjuncts(sinner) -> %r; cold_run_vayikra5.pointers(asham_procedure) -> %r [IMPORT, live calls]' % (CH_SIN, MN_SINNER, str(V5_ASHAM)[:60]), 'the sin, meal and guilt offerings the engines\\' own objects')\n        return out(\"every offering, every meal offering, every sin offering, every guilt offering (18:9)")
rep(f'{S}/korach_part3.py', "move('Chullin 136a:8; Menachot 84b:6, 84b:10', 'partners liable, outside the land exempt; roofs and ships; the household eats — the verse read as two')",
    "move('Chullin 136a:8; Menachot 84b:6, 84b:10', 'partners liable, outside the land exempt; roofs and ships; the household eats — the verse read as two'); move('CALLED cold_run_moadim.two_loaves() -> %r [IMPORT, live call]' % (str(MO_LOAVES)[:80],), 'the two loaves precede the first fruits (Menachot 84b:6)')")
rep(f'{S}/korach_part3.py', "move('Bekhorot 50a:6; Sifrei Bamidbar 118:1', '\"shall be\" — may add (the Sages\\' sixth); \"the same is twenty\" — never fewer')",
    "move('Bekhorot 50a:6; Sifrei Bamidbar 118:1', '\"shall be\" — may add (the Sages\\' sixth); \"the same is twenty\" — never fewer'); move('CALLED cold_run_yovel.field_valuation(49)[shekel] -> %r [IMPORT, live call]' % YV_SHEKEL, 'Lev 27:25 \"twenty gerah shall be the shekel\" — \"by your valuation\" (18:16) the valuations\\' word')")
rep(f'{S}/korach_part4.py', "    if k in ('levites_rebuked', 'censers_commanded', 'separation_commanded'):\n        return []                                  # the words are the lines' values (16:8-11, 16:16-17, 16:20-21)\n",
    "    if k == 'levites_rebuked':\n        return []                                  # the words are the line's value (16:8-11)\n    if k == 'censers_commanded':\n        return []                                  # the command restated (16:16-17)\n    if k == 'separation_commanded':\n        return []                                  # the threat the value (16:20-21)\n")
rep(f'{S}/korach_part4.py', "    if k in ('watch_case', 'stranger_service_case'):\n        v, e, _ = the_watch({'ask': event['ask']}, DATA); L = 'F3 [%s]' % v; s_ = event['person']\n        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'death_by_heaven': E_('death_by_heaven', s_, cp='HEAVEN', value=v, law=L), 'put_to_death': E_('put_to_death', s_, cp='HEAVEN', value=v, law=L),\n             'watch_owed': E_('watch_owed', s_, value=v, law=L), 'stranger_barred': E_('stranger_barred', s_, value=v, law=L)}\n        return [W[x] for x in e if x != FX.NONE]\n",
    "    if k == 'watch_case':\n        v, e, _ = the_watch({'ask': event['ask']}, DATA); L = 'F3 [%s]' % v; s_ = event['person']\n        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'death_by_heaven': E_('death_by_heaven', s_, cp='HEAVEN', value=v, law=L), 'put_to_death': E_('put_to_death', s_, cp='HEAVEN', value=v, law=L),\n             'watch_owed': E_('watch_owed', s_, value=v, law=L), 'stranger_barred': E_('stranger_barred', s_, value=v, law=L)}\n        return [W[x] for x in e if x != FX.NONE]\n    if k == 'stranger_service_case':\n        v, e, _ = the_watch({'ask': event['ask']}, DATA); L = 'F3 [%s]' % v; s_ = event['person']\n        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'death_by_heaven': E_('death_by_heaven', s_, cp='HEAVEN', value=v, law=L), 'put_to_death': E_('put_to_death', s_, cp='HEAVEN', value=v, law=L),\n             'watch_owed': E_('watch_owed', s_, value=v, law=L), 'stranger_barred': E_('stranger_barred', s_, value=v, law=L)}\n        return [W[x] for x in e if x != FX.NONE]\n")
# ---- the registries ----
rep(f'{R}/event_vocabulary.yaml', '  fire_consumed_the_250:\n', '  fire_consumed_the_two_hundred_fifty:\n')
rep(f'{R}/daemon_dispositions.yaml', "      fire_consumed_the_250: [put_to_death]                           # 16:35: by HEAVEN on the two hundred fifty\n",
    "      fire_consumed_the_two_hundred_fifty: [put_to_death]            # 16:35: by HEAVEN on the two hundred fifty (the kind renamed at the gate: the parser reads letters and underscores)\n")
rep(f'{R}/daemon_dispositions.yaml', "      plague_staff_case: [accepted, disqualified, exempt, atoned_forgiven, death_by_heaven]   # the exam's rows on 17:1-28\n",
    "      plague_staff_case: [accepted, disqualified, exempt, atoned_forgiven, death_by_heaven, altar_plated, rule_installed, plague_struck, staff_budded, kept_for_a_sign]   # the exam's rows on 17:1-28 — the cell's written set (the gate brought the declaration to it)\n")
rep(f'{R}/daemon_dispositions.yaml', "      watch_case: [accepted, disqualified, exempt, death_by_heaven, put_to_death]   # the exam's rows on 18:1-7\n",
    "      watch_case: [accepted, disqualified, exempt, death_by_heaven, put_to_death, watch_owed, stranger_barred]   # the exam's rows on 18:1-7 — the cell's written set\n")
rep(f'{R}/daemon_dispositions.yaml', "      stranger_service_case: [accepted, disqualified, exempt, death_by_heaven, put_to_death]   # the exam's rows on the stranger who served (Bamidbar's row CALLED)\n",
    "      stranger_service_case: [accepted, disqualified, exempt, death_by_heaven, put_to_death, watch_owed, stranger_barred]   # the exam's rows on the stranger who served (Bamidbar's row CALLED) — the cell's written set\n")
rep(f'{R}/daemon_dispositions.yaml', "      priestly_gifts_case: [accepted, disqualified, exempt, due_to_priest, consecrated_firstborn, redeem_or_break, pays, most_holy, terumah_fed, stranger_barred]   # the exam's rows on 18:8-19\n",
    "      priestly_gifts_case: [accepted, disqualified, exempt, due_to_priest, consecrated_firstborn, redeem_or_break, pays, most_holy, terumah_fed, stranger_barred, consecrated, priestly_dues_granted, covenant_of_salt]   # the exam's rows on 18:8-19 — the cell's written set\n")
rep(f'{R}/daemon_dispositions.yaml', "      tithe_case: [accepted, disqualified, exempt, due_to_priest, pays, inheritance_barred, tithe_granted]   # the exam's rows on 18:20-32\n",
    "      tithe_case: [accepted, disqualified, exempt, due_to_priest, pays, inheritance_barred, tithe_granted, terumah_of_the_tithe_owed]   # the exam's rows on 18:20-32 — the cell's written set\n")
# ---- the dependency edges and pointers ----
rep(f'{R}/dependency_dispositions.yaml', "  - {from: sequence, to: korach, disposition: CALL, link: none,\n",
    '''  - {from: korach, to: chatat, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 5b (2026-09-10) | 18:9 'every sin offering of theirs' — the sin offering among the most holy given to the priests: cold_run_chatat.domain({'intent': 'unwitting'}) CALLED (the engine's own object); 16:26 'lest you be swept away in all their SINS' the homograph (the noun, not the offering)"}
  - {from: korach, to: minchah, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 5b (2026-09-10) | 18:9 'every meal offering of theirs' — the sinner's meal offering's remainder eaten by the priests (Menachot 73a): cold_run_minchah.adjuncts('sinner') CALLED; 16:15 'do not turn to their OFFERING' is Cain's word (Gen 4:5) — the homograph, the reading's crown"}
  - {from: korach, to: moadim, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 5b (2026-09-10) | 18:13 'the first fruits of all that is in their land' — the two loaves precede all first fruits (Menachot 84b:6): cold_run_moadim.two_loaves() CALLED"}
  - {from: korach, to: vayikra5, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 5b (2026-09-10) | 18:9 'every guilt offering of theirs' — the Lev 5 engine's own asham: cold_run_vayikra5.pointers('asham_procedure') CALLED"}
  - {from: korach, to: yovel, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 5b (2026-09-10) | 18:16 'BY YOUR VALUATION, five shekels... twenty gerah' — the valuations' word and the shekel's definition at Lev 27:25: cold_run_yovel.field_valuation(49)['shekel'] CALLED (20); the tithe tokens at 18:21-28 reach Lev 27:30-33 VIA temurah (temurah.tithe, redeem(animal_tithe) CALLED there)"}
  - {from: korach, to: family, disposition: VIA, link: reference, via: zelophehad,
     why: "THE NUMBERS WALK 5b (2026-09-10) | the inheritance tokens at 16:14 (Dathan's 'an inheritance of field and vineyard'), 18:20-26 ('you shall not inherit', 'for an inheritance', 'no inheritance') — the inheritance engine's institution reached through cold_run_zelophehad (inheritance_order(excluded) CALLED), which calls the family engine"}
  - {from: sequence, to: korach, disposition: CALL, link: none,
''')
rep(f'{R}/dependency_dispositions.yaml', '''  - {verse: "Num 15:24", form: AS_PRESCRIBED, runner: shelach, disposition: INTERNAL, link: reference,''',
    '''  - {verse: "Num 17:5", form: AS_WHEN, runner: korach, disposition: INTERNAL, link: reference, why: "THE NUMBERS WALK 5b (2026-09-10) | 'that he be not as Korach and his congregation, AS THE LORD SPOKE BY THE HAND OF MOSES TO HIM' — the output verse's own citation: the speaking to Moses about Aaron within the span (Sifrei 117:1 reads 18:8's frame through it — 'to him' = about him); Sanhedrin 110a:6 the ban on maintaining a dispute"}
  - {verse: "Num 17:12", form: AS_WHEN, runner: korach, disposition: INTERNAL, link: reference, why: "THE NUMBERS WALK 5b (2026-09-10) | 'and Aaron took AS MOSES SPOKE' — 17:11's instruction (the censer, the fire from off the altar, the incense) run at 17:12 inside the span"}
  - {verse: "Num 17:26", form: AS_WHEN, runner: korach, disposition: INTERNAL, link: reference, why: "THE NUMBERS WALK 5b (2026-09-10) | 'and Moses did AS THE LORD COMMANDED him, so he did' — 17:25's command (return Aaron's staff before the testimony) run at 17:26 inside the span"}
  - {verse: "Num 15:24", form: AS_PRESCRIBED, runner: shelach, disposition: INTERNAL, link: reference,''')
# ---- the sequence runner: the import and the DAEMON_ORDER row ----
rep(f'{R}/cold_run_sequence.py', "import cold_run_shelach      # THE NUMBERS WALK 4b (2026-09-10): Shelach — the spies, the decree, the libations, the stranger, the challah, the error and the high hand; the 51st daemon law_shelach\n",
    "import cold_run_shelach      # THE NUMBERS WALK 4b (2026-09-10): Shelach — the spies, the decree, the libations, the stranger, the challah, the error and the high hand; the 51st daemon law_shelach\n"
    "import cold_run_korach       # THE NUMBERS WALK 5b (2026-09-10): Korach — the rebellion, the plague and the staffs, the priests' and the Levites' watch, gifts and tithe; the 52nd daemon law_korach\n")
rep(f'{R}/cold_run_sequence.py', "    ('cold_run_shelach', 'law_shelach'),         # THE NUMBERS WALK 4b (2026-09-10; NUMBERS_WALK.md \"Sitting 4b\"): Shelach — the spies, the decree, the libations, the stranger, the challah, the error, the high hand\n",
    "    ('cold_run_shelach', 'law_shelach'),         # THE NUMBERS WALK 4b (2026-09-10; NUMBERS_WALK.md \"Sitting 4b\"): Shelach — the spies, the decree, the libations, the stranger, the challah, the error, the high hand\n"
    "    ('cold_run_korach', 'law_korach'),           # THE NUMBERS WALK 5b (2026-09-10; NUMBERS_WALK.md \"Sitting 5b\"): Korach — the rebellion, the plague and the staffs, the watch, the gifts, the tithe\n")
print('patched: the parts, the registries, the dependency edges and pointers, the sequence runner')
