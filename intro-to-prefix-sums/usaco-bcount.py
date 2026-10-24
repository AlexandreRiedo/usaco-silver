import itertools

with open("bcount.in", "r") as fin, open("bcount.out", "w") as fout:
    N, Q = map(int, fin.readline().split())

    cows = []
    for _ in range(N):
        cows.append(int(fin.readline()))
    pre1 = [0] + [x for x in itertools.accumulate(c == 1 for c in cows)]
    pre2 = [0] + [x for x in itertools.accumulate(c == 2 for c in cows)]
    pre3 = [0] + [x for x in itertools.accumulate(c == 3 for c in cows)]

    for _ in range(Q):
        a, b = map(int, fin.readline().split())
        fout.write(
            f"{pre1[b] - pre1[a - 1]} {pre2[b] - pre2[a - 1]} {pre3[b] - pre3[a - 1]}\n"
        )
