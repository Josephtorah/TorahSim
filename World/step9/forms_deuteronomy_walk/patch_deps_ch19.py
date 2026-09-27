import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 16b (LEAN): THE FIVE DEMANDS OF THE DEPENDENCY GATE FILED FROM ITS PRINT (ch19b_dependency_first.out — the gate run alone before the chain, 15b's form):
# TWO token-demanded edges dispositioned FALSE (refuge_war_family -> chatat on 'chatat' at 19:15, 20:18 — the general word for sin, not the sin offering; -> pesach on
# 'firstborn' at 21:15-17 — the inheritance's firstborn, the womb's by CALL to release_firstborn) and THREE pointers AS_WHEN (19:8 'as He swore to your fathers' —
# RUN_CITATION behind, the oaths to the fathers; 19:19 'as he plotted to do' — PARAMETER, the talion's measure; 20:17 'as the LORD your God commanded you' — RUN_CITATION
# behind, 7:1-5's line nations_devoted). The Hebrew from the gate's own print, glossed. patch_deps_ch17b.py's form. RUN FROM THE REPO ROOT.
import subprocess, yaml
ROOT = _ROOT
P = ROOT + '/World/step9/dependency_dispositions.yaml'; s = open(P, encoding='utf-8').read()
W = 'THE DEUTERONOMY WALK 16b (2026-09-25; LEAN)'
assert 'from: refuge_war_family, to: chatat' not in s and 'verse: "Deut 20:17"' not in s, 'already filed'
i = s.index('  - {from: refuge_war_family, to: place_name, disposition: CALL'); j = s.index('\n  - {', i + 10)
EDGES = ('''  - {from: refuge_war_family, to: chatat, disposition: FALSE, link: none,
     why: "%s | the token census's 'chatat' at Deut 19:15 ('for any iniquity or any sin, in any sin that he sins' — the general noun and verb of sinning) and 20:18 ('and you sin against the LORD your God') is the WORD FOR SIN, not the sin offering's rite (Leviticus 4 — chatat's law): the runner names no offering, calls no cell of chatat; the gate's own print (FAIL EDGE refuge_war_family -> chatat [chatat] at Deut 19:15, Deut 20:18: NO DISPOSITION) — filed from the print at RUN B"}
  - {from: refuge_war_family, to: pesach, disposition: FALSE, link: none,
     why: "%s | the token census's 'firstborn' at Deut 21:15, 21:16, 21:17 is THE INHERITANCE'S FIRSTBORN — the father's first, 'the first of his strength' (Genesis 49:3 by CALL to family; Mishnah Bekhorot 8:1: for inheritance and not for the priest), not the womb's (the Passover's and the redemption's firstborn — Exodus 13:2, called through release_firstborn's the_firstling, itself Numbers 18:17's and korach's by CALL; family's own firstborn_by_call to pesach is family's edge, not this runner's); no Passover, no redemption, no plague of the firstborn here; the gate's own print (FAIL EDGE refuge_war_family -> pesach [firstborn] at Deut 21:15, Deut 21:16, Deut 21:17: NO DISPOSITION) — filed from the print at RUN B"}
''' % (W, W))
s = s[:j + 1] + EDGES + s[j + 1:]
k = s.index('  - {verse: "Deut 18:2", form: AS_WHEN, runner: courts_prophet'); l = s.index('\n', k)
POINTERS = ('''  - {verse: "Deut 19:8", form: AS_WHEN, runner: refuge_war_family, disposition: RUN_CITATION, link: reference, why: "%s | 'and if the LORD your God enlarges your border, AS HE SWORE TO YOUR FATHERS' (כאשר נשבע לאבתיך — as He swore to your fathers; the gate's own print) — THE OATH FORMULA, A RECEIPT BEHIND: the run citation of the tape's own oaths to the fathers (Genesis 22:16-18's sworn_by_himself, 26:3-4's and 28:13-14's promises — the patriarchs' lines), no register seat at 19:8 (good_land's receipt_seats(19) empty — the reading's finder), no pointer row (the readback's REFERENCE row 19:8); the three more cities a condition the tape never met (the Sifrei 185:2-3) — 15b's Deut 18:2 precedent"}
  - {verse: "Deut 19:19", form: AS_WHEN, runner: refuge_war_family, disposition: PARAMETER, link: reference, why: "%s | 'then you shall do to him AS HE PLOTTED TO DO to his brother' (כאשר זמם לעשות — as he plotted to do; the gate's own print) — not a receipt but THE MEASURE of the plotting witness's punishment: as he plotted and not as he did (the Sifrei 190:10-11; Mishnah Makkot 1:4 — the runner's parameter as_he_plotted: money for money, lashes for lashes, death for death by the second set's mouth); 14b's Deut 16:10 precedent (an AS_WHEN that is a quantity, a PARAMETER)"}
  - {verse: "Deut 20:17", form: AS_WHEN, runner: refuge_war_family, disposition: RUN_CITATION, link: reference, why: "%s | 'but you shall utterly devote them … AS THE LORD YOUR GOD COMMANDED YOU' (כאשר צוך יהוה — as the LORD commanded you; the gate's own print) — THE RECEIPT of the three chapters, BEHIND: the run citation of Deuteronomy 7:1-5's line nations_devoted on the tape (the readback's REFERENCE row 20:17 against it — tape_kind nations_devoted, first verse Deut 7:1; the six named here against the seven there, the Girgashite absent — the reading's find); the register's one seat in the three chapters (good_land's receipt_seats(20) = [17]) dispositioned in register_dispositions.yaml at the tail from the register gate's print; no pointer row (the receipt behind) — 15b's Deut 18:2 precedent"}
''' % (W, W, W))
s = s[:l + 1] + POINTERS + s[l + 1:]
open(P, 'w', encoding='utf-8').write(s); yaml.safe_load(open(P, encoding='utf-8'))
print('filed: two FALSE edges (chatat, pesach) and three pointers (19:8 RUN_CITATION, 19:19 PARAMETER, 20:17 RUN_CITATION); the yaml loads')
