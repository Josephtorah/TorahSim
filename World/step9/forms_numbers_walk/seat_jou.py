#!/usr/bin/env python3
# THE NUMBERS WALK sitting 13 — THE JOURNEYS (2026-09-12): SEAT the claims of the manifest into the draft unit as WITNESS_READ operators (sitting
# 9's rhythm, seat_offerings.py: one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own
# names), append derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its
# last) before the ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The
# prose is the manifest's own claim_en, so the operator and the claim cannot drift apart. Usage: seat_jou.py num_33_journeys
import json, re, sys, yaml
ROOT = '<repo-old>'
DATE = '2026-09-12'
UID = sys.argv[1]
SPEC = {
 'num_33_journeys': (33, 1, 56, [('MS33A-01', 1, 'these_are_the_journeys_by_the_hand_of_moses_and_aaron', 'moses_wrote_by_the_mouth_of_the_lord'), ('MS33A-02', 3, 'the_fifteenth_day_the_morrow_of_the_passover', 'the_judgments_on_their_gods_the_run_of_exodus_12'), ('MS33A-03', 5, 'from_rameses_to_the_wilderness_of_sinai', 'the_stations_retell_exodus_on_the_tokens'), ('MS33A-04', 16, 'kibroth_hattaavah_hazeroth_and_rithmah', 'the_spies_base_under_its_other_name'), ('MS33A-05', 19, 'the_seventeen_stations_named_nowhere_else', 'deuteronomy_10_in_another_order'), ('MS33A-06', 36, 'the_wilderness_of_zin_that_is_kadesh', 'mount_hor_in_the_edge_of_edom'), ('MS33A-07', 38, 'aaron_died_in_the_fortieth_year_the_fifth_month', 'the_tapes_own_marker_and_the_inks_checksum'), ('MS33A-08', 40, 'the_canaanite_king_of_arad_heard', 'the_hearing_after_aarons_death'), ('MS33A-09', 41, 'from_mount_hor_to_the_plains_of_moab', 'the_forty_two_on_the_inks_own_count'), ('MS33A-10', 50, 'drive_out_the_inhabitants_destroy_the_high_places', 'leviticus_26_curse_on_the_third_object'), ('MS33A-11', 54, 'inherit_the_land_by_lot', 'the_verbs_number_switching_inside_the_verse'), ('MS33A-12', 55, 'thorns_in_your_eyes_and_pricks_in_your_sides', 'the_negative_arm_run_back_reversed')],
   'the journeys (33:1-56)'),
}
CH, LO, HI, SEATS, WHAT = SPEC[UID]
claims = {c['id']: c for c in json.load(open(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json', encoding='utf-8'))}
TITLES = {cid: c['claim_en'].split('. ')[0].rstrip('.') for cid, c in claims.items()}

def wrap(prose, indent=10):
    lines, cur = [], ''
    for w in prose.split(' '):
        if len(cur) + len(w) + 1 > 78 - indent and cur: lines.append(cur); cur = w
        else: cur = (cur + ' ' + w) if cur else w
    lines.append(cur)
    return '\n'.join(' ' * indent + l for l in lines)
def q(s): return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

def STEP_E(ids):
    return f'''
  - step: E
    name_en: "Numbers {CH}:{LO}-{HI} derivation {DATE} — THE NUMBERS WALK sitting 13, the journeys"
    comment: >
      The walk's thirteenth reading, at the parashah grain (the portion Masei's
      first chapter as one draft — {WHAT}; the next draft opens at 34:1):
      Onkelos Numbers {CH}:{LO}-{HI} whole and fresh; the Sifrei on Numbers
      found BY POSITION to have NO piska on the chapter (158 on 31:22 is
      followed by 159 on 35:9 — the shelf silent from 31:25 to 35:8), the whole
      export scanned in both files for a row citing the chapter, the English
      "Ibid." and the Hebrew gershayim included: one row of another chapter
      cites 33:38 (133:3, dating the daughters), credited with a quick look
      (read whole at THE TENT sitting 4). Ledger {UID}_{DATE}.md, coverage
      computed by script, the ink facts computed from the Tanakh DB and the
      snapshot store (every fact an assert — fifteen fell on the first typed
      pass, each retyped from the leg print; none on the second), the engine's
      numeral parser measured on every verse (five number verses, every one
      read — 33:38's date the tape's own marker at 20:28; no gap), every
      quotation cut by consonants in glossed pieces (no cut miss; the lint
      clean on the first write). Seated as claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the forty-two stations as data or as markers — the design's
      question; 33:38-39's date and age against the tape's marker and Exodus
      7:7; the command to dispossess as the spec whose runs are Joshua's; the
      lot's rule by CALL into the second census; the negative arm as a data
      row) follows in its own sitting (World/step9/NUMBERS_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/{UID}_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
ci = set(re.findall(r'^(Onkelos Num \d+:\d+)$', led, re.M))
assert len(claims) == len(SEATS) == 12 and set(claims) == {s[0] for s in SEATS}, (sorted(claims), SEATS)
txt = open(unit, encoding='utf-8').read()
assert 'operators:' not in txt, 'the draft already carries operators'
by_step = {}
for cid, step, anchor, name in SEATS:
    assert LO <= step <= HI and re.fullmatch(r'[\w-]+', anchor) and re.fullmatch(r'[\w-]+', name), (cid, step, anchor, name)
    cites = claims[cid]['source'].split('; ')
    for c in cites: assert c in ci, (cid, c)
    prose = f"{TITLES[cid]} [claim {cid}]. {claims[cid]['claim_en']}"
    by_step.setdefault(step, []).append((anchor, name, cites, prose))
for step, ops in by_step.items():
    sid = f'  - id: STEP_Nm_{CH}_{step}\n'
    i = txt.index(sid)
    j = txt.index('    comment: >\n', i)
    nxt = txt.find(f'\n  - id: STEP_Nm_{CH}_', i + 1)
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
txt = txt[:k] + STEP_E([s[0] for s in SEATS]) + txt[k:]
a = txt.index('\nscenarios:\n'); b = txt.index('\nbinary_trees:', a)
scen = '\nscenarios:\n'
firsts = list(range(LO, min(LO + 6, HI + 1)))
for n, v in enumerate(firsts, 1):
    scen += f'  - id: S{n}\n    title_en: "after STEP_Nm_{CH}_{v} — Num {CH}:{v}"\n    expect_en: "no test, no name."\n'
scen += f'  - id: S_last\n    title_en: "after STEP_Nm_{CH}_{HI} — Num {CH}:{HI}"\n    expect_en: "no test, no name."\n'
txt = txt[:a] + scen + txt[b:]
open(unit, 'w', encoding='utf-8').write(txt)
d = yaml.safe_load(open(unit, encoding='utf-8'))
ops = [(s['id'], o) for s in d['boot_steps'] for o in s.get('operators', [])]
assert len(ops) == len(SEATS) and all(o['op'] == 'WITNESS_READ' for _, o in ops), len(ops)
assert d['derivation_log'][-1]['step'] == 'E' and len(d['boot_steps']) == HI - LO + 1
assert [s['id'] for s in d['scenarios']] == [f'S{n}' for n in range(1, len(firsts) + 1)] + ['S_last'] and all(s['expect_en'] == 'no test, no name.' for s in d['scenarios'])
print(f'{UID}: seated {len(ops)} operators on {len(by_step)} steps {sorted(by_step)}; scenarios {len(d["scenarios"])} in the anchor form')
