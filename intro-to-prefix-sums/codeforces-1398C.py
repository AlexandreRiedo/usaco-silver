import itertools

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input()]
    pre = [0] + list(itertools.accumulate(a))

    ans = 0
    for r in range(n + 1):
        for l in range(r):
            score, size = pre[r] - pre[l], (r - l)
            if score == size:
                ans += 1
    print(ans)
