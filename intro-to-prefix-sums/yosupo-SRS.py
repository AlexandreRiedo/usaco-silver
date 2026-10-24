import itertools

N, Q = map(int, input().split())
A = map(int, input().split())
prefix = [0] + [x for x in itertools.accumulate(A)]

for _ in range(Q):
    l, r = map(int, input().split())
    print(prefix[r] - prefix[l])
