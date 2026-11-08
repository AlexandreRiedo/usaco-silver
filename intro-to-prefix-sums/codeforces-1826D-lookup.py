from collections import deque
from math import inf

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))

    prefix = [0]
    for i, b in enumerate(s):
        prefix.append(max(prefix[-1], b + i))

    suffix = deque([-inf])
    for i in range(n - 1, -1, -1):
        b = s[i]
        suffix.appendleft(max(suffix[0], b - i))

    ans = 0
    for m in range(1, n - 1):
        ans = max(ans, s[m] + prefix[m] + suffix[m + 1])
    print(ans)
