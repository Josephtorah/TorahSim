#!/usr/bin/env python3
# THE TENT sitting 2 (2026-09-09) — SEAT the eleven claims of num_09_pesach_cloud_claims.json into the draft unit
# logic/units/num_09_pesach_cloud.yaml as WITNESS_READ operators (the Emor rhythm: one operator per claim at its verse's
# step, the [claim ID] marker in the prose, the cites the ledger's own names), and append derivation_log step E.
# Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after.
import json, re, yaml, sys
ROOT = '<repo-old>'
UNIT = f'{ROOT}/logic/units/num_09_pesach_cloud.yaml'
LEDGER = f'{ROOT}/logic/oral_triage/num_09_pesach_cloud_2026-09-09.md'
MAN = f'{ROOT}/logic/oral_audit/manifests/num_09_pesach_cloud_claims.json'
led = open(LEDGER, encoding='utf-8').read()
cite_index = set(re.findall(r'^(Sifrei Bamidbar \d+:\d+|Onkelos Num 9:\d+)$', led.split('## CITE INDEX')[1], re.M))
assert len(cite_index) == 33, len(cite_index)
claims = {c['id']: c for c in json.load(open(MAN, encoding='utf-8'))}
assert len(claims) == 11

# (claim id, step no, anchor, name, cites, prose)
SEATS = [
 ('NM09-01', 1, 'vayedaber_bamidbar_sinai_bashanah_hashenit', 'no_before_and_after_and_the_epoch_table',
  ['Sifrei Bamidbar 64:1', 'Sifrei Bamidbar 64:2'],
  "NO BEFORE AND AFTER, AND THE EPOCH TABLE [claim NM09-01]. 'In the FIRST month' after the book opened 'on the first day of "
  "the SECOND month' (1:1): the chronological rule — there is no before and after in the Torah — DERIVED FROM THIS VERSE "
  "(Rebbi: Exod 16:35's forty years of manna, written before they had passed, is exemplar enough); the eleven months at "
  "Sinai in DISPARAGEMENT (the Hebrew's word; the shelf's English says praise). 'In the second year of their going out' — "
  "THEY COUNT FROM THE EXODUS; in the land, from the entry (Lev 25:2); the Temple built, from its building (1 Kgs 9:10); "
  "destroyed, from the destruction (Ezek 40:1); the captivity, from the kings (Dan 2:1, Hag 1:1); months as years (Exod "
  "19:1) — the eras a run is dated by, named by the shelf at the case's frame."),
 ('NM09-02', 3, 'bearbaah_asar_yom_bachodesh_hazeh', 'the_appointed_time_overrides',
  ['Sifrei Bamidbar 65:1', 'Onkelos Num 9:3'],
  "THE APPOINTED TIME [claim NM09-02]. 'In its appointed time' — the first Passover OVERRIDES THE SABBATH: R. Yoshiyah's "
  "verbal analogy with the daily offering's 'in its appointed time' (Num 28:2, extra there since 28:9-10 already run the "
  "daily on the Sabbath); R. Yonatan's objection recorded. The SECOND 'in its appointed time' (9:3): it overrides COMMUNAL "
  "IMPURITY too — the red-heifer a-fortiori is refuted by the second Passover (which overrides the Sabbath yet not "
  "impurity), so the verse must say it. 'Its statutes' = the mitzvot ON ITS BODY (Exod 12:5); 'its ordinances' = the "
  "ATTENDANT (Deut 16:3); 'ALL its ordinances' — even the non-attendant (seven days' matzah, the leaven burned). "
  "Onkelos: 'according to all its DECREE and all that is FITTING for it' — the attendant tier in the translation."),
 ('NM09-03', 4, 'vayedaber_moshe_el_bene_yisrael_laasot', 'the_telling_before_the_doing',
  ['Sifrei Bamidbar 66:1'],
  "THE TELLING BEFORE THE DOING [claim NM09-03]. Why 'Moses spoke to the children of Israel to keep the Passover' when "
  "Lev 23:44 already has him declaring the festivals? Keep the Passover in its time so ALL the festivals fall in season "
  "(Deut 16:1); or: he HEARD the sections at Sinai, TOLD them, and REPEATED them before their performance — three "
  "passes over one law; or: the laws of each festival before its festival — 'whence they said: Moses instituted that "
  "they ask and expound the festival's laws before the festival'."),
 ('NM09-04', 5, 'vayaasu_et_hapesach_barishon', 'the_one_passover_of_the_wilderness',
  ['Sifrei Bamidbar 67:1', 'Onkelos Num 9:5'],
  "THE ONE PASSOVER OF THE WILDERNESS [claim NM09-04]. 'They kept the Passover in the first month' — in DISPARAGEMENT: the "
  "only Passover of the forty years (Amos 5:25); R. Shimon b. Yochai: Israel did not sacrifice, the tribe of LEVI did "
  "(Deut 33:10), Levi kept off the calf (Exod 32:26) and alone circumcised in the wilderness (Josh 5:5 against Deut "
  "33:9) — a recorded two-arm dispute on who kept the service; 'according to all that the LORD commanded' the PRAISE: as "
  "Moses told them, so they did. Onkelos: 'in NISAN' — the ink's ordinal month given its name."),
 ('NM09-05', 8, 'vayomer_alehem_moshe_imdu', 'the_men_and_the_halt',
  ['Sifrei Bamidbar 68:1', 'Onkelos Num 9:6', 'Onkelos Num 9:7', 'Onkelos Num 9:8'],
  "THE MEN AND THE HALT [claim NM09-05]. WHO THEY WERE — three arms, unresolved: Joseph's coffin-bearers (R. Yishmael), "
  "Mishael and Eltzafan unclean by Nadab and Abihu (R. Akiva), men unclean by a met mitzvah whose seventh day fell on "
  "the eve (R. Yitzchak — either of the others could have purified in time). 'Before Moses and before Aaron' — invert: "
  "Aaron did not know, then Moses (R. Yoshiyah), or both sat in the study house (Abba Chanan). 'THOSE men said' — the "
  "affected party asks, not his agent. THE DIALOGUE: not offered in impurity? — that is for offerings with a backup; not "
  "eaten in impurity? — then let the BLOOD be sprinkled on the unclean and the flesh eaten by the clean, an A-FORTIORI "
  "from the sin offering, holy of holies; Moses: 'I HAVE NOT HEARD' — 'stand and I will hear' = from my teacher's mouth "
  "(R. Chidka: Moses knew the eating ban; the sprinkling was the question); told through them, merit through the "
  "meritorious. Onkelos: 'unclean by the CORPSE of a man's soul' (9:6), 'why should we be PREVENTED' (9:7), 'WAIT' for "
  "'stand' and 'what is commanded BEFORE the LORD concerning you' (9:8) — the standing case: no guard, a wait."),
 ('NM09-06', 10, 'daber_el_bene_yisrael_ish_ish', 'the_output_wider_than_the_question',
  ['Sifrei Bamidbar 69:1', 'Onkelos Num 9:10'],
  "THE OUTPUT WIDER THAN THE QUESTION; THE DISTANCE PARAMETER [claim NM09-06]. 'Unclean by a corpse' — what Moses ASKED; "
  "'or on a distant way' — what he did NOT ask: the rule exceeds the case. Other impurities by BINYAN AV from the two: "
  "neither is like the other, what they share is one who did not keep the first keeps the second — so all who could "
  "not. 'Distant' — R. Akiva: he wished and could not, the sages measured it from MODI'IM (fifteen mil) around; R. "
  "Eliezer: the tithe's 'distant' (Deut 14:24) — outside the place of its EATING, Jerusalem's entrance; R. Yehuda: "
  "outside the place of its FITNESS, the court — three recorded settings of one parameter. Onkelos fills the bare 'soul' "
  "to corpse impurity again, 'before the LORD'."),
 ('NM09-07', 10, 'rechoqah_hadotted_heh', 'the_dotted_heh',
  ['Sifrei Bamidbar 69:2'],
  "THE DOTTED HEH [claim NM09-07]. A dot stands above the heh of 'distant' — he keeps the second Passover even on a "
  "NON-distant way if he did not keep the first. The Torah's dotted places beside it: 'between me and YOU' (Gen 16:5), "
  "'to HIM' (18:9), 'in her RISING' (19:33), 'and he KISSED him' (33:4), 'ET' (37:12), 'and AARON' (Num 3:39), 'ASHER' "
  "(21:30), the second issaron (the shelf's '3:29' — the verse is 29:15), 'for us and our children' (Deut 29:28). "
  "MACHINE-VERIFIED: eleven tokens at ten verses carry the upper dot in the Torah — the list exactly."),
 ('NM09-08', 12, 'lo_yashiru_mimenu_ad_boqer', 'the_second_passovers_scope',
  ['Sifrei Bamidbar 69:2', 'Onkelos Num 9:12'],
  "THE SECOND PASSOVER'S SCOPE [claim NM09-08]. The date and the lamb (9:11) = the BODY mitzvot; 'with matzah and bitter "
  "herbs they shall eat it' = the ATTENDANT; 'not leave until morning, not break a bone' — two body mitzvot superadded; "
  "the rest from 'according to ALL the statute of the Passover' — but 'a bone' was in the general and LEFT IT to teach on "
  "the general: as the bone is on its body, so 'all the statute' = the body mitzvot ONLY — not the seven days' matzah, "
  "not the leaven's burning (Issi b. Akavya: 'offer IT'). Onkelos: 'the DECREE of the Passover'."),
 ('NM09-09', 13, 'vehaish_asher_hu_tahor', 'individuals_and_the_karet_fork',
  ['Sifrei Bamidbar 70:1', 'Onkelos Num 9:13'],
  "INDIVIDUALS, NOT THE CONGREGATION; THE KARET FORK [claim NM09-09]. Individuals keep the second Passover, the "
  "congregation never — from 'there were MEN' (9:6); R. Natan from 'the MAN who is clean'. 'Refrained' = could and did "
  "not (the sages' Modi'im measure); 'that soul' — deliberate (R. Akiva); 'from its people' — they at peace. 'Cut off' "
  "= the first, 'his sin he shall bear' = the second — karet for BOTH (Rebbi); R. Natan: the first alone. 'In its "
  "appointed time' — the second overrides the SABBATH, not impurity ('its whole reason is his impurity'). 'That MAN' — "
  "not a minor; the woman from 'that soul'. Onkelos: one root for 'held back' (9:7) and 'refrained' (9:13), 'shall be "
  "DESTROYED', 'shall RECEIVE HIS DEBT'."),
 ('NM09-10', 14, 'vekhi_yagur_itkhem_ger', 'the_proselytes_two_clauses',
  ['Sifrei Bamidbar 71:1', 'Onkelos Num 9:14'],
  "THE PROSELYTE'S TWO CLAUSES [claim NM09-10]. Not as soon as he converts — 'for the proselyte and the native': as the "
  "native on the fourteenth, so he; converted BETWEEN the two Passovers — R. Shimon b. Elazar: as the native who was "
  "obligated in the first and could not keeps the second, so only the obligated — he is excluded. 'According to the "
  "statute of the Passover' equates him for the Passover; 'ONE STATUTE for you, the proselyte and the native of the "
  "land' — for ALL the mitzvot of the Torah. Onkelos: 'if he BECOMES A PROSELYTE', 'as is FITTING for it', 'one "
  "COVENANT', 'the ESTABLISHED one'."),
 ('NM09-11', 22, 'o_yomayim_o_chodesh_o_yamim', 'the_cloud_by_the_word_days_a_year',
  ['Onkelos Num 9:18', 'Onkelos Num 9:22'],
  "THE CLOUD BY THE WORD; DAYS = A YEAR [claim NM09-11]. 'By the mouth of the LORD they camped and journeyed' — Onkelos: "
  "by the WORD of the LORD, four times in 9:18-23 (the halt's own phrase at Lev 24:12, 'by the mouth of the LORD', "
  "carries the same Word); 'or two days, or a month, or DAYS' — Onkelos: 'a period of time', a YEAR — the bare 'days' "
  "read as the year (the counter idiom of Lev 25:29), the march's three durations."),
]
for cid, step, anchor, name, cites, prose in SEATS:
    assert cid in claims, cid
    for c in cites:
        assert c in cite_index, (cid, c)
    assert re.fullmatch(r'[\w-]+', anchor) and re.fullmatch(r'[\w-]+', name), (anchor, name)
    assert f'[claim {cid}]' in prose

txt = open(UNIT, encoding='utf-8').read()
assert 'operators:' not in txt, 'the draft already carries operators'

def wrap(prose, indent=10):
    words = prose.split(' ')
    lines, cur = [], ''
    for w in words:
        if len(cur) + len(w) + 1 > 78 - indent and cur:
            lines.append(cur); cur = w
        else:
            cur = (cur + ' ' + w) if cur else w
    lines.append(cur)
    return '\n'.join(' ' * indent + l for l in lines)

def q(s): return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

by_step = {}
for cid, step, anchor, name, cites, prose in SEATS:
    by_step.setdefault(step, []).append((anchor, name, cites, prose))
for step, ops in by_step.items():
    sid = f'  - id: STEP_Nm_9_{step}\n'
    i = txt.index(sid)
    j = txt.index('    comment: >\n', i)
    nxt = txt.find('\n  - id: STEP_Nm_9_', i + 1)
    assert nxt == -1 or j < nxt, step
    block = '    operators:\n'
    for anchor, name, cites, prose in ops:
        block += ('      - op: WITNESS_READ\n'
                  f'        expr_en: "WITNESS-READ({anchor}, {name})"\n'
                  '        en: >\n' + wrap(prose) + '\n'
                  '        cites: [' + ', '.join(q(c) for c in cites) + ']\n'
                  '        confidence: witnessed\n')
    txt = txt[:j] + block + txt[j:]

stepE = '''
  - step: E
    name_en: "Numbers 9 derivation 2026-09-09 — THE TENT sitting 2"
    comment: >
      The first Numbers reading: the Sifrei on Numbers as the spine
      (piskaot 64-71, ten rows) with Onkelos 9:1-23, read whole and
      fresh (ledger num_09_pesach_cloud_2026-09-09.md, coverage
      computed by script). Seated as claims NM09-01..11: no before
      and after with the epoch table; the appointed time's two
      overrides; the telling before the doing; the one Passover of
      the wilderness; the men and the halt; the output wider than
      the question with the distance parameter; the dotted heh
      machine-verified; the second Passover's scope by the eighth
      middah; individuals and the karet fork; the proselyte's two
      clauses; the cloud by the Word with days as a year. The
      case's compile (cold_run_pesach_sheni.py) and the tent's tape
      lines follow in the same sitting (THE_TENT.md section 2).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
k = txt.index('\nboot_steps:\n')
txt = txt[:k] + stepE + txt[k:]
open(UNIT, 'w', encoding='utf-8').write(txt)
d = yaml.safe_load(open(UNIT, encoding='utf-8'))
ops = [(s['id'], o) for s in d['boot_steps'] for o in s.get('operators', [])]
assert len(ops) == 11 and all(o['op'] == 'WITNESS_READ' for _, o in ops), len(ops)
assert d['derivation_log'][-1]['step'] == 'E'
print('seated %d operators on %d steps: %s' % (len(ops), len(by_step), sorted(by_step)))
