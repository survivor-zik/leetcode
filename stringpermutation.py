def check(s1: str, s2: str) -> bool:
    s1_len, s2_len = len(s1), len(s2)
    if s1_len > s2_len:
        return False
    map1 = [0] * 26
    map2 = [0] * 26

    for i in range(s1_len):
        map1[ord(s1[i]) - ord('a')] += 1
        map2[ord(s2[i]) - ord('a')] += 1

    if map1 == map2:
        return True

    for i in range(s2_len - s1_len):
        map2[ord(s2[i]) - ord('a')] -= 1
        map2[ord(s2[i+s1_len]) - ord('a')] += 1
        if map1 == map2:
            return True
    return map2 == map1


print(check("ab", "eidbaooo"))
