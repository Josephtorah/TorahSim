import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 8 — THE SECOND CENSUS (2026-09-11): SEAT the 12 claims of the manifest into the draft unit as WITNESS_READ
# operators (sitting 7's rhythm, seat_balak.py: one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose,
# the cites the ledger's own names), append derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM
# (the unit's first six verses + its last) before the ritual. Every cite is checked against the ledger's CITE INDEX before a byte is
# written; the yaml is re-loaded after. The prose is the manifest's own claim_en, so the operator and the claim cannot drift apart.
import json, re, yaml
ROOT = _ROOT
DATE = '2026-09-11'
UID, CH, LO, HI = 'num_26_second_census', 26, 1, 65
SEATS = [('PN26A-01', 1, 'the_lord_said_to_moses_and_eleazar', 'the_command_shortened_the_verb_supplied_the_exodus_generation_named'),
         ('PN26A-02', 5, 'reuben_the_firstborn', 'the_plene_firstborn_the_family_form_hanoch_bare'),
         ('PN26A-03', 8, 'dathan_abiram_and_korach', 'the_pair_reversed_the_strive_verb_the_mouth_opened_the_pole_word_the_sons_who_did_not_die'),
         ('PN26A-04', 12, 'simeon_five_for_six', 'ohad_absent_nemuel_zerah_the_count_word_absent_the_fall_of_37100'),
         ('PN26A-05', 15, 'gad_judah_issachar_zebulun', 'zephon_the_north_word_ozni_jashub_er_and_onan_verbatim_judah_largest'),
         ('PN26A-06', 28, 'the_sons_of_joseph', 'manasseh_first_machir_begot_gilead_the_daughters_row'),
         ('PN26A-07', 35, 'ephraims_becher_benjamins_five', 'ten_to_five_ahiram_ard_and_naaman_a_generation_down'),
         ('PN26A-08', 42, 'dan_asher_naphtali', 'one_family_64400_the_imnah_without_yod_serah_on_three_rosters'),
         ('PN26A-09', 51, 'six_hundred_thousand_and_a_thousand', 'the_twelve_sum_the_deltas_simeons_gap'),
         ('PN26A-10', 52, 'the_land_by_count_and_by_lot', 'the_number_of_names_the_lots_mouth_the_sifreis_four_rows'),
         ('PN26A-11', 57, 'the_levites_five_for_eight', 'korahs_in_jochebed_subjectless_in_egypt_miriam_nadab_and_abihu_shortened'),
         ('PN26A-12', 63, 'the_two_rolls', 'the_membership_predicate_the_decrees_words_caleb_and_joshua_verbatim')]
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
    name_en: "Numbers 26:1-65 derivation {DATE} — THE NUMBERS WALK sitting 8, the second census"
    comment: >
      The walk's eighth reading, at the parashah grain (the portion Pinchas
      opens at 25:10, read with Balak's last draft on the draft's-grain rule;
      this draft is chapter 26 whole; chapter 27 is frozen at THE TENT and
      skipped when reached): Onkelos Numbers 26:1-65 whole and fresh (the
      export's 26:1 row carrying 25:19's head, read at sitting 7); the Sifrei
      on Numbers piska 132 found BY POSITION (four rows on 26:53-56; row 3's
      head mistyped "26:25" in the export and two citations inside the rows
      mistyped, read to their verses — RESEARCH_LOG.md; the piska quick-looked
      at THE TENT and read whole here; NO piska on 26:1-52 or 57-65, computed
      on every head). Ledger {UID}_{DATE}.md, coverage computed by script, the
      ink facts computed from the Tanakh DB and the snapshot store (every fact
      an assert — ten fell on the first typed pass, each a measurement), every
      number by the engine's own numeral parser (right at every number verse of
      the chapter, the twelve counts summing to the ink's 601,730 — no new gap),
      every quotation cut by consonants, the roster rows built from the tokens,
      every narrative verb glossed by the store's own words.gloss. Seated as
      claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the two censuses as tables with their deltas and the
      checkpoints the ink sets — Simeon's 13,100, the seventy's missing one at
      26:59; the land's two criteria; the Levite families; the membership
      predicate on the tape) follows in its own sitting
      (World/step9/NUMBERS_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/{UID}_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
ci = set(re.findall(r'^(Sifrei Bamidbar \d+:\d+|Onkelos Num \d+:\d+)$', led, re.M))
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
