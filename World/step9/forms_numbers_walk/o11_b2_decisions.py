# O11 batch B2 — THE KITZUR LAYER (Kitzur Baal HaTurim rows), decided 2026-09-08 by reading scratchpad o11_b2_p1..p3.txt whole.
BATCH = 'B2'

E7 = "E7 (the concordance pair — the same wording at two seats, the Kitzur's reading at narrative strength)"
E30 = "E30 (notarikon — the initials, finals, or rearranged letters of the verse's own words, the Kitzur's reading)"
E29 = "E29 (gematria — the letter-values, the Kitzur's reading)"
E10 = "E10 (repetition signifies — the word counted in its own passage, the Kitzur's reading)"
INK = "ink (the verse's own count or written form — the Kitzur's homily on it, no rule moved)"
I2 = "I2 (the equal decree — a rule carried on the shared wording at two seats, the Kitzur's reading at law strength)"

def DEFAULT(uid, c):
    ct = (c.get('check') or {}).get('type')
    if ct in ('final_letters', 'initial_letters', 'letters_multiset'):
        return E30
    return E7

DEFER = set()

_E10 = ['EX01-05', 'EX01-09', 'EX03-10', 'EX05-13', 'EX11-03', 'EX12-15', 'G01-04', 'G07-02', 'G16-02', 'G33-12', 'G33-13',
        'G38-30', 'G39-10', 'G39-10b', 'G48-01', 'G48-02', 'G49-10', 'G49-11', 'G49-14', 'G59-03']
_E29 = ['EX06-05', 'EX14-10', 'EX16-06', 'EX16-11', 'EX20-02', 'EX20-11', 'EX21-02', 'EX21-10', 'G27-16', 'G35-06', 'G35-07', 'G65-13']
_E30 = ['EX15-06', 'EX17-06']
_INK = ['EX02-13', 'EX03-13', 'EX06-02', 'EX07-12', 'EX09-13', 'EX10-12', 'EX12-10', 'EX15-07', 'EX16-07', 'EX17-13', 'EX18-07',
        'EX20-06', 'EX20-07', 'EX21-09', 'G08-05', 'G11-03', 'G15-01', 'G30-02', 'G30-03', 'G30-04', 'G30-05', 'G30-06', 'G30-07',
        'G30-08', 'G34-06', 'G34-07', 'G37-05', 'G38-27', 'G39-09', 'G41-17', 'G43-06', 'G43-07', 'G45-11', 'G45-12', 'G45-16',
        'G46-19', 'G46-20', 'G51-17', 'G07-03', 'L19-03']
_I2 = ['EX10-04', 'EX16-09', 'EX16-10', 'EX19-10', 'EX21-03', 'EX21-05']

EXCEPTIONS = {}
for i in _E10: EXCEPTIONS[i] = E10
for i in _E29: EXCEPTIONS[i] = E29
for i in _E30: EXCEPTIONS[i] = E30
for i in _INK: EXCEPTIONS[i] = INK
for i in _I2: EXCEPTIONS[i] = I2
EXCEPTIONS.update({
    'EX12-11': "M-22 (the run read back into the spec — the performance verse's changed order taught as the order-indifference rule, the Kitzur's reading)",
    'EX06-14': "E28 (from the preceding — the juxtaposition across the portion's seam read, the Kitzur; the ciphers named beside)",
    'EX21-07': "E10 (repetition signifies — the doubled heal-verb read as the physician's license, the case shelf's derivation at law strength)",
    'EX08-02': "E7 (the concordance pair — the bring-up imperative at two seats; the furnace's a-fortiori, E5, rides beside)",
    'EX19-06': "E7 (the concordance pair — the treasure-word's four seats; the finals' anagram, E30, rides beside)",
    'EX20-01': "E7 (the concordance pair — the brought-you-out word at three seats; the throne's letter-value, E29, rides beside)",
    'EX18-01': "E7 (the concordance pair — the did-God phrase at two seats; the name's letter-value, E29, rides beside)",
    'G37-03': "E7 (the concordance pair — the speak-word's Scripture twin; the letter-sum of a hundred, E29, rides beside)",
    'G41-11': "E7 (the concordance pair — the two brought brides; the letter-count of twenty-four, E29, rides beside)",
    'G54-05': "E7 (the concordance pair — the two told flights; the informer's letter-sum, E29, rides beside)",
    'G46-16': "E7 (the concordance pair — the deceit-word at two seats; measure for measure, E27, the reading)",
    'G62-09': "E7 (the concordance pair — the bring-him-down word at two seats; measure for measure, E27, the reading)",
    'G44-17': "E7 (the concordance pair — the filled-them word's Scripture twin; measure for measure, E27, the reading)",
    'G37-04': "E7 (the concordance pair — the drive-out imperative at two seats; measure for measure, E27, the reading)",
    'EX14-07': "E7 (the concordance pair — the heaviness-word's receipt in the corpus; measure for measure, E27, the reading)",
    'G16-01': "E7 (the concordance pair — the four bare headers; each disqualifying what precedes it, E28, the reading)",
})
