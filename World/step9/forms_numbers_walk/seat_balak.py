import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 7 — BALAK (2026-09-11): SEAT the 40 claims of the four manifests into their draft units as WITNESS_READ
# operators (sitting 6's rhythm, seat_chukat.py: one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose,
# the cites the ledgers' own names), append derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM
# (the unit's first six verses + its last) before the ritual. Every cite is checked against the ledger's CITE INDEX before a byte is
# written; each yaml is re-loaded after. The prose is the manifest's own claim_en, so the operator and the claim cannot drift apart.
import json, re, yaml
ROOT = _ROOT
DATE = '2026-09-11'
UNITS = [  # (uid, chapter, lo, hi, [(claim id, step verse, anchor, name)])
 ('num_22_balak_bilam_call', 22, 1, 41, [('BK22A-01', 1, 'the_plains_of_moab', 'the_last_camp_balak_saw_the_conquest'), ('BK22A-02', 3, 'moab_feared_and_loathed', 'the_sojourn_verb_the_mannas_verb_the_elders_of_midian'),
                                        ('BK22A-03', 5, 'messengers_to_pethor', 'aram_and_the_euphrates_the_locusts_clause_three_curse_roots'), ('BK22A-04', 7, 'divinations_in_their_hand', 'god_came_to_three_gentiles_the_lord_refuses'),
                                        ('BK22A-05', 14, 'the_second_embassy', 'the_honor_promised_the_house_of_silver_the_word_formula'), ('BK22A-06', 21, 'balaam_saddled_his_ass', 'the_akedahs_morning_the_satan_word_the_angel'),
                                        ('BK22A-07', 23, 'the_ass_saw_the_angel', 'three_seeings_the_sword_plene_the_foot'), ('BK22A-08', 28, 'the_mouth_opened', 'three_feet_the_plene_three_egypts_verb_the_sword'),
                                        ('BK22A-09', 31, 'the_eyes_uncovered', 'pharaohs_confession_the_formula_second'), ('BK22A-10', 36, 'balak_at_the_arnon', 'the_border_drawn_bamoth_baal_the_edge')]),
 ('num_23_oracles_1_2', 23, 1, 30, [('BK23A-01', 1, 'seven_altars', 'twenty_one_altars_every_altar'), ('BK23A-02', 3, 'stand_by_your_offering', 'the_chance_verb_the_word_in_the_mouth'),
                                    ('BK23A-03', 7, 'took_up_his_parable', 'the_parable_tellers_paid_el_eight'), ('BK23A-04', 9, 'a_people_that_dwells_alone', 'the_lepers_words_abrahams_dust_the_fourth_part'),
                                    ('BK23A-05', 11, 'what_have_you_done', 'the_formula_keep_only_its_edge_pisgah'), ('BK23A-06', 16, 'the_lord_met_balaam', 'god_is_not_a_man_samuel_over_agag'),
                                    ('BK23A-07', 21, 'the_shout_of_a_king', 'the_teruah_made_the_shekhinah_one_letter'), ('BK23A-08', 23, 'no_divination_in_jacob', 'the_serpents_word_the_lioness_and_the_lion'),
                                    ('BK23A-09', 25, 'neither_curse_nor_bless', 'the_top_of_peor_the_third_stand'), ('BK23A-10', 29, 'seven_altars_again', 'the_second_saying_verbatim')]),
 ('num_24_oracles_3_4', 24, 1, 25, [('BK24A-01', 1, 'no_more_divinations', 'samsons_clause_the_spirit_of_god'), ('BK24A-02', 3, 'the_utterance_of_balaam', 'davids_form_abrahams_vision_shaddai'),
                                    ('BK24A-03', 5, 'how_goodly_are_your_tents', 'psalm_84_the_aloes_the_land'), ('BK24A-04', 7, 'water_from_his_buckets', 'meribahs_many_waters_agag'),
                                    ('BK24A-05', 8, 'el_brings_him_out', 'one_letter_judahs_lion_isaacs_blessing_reversed'), ('BK24A-06', 10, 'balak_clapped', 'three_times_the_honor_revoked_the_formula_sixth'),
                                    ('BK24A-07', 14, 'i_will_counsel_you', 'the_fruit_at_31_16_the_end_of_days'), ('BK24A-08', 15, 'the_star_and_the_scepter', 'the_most_high_jeremiah_fuses_the_messiah'),
                                    ('BK24A-09', 18, 'edom_amalek_the_kenite', 'the_creations_verb_the_sela_closed_kayin'), ('BK24A-10', 23, 'ships_from_kittim', 'daniel_quotes_rome_the_retellings')]),
 ('num_25_peor_pinchas', 25, 1, 19, [('BK25A-01', 1, 'israel_dwelt_in_shittim', 'the_timber_the_spec_and_its_run_the_wine'), ('BK25A-02', 3, 'israel_yoked_itself', 'the_lids_word_hang_them_the_judges'),
                                     ('BK25A-03', 6, 'a_man_brought_near', 'the_offering_verb_the_door'), ('BK25A-04', 7, 'phinehas_rose', 'korachs_phrase_the_spear'),
                                     ('BK25A-05', 8, 'into_the_alcove', 'the_curse_skin_both_of_them_the_plague_stayed'), ('BK25A-06', 9, 'twenty_four_thousand', 'korachs_formula_simeons_fall'),
                                     ('BK25A-07', 10, 'turned_back_my_wrath', 'the_sotahs_zeal_word'), ('BK25A-08', 12, 'my_covenant_of_peace', 'everlasting_priesthood_aarons_verb_the_tense'),
                                     ('BK25A-09', 14, 'zimri_and_cozbi_named', 'zur_of_the_five_kings_the_peoples'), ('BK25A-10', 16, 'harass_the_midianites', 'hamans_title_the_broken_verse')]),
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
    sifrei = {'num_22_balak_bilam_call': 'the Sifrei on Numbers has NO PISKA on this chapter (computed on every head of the export) — the chapter read on the translation alone; 22:1 is Chukat\'s last verse, read with this draft on sitting 6\'s own rule',
              'num_23_oracles_1_2': 'the Sifrei on Numbers has NO PISKA on this chapter (computed on every head of the export) — the chapter read on the translation alone',
              'num_24_oracles_3_4': 'the Sifrei on Numbers has NO PISKA on this chapter (computed on every head of the export) — the chapter read on the translation alone',
              'num_25_peor_pinchas': 'the Sifrei on Numbers piska 131 found BY POSITION (five rows on 25:1-6 and 25:11-13; two citations inside row 2 mistyped in the export, read to their verses — RESEARCH_LOG.md); 25:10-19 is Pinchas\'s opening, read with this draft on the same rule; the Onkelos export joins 25:19 into its 26:1 — the row cut from that head'}[uid]
    return f'''
  - step: E
    name_en: "Numbers {ch}:{lo}-{hi} derivation {DATE} — THE NUMBERS WALK sitting 7, Balak"
    comment: >
      The walk's seventh reading, at the parashah grain (Balak 22:2-25:9 with
      the drafts' own edges; four ledgers per block): Onkelos Numbers
      {ch}:{lo}-{hi} whole and fresh; {sifrei}. Ledger {uid}_{DATE}.md,
      coverage computed by script, the ink facts computed from the Tanakh DB
      and the snapshot store (every fact an assert), every number by the
      engine's own numeral parser (measured again on this portion — the
      plene "three" a new gap, the calf's "about three thousand" found by
      the cross-check), every quotation cut by consonants, every narrative
      verb glossed by the store's own words.gloss. Seated as claims
      {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the curse-roots and the word-formula as data, the three
      stands on the tape, the plague and its count, Phinehas's covenant and
      the Midian command's debit) follows in its own sitting
      (World/step9/NUMBERS_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
total = 0
for uid, ch, lo, hi, seats in UNITS: total += seat(uid, ch, lo, hi, seats)
assert total == 40, total
print(f'BALAK: {total} operators seated across {len(UNITS)} units')
