import sys

n, x = map(int, sys.stdin.readline().split())
arr = map(int, sys.stdin.readline().split())

prefix = [0]
for num in arr:
    prefix.append(num + prefix[-1])

num_freq = {k: 0 for k in prefix}
for num in prefix:
    num_freq[num] += 1
num_freq[0] -= 1

ans = 0
for idx in range(len(prefix) - 1):
    prev, curr = prefix[idx], prefix[idx + 1]
    ans += num_freq.get(x + prev, 0)
    num_freq[curr] -= 1
sys.stdout.write(f"{ans}\n")
