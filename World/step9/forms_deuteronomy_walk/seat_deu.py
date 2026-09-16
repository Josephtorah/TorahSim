import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 1 — THE OPENING SPEECH (2026-09-15): SEAT the claims of the six manifests into the six draft units as WITNESS_READ
# operators (sitting 9's rhythm: one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's
# own names), append derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses +
# its last) before the ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after.
# The prose is the manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v> (the Numbers
# walk's STEP_Dt_ regex changed — the one-line lesson of the form). Usage: seat_deu.py <uid>. Sitting 15's form (seat_ref.py).
import subprocess
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-15'
UID = sys.argv[1]
SPEC = {
 'deu_01_frame_officers': (1, 1, 18, [('DV01A-01', 1, 'the_frame_beyond_the_jordan', 'the_places_the_date_the_receipt_the_explaining'), ('DV01A-02', 6, 'horeb_enough_at_this_mountain', 'turn_and_journey_to_the_euphrates'), ('DV01A-03', 9, 'i_cannot_bear_you_alone', 'give_yourselves_wise_men'), ('DV01A-04', 14, 'the_officers_appointed', 'captains_of_thousands_hundreds_fifties_tens'), ('DV01A-05', 16, 'the_judges_charged', 'the_judgment_is_gods')], 'the frame and the officers (1:1-18)'),
 'deu_01_spies_refuse': (1, 19, 46, [('DV01B-01', 19, 'the_spies_sent', 'twelve_men_to_eshcol'), ('DV01B-02', 26, 'the_refusal', 'you_murmured_in_your_tents'), ('DV01B-03', 34, 'the_oath', 'none_of_this_evil_generation_but_caleb'), ('DV01B-04', 41, 'the_presumptuous_ascent', 'beaten_down_to_hormah')], 'the spies and the refusal (1:19-46)'),
 'deu_02_bypass_nations': (2, 1, 25, [('DV02A-01', 1, 'seir_passed', 'contend_not_with_esau'), ('DV02A-02', 9, 'moab_passed_and_the_emim', 'thirty_eight_years_to_the_zered'), ('DV02A-03', 16, 'ammon_passed_and_the_zamzummim', 'the_lord_spoke_to_me'), ('DV02A-04', 24, 'the_arnon_crossed', 'the_dread_of_you_on_the_peoples')], 'the bypass of the nations (2:1-25)'),
 'deu_02_sihon': (2, 26, 37, [('DV02B-01', 26, 'the_embassy_refused', 'words_of_peace_from_kedemoth'), ('DV02B-02', 31, 'sihon_smitten', 'jahaz_and_the_ban')], 'Sihon (2:26-37)'),
 'deu_03_og_gilead': (3, 1, 22, [('DV03A-01', 1, 'og_smitten', 'sixty_cities_of_argob'), ('DV03A-02', 8, 'the_land_taken_the_names_the_bed', 'nine_cubits_by_the_cubit_of_a_man'), ('DV03A-03', 12, 'the_east_given', 'reuben_gad_and_half_manasseh'), ('DV03A-04', 18, 'the_armed_passage_and_joshua_told', 'until_the_lord_gives_rest')], 'Og and the east (3:1-22)'),
 'deu_03_moses_barred': (3, 23, 29, [('DV03B-01', 23, 'the_plea', 'let_me_cross_and_see_the_good_land'), ('DV03B-02', 26, 'the_refusal_and_the_charge', 'go_up_pisgah_charge_joshua')], 'Moses barred (3:23-29)'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 1, the opening speech"
    comment: >
      The book's first reading, at the parashah grain (the portion Devarim's
      three chapters as six drafts — this unit {WHAT}): Onkelos Deuteronomy
      {CH}:{LO}-{HI} whole and fresh; THE SIFREI ON DEUTERONOMY found BY
      POSITION — piskaot 1-25 on 1:1-1:28 and 26-30 on 3:23-3:29 (147 rows,
      the two files' grains equal, each read in both files; no piska on
      1:29-3:22), seven rows of other piskaot citing the chapters credited
      with a quick look, six rows read before by topic in Genesis ledgers
      named. Ledger deu_01_03_devarim_{DATE}.md (one ledger for the six
      drafts), coverage computed by script, the ink facts computed from the
      Tanakh DB and the snapshot store (every fact an assert — the fallen ones
      retyped from the leg prints, none on the last pass), the engine's
      numeral parser measured on every verse (eleven number verses read, no
      gap; the fraction class named), every quotation cut by consonants (no
      cut miss; the lint 0). Seated as claims {ids[0]}..{ids[-1][-2:]}:
      {'; '.join(TITLES[i].lower() for i in ids)}. The compile (the speech's
      retellings against Numbers as the tape's own memory; the officers'
      table; the judges' charge; the two islands of the Sifrei; the register
      gate's four waiting seats) follows in its own sitting
      (World/step9/DEUTERONOMY_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_01_03_devarim_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
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
