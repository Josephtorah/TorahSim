import re
F='World/step9/forms_deuteronomy_walk'
s=open(F+'/patch_seq_literals_ch15.py',encoding='utf-8').read().split('\n')
print('---- patch_seq_literals_ch15.py lines 50-72 ----')
for i in range(49,72):
    l=s[i]; print(f'{i+1}: ' + (l if len(l)<=1400 else l[:800]+' ...[CUT %d]... '%len(l)+l[-300:]))
L=open('World/step9/cold_run_sequence.py',encoding='utf-8').read().split('\n')
print('---- the tape: the literal lines whole ----')
for i,l in enumerate(L,1):
    t=l.strip()
    if re.match(r'^(RUN|PREVIOUS_RUN|NEWEST_RUNNER|PLACEMENT|CENSUS\w*) = ', l) or re.match(r'^\s+\d+\)\s+#', l) or "'DG9 MATCH'" in l or t.startswith("cp('DB7 ") or "the story's dates" in l or re.match(r'^\s*CENSUS', l):
        print(f'{i}: ' + (l if len(l)<=2600 else l[:1500]+' ...[CUT %d]... '%len(l)+l[-600:]))
