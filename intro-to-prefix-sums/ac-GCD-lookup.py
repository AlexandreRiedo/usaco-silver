from math import gcd

N = int(input())
A = list(map(int, input().split()))

prefix, suffix = [0] * (N + 2), [0] * (N + 2)
for idx, num in enumerate(A, 1):
    prefix[idx] = gcd(prefix[idx - 1], num)
for idx, num in enumerate(reversed(A), 2):
    suffix[-idx] = gcd(suffix[-idx + 1], num)

ans = 0
for i in range(1, N + 1):
    ans = max(ans, gcd(prefix[i - 1], suffix[i + 1]))
print(ans)
