#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 20 — CHAPTER 32, THE SONG (LEAN, 2026-09-27): ONE LEAN MEASURE for the chapter (the facts the ink's asserts will be typed from its print,
# never typed): the kin by computation for the 52 verses (the three closest), the twins diffed, the formulas' seats over the Torah and the Bible, Onkelos's renderings over
# the book, the frames, the register and the parser (THE FALSE EIGHT at 32:15 and the joined thousand at 32:30), the prior reads. Sitting 19's form (ch29_measure_lean.py)
# printed COMPACT. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad and World/step9.
from ch32_ink import *
print('==== A. THE KIN BY COMPUTATION (the closest three re-scored in order; shared tokens outside the stop list)')
for c, v in SPAN: print(f'  {c}:{v}:', KINC[(c, v)][:3])
print('==== B. THE TWINS DIFFED (shared tokens in order / the longest run)')
PAIRS = [((32, 1), ('Isa', 1, 2)), ((32, 1), ('Deut', 31, 28)), ((32, 1), ('Deut', 4, 26)), ((32, 1), ('Deut', 30, 19)), ((32, 1), ('Ps', 50, 4)), ((32, 2), ('Deut', 33, 28)), ((32, 3), ('Ps', 29, 2)), ((32, 4), ('Ps', 92, 16)), ((32, 4), ('Deut', 32, 15)), ((32, 4), ('Deut', 32, 18)), ((32, 4), ('Deut', 32, 31)),
         ((32, 5), ('Deut', 32, 20)), ((32, 6), ('Deut', 32, 15)), ((32, 6), ('Exod', 4, 22)), ((32, 7), ('Deut', 4, 32)), ((32, 7), ('Exod', 13, 14)), ((32, 8), ('Gen', 11, 8)), ((32, 8), ('Gen', 10, 32)), ((32, 8), ('Gen', 46, 27)), ((32, 9), ('Deut', 9, 29)), ((32, 9), ('Deut', 4, 20)), ((32, 10), ('Deut', 8, 15)), ((32, 10), ('Ps', 17, 8)),
         ((32, 11), ('Exod', 19, 4)), ((32, 12), ('Num', 23, 9)), ((32, 13), ('Deut', 33, 29)), ((32, 13), ('Deut', 8, 15)), ((32, 13), ('Ps', 81, 17)), ((32, 14), ('Gen', 49, 11)), ((32, 14), ('Deut', 3, 1)), ((32, 15), ('Deut', 31, 20)), ((32, 15), ('Deut', 8, 14)), ((32, 15), ('Deut', 33, 5)), ((32, 15), ('Deut', 33, 26)),
         ((32, 16), ('Deut', 31, 16)), ((32, 17), ('Lev', 17, 7)), ((32, 17), ('Deut', 29, 25)), ((32, 17), ('Deut', 32, 21)), ((32, 18), ('Deut', 32, 4)), ((32, 19), ('Deut', 31, 16)), ((32, 20), ('Deut', 31, 17)), ((32, 20), ('Deut', 31, 18)), ((32, 20), ('Deut', 32, 5)), ((32, 21), ('Deut', 31, 20)), ((32, 21), ('Deut', 32, 16)),
         ((32, 22), ('Ps', 18, 8)), ((32, 22), ('Deut', 29, 19)), ((32, 23), ('Deut', 28, 15)), ((32, 24), ('Lev', 26, 22)), ((32, 25), ('Lev', 26, 25)), ((32, 25), ('Deut', 28, 25)), ((32, 26), ('Deut', 9, 14)), ((32, 27), ('Deut', 9, 28)), ((32, 27), ('Num', 14, 16)), ((32, 28), ('Deut', 4, 6)), ((32, 29), ('Deut', 5, 29)),
         ((32, 30), ('Lev', 26, 8)), ((32, 30), ('Deut', 28, 25)), ((32, 30), ('Josh', 23, 10)), ((32, 30), ('Deut', 32, 31)), ((32, 31), ('Deut', 32, 4)), ((32, 32), ('Deut', 29, 22)), ((32, 32), ('Gen', 19, 24)), ((32, 33), ('Deut', 32, 24)), ((32, 34), ('Job', 14, 17)), ((32, 35), ('Ps', 94, 1)), ((32, 35), ('Deut', 32, 41)),
         ((32, 36), ('Ps', 135, 14)), ((32, 36), ('Deut', 32, 1)), ((32, 37), ('Judg', 10, 14)), ((32, 38), ('Deut', 32, 17)), ((32, 38), ('Lev', 3, 16)), ((32, 39), ('Isa', 45, 5)), ((32, 39), ('1Sam', 2, 6)), ((32, 39), ('Deut', 4, 35)), ((32, 40), ('Gen', 14, 22)), ((32, 40), ('Exod', 6, 8)), ((32, 41), ('Lev', 26, 25)), ((32, 41), ('Deut', 32, 35)),
         ((32, 42), ('Deut', 32, 25)), ((32, 43), ('Ps', 79, 10)), ((32, 43), ('Deut', 32, 1)), ((32, 43), ('Deut', 32, 35)), ((32, 44), ('Deut', 31, 30)), ((32, 44), ('Deut', 31, 22)), ((32, 44), ('Num', 13, 16)), ((32, 45), ('Deut', 31, 1)), ((32, 45), ('Deut', 31, 30)), ((32, 46), ('Deut', 6, 6)), ((32, 46), ('Deut', 11, 18)), ((32, 46), ('Deut', 31, 12)),
         ((32, 47), ('Deut', 30, 20)), ((32, 47), ('Deut', 11, 9)), ((32, 47), ('Deut', 4, 40)), ((32, 48), ('Gen', 7, 13)), ((32, 48), ('Exod', 12, 17)), ((32, 48), ('Deut', 31, 2)), ((32, 49), ('Num', 27, 12)), ((32, 49), ('Deut', 34, 1)), ((32, 49), ('Num', 33, 47)), ((32, 50), ('Num', 20, 26)), ((32, 50), ('Num', 27, 13)), ((32, 50), ('Deut', 34, 5)),
         ((32, 51), ('Num', 20, 12)), ((32, 51), ('Num', 27, 14)), ((32, 51), ('Num', 20, 24)), ((32, 52), ('Deut', 34, 4)), ((32, 52), ('Deut', 3, 27)), ((32, 52), ('Deut', 31, 2)), ((32, 52), ('Num', 20, 12))]
for a, b in PAIRS:
    A_ = ('Deut',) + a
    if b not in by: print(f'  {a[0]}:{a[1]} vs {b[0]} {b[1]}:{b[2]}: NOT IN THE DB'); continue
    print(f'  {a[0]}:{a[1]} vs {b[0]} {b[1]}:{b[2]}: shared {SHN(A_, b)} of {len(words(*A_))}/{len(words(*b))}; run {SHARED(A_, b)}')
print('==== C. THE FORMULAS OVER THE TORAH AND THE BIBLE (phrase seats by consonants; the lists cut to fourteen, the counts whole)')
def PC(*seq):
    t, b = P(*seq, books=T), P(*seq, books=None); return f'Torah {len(t)} {t[:14]} | Bible {len(b)} {b[:14]}'
Q = [('give ear, O heavens (haazinu ha-shamayim)', ('האזינו', 'השמים')), ('and hear, O earth (ve-tishma ha-aretz)', ('ותשמע', 'הארץ')), ('the Rock (ha-tzur)', ('הצור',)), ('a perverse and crooked generation (dor ikkesh u-fetaltol)', ('דור', 'עקש', 'ופתלתל')), ('the apple of His eye (ke-ishon eino)', ('כאישון', 'עינו')), ('as an eagle (ke-nesher)', ('כנשר',)), ('honey from the rock (devash mi-sela)', ('דבש', 'מסלע')), ('Jeshurun (yeshurun)', ('ישרון',)),
     ('I will hide My face (astirah fanai)', ('אסתירה', 'פני')), ('vengeance and recompense (nakam ve-shillem)', ('נקם', 'ושלם')), ('vengeance is Mine (li nakam)', ('לי', 'נקם')), ('I kill and I make alive (amit va-achayeh)', ('אמית', 'ואחיה')), ('I lift My hand to heaven (esa el shamayim yadi)', ('אשא', 'אל', 'שמים', 'ידי')), ('the selfsame day (be-etzem ha-yom ha-zeh)', ('בעצם', 'היום', 'הזה')), ('the mountain of the Abarim (har ha-avarim)', ('הר', 'העברים')), ('Mount Nebo (har nevo)', ('הר', 'נבו')),
     ('gathered to your people (ve-heasef el ammekha)', ('והאסף', 'אל', 'עמיך')), ('as Aaron your brother died (kaasher met aharon achikha)', ('כאשר', 'מת', 'אהרן', 'אחיך')), ('Meribath-kadesh (merivat kadesh)', ('מריבת', 'קדש')), ('the wilderness of Zin (midbar tzin)', ('במדבר', 'צן')), ('you shall not go there (ve-shammah lo tavo)', ('ושמה', 'לא', 'תבוא')), ('and no god beside Me (ve-ein elohim immadi)', ('ואין', 'אלהים', 'עמדי')), ('Sodom and Gomorrah (sedom va-amorah)', ('סדם', 'ועמרה')), ('the blood of the grape (dam enav)', ('דם', 'ענב')),
     ('gods they knew not (elohim lo yedaum)', ('אלהים', 'לא', 'ידעום')), ('the days of old (yemot olam)', ('ימות', 'עולם')), ('the Most High (elyon)', ('עליון',)), ('this song (ha-shirah ha-zot)', ('השירה', 'הזאת')), ('set your heart (simu levavkhem)', ('שימו', 'לבבכם')), ('it is your life (hu chayyekhem)', ('הוא', 'חייכם')), ('you shall prolong days (taarikhu yamim)', ('תאריכו', 'ימים')), ('the number of the children of Israel (le-mispar bene yisrael)', ('למספר', 'בני', 'ישראל')), ('who made him (asahu)', ('עשהו',)), ('the sword without (mi-chutz ... cherev)', ('מחוץ', 'תשכל', 'חרב')), ('a nation void of counsel (goy oved etzot)', ('גוי', 'אבד', 'עצות')), ('the venom of asps (rosh petanim)', ('ראש', 'פתנים')), ('by the hand of Moses (be-yad moshe)', ('ביד', 'משה')), ('in the ears of the people (be-oznei ha-am)', ('באזני', 'העם'))]
for name, seq in Q: print(f'  {name}: {PC(*seq)}')
print('  single tokens (the chapter) — "rock" (tzur forms):', [(c, v, x) for c, v in SPAN for x in W(c, v) if x in ('צור', 'הצור', 'צורם', 'וצור', 'צורנו', 'כצורנו', 'צר')], '| "God" (el / eloah / elohim forms):', [(c, v, x) for c, v in SPAN for x in W(c, v) if x in ('אל', 'אלוה', 'אלהים', 'אלהי', 'אלהיו', 'אלהיהם', 'אלה')], '| the Name bare / with lamed / with vav:', [(c, v, x) for c, v in SPAN for x in W(c, v) if x in ('יהוה', 'ליהוה', 'ויהוה')])
print('  "Sheol" / "Jeshurun" / "Bashan" / "Hoshea" / "Nebo" / "Meribah" seats:', [(c, v, x) for c, v in SPAN for x in W(c, v) if x in ('שאול', 'ישרון', 'בשן', 'והושע', 'הושע', 'נבו', 'מריבת')], '| "vengeance" (nakam forms):', [(c, v, x) for c, v in SPAN for x in W(c, v) if x.startswith(('נקם', 'ונקם'))], '| "the Most High":', [(c, v, x) for c, v in SPAN for x in W(c, v) if x == 'עליון'])
print('  "you shall not / not" (the negations):', {c: sum(1 for v in range(1, NV[c] + 1) for x in W(c, v) if x in ('לא', 'ולא')) for c in CHS}, '| "for/when" (ki) count:', sum(1 for c, v in SPAN for x in W(c, v) if x == 'כי'), '| "if" (im) seats:', [(c, v) for c, v in SPAN if 'אם' in W(c, v) or 'ואם' in W(c, v)], '| "lest" (pen) seats:', [(c, v) for c, v in SPAN if 'פן' in W(c, v)], '| "saying" seats:', [(c, v) for c, v in SPAN if 'לאמר' in W(c, v)])
print('  32:8 tokens:', W(32, 8), '| 32:15:', W(32, 15), '| 32:30:', W(32, 30), '| 32:43:', W(32, 43), '| 32:44:', W(32, 44), '| 32:48:', W(32, 48), '| 32:13 (the store one more):', W(32, 13))
print('==== D. ONKELOS OVER THE BOOK (the plain Aramaic of every export row through NFKC; EXPORT verse numbers)')
for name, sub in [('the Rock — takifa (the Mighty One)', 'תקיפ'), ('the Shekhinah', 'שכינת'), ('the Memra (the Word)', 'מימר'), ('other gods — the errors (taavat)', 'טעו'), ('vengeance — puranuta (retribution)', 'פורענ'), ('hide the face — aslek (I will remove)', 'אסלק'), ('the song — tushbachta', 'תושבח'), ('the Torah — oraita', 'אורית'), ('the world — alma (the age / the world to come)', 'עלמ'), ('the mountain — tura', 'טור'), ('Meribah — matzuta (the strife)', 'מצות'), ('demons — shedin', 'שידין'), ('the eagle — nishra', 'נשר'), ('Jeshurun rendered Israel (yisrael in 32:15)', 'ישראל'), ('Sheol', 'שאול'), ('the fat — tarba', 'תרב')]:
    s = SEATS(sub); print(f'  {name}: {len(s)} {s[:24]}')
for c, v in ((32, 1), (32, 4), (32, 8), (32, 9), (32, 10), (32, 12), (32, 14), (32, 15), (32, 17), (32, 20), (32, 21), (32, 22), (32, 24), (32, 30), (32, 32), (32, 35), (32, 36), (32, 39), (32, 40), (32, 43), (32, 44), (32, 48), (32, 50), (32, 51)):
    print(f'  {c}:{v} HE {len(W(c, v))} ARM {len(ARM(c, v))}:', ' '.join(ARM(c, v)))
print('==== E. THE FRAMES, THE REGISTER AND THE PARSER')
MO = {(c, v): [(x, m) for x, m in by[('Deut', c, v)]] for c, v in SPAN}
print('  imperatives:', [(c, v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]v', m)], '| infinitive absolutes:', [(c, v, x) for c, v in SPAN for x, m in MO[(c, v)] if m and re.search(r'V[a-zA-Z]a$', m)])
print('  the morph codes at 32:1 and 32:7 (the dump\'s imperative scan printed empty — the codes read):', MO[(32, 1)][:3], MO[(32, 7)][:4])
for c in CHS:
    print(f'  chapter {c}: the Name bare / with lamed / "your God" pairs:', sum(1 for v in range(1, NV[c] + 1) for x in W(c, v) if x == 'יהוה'), sum(1 for v in range(1, NV[c] + 1) for x in W(c, v) if x == 'ליהוה'), [v for v in range(1, NV[c] + 1) if any(a == 'יהוה' and b == 'אלהיך' for a, b in zip(W(c, v), W(c, v)[1:]))])
with contextlib.redirect_stdout(io.StringIO()):
    import register_census as RC
    _ink = RC.read_ink()
try:
    print('  the register on Deut 32 — receipts:', [k for k in RC.receipts(_ink) if k[0] == 'Deut' and k[1] in CHS], '| footers:', [x for x in RC.footers(_ink) if x[0][0] == 'Deut' and x[0][1] in CHS], '| headers:', [x for x in RC.register_headers(_ink) if x[0][0] == 'Deut' and x[0][1] in CHS])
except Exception as e:
    print('  the register (the raw shapes):', repr(e)[:120], '| footers naming 32:', [x for x in RC.footers(_ink) if re.search(r"'Deut', 32", repr(x))][:4], '| headers naming 32:', [x for x in RC.register_headers(_ink) if re.search(r"'Deut', 32", repr(x))][:4])
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
PARSE = {}
for c, v in SPAN:
    vw = CS.verse_words('Deut', c, v); n, o = CS.ink_numbers(vw), CS.ink_ordinals(vw); marked = [t for t in vw if t[-1] in '#~^%@|*']
    if n or o or marked: PARSE[(c, v)] = (n, o, marked)
print('  the parser\'s hits:', PARSE, '| 32:15 "grew fat" (the false eight):', CS.verse_words('Deut', 32, 15)[0:5], '| 32:30 "one … a thousand … two … ten thousand":', CS.verse_words('Deut', 32, 30)[0:7], '| 32:8 "the number":', CS.verse_words('Deut', 32, 8)[-3:], '| 32:48 "the selfsame day":', CS.verse_words('Deut', 32, 48)[0:7])
print('==== F. THE PRIOR READS (computed from the ledgers)')
print('  spine rows read before:', len(SPINE_PRIOR), sorted({(p, r) for _, p, r in SPINE_PRIOR}), '| the ledgers:', sorted({f for f, _, _ in SPINE_PRIOR}))
print('  outside rows read before:', {k: v for k, v in PRIOR_READ.items()}, '| fresh:', FRESH)
print('  ledgers with an Onkelos row of Deut 32-34 or the Prophets (never read ahead — expected none):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Deut 3[2-4]|Josh|Judg|1Sam|2Sam|1Kgs|2Kgs|Isa|Jer|Ezek):', t, re.M)))
PREFS = [('exo_15', r'Exod 15:'), ('exo_19', r'Exod 19:'), ('gen_10', r'Gen 10:'), ('gen_11', r'Gen 11:'), ('gen_49', r'Gen 49:'), ('lev_26', r'Lev 26:'), ('num_20', r'Num 20:'), ('num_27', r'Num 27:'), ('num_33', r'Num 33:'), ('deu_03', r'Deut 3:'), ('deu_04', r'Deut 4:'), ('deu_08', r'Deut 8:'), ('deu_26', r'Deut 28:'), ('deu_29', r'Deut 31:')]
KIN = [(f, n) for f in sorted(LED) for pref, pat in PREFS if f.startswith(pref) for n in [len(re.findall(r'^- Onkelos ' + pat, LED[f], re.M))] if n]
print('  the kin ledgers\' Onkelos row counts:', KIN)
print('  the store mismatches:', STORE_MISMATCH, '| token counts:', {c: sum(len(W(c, v)) for v in range(1, NV[c] + 1)) for c in CHS}, '| distinct glosses:', {c: len({g for (cc, v) in SG if cc == c for _, _, g in SG[(cc, v)]}) for c in CHS}, '| "?" glosses:', [(cc, v, hp) for (cc, v) in SG for _, hp, g in SG[(cc, v)] if g == '?'])
print('THE LEAN MEASURE PRINTED')
