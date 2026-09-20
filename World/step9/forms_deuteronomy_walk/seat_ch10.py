import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 8 — CHAPTER 10 (2026-09-19, the one run): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch10.py <uid>.
# Sitting 7's form (seat_ch9.py).
import subprocess
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-19'
UID = sys.argv[1]
SPEC = {
 'deu_10_second_tablets': (10, 1, 22, [('DV10-01', 1, 'the_second_tablets_and_the_ark', 'hew_two_tablets_like_the_first_make_an_ark_of_wood_the_ten_words_written_the_tablets_in_the_ark_as_commanded'), ('DV10-06', 5, 'the_retelling_on_the_tape', 'the_ark_the_stations_the_levites_the_third_forty_the_laws_restated_the_receipts_owed_to_the_compile'), ('DV10-02', 6, 'the_stations_aarons_death_the_levites', 'beeroth_bene_jaakan_to_moserah_eleazar_in_his_stead_the_tribe_of_levi_separated_the_lord_his_inheritance'), ('DV10-03', 10, 'the_third_forty_and_the_command_to_go', 'forty_days_as_the_first_the_lord_hearkened_arise_go_before_the_people'), ('DV10-04', 12, 'what_the_lord_asks', 'to_fear_to_walk_to_love_to_serve_to_keep_the_heavens_his_the_fathers_chosen_the_foreskin_of_the_heart'), ('DV10-05', 17, 'the_god_of_gods', 'no_face_lifted_no_bribe_the_orphan_the_widow_the_stranger_fear_serve_cleave_swear_seventy_souls_to_the_stars')], 'the second tablets and the ark, the stations and the Levites, the third forty, what the LORD asks, the God of gods and the stranger, the seventy to the stars'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 8, chapter 10"
    comment: >
      The book's eighth reading, at the chapter's grain (chapter 10 as one
      draft — {WHAT}), ONE run under the two-run rule and every row whole
      under the whole-row rule: Onkelos Deuteronomy {CH}:{LO}-{HI} whole and
      fresh (the export's twenty-two rows the DB's twenty-two — the
      identity, asserted); THE SIFREI ON DEUTERONOMY SILENT ON THE CHAPTER
      (no piska head between 36 on 6:9 and 37 on 11:10) — its three rows
      outside any piska citing chapter 10 read whole in both files (act
      from love against the fearer's seat 10:20; the seventy of 10:22 as
      "few" and against the hundred and forty nations; two read before and
      reread whole), the kin's spine (Exodus 34:1-4 and 28-29, 25:10-22,
      37:1-9, 31:18; Numbers 33:30-39, 20:22-29, 3:5-13, 8:5-26, 18:20-24;
      Exodus 22, 23; Leviticus 19) credited by name from the Exodus,
      Leviticus and Numbers ledgers. Ledger deu_10_ekev_{DATE}.md, coverage
      computed by script, the ink facts computed from the Tanakh DB and the
      snapshot store (every fact an assert — eight fell on the first typed
      pass, forms not facts, retyped from the print), the engine's numeral
      parser measured on every verse (five number verses — the two tablets
      [2] and [2, 2], the ten words [10] with the ordinal [1], the forty days
      [40, 40], the seventy [70]; "swear" no number; the plural "first" no
      ordinal; no gap), no written/read pair in the chapter, every quotation
      cut by consonants (no miss). Seated as claims
      {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the readback's rows of the ark and the second tablets
      against Exodus 34, 25, 37 and 40 — the fragments in the ark; the
      stations and Aaron's death against Numbers 33 and 20; the Levites; the
      third forty on the clock; the laws restated by CALL; the receipt seats
      10:5 and 10:9) follows in its own sitting (World/step9/DEUTERONOMY_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_10_ekev_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
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
