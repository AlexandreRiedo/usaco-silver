import sys

n, x = map(int, sys.stdin.readline().split())
arr = map(int, sys.stdin.readline().split())

# cnt[s] = how many earlier prefix sums equal s (the empty prefix 0 counts once)
cnt = {0: 1}
s = ans = 0
for a in arr:
    s += a
    # a subarray ending here sums to x if some earlier prefix equals s - x
    ans += cnt.get(s - x, 0)
    cnt[s] = cnt.get(s, 0) + 1
sys.stdout.write(f"{ans}\n")
