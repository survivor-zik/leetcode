# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
#
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Explanation:
#
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:
#
# Input: strs = [""]
#
# Output: [[""]]
#
# Example 3:
#
# Input: strs = ["a"]
#
# Output: [["a"]]
#
#
#
# Constraints:
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


def group_anagrams(strs: list):
    if len(strs) == 0:
        return []
    text = {}

    for s in strs:
        count = [0] * 26
        for i in s:
            count[ord(i) - ord('a')] += 1

        check = str(count)
        if check in text:
            text[check].append(s)
        else:
            text[check] = [s]

    return list(text.values())

strs = ["eat","tea","tan","ate","nat","bat","poop"]
print(group_anagrams(strs))

# check=[0,1,0]
# check = str(check)
# kk = {
#     check:["eat","tea"]
# }
#
# print(kk[check])