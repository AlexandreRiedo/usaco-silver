from collections import defaultdict
from math import inf

for _ in range(int(input())):
    n = int(input())
    s = input()

    cnt_odd = defaultdict(int)
    cnt_even = defaultdict(int)
    for idx, char in enumerate(s):
        if idx % 2 == 0:
            cnt_even[char] += 1
        else:
            cnt_odd[char] += 1

    if n % 2 == 0:
        ans = n - (max(cnt_even.values(), default=0) + max(cnt_odd.values(), default=0))
    else:
        ans = inf
        chars = set(cnt_odd.keys()) | set(cnt_even.keys())
        cnt_odd_iter = defaultdict(int)
        cnt_even_iter = defaultdict(int)

        for idx, swap in enumerate(s):
            max_odd, max_even = 0, 0

            if idx % 2 == 0:
                cnt_even_iter[swap] += 1
            else:
                cnt_odd_iter[swap] += 1

            for char in chars:
                odd = cnt_odd_iter[char] + (cnt_even[char] - cnt_even_iter[char])
                even = cnt_even_iter[char] + (cnt_odd[char] - cnt_odd_iter[char])

                if char == swap:
                    if idx % 2 == 0:
                        even -= 1
                    else:
                        odd -= 1

                max_odd = max(max_odd, odd)
                max_even = max(max_even, even)
                ans = min(ans, n - (max_odd + max_even))
    print(ans)
