from rich import print as rprint

N = int(input())
A = sorted(map(int, input().split()), reverse=True)


def divisors(n, s=None):
    if s is None:
        s = n
    res = []

    for x in range(1, s + 1):
        if n % x == 0:
            res.append(x)

    return res


l = [list(reversed(divisors(A[0])))]
for idx, a in enumerate(A):
    if idx == 0:
        continue
    else:
        for d in l[0]:
            if a < d:
                continue
            else:
                if a % d == 0:
                    l.append(d)
                    break


rprint(f"{l=}")
