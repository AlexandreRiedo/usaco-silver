import itertools


def score(l1, l2, idx):
    return l1[idx] + (l2[-1] - l2[idx])


with open("hps.in") as fin, open("hps.out", "w") as fout:
    N = int(fin.readline())
    gestures = [fin.readline().strip() for _ in range(N)]

    preH = [0] + [x for x in itertools.accumulate(g == "H" for g in gestures)]
    preP = [0] + [x for x in itertools.accumulate(g == "P" for g in gestures)]
    preS = [0] + [x for x in itertools.accumulate(g == "S" for g in gestures)]

    ans = max(preH[-1], preP[-1], preS[-1])
    for idx in range(N + 1):
        HP = score(preH, preP, idx)
        HS = score(preH, preS, idx)
        PH = score(preP, preH, idx)
        PS = score(preP, preS, idx)
        SH = score(preS, preH, idx)
        SP = score(preS, preP, idx)
        ans = max(ans, HP, HS, PH, PS, SH, SP)

    fout.write(f"{ans}\n")
