from typing import Counter


def minWindow(s: str, t: str):
    lookup = Counter(t)
    mx = float("inf")
    output = ""
    S = len(s)
    start, end, count = 0, 0, len(lookup)

    while end < S:
        # loop for endpointer
        while end < S and count != 0:
            if s[end] in lookup:
                lookup[s[end]] -= 1
                if lookup[s[end]] == 0:
                    count -= 1
            end += 1

        # loop for start pointer
        while start < end and count == 0:
            if end - start < mx:
                mx = end - start
                output = s[start:end]
            if s[start] in lookup:
                lookup[s[start]] += 1
                if lookup[s[start]] > 0:
                    count += 1
            start += 1

    return output


print(minWindow("AB", "A"))
