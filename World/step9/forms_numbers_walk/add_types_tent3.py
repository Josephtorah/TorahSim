#!/usr/bin/env python3
# THE TENT sitting 3 (2026-09-09; World/step9/THE_TENT.md section 3): THE TYPES FIRST — three event kinds (one act on the tape,
# two case forms for the exam's scene), the SECOND SEATS of the tent's three kinds (placed_in_custody, sentence_declared,
# stoned_as_commanded — link: reference, the shared lemmas), one effect, the entity, the fourth registry's note. The `he` built
# from the pointed DB text (cantillation stripped), the witnesses the plain consonantal runs the events lint verifies. Idempotent.
import re, sqlite3, yaml
ROOT = "<repo-old>"
db = sqlite3.connect(f"file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro", uri=True)
def words(book, ch, vs):
    return [r[0] for r in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx", (book, ch, vs)).fetchall()]
def pointed(book, ch, vs, lo, hi):
    return ' '.join(''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF)) for w in words(book, ch, vs)[lo:hi])
def plain(book, ch, vs, lo, hi):
    return ' '.join(''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7)) for w in words(book, ch, vs)[lo:hi])
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

KINDS = [
 ("gathered_wood_on_the_sabbath", "act",
  "gathered wood on the Sabbath — THE CASE'S ACT: 'and the children of Israel were in the wilderness, and they found a man gathering wood on the Sabbath day; and they brought him near, those who found him gathering wood, to Moses and to Aaron and to all the congregation' (Num 15:32-33): the tape's act form of the Exodus engine's case token sabbath_profaned (ONE ACT, TWO FORMS — the pair named below); the finders are the witnesses and the warners (the Sifrei 113:1: the repetition teaches they warned him, specifying the labor); consumed by law_sabbath through its own cells (labor_barred, put_to_death, stoned — under boot the code decides before the halt, the mode included) and by law_mekoshesh (warned_specifying_the_labor)",
  pointed('Num', 15, 32, 4, 10) + " (and they found a man gathering wood on the Sabbath day — Num 15:32; Onkelos: collecting wood) · " + pointed('Num', 15, 33, 0, 4) + " (and they brought him near, those who found him — Num 15:33)",
  ["Num 15:32 | " + plain('Num', 15, 32, 4, 10), "Num 15:33 | " + plain('Num', 15, 33, 0, 4)],
  "Num 15:32-33 (the act and the bringing); Exod 31:14-15 (the standing liability — 'its profaners shall surely die'); Sifrei Bamidbar 113:1 (the labor — detaching; the identity dispute; the watchers; the warning specifying the labor); Onkelos Num 15:32 (MATERIAL: collecting); Shabbat 96b:15-20 (the labor's three arms; the identity baraita); Mishnah Sanhedrin 7:4, 7:8",
  "num_15_wood_tzitzit (STEP_Nm_15_32, STEP_Nm_15_33; claims NM15-01, NM15-02)",
  "submitted by cold_run_mekoshesh.py [subjects: the-wood-gatherer] (the narrative scene, THE TENT sitting 3); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_sabbath (cold_run_incense_shekel.py) -> labor_barred, put_to_death, stoned; consumed by law_mekoshesh (cold_run_mekoshesh.py) -> warned_specifying_the_labor",
  ["profaner", "witnessed", "labor", "warned", "labor_named"],
  "sabbath_profaned — one act, two forms: the exam's case token (form case, the Exodus engine's, Exod 31:14) and the tape's narrative act at its recorded run (Num 15:32-33); the pair named here (sitting 1's rule)"),
 ("forewarned_before_the_act", "case",
  "forewarned before the act — the exam's case on THE WARNING: 'those who found him gathering wood' (Num 15:33) repeats 15:32 to teach that they warned him and he continued, and that the warning SPECIFIED THE LABOR — for every primary labor (Sifrei 113:1; R. Yitzchak's a-fortiori from idolatry); whether the warning must also name the DEATH is the recorded row (the first tanna no, Rabbi Yehuda yes — Sanhedrin 80b:5, 8b:5); the court asks the witnesses 'did you warn him?' (Mishnah Sanhedrin 5:1)",
  pointed('Num', 15, 33, 2, 6) + " (those who found him gathering wood — Num 15:33; the Sifrei: they warned him, specifying his labor)",
  ["Num 15:33 | " + plain('Num', 15, 33, 2, 6)],
  "Num 15:33 (the repetition — the warning); Sifrei Bamidbar 113:1; Mishnah Sanhedrin 5:1 ('did you warn him' among the examinations); Sanhedrin 80b:5 (the first tanna against Rabbi Yehuda on naming the death; the same segment as the code-or-edict row), 8b:5 (Rabbi Yehuda's rule), 41a; Mishnah Makkot 1:9",
  "num_15_wood_tzitzit (STEP_Nm_15_33; claim NM15-02)",
  "submitted by cold_run_mekoshesh.py [subjects: the exam's persons] (the wrap's scene); consumed by law_mekoshesh (cold_run_mekoshesh.py) -> warned_specifying_the_labor, put_to_death, exempt",
  ["person", "transgression", "warned", "labor_named", "death_named"], None),
 ("stoning_carried_out", "case",
  "the stoning carried out — the exam's case on THE PROTOCOL: 'and all the congregation brought him outside the camp and stoned him with stones, and he died' (Num 15:36) against 'stoned him with a stone' (Lev 24:23) — reconciled by the stoning house (Sifrei 114:1 = Mishnah Sanhedrin 6:4): the platform, the first witness's push, the second's stone on the heart, all the people — 'the hand of the witnesses first' (Deut 17:7); the venue outside the court (6:1), the confession (6:2), the stripping (6:3), the hanging (6:4 — Rabbi Eliezer all the stoned, the sages the blasphemer and the idolater), the same-day burial in the court's graveyard and the unmourned death (6:5-6); the tape's act form is stoned_as_commanded (the pair named below)",
  pointed('Num', 15, 36, 7, 11) + " (and they stoned him with stones, and he died — Num 15:36; Onkelos: and he died)",
  ["Num 15:36 | " + plain('Num', 15, 36, 7, 11)],
  "Num 15:36 (the execution — 'with stones', 'and he died'); Lev 24:23 ('with a stone'); Deut 17:7 (the witnesses' hand first — OWED FORWARD), 21:22-23 (the hanging, the same-day burial — OWED FORWARD); Joshua 7:19-25 (Achan's confession and stoning — the Prophets' run); Sifrei Bamidbar 114:1; Mishnah Sanhedrin 6:1-6; Sanhedrin 42b-46b",
  "num_15_wood_tzitzit (STEP_Nm_15_36; claim NM15-05)",
  "submitted by cold_run_mekoshesh.py [subjects: the exam's persons] (the wrap's scene); consumed by law_mekoshesh (cold_run_mekoshesh.py) -> confessed, stoned, hanged, buried",
  ["person", "transgression", "died_at", "confessed", "sex"],
  "stoned_as_commanded — one act, two forms: the tape's narrative act (Lev 24:23, Num 15:36) and the exam's case token on the protocol's rows; the pair named here (sitting 1's rule, the second named pair)"),
]
SECOND_SEATS = {   # kind -> (witness run appended, the ink note appended, the corpus note appended)
 "placed_in_custody": ("Num 15:34 | " + plain('Num', 15, 34, 0, 3),
   "THE SECOND SEAT (THE TENT sitting 3, 2026-09-09): Num 15:34 — 'and they placed him in the guard, for it had not been declared what should be done to him' (the wood-gatherer; Onkelos: bound him in the guardhouse, the same idiom): the uncertainty THE MODE (Sanhedrin 78b:7; Sifrei Bamidbar 114:1 — Exod 31:14 the standing liability); the same word 'in the guard' at both halts (eight Torah seats) — THE TWO QUESTIONS answered: a REFERENCE",
   "num_15_wood_tzitzit (STEP_Nm_15_34; claim NM15-03)"),
 "sentence_declared": ("Num 15:35 | " + plain('Num', 15, 35, 7, 14),
   "THE SECOND SEAT (THE TENT sitting 3, 2026-09-09): Num 15:35 — 'and the LORD said to Moses: die shall die the man; stone him with stones, all the congregation, outside the camp' — THE LEANER FORM: 'said' without 'saying', no statute in the speech (computed against Lev 24:13, Num 9:9, Num 27:6); the generations' rule is THE MODE for a statute that predates the case (Sifrei 114:1 'for the generations' / 'for the hour') — rule_installed names a CELL of an existing law (law_sabbath:death_run), not a daemon; no hearers' hands (24:14's own); 'outside the camp' shared with 24:14 — THE TWO QUESTIONS answered: a REFERENCE",
   "num_15_wood_tzitzit (STEP_Nm_15_35; claim NM15-04)"),
 "stoned_as_commanded": ("Num 15:36 | " + plain('Num', 15, 36, 0, 10),
   "THE SECOND SEAT (THE TENT sitting 3, 2026-09-09): Num 15:36 — 'and all the congregation brought him outside the camp and stoned him with stones, and he died, as the LORD commanded Moses': 'with stones' against 24:23's 'a stone' (Sifrei 114:1: the stoning house), 'and he died' written here and not at 24:23 — the execution closes the sentence and the guard (the close pairing); law_mekoshesh's hanging watch under the row's Rabbi Eliezer arm alone; 'brought out', 'outside the camp', 'stoned him' shared with 24:23 — THE TWO QUESTIONS answered: a REFERENCE",
   "num_15_wood_tzitzit (STEP_Nm_15_36; claim NM15-05)"),
}
EFFECTS = [
 ("warned_specifying_the_labor", "status",
  "warned, the labor specified — the STATUS the finders' warning writes on the person: 'and they brought him near, those who found him gathering wood' (Num 15:33) repeats 15:32 to teach that they WARNED him and he continued, and that the warning NAMED THE LABOR (the Sifrei 113:1: 'whence for all the primary labors of the Torah the warning specifies the labor'); the forewarning the capital verdict needs (Mishnah Sanhedrin 5:1 'did you warn him'); the name checked: forewarned is the goring ox's recidivism status",
  pointed('Num', 15, 33, 2, 6) + " (those who found him gathering wood — Num 15:33; the Sifrei: they warned him, of the kind of his labor)",
  "Num 15:33 (the repetition); Sifrei Bamidbar 113:1; Mishnah Sanhedrin 5:1; Sanhedrin 80b:5, 8b:5 (naming the death — the row), 41a; Mishnah Makkot 1:9",
  "num_15_wood_tzitzit (STEP_Nm_15_33; claim NM15-02)",
  "law_mekoshesh (cold_run_mekoshesh.py) on gathered_wood_on_the_sabbath (the tape) and forewarned_before_the_act (the exam's rows)"),
]

# ---- the kinds: append INTO the `events:` mapping (the registry's second top-level section, narrative_verbs, follows it) ----
path = f"{ROOT}/World/step9/event_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
have = yaml.safe_load(text)['events']
out = []
for kid, form, en, he, wit, ink, corpus, tape, fields, alias in KINDS:
    if kid in have:
        print('already registered:', kid); continue
    lines = ['  %s:' % kid, '    en: %s' % q(en), '    he: %s' % q(he), '    form: %s' % form,
             '    witness: [%s]' % ', '.join(q(w) for w in wit), '    ink: %s' % q(ink), '    corpus: %s' % q(corpus),
             '    tape: %s' % q(tape), '    fields: [%s]' % ', '.join(q(f) for f in fields)]
    if alias:
        lines.append('    aliases_in_code: %s' % q(alias))
    out.append('\n'.join(lines) + '\n')
if out:
    i = text.index('\nnarrative_verbs:\n')            # THE TENT sitting 1's lesson: an appender writes into the RIGHT mapping
    text = text[:i].rstrip('\n') + '\n' + ''.join(out) + text[i:]
# ---- the second seats: the witness run appended, link: reference after form, the ink and corpus notes appended ----
for kid, (wit, ink_note, corpus_note) in SECOND_SEATS.items():
    m = re.search(r'(?ms)^  %s:\n(.*?)(?=^  [a-z_]+:\n|^narrative_verbs:\n)' % kid, text)
    assert m, kid
    block = m.group(0)
    if wit in block:
        print('second seat already on:', kid); continue
    assert 'link:' not in block, kid
    nb = re.sub(r'^(    witness: \[.*)\]$', lambda mm: mm.group(1) + ', ' + q(wit) + ']', block, count=1, flags=re.M)
    nb = re.sub(r'^(    form: \w+)$', r'\1\n    link: reference', nb, count=1, flags=re.M)
    nb = re.sub(r'^(    ink: ".*)"$', lambda mm: mm.group(1) + '; ' + ink_note.replace('"', '\\"') + '"', nb, count=1, flags=re.M)
    nb = re.sub(r'^(    corpus: ".*)"$', lambda mm: mm.group(1) + '; ' + corpus_note.replace('"', '\\"') + '"', nb, count=1, flags=re.M)
    nb = re.sub(r'^(    tape: ".*)"$', lambda mm: mm.group(1) + '; the second seat submitted by cold_run_mekoshesh.py [subjects: the-wood-gatherer]' + (' and consumed by law_mekoshesh (cold_run_mekoshesh.py) -> hanged (the row\'s Rabbi Eliezer arm alone)' if kid == 'stoned_as_commanded' else '') + '"', nb, count=1, flags=re.M)
    assert nb.count('link: reference') == 1 and wit in nb and ink_note[:20] in nb and corpus_note in nb, kid
    text = text.replace(block, nb)
open(path, 'w', encoding='utf-8').write(text)
after = yaml.safe_load(open(path, encoding='utf-8'))
print('kinds: registry %d -> %d; second section intact: %s' % (len(have), len(after['events']), 'narrative_verbs' in after))
for kid, *_ in KINDS:
    print('  ', kid, after['events'][kid]['form'], '| witness:', after['events'][kid]['witness'])
for kid in SECOND_SEATS:
    e = after['events'][kid]; print('  ', kid, '| link:', e.get('link'), '| witnesses:', len(e['witness']))
# ---- the effect ----
path = f"{ROOT}/World/step9/effect_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
have = yaml.safe_load(text)['effects']
out = []
for eid, op, en, he, ink, corpus, exam in EFFECTS:
    if eid in have:
        print('already registered:', eid); continue
    out.append('  %s:\n    en: %s\n    he: %s\n    ledger_op: %s\n    ink: %s\n    corpus: %s\n    exam: %s\n' % (eid, q(en), q(he), op, q(ink), q(corpus), q(exam)))
if out:
    if not text.endswith('\n'): text += '\n'
    open(path, 'w', encoding='utf-8').write(text + ''.join(out))
    after = yaml.safe_load(open(path, encoding='utf-8'))['effects']
    print('effects appended %d; registry %d -> %d effects' % (len(out), len(have), len(after)))
# ---- the entity ----
path = f"{ROOT}/logic/corpus/entity_registry.yaml"
text = open(path, encoding='utf-8').read()
if 'the_wood_gatherer' not in text:
    ent = ('  - id: the_wood_gatherer\n'
           '    en: "the wood-gatherer — the man found gathering wood on the Sabbath day in the wilderness, brought to Moses and Aaron and all the congregation, held in the guard because it had not been declared what should be done to him, stoned with stones outside the camp as the LORD commanded (Num 15:32-36); WHO HE WAS is a TWO-ARM DISPUTE the shelf leaves open (Sifrei Bamidbar 113:1; Shabbat 96b:19-20): ZELOPHEHAD — R. Akiva, by the verbal analogy \'wilderness\' here and at 27:3 (\'our father died in the wilderness... in his own sin\'), on which arm this person is the daughters\' father (sitting 4\'s decedent); ONE OF THE BOLD ONES of 14:44 — R. Yehuda b. Beteira, who rebukes the naming (\'the Torah concealed him and you reveal him\'); UNASSIGNED here, sitting 4 reads 27:3 against it"\n'
           '    kind: person\n'
           '    members:\n'
           '      - {token: the-wood-gatherer, units: [step9-scenes]}   # cold_run_mekoshesh.py\'s narrative scene (THE TENT sitting 3, 2026-09-09); the Exodus engine\'s bench token \'the-gatherer\' is NOT joined (the registry map is global at submit; that bench is its own world); the frozen unit\'s token a later join\n')
    i = text.index('  - id: the_unclean_men\n')
    k = text.find('\n  - id: ', i + 1)
    if k == -1:                                  # the_unclean_men is the file's LAST entry — append at the end
        text = text.rstrip('\n') + '\n' + ent
    else:
        text = text[:k + 1] + ent + text[k + 1:]
    text = text.replace('#   2026-09-09 THE TENT sitting 2 (World/step9/THE_TENT.md section 2): the_unclean_men (kind people)',
                        '#   2026-09-09 THE TENT sitting 3 (World/step9/THE_TENT.md section 3): the_wood_gatherer (kind person) — the identity dispute recorded unassigned (Zelophehad / one of the bold ones)\n'
                        '#   2026-09-09 THE TENT sitting 2 (World/step9/THE_TENT.md section 2): the_unclean_men (kind people)', 1)
    open(path, 'w', encoding='utf-8').write(text)
    reg = yaml.safe_load(open(path, encoding='utf-8'))
    ents = reg['entities'] if isinstance(reg, dict) and 'entities' in reg else reg
    ids = [e['id'] for e in ents] if isinstance(ents, list) else list(ents)
    print('entity the_wood_gatherer appended; entities', len(ids), '| present:', 'the_wood_gatherer' in ids)
else:
    print('entity already present')
# ---- the fourth registry: the installing act's second-seat note ----
path = f"{ROOT}/World/step9/installation_parameters.yaml"
text = open(path, encoding='utf-8').read()
tag = 'THE SECOND SEAT (THE TENT sitting 3)'
if tag not in text:
    m = re.search(r'(?ms)^  sentence_declared:\n.*?^    note: "(.*?)"$', text)
    assert m
    old = m.group(0)
    new = old[:-1] + '; ' + tag + ': Num 15:35 — the wood-gatherer\'s sentence installs THE MODE for a statute that predates the case (Exod 31:14): rule_installed names a CELL of an existing law, law_sabbath:death_run, not a daemon — the cell\'s own in-force gate is the second pass\'s (D2)"'
    text = text.replace(old, new, 1)
    open(path, 'w', encoding='utf-8').write(text)
    yaml.safe_load(open(path, encoding='utf-8'))
    print('installation_parameters: the second-seat note appended to sentence_declared')
else:
    print('installation note already present')
