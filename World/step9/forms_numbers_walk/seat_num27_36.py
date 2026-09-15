import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE TENT sitting 4 (2026-09-09) — SEAT the claims of num_27_zelophehad_joshua_claims.json (NM27-01..11) and num_36_heiresses_claims.json
# (NM36-01..04) into their draft units as WITNESS_READ operators (sitting 3's rhythm, seat_num15.py: one operator per claim at its
# first verse's step, the [claim ID] marker in the prose, the cites the ledgers' own names), append derivation_log step E, and
# REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM before the ritual (sitting 2's lesson). Every cite is checked
# against the ledger's CITE INDEX before a byte is written; each yaml is re-loaded after.
import json, re, yaml
ROOT = _ROOT

def cite_index(ledger, pat):
    led = open(ledger, encoding='utf-8').read().split('## CITE INDEX')[1]
    return set(re.findall(pat, led, re.M))
CI27 = cite_index(f'{ROOT}/logic/oral_triage/num_27_zelophehad_joshua_2026-09-09.md', r'^(Sifrei Bamidbar \d+:\d+|Onkelos Num 27:\d+)$')
CI36 = cite_index(f'{ROOT}/logic/oral_triage/num_36_heiresses_2026-09-09.md', r'^(Onkelos Num 36:\d+)$') | \
       cite_index(f'{ROOT}/logic/oral_triage/num_36_heiresses_2026-09-09.md', r'^(Sifrei Bamidbar \d+:\d+) \(credited\)$')
assert len(CI27) == 46 and len(CI36) == 16, (len(CI27), len(CI36))

# (claim id, verse step, anchor, name, cites, prose)
SEATS27 = [
 ('NM27-01', 1, 'vatikravnah_benot_tzelofchad', 'the_approach_and_the_counsel',
  ['Sifrei Bamidbar 133:1', 'Sifrei Bamidbar 133:2', 'Onkelos Num 27:1'],
  "THE APPROACH AND THE COUNSEL [claim NM27-01]. The daughters heard the land was apportioned to the tribes and not to females "
  "and took counsel: not as the mercies of flesh and blood are the mercies of the Place — His are on all (Ps 145:9). The pedigree: "
  "as Zelophehad was a firstborn so all of them — worthy daughters of a worthy man; as Joseph held the land dear so they. THE "
  "NAMES' TWO ORDERS: 27:1 (with 26:33, Josh 17:3) against 36:11 — all equal. Onkelos: of the SEED-family of Manasseh. The feminine "
  "'and they drew near' stands at 27:1 and Josh 17:4 alone — the case and its run in the sixth book (computed)."),
 ('NM27-02', 2, 'vataamodnah_lifnei_moshe', 'the_standing_the_date_the_identity_arm',
  ['Sifrei Bamidbar 133:3', 'Onkelos Num 27:2', 'Onkelos Num 27:3'],
  "THE STANDING, THE DATE, THE IDENTITY ARM [claim NM27-02]. They STOOD (Onkelos: stood, where 9:8's men wait) at the door of the "
  "tent of meeting; dated by the roster — only in the fortieth year, the year Aaron died (33:38: Eleazar in the list). If Moses did "
  "not know, would Eleazar? invert the verse (R. Yoshiyah); the study house (Abba Chanin in R. Eliezer's name) — the halt's stage as "
  "at 9:6 and 15:33. R. AKIVA: 'wilderness' here and at 15:32 — the gatherer is Zelophehad: the identity arm's second seat, 113:1's "
  "rebuke standing, the registry's arm unassigned. The three congregations (the murmurers, the spies of 14:35, Korach's); 'in his "
  "own sin' — he led no one; Onkelos: in his DEBT."),
 ('NM27-03', 4, 'lamah_yigara_shem_avinu', 'the_plea_rides_the_levirates_word',
  ['Sifrei Bamidbar 133:4', 'Onkelos Num 27:4'],
  "THE PLEA RIDES THE LEVIRATE'S WORD [claim NM27-03]. R. Yehuda: 'name' here and 'name' at Deut 25:6 — as name there is inheritance "
  "so here, as name there is seed so here. 'Because he has no son' after 'he had no sons' — they were wise and expounded: had there "
  "been a son's daughter we would make no claim. R. Natan: the women's strength — 'let us make a head' (14:4) against 'give us a "
  "holding'. The plea's verb 'be held back' is the unclean men's (9:7) and the tribes' (36:3-4), computed; Onkelos's one idiom."),
 ('NM27-04', 5, 'vayakrev_moshe_et_mishpatan', 'the_halts_third_form_and_the_fourth_uncertainty',
  ['Sifrei Bamidbar 133:4', 'Onkelos Num 27:5'],
  "THE HALT'S THIRD FORM AND THE FOURTH UNCERTAINTY [claim NM27-04]. 'And Moses brought their judgment near before the LORD' — no "
  "guard (Lev 24:12, Num 15:34), no 'stand and I will hear' (9:8): the case CARRIED IN by Moses in the causative verb that brings the "
  "offerings near (computed); 'their judgment' once in the Tanakh (Onkelos: their CASE). R. Chidka from Shimon HaShikmoni: Moses KNEW "
  "that daughters inherit; the question was whether they inherit what is FIT (not yet possessed) as what is HELD — the uncertainty "
  "is the SCOPE. The section was fit to be said through Moses; the daughters merited it — merit through the meritorious."),
 ('NM27-05', 6, 'ken_benot_tzelofchad_dovrot', 'rightly_the_section_written_on_high_the_three_portions',
  ['Sifrei Bamidbar 134:1', 'Onkelos Num 27:6', 'Onkelos Num 27:7'],
  "RIGHTLY; THE SECTION WRITTEN ON HIGH; THE THREE PORTIONS [claim NM27-05]. The frame 'and the LORD SAID to Moses, SAYING' "
  "(computed: five Torah seats, the block's fourth frame form). 'Rightly do the daughters speak — for so is this section written "
  "before Me on high': the rule pre-exists the case; happy the man whose words the Place acknowledges (likewise 36:5, 14:20). 'Given "
  "shall be given' = their father's share; 'among their father's brothers' = Hepher's; 'pass over the inheritance' = the firstborn's "
  "double — THREE PORTIONS; R. Eliezer b. Akiva (the Hebrew; the English b. Yaakov): also the uncles' share. Onkelos: transfer at "
  "27:7 against give at 27:9-11."),
 ('NM27-06', 8, 'vehaavartem_et_nachalato_levito', 'the_generations_rule_and_the_orders_first_degrees',
  ['Sifrei Bamidbar 134:2', 'Onkelos Num 27:8'],
  "THE GENERATIONS' RULE AND THE ORDER'S FIRST DEGREES [claim NM27-06]. 'To the children of Israel speak' — the hour told, the "
  "generations from the address. In all the others GIVE, here PASS OVER (computed: the transfer verb at 27:8 alone) — Rebbi: only a "
  "daughter passes an inheritance, her son and husband inheriting her. THE FATHER PRECEDES THE BROTHERS (R. Yishmael b. R. Yose); "
  "the father inherits — a-fortiori from his brothers who come by his power; THE SON'S DAUGHTER AS THE SON — a-fortiori from the "
  "daughters who were only for the hour; females as males in every degree and males first — induction from sons and the redeemers "
  "(Lev 25:49). Onkelos: you shall TRANSFER his possession to his daughter."),
 ('NM27-07', 11, 'lisheero_hakarov_elav_veyarash_otah', 'the_last_degrees_the_wife_the_statute',
  ['Sifrei Bamidbar 134:2', 'Sifrei Bamidbar 134:3', 'Onkelos Num 27:9', 'Onkelos Num 27:10', 'Onkelos Num 27:11'],
  "THE LAST DEGREES, THE WIFE, THE STATUTE [claim NM27-07]. Give to his brothers, to his father's brothers, to his flesh nearest of "
  "his family — the FATHER'S family (1:2); the near in flesh first. THE HUSBAND INHERITS HIS WIFE — R. Akiva from 'of his family, and "
  "he shall inherit HER' (the feminine object; 'his flesh, the near' shared with Lev 21:2 alone, computed); R. Yishmael: from 36:8, "
  "36:7, Josh 24:33 (Phinehas's hill in Ephraim) and 1 Chr 2:22 (Yair's cities). 'A STATUTE OF JUDGMENT' — the Torah gave the sages "
  "knowledge to rank the near (Onkelos: a DECREE of judgment); the phrase at 27:11 and 35:29 alone (computed)."),
 ('NM27-08', 12, 'aleh_el_har_haavarim', 'moses_viewing_and_his_recorded_sin',
  ['Sifrei Bamidbar 134:4', 'Sifrei Bamidbar 134:5', 'Sifrei Bamidbar 135:1', 'Sifrei Bamidbar 136:1', 'Sifrei Bamidbar 136:2',
   'Sifrei Bamidbar 136:3', 'Sifrei Bamidbar 137:1', 'Sifrei Bamidbar 137:2', 'Onkelos Num 27:12', 'Onkelos Num 27:13', 'Onkelos Num 27:14'],
  "MOSES' VIEWING AND HIS RECORDED SIN [claim NM27-08]. Mount Abarim = Reuben's inheritance; Moses rejoiced at entering it, thinking "
  "the decree revoked, and poured out supplication — the Sifrei reads Deut 3:23-29 and 34:4 here, its own excursus: the requests "
  "refused one by one, the seeing granted (the third pass's material). 'As Aaron was gathered' — Moses desired that death. R. Shimon "
  "b. Elazar: Moses and Aaron died by KARET — 'because you did not sanctify Me' (Deut 32:51). Wherever a righteous one's death is "
  "told his sin is told (R. Eliezer HaModai). Onkelos: you refused My WORD; Kadesh = Rekem."),
 ('NM27-09', 15, 'yifkod_yhwh_elohei_haruchot', 'the_request_for_a_leader',
  ['Sifrei Bamidbar 138:1', 'Sifrei Bamidbar 139:1', 'Sifrei Bamidbar 139:2', 'Onkelos Num 27:15', 'Onkelos Num 27:16', 'Onkelos Num 27:17'],
  "THE REQUEST FOR A LEADER [claim NM27-09]. The righteous, about to die, set aside their own concerns for the congregation's; 'TO "
  "SAY' — tell me whether You appoint leaders: R. Eliezer b. Azaryah's four 'to say' requests each answered. 'God of the spirits' — "
  "all spirits from Him; the living soul in its Owner's hand, at death in the treasury. 'A man over the congregation' = Joshua "
  "(Ps 78:25), unnamed lest strife rise between Moses' sons and his brother's sons. 'Who goes out before them' — at the head, in a "
  "troop, on the way, in his merits, WITH A COUNT (31:49). Onkelos: let the LORD APPOINT."),
 ('NM27-10', 18, 'kach_lekha_et_yehoshua', 'the_commission',
  ['Sifrei Bamidbar 140:1', 'Sifrei Bamidbar 140:2', 'Sifrei Bamidbar 141:1', 'Onkelos Num 27:18', 'Onkelos Num 27:19', 'Onkelos Num 27:20', 'Onkelos Num 27:21'],
  "THE COMMISSION [claim NM27-10]. 'Take for YOURSELF' — whom you know worthy (Prov 27:18); 'a man in whom there is spirit' — who "
  "bears each one's spirit (Onkelos: of PROPHECY); 'lay your HAND' (singular, computed against 27:23) — give him an interpreter to "
  "ask, expound and RULE in your lifetime, raised to the bench; 'OF your glory' — not all: Moses' face as the sun, Joshua's as the "
  "moon; 'stand him before Eleazar'; 'inquire by the judgment of the Urim' — not between himself and himself, not aloud: lips "
  "moving, the high priest answering; 'by his mouth they go out and come in' (Onkelos: by his WORD — the court's oracle)."),
 ('NM27-11', 22, 'vayismokh_et_yadav_alav', 'the_investiture_run',
  ['Sifrei Bamidbar 141:2', 'Sifrei Bamidbar 141:3', 'Onkelos Num 27:22', 'Onkelos Num 27:23'],
  "THE INVESTITURE RUN [claim NM27-11]. Moses did it WITH JOY, no regret for his son or his brother's sons; took Joshua with words — "
  "the leaders' reward in the world to come; 'he laid his HANDS' (plural — the run exceeds the command's one hand, computed) — a "
  "full and overflowing vessel (Exod 33:11, Josh 1:8); commanded him as the LORD spoke by the hand of Moses — with joy; Moses' powers "
  "unwaned (Deut 34:7). THE OFFICE INSTALLED by the hand-laying in the master's lifetime — the leadership's installing act, owed "
  "forward to Deut 34:9's second seat and the sixth book."),
]
SEATS36 = [
 ('NM36-01', 1, 'vayikrevu_rashei_haavot', 'the_tribes_plea',
  ['Onkelos Num 36:1', 'Onkelos Num 36:2', 'Onkelos Num 36:3', 'Onkelos Num 36:4'],
  "THE TRIBES' PLEA [claim NM36-01]. The heads of the fathers of Gilead DREW NEAR (the unclean men's verb, 9:6, computed) and spoke "
  "before Moses and the princes: the LORD commanded my lord to give the land by LOT, and my lord was commanded by the LORD (Onkelos: "
  "by the Word) to give Zelophehad's inheritance to his daughters — the tribes cite the first output as standing law; if they marry "
  "into another tribe our inheritance shall be DIMINISHED (the three pleas' verb, 9:7 / 27:4 / 36:3-4; Onkelos's one idiom) and added "
  "to the other tribe's; 'and if the JUBILEE be' — even the release does not return it (the word's ninth Torah seat, computed: a "
  "reference to the release engine)."),
 ('NM36-02', 5, 'vayetzav_moshe_al_pi_yhwh', 'the_second_outputs_frame_and_the_thing',
  ['Sifrei Bamidbar 134:1', 'Onkelos Num 36:5', 'Onkelos Num 36:6'],
  "THE SECOND OUTPUT'S FRAME AND THE THING [claim NM36-02]. 'And Moses COMMANDED the children of Israel BY THE MOUTH OF THE LORD, "
  "saying' — no 'and the LORD said': the output relayed in Moses' mouth (the phrase's eighteen Torah seats, Lev 24:12's halt among "
  "them, computed); 'RIGHTLY the tribe of the sons of Joseph speak' — 27:7's word, the Sifrei's pair. 'THIS IS THE THING that the "
  "LORD commanded' (the formula's eight Torah seats); 'as is good in their eyes they shall be wives' (Onkelos: to whoever is "
  "FITTING) — the permission; 'ONLY to the family of their father's tribe' — the limit."),
 ('NM36-03', 7, 'velo_tisov_nachalah', 'the_transfer_barred_the_cleaving_the_daughters_inheritance',
  ['Sifrei Bamidbar 134:2', 'Onkelos Num 36:7', 'Onkelos Num 36:8', 'Onkelos Num 36:9'],
  "THE TRANSFER BARRED, THE CLEAVING, THE DAUGHTER'S INHERITANCE [claim NM36-03]. 'An inheritance shall not GO AROUND from tribe to "
  "tribe' (Onkelos: circulate); 'each man to his fathers' tribe's inheritance shall the children of Israel CLEAVE' — Gen 2:24's verb "
  "(computed). 'Every daughter who inherits an inheritance from the tribes' — the daughter inherits her MOTHER (Sifrei 134:2); with "
  "36:7 the route R. Yishmael takes to the husband's inheritance (Phinehas's hill, Yair's cities). 36:9 repeats the bar with "
  "'ANOTHER tribe'."),
 ('NM36-04', 10, 'kaasher_tzivah_yhwh_ken_asu', 'the_execution_and_the_colophon',
  ['Sifrei Bamidbar 133:2', 'Onkelos Num 36:10', 'Onkelos Num 36:11', 'Onkelos Num 36:12', 'Onkelos Num 36:13'],
  "THE EXECUTION AND THE COLOPHON [claim NM36-04]. 'As the LORD commanded Moses, SO DID the daughters' — the report formula of Lev "
  "24:23 and Num 15:36 on the fourth case: the execution is the daughters' own marriage. 'Mahlah, TIRZAH, Hoglah, Milcah and NOAH' — "
  "the second order (computed against 26:33, 27:1, Josh 17:3; the Sifrei: all equal); 'to the sons of their UNCLES' (Onkelos: their "
  "father's brothers); 'their inheritance REMAINED on the tribe of their father's family' — the ledger's close in the ink. 36:13: 'in "
  "the plains of Moab' — Deut 1:5's site (computed): the book closes where the third pass opens."),
]

def wrap(prose, indent=10):
    words = prose.split(' ')
    lines, cur = [], ''
    for w in words:
        if len(cur) + len(w) + 1 > 78 - indent and cur:
            lines.append(cur); cur = w
        else:
            cur = (cur + ' ' + w) if cur else w
    lines.append(cur)
    return '\n'.join(' ' * indent + l for l in lines)
def q(s): return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

def seat(uid, ch, seats, ci, manifest, stepE, nsteps, last_verse):
    unit = f'{ROOT}/logic/units/{uid}.yaml'
    claims = {c['id']: c for c in json.load(open(manifest, encoding='utf-8'))}
    assert len(claims) == len(seats)
    for cid, step, anchor, name, cites, prose in seats:
        assert cid in claims, cid
        for c in cites: assert c in ci, (cid, c)
        assert re.fullmatch(r'[\w-]+', anchor) and re.fullmatch(r'[\w-]+', name), (anchor, name)
        assert f'[claim {cid}]' in prose
    txt = open(unit, encoding='utf-8').read()
    assert 'operators:' not in txt, 'the draft already carries operators'
    by_step = {}
    for cid, step, anchor, name, cites, prose in seats:
        by_step.setdefault(step, []).append((anchor, name, cites, prose))
    for step, ops in by_step.items():
        sid = f'  - id: STEP_Nm_{ch}_{step}\n'
        i = txt.index(sid)
        j = txt.index('    comment: >\n', i)
        nxt = txt.find(f'\n  - id: STEP_Nm_{ch}_', i + 1)
        assert nxt == -1 or j < nxt, step
        block = '    operators:\n'
        for anchor, name, cites, prose in ops:
            block += ('      - op: WITNESS_READ\n'
                      f'        expr_en: "WITNESS-READ({anchor}, {name})"\n'
                      '        en: >\n' + wrap(prose) + '\n'
                      '        cites: [' + ', '.join(q(c) for c in cites) + ']\n'
                      '        confidence: witnessed\n')
        txt = txt[:j] + block + txt[j:]
    k = txt.index('\nboot_steps:\n')
    txt = txt[:k] + stepE + txt[k:]
    # THE SCENARIOS to the frozen anchor form (sitting 2's lesson: the ritual's honest FAIL, now done before it)
    a = txt.index('\nscenarios:\n'); b = txt.index('\nbinary_trees:', a)
    scen = '\nscenarios:\n'
    for n in range(1, 7):
        scen += f'  - id: S{n}\n    title_en: "after STEP_Nm_{ch}_{n} — Num {ch}:{n}"\n    expect_en: "no test, no name."\n'
    scen += f'  - id: S_last\n    title_en: "after STEP_Nm_{ch}_{last_verse} — Num {ch}:{last_verse}"\n    expect_en: "no test, no name."\n'
    txt = txt[:a] + scen + txt[b:]
    open(unit, 'w', encoding='utf-8').write(txt)
    d = yaml.safe_load(open(unit, encoding='utf-8'))
    ops = [(s['id'], o) for s in d['boot_steps'] for o in s.get('operators', [])]
    assert len(ops) == len(seats) and all(o['op'] == 'WITNESS_READ' for _, o in ops), len(ops)
    assert d['derivation_log'][-1]['step'] == 'E' and len(d['boot_steps']) == nsteps
    assert [s['id'] for s in d['scenarios']] == [f'S{n}' for n in range(1, 7)] + ['S_last'] and all(s['expect_en'] == 'no test, no name.' for s in d['scenarios'])
    print(f'{uid}: seated {len(ops)} operators on {len(by_step)} steps {sorted(by_step)}; scenarios {len(d["scenarios"])} in the anchor form')

STEP_E27 = '''
  - step: E
    name_en: "Numbers 27:1-23 derivation 2026-09-09 — THE TENT sitting 4"
    comment: >
      The third Numbers reading: the Sifrei on Numbers as the spine
      (piskaot 133-141 by position, 23 rows — its excursus on Moses'
      plea inside) with Onkelos 27:1-23, read whole and fresh (ledger
      num_27_zelophehad_joshua_2026-09-09.md, coverage computed by
      script, the ink facts computed from the Tanakh DB). Seated as
      claims NM27-01..11: the approach and the counsel; the standing,
      the date by the roster, the identity arm's second seat; the plea
      on the levirate's word; the halt's third form and the fourth
      uncertainty (the scope); rightly, the section written on high,
      the three portions; the generations' rule and the order's first
      degrees; the last degrees, the wife, the statute; Moses' viewing
      and his recorded sin; the request for a leader; the commission;
      the investiture run (the office installed, owed forward). The
      case's compile (the inheritance order), the loop's cursor and
      scenarios, and the tent's fourth case on the tape follow in the
      same sitting (THE_TENT.md section 4).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
STEP_E36 = '''
  - step: E
    name_en: "Numbers 36:1-13 derivation 2026-09-09 — THE TENT sitting 4"
    comment: >
      The fourth Numbers reading: Onkelos 36:1-13 whole and fresh — the
      Sifrei on Numbers ends at 35:29 (computed: no piska on chapter
      36), its three rows on 36:5-11 credited from the same sitting's
      27 ledger (ledger num_36_heiresses_2026-09-09.md, coverage
      computed by script, the ink facts computed from the Tanakh DB).
      Seated as claims NM36-01..04: the tribes' plea (the first output
      cited as standing law, the jubilee reached); the second output's
      frame (Moses commanding by the mouth of the LORD) and the thing;
      the transfer barred, the cleaving, the daughter's inheritance;
      the execution (the daughters' own marriage, the names' second
      order) and the colophon (the plains of Moab). The second output
      on the same case joins the tape in the same sitting
      (THE_TENT.md section 4).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
seat('num_27_zelophehad_joshua', 27, SEATS27, CI27, f'{ROOT}/logic/oral_audit/manifests/num_27_zelophehad_joshua_claims.json', STEP_E27, 23, 23)
seat('num_36_heiresses', 36, SEATS36, CI36, f'{ROOT}/logic/oral_audit/manifests/num_36_heiresses_claims.json', STEP_E36, 13, 13)
