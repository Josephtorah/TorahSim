#!/usr/bin/env python3
# THE NUMBERS WALK sitting 10 — THE VOWS (2026-09-12): SEAT the claims of the manifest into the draft unit as WITNESS_READ operators (sitting 9's
# rhythm, seat_offerings.py: one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own
# names), append derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its
# last) before the ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The
# prose is the manifest's own claim_en, so the operator and the claim cannot drift apart. Usage: seat_vows.py num_30_vows
import json, re, sys, yaml
ROOT = '<repo-old>'
DATE = '2026-09-12'
UID = sys.argv[1]
SPEC = {
 'num_30_vows': (30, 1, 17, [('MT30A-01', 1, 'the_receipt_and_the_heads_of_the_tribes', 'this_is_the_thing_no_divine_frame'), ('MT30A-02', 3, 'a_man_when_he_vows', 'the_doubled_oath_and_bond_he_shall_not_profane'), ('MT30A-03', 4, 'a_woman_in_her_fathers_house', 'silence_confirms_restraint_annuls_the_lord_forgives'), ('MT30A-04', 7, 'the_betrothed', 'the_utterance_of_her_lips_an_oath'), ('MT30A-05', 10, 'the_widow_and_the_divorcee', 'her_husbands_house_the_two_silences_the_caretaker'), ('MT30A-06', 14, 'the_affliction_oath', 'from_day_to_day_after_his_hearing_her_iniquity'), ('MT30A-07', 17, 'these_are_the_statutes', 'the_father_likened_to_the_husband')],
   'the vows (30:1-17)'),
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
    name_en: "Numbers {CH}:{LO}-{HI} derivation {DATE} — THE NUMBERS WALK sitting 10, the vows"
    comment: >
      The walk's tenth reading, at the parashah grain (the portion Matot's
      first chapter as one draft — {WHAT}; 30:1 the portion Pinchas's last
      verse, the calendar's closer, read with this draft by the draft's-grain
      rule; the next draft opens at 31:1): Onkelos Numbers {CH}:{LO}-{HI} whole
      and fresh; the Sifrei on Numbers piskaot found BY POSITION (four on the
      chapter, seventeen rows; none on 30:1 — 152:1's, credited; the rows' own
      defects read to their verses — the export's seventh mistyped head among
      them, RESEARCH_LOG.md). Ledger {UID}_{DATE}.md, coverage computed by script,
      the ink facts computed from the Tanakh DB and the snapshot store (every
      fact an assert — one fell on the first typed pass, an index typed from
      memory), every number by the engine's own numeral parser (no cardinal
      and no ordinal in the chapter; the three oath-tokens starred as refused
      homographs of the seven-stem — no gap), every quotation cut by
      consonants in glossed pieces (no cut miss). Seated as claims
      {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the vow as a ledger entry with its confirm/annul state
      machine; the day-of-hearing timer with its two recorded settings; the
      father's and the husband's authority tables; the affliction filter; the
      widow, the divorcee, the betrothed, the married; the delay ban by CALL
      to Deuteronomy's clock) follows in its own sitting
      (World/step9/NUMBERS_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/{UID}_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
ci = set(re.findall(r'^(Sifrei Bamidbar \d+:\d+|Onkelos Num \d+:\d+)$', led, re.M))
assert len(claims) == len(SEATS) == 7 and set(claims) == {s[0] for s in SEATS}, (sorted(claims), SEATS)
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
