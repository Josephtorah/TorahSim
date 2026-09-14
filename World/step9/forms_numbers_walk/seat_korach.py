#!/usr/bin/env python3
# THE NUMBERS WALK sitting 5 — KORACH (2026-09-10): SEAT the 30 claims of the three manifests into their draft units as WITNESS_READ
# operators (sitting 4's rhythm, seat_shelach.py: one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose,
# the cites the ledgers' own names), append derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM
# (the unit's first six verses + its last) before the ritual. Every cite is checked against the ledger's CITE INDEX before a byte is
# written; each yaml is re-loaded after. The prose is the manifest's own claim_en, so the operator and the claim cannot drift apart.
import json, re, yaml
ROOT = '<repo-old>'
DATE = '2026-09-10'
UNITS = [  # (uid, chapter, lo, hi, [(claim id, step verse, anchor, name)])
 ('num_16_korach', 16, 1, 35, [('KR16A-01', 1, 'and_korach_took', 'no_object_izhar_is_fresh_oil_the_shelf_silent'), ('KR16A-02', 3, 'too_much_for_you', 'returned_the_shekhinah_moses_alone_the_holy_one'),
                               ('KR16A-03', 9, 'is_it_too_little', 'the_high_priesthood_gathered_against_defective'), ('KR16A-04', 12, 'we_will_not_go_up', 'milk_and_honey_of_egypt_lording_the_eyes'),
                               ('KR16A-05', 15, 'it_was_hot_to_moses', 'the_cain_echo_not_one_ass_samuels_run'), ('KR16A-06', 17, 'each_his_censer', 'nadabs_phrase_250_censers_the_glory'),
                               ('KR16A-07', 21, 'separate_yourselves', 'one_aramaic_verb_god_of_the_spirits_the_dwelling'), ('KR16A-08', 26, 'turn_aside_i_pray', 'sodoms_verbs_by_this_you_shall_know_balaams'),
                               ('KR16A-09', 30, 'a_creation_he_creates', 'cains_ground_ground_to_earth_korach_not_named'), ('KR16A-10', 35, 'fire_from_with_the_lord', 'the_parsers_gap_the_definite_numeral')]),
 ('num_17_plague_staff', 17, 1, 28, [('KR17A-01', 2, 'the_censers_from_the_burning', 'beaten_plates_the_stranger_defined'), ('KR17A-02', 6, 'you_have_killed', 'the_threat_repeated_one_aramaic_verb'),
                                     ('KR17A-03', 11, 'fire_from_off_the_altar', 'yom_kippurs_phrase_the_plague_stayed'), ('KR17A-04', 17, 'a_staff_a_staff', 'twelve_with_levi_among_them'),
                                     ('KR17A-05', 19, 'before_the_testimony', 'the_spellings_alternate_the_floods_verb'), ('KR17A-06', 23, 'it_blossomed_a_blossom', 'the_frontplates_word_almonds'),
                                     ('KR17A-07', 25, 'return_aarons_staff', 'the_manna_jars_formula_sons_of_rebellion'), ('KR17A-08', 27, 'we_expire_we_perish', 'the_translations_three_deaths')]),
 ('num_18_priest_levite_dues', 18, 1, 32, [('KR18A-01', 1, 'the_lord_said_to_aaron', 'five_seats_the_frontplates_levis_naming_verb'), ('KR18A-02', 4, 'a_stranger_shall_not_come_near', 'the_warning_the_punishment_no_more_wrath'),
                                           ('KR18A-03', 8, 'the_watch_of_my_terumah', 'through_moses_joy_the_deed_registered'), ('KR18A-04', 11, 'the_terumah_of_their_gift', 'the_betrothed_daughter_izhar_the_triad_reversed'),
                                           ('KR18A-05', 14, 'every_devoted_thing', 'the_four_way_dispute'), ('KR18A-06', 15, 'all_that_opens_the_womb', 'kerem_beyavneh_the_sela_and_the_maah'),
                                           ('KR18A-07', 17, 'the_firstborn_of_an_ox', 'one_application_two_days_and_a_night'), ('KR18A-08', 19, 'a_covenant_of_salt', 'aarons_and_davids'),
                                           ('KR18A-09', 20, 'i_am_your_portion', 'the_exclusions_the_gifts_the_crowns'), ('KR18A-10', 21, 'all_the_tithe_in_israel', 'in_exchange_the_levite_he'),
                                           ('KR18A-11', 26, 'a_tithe_from_the_tithe', 'the_threshing_floor_paid_the_thresholds'), ('KR18A-12', 30, 'its_best', 'in_every_place_the_wage_you_shall_not_die')]),
]
TITLES = {}
for uid, _, _, _, seats in UNITS:
    for c in json.load(open(f'{ROOT}/logic/oral_audit/manifests/{uid}_claims.json', encoding='utf-8')):
        TITLES[c['id']] = c['claim_en'].split('. ')[0].rstrip('.')

def wrap(prose, indent=10):
    lines, cur = [], ''
    for w in prose.split(' '):
        if len(cur) + len(w) + 1 > 78 - indent and cur: lines.append(cur); cur = w
        else: cur = (cur + ' ' + w) if cur else w
    lines.append(cur)
    return '\n'.join(' ' * indent + l for l in lines)
def q(s): return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

def seat(uid, ch, lo, hi, seats):
    unit = f'{ROOT}/logic/units/{uid}.yaml'
    led = open(f'{ROOT}/logic/oral_triage/{uid}_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
    ci = set(re.findall(r'^(Sifrei Bamidbar \d+:\d+|Onkelos Num \d+:\d+)$', led, re.M))
    claims = {c['id']: c for c in json.load(open(f'{ROOT}/logic/oral_audit/manifests/{uid}_claims.json', encoding='utf-8'))}
    assert len(claims) == len(seats) and set(claims) == {s[0] for s in seats}, (uid, sorted(claims), seats)
    txt = open(unit, encoding='utf-8').read()
    assert 'operators:' not in txt, 'the draft already carries operators'
    by_step = {}
    for cid, step, anchor, name in seats:
        assert lo <= step <= hi and re.fullmatch(r'[\w-]+', anchor) and re.fullmatch(r'[\w-]+', name), (cid, step, anchor, name)
        cites = claims[cid]['source'].split('; ')
        for c in cites: assert c in ci, (cid, c)
        prose = f"{TITLES[cid]} [claim {cid}]. {claims[cid]['claim_en']}"
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
    txt = txt[:k] + STEP_E(uid, ch, lo, hi, [s[0] for s in seats]) + txt[k:]
    a = txt.index('\nscenarios:\n'); b = txt.index('\nbinary_trees:', a)
    scen = '\nscenarios:\n'
    firsts = list(range(lo, min(lo + 6, hi + 1)))
    for n, v in enumerate(firsts, 1):
        scen += f'  - id: S{n}\n    title_en: "after STEP_Nm_{ch}_{v} — Num {ch}:{v}"\n    expect_en: "no test, no name."\n'
    scen += f'  - id: S_last\n    title_en: "after STEP_Nm_{ch}_{hi} — Num {ch}:{hi}"\n    expect_en: "no test, no name."\n'
    txt = txt[:a] + scen + txt[b:]
    open(unit, 'w', encoding='utf-8').write(txt)
    d = yaml.safe_load(open(unit, encoding='utf-8'))
    ops = [(s['id'], o) for s in d['boot_steps'] for o in s.get('operators', [])]
    assert len(ops) == len(seats) and all(o['op'] == 'WITNESS_READ' for _, o in ops), len(ops)
    assert d['derivation_log'][-1]['step'] == 'E' and len(d['boot_steps']) == hi - lo + 1
    assert [s['id'] for s in d['scenarios']] == [f'S{n}' for n in range(1, len(firsts) + 1)] + ['S_last'] and all(s['expect_en'] == 'no test, no name.' for s in d['scenarios'])
    print(f'{uid}: seated {len(ops)} operators on {len(by_step)} steps {sorted(by_step)}; scenarios {len(d["scenarios"])} in the anchor form')
    return len(ops)

def STEP_E(uid, ch, lo, hi, ids):
    sifrei = {'num_16_korach': 'the Sifrei on Numbers has NO PISKA on this chapter (computed on every head of the export) — the chapter read on the translation alone',
              'num_17_plague_staff': 'the Sifrei on Numbers has NO PISKA on this chapter (computed on every head of the export) — the chapter read on the translation alone',
              'num_18_priest_levite_dues': 'the Sifrei on Numbers piskaot 116-122 found BY POSITION (every head in order, none mistyped; the export\'s translator stops inside 121 — the shelf\'s gap, RESEARCH_LOG.md)'}[uid]
    return f'''
  - step: E
    name_en: "Numbers {ch}:{lo}-{hi} derivation {DATE} — THE NUMBERS WALK sitting 5, Korach"
    comment: >
      The walk's fifth reading, at the parashah grain (Korach 16:1-18:32;
      three ledgers per block): Onkelos Numbers {ch}:{lo}-{hi} whole and
      fresh; {sifrei}. Ledger {uid}_{DATE}.md, coverage computed by
      script, the ink facts computed from the Tanakh DB and the snapshot
      store (every fact an assert), every number by the engine's own
      numeral parser (measured again on this portion — the definite numeral
      at the head of a compound a new gap), every quotation cut by
      consonants, every narrative verb glossed by the store's own
      words.gloss. Seated as claims {ids[0]}..{ids[-1][-2:]}:
      {'; '.join(TITLES[i].lower() for i in ids)}. The compile (the
      stranger's law, the dues, the firstborn's redemption, the tithe of the
      tithe, the earth and the fire and the plague on the tape) follows in
      its own sitting (World/step9/NUMBERS_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
total = 0
for uid, ch, lo, hi, seats in UNITS: total += seat(uid, ch, lo, hi, seats)
assert total == 30, total
print(f'KORACH: {total} operators seated across {len(UNITS)} units')
