import itertools
import math
from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input()]

    pre = [0] + list(itertools.accumulate(a))
    sum_dist = defaultdict(list[int])
    ans = 0

    for i in range(n + 1):
        sum_dist[pre[i] - i].append(i)

    for values in (x for x in sum_dist.values() if len(x) > 1):
        ans += math.comb(len(values), 2)

    print(ans)
