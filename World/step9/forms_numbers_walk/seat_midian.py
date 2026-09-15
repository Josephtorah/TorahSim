import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 11 — MIDIAN (2026-09-12): SEAT the claims of the manifest into the draft unit as WITNESS_READ operators (sitting 9's
# rhythm, seat_offerings.py: one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own
# names), append derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its
# last) before the ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The
# prose is the manifest's own claim_en, so the operator and the claim cannot drift apart. Usage: seat_midian.py num_31_midian
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-12'
UID = sys.argv[1]
SPEC = {
 'num_31_midian': (31, 1, 54, [('MT31A-01', 1, 'avenge_the_vengeance_from_the_midianites', 'the_command_and_its_run_share_the_word'), ('MT31A-02', 3, 'a_thousand_to_a_tribe_and_phinehas', 'the_trumpets_one_narrative_seat'), ('MT31A-03', 7, 'the_war_and_the_five_kings', 'balaam_by_the_sword_the_first_receipt'), ('MT31A-04', 9, 'the_spoil_brought_to_moses', 'the_booty_nouns_and_the_plains_of_moab'), ('MT31A-05', 13, 'moses_was_wroth_with_the_officers', 'the_word_of_balaam_and_the_plague'), ('MT31A-06', 17, 'kill_the_women_who_knew_a_man', 'jabesh_gilead_runs_the_sentence'), ('MT31A-07', 19, 'seven_days_and_the_heifers_water', 'eleazar_speaks_the_statute_the_six_metals'), ('MT31A-08', 25, 'halve_the_prey_and_levy_the_tribute', 'one_of_five_hundred_one_of_fifty'), ('MT31A-09', 32, 'the_census_of_the_spoil_and_the_tribute', 'the_arithmetic_exact'), ('MT31A-10', 42, 'the_congregations_half_and_the_levites', 'the_share_never_written'), ('MT31A-11', 48, 'the_officers_gold_none_missing', 'the_ransom_of_exodus_30_run_at_a_count')],
   'Midian (31:1-54)'),
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
    name_en: "Numbers {CH}:{LO}-{HI} derivation {DATE} — THE NUMBERS WALK sitting 11, Midian"
    comment: >
      The walk's eleventh reading, at the parashah grain (the portion Matot's
      second chapter as one draft — {WHAT}; the next draft opens at 32:1):
      Onkelos Numbers {CH}:{LO}-{HI} whole and fresh; the Sifrei on Numbers
      piskaot found BY POSITION (two on the chapter, twelve rows, every head
      checked against its rows' own citations; NO row from 31:25 to 35:8 —
      the shelf silent on the division, the tribute, the census of the spoil
      and the officers' gold; the rows' own defects read to their verses in
      both files — an arm reversed, an ancestor inserted, a rule about rules
      dropped, RESEARCH_LOG.md). Ledger {UID}_{DATE}.md, coverage computed by
      script, the ink facts computed from the Tanakh DB and the snapshot store
      (every fact an assert — fourteen fell on the first typed pass and one on
      the second, each retyped from the leg print), every number by the
      engine's own numeral parser (right on the spoil's census, the halves, the
      tributes and the shekels; silent on the ratio's denominator at 31:28, 30,
      47 — the fraction class named and left for the compile), every quotation
      cut by consonants in glossed pieces (no cut miss). Seated as claims
      {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the Midian debit closed at 31:7 by the receipt, Balaam's
      death closing the ass's sword clause, the trumpets' debit run at 31:6,
      the heifer's water by CALL, the fire-passing rule, the division and the
      tribute as computed cells with the fraction class taught to the parser,
      the officers' gold by CALL into the half-shekel engine, the register
      gate's eight seats paid) follows in its own sitting
      (World/step9/NUMBERS_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/{UID}_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
ci = set(re.findall(r'^(Sifrei Bamidbar \d+:\d+|Onkelos Num \d+:\d+)$', led, re.M))
assert len(claims) == len(SEATS) == 11 and set(claims) == {s[0] for s in SEATS}, (sorted(claims), SEATS)
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
