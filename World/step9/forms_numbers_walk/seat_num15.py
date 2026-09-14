#!/usr/bin/env python3
# THE TENT sitting 3 (2026-09-09) — SEAT the eight claims of num_15_wood_tzitzit_claims.json into the draft unit
# logic/units/num_15_wood_tzitzit.yaml as WITNESS_READ operators (sitting 2's rhythm, seat_num09.py: one operator per claim
# at its verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), and append derivation_log step E.
# Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after.
import json, re, yaml
ROOT = '<repo-old>'
UNIT = f'{ROOT}/logic/units/num_15_wood_tzitzit.yaml'
LEDGER = f'{ROOT}/logic/oral_triage/num_15_wood_tzitzit_2026-09-09.md'
MAN = f'{ROOT}/logic/oral_audit/manifests/num_15_wood_tzitzit_claims.json'
led = open(LEDGER, encoding='utf-8').read()
cite_index = set(re.findall(r'^(Sifrei Bamidbar \d+:\d+|Onkelos Num 15:\d+)$', led.split('## CITE INDEX')[1], re.M))
assert len(cite_index) == 14, len(cite_index)
claims = {c['id']: c for c in json.load(open(MAN, encoding='utf-8'))}
assert len(claims) == 8

# (claim id, verse step, anchor, name, cites, prose)
SEATS = [
 ('NM15-01', 32, 'vayimtzeu_ish_mekoshesh_etzim', 'the_gatherer_found',
  ['Sifrei Bamidbar 113:1', 'Onkelos Num 15:32'],
  "THE GATHERER FOUND [claim NM15-01]. In DISPARAGEMENT: the first Sabbath kept, the second desecrated. 'Gathering' is a "
  "LABOR, not a man's name — detaching from the ground (the Sifrei) or collecting (Onkelos: 'while collecting wood'): what "
  "the labor was is a recorded question. WHO HE WAS: Zelophehad — R. Akiva's verbal analogy on 'wilderness' (15:32 / 27:3, "
  "'our father died in the wilderness'); R. Yehuda b. Beteira: 'He who spoke and the world was covered him, and you uncover "
  "him' — one of the BOLD ONES (14:44). Unresolved, data on the entity; on R. Akiva's arm the gatherer is the daughters' "
  "father. 'And they FOUND' — Moses appointed watchers."),
 ('NM15-02', 33, 'hamotzeim_oto_mekoshesh_etzim', 'the_warning_specifies_the_labor',
  ['Sifrei Bamidbar 113:1', 'Onkelos Num 15:33'],
  "THE WARNING SPECIFIES THE LABOR [claim NM15-02]. 'Those who found him gathering' REPEATS 15:32 — to teach that they "
  "WARNED him and he continued; R. Yitzchak: the warning itself follows a-fortiori from idolatry (the gravest, not liable "
  "without it), so the repetition teaches that the warning NAMES THE LABOR — for every primary labor of the Torah. 'To Moses "
  "and to Aaron and to all the congregation': if Moses did not know, would Aaron? — invert the verse (R. Yoshiyah), or the "
  "study house where the finders stood before them (R. Yonatan in R. Elazar's name). The participle stands twice in the "
  "Torah, both in this case — machine-checked."),
 ('NM15-03', 34, 'vayanichu_oto_bamishmar', 'the_guard_and_the_mode',
  ['Sifrei Bamidbar 114:1', 'Onkelos Num 15:34'],
  "THE GUARD AND THE MODE [claim NM15-03]. 'They placed him in the guard' — all liable to karet (the shelf's Hebrew; its "
  "emendation: to death) are CONFINED pending judgment: the custody rule stated as a general. 'For it had not been declared "
  "what should be done to him' — but Exod 31:14 already says 'its profaners shall surely die'; what was not declared is WHICH "
  "DEATH: the uncertainty is THE MODE, the liability standing law (Sanhedrin 78b:7's distinction from the blasphemer, at its "
  "source). Onkelos: 'and they BOUND him in the GUARDHOUSE, for it had not been explained TO THEM' — Lev 24:12's own idiom, "
  "the guard form of the halt; the court's ignorance the clause's subject."),
 ('NM15-04', 35, 'mot_yumat_haish_ragom_oto', 'the_output_for_the_generations_and_the_hour',
  ['Sifrei Bamidbar 114:1', 'Onkelos Num 15:35'],
  "THE OUTPUT FOR THE GENERATIONS AND THE HOUR [claim NM15-04]. 'Die shall die the man' — FOR THE GENERATIONS; 'stone him "
  "with stones' — FOR THE HOUR: the rule and the instance split inside one sentence, and the rule is the MODE (stoning for "
  "every Sabbath profaner) for a statute that predates the case (Exod 31:14). 'All the congregation' — in its PRESENCE, not "
  "literally: Deut 17:7, the witnesses' hand first. THE FRAME (computed): the bare 'and the LORD SAID to Moses', no 'saying' "
  "and no statute in the speech — Lev 24:13 and Num 9:9 open 'spoke... saying' with a statute following; the sentence alone "
  "is this output. Onkelos: 'being killed, the man shall be killed' — the doubled infinitive kept."),
 ('NM15-05', 36, 'vayirgemu_oto_baavanim_vayamot', 'the_execution_stones_and_a_stone',
  ['Sifrei Bamidbar 114:1', 'Onkelos Num 15:36'],
  "THE EXECUTION: STONES AND A STONE [claim NM15-05]. 'They brought him outside the camp' — the liable are executed OUTSIDE "
  "THE COURT. 'With stones' here against 'with a STONE' at Lev 24:23 — reconciled by the stoning house's protocol: two "
  "stories high, the first witness's push at the loins, turned onto the heart and back, the second witness's stone on the "
  "heart, then all Israel with stones — Deut 17:7's 'the hand of the witnesses first, the hand of all the people after'. 'As "
  "the LORD commanded' — stone, and HANG (Deut 21:22; R. Eliezer). R. Chidka in Shimon HaShikmoni's name: Moses knew the "
  "death, not its mode — the section told through the gatherer, liability rolled through the liable (the mirror of 68:1's "
  "merit through the meritorious). 'AND HE DIED' written here (Onkelos: 'and he died'), absent at 24:23 — computed."),
 ('NM15-06', 38, 'veasu_lahem_tzitzit', 'the_fringes_making',
  ['Sifrei Bamidbar 115:1', 'Onkelos Num 15:38'],
  "THE FRINGES' MAKING [claim NM15-06]. WOMEN included — R. Shimon exempts: 'every positive command that time causes, women "
  "are exempt from' — the rule stated here in full; the veil exempt, the wrap obligated because the husband covers with it "
  "(R. Yehuda b. Bava). 'Fringe' = what PROTRUDES, of any amount — no measure (the elders of both houses in Yonatan b. "
  "Beteira's upper room; nor the lulav). Not one thread: 'cords' (Deut 22:12) — three (Beth Hillel) / three white and the "
  "fourth blue (Beth Shammai, the law; the shelf's Hebrew emended at the line). The cord from the corner, the fringe from the "
  "cord. FOUR corners (Deut 22:12) exclude the three- to eight-cornered; pillows excluded by 'wherewith you cover yourself'; "
  "NIGHT garments by 'you shall see it'; the BLIND man's garment included by 'it shall be for you'. The blue SPUN AND "
  "DOUBLED, the white by the shared verb 'place'; at the weaving, not the growing (R. Eliezer b. Yaakov: both); TIED, not "
  "woven. Onkelos: kruspedin — the Greek loanword for the fringe; 'their COVERING' for 'their garments'."),
 ('NM15-07', 39, 'ureitem_oto_uzkhartem', 'seeing_and_remembering',
  ['Sifrei Bamidbar 115:1', 'Onkelos Num 15:39'],
  "SEEING AND REMEMBERING [claim NM15-07]. The four are ONE mitzvah, mutually inclusive — R. Yishmael: four. The names: blue "
  "from the Egyptians' bereavement of the firstborn or their destruction at the sea; fringe from 'He PEERED over our "
  "fathers' houses' (Song 2:9). R. Meir: not 'see THEM' but 'see HIM' — as receiving the Shekhinah's face: the blue like the "
  "sea, the sea the firmament, the firmament the Throne (Ezek 1:26). 'See and remember' — see THIS command and remember "
  "ANOTHER: the Shema, tied by 15:41's 'I am the LORD your God', found only in the Shema's sections; the three sections' "
  "order — the kingdom's yoke, the commands' yoke, the fringes by day only ('you shall see it'); R. Shimon b. Yochai: learn, "
  "teach, do; an a-fortiori from the fringes' sign to every deed. 'After your hearts' heresy, 'after your eyes' harlotry, "
  "'after which you go astray' idolatry; THE EYES FOLLOW THE HEART (the blind sin too). Onkelos: 'after the THOUGHT of your "
  "heart and after the SIGHT of your eyes' — the two faculties supplied."),
 ('NM15-08', 41, 'ani_yhwh_elohekhem_twice', 'remember_is_do_and_the_two_i_am',
  ['Sifrei Bamidbar 115:1', 'Sifrei Bamidbar 115:2', 'Onkelos Num 15:40', 'Onkelos Num 15:41'],
  "REMEMBER IS DO; THE TWO 'I AM' [claim NM15-08]. 'So that you remember and do' (15:40) EQUATES remembering with doing; 'holy "
  "to your God' — all the commands' holiness, or Rebbi: the fringes' own (Lev 19:2 already carries the commands') — the "
  "fringes ADD holiness (Onkelos: holy BEFORE your God). 'Who brought you out of Egypt' — against IMITATION DYE for blue and "
  "'who will know?': the secret sinner exposed as Egypt was, and the greater measure of good; THE SERVANT PARABLE — redeemed "
  "as servants, not sons, the light and heavy decrees (the Sabbath, illicit unions, the fringes, the tefillin) on that "
  "condition. 'I am the LORD your God' AGAIN after Exod 20:2 — against 'we will not do and not receive' (Ezekiel 20's elders: "
  "sold to return, no leaving — pestilence, sword, famine, then rule perforce). R. Natan: the reward at the command's side — "
  "the diligent man's four fringes as FOUR WITNESSES, the doubled 'I am' reward and punishment."),
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
    sid = f'  - id: STEP_Nm_15_{step}\n'
    i = txt.index(sid)
    j = txt.index('    comment: >\n', i)
    nxt = txt.find('\n  - id: STEP_Nm_15_', i + 1)
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
    name_en: "Numbers 15:32-41 derivation 2026-09-09 — THE TENT sitting 3"
    comment: >
      The second Numbers reading: the Sifrei on Numbers as the spine
      (piskaot 113-115, four rows) with Onkelos 15:32-41, read whole
      and fresh (ledger num_15_wood_tzitzit_2026-09-09.md, coverage
      computed by script, the ink facts computed from the Tanakh DB).
      Seated as claims NM15-01..08: the gatherer found (the labor,
      the identity dispute, the watchers); the warning specifying the
      labor by the case's own repetition; the guard and the mode
      (the uncertainty the mode, Exod 31:14 the standing liability);
      the output for the generations and the hour inside one bare
      sentence; the execution's stones against the stone, the
      hanging, the death written; the fringes' making; seeing and
      remembering; remember is do and the two I-am. The case's
      compile (the Sabbath profaner's mode) and the tent's second
      seats follow in the same sitting (THE_TENT.md section 3).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
k = txt.index('\nboot_steps:\n')
txt = txt[:k] + stepE + txt[k:]
open(UNIT, 'w', encoding='utf-8').write(txt)
d = yaml.safe_load(open(UNIT, encoding='utf-8'))
ops = [(s['id'], o) for s in d['boot_steps'] for o in s.get('operators', [])]
assert len(ops) == 8 and all(o['op'] == 'WITNESS_READ' for _, o in ops), len(ops)
assert d['derivation_log'][-1]['step'] == 'E'
print('seated %d operators on %d steps: %s' % (len(ops), len(by_step), sorted(by_step)))
