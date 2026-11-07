for _ in range(int(input())):
    n = int(input())
    s = [ord(ch) - ord("a") for ch in input()]

    # counts of each letter on even / odd positions, to the right of the current index
    after_even = [0] * 26
    after_odd = [0] * 26
    for i, c in enumerate(s):
        if i % 2 == 0:
            after_even[c] += 1
        else:
            after_odd[c] += 1

    if n % 2 == 0:
        print(n - max(after_even) - max(after_odd))
        continue

    # odd length: we must delete one character.
    # deleting index i keeps the parity of everything before i
    # and flips the parity of everything after i.
    before_even = [0] * 26
    before_odd = [0] * 26
    best = n
    for i, c in enumerate(s):
        # s[i] gets deleted, so it is neither before nor after
        if i % 2 == 0:
            after_even[c] -= 1
        else:
            after_odd[c] -= 1

        new_even = max(before_even[x] + after_odd[x] for x in range(26))
        new_odd = max(before_odd[x] + after_even[x] for x in range(26))
        best = min(best, n - new_even - new_odd)

        if i % 2 == 0:
            before_even[c] += 1
        else:
            before_odd[c] += 1

    print(best)
