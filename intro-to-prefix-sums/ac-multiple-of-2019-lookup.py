import itertools
import sys
from math import comb

S = sys.stdin.readline().strip()

remainders = {x: 0 for x in range(2019)}
remainders[0] = 1
for s in itertools.accumulate(reversed(S), func=lambda a, b: b + a):
    remainders[int(s) % 2019] += 1

ans = 0
for cnt in remainders.values():
    ans += comb(cnt, 2)
sys.stdout.write(f"{ans}\n")

"""
1817181712114
"""
