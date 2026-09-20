# the one lint flag on a carried note (chapter 6's docket's 'the halakha per R. Akiva'): a gloss beside the word is display, inserted at the carry
SP = '<scratch>'
p = f'{SP}/ch11_credit_carry.py'; t = open(p, encoding='utf-8').read()
old = "        l, v, n = resolved[addr]; out.append("
new = "        l, v, n = resolved[addr]; n = n.replace('the halakha per R. Akiva', 'the halakha (the ruling) per R. Akiva'); out.append("
assert t.count(old) == 1; t = t.replace(old, new); open(p, 'w', encoding='utf-8').write(t); print('carry glosses the one flagged word')
