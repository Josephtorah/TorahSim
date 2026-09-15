import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 12 — GAD AND REUBEN (2026-09-12): SEAT the claims of the manifest into the draft unit as WITNESS_READ operators (sitting
# 9's rhythm, seat_offerings.py: one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own
# names), append derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its
# last) before the ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The
# prose is the manifest's own claim_en, so the operator and the claim cannot drift apart. Usage: seat_gad.py num_32_gad_reuben
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-12'
UID = sys.argv[1]
SPEC = {
 'num_32_gad_reuben': (32, 1, 42, [('MT32A-01', 1, 'much_cattle_and_a_place_for_cattle', 'the_request_for_the_land_of_jazer_and_gilead'), ('MT32A-02', 6, 'shall_your_brothers_go_to_war', 'the_hinder_root_the_vows_verb'), ('MT32A-03', 10, 'the_oath_of_chapter_14_retold', 'the_verb_swore_supplied'), ('MT32A-04', 14, 'a_brood_of_sinful_men', 'the_rebukes_own_condition'), ('MT32A-05', 16, 'folds_for_the_cattle_cities_for_the_little_ones', 'the_arm_root_and_the_retellings_rest'), ('MT32A-06', 20, 'the_condition_doubled_before_the_lord', 'the_clearance_and_the_utterance_rule'), ('MT32A-07', 25, 'your_servants_will_do_as_my_lord_commands', 'the_acceptance_in_moses_order'), ('MT32A-08', 28, 'eleazar_joshua_and_the_heads_charged', 'the_second_doubled_condition_and_the_lords_word'), ('MT32A-09', 33, 'the_grant_to_gad_reuben_and_half_manasseh', 'the_cities_built_and_renamed'), ('MT32A-10', 39, 'machir_jair_and_nobah_in_gilead', 'joseph_knees_and_the_daughter_towns')],
   'Gad and Reuben (32:1-42)'),
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
    name_en: "Numbers {CH}:{LO}-{HI} derivation {DATE} — THE NUMBERS WALK sitting 12, Gad and Reuben"
    comment: >
      The walk's twelfth reading, at the parashah grain (the portion Matot's
      third and last chapter as one draft — {WHAT}; the next draft opens at
      33:1): Onkelos Numbers {CH}:{LO}-{HI} whole and fresh; the Sifrei on
      Numbers found BY POSITION to have NO piska on the chapter (158 on 31:22
      is followed by 159 on 35:9 — the shelf silent from 31:25 to 35:8), the
      whole export scanned for a row citing the chapter: three rows of other
      chapters cite 32:1 and 32:37-38, credited with a quick look (read whole
      at sitting 3). Ledger {UID}_{DATE}.md, coverage computed by script, the
      ink facts computed from the Tanakh DB and the snapshot store (every fact
      an assert — ten fell on the first typed pass, each retyped from the leg
      print; one more on the second), the engine's numeral parser measured on
      every verse (two numbers, both read — no gap), every quotation cut by
      consonants in glossed pieces (no cut miss; the lint clean on the first
      write). Seated as claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the doubled condition as a conditional grant with both
      arms, the utterance rule's second seat by CALL into the vows' runner,
      the clearance before the LORD and before Israel, the oath's retelling
      against chapter 14's tape lines, the cities as entities, the release at
      Joshua 22 a run outside the Torah) follows in its own sitting
      (World/step9/NUMBERS_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/{UID}_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
ci = set(re.findall(r'^(Onkelos Num \d+:\d+)$', led, re.M))
assert len(claims) == len(SEATS) == 10 and set(claims) == {s[0] for s in SEATS}, (sorted(claims), SEATS)
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
