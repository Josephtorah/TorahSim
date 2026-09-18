# THE WHOLE-ROW FIX, part (d) (2026-09-17): the corrections found by reading the long rows of 2b's and 1b's dockets WHOLE against the verdict each
# received. CH4 / DEU = {address: (new verdict or None if unchanged, "what the cut had wrong / what the whole row adds")}. Written chunk by chunk,
# each chunk's findings on disk before the next chunk is read. The committed dockets are append-only: these go into an APPENDED section.
CH4 = {}
DEU = {}
# ---- ch4 chunk 1 (rows 1-38 of 114) ----
CH4.update({
 'Berakhot 21b:15': ('DERIVATION', "the note had R. Yehuda needing 4:9-10's juxtaposition for R. Yehoshua ben Levi's statement on awe and fear — that is Berakhot 22a:4's baraita; THIS row's other statement is 'one who teaches his son Torah, the verse ascribes to him as if he received it from Horeb' (4:9 'make them known to your sons' then 4:10 'the day you stood at Horeb') — the same juxtaposition Kiddushin 30a teaches, so R. Yehuda cannot spend it on the emission bar: a DERIVATION, not a dispute (F2 take_heed_lest_you_forget, the DATA row the_teach_your_sons)"),
 'Gittin 12a:11': (None, "the note stated the row's hypothesis as its ruling — 'act for him that he have life, the surplus of his labor his'; the whole row REJECTS it: the baraita teaches that no such obligation applies even to the slave exiled to a city of refuge, the surplus the master's (the hook from 4:42 raised and refused; the verdict DERIVATION stands on the hook)"),
 'Gittin 88a:17': (None, "the note counted R. Ammi's seven dynasties from 'seven verbs'; the whole row counts them from 'you will beget' (singular, one generation) and 'children' (plural, two) said three times — 1 + 3 × 2 = 7 generations; the crowns' line 'seven dynasties from the seven verbs' is corrected by this section"),
 'Tosefta Rosh Hashanah 2:11': ('DISPUTE', "the whole row carries the same dispute as Rosh Hashanah 32b:17 (DISPUTE there) with R. Yehuda's REASON — 6:4 and 4:39 are not said with the kingship verses because no 'shofar' is in them; the note already names the DATA row the_creed's two arms: the verdict reads DISPUTE like its Talmud twin"),
})
CH4_NOTES_1 = ["Bekhorot 29a:8 — the row's third derivation: one who learned for pay may not therefore teach for pay ('do not sell it')", "Megillah 31b:2 — the reading of 4:25-40 on the Ninth of Av is Abaye's 'nowadays everyone is accustomed', not the baraita's 'some say' (that is Numbers 14:27)", "Nedarim 37a:2 — the row is the Gemara's QUESTION (why should Bible differ from midrash when 4:14 and 4:5 make both free), the answer in the rows after", "Tosefta Sanhedrin 4:5 — the row runs on past 4:14 to the script's change and return (Assyrian), the king's two scrolls (17:18) and Joshua's 'do not let it depart' — other engines"]
# ---- ch4 chunk 2 (rows 39-76 of 114) ----
CH4.update({
 'Sanhedrin 89a:2': (None, "the note gave the row's CHALLENGE as its resolution — 'a fifth placed beside stands alone, five made spoil from the outset'; the whole row answers it by R. Zeira: an outer compartment not exposed to the air makes the head tefillin unfit, so a fifth compartment ALWAYS compromises the mitzva, placed beside or made as one; the crowns' line 'made as one (five made) against a fifth placed beside (stands alone)' is corrected by this section; the verdict LAW stands (F1 add_nothing — the fifth compartment)"),
 'Eruvin 96a:6': (None, "the note put R. Akiva's reading of Exodus 13:10 as the Passover's on this row; the row's baraita is R. YOSEI HAGELILI's — 'from days to days' excludes the nights and its mem excludes Shabbat and the festivals from the tefillin; R. Akiva's reading of the verse as the Passover's is the row after (credited; the tefillin's time chapter 6's engine)"),
})
CH4_NOTES_2 = ["Mishnah Rosh Hashanah 2:8 — the row runs on to the two witness incidents (R. Yochanan ben Nuri, R. Dosa ben Horkinas) — the calendar engine's", "Sanhedrin 88b:15 — R. Oshaya's rule is in accordance with R. Yehuda's on the rebellious elder"]
# ---- ch4 chunk 3 (rows 77-114 of 114): no correction ----
CH4_NOTES_3 = ["Rosh Hashanah 24b:3 — Abaye's ground: the Torah forbade only the four faces of the Chariot together (the sun and the moon not attendants of that kind)", "Makkot 9b:18 — 'you shall divide into three' (19:3): the three cities as three lines cutting the land's length into four equal parts"]
# THE CELL TYPED FROM THE CUT (cold_run_obey_horeb.py, F1 the_exhortation, the ask 'add_beside' and the person 'the-fifth-beside' → exempt; the move at
# 'the_law_bal_tosif' and the move on 4:25 'seven dynasties from the seven verbs'): to be retyped from the whole rows after the reading of 1b's rows.
# ---- deu chunk 1 (rows 1-54 of 215): no correction ----
DEU_NOTES_1 = ["Mishnah Sanhedrin 4:1 — the row's tail: capital cases not judged on the eve of Shabbat or a festival (the two-day rule)", "Mishnah Sanhedrin 3:6 — the row's tail: a split court adds judges (the abstainer not a member)"]
# ---- deu chunks 2-3 (rows 55-162 of 215): no correction ----
DEU_NOTES_2 = ["Sanhedrin 6b:15 — the row's tail: Rav rules as R. Yehoshua ben Korcha, a mitzva to mediate (Rav Huna's 'judgment or compromise?' the Gemara's question on it)", "Sanhedrin 16b:11 — the row's tail: R. Yehuda one court over all the appointments; Rabban Shimon ben Gamliel a tribe judges its own"]
# ---- deu chunk 4 (rows 163-215 of 215): no verdict changed ----
DEU.update({
 'Makkot 10a:13': (None, "the credited note said 'protection from the evil inclination'; the whole row's second reading of R. Yochanan is protection from the ANGEL OF DEATH (Rav Chisda's unceasing study; chapter 4's docket has it right); the verdict CONTEXT stands"),
})
