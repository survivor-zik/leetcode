# Given 2 string s and t, return True if t is an anagram of s, return False otherwise.
# characters present in each other are called anagram
# cat , tac

start = ['aa','bab']
target = ['bb','abb']


def valid_anagram(s, t) -> bool:
    if len(s) != len(t):
        return False

    counts = [0] * 26
    for i in range(len(s)):
        counts[ord(s[i]) - ord('a')] += 1
        counts[ord(t[i]) - ord('a')] -= 1

    for n in counts:
        if n !=0:
            return False

    return True


print(valid_anagram(start[1], target[1]))
