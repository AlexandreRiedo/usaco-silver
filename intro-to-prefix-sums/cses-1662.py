import math
from collections import defaultdict

n = int(input())
a = map(int, input().split())

prefix = [0]
mod_map = defaultdict(list[int])
for idx, num in enumerate(a, 1):
    val = (prefix[idx - 1] + num) % n
    prefix.append(val)
    mod_map[val].append(idx)

print(sum(math.comb(len(x), 2) for x in mod_map.values()) + prefix.count(0) - 1)
