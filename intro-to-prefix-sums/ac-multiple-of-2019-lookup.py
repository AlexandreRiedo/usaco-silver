import sys
from math import comb

S = sys.stdin.readline().strip()

remainders = {x: 0 for x in range(2019)}
remainders[0] = 1
num, power = 0, 1
for digit in reversed(S):
    num = (num + int(digit) * power) % 2019
    power = power * 10 % 2019
    remainders[num] += 1

sys.stdout.write(f"{sum(comb(x, 2) for x in remainders.values())}\n")
