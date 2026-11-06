import itertools
from collections import defaultdict

with open("div7.in") as fin:
    N = int(fin.readline())
    cows = [int(cow) for cow in fin]

prefix = list(itertools.accumulate(cows, lambda a, b: (a + b) % 7))
pos = defaultdict(list)
for idx, num in enumerate(prefix):
    pos[num].append(idx)

ans = 0
for indices in (l for l in pos.values() if len(l) > 1):
    ans = max(ans, indices[-1] - indices[0])

with open("div7.out", "w") as fout:
    fout.write(f"{ans}\n")
