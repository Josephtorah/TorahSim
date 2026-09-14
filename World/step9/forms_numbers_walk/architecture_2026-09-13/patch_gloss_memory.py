#!/usr/bin/env python3
# THE PROJECT REVIEW, finding 13's memory side (2026-09-13; the owner: "Yes"): every flagged term in the memory folder given its
# English marker in place (a gloss in parentheses, a quoted gloss, or ", the …"); link lists get a gloss per link because the lint's
# window runs ninety characters and stops at a period. Every replacement asserted once; a pair already applied is skipped.
M = '<memory>/'
def patch(name, pairs):
    p = M + name; t = open(p, encoding='utf-8').read(); done = 0
    for old, new in pairs:
        n = t.count(old)
        if n == 0 and new in t: continue
        assert n == 1, (name, n, old[:50]); t = t.replace(old, new); done += 1
    open(p, 'w', encoding='utf-8').write(t); print('patched', name, done)
patch('MEMORY.md', [
 ('not va-yisgor. See', 'not va-yisgor (the transliteration). See'),
 ('(grok-full-control-handoff.md) — CLOSED 2026-08-06; SOLO MODE', '(grok-full-control-handoff.md) — the handoff CLOSED 2026-08-06; SOLO MODE'),
 ('(torahsim-public-era.md) — site LIVE at', '(torahsim-public-era.md) — the site LIVE at'),
 ('(two-window-workflow.md) — ⚠ CANON FLIP 2026-09-01:', '(two-window-workflow.md) — the CANON FLIP (⚠ 2026-09-01):'),
 ('(verse-status-labeling.md) — vstat {o,d,p,g};', '(verse-status-labeling.md) — the labels vstat {o,d,p,g};'),
])
patch('agent-derivation-trial.md', [('Reviewer still re-queries the raw snapshot', 'Reviewer still queries the raw snapshot again')])
patch('chat-hebrew-glossing.md', [('not va-yisgor. What stays', 'not va-yisgor (the transliteration). What stays')])
patch('demonstrate-compile-link.md', [('meforash = targum)', 'meforash = targum, the Aramaic translation)')])
patch('derivation-era.md', [
 ('prefixed forms (לְ, וּלְ, בְּ, הַ), which hide', "prefixed forms (לְ 'to', וּלְ 'and to', בְּ 'in', הַ 'the'), which hide"),
 ('homographs like אשר tribe vs relative pronoun', "homographs like אשר ('Asher' the tribe against 'which' the relative pronoun)"),
 ('[[two-window-workflow]] for the', '[[two-window-workflow]] (the two windows) for the'),
])
patch('external-review-standing-law.md', [('etnachta splits,', 'etnachta (the mid-verse pause) splits,')])
patch('findings-loop-stamp-law.md', [('see [[two-window-workflow]])', 'see [[two-window-workflow]], the two windows)')])
patch('grok-full-control-handoff.md', [('description: CLOSED 2026-08-06 — Grok tenure', 'description: CLOSED 2026-08-06 — the Grok tenure')])
patch('law-era-top10.md', [('21:1 only verse w/o etnachta; qere/ketiv as two', '21:1 only verse without an etnachta (the mid-verse pause); qere/ketiv (the read and the written forms) as two')])
patch('machine_transfer_2026-08-09.md', [('`DISPOSABLE_scan/<old-mac-project-folder>.zip`', "the old Mac's zip in `DISPOSABLE_scan/` (its name the old path)")])
patch('oral-first-insight-pipeline.md', [
 ('חקותי one-full vs nine-lean-all-Leviticus, הקל unique at the voice-of-Jacob', "חקותי ('My statutes') one-full vs nine-lean-all-Leviticus, הקל ('the voice') unique at the voice-of-Jacob"),
 ('the fifteen-list בגד, פי הבאר ×5)', "the fifteen-list בגד ('garment'), פי הבאר ('the mouth of the well') ×5)"),
 ('יכול=Caleb, בנימין-in-Genesis, שלוחה, ואיטיבה)', "יכול=Caleb, בנימין ('Benjamin') in Genesis, שלוחה ('let loose'), ואיטיבה ('and I will do good'))"),
 ("the deceit's one lean להמל.", "the deceit's one lean להמל ('to be circumcised')."),
 ('28:18 tzadi-dagesh, 30:20 zayin-dots', '28:18 tzadi-dagesh (the letter tzadi with the doubling dot), 30:20 zayin-dots'),
 ('maqqef-in-plain/space-in-trees', 'maqqef-in-plain (the joining stroke kept in the plain text)/space-in-trees'),
 ('see [[torahsim-public-era]],\n[[verse-status-labeling]], [[law-era-top10]] addendum, and\n[[two-window-workflow]].', 'see [[torahsim-public-era]] (the public site),\n[[verse-status-labeling]] (the labels), [[law-era-top10]] addendum, and\n[[two-window-workflow]] (the two windows).'),
 ('Chullin halakha.', 'Chullin halakha (the ruling).'),
 ('block midrash, named Talmud loci', 'block midrash (the rabbinic reading), named Talmud loci'),
])
patch('re-era-constitution.md', [('the matching-decompilation model.', 'the matching-decompilation (the match of code to text) model.')])
patch('spine-default.md', [("five-disqualified table derived word by", "five-disqualified table, the one derived word by")])
patch('step9-exam-era.md', [
 ('(המצות/צו)', "(המצות 'the unleavened bread' / צו 'command')"),
 ('EX22-05 both-parties+heirs at the Mekhilta layer', 'EX22-05 both-parties (the two parties) + heirs at the Mekhilta layer'),
 ('[equal-for-mitzvah; AGAINST-the-day', '[equal-for-mitzvah (equal for the commandment); AGAINST-the-day'),
 ('a mapping-registry is appended as text', 'a mapping-registry (the map of names) is appended as text'),
 ("the register test's lowercase-only stem regex", "the register test's lowercase-only (all lower case) stem regex"),
 ("the front end's etnachta measured", "the front end's etnachta (the mid-verse pause) measured"),
 ('the LAW-midrash spine anticipates', 'the LAW-midrash (the rabbinic reading) spine anticipates'),
])
patch('the-effects-law.md', [('all ink-verified.', 'all ink-verified (checked on the ink).')])
patch('the-loop-ruling.md', [('grok-mockups stays never-commit.', 'grok-mockups (the mockups folder) stays never-commit.')])
patch('the-world-architect-file.md', [('[[corpus-world-simulation]], [[torahsim-public-era]].', '[[corpus-world-simulation]], [[torahsim-public-era]] (the related memories).')])
patch('torahsim-public-era.md', [('Related: [[two-window-workflow]], [[verse-status-labeling]], [[law-era-top10]]', 'Related: [[two-window-workflow]] (the two windows), [[verse-status-labeling]] (the labels), [[law-era-top10]]')])
patch('two-shelves-classification.md', [('the midrash collections — verse-by-verse', 'the midrash collections (the rabbinic readings) — verse-by-verse')])
patch('two-window-workflow.md', [
 ('parity is checked by byte-diffing web/scroll/data', 'parity is checked by byte-diffing (comparing byte by byte) web/scroll/data'),
 ('[[torahsim-public-era]] for what remains', '[[torahsim-public-era]] (the public-era memory) for what remains'),
 ('the changelog-gate fix ported)', 'the changelog-gate (the unit-edit gate) fix ported)'),
])
patch('verse-status-labeling.md', [('Related: [[torahsim-public-era]], [[two-window-workflow]], [[law-era-top10]]', 'Related: [[torahsim-public-era]] (the public site), [[two-window-workflow]] (the two windows), [[law-era-top10]]')])
