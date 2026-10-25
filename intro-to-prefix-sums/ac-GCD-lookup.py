from itertools import islice
from math import gcd

N = int(input())
A = list(map(int, input().split()))

prefix, suffix = [0], [0]
for i in range(N):
    prefix.append(gcd(*islice(A, i)))
    suffix.append(gcd(*islice(A, i, N)))
    # rprint(f"[magenta]{list(islice(A, i))} {gcd(*islice(A, i))}")
    # rprint(f"[blue]{list(islice(A, i, N))} {gcd(*islice(A, i, N))}")
prefix.append(0)
suffix.append(0)

# rprint()
# rprint(f"{prefix=}")
# rprint(f"{suffix=}")
# rprint()

ans = 0
for i in range(1, N + 1):
    ans = max(ans, gcd(prefix[i], suffix[i + 1]))
    # rprint(f"[red]{prefix[i]} {suffix[i + 1]} {gcd(prefix[i], suffix[i + 1])}")
# rprint(f"[green]{ans}")
print(ans)
