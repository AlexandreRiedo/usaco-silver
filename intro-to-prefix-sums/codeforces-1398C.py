import itertools
from random import randint

from rich import print as rprint

for _ in range(int(input())):
    n = int(input())
    # a = [int(x) for x in input()]
    a = [randint(0, 9) for _ in range(10**5)]
    # rprint(f"[pink]{a}")
    pre = [0] + list(itertools.accumulate(a))
    rprint(f"[magenta]{pre}")

    ans = 0
    for r in range(n + 1):
        for l in range(r):
            score, size = pre[r] - pre[l], (r - l)
            if score == size:
                ans += 1
                rprint(f"[green]{l + 1} {r}")
    rprint(ans)
    rprint()

"""
1
10
9561920382

1
100
7716951256832213820430838838842605059165153656715680983178224523910543679234857209348572110293845722

1
100000
RNG!
"""
