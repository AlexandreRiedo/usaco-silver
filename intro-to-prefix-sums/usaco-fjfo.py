from math import inf

for _ in range(int(input())):
    N, M = map(int, input().split())
    arr = [int(x) for x in input().split()]

    mod_map = {x: (0 - x) if abs(0 - x) < abs(M - x) else (M - x) for x in range(M)}
    # rprint(f"{mod_map=}")

    ans = inf
    for x in range(M):
        t = [mod_map[(c - x) % M] for c in arr]
        val = sum(abs(c) for c in t)
        ans = min(val, ans)
        # rprint(f"{x=}\t{t=}\t{[abs(c) for c in t]}\t{val=}")
    # rprint(f"{ans=}")
    print(ans)

"""
1
5 9
15 12 18 3 8

1
3 69
1 988244353 998244853
"""


"""
15 12 18 3 8
3  3  0  3 1 -> x = 0 ; s = 10
4  2  1  2 2 -> x = 1 ; s = 11
4  1  2  1 3 -> x = 2 ; s = 11
3  0  -3 0 4 -> x = 3 ; s = 10
2  1  4  1 4 -> x = 4 ; s = 12

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 -> 9
0 1 2 3 4 4 3 2 1 0 1  2  3  4  4  3  2  1  0

0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19  -> 9
0 -1 -2 -3 -4  4  3  2  1  0 -1 -2 -3 -4  4  3  2  1  0 -1  -> dist to mod
4  3  2  1  0  8  7  6  5  4  3  2  1  0  8  7  6  5  4  3  -> mod conv.

0  1  2  3  4  5  6  7  8  9 10 11 12 13 14  -> 5
0 -1 -2  2  1  0 -1 -2  2  1  0 -1 -2  2  1

0  1  2  3  4  5  6  7  8  9 10 11  -> 4
0 -1 -2  1  0 -1 -2  1  0 -1 -2  1

0 1 2 3 4 5 6 7 8 -> 4
0 1 2 1 0 1 2 1 0
"""
