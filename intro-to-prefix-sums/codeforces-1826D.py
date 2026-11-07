from itertools import islice

for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))

    ans = 0
    for l in range(n - 2):
        for r in range(l + 3, n + 1):
            sights = sorted(islice(b, l, r), reverse=True)
            ans = max(ans, sum(islice(sights, 3)) - (r - 1 - l))
    print(ans)

"""
import random

n = 5
print(1)
print(n)
print(*(random.randint(1,9) for _ in range(n)), sep=" ")
"""

"""
1
5
4 1 5 1 7
"""

"""
9 8 7 6 5 4
9 8 7 -> 24 - (3-1) = 22

5 1 4 2 3
-10--
  --7--
    --9--

5 1 4 2 3
-8---
---8---
----8----

5 1 4 2 3
5 0 2 1 0 (factor in the distance)

9 8 7 6 5 4
9 7 5 3 1 0

1   1   1   1
1   0   -1  -2
"""
