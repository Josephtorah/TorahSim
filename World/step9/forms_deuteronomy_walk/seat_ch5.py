#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 3 — CHAPTER 5 (2026-09-16): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch5.py <uid>.
# Sitting 2's form (seat_ch4.py).
import subprocess
import json, re, sys, yaml
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
DATE = '2026-09-16'
UID = sys.argv[1]
SPEC = {
 'deu_05_decalogue': (5, 1, 33, [('DV05-01', 1, 'the_covenant_at_horeb', 'not_with_our_fathers_face_to_face_i_stood_between'), ('DV05-02', 6, 'the_first_words', 'i_am_the_lord_no_other_gods_no_image_the_name'), ('DV05-03', 12, 'the_sabbath_word', 'keep_for_remember_the_slave_for_the_creation'), ('DV05-04', 16, 'honor_and_the_five', 'and_not_the_vain_witness_the_wife_first'), ('DV05-05', 22, 'the_voice_and_the_request', 'a_great_voice_added_no_more_we_will_hear_and_do'), ('DV05-06', 28, 'the_answer_and_the_charge', 'they_have_done_well_stand_here_with_me')], 'the second copy of the ten words with its frame (5:1-33)'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 3, chapter 5"
    comment: >
      The book's third reading, at the chapter's grain (chapter 5 as one
      draft — {WHAT}): Onkelos Deuteronomy {CH}:{LO}-{HI} whole and fresh
      through the map of the two divisions (the export's thirty rows against
      the DB's thirty-three — its 17 the DB's 17-20, computed by alignment);
      THE SIFREI ON DEUTERONOMY has NO PISKA on the chapter (30 on 3:29, 31
      on 6:4) — its six rows citing chapter 5 found by the scan of the whole
      export in both files, five read fresh (41:1, 41:4, 233:1, 306:16,
      357:40), one credited from sitting 1 (20:1). Ledger
      deu_05_vaetchanan_{DATE}.md, coverage computed by script, the ink
      facts computed from the Tanakh DB and the snapshot store (every fact
      an assert — three fell on the first typed pass, retyped from the leg
      print), the two copies of the ten words diffed verse by verse (172
      tokens against 189), the engine's numeral parser measured on every
      verse (three number verses read, the third generation starred, no
      gap), every quotation cut by consonants (no cut miss). Seated as
      claims {ids[0]}..{ids[-1][-2:]}:
      {'; '.join(TITLES[i].lower() for i in ids)}. The compile (the laws'
      readback — code graded against code, the second copy against the
      decalogue runner's cells; the receipts inside the ten words paying the
      register's seats 5:12, 5:16, 5:32; the written-and-read pair at 5:10)
      follows in its own sitting (World/step9/DEUTERONOMY_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_05_vaetchanan_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
ci = set(re.findall(r'^(Onkelos Deut \d+:\d+|Sifrei Devarim \d+:\d+)$', led, re.M))
assert len(claims) == len(SEATS) and set(claims) == {s[0] for s in SEATS}, (sorted(claims), SEATS)
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
    sid = f'  - id: STEP_Dt_{CH}_{step}\n'
    i = txt.index(sid)
    j = txt.index('    comment: >\n', i)
    nxt = txt.find(f'\n  - id: STEP_Dt_{CH}_', i + 1)
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
    scen += f'  - id: S{n}\n    title_en: "after STEP_Dt_{CH}_{v} — Deut {CH}:{v}"\n    expect_en: "no test, no name."\n'
scen += f'  - id: S_last\n    title_en: "after STEP_Dt_{CH}_{HI} — Deut {CH}:{HI}"\n    expect_en: "no test, no name."\n'
txt = txt[:a] + scen + txt[b:]
open(unit, 'w', encoding='utf-8').write(txt)
d = yaml.safe_load(open(unit, encoding='utf-8'))
ops = [(s['id'], o) for s in d['boot_steps'] for o in s.get('operators', [])]
assert len(ops) == len(SEATS) and all(o['op'] == 'WITNESS_READ' for _, o in ops), len(ops)
assert d['derivation_log'][-1]['step'] == 'E' and len(d['boot_steps']) == HI - LO + 1
assert [s['id'] for s in d['scenarios']] == [f'S{n}' for n in range(1, len(firsts) + 1)] + ['S_last'] and all(s['expect_en'] == 'no test, no name.' for s in d['scenarios'])
print(f'{UID}: seated {len(ops)} operators on {len(by_step)} steps {sorted(by_step)}; scenarios {len(d["scenarios"])} in the anchor form')
