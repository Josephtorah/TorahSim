# the recon's print cut to what the design reads: (1) the runners' kin lines, (2) thirteen kin runners' defs/asks/DATA, (3) the one-line kind/effect rows on a tight regex + six rows whole, (4), (6), (7) whole, (5) without the log rows
import re, os
SP = os.path.dirname(os.path.abspath(__file__))
t = open(f'{SP}/ch13_recon.out', encoding='utf-8').read()
secs = re.split(r'^(?====+ \(\d\))', t, flags=re.M)
out = []
FOCUS = ('ordinances', 'erection', 'sanctions', 'lev24', 'temurah', 'mekoshesh', 'shelach', 'chukat', 'balak', 'beha', 'mamre', 'seven_nations', 'place_name', 'holiness', 'obey_horeb')
KW = re.compile(r'prophet|ston|\bban|devot|herem|test|idol|gods|calf|cloud|dream|sword|purge|anger|mercy|city|witness|entic|incit|redeem|cleave|voice|sacrific|blasphem|molech|wood|high_hand|hormah|peor|akedah|isaac|sign|wonder|kill|death|execut|strangl|burn|karet|curse|rebel|fear|serve|walk|other', re.I)
K3 = re.compile(r'ston|devot|herem|purge|idol|gods|prophet|dream|test|sacrific|calf|cloud|blasphem|molech|wood|karet|death|execut|strangl|burn|curse|rebellion|witness|city|sword|anger|mercy|entic|seduc|ban\b|banned|redeem|hormah|peor|fear', re.I)
WHOLE = ('stoned', 'sacrificed_to_gods', 'karet_cut_off', 'purge_deadline', 'devoted', 'herem', 'name_cursed', 'burned_by', 'strangled', 'death_by_heaven', 'seed_given_to_molech', 'sorcery_done', 'wood_gathered', 'high_hand', 'idolat')
for s in secs:
    if not s.strip(): continue
    ls = s.split('\n'); head = ls[0]; tag = head[:12]
    if '(1)' in tag:
        out.append(head)
        for i, l in enumerate(ls):
            if l.startswith('  -- '):
                kin = []
                for x in ls[i + 1:]:
                    if x.startswith('     '): kin.append(x[:190])
                    else: break
                if kin: out.append(l[:150]); out.extend(kin[:14])
            elif l.startswith('  THE KIN RUNNERS') or l.startswith('  modules imported'): out.append(l[:700])
    elif '(2)' in tag:
        out.append(head)
        for blk in re.split(r'^(?=====+ [a-z_0-9]+: \d+ defs)', s, flags=re.M)[1:]:
            name = re.match(r'==== ([a-z_0-9]+):', blk).group(1)
            if name not in FOCUS: continue
            bl = blk.split('\n'); keep = [bl[0][:260]]
            keep += [l[:200] for l in bl[1:] if (' asks ' in l and KW.search(l)) or 'DATA keys' in l or l.strip().startswith('imports:') or l.strip().startswith('broad counts')]
            out.extend(keep[:14])
    elif '(3)' in tag:
        for l in ls:
            if l.startswith('  a kind row whole') or l.startswith('  an effect row'):
                if any(w in l[:60] for w in WHOLE): out.append(l[:480])
            elif l.startswith('    '):
                if K3.search(l[:48]): out.append(l[:160])
            else: out.append(l[:170])
    elif '(5)' in tag:
        for l in ls:
            if l.startswith('    ') and ' day ' in l[:16]: continue
            out.append(l[:230])
    else:
        out.extend(l[:280] for l in ls)
x = '\n'.join(out)
open(f'{SP}/ch13_recon_excerpt.txt', 'w', encoding='utf-8').write(x)
print('excerpt', len(x), 'bytes;', len(out), 'lines')
