import math

n = int(input())
a = map(int, input().split())

val = 0
singles = 0
mod_map = [0] * n
for idx, num in enumerate(a, 1):
    val = (val + num) % n
    if val == 0:
        singles += 1
    mod_map[val] += 1

print(sum(math.comb(x, 2) for x in mod_map) + singles)
